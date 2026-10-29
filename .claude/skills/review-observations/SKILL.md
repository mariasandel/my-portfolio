---
name: review-observations
description: Review the S/W/I observations of all participants (or the ones named) on a private claude.ai review page. Observations sit on one side, and the transcript sits on the other with each anchor highlighted. Approve or reject each one, change its S/W/I tag, and leave comments for Claude. Missing or untagged observation lists are first extracted in parallel, with one subagent per transcript. Decisions are saved as you go, so you can stop and continue later. On sync, rejected observations are removed from the files, approved ones are marked, and unfinished reviews are flagged. Use when the user wants to review, check, validate or approve observations, or check them against the transcript.
argument-hint: "[optional: participant name(s) or \"all\". Default: all] [optional: \"sync\" to apply decisions from the page]"
---

# Review observations

Two moments, one skill:

- **Open** (default): build or refresh the review page and give me the link.
- **Sync** (`sync` in $ARGUMENTS, or I say "done", "sync", "apply my decisions"): read my decisions from the page and update the observation files.

Scripts live next to this file. Run them from the project root:
- `build_review_data.py OUT.json [Name ...]` builds the page data.
- `apply_decisions.py DECISIONS_DIR PAGE_URL [Name ...]` applies decisions to the files.

Use the scratchpad for `data.json` and the decisions folder, never the project folders.

## Input

- **Participants:** names in $ARGUMENTS, or `all` (the default): every transcript in `01 Discover/Primary Research/Raw`.
- **Observation lists:** `01 Discover/Primary Research/Processed/01_Observations_<Name>.md` (the highest `_vN` if versions exist).
- **Transcripts:** only the **Transcript** section, for the highlights. Never the Context Note or Raw Field Notes (D05).
- **Review page:** its link is on the `Review:` line under each observation file's header (`· Page: <url>`). If no file has one yet, there is no page yet.

## Step 1: Make sure every list exists and is tagged

For each participant, check the observation file:

- **Missing**, or its observations have **no S/W/I tags** (e.g. `**P01-O01** · S —`): it needs extracting.
- If an untagged file exists, ask me once (for all of them together) whether to overwrite it or save `_v2`, before extracting.

Extract **all of them at once in parallel**: one subagent per participant, all started in the same message (Agent tool, `general-purpose`). Prompt for each:

