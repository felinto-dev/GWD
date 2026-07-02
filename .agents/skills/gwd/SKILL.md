---
name: gwd
description: Get Work Done, a local life and work execution method. Use whenever the user mentions GWD, capture, inbox, next actions, projects, contexts, waiting-for, someday/maybe, daily planning, weekly review, focus areas, goals, vision, purpose, horizons of focus, alignment, mind sweep, personal organization, or wants help deciding what to do next. Also use for the /gwd* commands.
---

# GWD - Get Work Done

GWD is a local-first organization and execution method. Help the user capture, clarify, organize, review, and execute commitments across all horizons: daily actions, projects, areas, goals, vision, and principles.

Default language: PT-BR. Keep it direct, practical, and calm. ASCII is fine. Use tables only when they reduce ambiguity.

## Core loop

```text
capture -> clarify -> organize -> reflect -> engage
```

## Horizons of focus

Use these horizons to connect execution with direction. Prefer bottom-up stabilization first: clear what is pulling attention now, then climb to broader decisions.

```text
+--------------------------------------------------+
| H5  purpose.md       Purpose + principles        |
+--------------------------------------------------+
| H4  vision.md        3-5 year vision             |
+--------------------------------------------------+
| H3  goals.md         3 month-2 year goals        |
+--------------------------------------------------+
| H2  areas.md         ongoing responsibilities    |
+--------------------------------------------------+
| H1  projects.md      outcomes within ~1 year     |
+--------------------------------------------------+
| H0  next-actions.md  visible physical actions    |
+--------------------------------------------------+
```

H0 and H1 create control. H2-H5 create perspective. The system needs both.

## Non-negotiables

- Store state in visible markdown files at the workspace root when writing is needed.
- One commitment lives in one canonical place. Dashboards summarize; they do not duplicate tasks.
- Prefer inserting new rows in date-descending order instead of appending. Before overwriting, deleting, archiving, or resetting, inspect the target and ask for exact confirmation.
- If a request is vague, capture first; clarify later.
- Preserve the user's wording in inbox title and description. Do not over-process raw captures.
- During setup and sweep, inspect useful local reference files before asking questions.
- During `/gwd-process`, ask confirmation questions in plain text instead of using interactive question tools; the extra UI slows down inbox triage and can obscure that only one item is being processed.
- For each setup/sweep question, provide a recommended answer and the reason.
- Run alignment automatically when creating/reviewing projects and during monthly/quarterly reviews.

## State layout

Use this structure when setting up or maintaining the system:

```text
./
|-- inbox.md
|-- next-actions.md
|-- projects.md
|-- areas.md
|-- goals.md
|-- vision.md
|-- purpose.md
|-- horizons.md
|-- gwd-memory.md
|-- waiting-for.md
|-- someday-maybe.md
|-- calendar.md
|-- daily/
|   `-- YYYY-MM-DD.md
|-- reviews/
|   |-- weekly/YYYY-WW.md
|   |-- monthly/YYYY-MM.md
|   `-- quarterly/YYYY-QN.md
|-- projects/
|   |-- active/<project-slug>/info.md
|   |-- active/<project-slug>/tasks.md
|   `-- archived/
`-- reference/
```

If `inbox.md` and the base GWD files are missing from the workspace root and the user is not running setup, offer `/gwd-setup` or capture the request in conversation without writing.

## Canonical vs derived files

Canonical files are the source of truth. Derived files are dashboards, logs, or snapshots that should be refreshed from canonical data.

