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
waiting-for.md
someday-maybe.md
calendar.md
```

## Task line

Canonical format:

```markdown
- [ ] P1 @context Task text (30m) -> Project or Area
```

Fields:

| Field | Required | Example |
|---|---|---|
| checkbox | yes | `[ ]`, `[x]` |
| priority | recommended | `P0`, `P1`, `P2` |
| context | recommended | `@computer`, `@phone`, `@deep` |
| text | yes | `Review proposal` |
| estimate | optional | `(30m)` |
| link | optional | `-> Sales project` |

## `inbox.md`

Canonical capture:

```markdown
- [ ] YYYY-MM-DD HH:MM | raw item text
```

Rules:

- Preserve original wording.
- One capture per line.
- Do not classify here unless user explicitly asks.

## `next-actions.md`

Use context sections and task lines.

```markdown
## @computer
- [ ] P1 Review proposal (30m) -> Client project

## @phone
- [ ] P0 Call Ana about contract (10m) -> Sales
```

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
