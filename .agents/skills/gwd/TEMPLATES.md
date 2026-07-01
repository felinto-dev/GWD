# GWD Templates

Use these templates as defaults. Keep user data concise. Prefer appends and small edits.

Keep these formats parseable by `scripts/gwd-query`; see `SCHEMA.md` before changing table columns or task-line structure.

## Base files

### `inbox.md`

```markdown
# Inbox

Raw captures. Process top-down. Preserve original wording.

| ID | Added | Title | Description |
|---|---|---|---|
| in-YYYYMMDD-HHMMSS-001 | YYYY-MM-DD HH:MM | Example title | Optional details, context, links, or notes |
```

### `next-actions.md`

```markdown
# Next Actions (H0)

Canonical list of single visible physical actions.

| ID | Added | Title | Description | Context |
|---|---|---|---|---|
| na-YYYYMMDD-HHMMSS-001 | YYYY-MM-DD HH:MM | Call Ana about contract | Project/area, notes, or useful detail | @phone |
```

### `projects.md`

```markdown
# Projects (H1)

Outcomes that require more than one action and can be completed within about one year.
Canonical project details live in `projects/active/<slug>/`.

| Project | Area | Goal | Status | Next Action | Updated |
|---|---|---|---|---|---|
| Example | Work | Goal name | active | Example next action | YYYY-MM-DD |
```

### `areas.md`

```markdown
# Areas of Focus (H2)

Ongoing responsibilities that need standards, not completion.

| Area | Standard | Current attention | Related projects | Review cadence |
|---|---|---|---|---|
| Work | Reliable delivery and clear priorities | normal |  | weekly |
| Health | Energy, sleep, movement, prevention | normal |  | weekly |
```

### `goals.md`

```markdown
# Goals (H3)

Outcomes for roughly 3 months to 2 years.

| Goal | Horizon | Area | Evidence of success | Projects | Status |
|---|---|---|---|---|---|
| Example goal | 12 months | Work | measurable result | project slug | active |
```

### `vision.md`

```markdown
# Vision (H4)

Direction for roughly 3 to 5 years.

## Life / Work Picture

- 

## Strategic Themes

| Theme | Why it matters | Related goals |
|---|---|---|
|  |  |  |

## Constraints

- 
```

### `purpose.md`

```markdown
# Purpose and Principles (H5)

## Purpose

Why this life/work exists.

## Principles

- Principle: how it changes decisions.

## Non-Negotiables

- 

## Trade-offs

| Prefer | Over |
|---|---|
|  |  |
```

### `horizons.md`

Derived snapshot. Refresh from canonical H0-H5 files; do not treat as source of truth.

```markdown
# Horizons Map

Generated: YYYY-MM-DD HH:MM

## Snapshot

H5 : clear|fuzzy|missing
H4 : clear|fuzzy|missing
H3 : clear|overloaded|missing
H2 : clear|neglected|missing
H1 : current|stale|missing
H0 : clear|noisy|missing

## Counts

- inbox_open: 0
- next_open: 0
- projects_active: 0
- projects_missing_next: 0
- waiting_due: 0

## Gaps

- 

## Next

- /gwd-next

## Notes

User-written notes to preserve across refreshes.
```


### `gwd-memory.md`

```markdown
# GWD Memory

Operational memory for preferences, decisions, patterns, and workflow friction. Do not store tasks or daily logs here.

## Ativas

### mem-YYYYMMDD-001 - Short title

Tipo: decisao operacional
Criada em: YYYY-MM-DD
Escopo: inbox, projetos, reviews
Status: ativa
Esquecer em: objective condition for when this memory stops being useful

Nota:
- Practical rule or observation to apply in future GWD decisions.

### mem-20260701-001 - Transicao Super Downloads API -> Splita

Tipo: decisao operacional
Criada em: 2026-07-01
Escopo: inbox, projetos, triagem de features
Status: ativa
Esquecer em: Super Downloads API nao estiver mais ativo ou a migracao para Splita estiver concluida

Nota:
- Ideias antigas do Super Downloads API devem ser reavaliadas para Splita.
- Features futuras do Splita devem ir para backlog SDD quando ele for canonico.
- GWD mantem compromisso, foco e proximas acoes atuais, sem duplicar backlog tecnico.

## Arquivadas
```

### `waiting-for.md`

```markdown
# Waiting For

| Date | Item | Person/Source | Follow-up | Project/Area | Status |
|---|---|---|---|---|---|
| YYYY-MM-DD | Item | Name | YYYY-MM-DD | Project | open |
```