| File | Type | Refresh when |
|---|---|---|
| `inbox.md` | canonical capture | `/gwd-capture`, sweep discoveries, loose thoughts in reviews |
| `next-actions.md` | canonical actions | `/gwd-process`, `/gwd-next`, `/gwd-done` when creating follow-up actions |
| `projects/active/<slug>/` | canonical project detail | `/gwd-project`, project review, project completion/archive |
| `projects.md` | dashboard | project created/paused/archived, next action changes, weekly review |
| `areas.md` | canonical areas + standards | setup/sweep, `/gwd-areas`, monthly review, project assigned to a new area |
| `goals.md` | canonical goals | `/gwd-goals`, monthly/quarterly review, project linked/unlinked to a goal |
| `vision.md` | canonical vision | `/gwd-vision`, quarterly review |
| `purpose.md` | canonical principles | `/gwd-purpose`, quarterly review |
| `horizons.md` | derived snapshot | setup finalization, `/gwd-horizons`, `/gwd-align all`, monthly/quarterly review, any significant H0-H5 change |
| `gwd-memory.md` | canonical operating memory | confirmed preferences, decisions, patterns, and workflow friction; monthly review checks `Esquecer em` conditions |
| `waiting-for.md` | canonical waiting list | `/gwd-waiting`, delegated item, follow-up resolved, weekly review |
| `someday-maybe.md` | canonical incubator | `/gwd-someday`, deferred item, monthly review |
| `calendar.md` | canonical hard landscape | date/time-specific item discovered in process/sweep |
| `daily/YYYY-MM-DD.md` | log/plan | `/gwd-today`, `/gwd-done`, daily review |
| `reviews/*` | review archive | end of weekly/monthly/quarterly reviews |

`horizons.md` is not a source of truth. Update it from `next-actions.md`, `projects.md`, `areas.md`, `goals.md`, `vision.md`, and `purpose.md`. Generate a compact snapshot with:

```text
.agents/skills/gwd/scripts/gwd-query horizons --root . --format md
```

Before updating derived files, read the target file if it already exists. Preserve user notes that are not regenerated by the script.

## Token-saving queries

Use bundled scripts before reading large GWD markdown files. This keeps context small as the system grows.

Default command from the workspace root:

```text
.agents/skills/gwd/scripts/gwd-query <mode> --root . --format json
```

Prefer scripts for read-only summaries:

| Need | Query |
|---|---|
| mission-control summary | `gwd-query summary --root . --format md` |
| overall status | `gwd-query status --root .` |
| inbox items | `gwd-query inbox --root . --limit 20` |
| next actions | `gwd-query next --root . --context @computer --time 30 --energy low` |
| project health | `gwd-query projects --root . --missing-next` |
| horizons map | `gwd-query horizons --root .` |
| operating memory | `gwd-query memory --root .` |
| review summary | `gwd-query review --root . --type weekly` |
| alignment | `gwd-query align --root . --item "..."` |
| waiting-for | `gwd-query waiting --root . --due` |
| someday/maybe | `gwd-query someday --root . --limit 20` |

Read full markdown only when:

- editing that file;
- script returns warnings or ambiguity;
- user asks for full detail;
- destructive/archive/reset confirmation needs exact file contents.

Scripts are read-only. They never modify user data. See `SCHEMA.md` for parseable markdown conventions.

## List ordering

Any canonical list with an added/created date column must stay sorted newest first by that date. This applies to `inbox.md`, `next-actions.md`, `projects.md`, `waiting-for.md`, `someday-maybe.md`, `calendar.md`, and project task lists when they store added dates.

When adding or moving an item:

- Preserve existing headings/sections.
- Read the destination table and compare the new row's `Added`/created timestamp against neighboring rows before editing.
- Insert the row in date-descending position: below newer rows and above older rows in the same table/section.
- Never append to the bottom just because it is easier; bottom insertion is only correct when the new row is the oldest item in that table/section.
- If several rows share the same timestamp, preserve their existing relative order and place the new row after existing rows with that same timestamp unless there is a clear ID/order convention.
- If the destination table has no added/created date column, add one only when the workflow schema requires it; otherwise keep the existing format and choose the nearest date column available.
- If a list is already out of order, fix the affected table/section enough that the inserted/moved row is correctly positioned; do not perform a broad cleanup unless the user asks.

## GWD memory workflow

Use `gwd-memory.md` for operational memory: preferences, decisions, recurring patterns, and workflow friction that should guide future triage. Do not store tasks, project backlogs, daily logs, or immutable history there.

Memory entries need explicit user confirmation before writing. Each active entry should include `Esquecer em`, an objective condition for when the memory stops being useful.

During `/gwd-review monthly`, review `gwd-memory.md` first when it exists:

1. Read active memories.
2. Check each `Esquecer em` condition against current reality.
3. If the condition is met, recommend archive or removal.
4. Remove only after confirmation; archive under `## Arquivadas` when historical context may remain useful.
5. Keep valid memories unchanged.

Daily logs are immutable and do not participate in memory expiry.

## Slash command routing

