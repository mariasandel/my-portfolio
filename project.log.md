# Project Log

What happened and where we are. Start a session with: "Read the project log and continue from where we stopped."
Decisions and their reasons are in `decision.log.md`.

## Where we are

_Updated: 2026-10-29_

- **Phase:** 03 Develop (concept generation)
- **Done:**
  - **00 Context:** brief saved (`00 Context/00_Brief.md`) and interrogated (`00 Context/00_Brief-Interrogation.md`). Assumptions mapped (`00 Context/00_Assumptions.md`). Discussion guide built from the transcripts (`00 Context/00_Discussion-Guide.md`, see D09).
  - **01 Discover:** four raw transcripts in `01 Discover/Primary Research/Raw` (Lena, Tobias, Aiyana, Jonas). Observations extracted for all four in `01 Discover/Primary Research/Processed`. Secondary research: alternatives and analogous domains (`01 Discover/Secondary Research/01_Alternatives.md`).
  - **02 Define:** synthesis (`02_Synthesis.md`: 3 themes, 5 confirmed clusters, 1 parked). Need statement (`02_Need-Statement.md`). Five framings PS1–PS5 with `/frame-and-audit` (`02_Problem-Statements.md`), PS1 audited (`02_Problem-Statement-Audit_PS1.md`). Divergence map and two proto-personas, Sam (Safety first) and Felix (Value first) (`02_Divergence-Map.md`, `02_Personas.md`, see D11). Selected problem statement, HMW and success statements (`02_HMW-Success-Statements.md`, see D12).
  - **03 Develop:** concept input ready: platform constraints from Kiezkarte (`03_Platform-Constraints.md`). Early mobile prototype (`03_Prototype_Mobile.html`): 4 screens (setup, on your way, drink detail, season alerts) with an evidence layer; a probe built before concept generation, not the chosen concept. Moodboard for look and feel (`03_Moodboard_Look-And-Feel.md`, images in `Inspiration/`): pumpkin, peach-honey and apricot set the colours and branding; not applied to the prototype yet.
- **Pre-interview tools:** `/map-assumptions`, `/plan-research`, `/draft-questions`, `/write-screener`, `space-map` and `generate-guide` work from `00 Context/` only and skip the discussion guide (D06, D09). `/calibrate-guide` sharpens the guide for one session.
- **OS:** `README.md` indexes every command and skill by phase; `CLAUDE.md` lists the phase subfolders. Keep both in step with every change (D10). `/audit-concept-diversity` is ready for 03 Develop; it reads `03 Develop/03_Concepts.md`, which no tool writes yet.
- **In progress:** Problem space map (`/space-map`): questions saved in `00 Context/00_Space-Map.md`, questions 1–16 not answered yet.
- **Next step:** Generate concepts from the selected HMW, the two personas, the platform constraints and the alternatives (`01 Discover/Secondary Research`), saved as `03 Develop/03_Concepts.md` (a `generate-concepts` skill is being built for this). Then check them with `/audit-concept-diversity`.
- **Open questions:** Do people with dietary needs skip seasonal drinks altogether, or just ask? (open question from the synthesis). Reason for the 2-week sprint / no deadline (D08 Why: ?). Reason for ask-before-logging (D04 Why: ?).

## History

Newest at the bottom. One line per entry; never edit or delete existing lines.

