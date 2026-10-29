---
description: Write a 5–8 question recruitment screener with explicit accept / borderline / reject logic for every question
argument-hint: "[optional: extra criteria or focus, e.g. must ride at night]"
---

# Write a recruitment screener

## Input

Read **everything** in `00 Context/` (the brief, the brief interrogation, the space map, the assumption list and any other file there).
Also read `decision.log.md`, so the screener does not reopen settled decisions (e.g. what is in scope).

Look specifically for the **participant profile** and **recruiting criteria**:
- a file in `00 Context/` with `Participant`, `Profile`, `Recruiting`, `Criteria` or `Screener` in its name;
- or sections about participants, the target user or who to recruit inside the other files.

Say which sources you used.

**If there is no participant profile or recruiting criteria:** do not stop. Derive draft criteria from the context (e.g. who the brief names as the user, the in-scope themes, the Unknowns and Assumptions about the sample) and list them under **Criteria used** with the source of each, marked `(derived, check)`. Say clearly that the screener rests on derived criteria.

Do **not** read or use anything in `01 Discover/` or later phase folders (same rule as the other pre-interview tools, see D06).
Also skip `00 Context/00_Discussion-Guide.md`: it was built from the interview transcripts (see D09), so it counts as interview data.

If `00 Context/` is empty, stop and tell me.
If something was given after the command ($ARGUMENTS), add it as an extra criterion.

## Task

Write a recruitment screener with **5–8 questions**. Every question must return a **decision**, not just data:

- **Accept:** the answer that passes
- **Borderline:** the answer that needs a judgement call, and what decides it
- **Reject:** the answer that fails

## Rules

- Each question tests one criterion. Cite the criterion it tests.
- Order: hard knock-outs first (e.g. uses the product, lives in the area, age), then behaviour and frequency, then nice-to-have mix criteria.
- Do not reveal the study topic or the "right" answer. Do not name trust, pricing or safety in a way that tells the person what to say; hide the target answer among real options.
- Prefer multiple choice with concrete, recent ranges ("In the last 3 months, how often…") over opinions or yes/no.
- Include at least one **articulation check** (an open question showing the person can describe a real past experience) and, where relevant, a check that screens out people who work in UX, market research or for the company or a competitor.
- Accept / borderline / reject must cover **every** answer option. No option without a decision.
- Borderline must say what tips it: e.g. "Accept if we still need someone over 50", "Accept if the open answer describes a specific trip".
- If a criterion is about **quotas** (mix of ages, cities, genders), put it in **Quotas**, not as a reject rule.
- Plain language a buyer would use, no design or industry jargon.
- Do not invent facts, participants or numbers that are not in the context files. When you choose a threshold yourself (e.g. "at least twice a month"), mark it `(my threshold, check)`.

## Format

Reply in the chat only. Do not create a file.

```markdown
# Recruitment screener

Read: <files used> · Date: <today>
Criteria source: <participant profile / recruiting criteria file> or "derived from context, no profile found"

## Criteria used
- C1: <criterion> · Source: <file / K, U, A number> <(derived, check) if derived>
- C2: ...

## Questions

### 1. <question>  · Tests: C1
- a) <option>
- b) <option>
- c) <option>

| Answer | Decision |
|---|---|
| a | ✅ Accept |
| b | ⚠️ Borderline: <what decides it> |
| c | ❌ Reject: <why> |

### 2. ...

## Quotas
- <e.g. at least 2 of 5 over 45 · Source>

## Decision rule
- Any ❌ → reject.
- More than <n> ⚠️ → reject or review.
- Otherwise → accept, then check quotas.
```

## Output

1. Post the criteria, the screener, the quotas and the decision rule.
2. End with:
   - any criterion that has no question yet;
   - every threshold or criterion marked `check`, so I can confirm or change it.
