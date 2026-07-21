---
description: Gerencie os contextos de execução do GWD e seus sinais de identificação.
argument-hint: "[listar|revisar|adicionar|editar|renomear|mesclar|arquivar] [contexto]"
skills: gwd
---
Use a skill `gwd` em modo contexts.

Argumentos:
$ARGUMENTS

Antes de ler Markdown completo, rode:

```text
.agents/skills/gwd/scripts/gwd-query contexts --root . --format json
```

Sem argumentos, mostre somente os contextos cadastrados pelo usuário, seus sinais e referências a contextos arquivados. Uma lista vazia é válida.

Não trate etiquetas genéricas encontradas nas próximas ações, como `@phone` ou `@computer`, como contextos ausentes ou erros. Elas são restrições de execução e não precisam existir em `contexts.md`.

Para renomear, mesclar ou arquivar, leia os arquivos afetados, mostre o impacto e peça confirmação antes de editar. Preserve IDs, atualize referências canônicas e registre a mudança em `daily/YYYY-MM-DD.md`.
