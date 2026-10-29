---
name: generate-guide
description: Read everything in 00 Context and any saved research questions, then ask the questions needed to write a full interview discussion guide (session length, sensitive domain, what the user already knows about the participant type, and anything else missing). Asks first; produces the guide only when asked, and saves it to 00 Context/00_Discussion-Guide.md when asked. Use when the user wants a discussion guide, an interview guide or script, or to prepare for running interviews.
argument-hint: "[optional: session length, sensitive yes/no, what you know about participants]"
---

# Discussion guide: questions first

## Input

Read **everything** in `00 Context/` (the brief, the brief interrogation, the space map, the assumption list and any other file there).
Also read `decision.log.md` and the "Where we are" section of `project.log.md`, so you do not ask about choices that are already settled.

Also use my **research questions** if they exist:
- as a saved file in `00 Context/` (e.g. a file with `Interview-Questions` or `Research-Questions` in its name);
- or, if not saved, as output of `/draft-questions` earlier in this conversation.

Say which sources you found and used. If there are no research questions, carry on with the Unknowns and Assumptions from `00 Context/` and say so. Suggest running `/draft-questions` first.

Do **not** read or use anything in `01 Discover/` or later phase folders. The guide is prepared before interviewing (same rule as the other pre-interview tools, see D06).
If `00 Context/00_Discussion-Guide.md` already exists, do not use it as input: it was built from the interview transcripts (see D09). Handle it only in the Save step (overwrite or `_v2`).

If `00 Context/` is empty, stop and tell me.

If something was given after the command ($ARGUMENTS) or in my message, use it as answers. Look especially for:
- **Session length** (e.g. 45 minutes)
- **Sensitive domain** (yes/no, and why)
- **What I already know about this participant type**

Do not ask again for anything I already gave.

## Task

I want a full discussion guide for my interviews. **Do not produce the guide yet.** Only ask me the questions you need to write it.

The finished guide will have these parts, so ask what you need for each:

1. **Session setup:** length, remote or in person, recording, consent, incentive, who interviews and who takes notes
2. **Intro and consent:** what I tell the participant about the study and how their data is used
3. **Warm-up:** easy questions about their background and how they use the product
4. **Main sections:** one per theme, built from the research questions, with timing, probes and follow-ups
5. **Sensitive moments:** how to approach difficult topics, give the participant a way out and point them to support
6. **Wrap-up:** last open question, thank you, next steps
7. **Interviewer notes:** what to watch for, what not to say

## Rules for the questions

- Always cover the three core inputs first, unless I already gave them: **session length**, **sensitive domain (yes/no, and why)**, **what I already know about this participant type**.
- Ask only what the context files cannot answer. Do not ask about anything already stated in `00 Context/` or settled in `decision.log.md`.
- Ask me to **prioritise** the research questions: which are must-cover and which can be dropped if time runs out. Cite them by number or by the Unknown/Assumption they target (e.g. `U3`, `A5`).
- If the session length looks too short for the number of research questions, say so and ask what to cut.
- If the topic may be sensitive (e.g. safety, harassment, money worries), ask how I want to handle it even if I said "no", and say why you are asking.
- Ask about stimulus: will I show anything (screenshots, the participant's own app or ride history, a prototype)?
- Do not ask me questions that only the interviews can answer. Those go into the guide.
- One thing per question. Keep each question short and concrete; say in a few words why you need it when that is not obvious.
- About 10–15 questions in total. Fewer is fine if the context covers a part.

## Format

Reply in the chat. Create a file only in the Save step below.

```markdown
# Discussion guide: questions

Read: <files and sources used> · Date: <today>

Answer by number. "Don't know" is fine: I will use a sensible default and mark it in the guide.

## Core inputs
1. How long is each session?
2. Is the domain sensitive? If yes, why?
3. What do you already know about this participant type?

## Session setup
...

## Research questions: priority
...

## Sensitive moments
...

## Stimulus and wrap-up
...

## Gaps I noticed
- <e.g. no research question covers A12; the space map says X but the brief says Y>
```

## Output

1. Post the questions and stop. Do not draft the guide, an outline of it or a partial guide.
2. Wait for my answers. Ask follow-ups only if an answer is unclear or contradicts the context.
3. Produce the guide only when I explicitly ask for it.

## The guide (when asked)

- Timing per section, adding up to the session length. Leave about 5 minutes of buffer.
- Every main question follows the `/draft-questions` checks: targets a specific unknown (cite it), starts from what the participant has actually done, cannot be answered yes or no. Not leading, one question at a time, in plain language a participant would use.
- Under each main question, give 1–3 neutral probes ("What happened next?", "Can you say more about that?", "What did you do then?").
- Mark must-cover questions with ★ so I know what to keep when time runs short.
- If the domain is sensitive: put the sensitive questions after rapport is built (not in the warm-up), tell the participant they can skip any question, and add a short script for pausing or stopping the interview and pointing them to support.
- Where I answered "don't know", use a sensible default and mark it `(default, check)`.
- Do not invent facts, participants or data that are not in the context files or my answers.

## Save

The guide is a document, not a decision. Save it with this skill, never as a decision note through `/consolidation-prompt`.

- **When:** only when I ask to save it ("save the guide").
- **Where:** `00 Context/00_Discussion-Guide.md` (prepared before interviewing, like the space map and the assumption list).
- **What:**
  - Before the guide exists: the questions as posted, with my answers under each (`→ Answer: …`) and unanswered ones marked `→ Not answered yet`.
  - After I ask for the guide: the full guide at the top, followed by the questions and answers as an appendix.
- **Existing file:** if `00_Discussion-Guide.md` already exists, show what it contains and ask whether to overwrite it or save `_v2`.
- **After saving:** confirm with a link to the file and propose a project log line (see "Ask before logging" in `CLAUDE.md`).
