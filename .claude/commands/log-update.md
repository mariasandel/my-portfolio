---
description: Review the session and propose missing entries for project.log.md and decision.log.md
argument-hint: "[optional: a decision or change to log]"
---

# Log update

## Input

Read `project.log.md` and `decision.log.md` in the project root. If one does not exist, stop and tell me.
If something was given after the command ($ARGUMENTS), treat it as a decision or change I want logged.

## Task

1. Review this conversation so far and find important changes and decisions that are not yet logged.
   Use the "Logs" section in `CLAUDE.md` to decide what counts as important and which log it belongs in:
   - **Project log:** what happened / progress (new input, finished output, step done, structure change).
   - **Decision log:** a choice that was settled (direction, scope, focus, method, rules), especially when something was rejected or removed on purpose.
2. If I gave text after the command, turn it into an entry too.
3. Skip anything already logged, even if worded differently.
4. Check whether the project log's **Where we are** section is still correct; if not, propose the update.

## Rules

- Project log line: `- YYYY-MM-DD — what changed — because why.`
- Decision log entry: the format in `CLAUDE.md` (Decision / Why / Do not / Source / Status), numbered after the last `Dxx`. A decision also gets a short project log line ending `— see Dxx`.
- Use today's date unless the conversation shows a different date for the change.
- Every entry must include the **reason**, not just what happened. Take it from the conversation; if it is not clear, mark it `?` in the proposal and ask me. Never invent a reason.
- Keep entries short and specific: name the file, folder, rule or decision.
- Do not invent decisions that were not made in the conversation.
- Only add entries; never edit or delete existing ones (except the **Where we are** section, and the `Status` of a replaced decision).

## Output

1. **Propose first, never write straight away.** Show all proposals in one numbered list, grouped by log, and ask me to review them:

   ```
   📝 Proposed log entries (approve, change or rephrase):

   Project log
   1. - YYYY-MM-DD — what changed — because why.
   2. - YYYY-MM-DD — what changed — because ?

   Decision log
   3. D06 — <Type>: <title>
      Decision: ... / Why: ... / Do not: ...

   Where we are
   4. Next step: ...
   ```

   I can approve all, pick some by number, drop some, or change or rephrase any entry (including the reason).
2. If I change or rephrase anything, show the updated entries again and wait for my OK.
3. Write only the approved entries, exactly as approved, then confirm in one short line.
4. If nothing is missing and I gave no text, say both logs are up to date and stop.
