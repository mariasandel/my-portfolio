# Process: 2026-10-14

**In one sentence:** Four pre-interview tools now prepare research from `00 Context/` only: the `space-map` skill and the commands `/map-assumptions`, `/plan-research` and `/draft-questions`. None of them reads `01 Discover/`.

## Context
Before working with the interview data, we built tools to map the problem space and prepare research using only the brief and the brief interrogation (`00 Context/00_Brief.md`, `00 Context/00_Brief-Interrogation.md`). Then we ran `/space-map`.

## Decision
- **`space-map` is a skill**, in `.claude/skills/space-map/SKILL.md`. It reads `00 Context/`, `decision.log.md` and `project.log.md`, then asks questions in six sections: Known, Unknown, Assumed, Domain boundaries, Stakeholders and Constraints. It does not produce the map until the user explicitly asks for it.
- **`/map-assumptions`** is a command in `.claude/commands/map-assumptions.md`. It lists every assumption in `00 Context/` and tags each one User, Problem, Context or Solution. It cites A1–A14 and marks the assumptions it adds as `New`.
- **`/plan-research`** is a command in `.claude/commands/plan-research.md`. The user gives it their constraints and it recommends 3–5 research methods, each with a one-line reason tied to a constraint. Methods that don't fit the timeline are excluded.
- **`/draft-questions`** is a command in `.claude/commands/draft-questions.md`. It turns Unknowns and Assumptions into interview questions that:
  - target a specific unknown
  - start from something the participant has actually done
  - can't be answered yes or no (questions that fail this are flagged ⚑ and rewritten)
- **None of the four reads `01 Discover/`** or the later phase folders.

## Why
- Skill instead of command for `space-map`: it is a multistep process (ask questions, wait for answers, follow up, then produce the map only on request).
- The name `/map-assumptions`: the user's preference.
- Ignoring `01 Discover/`: this framing should have happened earlier in the process, before the Discover information existed, so it must not be shaped by the interview data.

## Options considered
| Option | Outcome | Why |
|--------|---------|-----|
| `space-map` as a command in `.claude/commands/` | Rejected | It is multistep, so it belongs in a skill |
| Name `/extract-assumptions` | Rejected | Renamed to `/map-assumptions` at the user's request |
| Tools that read `01 Discover/` | Rejected | This step belongs before Discover; interview data would bias it |

## Consequences
- Don't turn `space-map` back into a command. Don't let these four tools read `01 Discover/`.
- **Next:** answer the 19 `/space-map` questions and the two tensions (independents vs chains; whether dietary safety is its own concern). Then ask for the map.

## Open questions
- All four tools reply in the chat only. That was Claude's default, not the user's decision. `/draft-questions` looks for a saved space map or assumption list. Should `space-map` and `/map-assumptions` save files to `00 Context/` (e.g. `00_Space-Map.md`, `00_Assumptions.md`)?
- The two tensions from `/space-map` are still unresolved.