| Command | Mode |
|---|---|
| `/gwd` | route request, show status, or choose workflow |
| `/gwd-summary` | polished mission-control dashboard across tasks, projects, and horizons |
| `/gwd-setup` | initialize files, inspect references, run first sweep |
| `/gwd-sweep` | guided mind sweep and horizon discovery |
| `/gwd-capture` | quick capture to inbox |
| `/gwd-clarify` | clarify one item |
| `/gwd-refine` | improve title and description for one existing item by ID |
| `/gwd-process` | process inbox items |
| `/gwd-plan` | plan today or week |
| `/gwd-today` | fast daily plan |
| `/gwd-next` | choose executable next actions now |
| `/gwd-start` | break one action into steps |
| `/gwd-done` | log completion and update task state |
| `/gwd-project` | create or review a project |
| `/gwd-areas` | review areas of focus and responsibility |
| `/gwd-goals` | define/review goals for 3 months-2 years |
| `/gwd-vision` | define/review 3-5 year vision |
| `/gwd-purpose` | define/review purpose and principles |
| `/gwd-horizons` | show the full horizon map |
| `/gwd-align` | check alignment across horizons |
| `/gwd-waiting` | manage delegated or pending items |
| `/gwd-someday` | manage incubated ideas |
| `/gwd-review` | daily, weekly, monthly, or quarterly review |
| `/gwd-weekly` | full weekly review |
| `/gwd-reset` | safe reset or archive flow |

If the mode is unclear, route by intent and state the chosen mode in one line.

## Summary workflow

Use `/gwd-summary` when the user wants the big picture, main tasks, or a dashboard.

1. Run `.agents/skills/gwd/scripts/gwd-query summary --root . --format json` first.
2. Optionally run `--format md` for a ready-made ASCII mission-control panel.
3. Show: focus, counts, horizons, top actions, flagged projects, due waiting items, gaps, and next command.
4. Keep it visual and scannable. Use ASCII banners/boxes. Do not dump full files.
5. If script returns warnings, mention them and read only the needed file/section.

## Local reference discovery

Use this before setup questions and during `/gwd-sweep` when it can reduce guesswork.

- Look for relevant visible files in the current workspace: `.md`, `.txt`, `.csv`, `.json`, `.yaml`, `.yml`, `.ics`, `.opml`, exports, task lists, notes, plans, or README-like files.
- Ignore tool/system folders unless the user points to them: `.git/`, `.agents/`, `.zcode/`, `node_modules/`, build outputs, caches, vendor folders.
- Do not treat this skill's own files as user reference material.
- For large files, inspect names, headings, schemas, headers, and representative samples first.
- For CSV/task exports, infer columns like task, project, due date, status, labels, notes, and priority.
- If a question can be answered from local reference material, answer it from the file instead of asking.
- When inference is uncertain, show the evidence and ask for confirmation.
- Before importing or rewriting many items from a reference file, summarize the proposed mapping and ask for confirmation.

## Setup workflow

Use for `/gwd-setup` or first-time onboarding.

1. Inspect whether base files exist at the workspace root.
2. Run local reference discovery before asking personal questions.
3. Infer possible areas, goals, active projects, waiting items, and imported tasks from discovered material.
4. If missing, create the folder tree and base files from `TEMPLATES.md`.
5. Run the sweep workflow automatically on first initialization unless the user explicitly says to skip it.
6. Sweep bottom-up by default: inbox/open loops -> actions -> projects -> areas -> goals -> vision -> purpose.
7. Ask focused questions in rounds. For each question, include your recommended answer.
8. Create no fake tasks. Seed only headings and confirmed items.
9. Refresh `horizons.md` from canonical files.
10. End with setup summary, open decisions, and the first next action.

## Sweep workflow

Use for `/gwd-sweep`, during first setup, and whenever the user wants a deep reset of mental open loops.

Mindset:

- Interview the user relentlessly until there is shared understanding.
- Walk down each branch of the design tree one decision at a time.
- Resolve dependencies in order: open loops -> actions -> projects -> areas -> goals -> vision -> purpose.
- If a question can be answered by exploring local reference material, explore first and ask only for confirmation.
- For every question, provide a recommended answer and why.
- Relentless does not mean overwhelming: ask 3-5 high-leverage questions per round, then continue.

Sweep branches:

