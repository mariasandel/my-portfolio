#!/usr/bin/env python3
"""Build data.json for the observation review page.

Reads the observation files in 01 Discover/Primary Research/Processed and the Transcript section
of each transcript in 01 Discover/Primary Research/Raw (never the Context Note
or Raw Field Notes, D05). Finds every anchor in the transcript so the page can
highlight it.

Usage (from the project root):
    python3 .claude/skills/review-observations/build_review_data.py OUT.json [Name ...]
No names = every transcript that has an observation file.
"""
import datetime
import json
import re
import sys
from pathlib import Path

RAW = Path("01 Discover/Primary Research/Raw")
PROCESSED = Path("01 Discover/Primary Research/Processed")

OBS_RE = re.compile(r"^(\d+)\. \*\*(P\d+-O\d+)\*\* · ([SWI]) — (.*)$")
FIELD_RE = re.compile(r"^\s+- (Anchor|Turn|Inference|Reviewer comment): (.*)$")
NOTE_RE = re.compile(r"^\*\[NOTE: (.*)\]\*$", re.S)
TURN_RE = re.compile(r"A(\d+)")


def latest_obs_file(name):
    files = list(PROCESSED.glob(f"01_Observations_{name}.md")) + list(
        PROCESSED.glob(f"01_Observations_{name}_v*.md"))
    if not files:
        return None

    def version(p):
        m = re.search(r"_v(\d+)\.md$", p.name)
        return int(m.group(1)) if m else 1
    return max(files, key=version)


def parse_transcript(path):
    text = path.read_text()
    header = {}
    for key in ("PROJECT", "PARTICIPANT", "FREQUENCY", "DATE"):
        m = re.search(rf"^{key}(?: \d+)?: (.*)$", text, re.M)
        header[key] = m.group(1).strip() if m else ""
    body = text.split("## Transcript", 1)[1]
    body = body.split("## Raw Field Notes", 1)[0]
    body = re.sub(r"\n---\s*$", "", body.strip())
    turns = []
    for block in re.split(r"\n\s*\n", body):
        block = block.strip()
        if not block or block == "---":
            continue
        if block.startswith("**") and block.endswith("**"):
            turns.append({"n": len(turns) + 1, "q": block.strip("*").strip(), "paras": []})
            continue
        if not turns:
            continue
        m = NOTE_RE.match(block)
        if m:
            turns[-1]["paras"].append({"kind": "note", "text": m.group(1).strip()})
        else:
            turns[-1]["paras"].append({"kind": "p", "text": block})
    return header, turns


def parse_observations(path):
    obs, review = [], ""
    cur = None
    for line in path.read_text().splitlines():
        if line.startswith("Review:"):
            review = line
        m = OBS_RE.match(line)
        if m:
            text = m.group(4).strip()
            flags = {"approx": "⚠ Approximate" in text, "remove": "✗ Remove" in text,
                     "approved": "✓ Approved" in text}
            for mark in ("· ✓ Approved", "✓ Approved", "⚠ Approximate", "✗ Remove"):
                text = text.replace(mark, "")
            cur = {"id": m.group(2), "tag": m.group(3), "text": text.strip(" ·"),
                   "anchor": "", "turn": "", "inference": "", "comment": "", **flags}
            obs.append(cur)
            continue
        m = FIELD_RE.match(line)
        if m and cur:
            key, val = m.group(1), m.group(2).strip()
            if key == "Anchor":
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                cur["anchor"] = val
            elif key == "Turn":
                cur["turn"] = val
            elif key == "Inference":
                cur["inference"] = val
            else:
                cur["comment"] = val
    return obs, review


def find_anchor(anchor, turns, turn_ref):
    """Return a list of {t, p, s, e} spans; empty if not found word for word."""
    if not anchor or anchor.lower().startswith("none"):
        return []
    m = TURN_RE.search(turn_ref)
    preferred = int(m.group(1)) if m else None
    order = sorted(turns, key=lambda t: (t["n"] != preferred, t["n"]))
    # A few anchors quote two separate sentences: "X." "Y."
    pieces = [anchor] + ([p for p in re.split(r'"\s+"', anchor) if p] if '" "' in anchor else [])
    for piece_set in ([pieces[0]], pieces[1:]):
        if not piece_set:
            continue
        spans = []
        for piece in piece_set:
            hit = None
            for t in order:
                for i, para in enumerate(t["paras"]):
                    s = para["text"].find(piece)
                    if s >= 0:
                        hit = {"t": t["n"], "p": i, "s": s, "e": s + len(piece)}
                        break
                if hit:
                    break
            if not hit:
                spans = []
                break
            spans.append(hit)
        if spans:
            return spans
    return []


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = Path(sys.argv[1])
    names = sys.argv[2:] or sorted(
        p.stem.split("_", 2)[2] for p in RAW.glob("01_Transcript_*.md"))
    data = {"generated": datetime.date.today().isoformat(), "project": "", "participants": []}
    problems = []
    for name in names:
        tpath = RAW / f"01_Transcript_{name}.md"
        opath = latest_obs_file(name)
        if not tpath.exists():
            problems.append(f"{name}: transcript missing ({tpath})")
            continue
        if not opath:
            problems.append(f"{name}: observation file missing")
            continue
        header, turns = parse_transcript(tpath)
        obs, review = parse_observations(opath)
        if not obs:
            problems.append(f"{name}: no tagged observations in {opath.name}")
            continue
        data["project"] = re.sub(r"^PROJECT \d+: ", "", header["PROJECT"]) or data["project"]
        pid, _, rest = header["PARTICIPANT"].partition(" — ")
        for o in obs:
            o["spans"] = find_anchor(o["anchor"], turns, o["turn"])
            if not o["spans"]:
                problems.append(f"{o['id']}: anchor not found word for word")
        data["participants"].append({
            "id": pid.strip(), "name": name, "profile": rest.strip(),
            "frequency": header["FREQUENCY"], "date": header["DATE"],
            "transcriptFile": str(tpath), "obsFile": str(opath), "review": review,
            "turns": turns, "observations": obs,
        })
    data["participants"].sort(key=lambda p: p["id"])
    out.write_text(json.dumps(data, ensure_ascii=False))
    total = sum(len(p["observations"]) for p in data["participants"])
    print(f"Wrote {out}: {len(data['participants'])} participants, {total} observations")
    for p in problems:
        print("FLAG:", p)


if __name__ == "__main__":
    main()