### `someday-maybe.md`

```markdown
# Someday / Maybe

Ideas and non-committed outcomes.

## Theme or Area

| Item | Motivo | Próxima revisão | Logs |
|---|---|---|---|
| Idea text | Why it is not active now | YYYY-MM-DD | YYYY-MM-DD: user deferred for 1 month. Motivo: reason/context. |
```

### `calendar.md`

```markdown
# Calendar

Hard landscape only: date-specific or time-specific commitments.

## YYYY-MM-DD
- HH:MM Item
- All day: Item
```

## Project files

### `projects/active/<slug>/info.md`

```markdown
# Project: <Name>

Status: active
Area: <area>
Goal: <goal or none>
Vision link: <theme or none>
Created: YYYY-MM-DD
Updated: YYYY-MM-DD

## Outcome

What is true when this is done?

## Why

Why this matters.

## Alignment

- H2 Area:
- H3 Goal:
- H4 Vision:
- H5 Principle:

## Definition of Done

- [ ] Criterion

## Notes

- Support material belongs here or in reference.
```

### `projects/active/<slug>/tasks.md`

```markdown
# Tasks: <Name>

## Next Actions

- [ ] @context Action text (30m)

## Later

- [ ] Future action

## Done

- [x] YYYY-MM-DD Completed action
```

## Daily file

### `daily/YYYY-MM-DD.md`

```markdown
# YYYY-MM-DD

## Plan

Focus: <one outcome>
Time: <available time>
Energy: high|medium|low

### Must
- [ ] @context Action (time)

### Should
- [ ] @context Action (time)

### Could
- [ ] @context Action (time)

## Log

- HH:MM Done/started note

## Shutdown

Done:
Carry:
Tomorrow first move:
```

## Response templates

### Capture response

```markdown
Capture -> N item(s).

Added:
- item 1 - description if present
- item 2

Next -> `/gwd-process`.
```

### Clarify response

```markdown
Clarify -> <item>

Decision: next action | project | waiting | someday | reference | calendar | trash
Destination: `<path>`

Next action row: `| na-... | YYYY-MM-DD HH:MM | action | description | @context |`
Question: <only if needed>
```

### Setup sweep response

```markdown
Setup -> sweep

References checked:
- `<file>` -> <useful signal>

Recommended horizons:
- H2 <area> -> <why>
- H3 <goal> -> <why>

Questions:
1. <question>
   Recommended: <answer> -> <reason>
2. <question>
   Recommended: <answer> -> <reason>

Next branch: <actions|projects|areas|goals|vision|purpose>
```

### Horizons response

```markdown
Horizons -> snapshot

H5 Purpose  : <status>
H4 Vision   : <status>
H3 Goals    : <status>
H2 Areas    : <status>
H1 Projects : <status>
H0 Actions  : <status>

Gaps:
- ...

Recommended next command: `/gwd-...`
```

### Alignment response

```markdown
Align -> <item>

Status: aligned | weak alignment | conflict | unknown

Chain:
H0 action -> H1 project -> H2 area -> H3 goal -> H4 vision -> H5 principle

Evidence:
- ...

Risk:
- ...

Recommendation:
- keep | revise | pause | move to someday | delete after confirmation
```

### Daily plan response

```markdown
Plan -> hoje

Focus: <one outcome>
Capacity: <time>, energy <level>

1. @context <action> -> why
2. @context <action> -> why
3. @context <action> -> why

First move: <2-minute start>
```

### Next action picker

```markdown
Next -> agora

Recommended: #1 because <reason>.

| # | Action | Context | Time | Energy | Why |
|---|---|---|---|---|---|
| 1 | ... | @computer | 25m | low | ... |

Comecar por qual acao?
```

### Task start

```markdown
Start -> <action>

Objective: <result>

Steps:
1. <2-minute start>
2. <next step>
3. <next step>

Done when:
- [ ] <criterion>

If blocked: <fallback>
```

### Done response

```markdown
Done -> <action>

Updated:
- `<canonical file>`
- `daily/YYYY-MM-DD.md`

Next action: <new action or none>
```

## Priority guide

- Consequence if not done soon.
- Alignment with active outcomes.
- Context, time, energy, and momentum.

## Context guide

- `@computer`: any computer work.
- `@phone`: calls or messages.
- `@errand`: outside/home logistics.
- `@home`: physical home tasks.
- `@office`: workplace-only tasks.
- `@deep`: focus, high cognition.
- `@low-energy`: admin or simple tasks.
- `@agenda-name`: discuss with a person.
