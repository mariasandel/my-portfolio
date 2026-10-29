---
description: Check a set of concepts for real diversity, flagging shared behaviour, user and moment, or mechanism, and drift from the lens or into UI, without ranking, selecting or replacing any concept
argument-hint: "[optional: folder with 03_Concepts.md. Default: 03 Develop]  — or paste the concepts as text"
---

# Audit concept diversity

## Input

1. **Folder:** if a folder was given in $ARGUMENTS, read from there and save there. If not, use `03 Develop`. Below, `<folder>` means that folder.
2. **Concepts:** read `<folder>/03_Concepts.md`.
   - If I pasted concepts as text instead, audit that text.
   - If the file does not exist and nothing was pasted, stop and ask me for the concepts.
3. **Fields:** each concept needs:
   - **ID** (C1, C2…). If a concept has none, number them in the order they appear and say so in the header.
   - **Lens**, and the lens definition if the file gives one
   - **User**
   - **Moment**
   - **Primary behaviour:** what the user does or is helped to do
   - **Mechanism:** how the concept makes that happen
   - If a field is missing, fill it from the concept text and mark it *(inferred)*. If it cannot be inferred, mark it "missing" and run every check that does not need it. List the checks skipped for that concept under Pairs checked.

Read only the concepts. Do not read the synthesis, the problem statements, the observation files, the transcripts or `00 Context`, and never use the Context Note or Raw Field Notes (D05).

## Checks

1. **Pairwise overlap.** Compare every pair of concepts on:
   - **Behaviour:** the same primary behaviour
   - **User and moment:** the same user **and** the same moment, both together
   - **Mechanism:** the same mechanism

   Flag a match as **⚑ Same**. Flag a near-match as **⚑ Close**, with a one-line reason (e.g. "show the ingredients" vs "list what is in the sauce").
2. **Lens drift:** the concept does not answer what its lens asks. Check against the lens definition when the file gives one, otherwise against the lens name, and say which in the header.
3. **UI drift:** the concept names screens, components, layouts, buttons or visual treatment instead of a behaviour or mechanism. A named channel (push notification, SMS, email) is flagged **⚑ Close** to UI drift, not a full UI drift flag.

With fewer than 2 concepts, run only checks 2 and 3 and say so.

## Rules

- **Flag only.** Do not rank, select, recommend, merge, replace or rewrite a concept. No alternative wording, not even for one phrase.
- Every drift flag quotes the exact phrase it applies to.
- Every pair flag appears in the rows of both concepts.
- No severity, overall verdict or pass/fail. Give counts only.
- Lens, user, moment, behaviour and mechanism are taken from the concepts as written. Do not correct them.

## Format

```markdown
# Concept Diversity Audit

Concepts: `<folder>/03_Concepts.md` (or "pasted") · Concepts: n · Lens checked against: definitions / names only · Date: <today>

Flags: Same n · Close n · Lens drift n · UI drift n

| Concept | Lens | Primary behaviour | Diversity flags |
|---------|------|-------------------|-----------------|
| C1. <short title> | <lens> | <behaviour> | ⚑ Same behaviour as C3 · ⚑ UI drift: "swipe-up card" |
| C2. <short title> | <lens> | <behaviour> *(inferred)* | ⚑ Close mechanism to C4: <reason> |
| C3. … | … | … | No flags |

## Pairs checked

- <n> pairs compared. Pairs with no flags: <C1–C2, C1–C4, …>
- <skipped checks per concept because of missing fields, if any>

What to keep or change is your call.
```

### File name

Follow the naming rule in `CLAUDE.md`: `03_Concept-Diversity-Audit.md`.

## Output

1. Before saving, check that every pair has been compared, every pair flag sits in both rows, every quoted phrase is really in the concept, and nothing ranks or rewrites a concept.
2. Save the file in `<folder>`. If it already exists, ask me whether to overwrite it or save a new version (`_v2`).
3. In the chat, reply with a short summary only: the flag counts, one line per flag, a link to the file, and "What to keep or change is your call."
