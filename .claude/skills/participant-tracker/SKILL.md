---
name: participant-tracker
description: Create and keep up to date a participant tracker for the project, kept as a local markdown file (01 Discover/01_Participant-Tracker.md) and mirrored to a Google Sheet. "create" builds it from the participant profile in 00 Context; "sync" updates each participant's row from the files in 01 Discover (transcript added, observations extracted). Other commands call sync at the end of their run. Use when the user wants a participant tracker, recruitment tracker or interview status overview, or asks to update or sync it.
argument-hint: "[create | sync] [optional: participant name]"
---

# Participant tracker

Two copies, one source of truth:

- **Local copy (source of truth):** `01 Discover/01_Participant-Tracker.md`. It holds the table and the Google Sheet link. Later sessions read this file, not the sheet.
- **Google Sheet (mirror):** the same table, for viewing and sharing. Its link is saved at the top of the local copy.

Modes: `create` or `sync` ($ARGUMENTS). If no mode is given: run `sync` if the local copy exists, otherwise `create`. A participant name after `sync` (e.g. `sync Lena`) updates that row only.

Before any Google Sheets call, load the `google-workspace` skill and read its `references/sheets.md`.

## Columns

Fixed columns, in this order:

| Column | Filled by | Source |
|---|---|---|
| ID | sync | `PARTICIPANT` line in the transcript header (e.g. `P01`), or from the profile |
| Name | create | Participant profile / brief |
| Status | me (sync can set Completed) | `Recruiting` / `Scheduled` / `Completed` / `No-show` |
| Screener score | me | From `/write-screener` results |
| Session date | sync, or me | `DATE` line in the transcript header |
| Recording link | me | |
| Progress | sync | `Not started` → `Transcript added` → `Observations extracted` (extend as later phases add steps) |
| Transcript file | sync | Link to `01 Discover/Primary Research/Raw/01_Transcript_<Name>.md` |
| Observation file | sync | Link to `01 Discover/Primary Research/Processed/01_Observations_<Name>.md` |
| Key quote | sync (only if empty), or me | One verbatim sentence from the **Transcript section** only (see D05) |
| Notes | me | |

**Profile columns:** add the columns the participant profile supports, placed after Name. With the current context these are **City**, **Age**, **Occupation**, **Ride frequency** and **Main use** (from the brief and the transcript headers). If the profile names other criteria (e.g. gender, platform iOS/Android, rides at night), add a column for each. Do not add columns for data nobody has; list them as suggestions instead.

## Create

1. Read everything in `00 Context/`, especially the **participant profile** and **recruiting criteria** (a file with `Participant`, `Profile`, `Recruiting`, `Criteria` or `Screener` in its name, or participant sections in other files). If there is no profile, use the participants named in the brief and say so.
2. If `01 Discover/01_Participant-Tracker.md` already exists, stop: show what it contains and ask whether to run `sync` instead or rebuild it.
3. Propose the column list (fixed + profile columns, and suggested extra columns with the reason for each) and the starting rows. **Wait for my OK** before creating anything.
4. After my OK:
   - Write the local copy (format below).
   - Run one `sync` pass so existing transcripts and observation files are filled in.
   - Create the Google Sheet titled `Participant Tracker: <project name from the brief>`: use the Sheets connector if it is on (create, write the header and rows, bold and freeze the header row); otherwise use Drive `create_file` with the table as CSV (`contentMimeType: text/csv`) so it converts to a Sheet.
   - Save the sheet link at the top of the local copy.
5. Reply with a link to the local file and the sheet, and propose a project log line (see "Ask before logging" in `CLAUDE.md`).

## Sync

1. Read the local copy. If it does not exist, say so and offer `create`. Stop.
2. **Pull my edits from the sheet first** (only if the Sheets connector is on): read the sheet's values. For columns filled by **me** (Status, Screener score, Session date, Recording link, Key quote, Notes), copy any value I typed in the sheet into the local copy. If the sheet and the local copy disagree on one of these, show both and ask which to keep.
3. Scan `01 Discover/`:
   - `Primary Research/Raw/01_Transcript_<Name>.md` exists → Progress at least `Transcript added`; fill ID, Session date and profile columns from the transcript header; set Status to `Completed` unless it is `No-show`.
   - `Primary Research/Processed/01_Observations_<Name>.md` exists → Progress `Observations extracted`; fill Observation file.
   - A transcript for someone not in the tracker → add a row and say so.
   - A row whose file was removed or renamed → do not delete the row; flag it.
4. **Key quote:** fill only if empty. Pick one sentence from the Transcript section that is copied word for word and reflects what the participant talked about most; mark it `(suggested)`. Never overwrite a quote I wrote.
5. Never overwrite a value I filled in with a value derived from files, except Progress and the file links.
6. Write the local copy, then push the full table to the sheet:
   - **Sheets connector on:** write the values to the same sheet (same link). Read it again to check.
   - **Sheets connector off:** do **not** create a new sheet. Update the local copy only and say: "The Google Sheet is out of date. Turn on the Google Sheets connector and run `/participant-tracker sync` to update it (same link)."
7. Reply in a few lines: which rows changed and how, anything flagged. Do not propose a log line for a routine sync; only for a new participant or a status change to `No-show`.

## Local copy format

```markdown
# Participant tracker

Google Sheet: <link, or "not created yet"> · Last sync: <YYYY-MM-DD> · Sheet in sync: <yes / no, connector off>

| ID | Name | City | Age | ... | Status | Screener score | Session date | Recording link | Progress | Transcript file | Observation file | Key quote | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Lena | Berlin | 34 | ... | Completed | | 2026-10-16 | | Observations extracted | [Transcript](Primary%20Research/Raw/01_Transcript_Lena.md) | [Observations](Primary%20Research/Processed/01_Observations_Lena.md) | "…" (suggested) | |
```

Dates as `YYYY-MM-DD`. Empty cells stay empty; do not write `n/a` or `TBD`.

## Called from other commands

Commands that change a participant's files end with: "Run the `participant-tracker` skill in `sync` mode for <Name>." When called this way, sync that row only, keep the reply to one line, and skip step 2 if the Sheets connector is off. If the tracker does not exist yet, say so in one line and do not create it.
