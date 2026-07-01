---
description: Manage GWD someday/maybe items.
argument-hint: "[idea or scope]"
skills: gwd
---
Use a skill `gwd` em modo someday.

Argumentos:
$ARGUMENTS

Token-saver:
Antes de ler markdown completo, rode:

```text
.agents/skills/gwd/scripts/gwd-query someday --root . --format json
```

Leia arquivos completos so para editar, resolver warnings, ou quando o usuario pedir detalhe integral.

Ao promover item para projeto/proxima acao, atualize `someday-maybe.md`, destino canonico, `projects.md` se necessario, e `horizons.md` se virou compromisso relevante.