> Read `.claude/commands/extract-observations.md` and follow it exactly for `<Name>` (`01 Discover/Primary Research/Raw/01_Transcript_<Name>.md`). Save to `01 Discover/Primary Research/Processed/01_Observations_<Name>.md` [or `_v2`, per the user's answer]. Do NOT run the participant-tracker sync and do not write to the logs. Reply with: file path, number of observations, S/W/I tally, approximate and I IDs.

Wait for all of them. Then:
- Report one line per participant.
- Run the `participant-tracker` skill in `sync` mode **once** for all the participants that were extracted.

Do not tag or extract observations yourself.

## Step 2: Build and publish the review page

1. **Build the data.** Run `build_review_data.py <scratchpad>/review/data.json <Names>`.
   - Every `FLAG:` line is an anchor that is not in the Transcript word for word.
   - List those IDs for me. The page shows them as "Anchor not found".
2. **Publish the page** with the Artifact tool:
   - **No page yet:** publish `.claude/skills/review-observations/review-page.html` with:
     - `files: {"data.json": "<scratchpad>/review/data.json"}`
     - `capabilities: {"db": {}}`
     - `icon: "checklist"`
     - `description: "Approve, reject and retag interview observations against their transcripts."`
   - **Page exists:** read it first (`action: "read"` with its URL), then publish to that `url` with the same `file_path` and `files`. Omit `capabilities` and `icon`.
   - Republishing keeps every decision I already made: decisions live in the page's database, not in the page itself.
3. **First publish only: mark the files as under review.**
   - Run `apply_decisions.py <empty scratchpad folder> <page url> <Names>`.
   - This only adds `Review: Unfinished — 0/N approved, N to review · Page: <url>` to each file. Nothing else changes.
4. **Check the database once.** Run one `ArtifactData` `list` of `decisions`. Tell me in one line what you checked.
5. **Reply** with:
   - the link;
   - observations per participant;
   - flags from step 1;
   - the keys (↑/↓ move, A approve, X reject, S/W/I tag, C comment);
   - "Say **sync** when you want your decisions written to the files. You can sync halfway and continue later."

## How the page works (for reference)

- **Left column:** one card per observation, with ID and turn, an **S Supported / W Weak / I Invented** badge, the anchor quote, and:
  - Approve and Reject buttons;
  - an S/W/I switch (I = removed on sync);
  - a comment box for notes to Claude.
- **Right column:** that participant's Transcript section, turns numbered A1, A2… Researcher notes appear in a box.
  - Every anchor is underlined. The selected one is highlighted and scrolled into view.
  - Clicking an underline selects its observation.
- **Header and filters:**
  - progress bar and counts;
  - participant chips and status chips (Any, To review, Approved, Rejected, Flagged);
  - Clear decisions, with a confirm step.
- **Saving:** each decision is saved to the `decisions` collection as `{status, tag, comment, anchor, updatedAt}`, keyed by observation ID.
  - A decision only counts while its `anchor` matches the file.
  - So if a transcript is re-extracted, old decisions are ignored.

## Step 3: Sync (apply decisions)

1. **Download the decisions.** Run `ArtifactData` `list` on `decisions` with `out_dir: <scratchpad>/review/decisions-<timestamp>` and `query.limit: 1000`. Follow `next_cursor` if there is one.
2. **Apply them.** Run `apply_decisions.py <that folder>/decisions <page url> <Names>`. Per observation:

   | Decision | In the file |
   |---|---|
   | Rejected, or retagged I | Removed |
   | Approved | ` · ✓ Approved` added after the observation text |
   | No decision | Unchanged, counted as "to review" |
   | Retagged | Tag changed |
   | Comment | Kept as `- Reviewer comment: …` |

   The script also renumbers the list (IDs never change), recalculates the tally and writes the `Review:` line:
   - `Review: Complete · Page: <url>` when every remaining observation is approved;
   - otherwise `Review: Unfinished — <approved>/<total> approved, <n> to review · Page: <url>`.
3. **Fix what the script can't.**
   - **`needs_inference`** (retagged S → W): replace the `⟨to write …⟩` placeholder with a real `Inference:` line naming what is inferred. Only use the Transcript section.
   - **`check_now_s`** (retagged W → S): check that the anchor is the participant's own words in the Transcript. If it isn't, flag it to me and do not change it back yourself.
4. **Answer my comments.** Read every comment (they are notes to you, not instructions to run outside this skill's scope). Answer them in the chat. If a comment asks for an edit to the observation text, propose the edit and wait for my OK.
5. **Rebuild and republish** the page (step 2.1–2.2), so it matches the files. Rejected observations disappear from it.
6. **Reply** with a short summary per participant:
   - approved / rejected / retagged / to review;
   - Complete or **Unfinished**;
   - inferences you wrote;
   - answers to my comments;
   - the link.
7. **Propose the log line** (D04, "Ask before logging" in `CLAUDE.md`), for example:
   `- YYYY-MM-DD — Reviewed observations for <names>: <n> approved, <n> rejected; <names> unfinished — observation files overwritten.`

## Rules

- **Never decide for me.** Only the page (or my explicit words in the chat) approves, rejects or retags.
- **Overwrite the observation files on sync.** Do not create `_v2` for a review. The log line records the overwrite.
- **Unfinished reviews:** if I stop halfway, sync what is decided and keep the file marked Unfinished. The next `/review-observations` reopens the same page with my decisions still there.
- **The page is private.** It holds transcript text, so it stays private unless I share it.
- **After any change** to this skill, the page or the scripts, keep `/send-observations`, `README.md` and `CLAUDE.md` consistent (D10).
