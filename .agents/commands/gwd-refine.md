---
description: Refine title and description for one existing GWD item without moving it.
argument-hint: "[item id|inbox]"
skills: gwd
---
Use a skill `gwd` em modo refine.

Escopo:
- Refine somente título e descrição, salvo pedido explícito para outro campo.
- Preserve ID, data, status, contexto, revisão, bloqueios, local canônico e ordenação.
- Não processe inbox, mova, apague, priorize ou marque como concluído.
- Para `inbox`, refine uma linha por vez, da mais nova para a mais antiga.

Fluxo:
1. Identifique o item por ID ou use `inbox` como fila de refinamento.
2. Leia o arquivo canônico antes de propor mudanças.
3. Inspecione contexto local relacionado antes de perguntar.
4. Faça uma pergunta por vez, com resposta recomendada e motivo.
5. Mostre título e descrição propostos e peça confirmação antes de editar.
6. Após confirmação, altere só os campos de título/descrição e resuma antigo -> novo.

Argumentos:
$ARGUMENTS
