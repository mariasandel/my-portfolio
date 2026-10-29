---
description: Recommend research methods for the project that fit my constraints and timeline
argument-hint: "<my constraints, e.g. 5 interviews max, 2 weeks, no incentive budget, hard to recruit because X>"
---

# Plan research

## Input

Read **everything** in `00 Context/` (the brief, the brief interrogation and any other file there).
Also read `decision.log.md`, so the plan does not reopen settled decisions.

Do **not** read or use anything in `01 Discover/` or later phase folders.
Also skip `00 Context/00_Discussion-Guide.md`: it was built from the interview transcripts (see D09), so it counts as interview data.

If `00 Context/` is empty, stop and tell me.

### My constraints

My constraints are given after the command ($ARGUMENTS), e.g. "5 interviews max, 2 weeks total, no budget for incentives, participants are hard to recruit because X".

- If nothing was given, ask me for my constraints (time, number of participants, budget, recruitment, access, tools) with one example, and stop.
- Also take any constraints stated in the context files (deadline, deliverables, scope). If they conflict with mine, say so and ask which applies before recommending.

## Task

Help me plan the research phase for this project. Recommend the research methods that fit best.

- For each method, give a **one-line reason tied to my specific constraints** (name the constraint).
- Link each method to the Unknowns or Assumptions from `00_Brief-Interrogation.md` it helps answer or test (e.g. `U5`, `A5`).
- **Exclude anything that does not fit the timeline.** Do not recommend it, not even as optional.

## Rules

- Recommend only methods that fit every stated constraint. If a method only fits with a change (e.g. fewer participants), say what changes.
- Prefer few methods that work together over a long menu. 3–5 recommendations at most.
- Order the methods by priority: the one that answers the most important Unknowns first.
- Reasons must be specific to this project and these constraints, not generic method descriptions.
- Do not invent constraints, participants or data that are not in the context files or my input.

## Format

Reply in the chat only. Do not create a file.

```markdown
# Research plan: methods

Read: <list of files read> · Date: <today>
Constraints: <my constraints, plus any taken from the context files>

| # | Method | Reason (tied to constraint) | Answers |
|---|--------|-----------------------------|---------|
| 1 | <method> | <one line, naming the constraint> | U5, A7 |

**Excluded (does not fit the timeline):** <method> (<few words why>), <method> (<few words why>)

**Not covered:** <important Unknowns or Assumptions none of the methods address, if any>
```

## Output

Post the table and the excluded and not-covered lines. Keep the reply short; no method explanations beyond the one-line reason.
