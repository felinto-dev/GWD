---
description: Refine title and description for one existing GWD item without moving it.
argument-hint: "[item id|inbox]"
skills: gwd
---
Use a skill `gwd` em modo refine.

Escopo:
- Refine somente título e descrição, salvo pedido explícito para outro campo.
- Preserve ID, data, status, contexto, revisão, bloqueios, local canônico e ordenação.
- Não processe inbox, mova, priorize ou marque como concluído.
- Se o usuário não quiser mais o item, permita excluí-lo neste fluxo somente após confirmação explícita.
- Para `inbox`, refine uma linha por vez, da mais nova para a mais antiga.
- Sempre mostre o título e a descrição brutos e completos. Nunca resuma, abrevie, trunque ou substitua partes por reticências.

Fluxo:
1. Identifique o item por ID ou use `inbox` como fila de refinamento.
2. Leia o arquivo canônico antes de propor mudanças.
3. Inspecione contexto local relacionado antes de perguntar.
4. Em toda apresentação, pergunta, proposta, confirmação, resultado e próximo item, mostre título e descrição brutos e completos.
5. Faça uma pergunta por vez, com resposta recomendada e motivo.
6. Mostre título e descrição propostos completos e peça confirmação antes de editar.
7. Após confirmação, altere só os campos de título/descrição e mostre integralmente os valores antigos e novos.
8. Se o usuário pedir exclusão, mostre ID, arquivo, título e descrição completos e peça confirmação. Após confirmação, remova somente o item canônico, registre a exclusão em `daily/YYYY-MM-DD.md` e apresente imediatamente o próximo item da fila.

Argumentos:
$ARGUMENTS