| Branch | Goal |
|---|---|
| Open loops | Capture anything pulling attention |
| Next actions | Extract visible physical actions |
| Projects | Convert multi-step outcomes into project candidates |
| Areas | Define ongoing responsibilities and standards |
| Goals | Define 3 month-2 year outcomes |
| Vision | Define 3-5 year direction |
| Purpose | Define principles and why |
| Waiting | Identify people/systems blocking progress |
| Calendar | Find date-specific commitments |
| Someday | Preserve ideas without making false commitments |
| Contexts | Define where/how work actually gets done |
| Energy and capacity | Match work to realistic attention and time |
| Review cadence | Decide how the system stays trusted |

Sweep response shape:

```markdown
Sweep -> <scope>

Found in references:
- <file>: <useful fact>

Recommended horizons:
- H2 <area> -> why
- H3 <goal> -> why

Questions:
1. <question>
   Recommended: <answer> -> <reason>

Next branch: <branch>
```

For first setup, prioritize areas of focus and imported commitments before deep productivity coaching.

## Horizon workflows

### `/gwd-purpose`

Define or review `purpose.md`:

- Why do I exist / why does this work matter?
- Which principles are non-negotiable?
- What trade-offs am I unwilling to make?
- What does success never get to cost?

### `/gwd-vision`

Define or review `vision.md` for 3-5 years:

- Desired life/career/business picture.
- Lifestyle constraints.
- Identity shifts.
- External trends or opportunities.

### `/gwd-goals`

Define or review `goals.md` for 3 months-2 years:

- Outcomes with measurable evidence.
- Linked areas and vision.
- Projects required to make progress.
- Things to reduce, stop, or avoid.

### `/gwd-areas`

Define or review `areas.md`:

- Ongoing responsibilities.
- Standards to maintain.
- Current attention level.
- Related projects and recurring reviews.

### `/gwd-horizons`

Show the full pyramid and current content of each horizon. Highlight gaps, overload, or misalignment.

### `/gwd-align`

Check whether an action, project, area, or goal fits the higher horizons.

Run automatically when:

- Creating or reviewing a project with `/gwd-project`.
- Running `/gwd-review monthly`.
- Running `/gwd-review quarterly`.
- Setup/sweep discovers a major commitment.

After `/gwd-align all`, refresh `horizons.md`.

Manual use cases:

```text
/gwd-align projeto Criar canal no YouTube
/gwd-align next action escrever roteiro do video
/gwd-align all
```

Alignment response:

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

## Capture workflow

Use for `/gwd-capture` and any raw input.

- Add each item as one row in the `inbox.md` table with stable `ID` and `Added` timestamp.
- Generate `ID` once when capturing, using `in-YYYYMMDD-HHMMSS-NNN`; never regenerate existing IDs.
- `Added` is the local date and time when the item entered inbox.
- Use the first short phrase as `Title`; put extra context in `Description`.
- Preserve original wording across title and description.
- Split obvious multi-item lists into separate rows.
- Do not add checklist/status columns to inbox; inbox items are unresolved, not tasks to complete.
- If an item takes less than 2 minutes, do it now and log it instead of keeping it in inbox.
- Escape literal pipes as `\|` inside table cells.
- Do not decide project/context unless the user asks or the item is unambiguous.
- If writing is not possible, return a capture block the user can paste.

Capture format:

```markdown
| ID | Added | Title | Description |
|---|---|---|---|
| in-YYYYMMDD-HHMMSS-001 | YYYY-MM-DD HH:MM | Titulo da captura | detalhes opcionais preservados do pedido original |
```

## Clarify workflow

Use for `/gwd-clarify` or one inbox item.

Ask these questions quickly:

1. What is it?
2. Is it actionable?
3. If no: trash, reference, someday/maybe.
4. If yes: what is the desired outcome?
5. What is the next visible physical action?
6. Is it one step or a project?
7. Is it time-specific, delegated, or context-based?

Decision rules:

| Case | Destination |
|---|---|
| Not useful | delete only after confirmation |
| Non-actionable info | `reference/` or note path |
| Maybe later | `someday-maybe.md` |
| Time/date-specific | `calendar.md` |
| Delegated / pending | `waiting-for.md` |
| One action | `next-actions.md` table |
| Multi-step outcome | `projects/active/<slug>/` + next action |

Do not leave a clarified item only in inbox. Move it to its canonical place or ask the missing question.

