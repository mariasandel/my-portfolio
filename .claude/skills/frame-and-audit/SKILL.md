---
name: frame-and-audit
description: Frame the problem through five lenses in parallel (frequency, underserved segment, need statement, outcome, outlier), one /frame-problem instance per lens, each returning one statement with an evidence score and a justification. Flags overlap, saves the five as PS1–PS5, shows a comparison table and pauses for the user to pick one. Then runs /audit-problem-statement on the pick and returns the flagged list. Never picks, ranks or rewrites a statement. Use when the user wants to frame with lenses, compare five framings, or frame and audit in one go.
argument-hint: "[optional: folder with the need statement and synthesis, e.g. a test folder. Default: 02 Define]"
---

# Frame and audit

This skill only orchestrates two commands: `/frame-problem` (once per lens) and `/audit-problem-statement` (on the statement I pick). Their rules apply unless this file says otherwise.

**Folder:** if a folder was given ($ARGUMENTS), use it for every read and save, and pass it on to both commands. If nothing was given, use `02 Define`. Below, `<folder>` means that folder.

## Step 1: Pre-check

Run the stop checks from `.claude/commands/frame-problem.md` once, before starting any instance:

- `<folder>/02_Need-Statement.md` exists. If not, stop and ask me to write it first.
- `<folder>/02_Synthesis.md` has at least one confirmed theme. If not, stop and ask me to mark the confirmed themes first.
- If `<folder>/02_Problem-Statements.md` already exists, ask now whether to overwrite it or stop. There is no `_v2` option: `/audit-problem-statement` only reads `02_Problem-Statements.md`.

## Step 2: Five lens instances in parallel

Start **all five at once**: one subagent per lens, all in the same message (Agent tool, `general-purpose`). Prompt for each:

> Read `.claude/commands/frame-problem.md` and follow its Input, Task fields, Evidence score and Rules for the folder `<folder>`, with these differences:
> - Write **one** problem statement, framed only through this lens: **<lens name>: <lens instruction>**.
> - <lens-specific rule, if any, from the table below>
> - Save nothing. Do not write to the logs.
> - If the confirmed themes hold no S evidence for this lens, reply "No statement: <reason>" instead of forcing one.
>
> Reply with exactly: Lens · User · Moment · Root cause · Statement · Evidence (clusters and observation IDs with S/W tags) · Score (n/N, label, participants) · Tension (if any) · IDs checked (yes/no) · Justification (1–2 lines: how the lens and the evidence led to this statement).

| # | Lens | Instruction | Lens-specific rule |
|---|------|-------------|--------------------|
| 1 | Frequency | Frame around the most-cited behaviour or frustration | — |
| 2 | Underserved segment | Frame around the group least served by current solutions | — |
| 3 | Need statement | Frame around what "users need a way to X in order to Y" opens up | Use the framing to find the need, but write the standard sentence "[user] needs [need] when [moment] because [root cause]". Never write "needs a way to…" (it is solution bias for `/audit-problem-statement`) |
| 4 | Outcome | Work backward from what changes for the user if the problem is fully solved | Describe the problem, not the solved state or a fix |
| 5 | Outlier | Centre the participant whose experience diverged most from the group | Exempt from the 2-participant rule and from "outliers count as 0". Score it `1/N, Thin` and add `⚑ Rests on one participant` next to the score |

Wait for all five before going on. Do not write statements yourself, and do not re-run an instance to get a "better" one.

## Step 3: Flag overlap

Compare every pair of returned statements. Two flag types:

- **⚑ Too similar:** the pair differs on only one of user, moment and root cause (the `/frame-problem` similarity rule).
- **⚑ Shared evidence:** the pair shares more than half the observation IDs of the smaller evidence set.

```
⚑ Too similar: PS1 and PS3, same user and moment (dairy-free buyer, at the counter); only the root cause differs.
⚑ Shared evidence: PS2 and PS4 share 4 of 5 IDs (P01-O12, P03-O07, P04-O21, P05-O03).
```

## Step 4: Save

Save `<folder>/02_Problem-Statements.md` in the `/frame-problem` format, so `/audit-problem-statement` can read it unchanged:

- PS1–PS5 in lens order (PS1 = Frequency … PS5 = Outlier). A lens that returned "No statement" keeps its number, with the reason instead of the frame.
- Add a **Lens** line as the first bullet of each statement.
- Header: `IDs checked: yes` only if all five instances checked their IDs; otherwise `no` and which ones did not.
- **Similarity check:** both flag types from Step 3 (or "No pairs flagged.").
- **Not used:** merge the instances' Not used lines, without duplicates.
- Leave out the "Why <n> statements" section. End with "Choosing one is your call."

## Step 5: Compare and pause

In the chat, show only:

```markdown
| # | Lens | Statement | Score | Justification | Overlap flags |
|---|------|-----------|-------|---------------|---------------|
| PS1 | Frequency | "…" | 4/5, Strong | … | ⚑ Too similar: PS3 |
```

Then the full flag lines, whether the IDs were checked, a link to the file, and: **"Which one should I audit?"**

Stop here. Do not rank, recommend or hint at a pick.

## Step 6: Audit

When I reply with an ID (e.g. `PS3`), run `/audit-problem-statement <ID> [<folder> if one was given]` with the Skill tool and follow it exactly. Return its chat summary: flag counts by severity, one line per flag, and a link to the audit file.

- If my reply is not a valid ID, list PS1–PS5 again and ask once more.
- Do not record which statement I picked, in any file or log (as `/audit-problem-statement` requires).

## Rules

- Never pick, rank, recommend or rewrite a statement.
- No solutions in the statements: no features, screens or fixes.
- Never read the transcripts or `00 Context`, and never use the Context Note or Raw Field Notes (D05).
- At the end, propose a project log line (see "Ask before logging" in `CLAUDE.md`), without naming the picked statement.
