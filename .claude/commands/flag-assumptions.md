---
description: Check every assumption against the S/W/I observations from one session and mark it Held, Challenged or Open
argument-hint: "[optional: participant name, e.g. Lena. Default: the most recent session]"
---

# Flag assumptions

## Input

1. **Assumption list:** read `00 Context/00_Assumptions.md` (made with `/map-assumptions`). If it does not exist, ask me to paste the list, or to run `/map-assumptions` first. Stop there.
2. **Session:** pick one participant.
   - If a name was given ($ARGUMENTS), use that participant.
   - If nothing was given, use the most recent session: the transcript in `01 Discover/Primary Research/Raw` with the latest `DATE` in its header. Say which session you picked and why.
3. **Observation list:** read `01 Discover/Primary Research/Processed/01_Observations_<Name>.md` (made with `/extract-observations`).
   - If it does not exist, stop and tell me to run `/extract-observations <Name>` first.
   - If its observations have no S/W/I tags, stop and tell me to re-run `/extract-observations <Name>` so they are tagged.

Use only the observation list as evidence. Do not read the transcript for evidence (the observations already carry the verbatim anchors), and never use the Context Note or Raw Field Notes (D05).

## Task

Mark each assumption as:

- **Held:** the session confirmed it
- **Challenged:** the session contradicted it or raised doubt
- **Open:** the session did not address it

For each verdict, cite the specific observation or quote that supports it.

## Rules

- **Do not mark an assumption as Held without a Supported (S) observation.** If only W observations point that way, mark it Open and note the W evidence ("leans held, W only").
- W observations can back a **Challenged** verdict. Say that the evidence is W and name the inference it rests on.
- Never use I (Invented) observations as evidence.
- Cite by observation ID and anchor, e.g. `P05-O14 (S): "I thought the price it shows you was the price you paid."`
- Go through **every** assumption in the list, in the list's order, keeping its number and ID (`A9`, `New`). Do not skip or merge any.
- If the session gives evidence both ways, mark it **Challenged** and cite both sides.
- One session can hold or challenge an assumption. It cannot prove or disprove it. Do not write "validated" or "disproved".
- Do not invent evidence. If nothing in the observations addresses an assumption, it is Open.

## Format

```markdown
# Assumption Check: <Participant ID> <Name>

Assumptions: `00 Context/00_Assumptions.md` · Observations: `01 Discover/Primary Research/Processed/01_Observations_<Name>.md` · Session date: <date> · Date: <today>

Held: n · Challenged: n · Open: n

| # | Assumption | Tag | Verdict | Evidence |
|---|------------|-----|---------|----------|
| 2 | Price matters to every buyer… | A6 · User | Challenged | P03-O17 (S): "…" |
| 3 | … | New · User | Open | No observation addresses it |

## Challenged: what to look at next
- #<n> <assumption>: <one line on what the session raised, with the observation ID>
```

### File name

Follow the naming rule in `CLAUDE.md`: `01_Assumption-Check_<Name>.md` (e.g. `01_Assumption-Check_Jonas.md`).

## Output

1. Before saving, check that every Held verdict cites at least one S observation, and that every cited ID and anchor matches the observation file.
2. Save the file in `01 Discover/Primary Research/Processed`. If it already exists, ask me whether to overwrite it or save a new version (`_v2`).
3. In the chat, reply with a short summary only: which session, the Held / Challenged / Open counts, the Challenged assumptions in one line each, and a link to the file.