- 2026-10-13 — Brief from Kiezkarte saved as `00 Context/00_Brief.md` and interrogated with `/brief-interrogate` (`00 Context/00_Brief-Interrogation.md`).
- 2026-10-13 — Naming rule changed: project name dropped from file names, Subject is now optional (e.g. `00_Brief.md`, `01_Transcript_Lena.md`); brief files renamed and `/brief-interrogate` updated.
- 2026-10-13 — Added `project.log.md` to record important decisions and changes.
- 2026-10-13 — Project log changed to ask-first: Claude proposes entries and only logs them after the user agrees.
- 2026-10-13 — Added `/log-update` command to review the session and catch up on missing log entries on demand.
- 2026-10-13 — Split logging into `project.log.md` (progress, where we stopped) and `decision.log.md` (settled decisions D01–D05 with reasons); added `/consolidation-prompt` — so Claude can resume work and does not undo settled choices.
- 2026-10-14 — Added /map-assumptions, /plan-research and /draft-questions commands to prepare research from 00 Context only, before the Discover data — see D06.
- 2026-10-14 — Mapped assumptions in 00 Context (22, of which 15 new and 4 solution leaks) and saved them as 00 Context/00_Assumptions.md — see D07.
- 2026-10-14 — Chains set as context only, dietary safety in scope; 2-week sprint, no deadline; tools and time budget set — see D08.
- 2026-10-14 — `/space-map` questions saved in `00 Context/00_Space-Map.md`; constraints and both tensions answered, questions 1–16 still open.
- 2026-10-18 — Interviewed four participants (P01 Lena, P02 Tobias on 16 Oct, P03 Aiyana on 17 Oct, P04 Jonas on 18 Oct); raw transcripts saved in `01 Discover/Primary Research Raw`.
- 2026-10-19 — Observations extracted for all four participants and saved in `01 Discover/Processed` (Lena 20, Tobias 22, Aiyana 21, Jonas 16).
- 2026-10-19 — Added `/calibrate-guide` command to sharpen the discussion guide per session from screener answers and open coverage gaps.
- 2026-10-19 — Discussion guide built from the four transcripts and saved as `00 Context/00_Discussion-Guide.md`; pre-interview tools now skip it; decision note kept in `00 Context/00_Decision_Pre-Interview-Tools.md` — see D09.
- 2026-10-20 — `README.md` rewritten as an index of folders, logs and tools by phase; `CLAUDE.md` now lists the phase subfolders — so the OS stays consistent for the student demo — see D10.
- 2026-10-20 — Synthesis done: 26 observations on the board, 6 clusters in 3 themes (Finding it, Not knowing what's in it, Is it worth it?), 5 confirmed, C2 "Tastes like home" parked; saved as `02 Define/02_Synthesis.md`.
- 2026-10-20 — Need statement written from the confirmed themes and insights (`02 Define/02_Need-Statement.md`).
- 2026-10-21 — Ran `/frame-and-audit`: five framings saved as PS1–PS5 (`02 Define/02_Problem-Statements.md`); PS1, PS3 and PS4 flagged as too similar; PS1 audited (0 high, 3 medium, 3 low flags) in `02 Define/02_Problem-Statement-Audit_PS1.md`.
- 2026-10-21 — Divergence map and two proto-personas saved (`02 Define/02_Divergence-Map.md`, `02 Define/02_Personas.md`) — see D11.
- 2026-10-22 — PS1 reworded after the audit and selected, with HMW and four success statements (`02 Define/02_HMW-Success-Statements.md`) — see D12.
- 2026-10-22 — Added /audit-concept-diversity command (03 Develop) to flag concepts that share behaviour, user and moment, or mechanism, or drift from their lens or into UI; flag only, standalone for now.
- 2026-10-23 — Concept inputs saved in `03 Develop`: platform constraints from Kiezkarte (`03_Platform-Constraints.md`) and alternatives and analogous domains (`03_Alternatives.md`) — so concepts can be generated next.
- 2026-10-27 — Restructured 01 Discover into Primary Research (Raw, Processed) and Secondary Research; alternatives moved from 03 Develop to `01 Discover/Secondary Research/01_Alternatives.md`; all tools and docs updated — see D13.
- 2026-10-29 — Early mobile prototype built from the observations, HMW, personas and platform constraints (4 screens, evidence layer) and saved as `03 Develop/03_Prototype_Mobile.html` — as a probe before concept generation.
- 2026-10-29 — Moodboard saved: 9 inspiration images in `03 Develop/Inspiration` and notes in `03 Develop/03_Moodboard_Look-And-Feel.md` (pumpkin, peach-honey and apricot set the colours and branding) — as look and feel input for the prototype.
