# Decision Log

Settled decisions and **why** they were made. Claude reads this before changing anything, so it does not undo or reopen these choices.
To change a decision, add a new entry that replaces it (`Replaces: Dxx`) and mark the old one `Status: Replaced by Dyy`. Never delete entries.

---

### D01 — Process: Commands and skills live in `.claude/` — 2026-10-13

- **Decision:** Project commands go in `.claude/commands/`, skills in `.claude/skills/`. The top-level `commands` and `skills` folders were removed.
- **Why:** Claude Code only reads commands and skills from inside `.claude/`; the top-level folders were ignored and confusing.
- **Do not:** Recreate `commands` or `skills` folders in the project root.
- **Status:** Active

### D02 — Process: File naming rule — 2026-10-13

- **Decision:** Files in the phase folders are named `NN_Type_Subject.ext` (Subject optional), e.g. `00_Brief.md`, `01_Transcript_Lena.md`. The project name is not part of file names. Full rule in `CLAUDE.md`.
- **Why:** Consistent, sortable names without spaces; the whole repo is one project, so repeating the project name adds nothing.
- **Do not:** Add the project name (e.g. `Pumpkin-Spice-Berlin`) back into file names.
- **Status:** Active

### D03 — Process: Ask before renaming files — 2026-10-13

- **Decision:** When a file breaks the naming rule, Claude flags it, shows the proposed new name and asks before renaming.
- **Why:** The user wants to see and approve every rename instead of Claude renaming files automatically.
- **Do not:** Rename files without asking (new files Claude creates are named with the rule directly).
- **Status:** Active

### D04 — Process: Ask before logging — 2026-10-13

- **Decision:** Claude proposes log entries and only writes them after the user agrees.
- **Why:** ? (reason not recorded, ask the user)
- **Do not:** Write to either log without approval, unless the user explicitly asks to log something.
- **Status:** Active

### D05 — Research: Observations come only from the Transcript section — 2026-10-13

- **Decision:** `/extract-observations` uses only the Transcript section of each interview, not the Context Note or Raw Field Notes.
- **Why:** The Context Note and Raw Field Notes are the researcher's interpretation, not what happened in the interview.
- **Do not:** Pull observations from the Context Note or Raw Field Notes.
- **Status:** Active

### D06 — Process: Pre-interview tools work from 00 Context only — 2026-10-14

- **Decision:** The commands `/map-assumptions`, `/plan-research` and `/draft-questions` read only `00 Context/` (plus the logs). They do not read `01 Discover/` or later phase folders.
- **Why:** Mapping assumptions, planning research and drafting questions belong earlier in the process, before the Discover information existed, so they must not be shaped by the interview data.
- **Do not:** Make these commands read `01 Discover/` or use the transcripts or observations.
- **Source:** `00 Context/00_Decision_Pre-Interview-Tools.md`
- **Status:** Active

### D07 — Process: Assumption list saved in 00 Context — 2026-10-14

- **Decision:** The output of /map-assumptions is saved as `00 Context/00_Assumptions.md`.
- **Why:** So /draft-questions and later sessions can use it without the conversation; it is built from the context only, before Discover (see D06).
- **Do not:** Move it to 01 Discover or rebuild it from interview data.
- **Source:** conversation 2026-10-14
- **Status:** Active

### D08 — Scope: Chains as context, dietary safety in scope; 2-week sprint, no deadline — 2026-10-14

- **Decision:** Chains (e.g. Starbucks) are research context and counter-evidence, not a design target: the service partners with independent cafés only. Dietary safety (dairy, vegan) is in scope as its own concern, alongside finding the drink and its price. The project is a 2-week sprint with no fixed deadline. Tools: Figma Make, Claude Design, Claude Code. Time: 1–2 days synthesis, 2–3 days prototyping.
- **Why:** Kiezkarte only works with independent cafés (brief), but buyers know the drink from chains, so chains shape their expectations (user, 2026-10-14). Dietary needs were listed only under one focus area, and the user wanted them treated as a concern of their own. Timeline: ?
- **Do not:** Design for chains or chain partnerships; treat dietary needs as a side note of "knowing what is in it"; plan against a fixed deadline.
- **Source:** conversation 2026-10-14
- **Status:** Active

### D09 — Process: Discussion guide built from the transcripts, saved in 00 Context — 2026-10-19

