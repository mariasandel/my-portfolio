---
description: Write a desk research plan for the secondary research phase from the research questions and the context, without doing the research
argument-hint: "[optional focus, e.g. alternatives and pricing. Default: every question desk research can answer]"
---

# Scope research

## Input

Read **everything** in `00 Context/`, in particular:
- `00 Context/00_Research-Questions.md`: the research questions (main question and RQ1, RQ2…), with the Unknowns and Assumptions each covers and whether desk research can answer it.
- `00 Context/00_Brief.md`, `00_Brief-Interrogation.md` and `00_Assumptions.md`: the domain, constraints, Unknowns (`U`) and Assumptions (`A`).

Also read `decision.log.md`, so the plan does not reopen settled decisions (e.g. scope in D08).

Do **not** read or use anything in `01 Discover/` or later phase folders (D06).
Also skip `00 Context/00_Discussion-Guide.md`: it was built from the interview transcripts (D09), so it counts as interview data.

If `00 Context/` is empty, stop and tell me.
If `00_Research-Questions.md` is missing, use the Unknowns in `00_Brief-Interrogation.md` as the questions instead, and say so in the header.

### Focus

An optional focus can follow the command ($ARGUMENTS), e.g. "alternatives and pricing". If given, cover only the questions that match it and name the focus in the header. If nothing was given, cover every question desk research can answer.

## Task

Write a desk research plan that I will use to guide the secondary research phase. **Do not do the research itself.**

1. **Pick the questions.** Keep only the questions desk research can answer (in `00_Research-Questions.md`: `Desk research` or `Both`). Questions that need participants go in the "Not for desk research" line at the end.
2. **What to look for:** turn each kept question into specific topics and questions to look up. Tie each one to its research question and its `U`/`A` IDs.
3. **Where to look:** name the source types that fit this domain, each with one line on why it fits and which topics it serves. Name types, not specific sources or URLs.
4. **How to assess:** give two or three criteria for deciding whether a source is credible **for this domain and project**, each with one line on why it matters here.

## Rules

- Never do the research: no findings, figures, prices, names of real studies or claims about what sources will say.
- Never invent sources or data. Source types only.
- No generic advice ("search Google", "check reliable websites"). Every source type and criterion must be specific to the domain in the context files.
- No solution language: the plan looks at the problem space and its alternatives, not at features to design.
- Respect the scope in the brief and `decision.log.md`. Say when a topic touches a scope exclusion, and leave it out.
- Keep it short: 4–8 topics, 3–6 source types, 2–3 criteria.

## Format

```markdown
# Desk Research Plan

Read: <files read> · Questions from: <00_Research-Questions.md | Unknowns in 00_Brief-Interrogation.md> · Focus: <focus | all> · Date: <today>

## 1. What to look for

| # | Topic and questions to answer | Research question | Covers |
|---|-------------------------------|-------------------|--------|
| T1 | <topic>: <specific question(s)> | RQ2 | U6, A8 |

## 2. Where to look

| Source type | Why it fits this domain | Topics |
|-------------|-------------------------|--------|
| <source type> | <one line> | T1, T3 |

## 3. How to assess

1. **<criterion>:** <one line on why it matters for this domain and project>

**Not for desk research:** <research questions that need participants, e.g. RQ3 (how buyers judge value)>
```

## Output

1. Save the plan as `00 Context/00_Desk-Research-Plan.md`. If it already exists, ask me whether to overwrite it or save a new version (`_v2`).
2. In the chat, reply with a short summary only: number of topics, source types and criteria, the questions left out, and a link to the file.
3. The plan is the input for the secondary research, saved in `01 Discover/Secondary Research` (e.g. `01_Alternatives.md`).
