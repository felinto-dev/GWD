import importlib.util
from importlib.machinery import SourceFileLoader
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import URLError


SKILL_ROOT = Path(__file__).resolve().parents[1]
QUERY_PATH = SKILL_ROOT / "scripts" / "gwd-query.py"
CONTEXT_PATH = SKILL_ROOT / "scripts" / "gwd-context"


def load_module(name, path):
    loader = SourceFileLoader(name, str(path))
    spec = importlib.util.spec_from_loader(name, loader)
    assert spec
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


class QueryTests(unittest.TestCase):
    def run_query(self, root, *args):
        output = subprocess.check_output(
            ["python3", str(QUERY_PATH), *args, "--root", str(root), "--format", "json"],
            text=True,
        )
        return json.loads(output)

    def test_context_inventory_and_archived_references(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "contexts.md").write_text(
                "| Contexto | Definição | Estado |\n"
                "|---|---|---|\n"
                "| @computer | Computador | ativo |\n"
                "| @old | Antigo | arquivado |\n",
                encoding="utf-8",
            )
            (root / "next-actions.md").write_text(
                "| ID | Added | Title | Description | Context |\n"
                "|---|---|---|---|---|\n"
                "| na-1 | 2026-07-15 10:00 | A | - | @computer |\n"
                "| na-2 | 2026-07-15 09:00 | B | - | @old |\n"
                "| na-3 | 2026-07-15 08:00 | C | - | @unknown |\n",
                encoding="utf-8",
            )
            result = self.run_query(root, "contexts")
            self.assertEqual(result["counts"]["active"], 1)
            self.assertNotIn("unknown_references", result)
            self.assertEqual(result["archived_references"][0]["context"], "@old")

    def test_empty_context_list_accepts_generic_action_labels(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "contexts.md").write_text(
                "| Contexto | Definição | Estado |\n|---|---|---|\n",
                encoding="utf-8",
            )
            (root / "next-actions.md").write_text(
                "| ID | Added | Title | Description | Context |\n"
                "|---|---|---|---|---|\n"
                "| na-1 | 2026-07-15 10:00 | Ligar | - | @phone |\n",
                encoding="utf-8",
            )
            result = self.run_query(root, "contexts")
            self.assertEqual(result["counts"]["total"], 0)
            self.assertEqual(result["counts"]["archived_references"], 0)
            self.assertNotIn("unknown_references", result)
            self.assertEqual(result["next_command"], "/gwd-next")

    def test_optional_time_and_energy_filters(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "next-actions.md").write_text(
                "| ID | Added | Title | Description | Context | Time | Energy |\n"
                "|---|---|---|---|---|---|---|\n"
                "| na-1 | 2026-07-15 10:00 | Deep | - | @computer | 60 | high |\n"
                "| na-2 | 2026-07-15 09:00 | Quick | - | @computer | 15 | low |\n",
                encoding="utf-8",
            )
            result = self.run_query(root, "next", "--time", "30", "--energy", "low")
            self.assertEqual([item["id"] for item in result["items"]], ["na-2"])


class ContextSignalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module("gwd_context", CONTEXT_PATH)

    def test_offline_keeps_hostname_and_skips_network(self):
        result = self.module.collect(include_network=False)
        self.assertIn("hostname", result)
        self.assertEqual(result["network"]["status"], "skipped")
        self.assertFalse(result["privacy"]["ip_included"])

    def test_network_failure_degrades(self):
        with patch.object(self.module, "urlopen", side_effect=URLError("offline")):
            result = self.module.fetch_network(timeout=0.01)
        self.assertEqual(result["status"], "unavailable")

    def test_security_flags_are_exposed_without_ip(self):
        payload = json.dumps(
            {
                "success": True,
                "ip": "203.0.113.10",
                "city": "São Paulo",
                "country": "Brazil",
                "security": {"vpn": True, "proxy": False, "tor": False, "relay": None},
                "connection": {"org": "Example", "isp": "Example ISP"},
            }
        ).encode()

        class Response:
            def __enter__(self):
                return self

            def __exit__(self, *args):
                return False

            def read(self, _limit):
                return payload

        with patch.object(self.module, "urlopen", return_value=Response()):
            result = self.module.fetch_network()
        self.assertTrue(result["security"]["vpn"])
        self.assertNotIn("ip", result)


if __name__ == "__main__":
    unittest.main()
