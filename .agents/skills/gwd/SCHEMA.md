# GWD Markdown Schema

This schema keeps GWD files parseable by `scripts/gwd-query`. The goal is token savings: scripts return compact summaries, and the agent reads full markdown only when needed.

## Query rule

Before reading large GWD files, prefer:

```text
.agents/skills/gwd/scripts/gwd-query <mode> --root . --format json
```

Read full markdown only when editing, resolving warnings, confirming destructive actions, or when the user asks for full detail.

## Base files

```text
inbox.md
next-actions.md
projects.md
areas.md
goals.md
vision.md
purpose.md
horizons.md
gwd-memory.md
waiting-for.md
someday-maybe.md
calendar.md
```

## Task line legacy format

Checklist task lines are legacy/fallback for older project support files. Root `next-actions.md` uses a table.

```markdown
- [ ] @context Task text (30m) -> Project or Area
```


## `inbox.md`

Canonical capture table:

```markdown
| ID | Added | Title | Description |
|---|---|---|---|
| in-YYYYMMDD-HHMMSS-001 | YYYY-MM-DD HH:MM | Title | Optional detail preserved from the original capture |
```

Fields:

| Field | Required | Example |
|---|---|---|
| ID | yes | `in-20260701-093000-001` |
| Added | yes | `2026-07-01 09:30` |
| Title | yes | `Responder Ana` |
| Description | optional | `Ela pediu retorno sobre contrato e prazo.` |

Rules:

- Preserve original wording across title and description.
- One capture entry per table row.
- Keep `ID` stable; never regenerate it after row creation.
- `Added` is the date and time when the item entered inbox.
- Do not track completion status in inbox; processed items leave the table.
- If an item takes less than 2 minutes, do it now and log it instead of keeping it in inbox.
- Escape literal pipes as `\|` inside cells.
- Do not classify here unless user explicitly asks.


## `gwd-memory.md`

Canonical operating memory. Use for confirmed preferences, decisions, recurring patterns, and workflow friction that should guide future GWD decisions. Do not store tasks, product backlog items, or daily logs here.

Entry format:

```markdown
### mem-YYYYMMDD-001 - Short title

Tipo: decisao operacional
Criada em: YYYY-MM-DD
Escopo: inbox, projetos, reviews
Status: ativa
Esquecer em: objective condition

Nota:
- Memory text.
```

Fields:

| Field | Required | Example |
|---|---|---|
| ID | yes | `mem-20260701-001` |
| Tipo | yes | `decisao operacional` |
| Criada em | yes | `2026-07-01` |
| Escopo | recommended | `inbox, projetos` |
| Status | yes | `ativa`, `arquivada` |
| Esquecer em | recommended | `quando o projeto X for concluido` |
| Nota | yes | practical guidance |

Rules:

- Add memories only after user confirmation.
- `Esquecer em` is an expiry condition, not a review cadence.
- Monthly review checks whether each active memory's expiry condition has been met.
- Remove only after confirmation; archive under `## Arquivadas` when context may remain useful.
- Daily logs are immutable and separate from memory expiry.

## `next-actions.md`

Canonical next-action table:

```markdown
| ID | Added | Title | Description | Context |
|---|---|---|---|---|
| na-YYYYMMDD-HHMMSS-001 | YYYY-MM-DD HH:MM | Review proposal | Project/area, notes, or useful detail | @computer |
```

Fields:

| Field | Required | Example |
|---|---|---|
| ID | yes | `na-20260701-143000-001` |
| Added | yes | `2026-07-01 14:30` |
| Title | yes | `Review proposal` |
| Description | optional | `Project/area: Client project` |
| Context | yes | `@computer`, `@phone`, `@splita` |

Rules:

- One visible physical action per row.
- Keep IDs stable after creation.
- Do not use P0/P1/P2 priority labels; choose by context, time, energy, consequence, and alignment.
- Escape literal pipes as `\|` inside cells.


## `projects.md`

Dashboard table. Project details live in `projects/active/<slug>/`.

```markdown
| Project | Area | Goal | Status | Next Action | Updated |
|---|---|---|---|---|---|
| Launch site | Work | Grow sales | active | Publish landing page | 2026-06-30 |
```

Required columns:

```text
Project | Area | Goal | Status | Next Action | Updated
```

Status values:

```text
active | paused | waiting | archived
```

## `areas.md`

```markdown
| Area | Standard | Current attention | Related projects | Review cadence |
|---|---|---|---|---|
| Health | Energy, sleep, movement | normal | Sleep reset | weekly |
```

## `goals.md`

```markdown
| Goal | Horizon | Area | Evidence of success | Projects | Status |
|---|---|---|---|---|---|
| Build authority in AI | 12 months | Career | 12 essays published | AI writing system | active |
```

## `waiting-for.md`

```markdown
| Date | Item | Person/Source | Follow-up | Project/Area | Status |
|---|---|---|---|---|---|
| 2026-06-30 | Contract feedback | Ana | 2026-07-03 | Sales | open |
```

## `someday-maybe.md`

Use task lines when possible:

```markdown
- [ ] Write a book | captured 2026-06-30 | maybe 2027
```

## Horizons files

```text
H0 -> next-actions.md
H1 -> projects.md
H2 -> areas.md
H3 -> goals.md
H4 -> vision.md
H5 -> purpose.md
```

`horizons.md` is a derived snapshot, not a source of truth. Regenerate or refresh it from the canonical horizon files:

```text
next-actions.md
projects.md
areas.md
goals.md
vision.md
purpose.md
```

Refresh `horizons.md` when:

- `/gwd-setup` finishes the first sweep.
- `/gwd-horizons` is executed.
- `/gwd-align all` is executed.
- `/gwd-review monthly` or `/gwd-review quarterly` finishes.
- A significant H0-H5 file changes: new project, changed area, changed goal, changed vision, changed purpose.

Generate a compact markdown snapshot with:

```text
gwd-query horizons --root . --format md
```

## Derived files update map

| Derived file | Canonical inputs | Refresh trigger |
|---|---|---|
| `horizons.md` | H0-H5 files | setup, horizons, align all, monthly/quarterly review, significant horizon change |
| `projects.md` | `projects/active/<slug>/info.md`, `tasks.md` | project create/update/archive, weekly review, next action changed |
| `daily/YYYY-MM-DD.md` | selected next actions + done events | today plan, done, daily review |
| `reviews/*` | current system state | end of weekly/monthly/quarterly review |

## Script modes

```text
gwd-query status   --root .
gwd-query summary  --root . --format md
gwd-query inbox    --root . --limit 20
gwd-query next     --root . --context @computer --time 30 --energy low
gwd-query projects --root . --missing-next
gwd-query horizons --root .
gwd-query review   --root . --type weekly
gwd-query align    --root . --item "Criar canal no YouTube"
gwd-query waiting  --root . --due
gwd-query someday  --root . --limit 20
```

## Summary mode

`gwd-query summary --root . --format md` prints a visual mission-control dashboard:

```text
+======================================================================+
|                         GWD MISSION CONTROL                          |
+======================================================================+
| Inbox ... | Next ... | Projects ... | Missing Next ... | Waiting Due ... |
+----------------------------------------------------------------------+
```

Use it for `/gwd-summary` and for quick status checks before reading files.

## Output contract

Every JSON output includes:

```json
{
  "mode": "next",
  "root": "/path/to/root",
  "generated_at": "YYYY-MM-DDTHH:MM:SS",
  "files_read": ["next-actions.md"],
  "warnings": [],
  "next_command": "/gwd-start na:12"
}
```

Scripts are tolerant. If a file is missing or partially formatted, return `warnings` instead of failing.
