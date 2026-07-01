---
description: Run a GWD daily, weekly, monthly, or quarterly review.
argument-hint: "[daily|weekly|monthly|quarterly]"
skills: gwd
---
Use a skill `gwd` em modo review.

Argumentos:
$ARGUMENTS

Token-saver:
Antes de ler markdown completo, rode:

```text
.agents/skills/gwd/scripts/gwd-query review --root . --type $ARGUMENTS --format json
```

Leia arquivos completos so para editar, resolver warnings, ou quando o usuario pedir detalhe integral.

No review mensal, consulte `gwd-memory.md` quando existir e verifique as condicoes `Esquecer em` antes de decidir o proximo mes. Ao finalizar review mensal ou trimestral, atualize `horizons.md`. Ao finalizar review semanal, atualize `projects.md` se status/proximas acoes mudaram.
