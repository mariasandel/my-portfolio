---
description: Sharpen the discussion guide for one specific session, based on the participant's screener answers and open coverage gaps
argument-hint: "[participant's key screener answers] · [questions still open from previous sessions, or \"none — first session\"]"
---

# Calibrate the discussion guide

## Input

Read my discussion guide (`00 Context/00_Discussion-Guide.md`) and the project context in `00 Context/` (the brief, the brief interrogation, the assumptions, the space map and any other file there).
Also read `decision.log.md`, so the calibrated guide does not reopen settled decisions.

Do **not** read anything in `01 Discover/` or later phase folders (see D06). Transcripts and observations are not input here: open coverage gaps come from me.

What was given after the command ($ARGUMENTS) contains:

- **This participant's screener answers:** the key answers.
- **Questions still open from previous sessions:** a list, or "none — first session".

If no discussion guide exists, stop and tell me (it can be made with `/generate-guide`).
If $ARGUMENTS is empty, or the screener answers or the open questions are missing, ask me for them before doing anything else.

## Task

Sharpen the guide for this specific session. Prioritise questions that match this participant's profile and any open coverage gaps.

## Output

Return the revised guide only — no explanation needed.
