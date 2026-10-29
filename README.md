# Design OS

A working system for running a design project with Claude Code along the Double Diamond. It has a folder per phase, project commands and skills that do the repeatable steps, and two logs. The logs let Claude pick up where you stopped without undoing settled choices.

Current project: **Buying a Pumpkin Spice Latte in Berlin** (for Kiezkarte: finding it, knowing what is in it, and whether it is worth the price).

## Folders

| Folder | What goes in it |
|--------|-----------------|
| `00 Context` | Brief and everything prepared before interviewing: brief interrogation, assumptions, research questions, space map, desk research plan, discussion guide, decision notes |
| `01 Discover` | Research. `Primary Research/Raw`: transcripts · `Primary Research/Processed`: observations and assumption checks · `Secondary Research`: desk research (alternatives, analogous domains) |
| `02 Define` | Synthesis, need statement, problem framing, divergence map, personas, HMW and success statements |
| `03 Develop` | Concept inputs (platform constraints), concepts, prototypes, moodboard. `Inspiration`: look and feel reference images |
| `04 Deliver` | Final outputs |
| `.claude/commands`, `.claude/skills` | The tools below |

Files are named `NN_Type_Subject.ext`, e.g. `01_Transcript_Lena.md`. The full rule is in `CLAUDE.md`.

## Logs

- `project.log.md`: where we are, what happened, what comes next. Start a session with: "Read the project log and continue from where we stopped."
- `decision.log.md`: settled decisions (D01, D02…) and why they were made. Claude checks it before changing anything.

Claude proposes log entries and writes them only after you agree.

## Tools by phase

Commands run in one step. Skills are multistep: they ask questions first and produce the output only when you ask.

To add a new command or skill, just ask Claude: it interrogates you first (purpose, input, output, rules) and proposes a spec before creating anything. The full rule is in `CLAUDE.md`.

### 00 Context: before interviewing

| Tool | Type | What it does |
|------|------|--------------|
| `/setup-project-context` | Skill | Asks what is needed to write a lean project context block |
| `/brief-interrogate` | Command | Lists the brief's Knowns, Unknowns and Assumptions |
| `/map-assumptions` | Command | Tags every assumption as user, problem, context or solution |
| `/space-map` | Skill | Builds the problem space map (known, unknown, assumed, boundaries, stakeholders, constraints) |
| `/scope-research` | Command | Writes the desk research plan for secondary research (what to look for, where, how to judge a source) from the research questions; saves `00_Desk-Research-Plan.md` and never does the research |
| `/plan-research` | Command | Recommends research methods that fit your constraints |
| `/draft-questions` | Command | Turns gaps and assumptions into open, experience-grounded interview questions |
| `/write-screener` | Command | Writes a recruitment screener with accept / borderline / reject logic |
| `/generate-guide` | Skill | Writes the interview discussion guide |
| `/calibrate-guide` | Command | Sharpens the guide for one session, from the participant's screener answers and open gaps |

These tools read `00 Context/` only, never the interview data (D06). The one exception is the discussion guide in this project, which was built from the transcripts (D09).

### 01 Discover

| Tool | Type | What it does |
|------|------|--------------|
| `/participant-tracker` | Skill | Creates and syncs the participant tracker (markdown + Google Sheet) |
| `/extract-observations` | Command | Extracts observations from one transcript, each tagged S (Supported), W (Weak) or I (Invented) |
| `/flag-assumptions` | Command | Marks every assumption Held, Challenged or Open against one session's observations |
| `/review-observations` | Skill | Opens a review page: observations beside the highlighted transcript. Approve, reject, retag S/W/I and comment, then sync to the files. Extracts missing lists in parallel first; unfinished reviews are flagged and can be continued |
| `/send-observations` | Skill | Sends the approved S/W observations to FigJam as stickies grouped by participant (S green with quote, W yellow, I and unapproved never sent) |

### 02 Define

| Tool | Type | What it does |
|------|------|--------------|
| `/frame-problem` | Command | Writes 3–5 distinct problem statements (different user, moment, root cause) from the need statement and confirmed themes, each with an evidence score; flags pairs that are too similar and never picks one |
| `/audit-problem-statement` | Command | Audits the statement you selected against its frame in the `/frame-problem` output: solution bias, unsupported assumptions, vague needs, weak research connections. Returns a flagged list and never rewrites the statement |
| `/frame-and-audit` | Skill | Runs `/frame-problem` five times in parallel, one lens each (frequency, underserved segment, need statement, outcome, outlier), flags overlap, saves PS1–PS5 with a comparison table, asks which one to audit, then runs `/audit-problem-statement` on your pick |

### 03 Develop

| Tool | Type | What it does |
|------|------|--------------|
| `/audit-concept-diversity` | Command | Checks a set of concepts (`03_Concepts.md`) for real diversity: flags pairs with the same primary behaviour, user and moment, or mechanism (⚑ Same / ⚑ Close), and concepts that drift from their lens or into UI. Returns a table and never ranks, selects or replaces a concept |

### Any time

| Tool | Type | What it does |
|------|------|--------------|
| `/log-update` | Command | Reviews the session and proposes missing log entries |
| `/consolidation-prompt` | Command | Turns a decision from the conversation into a standalone note and logs it |
| `/clean-design-os` | Skill | At the end of a project, sorts everything into reusable, archive or unsure |
