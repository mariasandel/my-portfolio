# Where to read and save files: 00 Context vs 01 Discover

The fix is to pick **one rule for where a file belongs**, then make every command follow it for reading as well as saving. In my Design OS that rule is **time**:

> **Did this exist before I spoke to a participant?**
> Yes → `00 Context` · No, it came from the interviews → `01 Discover`

## `00 Context`: everything before the interviews

- The brief and its interrogation
- Assumptions, space map, screener, discussion guide
- Notes on decisions made at that stage

## `01 Discover`: everything that comes from the interviews

- `Primary Research`: research with participants
  - `Raw`: transcripts, exactly as recorded. They are never edited.
  - `Processed`: what I build from them, like observations and assumption checks
- `Secondary Research`: desk research done during Discover, like alternatives and analogous domains
- The participant tracker

## Reading follows the same rule

This is the part that cleans things up:

- **Pre-interview tools read only `00 Context`** (my decision D06). Assumption mapping, research planning, question drafting, the space map and the guide must not be shaped by what participants later said. Otherwise you're "preparing" with hindsight.
- **Post-interview tools read `01 Discover`.** They can pull one specific file from `00 Context` when comparing is the point. For example, `/flag-assumptions` takes `00_Assumptions.md` and checks it against one participant's observations. The result goes to `01 Discover/Primary Research/Processed`, because it's built from interview data.
- **Synthesis tools (`/frame-problem`) don't read `00 Context` at all.** That keeps problem statements based on evidence, not on the brief.

## One exception, written down on purpose (D09)

My discussion guide sits in `00 Context`, but I rebuilt it from the transcripts after the interviews. So every pre-interview tool has an explicit line telling it to skip that file. Exceptions are fine; hidden ones are where the mess comes from.

## To fix yours

1. Write the rule, and the list of folders and subfolders, in your `CLAUDE.md`.
2. In every command or skill, state three things explicitly:
   - **Read:** the exact paths it reads
   - **Do not read:** the paths it must ignore
   - **Save to:** the exact path and file name
3. Log the rule as a decision so Claude doesn't drift from it later.
4. Go through your commands one by one and check that paths match the folders that actually exist.
