#!/usr/bin/env python3
"""Apply the review page's decisions to the observation files.

DECISIONS_DIR is the folder ArtifactData `list` wrote with `out_dir`
(one JSON file per observation ID, e.g. decisions/P01-O04.json).
A decision only counts when its saved anchor matches the observation's
current anchor (so decisions on an older extraction are ignored).

Usage (from the project root):
    python3 .claude/skills/review-observations/apply_decisions.py DECISIONS_DIR PAGE_URL [Name ...]
Prints a JSON summary per participant.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_review_data import OBS_RE, latest_obs_file, RAW  # noqa: E402

TODO_INFERENCE = "⟨to write: retagged S → W in review⟩"


def load_decisions(folder):
    out = {}
    for f in Path(folder).rglob("*.json"):
        doc = json.loads(f.read_text())
        body = doc.get("data") if isinstance(doc.get("data"), dict) else doc
        out[f.stem] = body
    return out


def split_blocks(lines):
    """Return (head, blocks, tail): blocks are lists of lines, one per observation."""
    head, blocks, tail = [], [], []
    for line in lines:
        if OBS_RE.match(line):
            blocks.append([line])
        elif re.match(r"^(S|W|I): \d+", line):
            tail.append(line)
        elif blocks and not tail:
            blocks[-1].append(line)
        elif tail:
            tail.append(line)
        else:
            head.append(line)
    return head, blocks, tail


def apply(name, decisions, url):
    path = latest_obs_file(name)
    if not path:
        return {"participant": name, "error": "observation file missing"}
    head, blocks, _ = split_blocks(path.read_text().splitlines())
    kept, summary = [], {"participant": name, "file": str(path), "approved": 0,
                         "rejected": [], "retagged": [], "needs_inference": [],
                         "check_now_s": [], "comments": [], "undecided": 0}
    for block in blocks:
        m = OBS_RE.match(block[0])
        oid, tag, text = m.group(2), m.group(3), m.group(4)
        fields = [l for l in block[1:] if l.strip()]
        anchor = next((l.split("Anchor:", 1)[1].strip() for l in fields if "- Anchor:" in l), "")
        if anchor.startswith('"') and anchor.endswith('"'):
            anchor = anchor[1:-1]
        d = decisions.get(oid)
        if d and d.get("anchor") != anchor:
            d = None
        approved = "✓ Approved" in text
        if d:
            new_tag = d.get("tag") or tag
            status = d.get("status")
            if status == "rejected" or new_tag == "I":
                summary["rejected"].append(oid)
                continue
            if new_tag != tag:
                summary["retagged"].append(f"{oid} {tag}→{new_tag}")
                if new_tag == "W" and not any("- Inference:" in l for l in fields):
                    fields.append(f"   - Inference: {TODO_INFERENCE}")
                    summary["needs_inference"].append(oid)
                if new_tag == "S":
                    fields = [l for l in fields if "- Inference:" not in l]
                    summary["check_now_s"].append(oid)
                tag = new_tag
            approved = status == "approved"
            comment = (d.get("comment") or "").strip().replace("\n", " ")
            fields = [l for l in fields if "- Reviewer comment:" not in l]
            if comment:
                fields.append(f"   - Reviewer comment: {comment}")
                summary["comments"].append(f"{oid}: {comment}")
        text = text.replace(" · ✓ Approved", "").replace("✓ Approved", "").rstrip()
        if approved:
            text += " · ✓ Approved"
            summary["approved"] += 1
        else:
            summary["undecided"] += 1
        kept.append((oid, tag, text, fields))

    # Rebuild the file: header, review line, renumbered observations, tally.
    head = [l for l in head if not l.startswith("Review:")]
    while head and not head[-1].strip():
        head.pop()
    total = len(kept)
    if summary["undecided"] == 0:
        review = "Review: Complete"
    else:
        review = (f"Review: Unfinished — {summary['approved']}/{total} approved, "
                  f"{summary['undecided']} to review")
    review += f" · Page: {url}"
    out = head + ["", review, ""]
    for i, (oid, tag, text, fields) in enumerate(kept, 1):
        pad = " " * (len(str(i)) + 2)
        fields = [pad + l.strip() for l in fields]
        out += [f"{i}. **{oid}** · {tag} — {text}"] + fields + [""]
    counts = {t: sum(1 for k in kept if k[1] == t) for t in "SWI"}
    out.append(f"S: {counts['S']} · W: {counts['W']} · I: {counts['I']}")
    path.write_text("\n".join(out) + "\n")
    summary["status"] = review.split(" · Page:")[0]
    summary["tally"] = counts
    return summary


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    decisions = load_decisions(sys.argv[1])
    url = sys.argv[2]
    names = sys.argv[3:] or sorted(
        p.stem.split("_", 2)[2] for p in RAW.glob("01_Transcript_*.md"))
    print(json.dumps([apply(n, decisions, url) for n in names], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