## Refine item workflow

Use for `/gwd-refine <item-id>` when the user wants to improve the title and description of one existing item without moving it.

Intent:

- Make an existing item easier to understand later.
- Preserve the item's ID, date, status, context, review date, blockers, and canonical location.
- Improve only the title and description unless the user explicitly asks for another change.

Supported item locations:

| ID prefix | Primary location |
|---|---|
| `in-` | `inbox.md` |
| `na-` | `next-actions.md` |
| `sm-` | `someday-maybe.md` |
| project/task IDs or unknown prefixes | search canonical GWD files and `projects/active/*/` |

Workflow:

1. Require exactly one item ID. If missing, ask which ID to refine.
2. Locate the item from the ID. Prefer prefix-based files first, then search canonical files. If multiple matches exist, show the candidates and ask which one.
3. Read the full file before editing. Capture the current row/section, title, description, and nearby context.
4. Inspect related local context before asking: project detail files, `projects.md`, linked area/goal, blockers, waiting-for, daily logs, or other tasks with the same project/title words.
5. Interview until there is shared understanding. Ask one question at a time and wait for the user's answer before continuing.
6. For every question, include a recommended answer and why. If evidence already answers it, state the inference and ask only for confirmation.
7. Walk the decision tree in dependency order: what it means -> desired outcome -> why it matters -> boundaries/exclusions -> next visible action or done state -> wording.
8. Stop interviewing when the improved wording is clear enough to be useful on review day; do not chase perfection.
9. Show the proposed replacement title and description, then ask for confirmation before editing.
10. After confirmation, update only the title/description cells or fields in the canonical item. Preserve ID, Added/date, context, review date, blockers, ordering, and surrounding formatting.
11. Summarize old -> new and the file changed.

Question shape:

```markdown
Refine -> <item-id>

Atual:
- Título: <current title>
- Descrição: <current description or ->

Inferi:
- <fact from existing tasks/logs/context>

Pergunta: <one question>
Recomendado: <answer> -> <reason>
```

Confirmation shape before editing:

```markdown
Refine -> proposta

Título: <new title>
Descrição: <new description>

Aplicar esta alteração em `<file>`?
```

Do not use `/gwd-refine` to process inbox, change destination, mark done, reprioritize, or create project structure. If the interview reveals that the item belongs elsewhere, recommend `/gwd-clarify` or `/gwd-process` after refining, but do not move it in the same step unless the user explicitly asks.

## Process inbox workflow

Use for `/gwd-process`.

`/gwd-process` is confirmation-first. It never categorizes, moves, or removes an inbox item automatically, even when the destination looks obvious.

1. Run the inbox query before reading full markdown when possible.
2. Process top-down unless user gave a scope.
3. Show one item at a time, or a small numbered batch if the user asks for batch triage.
4. Before asking any destination question, display the item title and, when present, its description in the question itself or its visible context. Do not include the ID unless it helps disambiguate duplicate titles. Do not mention the description when it is empty. The user must know exactly what they are confirming without relying on previous messages.
5. This also applies when presenting the next item after a move: show the next item's title and description before recommending a destination. Do not collapse described items to title-only prompts.
6. For long descriptions, show a useful concise version that preserves the decision-relevant details; if the user asks or the destination decision depends on details, show the full description before asking.
7. For each item, ask the user to choose or confirm the destination before editing any file.
8. Include a recommended destination and the reason when useful, but treat it as a suggestion only.
9. After user confirmation, update the destination file, then remove the row from `inbox.md`; do not mark inbox rows as done.
10. Stop when waiting for the user's answer, blocked by missing info, user time limit, or inbox zero.
11. Summarize confirmed moves and remaining inbox count.

Do not batch-delete inbox content without preserving the moved decisions. Do not infer permission from obvious wording; ask first.

## Project workflow

Use for `/gwd-project` and multi-step outcomes.

A project is any outcome needing more than one action and finishable within about one year.

Each active project needs:

- Outcome: clear done state.
- Why: reason it matters.
- Area: life/work domain.
- Goal or vision link when applicable.
- Status: active, paused, waiting, archived.
- Next action: at least one visible physical action.
- Support material: links or notes, not mixed with next actions.

Run alignment before making a new project active if higher-horizon data exists.

If a project has no next action, flag it during reviews.

