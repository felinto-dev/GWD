#!/usr/bin/env python3
"""Read-only query helper for GWD markdown files.

The goal is to return compact, deterministic summaries so the agent does not
need to read large markdown files unless it is about to edit or inspect detail.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, date
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

BASE_FILES = [
    "inbox.md",
    "next-actions.md",
    "projects.md",
    "areas.md",
    "goals.md",
    "vision.md",
    "purpose.md",
    "horizons.md",
    "waiting-for.md",
    "someday-maybe.md",
    "calendar.md",
]

HORIZON_FILES = {
    "H0": "next-actions.md",
    "H1": "projects.md",
    "H2": "areas.md",
    "H3": "goals.md",
    "H4": "vision.md",
    "H5": "purpose.md",
}

TASK_RE = re.compile(r"^\s*-\s*\[(?P<status>[^\]]*)\]\s*(?P<rest>.+?)\s*$")
INBOX_RE = re.compile(
    r"^\s*-\s*\[(?P<status>[^\]]*)\]\s*"
    r"(?P<stamp>\d{4}-\d{2}-\d{2}(?:\s+\d{2}:\d{2})?)\s*\|\s*(?P<text>.+?)\s*$"
)
PRIORITY_RE = re.compile(r"\b(P[0-2])\b")
CONTEXT_RE = re.compile(r"(^|\s)(@[-A-Za-z0-9_./]+)\b")
MINUTES_RE = re.compile(r"\((?P<num>\d+)\s*(?:m|min|minutes?)\)", re.I)
DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")


def now_iso() -> str:
    return datetime.now().replace(microsecond=0).isoformat()


@dataclass
class Ctx:
    root: Path
    files_read: List[str]
    warnings: List[str]

    def rel(self, path: Path) -> str:
        try:
            return str(path.relative_to(self.root))
        except ValueError:
            return str(path)

    def read_text(self, rel_path: str) -> str:
        path = self.root / rel_path
        if not path.exists():
            self.warnings.append(f"missing file: {rel_path}")
            return ""
        if path.is_dir():
            self.warnings.append(f"expected file, got directory: {rel_path}")
            return ""
        self.files_read.append(rel_path)
        try:
            return path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            self.warnings.append(f"utf-8 decode failed: {rel_path}")
            return path.read_text(errors="replace")

    def file_exists(self, rel_path: str) -> bool:
        return (self.root / rel_path).exists()


def base_result(mode: str, ctx: Ctx) -> Dict[str, Any]:
    return {
        "mode": mode,
        "root": str(ctx.root),
        "generated_at": now_iso(),
        "files_read": ctx.files_read,
        "warnings": ctx.warnings,
    }


def parse_markdown_table(text: str) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not (line.startswith("|") and line.endswith("|")):
            i += 1
            continue
        if i + 1 >= len(lines):
            i += 1
            continue
        sep = lines[i + 1].strip()
        if not (sep.startswith("|") and set(sep.replace("|", "").replace("-", "").replace(":", "").strip()) == set()):
            i += 1
            continue
        headers = [c.strip() for c in line.strip("|").split("|")]
        i += 2
        while i < len(lines):
            row_line = lines[i].strip()
            if not (row_line.startswith("|") and row_line.endswith("|")):
                break
            cells = [c.strip() for c in row_line.strip("|").split("|")]
            row = {headers[j]: cells[j] if j < len(cells) else "" for j in range(len(headers))}
            row["_line"] = str(i + 1)
            rows.append(row)
            i += 1
    return rows


def normalize_key(row: Dict[str, str], *names: str) -> str:
    lower = {k.lower().strip(): v for k, v in row.items()}
    for name in names:
        key = name.lower().strip()
        if key in lower:
            return lower[key]
    return ""


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "item"


def parse_minutes(text: str) -> Optional[int]:
    m = MINUTES_RE.search(text)
    if not m:
        return None
    try:
        return int(m.group("num"))
    except ValueError:
        return None


def parse_task_line(line: str, line_no: int, section_context: Optional[str] = None, prefix: str = "task") -> Optional[Dict[str, Any]]:
    m = TASK_RE.match(line)
    if not m:
        return None
    status = m.group("status").strip()
    rest = m.group("rest").strip()
    link = ""
    if " -> " in rest:
        rest, link = rest.rsplit(" -> ", 1)
        rest = rest.strip()
        link = link.strip()
    priority = None
    pm = PRIORITY_RE.search(rest)
    if pm:
        priority = pm.group(1)
        rest = (rest[: pm.start()] + rest[pm.end() :]).strip()
    context = section_context
    cm = CONTEXT_RE.search(rest)
    if cm:
        context = cm.group(2)
        rest = (rest[: cm.start()] + " " + rest[cm.end() :]).strip()
    minutes = parse_minutes(rest)
    if minutes is not None:
        rest = MINUTES_RE.sub("", rest).strip()
    text = re.sub(r"\s+", " ", rest).strip()
    return {
        "id": f"{prefix}:{line_no}",
        "line": line_no,
        "status": status or " ",
        "done": status.lower() == "x",
        "priority": priority,
        "context": context,
        "text": text,
        "minutes": minutes,
        "link": link,
        "raw": line.strip(),
    }


def parse_bullets(text: str, prefix: str = "item") -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        task = parse_task_line(line, line_no, prefix=prefix)
        if task:
            items.append(task)
    return items


def parse_inbox(ctx: Ctx) -> List[Dict[str, Any]]:
    text = ctx.read_text("inbox.md")
    items: List[Dict[str, Any]] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        m = INBOX_RE.match(line)
        if m:
            status = m.group("status").strip()
            items.append(
                {
                    "id": f"inbox:{line_no}",
                    "line": line_no,
                    "status": status or " ",
                    "done": status.lower() == "x",
                    "stamp": m.group("stamp"),
                    "text": m.group("text").strip(),
                    "raw": line.strip(),
                }
            )
            continue
        task = parse_task_line(line, line_no, prefix="inbox")
        if task:
            task["stamp"] = None
            items.append(task)
    return items


def parse_next_actions(ctx: Ctx) -> List[Dict[str, Any]]:
    text = ctx.read_text("next-actions.md")
    items: List[Dict[str, Any]] = []
    section_context: Optional[str] = None
    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("## "):
            title = stripped[3:].strip()
            section_context = title if title.startswith("@") else None
            continue
        task = parse_task_line(line, line_no, section_context=section_context, prefix="na")
        if task:
            items.append(task)
    return items


def parse_projects(ctx: Ctx, stale_days: int = 14) -> List[Dict[str, Any]]:
    text = ctx.read_text("projects.md")
    rows = parse_markdown_table(text)
    projects: List[Dict[str, Any]] = []
    today = date.today()
    for row in rows:
        name = normalize_key(row, "Project", "Projeto", "Name", "Nome")
        if not name or name.lower() == "example":
            continue
        area = normalize_key(row, "Area")
        goal = normalize_key(row, "Goal", "Meta")
        status = normalize_key(row, "Status") or "active"
        next_action = normalize_key(row, "Next Action", "Proxima Acao")
        updated = normalize_key(row, "Updated", "Atualizado")
        slug = slugify(name)
        flags: List[str] = []
        if status.lower() in {"paused", "waiting", "archived"}:
            flags.append(status.lower())
        if not next_action or next_action.lower() in {"none", "n/a", "-"}:
            flags.append("missing_next")
        days_old: Optional[int] = None
        dm = DATE_RE.search(updated or "")
        if dm:
            try:
                days_old = (today - date.fromisoformat(dm.group(0))).days
                if days_old > stale_days and status.lower() == "active":
                    flags.append("stale")
            except ValueError:
                pass
        projects.append(
            {
                "id": f"proj:{slug}",
                "name": name,
                "area": area,
                "goal": goal,
                "status": status,
                "next_action": next_action or None,
                "updated": updated or None,
                "days_old": days_old,
                "flags": sorted(set(flags)),
                "line": int(row.get("_line", "0") or 0),
            }
        )
    # Include project folders not listed in the dashboard.
    active_dir = ctx.root / "projects" / "active"
    if active_dir.exists() and active_dir.is_dir():
        for proj_dir in sorted(p for p in active_dir.iterdir() if p.is_dir()):
            slug = proj_dir.name
            if any(p["id"] == f"proj:{slug}" for p in projects):
                continue
            info = proj_dir / "info.md"
            tasks = proj_dir / "tasks.md"
            next_count = 0
            if tasks.exists():
                ctx.files_read.append(ctx.rel(tasks))
                for task in parse_bullets(tasks.read_text(encoding="utf-8", errors="replace"), prefix="na"):
                    if not task["done"]:
                        next_count += 1
            flags = [] if next_count else ["missing_next"]
            projects.append(
                {
                    "id": f"proj:{slug}",
                    "name": slug.replace("-", " ").title(),
                    "area": "",
                    "goal": "",
                    "status": "active",
                    "next_action": None,
                    "updated": None,
                    "days_old": None,
                    "flags": flags,
                    "line": None,
                    "source": ctx.rel(info) if info.exists() else ctx.rel(proj_dir),
                }
            )
    return projects


def parse_waiting(ctx: Ctx) -> List[Dict[str, Any]]:
    text = ctx.read_text("waiting-for.md")
    rows = parse_markdown_table(text)
    items: List[Dict[str, Any]] = []
    today = date.today()
    for row in rows:
        item = normalize_key(row, "Item")
        if not item or item.lower() == "item":
            continue
        follow = normalize_key(row, "Follow-up", "Follow up", "Followup")
        status = normalize_key(row, "Status") or "open"
        due = False
        dm = DATE_RE.search(follow or "")
        if dm:
            try:
                due = date.fromisoformat(dm.group(0)) <= today
            except ValueError:
                due = False
        items.append(
            {
                "id": f"wait:{row.get('_line')}",
                "line": int(row.get("_line", "0") or 0),
                "date": normalize_key(row, "Date"),
                "item": item,
                "person": normalize_key(row, "Person/Source", "Person", "Source"),
                "follow_up": follow,
                "project_area": normalize_key(row, "Project/Area", "Project", "Area"),
                "status": status,
                "due": due,
            }
        )
    return items


def parse_simple_table_count(ctx: Ctx, rel_path: str) -> int:
    text = ctx.read_text(rel_path)
    rows = parse_markdown_table(text)
    return len([r for r in rows if any(v.strip() for k, v in r.items() if not k.startswith("_"))])


def file_signal(ctx: Ctx, rel_path: str) -> Dict[str, Any]:
    path = ctx.root / rel_path
    if not path.exists():
        return {"file": rel_path, "exists": False, "status": "missing", "bytes": 0}
    if path.is_dir():
        return {"file": rel_path, "exists": True, "status": "directory", "bytes": 0}
    text = ctx.read_text(rel_path)
    content = [ln.strip() for ln in text.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    if not content:
        status = "empty"
    elif len(" ".join(content)) < 80:
        status = "fuzzy"
    else:
        status = "clear"
    return {"file": rel_path, "exists": True, "status": status, "bytes": len(text.encode("utf-8"))}


def query_status(ctx: Ctx, args: argparse.Namespace) -> Dict[str, Any]:
    result = base_result("status", ctx)
    files = []
    for rel in BASE_FILES:
        files.append(file_signal(ctx, rel))
    inbox = parse_inbox(ctx)
    next_actions = parse_next_actions(ctx)
    projects = parse_projects(ctx, args.stale_days)
    waiting = parse_waiting(ctx)
    result.update(
        {
            "files": files,
            "counts": {
                "inbox_open": sum(1 for i in inbox if not i.get("done")),
                "next_open": sum(1 for i in next_actions if not i.get("done")),
                "projects_active": sum(1 for p in projects if p.get("status", "").lower() == "active"),
                "projects_missing_next": sum(1 for p in projects if "missing_next" in p.get("flags", [])),
                "waiting_open": sum(1 for w in waiting if w.get("status", "").lower() == "open"),
                "waiting_due": sum(1 for w in waiting if w.get("due")),
            },
            "next_command": "/gwd-process" if any(not i.get("done") for i in inbox) else "/gwd-next",
        }
    )
    return result


def query_inbox(ctx: Ctx, args: argparse.Namespace) -> Dict[str, Any]:
    items = parse_inbox(ctx)
    open_items = [i for i in items if not i.get("done")]
    result = base_result("inbox", ctx)
    result.update(
        {
            "counts": {"total": len(items), "open": len(open_items), "done": len(items) - len(open_items)},
            "items": open_items[: args.limit],
            "next_command": "/gwd-process" if open_items else "/gwd-next",
        }
    )
    return result


def query_next(ctx: Ctx, args: argparse.Namespace) -> Dict[str, Any]:
    items = [i for i in parse_next_actions(ctx) if not i.get("done")]
    filtered = []
    for item in items:
        if args.context and item.get("context") != args.context:
            continue
        if args.priority and item.get("priority") != args.priority:
            continue
        if args.time is not None and item.get("minutes") is not None and item["minutes"] > args.time:
            continue
        if args.energy == "low" and item.get("context") == "@deep":
            continue
        filtered.append(item)
    def score(item: Dict[str, Any]) -> Tuple[int, int, int]:
        priority_score = {"P0": 0, "P1": 1, "P2": 2}.get(item.get("priority"), 3)
        time_score = item.get("minutes") if item.get("minutes") is not None else 999
        low_bonus = 0 if args.energy == "low" and item.get("context") == "@low-energy" else 1
        return (priority_score, low_bonus, time_score)
    filtered.sort(key=score)
    limited = filtered[: args.limit]
    result = base_result("next", ctx)
    result.update(
        {
            "filters": {"context": args.context, "time_max": args.time, "energy": args.energy, "priority": args.priority},
            "counts": {"open": len(items), "matched": len(filtered)},
            "recommended_id": limited[0]["id"] if limited else None,
            "items": limited,
            "next_command": f"/gwd-start {limited[0]['id']}" if limited else "/gwd-capture",
        }
    )
    return result


def query_projects(ctx: Ctx, args: argparse.Namespace) -> Dict[str, Any]:
    projects = parse_projects(ctx, args.stale_days)
    if args.missing_next:
        projects = [p for p in projects if "missing_next" in p.get("flags", [])]
    result = base_result("projects", ctx)
    result.update(
        {
            "counts": {
                "total": len(projects),
                "active": sum(1 for p in projects if p.get("status", "").lower() == "active"),
                "paused": sum(1 for p in projects if p.get("status", "").lower() == "paused"),
                "missing_next": sum(1 for p in projects if "missing_next" in p.get("flags", [])),
                "stale": sum(1 for p in projects if "stale" in p.get("flags", [])),
            },
            "projects": projects[: args.limit],
            "next_command": "/gwd-weekly" if projects else "/gwd-project",
        }
    )
    return result


def horizon_status(ctx: Ctx) -> Dict[str, str]:
    status: Dict[str, str] = {}
    next_open = len([i for i in parse_next_actions(ctx) if not i.get("done")])
    projects = parse_projects(ctx)
    for h, rel in HORIZON_FILES.items():
        signal = file_signal(ctx, rel)
        status[h] = signal["status"]
    if next_open > 0:
        status["H0"] = "clear"
    if projects:
        missing = sum(1 for p in projects if "missing_next" in p.get("flags", []))
        status["H1"] = "current" if missing == 0 else "stale"
    goals_count = parse_simple_table_count(ctx, "goals.md")
    if goals_count > 7:
        status["H3"] = "overloaded"
    return status


def query_horizons(ctx: Ctx, args: argparse.Namespace) -> Dict[str, Any]:
    status = horizon_status(ctx)
    projects = parse_projects(ctx, args.stale_days)
    inbox = parse_inbox(ctx)
    next_actions = parse_next_actions(ctx)
    waiting = parse_waiting(ctx)
    gaps: List[str] = []
    for h, rel in HORIZON_FILES.items():
        if status.get(h) in {"missing", "empty", "fuzzy"}:
            gaps.append(f"{h} {rel} is {status[h]}")
    missing_next = sum(1 for p in projects if "missing_next" in p.get("flags", []))
    if missing_next:
        gaps.append(f"{missing_next} active projects lack next action")
    counts = {
        "inbox_open": sum(1 for i in inbox if not i.get("done")),
        "next_open": sum(1 for i in next_actions if not i.get("done")),
        "projects_active": sum(1 for p in projects if p.get("status", "").lower() == "active"),
        "projects_missing_next": missing_next,
        "waiting_due": sum(1 for w in waiting if w.get("due")),
    }
    result = base_result("horizons", ctx)
    result.update(
        {
            "status": status,
            "counts": counts,
            "gaps": gaps,
            "next_command": "/gwd-weekly" if missing_next else ("/gwd-vision" if status.get("H4") in {"missing", "empty", "fuzzy"} else "/gwd-next"),
        }
    )
    return result


def query_review(ctx: Ctx, args: argparse.Namespace) -> Dict[str, Any]:
    review_type = args.type or "weekly"
    inbox = parse_inbox(ctx)
    next_actions = parse_next_actions(ctx)
    projects = parse_projects(ctx, args.stale_days)
    waiting = parse_waiting(ctx)
    hstatus = horizon_status(ctx)
    missing_next = [p for p in projects if "missing_next" in p.get("flags", [])]
    result = base_result("review", ctx)
    result.update(
        {
            "type": review_type,
            "pass": len([i for i in inbox if not i.get("done")]) == 0 and len(missing_next) == 0,
            "inbox_open": sum(1 for i in inbox if not i.get("done")),
            "next_open": sum(1 for i in next_actions if not i.get("done")),
            "projects_active": sum(1 for p in projects if p.get("status", "").lower() == "active"),
            "projects_missing_next": len(missing_next),
            "waiting_open": sum(1 for w in waiting if w.get("status", "").lower() == "open"),
            "waiting_followups_due": sum(1 for w in waiting if w.get("due")),
            "horizons": hstatus,
        }
    )
    if review_type == "daily":
        result["next_command"] = "/gwd-review daily"
    elif review_type == "monthly":
        result["next_command"] = "/gwd-align all"
    elif review_type == "quarterly":
        result["next_command"] = "/gwd-horizons"
    else:
        result["next_command"] = "/gwd-process" if result["inbox_open"] else "/gwd-next"
    return result


def query_waiting(ctx: Ctx, args: argparse.Namespace) -> Dict[str, Any]:
    items = parse_waiting(ctx)
    open_items = [w for w in items if w.get("status", "").lower() == "open"]
    if args.due:
        open_items = [w for w in open_items if w.get("due")]
    result = base_result("waiting", ctx)
    result.update(
        {
            "counts": {"total": len(items), "open": len(open_items), "due": sum(1 for w in items if w.get("due"))},
            "items": open_items[: args.limit],
            "next_command": "/gwd-waiting",
        }
    )
    return result


def query_someday(ctx: Ctx, args: argparse.Namespace) -> Dict[str, Any]:
    text = ctx.read_text("someday-maybe.md")
    items = [i for i in parse_bullets(text, prefix="sm") if not i.get("done")]
    result = base_result("someday", ctx)
    result.update(
        {
            "counts": {"open": len(items)},
            "items": items[: args.limit],
            "next_command": "/gwd-someday",
        }
    )
    return result


def words(value: str) -> List[str]:
    return [w for w in re.findall(r"[A-Za-z0-9]{3,}", value.lower()) if w not in {"the", "and", "para", "com", "uma", "por", "que"}]


def best_line_match(ctx: Ctx, rel_path: str, query: str) -> Optional[Dict[str, Any]]:
    text = ctx.read_text(rel_path)
    qs = set(words(query))
    if not qs:
        return None
    best: Optional[Tuple[int, int, str]] = None
    for line_no, line in enumerate(text.splitlines(), start=1):
        ls = set(words(line))
        score = len(qs & ls)
        if score and (best is None or score > best[0]):
            best = (score, line_no, line.strip())
    if not best:
        return None
    return {"file": rel_path, "line": best[1], "text": best[2], "score": best[0]}


def query_align(ctx: Ctx, args: argparse.Namespace) -> Dict[str, Any]:
    item = args.item or " ".join(args.extra or [])
    result = base_result("align", ctx)
    if not item.strip():
        result.update({"status": "unknown", "warnings": ctx.warnings + ["missing --item"], "next_command": "/gwd-align <item>"})
        return result
    matches = {
        "H0": best_line_match(ctx, "next-actions.md", item),
        "H1": best_line_match(ctx, "projects.md", item),
        "H2": best_line_match(ctx, "areas.md", item),
        "H3": best_line_match(ctx, "goals.md", item),
        "H4": best_line_match(ctx, "vision.md", item),
        "H5": best_line_match(ctx, "purpose.md", item),
    }
    found = {k: v for k, v in matches.items() if v}
    if len(found) >= 4:
        status = "aligned"
    elif len(found) >= 2:
        status = "weak alignment"
    else:
        status = "unknown"
    result.update(
        {
            "item": item,
            "status": status,
            "chain": {k: (v["text"] if v else None) for k, v in matches.items()},
            "evidence": list(found.values()),
            "risks": [] if status == "aligned" else ["higher-horizon link is missing or unclear"],
            "recommendation": "keep" if status == "aligned" else "clarify before activating",
            "next_command": "/gwd-horizons" if status != "aligned" else "/gwd-next",
        }
    )
    return result


def output_json(result: Dict[str, Any]) -> None:
    print(json.dumps(result, ensure_ascii=False, indent=2))


def output_ndjson(result: Dict[str, Any]) -> None:
    collection = None
    for key in ("items", "projects"):
        if isinstance(result.get(key), list):
            collection = result[key]
            break
    if collection is None:
        collection = [result]
    for item in collection:
        print(json.dumps(item, ensure_ascii=False))


def output_md(result: Dict[str, Any]) -> None:
    if result.get("mode") == "horizons":
        print("# Horizons Map")
        print()
        print(f"Generated: {result.get('generated_at')}")
        print()
        print("## Snapshot")
        print()
        for h in ("H5", "H4", "H3", "H2", "H1", "H0"):
            print(f"{h} : {result.get('status', {}).get(h, 'unknown')}")
        if result.get("counts"):
            print()
            print("## Counts")
            print()
            for k, v in result["counts"].items():
                print(f"- {k}: {v}")
        if result.get("gaps"):
            print()
            print("## Gaps")
            print()
            for gap in result["gaps"]:
                print(f"- {gap}")
        print()
        print("## Next")
        print()
        print(f"- {result.get('next_command')}")
        if result.get("warnings"):
            print()
            print("## Warnings")
            print()
            for warning in result["warnings"]:
                print(f"- {warning}")
        return

    print(f"{result.get('mode', 'gwd').title()} -> summary")
    if "counts" in result:
        print("\nCounts:")
        for k, v in result["counts"].items():
            print(f"- {k}: {v}")
    if "status" in result and isinstance(result["status"], dict):
        print("\nStatus:")
        for k, v in result["status"].items():
            print(f"- {k}: {v}")
    items = result.get("items") or result.get("projects") or []
    if items:
        print("\nItems:")
        for item in items[:10]:
            label = item.get("text") or item.get("name") or item.get("item") or item.get("raw")
            print(f"- {item.get('id', '')}: {label}")
    if result.get("gaps"):
        print("\nGaps:")
        for gap in result["gaps"]:
            print(f"- {gap}")
    if result.get("next_command"):
        print(f"\nNext: {result['next_command']}")
    if result.get("warnings"):
        print("\nWarnings:")
        for warning in result["warnings"]:
            print(f"- {warning}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Query GWD markdown files without reading them into the agent context.")
    parser.add_argument("mode", choices=["status", "inbox", "next", "projects", "horizons", "review", "align", "waiting", "someday"])
    parser.add_argument("extra", nargs="*", help="extra words for align/item queries")
    parser.add_argument("--root", default=".", help="GWD workspace root")
    parser.add_argument("--format", choices=["json", "md", "ndjson"], default="json")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--context")
    parser.add_argument("--time", type=int, help="max minutes")
    parser.add_argument("--energy", choices=["low", "medium", "high"])
    parser.add_argument("--priority", choices=["P0", "P1", "P2"])
    parser.add_argument("--stale-days", type=int, default=14)
    parser.add_argument("--type", choices=["daily", "weekly", "monthly", "quarterly"], default="weekly")
    parser.add_argument("--item")
    parser.add_argument("--missing-next", action="store_true")
    parser.add_argument("--due", action="store_true")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    ctx = Ctx(root=Path(args.root).resolve(), files_read=[], warnings=[])
    handlers = {
        "status": query_status,
        "inbox": query_inbox,
        "next": query_next,
        "projects": query_projects,
        "horizons": query_horizons,
        "review": query_review,
        "align": query_align,
        "waiting": query_waiting,
        "someday": query_someday,
    }
    result = handlers[args.mode](ctx, args)
    # Ensure mutations to warnings/files_read after base_result are visible.
    result["files_read"] = list(dict.fromkeys(ctx.files_read))
    result["warnings"] = list(dict.fromkeys(ctx.warnings))
    if args.format == "json":
        output_json(result)
    elif args.format == "ndjson":
        output_ndjson(result)
    else:
        output_md(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
