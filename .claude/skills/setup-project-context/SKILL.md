---
name: setup-project-context
description: At the start of a new project, read CLAUDE.md and everything in 00 Context, then ask the questions needed to write a lean project-specific context block. Keeps general OS rules untouched and does not duplicate anything already in the OS. Asks only; does not write or edit anything. Use when the user is starting a new project, wants to set up or refresh the project context, or asks for a context block.
argument-hint: "[optional: project name or extra focus]"
---

# Project context: questions first

## Input

Read:

- `CLAUDE.md` in full
- **everything** in `00 Context/` (brief, brief interrogation, research input, any other file)
- `decision.log.md` and the "Where we are" section of `project.log.md`
- the names and descriptions of the commands in `.claude/commands/` and skills in `.claude/skills/`, so you know what the OS already covers

Do **not** read or use anything in `01 Discover/` or later phase folders.

If `00 Context/` is empty, stop and tell me. A context block needs at least a brief.

If something was given after the command ($ARGUMENTS), treat it as the project name or an extra focus.

## Task

I want a lean, project-specific context block for the new project. **Do not write it yet.** Only ask me the questions you need to produce it.

The block holds **contextual data only**: what this project is about. It does not hold rules for how the OS works.

### Sort before you ask

Go through `CLAUDE.md` and sort its content into two groups:

1. **General OS rules (leave untouched):** project structure, session start, naming rule, logs, decision handling, and anything else that applies to every project.
2. **Project-specific content:** domain, client, users, brief details, project terms, or leftovers from a previous project.

Then check `00 Context/` against the OS. Anything already stated in `CLAUDE.md`, a command, a skill or the decision log must not be repeated in the block. The block only adds what is new and specific to this project.

### What the block should cover (if the context supports it)

- Project name and one-line summary
- Client or brief owner, and the challenge in their words
- Domain and key terms (short glossary, only terms Claude would get wrong)
- Target users or audience
- Goal and what success looks like
- Scope: in and out
- Constraints: time, deliverables, tools, assessment
- Known stakeholders
- Leftovers from a previous project that must be removed or ignored

## Rules for the questions

- Ask only what `00 Context/` and `CLAUDE.md` cannot answer. If something is already clear, state it as a given instead of asking.
- One thing per question. Short and concrete. Say which file or line raised it when that helps.
- Flag every place where `CLAUDE.md` still holds content from a previous project, and ask whether to remove it, keep it or move it.
- Flag tensions between files (e.g. the brief says one deadline, another file says a different one) and ask which applies.
- Ask where the block should live: a section in `CLAUDE.md`, or a separate file in `00 Context/` that `CLAUDE.md` points to. Propose one and say why.
- Ask how lean it should be (e.g. a maximum length) if that is not clear.
- Do not ask about Active decisions in `decision.log.md`; treat them as settled.
- About 10–15 questions in total. Fewer is better if the context is clear.

## Format

Reply in the chat only. Do not create or edit a file.

```markdown
# Project context: questions

Read: <files read> · Date: <today>

## What I found

**General OS rules in CLAUDE.md (will not touch):** <short list of sections>
**Project-specific or leftover content in CLAUDE.md:** <list, or "none">
**Already covered by the OS (will not repeat):** <list>
**Clear from 00 Context (will use as given):** <short list>

## Questions

Answer by number. "Not sure" is a useful answer.

### Project and domain
1. ...

### Users, goal and scope
...

### Constraints
...

### Leftovers and tensions
...

### Where the block lives
...
```

## Output

1. Post what you found and the questions, then stop. Do not draft the block, a partial block or an edit to `CLAUDE.md`.
2. Wait for my answers. Ask follow-ups only if an answer is unclear or contradicts the context. Write the block only when I explicitly ask for it, and never change the general OS rules in `CLAUDE.md` while doing so.
