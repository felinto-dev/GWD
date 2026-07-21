---
description: Choose the best GWD next action available now.
argument-hint: "[restrições ou preferências atuais]"
skills: gwd
---
Use a skill `gwd` em modo next.

Argumentos:
$ARGUMENTS

Antes da entrevista, colete sinais transitórios e consulte contextos e ações:

```text
.agents/skills/gwd/scripts/gwd-context
.agents/skills/gwd/scripts/gwd-query contexts --root . --format json
.agents/skills/gwd/scripts/gwd-query next --root . --format json
```

Mostre o contexto inferido, as evidências e a confiança antes de recomendar. Dê oportunidade para correção. Faça somente perguntas adaptativas cuja resposta possa mudar a escolha.

Leia arquivos completos so para editar, resolver warnings, ou quando o usuario pedir detalhe integral.

Selecionar uma acao nao muda arquivos. So atualize `daily/YYYY-MM-DD.md` se a acao for incorporada ao plano do dia.
