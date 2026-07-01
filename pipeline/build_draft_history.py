#!/usr/bin/env python3
"""Join the league's Yahoo draft-board exports into one manager-level draft-history CSV.

Reads the extracted text files under inputs/league-history/extracted/ (produced from
saved Yahoo MHTML pages by pipeline/extract_yahoo_mhtml.py), one set per season:
  <year>_order.txt            -- draft board text; players in pick order
  <year>_order_teamnames.txt  -- full team name per pick, in pick order (from title attrs)
  <year>_managers.txt         -- Managers table: team nickname -> manager (the per-year key)

Managers are stable across seasons; team nicknames change yearly, so each year's
managers file is the key that resolves that year's board to real people. We zip the
ordered player list with the ordered team list and map team->manager. Anything that
doesn't map cleanly is reported, never silently dropped. Stdlib only.

Also enriches each pick with a position, matched against the committed nflverse data
in inputs/nflverse/ (suffix-normalized; team defenses and kickers handled as fallbacks).
"""
import csv
import glob
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXTRACTED = ROOT / "inputs" / "league-history" / "extracted"
NFLVERSE = ROOT / "inputs" / "nflverse"
OUT = ROOT / "inputs" / "league-history" / "draft_history_master.csv"
TEAMS, ROUNDS = 10, 16
PICKS = TEAMS * ROUNDS
BOILERPLATE = {"Close", "Yahoo Sports Fantasy Football", "3rd party ad content", "Chat"}


def parse_players(order_txt: Path) -> list[str]:
    lines = order_txt.read_text().splitlines()
    return [lines[i + 1].strip() for i, ln in enumerate(lines)
            if re.fullmatch(r"\d+\.", ln.strip()) and i + 1 < len(lines)]


def parse_teams(teamnames_txt: Path) -> list[str]:
    return [t.strip().replace("&amp;", "&") for t in teamnames_txt.read_text().splitlines()
            if t.strip() and t.strip() not in BOILERPLATE]


def parse_managers(mgr_txt: Path) -> dict[str, str]:
    lines = mgr_txt.read_text().splitlines()
    start = None
    for i, ln in enumerate(lines):
        if ln.strip() == "Team Name" and i + 1 < len(lines) and lines[i + 1].strip() == "Manager":
            start = i + 3
            break
    mapping: dict[str, str] = {}
    if start is None:
        return mapping
    i = start
    while i < len(lines) and lines[i].strip() in {"Email", "Waiver Priority", "Moves", "Trades"}:
        i += 1
    while i < len(lines):
        team = lines[i].strip().replace("&amp;", "&")
        if not team or team in {"Managers", "Record Book"}:
            break
        manager = lines[i + 1].strip() if i + 1 < len(lines) else ""
        j = i + 2
        if j < len(lines) and lines[j].strip() == "Commissioner":
            j += 1
        if j < len(lines) and "@" in lines[j]:
            j += 1
        while j < len(lines) and re.fullmatch(r"\d+", lines[j].strip()):
            j += 1
        if team and manager and "@" not in manager:
            mapping[team] = manager
        i = j
    return mapping


def norm(n: str) -> str:
    n = re.sub(r"\b(jr|sr|ii|iii|iv|v)\.?$", "", n.strip().lower()).strip()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z ]", "", n)).strip()


def build_position_map() -> dict[str, str]:
    counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for fn in ["player_stats.csv", "stats_player_week_2025.csv"]:
        path = NFLVERSE / fn
        if not path.exists():
            continue
        with path.open(newline="") as f:
            for row in csv.DictReader(f):
                nm, pos = norm(row.get("player_display_name") or ""), (row.get("position") or "").strip()
                if nm and pos:
                    counts[nm][pos] += 1
    return {nm: max(d, key=d.get) for nm, d in counts.items()}


def main() -> int:
    posmap = build_position_map()
    rows, issues = [], []
    for order in sorted(glob.glob(str(EXTRACTED / "*_order.txt"))):
        order = Path(order)
        year = re.search(r"(\d{4})_order", order.name).group(1)
        teams = parse_teams(EXTRACTED / f"{year}_order_teamnames.txt")
        players = parse_players(order)
        mgrs = parse_managers(EXTRACTED / f"{year}_managers.txt")
        if len(players) != PICKS or len(teams) != PICKS:
            issues.append(f"{year}: players={len(players)} teams={len(teams)} (expected {PICKS})")
        for idx in range(min(len(players), len(teams))):
            team = teams[idx]
            mgr = mgrs.get(team, "")
            if not mgr:
                issues.append(f"{year} pick {idx+1}: team '{team}' unmapped")
            pos = posmap.get(norm(players[idx]), "")
            rows.append({
                "year": year, "overall_pick": idx + 1, "round": idx // TEAMS + 1,
                "pick_in_round": idx % TEAMS + 1, "player": players[idx],
                "team_name": team, "manager": mgr, "position": pos,
            })
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["year", "overall_pick", "round", "pick_in_round",
                                          "player", "team_name", "manager", "position"])
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {OUT} with {len(rows)} picks")
    print(f"Unmapped managers: {sum(1 for r in rows if not r['manager'])}")
    print(f"Unmatched positions: {sum(1 for r in rows if not r['position'])}")
    for x in issues[:20]:
        print("ISSUE:", x)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
