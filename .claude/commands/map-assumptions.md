---
description: Extract every assumption in 00 Context and tag it as user, problem, context or solution direction
argument-hint: "[optional: extra focus, e.g. pricing]"
---

# Extract assumptions

## Input

Read **everything** in `00 Context/` (the brief, the brief interrogation and any other file there).
Also read `decision.log.md`, so settled decisions are not listed as open assumptions.

Do **not** read or use anything in `01 Discover/` or later phase folders.
Also skip `00 Context/00_Discussion-Guide.md`: it was built from the interview transcripts (see D09), so it counts as interview data.

If `00 Context/` is empty, stop and tell me.
If something was given after the command ($ARGUMENTS), treat it as an extra focus, but still list every assumption.

## Task

Extract every assumption I am making: about who the user is, what the problem is, how the context works, and whether a solution direction has already leaked in.

An assumption is anything treated as true that is not confirmed by evidence in the context files. It can be stated outright, implied by wording, or built into what is included or left out.

Tag each assumption with one category:

- **User:** who the user is, what they want, know, do or feel.
- **Problem:** what the problem is, where it sits, how big it is, what causes it.
- **Context:** how the domain, the market, the client, the research or the project setup works.
- **Solution:** a solution direction that has already leaked in (e.g. "more information will fix it", "it is a screen problem", a feature or flow already implied).

## Rules

- Include the assumptions already listed in `00_Brief-Interrogation.md` and cite their ID (e.g. `A5`). Add the ones it missed and mark them `New`.
- Every assumption includes **where it comes from**: a short exact quote from the file, or a note on what is implied or left out.
- One assumption per item. Do not merge two into one.
- If an assumption fits two categories, pick the main one and name the second in brackets.
- Look hard for **Solution** leaks: wording in the brief, the suggested focus areas, the constraints or my own notes that already points to an answer.
- Do not judge whether an assumption is true. Only name it.
- Do not invent facts that are not in the context files.

## Format

Reply in the chat only. Do not create a file.

```markdown
# Assumptions: 00 Context

Read: <list of files read> · Date: <today>

1. **[User]** <assumption> · `A7`
   - From: "<exact quote>" (<file>)
2. **[Solution]** <assumption> · `New`
   - From: implied by <what>
3. **[Problem] (also Solution)** <assumption> · `A2`
   - From: "<exact quote>" (<file>)

**Count:** User n · Problem n · Context n · Solution n · New n
```

Order the list by category: User, Problem, Context, Solution.

## Output

1. Post the numbered list and the count.
2. End with the Solution leaks in one short line each, since those are the ones most likely to bias the interviews.
