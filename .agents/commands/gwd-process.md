---
description: Process GWD inbox items into trusted places.
argument-hint: "[scope or limit]"
skills: gwd
---
Use a skill `gwd` em modo process.

Argumentos:
$ARGUMENTS

Token-saver:
Antes de ler markdown completo, rode:

```text
.agents/skills/gwd/scripts/gwd-query inbox --root . --format json
```

Leia arquivos completos so para editar, resolver warnings, ou quando o usuario pedir detalhe integral.

Regra de confirmacao:
- Sempre pergunte antes de categorizar, mover, marcar ou remover qualquer item do inbox.
- Se a categoria parecer obvia, sugira destino + motivo, mas espere confirmacao do usuario.
- Processe um item por vez, salvo se o usuario pedir triagem em lote.

Ao mover itens confirmados para projetos/proximas acoes/waiting/someday/calendar, atualize os arquivos de destino. Se criou projeto ou alterou area/meta, atualize `projects.md` e possivelmente `horizons.md`.
