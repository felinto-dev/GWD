---
description: Show a polished GWD mission-control summary of tasks, projects, and horizons.
argument-hint: "[today|week|all]"
skills: gwd
---
Use a skill `gwd` em modo summary.

Argumentos:
$ARGUMENTS

Token-saver:
Antes de ler markdown completo, rode:

```text
.agents/skills/gwd/scripts/gwd-query summary --root . --format json
```

Para UI/UX visual no terminal, use tambem:

```text
.agents/skills/gwd/scripts/gwd-query summary --root . --format md
```

Objetivo: mostrar um painel bonito com principais tarefas, estado dos horizontes, projetos problematicos, gaps e proximo comando recomendado. Capriche em ASCII art/banners. Leia arquivos completos so para editar, resolver warnings, ou quando o usuario pedir detalhe integral.
