---
name: send-observations
description: Send the approved S/W observations from one or more sessions to the project's FigJam board as sticky notes, one per observation, grouped by participant (S green with the verbatim quote, W yellow, I never sent). Only observations marked ✓ Approved by /review-observations are sent. Checks the observation list first, runs /extract-observations if it is missing or untagged, flags lists that are not reviewed or not fully reviewed, and reports every flag before creating anything on the board. Use when the user wants to send, push or export observations to FigJam or Figma, set up the affinity mapping board, or put observations on stickies.
argument-hint: "[optional: participant name(s) or \"all\". Default: the most recent session] [optional: FigJam board URL]"
---

# Send observations to FigJam

## Input

1. **FigJam board:** a `figma.com/board/...` URL in $ARGUMENTS. If none was given, ask me for the board URL (or board name) and stop until I give it. Take the `fileKey` from the URL (`figma.com/board/:fileKey/:fileName`).
2. **Sessions:** pick the participants.
   - Name(s) in $ARGUMENTS (e.g. `Lena Tobias`): use those.
   - `all`: every transcript in `01 Discover/Primary Research/Raw`.
   - Nothing given: the most recent session, meaning the transcript with the latest `DATE` in its header. Say which session you picked and why.
3. **Observation list** for each participant: `01 Discover/Primary Research/Processed/01_Observations_<Name>.md`. If there are versions (`_v2`, `_v3`), use the highest one and say which.
   - **Missing**, or its observations **have no S/W/I tags** (e.g. `**P01-O01** · S —`): run `/extract-observations <Name>` for that participant first. If it asks whether to overwrite or save `_v2`, pass the question on to me. Then use the new file.
   - Do not tag observations yourself. Tags only come from `/extract-observations`.
4. **Review status** of each observation list: the `Review:` line under its header, written by `/review-observations`.
   - **No `Review:` line** (never reviewed): nothing from this participant is sent. Ask whether to run `/review-observations` first.
   - **`Review: Unfinished`**: only the approved observations can be sent. Say how many are still to review and ask whether to send the approved ones now or finish the review first.
   - **`Review: Complete`**: go ahead.
   - Do not approve observations yourself. Approval only comes from `/review-observations`.

Use only the observation files as the source. Never use the Context Note or Raw Field Notes (D05). The transcript is only read for the anchor check in the next section.

## Validate and report flags

Check every observation before anything goes to the board:

| Check | Flag |
|---|---|
| Not marked `✓ Approved` | Not sent. Give the count per participant (not every ID). |
| Tagged `I` or marked `✗ Remove` | Not sent. List the IDs. |
| Marked `⚠ Approximate` | Sent as W (yellow). List the IDs so I know which anchors are approximate. |
| S anchor does not appear word for word in the Transcript section | Not sent until fixed. List the ID, the anchor and the closest sentence. |
| No tag, two tags, or no anchor | Not sent. List the ID. |
| Duplicate observation ID | Not sent. List the IDs. |
| Participant already has a section on the board | Ask: replace it, add next to it, or skip this participant. |

To check the board for existing sections, read it with `get_figjam` first.

Then **report before creating**, in the chat:

- per participant: the observation file used, its review status (Complete / Unfinished / not reviewed), and the S / W / not-sent counts;
- every flag from the table above, grouped by flag;
- the board it will go to.

**Wait for my OK.** If there are flags, I may fix the observation file first, or tell you to go ahead without the flagged items.

## Create the stickies

Before any `use_figma` call, load the `figma-use` and `figma-use-figjam` skills. If no Figma plugin is installed, read the MCP resources `skill://figma/figma-use/SKILL.md` and `skill://figma/figma-use-figjam/SKILL.md` instead. Follow them for node creation, sticky colours and batching.

- **One sticky per observation.** Approved S and W observations only, never I or unapproved ones.
- **Colour:** S green, W yellow (FigJam's standard sticky colours).
- **Group by participant:** one FigJam section per participant, titled `<Participant ID> <Name>` (e.g. `P04 Jonas`). Sections sit side by side in participant ID order.
- **Inside a section:** stickies in observation ID order, in a grid with even spacing (e.g. 6 per row), so none overlap.
- **Sticky text:**
  - S:
    ```
    P05-O04 · S
    Car came in four minutes
    "Car came in four minutes." (A1)
    ```
  - W:
    ```
    P05-O12 · W
    <observation>
    (Note after A4)
    ```
    No quote and no `Inference:` line on W stickies, so the board shows what happened, not the interpretation.
- Leave the review marks (`· ✓ Approved`, `- Reviewer comment:`) off the stickies.
- Use the observation and anchor text exactly as written in the file. Do not shorten or rephrase.
- Send in batches if there are many stickies, and check after each batch that the count on the board matches.

## Output

1. Read the board back with `get_figjam` and check, per participant, that the number of green and yellow stickies matches the S and W counts sent.
2. In the chat, reply with a short summary only: the board link, stickies sent per participant (S / W), what was not sent and why (one line per flag group), and any mismatch from step 1.
3. Propose a project log line (see "Ask before logging" in `CLAUDE.md`).
