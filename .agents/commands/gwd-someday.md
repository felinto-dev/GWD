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

Ao adicionar ou adiar item em `someday-maybe.md`, use tabela agrupada por tema/seção com colunas `Item`, `Motivo`, `Próxima revisão`, `Logs`. Não use coluna `Revisar em`. Registre em `Logs` o motivo do adiamento e por quanto tempo foi adiado.

Ao promover item para projeto/próxima ação, atualize `someday-maybe.md`, destino canônico, `projects.md` se necessário, e `horizons.md` se virou compromisso relevante.
