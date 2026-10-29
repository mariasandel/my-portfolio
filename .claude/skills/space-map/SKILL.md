---
name: space-map
description: Read everything in 00 Context and ask the questions needed to build a problem space map (known, unknown, assumed, domain boundaries, stakeholders, constraints) before interviewing. Uses the Unknowns and Assumptions from the brief interrogation. Asks first; produces the map only when asked, and saves the output to 00 Context/00_Space-Map.md when asked. Use when the user wants to map the problem space, prepare for interviews, or asks for a space map.
argument-hint: "[optional: extra focus or note for the questions]"
---

# Problem space map: questions first

## Input

Read **everything** in `00 Context/` (the brief, the brief interrogation and any other file there).
Also read `decision.log.md` and the "Where we are" section of `project.log.md`, so you do not ask about choices that are already settled. Use the open questions there as input.

From `00 Context/00_Brief-Interrogation.md`, take:
- the **Unknowns** (U1, U2…): what I still do not understand about this domain;
- the **Assumptions** (A1, A2…): what I suspect but cannot confirm.

Do **not** read or use anything in `01 Discover/` or later phase folders. The map is built from the context only, before interviewing.
Also skip `00 Context/00_Discussion-Guide.md`: it was built from the interview transcripts (see D09), so it counts as interview data.

If `00 Context/` is empty or the brief interrogation is missing, stop and tell me. Suggest running `/brief-interrogate` first.

If something was given after the command ($ARGUMENTS), treat it as an extra focus for the questions.

## Task

I want a structured map of this problem space before I start interviewing. **Do not produce the map yet.** Only ask me the questions you need to build a complete map with six sections:

1. **Known:** what is confirmed (brief + what I already know about the domain)
2. **Unknown:** what nobody on the project knows yet
3. **Assumed:** what I believe but cannot confirm
4. **Domain boundaries:** what is inside and outside the problem space
5. **Stakeholders:** who is affected, who decides, who influences trust
6. **Constraints:** time, scope, platform, tools, access, assessment

## Rules for the questions

- Ask only what the context files cannot answer. Do not ask about anything already stated as a Known in the brief interrogation.
- Do not ask me questions that only the interviews can answer (e.g. "why do buyers walk away?"). Those stay Unknowns. Instead, ask what **I** know, believe or have decided about them.
- Use the Unknowns and Assumptions to drive the questions: for each important one, ask whether I can already answer it, how confident I am, or where I would find out. Cite the reference (e.g. `U3`, `A5`) next to the question.
- Look for tensions or gaps between files (e.g. brief says "pricing and driver identity" but the research theme says "pricing and safety") and ask me to resolve them.
- Ask about my own position too: my own experience with the product or service and with its alternatives, my hunches, and what would surprise me.
- One thing per question. Keep each question short and concrete; say in a few words why you need it when that is not obvious.
- Prefer questions that sort things into a map section over open-ended discussion questions.
- Do not repeat questions about settled decisions in `decision.log.md`.
- Ask 3–5 questions per section, about 20–25 in total. Leave out a section's questions only if the context already covers it fully, and say so.

## Format

Reply in the chat. Create a file only in the Save step below.

```markdown
# Space map: questions

Read: <list of files read> · Date: <today>

Answer by number. "Don't know" is a useful answer: it goes into Unknowns.

## 1. Known
1. <question> (ref: K/U/A number if any)
2. ...

## 2. Unknown
...

## 3. Assumed
...

## 4. Domain boundaries
...

## 5. Stakeholders
...

## 6. Constraints
...

## Tensions to resolve
- <file A says X, file B says Y: which applies?>
```

## Output

1. Post the questions and stop. Do not draft the map, a summary of it or a partial map.
2. Wait for my answers. When I answer, ask follow-ups only if an answer is unclear or contradicts the context. Produce the map only when I explicitly ask for it.

## Save

The space map output is a document, not a decision. Save it with this skill, never as a decision note through `/consolidation-prompt`.

- **When:** only when I ask to save it ("save the space map", "save this as a doc"). If it is unclear whether I mean this output or a decision note, ask.
- **Where:** `00 Context/00_Space-Map.md` (built from the context only, before Discover; see D06).
- **What:**
  - Before the map exists: the questions exactly as posted, in the format above, with my answers so far under each question (`→ Answer: …`) and unanswered ones marked `→ Not answered yet`.
  - After I ask for the map: the six-section map at the top, followed by the questions and answers as an appendix.
- **Existing file:** if `00_Space-Map.md` already exists, show what it contains and ask whether to overwrite it or save `_v2`.
- **After saving:** confirm with a link to the file and propose a project log line (see "Ask before logging" in `CLAUDE.md`).
