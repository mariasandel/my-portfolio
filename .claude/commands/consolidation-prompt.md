---
description: Summarise what we just decided as a standalone note, then save it and update both logs
argument-hint: "[optional: which decision or topic to consolidate]"
---

# Consolidation

## Input

Review this conversation, focusing on the most recent discussion.
If something was given after the command ($ARGUMENTS), consolidate only that decision or topic.
Read `project.log.md` and `decision.log.md` so you know what is already recorded.

## Task

Summarise what we have just decided. Write it as a clean, standalone note that includes everything needed to reconstruct the decision **without this conversation history**: someone (or a new Claude session) reading only this note must understand what was decided, why, and what follows.

## Rules

- Only include what was actually decided or said in the conversation. Do not invent decisions, reasons or evidence.
- If a reason or detail is missing, write `?` and ask me instead of guessing.
- Name files, research findings, participants and quotes specifically, so the decision is traceable.
- Record what was rejected and why: this is what stops the decision from being reopened later.
- If the decision goes against an Active entry in `decision.log.md`, say so and name the entry (e.g. "Replaces D03").

## Format

Title: `[Decision type]: [today's date]`. Decision type is one of `Scope`, `Research`, `Synthesis`, `Problem-Framing`, `Design-Direction`, `Process` (the same types as the decision log).

```markdown
# <Decision type>: <YYYY-MM-DD>

**In one sentence:** <the decision>

## Context
What we were working on and the question we had to answer.

## Decision
What we decided, specific enough to act on.

## Why
The reasons and the evidence (research findings, quotes with participant and turn, brief constraints).

## Options considered
| Option | Outcome | Why |
|--------|---------|-----|
| ... | Chosen / Rejected | ... |

## Consequences
What this changes, what we will do next, and what we must **not** do or reintroduce.

## Open questions
Anything still undecided (or "None").
```

## Output

Work in two steps. **Do not write any file before I approve.**

### Step 1: show me first

Show in the chat:

1. The full note.
2. The proposed log entries, in the format from `CLAUDE.md`:
   - **Decision log:** the most important decision from the note, as the next `Dxx` entry, with `Source:` pointing to the note file (or `conversation YYYY-MM-DD` if I choose not to save one).
   - **Project log:** one line ending `— see Dxx`, plus the updated **Where we are** section if it changes.
3. **Ask me directly whether to save the note as a document, and in which folder.** Do not decide this yourself. Always ask, even if the note seems minor:

   ```
   💾 Save this note as a document?
   - No, logs only
   - 00 Context  → 00_Decision_<Subject>.md
   - 01 Discover → 01_Decision_<Subject>.md
   - 02 Define   → 02_Decision_<Subject>.md
   - 03 Develop  → 03_Decision_<Subject>.md
   - 04 Deliver  → 04_Decision_<Subject>.md
   Recommended: <folder>, because <one short reason>.
   ```

   Fill in `<Subject>` with a short topic (e.g. `Problem-Focus`), following the naming rule in `CLAUDE.md` (Type `Decision`). I may also change the file name.

Then ask: approve, change, or drop any part of the note and log entries?

### Step 2: after I approve

1. If I chose a folder, save the note there with the `NN` of that folder (e.g. `02 Define/02_Decision_Problem-Focus.md`). If the file already exists, ask whether to overwrite it or save `_v2`. If I chose "No", save no note file.
2. Add the approved entries to `decision.log.md` and `project.log.md`, exactly as approved.
3. Confirm in one short line with links to the files you changed.
