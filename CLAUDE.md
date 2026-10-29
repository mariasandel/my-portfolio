# Design OS

## Project structure

- `00 Context`: brief, research input and analysis of the brief
- `01 Discover`, `02 Define`, `03 Develop`, `04 Deliver`: one folder per Double Diamond phase
  - `01 Discover/Primary Research`: research with participants
    - `Raw`: interview transcripts, as recorded (`01_Transcript_<Name>.md`)
    - `Processed`: outputs built from the transcripts (e.g. `01_Observations_<Name>.md`, `01_Assumption-Check_<Name>.md`)
  - `01 Discover/Secondary Research`: desk research, e.g. alternatives and analogous domains (`01_Alternatives.md`)
  - `03 Develop/Inspiration`: look and feel reference images (`03_Inspo_<Subject>.ext`), described in `03 Develop/03_Moodboard_Look-And-Feel.md`
- When a subfolder is added, renamed or removed, update this list in the same turn.
- `.claude/commands`, `.claude/skills`: project commands and skills
- `project.log.md`: progress log: where we are, what happened, next step
- `decision.log.md`: settled decisions and why they were made

## Start of every session

1. Read `project.log.md` ("Where we are") to know where we stopped and what comes next.
2. Read `decision.log.md` so you do not undo or reopen settled choices.

## File naming rule

Every file in the phase folders (`00 Context` to `04 Deliver`) is named:

```
NN_Type_Subject.ext
```

The project name is never part of the file name: the whole repo is one project.

| Part | Meaning | Examples |
|------|---------|----------|
| `NN` | Number of the folder the file is in | `00`, `01`, `02`, `03`, `04` |
| `Type` | What kind of document it is | `Brief`, `Brief-Interrogation`, `Transcript`, `Problem-Statement`, `HMW`, `Design-Rationale` |
| `Subject` (optional) | The specific person or topic it is about. Leave it out when there is none (e.g. the brief) | `Lena`, `Pricing`, `Dairy-Check` |
| `_vN` (optional) | Version, only when an older version is kept | `_v2`, `_v3` |

Rules:

- **Underscore `_` separates the parts; hyphen `-` joins words inside a part.**
- Each word starts with a capital letter: `Brief-Interrogation`, not `brief interrogation`.
- Only letters, numbers, `-` and `_`. No spaces, accents or special characters (`á`, `&`, `?`, `#`...).
- English names, short and descriptive.
- No `final`, `new`, `copy` or dates in the name. Use `_v2`, `_v3` for versions.
- Extensions in lower case: `.md`, `.pdf`, `.png`.

Examples:

- `00_Brief.md`
- `01_Transcript_Lena.md`
- `02_Problem-Statement.md`
- `03_Wireframe-Flow_Booking_v2.png`

Exceptions (do not rename):

- The phase folders themselves (`00 Context`, `01 Discover`...).
- `CLAUDE.md`, `README.md`, `project.log.md`, `decision.log.md`.
- Everything in `.claude/`: command and skill names are lower case with hyphens (e.g. `brief-interrogate.md`), because the file name becomes the `/command` name.

## Applying the naming rule

- Always name new files with this rule.
- When you notice a file in the phase folders that does not follow the rule (for example one the user added), **do not rename it yourself**. Flag it and show the proposed rename, then ask the user before changing anything:

  ```
  ⚑ Naming: this file does not follow the project naming rule.
  Current:  01 Discover/interview notes lena.md
  Proposed: 01 Discover/01_Interview-Notes_Lena.md
  Rename it?
  ```

- Several files can be flagged together in one list, with one question.
- Only rename after the user agrees. Then check whether other files mention the old name and update those mentions too.
- If the right `Type` or `Subject` is unclear, propose your best option and say what you are unsure about.

## Creating commands and skills

Before creating a new command or skill, **always interrogate the user first**. Never write the file straight from the request, even when the request looks complete.

1. Read the related commands and skills, `README.md` and `decision.log.md`, so the questions build on what exists.
2. Ask, in one numbered list, only what the request does not already answer:
   - **Purpose:** what problem it solves, and when it should be used (trigger words).
   - **Type:** command (one step) or skill (asks questions first, produces the output only when asked).
   - **Input:** which files or folders it reads, and what it must not read (check D06, D09).
   - **Output:** what it produces, in what format and structure, and whether and where it is saved (file name per the naming rule).
   - **Rules and limits:** what it must always or never do, and what happens when an input is missing.
   - **Links:** which other commands or skills it calls or feeds (e.g. participant-tracker sync), and its phase in `README.md`.
3. Propose a short spec (name, type, input, output, steps) built from the answers, and wait for the user's go-ahead.
4. Only then create the file, add it to `README.md` and check consistency (D10).

The same applies when changing an existing command or skill in a way that changes its input, output or purpose. Small wording fixes do not need it.

## Logs: project log vs decision log

Two files, two jobs:

| | `project.log.md` | `decision.log.md` |
|---|---|---|
| Answers | Where are we, what happened, what is next? | What did we settle, and why? |
| Used for | Getting Claude up to speed: "continue from where we stopped" | Stopping Claude from undoing or reopening choices |
| Contains | "Where we are" status + one-line history | One entry per decision: decision, why, do not, status |
| Example | `- 2026-10-13 — Extracted observations for Lena.` | `D06 — Synthesis: Focus on hidden dairy` |

### Ask before logging

When something might be important, propose the entry at the end of your reply and ask the user. Only write it after they agree (they may edit the wording):

```
📝 Log this?
Project log:  - YYYY-MM-DD — what changed — because why.
Decision log: D06 — <Type>: <short title> (decision / why / do not)
```

- Propose a **project log** line for: a new research input, a finished phase output, progress on a step, a change to project structure or commands.
- Propose a **decision log** entry for: a choice about direction, scope, focus, method or project rules, especially when an option was rejected or something was removed on purpose.
- A decision usually gets both: the full entry in the decision log and a one-line mention (`see D06`) in the project log.
- Do not ask about routine edits, typo fixes or file reads.
- Several entries in one turn can be proposed together, with one question.
- If the user asks you to log something, add it directly.
- `/log-update` reviews the session and catches up on missing entries; `/consolidation-prompt` turns a decision from the conversation into a standalone note and logs it.

### Project log format

- Keep the **Where we are** section current: update it whenever an entry is added (phase, done, in progress, next step, open questions).
- History: one line at the bottom, `- YYYY-MM-DD — what changed — because why.` Only add lines; never edit or delete existing ones.

### Decision log format

```
### Dxx — <Type>: <short title> — YYYY-MM-DD

- **Decision:** what was decided, specific enough to act on.
- **Why:** the reason, with the evidence (research finding, constraint, user preference).
- **Do not:** what Claude must not do or reintroduce because of this decision.
- **Source:** the note or file it comes from (optional).
- **Status:** Active
```

- Types: `Scope`, `Research`, `Synthesis`, `Problem-Framing`, `Design-Direction`, `Process`.
- Never invent the **Why**. If it is unclear, write `?` and ask the user.
- Never delete or rewrite a decision. To change one, add a new entry with `Replaces: Dxx` and change the old one's status to `Replaced by Dyy`.

### Respecting decisions

- Before suggesting or making a change, check `decision.log.md`.
- If a request or your own idea goes against an Active decision, do not just do it. Point to the decision (e.g. "This reopens D03") and ask whether the user wants to replace it.