- **Decision:** The discussion guide (`00 Context/00_Discussion-Guide.md`) records the guide the four interviews actually followed. It was built from the transcripts in `01 Discover/Primary Research Raw`. It is saved in `00 Context`, where `/generate-guide` saves guides. Pre-interview material goes in `00 Context` directly, with no `Preparation` subfolder; the pre-interview tools decision note moved there too (`00 Context/00_Decision_Pre-Interview-Tools.md`).
- **Why:** The interviews had already happened, so the user chose to record the guide as it was used (user, 2026-10-19). `00 Context` is where `/generate-guide` saves the guide, so the guide and the tools stay in one place.
- **Do not:** Recreate `01 Discover/Preparation`. Let `/map-assumptions`, `/plan-research`, `/draft-questions`, `/write-screener`, `space-map` or `generate-guide` use the guide as input: it counts as interview data, so D06 still applies to them.
- **Source:** conversation 2026-10-19
- **Status:** Active (an exception to D06; D06 stays Active)

### D10 — Process: Keep the OS consistent across files — 2026-10-20

- **Decision:** Every new or changed command, skill or doc is checked against the other commands, skills, `CLAUDE.md`, `README.md` and this log. Paths, names and rules that must change with it are updated in the same turn. `CLAUDE.md` lists the phase subfolders. `README.md` indexes every command and skill by phase.
- **Why:** The project is a demo for the user's students (show & tells), so mismatches between files undermine it (user, 2026-10-20).
- **Do not:** Leave a tool, doc or log pointing to an old path, name or rule after a change. Add a command or skill without adding it to `README.md`.
- **Source:** conversation 2026-10-20
- **Status:** Active

### D11 — Synthesis: Two personas, split by what decides the purchase — 2026-10-21

- **Decision:** Two proto-personas: **Sam, Safety first** (from P03 Aiyana, P04 Jonas) and **Felix, Value first** (from P01 Lena, P02 Tobias). Tobias making the drink at home stays a note on Felix, not a third persona. The chain vs independent split is not a persona.
- **Why:** The divergence map shows one main split, "Can I drink it?" vs "Is it worth €6.50?", with two participants on each side. The secondary split (willingness to pay) follows it, and only one participant is on the chain side (`02 Define/02_Divergence-Map.md`).
- **Do not:** Add a third persona for Tobias or for chain buyers; give the personas age or job (not supported by the data).
- **Source:** `02 Define/02_Divergence-Map.md`, `02 Define/02_Personas.md`
- **Status:** Active

### D12 — Problem-Framing: PS1, reworded after the audit, is the selected problem statement — 2026-10-22

- **Decision:** The selected problem statement is PS1, reworded: "Buyers in Berlin can't find out whether a pumpkin spice latte is sold nearby, safe for them, or worth €6.50 until they are already at the counter. So they either give up or buy with doubt." Selected HMW: "How might we help buyers know what they are getting before they reach the counter?" Four success statements are in `02 Define/02_HMW-Success-Statements.md`.
- **Why:** The audit flagged PS1's "know what is in it" as vague (flag 2), the dropped dairy-free group (flag 6) and the "nobody can tell them" solution lean (flag 1). The rewording names the three things buyers need to know, so it covers both personas. PS1, PS3 and PS4 overlapped (similarity check), so choosing among them added nothing. PS5 rests on one participant.
- **Do not:** Reopen PS2–PS5 or re-run the framing without a new decision; narrow the problem to ingredients only.
- **Source:** `02 Define/02_Problem-Statements.md`, `02 Define/02_Problem-Statement-Audit_PS1.md`
- **Status:** Active

### D13 — Process: 01 Discover is split into Primary and Secondary Research — 2026-10-27

- **Decision:** Transcripts go in `01 Discover/Primary Research/Raw`, outputs built from them (observations, assumption checks) in `01 Discover/Primary Research/Processed`, and desk research (alternatives, analogous domains) in `01 Discover/Secondary Research`. The paths named in D09 and in older project log lines (`01 Discover/Primary Research Raw`, `01 Discover/Processed`) are out of date and follow this structure.
- **Why:** Primary and secondary research are both Discover-phase work, so they belong together, even when secondary research later feeds concept generation (user, 2026-10-27).
- **Do not:** Recreate `01 Discover/Primary Research Raw` or `01 Discover/Processed`; save secondary research in `03 Develop`.
- **Source:** conversation 2026-10-27
- **Status:** Active
