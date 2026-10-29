---
description: Interrogate the project brief and list its Knowns, Unknowns and Assumptions
argument-hint: "[optional: brief file, default 00 Context/00_Brief.md]"
---

# Brief interrogation

## Input

Read the brief at `00 Context/00_Brief.md`.
If something was given after the command ($ARGUMENTS):
- if it is a file name, read that file instead;
- if it is text, treat that text as the brief.
If the file does not exist, stop and tell me which file is missing.

## Task

Interrogate the brief. Identify:

1. **Knowns:** what does the brief actually confirm as fact?
2. **Unknowns:** what important questions does the brief leave unanswered that a research sprint could address?
3. **Assumptions:** what is the brief assuming, about users, about the problem, or about what matters, without stating it explicitly?

## Rules

- Knowns must be directly stated in the brief, not inferred. If you are inferring, it is not a Known.
- Every Known includes an **evidence quote**: the exact words from the brief it comes from.
- Every Assumption gets a **risk rating** (High / Medium / Low): how much would the project be affected if this assumption turned out to be wrong?
- Flag (⚑) any Assumption that you think could be challenged by the research, and say briefly how.
- Do not invent facts, users or data that are not in the brief.

## Format

Three labelled sections: **Knowns**, **Unknowns**, **Assumptions**.

```markdown
# Brief Interrogation: <brief name>

Source: <brief file> · Date: <today>

## Knowns
| # | Known | Evidence quote |
|---|-------|----------------|
| K1 | ... | "..." |

## Unknowns
| # | Unknown | Why it matters |
|---|---------|----------------|
| U1 | ... | ... |

## Assumptions
| # | Assumption | Risk | Could research challenge it? |
|---|------------|------|------------------------------|
| A1 | ... | High | ⚑ Yes: ... |
```

### File name

Follow the project naming rule in `CLAUDE.md`: `NN_Type_Subject.md` (Subject optional)

- `NN` = `00` (the file goes in `00 Context`)
- `Type` = `Brief-Interrogation`
- `Subject` = only if the brief file name has one, reuse it (e.g. `00_Brief_Pricing.md` → `Pricing`).
  For the default brief (`00_Brief.md`) or pasted text, leave the Subject out.

Examples: `00_Brief-Interrogation.md`, `00_Brief-Interrogation_Pricing.md`

## Output

1. Save the result in `00 Context` using the file name above.
   If that file already exists, ask me whether to overwrite it or save a new version (`_v2`).
2. In the chat, reply with a short summary only: how many Knowns, Unknowns and Assumptions, the High-risk flagged Assumptions, and a link to the file.
