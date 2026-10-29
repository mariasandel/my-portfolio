---
name: clean-design-os
description: At the end of a project, inventory the whole Design OS and ask the questions needed to sort every item into reusable (carry forward), archive (project-specific) or unsure. Asks only; does not move, rename, delete or reorganise anything. Use when the user has finished a project, wants to clean up or reset the Design OS, or prepare it for the next project.
argument-hint: "[optional: name of the finished project or extra focus]"
---

# Clean the Design OS: questions first

## Input

Build a full inventory of the repo. Read or list:

- `CLAUDE.md`, `README.md`, `project.log.md`, `decision.log.md`
- every command in `.claude/commands/` and every skill in `.claude/skills/` (read each one, not just the name)
- `.claude/settings.json`, `.claude/settings.local.json` and any hooks, if they exist
- the phase folders `00 Context` to `04 Deliver` (list the files; read only what you need to judge whether it is project-specific)
- any other file or folder at the root

If something was given after the command ($ARGUMENTS), treat it as the project name or an extra focus.

## Task

I want to separate what carries forward to any future project from what belongs to this finished project and should be archived. **Do not reorganise anything.** No moving, renaming, deleting, editing or archiving. Only ask me the questions you need to sort every item into one of three groups:

1. **Reusable:** general enough to keep as-is for any project
2. **Archive:** specific to this project (domain context, brief, research, outputs, project-specific commands)
3. **Unsure / needs reworking:** useful in general but contains project-specific content (e.g. a command that names the domain, a CLAUDE.md section about this brief, decisions that are really process rules)

## How to prepare the questions

For each item, make a first guess yourself and look for the evidence:

- Does it mention the project's domain, client, users, brand or brief? (e.g. names, product terms, specific research themes)
- Is it a method that works for any Double Diamond project, or was it built for one step of this one?
- In the logs: which decisions are **project** decisions (scope, synthesis, design direction) and which are **process** decisions (naming rules, how logs work) that should survive?
- In `CLAUDE.md`: which sections are general setup and which describe this project?

Only ask about items where the answer is not obvious. For the obvious ones, state your guess in the inventory so I can correct it.

## Rules for the questions

- One thing per question. Short and concrete. Name the file and quote the line that makes it ambiguous.
- Ask about the archive itself too: where it should live (folder in this repo, separate repo, zip), its name, and whether archived files keep their current structure.
- Ask what the next project needs to start clean: empty phase folders? blank logs or a template? which decisions carry over?
- For "needs reworking" items, ask whether I want a generic version made later, and what should replace the project-specific parts.
- Ask whether anything should become a template (e.g. log headers, brief interrogation format).
- Do not reopen Active decisions in `decision.log.md`; only ask whether each one is project-specific or should carry forward.
- About 15–25 questions in total.

## Format

Reply in the chat only. Do not create a file.

```markdown
# Clean the Design OS: questions

Read: <files and folders read> · Date: <today>

## Inventory (my first guess, correct me)

| Item | Guess | Why |
|------|-------|-----|
| .claude/commands/log-update.md | Reusable | No project terms |
| 00 Context/00_Brief.md | Archive | Project brief |
| .claude/commands/xyz.md | Unsure | Mentions <domain term> in step 3 |

## Questions

Answer by number. "Not sure" is a useful answer.

### Commands and skills
1. ...

### CLAUDE.md, settings and hooks
...

### Logs and decisions
...

### Phase folders and research
...

### The archive and the fresh start
...
```

## Output

1. Post the inventory and questions, then stop. Do not move, rename, delete or edit anything, and do not draft a cleanup plan.
2. Wait for my answers. Ask follow-ups only if an answer is unclear or contradicts what is in the files. Make a cleanup plan only when I explicitly ask for it, and change files only after I approve that plan.
