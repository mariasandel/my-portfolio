---
description: Audit one selected problem statement for solution bias, unsupported assumptions, vague needs and weak research connections, and return a flagged list without rewriting it
argument-hint: "<statement ID, e.g. PS4> [optional: folder with 02_Problem-Statements.md. Default: 02 Define]  — or paste a statement as text"
---

# Audit problem statement

## Input

1. **Statement:** take the statement ID from $ARGUMENTS (e.g. `PS4`).
   - If no ID and no pasted statement was given, stop and ask me which statement to audit. Do not guess: nothing in the files marks which one I selected.
2. **Folder:** if a folder was given in $ARGUMENTS, read from there and save there. If not, use `02 Define`. Below, `<folder>` means that folder.
3. **Problem frame:** read `<folder>/02_Problem-Statements.md` (made with `/frame-problem`). Use:
   - the selected statement's frame: user, moment, root cause, statement, evidence, score and tension
   - the header: need statement, and whether the IDs were checked
   - the Similarity check (⚑ too-similar and ⚑ shared-evidence flags) and Not used sections
   - If the file does not exist, stop and tell me to run `/frame-problem` first. If the ID is not in it, stop and list the IDs that are.
4. **Pasted statement:** if I pasted a statement as text instead of an ID, audit that text. It has no frame, so run only checks 1 and 3. Mark checks 2 and 4 as "Not checked: no frame".

Read only the `/frame-problem` output. Do not read the synthesis, the observation files, the transcripts or `00 Context`, and never use the Context Note or Raw Field Notes (D05).

## Checks

1. **Solution bias:** the statement names or implies its own fix (a feature, label, app, channel or format), or uses "needs a way to…" phrasing that points at one answer.
2. **Unsupported assumptions:** a claim in the statement that its own frame and evidence line do not back. This includes claims resting only on W evidence or outliers, and claims that ignore the tension noted on the statement.
3. **Vague needs:** the need is a broad word ("know", "trust", "clarity", "better") that does not say what, when or how much, or the need is a want or a feeling.
4. **Weak research connections:** any of:
   - a Thin score
   - evidence from only one cluster
   - "IDs checked: no" in the header, or no "IDs checked" field at all (older output): treat a missing field as unknown and flag it Low
   - a ⚑ too-similar flag that names this statement
   - a ⚑ shared-evidence flag that names this statement (written by `/frame-and-audit`): the statement may not stand apart from the other one in the research
   - parts of the statement that do not map onto the frame's user, moment and root cause

## Rules

- **Do not rewrite the statement.** No alternative wording, no "better version", not even for one phrase. Flag it.
- Every flag quotes the exact phrase it applies to.
- Severity:
  - **High:** the statement points at a fix, or a core claim (user, moment, root cause, need) has no evidence.
  - **Medium:** the claim is only partly backed, or the need is too broad to design against.
  - **Low:** worth knowing, does not block moving forward.
- No overall verdict or pass/fail. Give counts only.
- In Passed / not checked, list every check once:
  - a check with no flags: passed, with a one-line reason
  - a check with flags: the parts of it that passed, with a one-line reason, and the flag numbers (e.g. "Flags 3, 5")
- Do not record which statement I selected, in any file or log.
- This audit trusts the evidence line in the `/frame-problem` output. It cannot check whether a cited ID says what the statement claims; say so in the header.

## Format

```markdown
# Problem Statement Audit: <ID>

Problem frame: `<folder>/02_Problem-Statements.md` · Statement: <ID> · Date: <today>
Evidence taken from the /frame-problem output; cited IDs not re-checked against the synthesis.

Statement: "<quoted>"

Flags: High n · Medium n · Low n

| # | Check | Phrase | Why it is a problem | Evidence | Severity | Question to consider |
|---|-------|--------|---------------------|----------|----------|----------------------|
| 1 | Solution bias | "needs a way to …" | … | … | High | … |

## Passed / not checked

- <Check>: passed, <one-line reason>
- <Check>: flags <n, n>; passed: <the parts that passed, one line>
- <Check>: not checked, no frame (pasted statement only)
```

### File name

Follow the naming rule in `CLAUDE.md`: `02_Problem-Statement-Audit_<ID>.md` (e.g. `02_Problem-Statement-Audit_PS4.md`). For a pasted statement, use `02_Problem-Statement-Audit.md`.

## Output

1. Before saving, check that every flag quotes a phrase that is really in the statement and that nothing in the file rewrites the statement.
2. Save the file in `<folder>`. If it already exists, ask me whether to overwrite it or save a new version (`_v2`).
3. In the chat, reply with a short summary only: the flag counts by severity, one line per flag, and a link to the file.
