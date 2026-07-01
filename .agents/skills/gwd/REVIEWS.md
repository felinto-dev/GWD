# GWD Reviews

Reviews keep the system trusted. They are not bureaucracy; they are how you regain control and perspective.

Before reading full review files, use `scripts/gwd-query review --root . --type <daily|weekly|monthly|quarterly>` and `scripts/gwd-query horizons --root .` for compact summaries.

## The review stack

```text
                 PERSPECTIVE

        +--------------------------------+
        | H5 Purpose + Principles        |  Quarterly / when life feels off
        +--------------------------------+
        | H4 Vision 3-5 years            |  Quarterly
        +--------------------------------+
        | H3 Goals 3 months-2 years      |  Monthly + quarterly
        +--------------------------------+
        | H2 Areas of Focus              |  Weekly touchpoint + monthly
        +--------------------------------+
        | H1 Projects                    |  Weekly
        +--------------------------------+
        | H0 Next Actions                |  Daily + weekly
        +--------------------------------+

                   CONTROL
```

Bottom-up is the default review path:

```text
H0 Actions -> H1 Projects -> H2 Areas -> H3 Goals -> H4 Vision -> H5 Purpose
```

Why: if the base is noisy, high-level thinking gets distorted by anxiety. Clear open loops first, then decide what matters.

## Command map

| Review | Main command | Horizons | Goal |
|---|---|---|---|
| Daily | `/gwd-review daily` | H0 | Close loops and choose tomorrow's first move |
| Weekly | `/gwd-weekly` | H0-H2 | Restore control and ensure each project has a next action |
| Monthly | `/gwd-review monthly` | H2-H3 | Check areas, goals, capacity, and project alignment |
| Quarterly | `/gwd-review quarterly` | H3-H5 | Check direction, vision, principles, and commitments |
| Full map | `/gwd-horizons` | H0-H5 | Show the whole pyramid and gaps |
| Alignment | `/gwd-align` | H0-H5 | Test whether work fits the higher horizons |

## Daily review

Use at shutdown or `/gwd-review daily`.

Focus: H0 next actions.

```text
+------------------+
| DAILY SHUTDOWN   |
+------------------+
| 1. What got done?|
| 2. What remains? |
| 3. What is loose?|
| 4. First move?   |
+------------------+
```

Checklist:

1. Check today's `daily/YYYY-MM-DD.md` plan and log.
2. Mark completed actions.
3. Move unfinished actions to `next-actions.md`, tomorrow, `waiting-for.md`, or `someday-maybe.md`.
4. Capture loose thoughts into `inbox.md`.
5. Choose tomorrow's first move.

Template:

```markdown
Review -> daily

Done:
- ...

Carry:
- ... -> destination

Loose loops captured:
- ...

Tomorrow first move: ...
```

Good daily review outcome:

```text
You know what is done, what is not done, and where tomorrow starts.
```

## Weekly review

Use `/gwd-weekly` or `/gwd-review weekly`.

Focus: H0-H2.

```text
             WEEKLY REVIEW

  inbox.md          -> empty or clarified
  next-actions.md   -> current and executable
  projects.md       -> every active project has next action
  waiting-for.md    -> follow-ups visible
  areas.md          -> nothing important neglected
```

Checklist:

1. Get clear:
   - Process `inbox.md` to zero or mark blockers.
   - Empty loose notes from the week.
2. Get current:
   - Review `calendar.md` past 7 days and next 14 days.
   - Review `waiting-for.md` and create follow-ups.
   - Review `next-actions.md` by context.
3. Review projects:
   - Every active project has a clear outcome.
   - Every active project has at least one next action.
   - Paused/stale projects are marked paused, waiting, someday, or archived.
4. Review areas:
   - Scan `areas.md` for neglected responsibilities.
   - Create projects or next actions only when needed.
5. Review someday lightly:
   - Promote, keep, or ignore. Delete only after confirmation.
6. Choose next week focus:
   - 1 main outcome.
   - 2-3 supporting outcomes.
   - First action.

Template:

```markdown
Review -> weekly

Inbox: N -> N
Projects reviewed: N
Projects missing next action: N
Waiting-for follow-ups: N
Areas needing attention: N
Someday promoted: N

Next week focus: ...
Top 3 outcomes:
1. ...
2. ...
3. ...

First action: ...
```

Weekly pass/fail rule:

```text
PASS: every active project has a trusted next action.
FAIL: project exists but no next visible action exists.
```

## Monthly review

Use `/gwd-review monthly`.

Focus: H2-H3.

```text
            MONTHLY REVIEW

       areas.md  <---->  goals.md
          |                 |
          v                 v
      projects.md  --->  /gwd-align
```

Purpose: make sure the month reflects responsibilities and goals, not just urgency.

Checklist:

1. Review `areas.md`:
   - Which area is under-maintained?
   - Which area has too many active projects?
   - Which standard is unclear?
2. Review `goals.md`:
   - Which goals moved?
   - Which goals are stale?
   - Which goals need projects?
