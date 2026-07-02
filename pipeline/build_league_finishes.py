#!/usr/bin/env python3
"""Parse the league's final-standings exports into league_finishes.csv.

Reads inputs/league-history/extracted/<year>_finish.txt (extracted from saved Yahoo
"Standings" pages via pipeline/extract_yahoo_mhtml.py). Yahoo's final standings table is:
  Rank / Team / W-L-T / PF / PA / Streak / Waiver / Moves
where Rank reflects FINAL finish including playoffs (the champion can have a worse W-L than
the 3rd-place team). Joins team -> manager via the same per-year managers files used by
build_draft_history.py. Reports anything unmappable instead of dropping it. Stdlib only.
"""
import csv
import glob
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_draft_history import parse_managers  # same per-year team->manager key

ROOT = Path(__file__).resolve().parent.parent
EXTRACTED = ROOT / "inputs" / "league-history" / "extracted"
OUT = ROOT / "inputs" / "league-history" / "league_finishes.csv"


def parse_standings(txt: Path) -> list[dict]:
    lines = [l.strip() for l in txt.read_text().splitlines()]
    # find the header sequence Rank/Team/W-L-T/PF/PA/Streak/Waiver/Moves
    start = None
    for i in range(len(lines) - 7):
        if lines[i] == "Rank" and lines[i + 1] == "Team" and lines[i + 2] == "W-L-T":
            start = i + 8
            break
    if start is None:
        raise ValueError(f"{txt.name}: standings header not found")
    rows = []
    i = start
    while i < len(lines) and len(rows) < 10:
        if not re.fullmatch(r"\*?\d+", lines[i]):
            i += 1
            continue
        rank = int(lines[i].lstrip("*"))
        j = i + 1
        while j < len(lines) and not lines[j]:
            j += 1
        team = lines[j]
        j += 1
        while j < len(lines) and not re.fullmatch(r"\d+-\d+-\d+", lines[j]):
            j += 1
        wlt = lines[j]
        pf, pa = float(lines[j + 1]), float(lines[j + 2])
        streak = lines[j + 3]
        waiver = lines[j + 4] if j + 4 < len(lines) else ""
        moves = lines[j + 5] if j + 5 < len(lines) else ""
        rows.append({"rank": rank, "team_name": team.replace("&amp;", "&"), "wlt": wlt,
                     "pf": pf, "pa": pa, "streak": streak, "waiver": waiver,
                     "moves": moves})
        i = j + 6
    return rows


def main() -> int:
    out_rows, issues = [], []
    for f in sorted(glob.glob(str(EXTRACTED / "*_finish.txt"))):
        f = Path(f)
        year = re.search(r"(\d{4})_finish", f.name).group(1)
        mgrs = parse_managers(EXTRACTED / f"{year}_managers.txt")
        try:
            rows = parse_standings(f)
        except ValueError as e:
            issues.append(str(e) + " -- skipped (wrong page saved? need the Standings tab)")
            continue
        if len(rows) != 10:
            issues.append(f"{year}: parsed {len(rows)} rows (expected 10)")
        for r in rows:
            mgr = mgrs.get(r["team_name"], "")
            if not mgr:
                issues.append(f"{year}: team '{r['team_name']}' unmapped")
            out_rows.append({"year": year, "manager": mgr, **r})

    with OUT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["year", "manager", "rank", "team_name", "wlt",
                                           "pf", "pa", "streak", "waiver", "moves"])
        w.writeheader()
        w.writerows(out_rows)
    print(f"Wrote {OUT} with {len(out_rows)} rows")
    for x in issues:
        print("ISSUE:", x)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
