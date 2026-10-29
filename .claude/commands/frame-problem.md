---
description: Generate 3–5 genuinely distinct problem statements from the need statement, confirmed themes and insights, each with an evidence score
argument-hint: "[optional: folder with the need statement and synthesis, e.g. a test folder. Default: 02 Define]"
---

# Frame problem

## Input

**Folder:** if a folder was given ($ARGUMENTS), read the input files from there and save the output there. If nothing was given, use `02 Define`. Below, `<folder>` means that folder.

1. **Need statement:** read `<folder>/02_Need-Statement.md`. If it does not exist, stop and ask me to write it first.
2. **Synthesis:** read `<folder>/02_Synthesis.md`.
   - Use only the confirmed themes, with their clusters, and the insights drawn from those clusters.
   - A theme counts as confirmed when it has a `Status: Confirmed` line, or `Confirmed` in a Status column of the themes table, or ✅ on its heading. Parked clusters (`Parked`, ⏸) are not used, even inside a confirmed theme.
   - If no theme is marked as confirmed, stop and ask me to mark the confirmed themes first.
   - Count the participants listed in the synthesis. This is **N**, used for the score.
   - The Tensions, Outliers and Parking lot sections may be read for context. They are not evidence (see Rules).
3. **Observation lists:** read `01 Discover/Primary Research/Processed/01_Observations_<Name>.md` only to check that every observation ID you cite exists and carries the S/W tag you claim.
   - If the observation files are missing (e.g. in a test folder), do not stop. Take the IDs and tags from the synthesis, and say in the output header and the chat summary that the IDs were not checked.

Do not read the transcripts, and never use the Context Note or Raw Field Notes (D05). Do not read `00 Context`.

## Task

Write **3 to 5** problem statements. Each one names:

- **User:** a buyer type drawn from the data (e.g. dairy-free buyer, budget-tight student, buyer who only goes to independent cafés), not a named participant
- **Moment:** when the problem happens
- **Root cause:** why it happens
- **Statement:** one sentence: "[user] needs [need] when [moment] because [root cause]"
- **Evidence:** the clusters and observation IDs it rests on
- **Score:** see Evidence score

The statements must be **genuinely distinct**: each one differs from every other on at least two of user, moment and root cause.

## Evidence score

- Score = number of participants with **S** evidence behind the statement, out of N (e.g. `3/5`, `2/4`).
- Label by share of N: **Strong** (80% or more), **Moderate** (50% to under 80%), **Thin** (under 50%, or exactly 2 participants).
- W observations can sit in the evidence but never raise the score.
- Outliers and single-participant clusters (e.g. D2, D3) count as 0. They can never carry a statement alone.
- If a tension from the synthesis applies (e.g. B3 vs B4), note it next to the score. It does not lower the score.

## Similarity check

Compare every pair of statements. Flag any pair that differs on only one of user, moment and root cause:

```
⚑ Too similar: PS1 and PS3, same user and moment (dairy-free buyer, at the counter); only the root cause differs.
```

## Rules

- **Do not select, rank or recommend a statement.** Choosing one is my job.
- No solutions in the statements: no features, screens or fixes.
- Do not invent evidence. Every statement cites at least one S observation from 2 or more participants.
- If the evidence only supports 3 distinct statements, write 3 and say why. Do not pad to 5.
- Cite by observation ID, e.g. `P02-O78 (S)`.

## Format

```markdown
# Problem Statements

Need statement: `<folder>/02_Need-Statement.md` · Synthesis: `<folder>/02_Synthesis.md` (confirmed themes: <letters>) · Participants: N · IDs checked: yes / no (observation files missing) · Date: <today>

Need statement: "<quoted>"

## PS1. <short title>

- **User:** …
- **Moment:** …
- **Root cause:** …
- **Statement:** "… needs … when … because …"
- **Evidence:** clusters <IDs> · <observation IDs>
- **Score:** 4/5, Strong (P01, P03, P04, P05) · Tension: <if any>

## PS2. …

## Similarity check

- ⚑ <pair, what overlaps> (or "No pairs flagged.")

## Not used

- <parked clusters, outliers and single-participant clusters left out, one line each with the reason>

## Why <n> statements
<only if fewer than 5: one line on what the evidence could not support>

Choosing one is your call.
```

### File name

Follow the naming rule in `CLAUDE.md`: `02_Problem-Statements.md`.

## Output

1. Before saving, check that every cited ID exists in the observation files with the tag claimed (unless they are missing), every score matches its S evidence, and every pair has been compared.
2. Save the file in `<folder>`. If it already exists, ask me whether to overwrite it or save a new version (`_v2`).
3. In the chat, reply with a short summary only: each statement in one line with its score, any similarity flags, whether the IDs were checked, a link to the file, and "Choosing one is your call."