3. Review `gwd-memory.md` when it exists:
   - Check active memories before planning the next month.
   - For each `Esquecer em`, decide whether the condition has been reached.
   - Remove or archive expired memories only after confirmation; keep valid memories unchanged.
4. Run alignment:
   - Use `/gwd-align all` or align top active projects.
   - Move weakly aligned projects to paused/someday when appropriate.
5. Check capacity:
   - Time, energy, money, attention.
   - Reduce active load if reality changed.
6. Decide next month:
   - 1-3 goals/outcomes.
   - Projects to continue, pause, start, stop.

Template:

```markdown
Review -> monthly

Areas needing attention:
- ...

Goals status:
- on track: ...
- at risk: ...
- stale: ...

Memory expiry:
- keep: ...
- archive/remove after confirmation: ...

Alignment findings:
- aligned: ...
- weak: ...
- conflict: ...

Start:
- ...

Stop/Pause:
- ...

Month focus: ...
```

Good monthly review outcome:

```text
Your active projects match your current responsibilities and goals.
```

After monthly review:

- Archive the review under `reviews/monthly/YYYY-MM.md`.
- Refresh `projects.md` if project statuses or next actions changed.
- Refresh `horizons.md` from canonical files.

## Quarterly review

Use `/gwd-review quarterly`.

Focus: H3-H5.

```text
          QUARTERLY REVIEW

  H5 purpose.md  ->  H4 vision.md  ->  H3 goals.md
         |                |                |
         v                v                v
      principles       direction        commitments
```

Purpose: confirm the direction before optimizing execution.

Checklist:

1. Review `purpose.md`:
   - Are the principles still true?
   - What did the last quarter reveal about values?
   - What success cost too much?
2. Review `vision.md`:
   - Is the 3-5 year picture still desirable?
   - What external changes matter?
   - Which lifestyle/career assumptions changed?
3. Review `goals.md`:
   - Which goals should continue, change, or end?
   - Which new goals are required by the vision?
4. Simplify commitments:
   - Which projects no longer belong?
   - Which areas are overloaded?
   - Which active work conflicts with principles?
5. Choose next quarter:
   - 1 main theme.
   - 3-5 goals or outcomes max.
   - Active project limits.

Template:

```markdown
Review -> quarterly

Purpose/principles:
- keep: ...
- refine: ...

Vision:
- still true: ...
- changed: ...

Goals:
- continue: ...
- change: ...
- stop: ...

Commitment cleanup:
- archive: ...
- pause: ...
- move to someday: ...

Quarter theme: ...
Operating rule: ...
```

Good quarterly review outcome:

```text
Your goals and active commitments serve the life you are trying to build.
```

After quarterly review:

- Archive the review under `reviews/quarterly/YYYY-QN.md`.
- Refresh `goals.md`, `vision.md`, or `purpose.md` if decisions changed.
- Refresh `projects.md` if commitments were paused/archived.
- Refresh `horizons.md` from canonical files.

## Horizons review

Use `/gwd-horizons` when the user asks for the whole picture.

Update `horizons.md` whenever `/gwd-horizons` runs. Treat it as derived: generate the snapshot from canonical files with `scripts/gwd-query horizons --root . --format md`, then preserve any user-written notes that should not be regenerated.

```text
Horizons -> snapshot

H5 Purpose  : clear | fuzzy | missing
H4 Vision   : clear | fuzzy | missing
H3 Goals    : clear | overloaded | missing
H2 Areas    : balanced | neglected | overloaded
H1 Projects : current | stale | overloaded
H0 Actions  : clear | noisy | missing
```

Recommended output:

```markdown
Horizons -> snapshot

H5 Purpose  : fuzzy
H4 Vision   : missing
H3 Goals    : overloaded
H2 Areas    : health neglected
H1 Projects : 4 missing next action
H0 Actions  : clear

Gaps:
- Vision missing; goals may be reactive.
- Health area has no project or recurring action.
- 4 active projects lack next action.

Recommended next command: `/gwd-weekly` first, then `/gwd-vision`.
```

## Alignment review

Use `/gwd-align` manually or automatically during project creation, monthly review, and quarterly review.

Alignment chain:

```text
H0 Action
  -> H1 Project
    -> H2 Area
      -> H3 Goal
        -> H4 Vision
          -> H5 Principle
```

Status meanings:

| Status | Meaning | Likely action |
|---|---|---|
| aligned | Chain is clear enough | Keep moving |
| weak alignment | Some link is missing or vague | Clarify or downgrade |
| conflict | Work violates a higher choice | Pause, redesign, or stop |
| unknown | Not enough data | Ask or inspect references |

Template:

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

## Review cadence rules

```text
Daily       -> H0
Weekly      -> H0 + H1 + H2
Monthly     -> H2 + H3 + alignment
Quarterly   -> H3 + H4 + H5
As needed   -> any horizon causing friction
```

If the user is overwhelmed, do not start with purpose. Start with the thing occupying attention now.

```text
Clear the runway first. Then climb.
```
