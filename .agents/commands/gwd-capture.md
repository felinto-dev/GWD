---
description: Quickly capture titled items with optional descriptions into the GWD inbox.
argument-hint: "[item or list]"
skills: gwd
---
Use a skill `gwd` em modo capture.

Regras:
- Capture primeiro; não faça entrevista estilo `/gwd-refine` quando os argumentos já bastam para criar título e descrição.
- Não pergunte outcome, porquê, limites, próxima ação, estado de concluído, prioridade, projeto, contexto ou wording melhorado durante capture.
- Pergunte antes de salvar somente se não houver item capturável ou se os argumentos forem ambíguos demais para criar uma linha.
- Depois de salvar, mostre automaticamente o `ID`, `Added`, `Título`, `Descrição` e arquivo gravado exatamente como ficaram no inbox. Use `-` se a descrição ficar vazia.

Formato do inbox:

```markdown
| ID | Added | Title | Description |
|---|---|---|---|
| in-YYYYMMDD-HHMMSS-001 | YYYY-MM-DD HH:MM | Título | detalhes opcionais preservados |
```

Formato da resposta após salvar:

```markdown
Capture -> inbox

ID: in-YYYYMMDD-HHMMSS-001
Added: YYYY-MM-DD HH:MM
Título: Título
Descrição: detalhes opcionais preservados
Arquivo: `inbox.md`
```

Argumentos:
$ARGUMENTS
