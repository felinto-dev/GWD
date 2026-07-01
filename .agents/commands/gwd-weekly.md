---
description: Run the complete GWD weekly review.
argument-hint: "[optional focus]"
skills: gwd
---
Use a skill `gwd` em modo weekly review.

Argumentos:
$ARGUMENTS

Token-saver:
Antes de ler markdown completo, rode:

```text
.agents/skills/gwd/scripts/gwd-query review --root . --type weekly --format json
```

Leia arquivos completos so para editar, resolver warnings, ou quando o usuario pedir detalhe integral.

Ao finalizar, atualize `projects.md` se status/proximas acoes mudaram. Atualize `horizons.md` apenas se areas/projetos mudaram significativamente.
