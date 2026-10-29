---
description: Extract observations from one interview transcript for affinity mapping
argument-hint: "<participant name or transcript file, e.g. Lena>"
---

# Extract observations

## Input

Process **one transcript per run**.

- If a participant name was given ($ARGUMENTS), read `01 Discover/Primary Research/Raw/01_Transcript_<Name>.md`.
- If a file name was given, read that file instead.
- If nothing was given, list the transcripts in `01 Discover/Primary Research/Raw`, mark which ones already have an observations file in `01 Discover/Primary Research/Processed`, and ask me which one to process. Stop there.
- If the file does not exist, stop and tell me which file is missing.

From the transcript header, take:
- the **project domain** (the `PROJECT` line, e.g. "Buying a Pumpkin Spice Latte in Berlin");
- the **participant ID and name** (the `PARTICIPANT` line, e.g. `P01 — Lena`).

## Task

This is a transcript from a UX research interview about the project domain above. Extract observations from it for an affinity mapping exercise.

Only use the **Transcript** section. Do not use the Context Note or the Raw Field Notes: they are the researcher's interpretation, not what happened in the interview.

### Turn references

The transcripts do not number turns, so number them yourself:
- Each interviewer question (bold line) is `Q1`, `Q2`, `Q3`... in order.
- The participant's answer to a question is `A1`, `A2`, `A3`..., matching its question. An answer that runs over several paragraphs keeps the same number.
- A researcher note (`*[NOTE: ...]*`) is referenced by the answer it sits in or follows, e.g. `Note after A4`.

### Each observation must

1. Use the participant's own language.
2. Include a **verbatim anchor**: the exact sentence the observation draws from, copied word for word.
3. Include the **turn reference** for traceability (e.g. `A4`).
4. Carry an **evidence tag** (S/W/I, see below).

### Evidence tags (S/W/I)

| Tag | Meaning | What to add |
|-----|---------|-------------|
| **S** (Supported) | The participant said it directly. | The verbatim quote is the anchor. |
| **W** (Weak) | Researcher inference from behaviour or implication: researcher notes, `⚠ Approximate` anchors, things the participant implied but did not say. | An `Inference:` line naming the inference. |
| **I** (Invented) | No participant source in the Transcript section. | Flag it `✗ Remove`. |

The observation text itself stays uninterpreted (see Rules). For W, the inference goes on its own `Inference:` line, never into the observation.

### Researcher notes

`[NOTE: ...]` lines describe behaviour the researcher saw (e.g. opening the app, a long pause). Turn these into observations too, labelled `Researcher note`. Use the note text as the anchor. Quotes the participant says inside a note count as participant language.

## Rules

- One observation per distinct moment.
- One thing per observation. Do not combine or synthesise across multiple moments.
- Do not interpret. Name what happened, not why.
- Do not use the interviewer's words as the observation; they only give context.
- If no clear verbatim anchor exists, still include the observation but flag it `⚠ Approximate`, give the closest sentence as the anchor, and tag it W.
- Do not skip moments because they seem minor or off-topic; the affinity map decides what matters.

## Format

Number the observations with IDs `<Participant ID>-O01`, `-O02`... (e.g. `P01-O01`), in transcript order.

```markdown
# Observations: <Participant ID> <Name>

Source: `<transcript file>` · Project: <project domain> · Date: <today>

1. **P01-O01** · S — <observation in the participant's language>
   - Anchor: "<exact sentence from the transcript>"
   - Turn: A3

2. **P01-O02** · W — <observation>
   - Anchor: "<exact sentence>"
   - Turn: Note after A4 · Researcher note
   - Inference: <what the researcher infers from the behaviour>

3. **P01-O03** · W — <observation> ⚠ Approximate
   - Anchor: "<closest sentence>"
   - Turn: A6
   - Inference: <what is implied but not said>

4. **P01-O04** · I — <observation> ✗ Remove
   - Anchor: none in the Transcript section
```

End the file with a tally: `S: n · W: n · I: n`.

### File name

Follow the naming rule in `CLAUDE.md`: `01_Observations_<Name>.md` (e.g. `01_Observations_Lena.md`).

## Output

1. Before saving, check every anchor against the transcript: it must appear there word for word. If it does not, fix it or flag the observation `⚠ Approximate` (and tag it W). Check that every observation has an S, W or I tag.
2. Save the file in `01 Discover/Primary Research/Processed`.
   If that file already exists, ask me whether to overwrite it or save a new version (`_v2`).
   If it has a `Review:` line (from `/review-observations`), warn me that overwriting drops the review marks and the decisions on the review page stop counting.
3. In the chat, reply with a short summary only: number of observations, the S/W/I tally, how many are flagged approximate, any I observations to remove, and a link to the file.
4. Run the `participant-tracker` skill in `sync` mode for this participant (one line in the reply).
