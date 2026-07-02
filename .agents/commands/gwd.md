---
description: GWD router for capture, planning, review, next actions, and completions.
argument-hint: "[request]"
skills: gwd
---
Use a skill `gwd` em modo router.

Argumentos:
$ARGUMENTS

Token-saver:
Antes de ler markdown completo, rode:

```text
.agents/skills/gwd/scripts/gwd-query status --root . --format json
```

Leia arquivos completos so para editar, resolver warnings, ou quando o usuario pedir detalhe integral.

Roteamento: se o pedido for marcar/concluir/registrar uma próxima ação como feita (ex.: "terminei X", "marcar X como concluída"), use modo done mesmo sem `/gwd-done`.
