---
description: Turn knowledge gaps and untested assumptions into open, experience-grounded interview questions
argument-hint: "[optional: focus, e.g. pricing or driver identity]"
---

# Draft interview questions

## Input

Read **everything** in `00 Context/` (the brief, the brief interrogation and any other file there).
Also read `decision.log.md`, so the questions do not reopen settled decisions.

Also use my **space map** and **assumption list** if they exist:
- as a saved file anywhere in the project outside `01 Discover/` (e.g. a file with `Space-Map` or `Assumptions` in its name);
- or, if not saved, as output of `/space-map` or `/map-assumptions` earlier in this conversation.

Say which of the two you found and used. If neither exists, carry on with `00 Context/` only and say so.

Do **not** read or use anything in `01 Discover/` or later phase folders.
Also skip `00 Context/00_Discussion-Guide.md`: it was built from the interview transcripts (see D09), so it counts as interview data.

If `00 Context/` is empty, stop and tell me.
If something was given after the command ($ARGUMENTS), treat it as a focus: draft questions for that area only.

## Task

Turn the knowledge gaps (Unknowns) and untested assumptions into research questions I can bring into interviews.

Each question must:

1. **Target a specific unknown**, not confirm something I already believe. Cite what it targets (e.g. `U6`, `A5`).
2. **Be experience-grounded:** start from what the participant has actually done ("Tell me about the last time you…", "Walk me through…"), not opinions, hypotheticals or the future.
3. **Be impossible to answer yes or no.**

## Rules

- Draft first, then check every question against all three criteria.
- If a question fails check 1 or 2, fix it before showing it. Do not show the failed version.
- If a question fails **check 3 (yes/no)**, flag it with ⚑ and show the original next to the rewrite.
- No leading questions: do not name the problem, the feature or the answer you expect (e.g. not "How did the price make you feel ripped off?").
- One question per item. No double-barrelled questions ("…and why…").
- Use plain language a buyer would use, not design or industry jargon.
- Not every Unknown can be answered in an interview (e.g. how participants were recruited, quantitative data). List those under **Not for interviews** instead of forcing a question.
- Do not invent facts, participants or data that are not in the context files.

## Format

Reply in the chat only. Do not create a file.

Group the questions by theme (e.g. booking, pickup, payment after the trip), in the order an interview would flow.

```markdown
# Interview questions

Read: <files and sources used> · Date: <today>

## <Theme>
1. <question> · Targets: U6
2. <question> · Targets: A5, A9
3. ⚑ <rewritten question> · Targets: U8
   - Was: "<original yes/no question>"

## Not for interviews
- U9: <why an interview cannot answer it, and where to find out instead>

**Count:** n questions · n flagged and rewritten · n Unknowns/Assumptions with no question
```

## Output

1. Post the questions, the "Not for interviews" list and the count.
2. End with any Unknown or High-risk Assumption that no question covers yet.
