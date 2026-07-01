---
description: Initialize GWD, inspect local references, and run the first sweep.
argument-hint: "[areas, contexts, preferences, reference files]"
skills: gwd
---
Use a skill `gwd` em modo setup.

Argumentos:
$ARGUMENTS

Inclua `gwd-memory.md` entre os arquivos base. Ao finalizar o primeiro sweep, atualize `horizons.md` com:

```text
.agents/skills/gwd/scripts/gwd-query horizons --root . --format md
```
