# GWD Examples

## 1. First setup with automatic sweep

User:

```text
/gwd-setup Quero organizar trabalho, saude, familia e projetos pessoais.
```

Assistant:

```markdown
Setup -> GWD

Vou criar a base na pasta principal e iniciar o primeiro sweep automaticamente.

References checked:
- nenhum arquivo de tarefas/plano encontrado ainda

Recommended areas:
- trabalho -> aparece como responsabilidade principal
- saude -> energia sustenta execucao
- familia -> compromissos recorrentes precisam de visibilidade
- projetos pessoais -> separar ambicoes de obrigacoes

Questions:
1. Essas areas representam bem sua vida hoje?
   Recommended: sim, com "financas" e "casa" adicionadas -> costumam gerar muitos loops ocultos.
2. Qual area esta mais desorganizada agora?
   Recommended: trabalho -> geralmente concentra prazos e dependencias.
3. Quer importar tarefas de algum arquivo local antes de criar os primeiros projetos?
   Recommended: sim, se houver CSV/TXT/MD exportado -> reduz perguntas e evita recapturar tudo manualmente.

Next branch: areas
```

## 2. Capture

User:

```text
/gwd-capture renovar passaporte; responder Ana; ideia app receitas; pagar IPVA
```

Assistant:

```markdown
Capture -> 4 item(s).

Added:
- renovar passaporte
- responder Ana
- ideia app receitas
- pagar IPVA

Next -> `/gwd-process`.
```

## 3. Clarify

User:

```text
/gwd-clarify renovar passaporte
```

Assistant:

```markdown
Clarify -> renovar passaporte

Decision: project
Outcome: passaporte renovado
Next action: @computer verificar documentos exigidos no site da PF (20m)
Destination: `projects/active/renovar-passaporte/`

Processar proximo item?
```

## 4. Sweep with a local export

User:

```text
/gwd-sweep use meu tarefas.csv
```

Assistant:

```markdown
Sweep -> imported reference

Found in references:
- `tarefas.csv`: columns task, project, due, status, tags
- 42 open items, 8 overdue, 6 waiting-like items

Recommended focus areas:
- trabalho -> 24 tasks across client/internal projects
- financas -> IPVA, invoice, tax notes
- casa -> repairs and purchases

Questions:
1. Posso mapear a coluna `project` para projetos ativos?
   Recommended: sim -> preserva agrupamentos existentes.
2. Itens com tag `waiting` devem ir para `waiting-for.md`?
   Recommended: sim -> sao dependencias, nao proximas acoes.
3. Itens sem projeto devem ir primeiro para `inbox.md`?
   Recommended: sim -> precisam ser esclarecidos antes de organizar.

Next branch: projects
```

## 5. Today plan

User:

```text
/gwd-today tenho 2h, energia baixa, preciso avancar projeto X
```

Assistant:

```markdown
Plan -> hoje

Focus: avancar projeto X sem exigir alta energia.
Capacity: 2h, energy low

1. P0 @low-energy revisar ultimo estado do projeto X (15m)
2. P0 @computer executar menor proxima acao desbloqueadora (45m)
3. P1 @phone enviar atualizacao para pessoa envolvida (10m)
4. P1 @low-energy registrar proxima acao clara (10m)

First move: abrir o arquivo do projeto X e escrever "estado atual" em 3 bullets.
```

## 6. Weekly review

User:

```text
/gwd-weekly
```

Assistant:

```markdown
Review -> weekly

Ordem:
1. Inbox zero
2. Calendar lookback/lookahead
3. Waiting-for
4. Projetos ativos
5. Next actions por contexto
6. Someday/maybe
7. Escolher foco da semana

Comecar pelo inbox?
```

## 6. Horizons snapshot

User:

```text
/gwd-horizons
```

Assistant:

```markdown
Horizons -> snapshot

H5 Purpose  : fuzzy
H4 Vision   : missing
H3 Goals    : overloaded
H2 Areas    : health neglected
H1 Projects : 2 missing next action
H0 Actions  : clear

Gaps:
- Vision missing; goals may be reactive.
- Health area has no current project or recurring action.

Recommended next command: `/gwd-weekly` first, then `/gwd-vision`.
```

## 7. Alignment check

User:

```text
/gwd-align projeto Criar canal no YouTube
```

Assistant:

```markdown
Align -> Criar canal no YouTube

Status: aligned

Chain:
H1 project -> H2 carreira/criatividade -> H3 construir autoridade em IA -> H4 negocio independente -> H5 autonomia/aprendizado

Evidence:
- Projeto apoia autoridade publica.
- Pode virar ativo de longo prazo.

Risk:
- Pode competir com familia/saude se nao houver limite.

Recommendation:
- keep
- limitar a 2 blocos por semana
- next action: escrever roteiro do primeiro video (45m)
```


## 8. Token-saving next query

User:

```text
/gwd-next @computer 30m energia baixa
```

Assistant internal first step:

```text
.agents/skills/gwd/scripts/gwd-query next --root . --context @computer --time 30 --energy low --format json
```

Assistant:

```markdown
Next -> agora

Recommended: na:24 because it matches context/time/energy.

1. P1 @computer revisar proposta (25m) -> Client project
2. P2 @computer limpar inbox de notas (15m) -> Admin

Comecar por qual acao?
```

## 9. Token-saving weekly review

User:

```text
/gwd-weekly
```

Assistant internal first step:

```text
.agents/skills/gwd/scripts/gwd-query review --root . --type weekly --format json
```

Assistant:

```markdown
Review -> weekly

Script summary:
- inbox_open: 12
- projects_missing_next: 3
- waiting_followups_due: 2

Recommended order:
1. `/gwd-process inbox`
2. fix projects missing next action
3. follow up waiting items

Comecar pelo inbox?
```