## Planning workflow

Use for `/gwd-plan` and `/gwd-today`.

Inputs to consider:

- Hard landscape from `calendar.md` or user-provided schedule.
- Time available.
- Energy: high, medium, low.
- Context: where/tools/people available.
- Consequence, urgency, and alignment with areas/goals.
- Waiting-for and deadlines.
- Alignment with areas/goals when choosing between important work.

Daily plan should be small enough to finish. Prefer 1 main outcome, 2-4 next actions, and a shutdown note.

## Engage workflow

Use for `/gwd-next` and decision support.

Filter next actions in this order:

1. Context available now.
2. Time available now.
3. Energy available now.
4. Consequence / urgency.
5. Alignment with areas/goals.
6. Momentum.

Return 3-7 options max. Recommend one.

## Start workflow

Use for `/gwd-start`.

Turn the selected next action into:

- Objective.
- 3-7 small steps.
- First 2-minute start.
- Definition of done.
- Blocker plan.

Do not create a new planning project when the user needs to act. Make the next move obvious.

## Done workflow

Use for `/gwd-done`.

- Add a timestamped daily log entry for every completed action.
- If it was a 2-minute inbox item, log completion and remove it from `inbox.md`.
- If it was an open next action, remove its table row from `next-actions.md`; do not keep completed actions there.
- If it was a project action, move/record it under the project's Done section when present, then propose or create the next action.
- If it completes the project, update `projects.md`; archive `projects/active/<slug>/` only after confirmation.
- Summarize briefly.

If the task cannot be identified, ask which item or provide a short candidate list.

## Waiting and someday workflows

Use `/gwd-waiting` for things delegated, ordered, requested, or blocked on others. Each item needs owner/source, date, follow-up trigger.

Use `/gwd-someday` for ideas, future possibilities, and non-committed outcomes. Review weekly lightly and monthly more deeply.

Someday/maybe table format:

```markdown
| ID | Added | Título | Descrição | Próxima revisão | Blockers |
|---|---|---|---|---|---|
| sm-YYYYMMDD-NNN | YYYY-MM-DD HH:MM | Ideia | detalhes opcionais | YYYY-MM-DD | - [ ] blocker opcional |
```

When adding or moving anything to `someday-maybe.md`:

- Always include `Added` with the local date and time when the idea entered someday/maybe.
- Always ask the user for the estimated next review date before writing the row, even when a default seems obvious.
- Suggest a review date with a reason, but wait for confirmation or a user-provided date.
- Keep someday/maybe rows sorted newest first by `Added` within the relevant section.
- If an existing someday/maybe table is missing `Added`, migrate the header for the table you edit and add best-known dates for existing rows when available; otherwise leave unknown existing dates blank and preserve their order below dated newer rows.

## Review workflows

Read `REVIEWS.md` when doing a review.

- Daily: H0 close loops, log completions, choose tomorrow's first move.
- Weekly: H0-H2 inbox zero, project list, next actions, waiting-for, areas touchpoint.
- Monthly: H2-H3 areas, goals, capacity, recurring friction, project alignment.
- Quarterly: H3-H5 goals, vision, principles, active commitments.

Weekly review success condition: every active project has a trusted next action or is paused/archived.

## Reset safety

Use for `/gwd-reset`.

1. Inspect root-level GWD files and folders before proposing changes.
2. Show exactly what will be archived, cleared, or deleted.
3. Prefer archive over delete: `archive/YYYY-MM-DD/`.
4. Require exact confirmation: `confirm gwd reset`.
5. If confirmation differs, do nothing.

## Response patterns

Start with the mode:

```text
Capture -> ...
Clarify -> ...
Refine -> ...
Plan -> ...
Review -> ...
Sweep -> ...
Align -> ...
Horizons -> ...
```

End with exactly one next prompt when interaction is needed:

- `Processar inbox agora?`
- `Qual item quer esclarecer?`
- `Qual ID quer refinar?`
- `Começar por qual ação?`
- `Continuar o sweep pelo próximo ramo?`
- `Quer alinhar esse projeto antes de ativar?`
- Confirmar com `confirm gwd reset`?

## References

- `TEMPLATES.md` for file and response templates.
- `REVIEWS.md` for review checklists and horizon review cadence.
- `EXAMPLES.md` for realistic PT-BR interactions.
