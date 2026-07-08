#!/usr/bin/env python3
"""2025 positional scoring under THIS league's exact scoring formula
(pipeline/league_scoring.py), to inform two live draft questions:

  (1) QB edge: how much does an elite QB (QB3-5) outscore a streamer (QB10-14)
      in this 6pt-passing / 25-yds-per-point league, per game and per season?
  (2) RB-vs-WR scarcity at the top of the draft (relevant at pick #4).

Reads data/raw/player_stats_weekly.csv (nflverse offense, 2016-2025). Reuses the
loading + scoring pattern from pipeline/predictive_stats.py. Stdlib only.

Method: for the 2025 regular season, sum each player's per-week league points
into a season total, divide by games played for PPG, rank players within each
position by PPG (min-games filter applied), then report the PPG at named
positional-rank tiers and the drop-off between tiers.

Known gap (inherited from league_scoring.offense_points): the 40+ yard
run/reception bonuses (+2 each) and offensive fumble-return TDs are NOT
computable from weekly aggregate data, so every PPG below slightly under-counts
real league points by a boom-play-dependent amount.
"""
import csv
import sys
from pathlib import Path

from league_scoring import offense_points

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
SEASON = 2025
MIN_GAMES = 8  # exclude injury-shortened / cup-of-coffee lines from tier ranks
POSITIONS = ("QB", "RB", "WR", "TE")

# Which rank tiers to report per position (1-indexed positional rank by PPG).
TIERS = {
    "QB": [1, 6, 12, 18, 24],
    "RB": [1, 6, 12, 24, 36],
    "WR": [1, 6, 12, 24, 36],
    "TE": [1, 6, 12],
}


def load_rows(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def aggregate_2025_regular(rows: list[dict]) -> dict:
    """(pid) -> {name, position, games, total, ppg} for 2025 REG only."""
    by_player: dict = {}
    for row in rows:
        if row.get("season") != str(SEASON):
            continue
        if row.get("season_type") != "REG":
            continue
        pos = row.get("position")
        if pos not in POSITIONS:
            continue
        pid = row.get("player_id")
        if not pid:
            continue
        rec = by_player.setdefault(
            pid,
            {
                "name": row.get("player_display_name") or row.get("player_name") or pid,
                "position": pos,
                "games": 0,
                "total": 0.0,
            },
        )
        rec["games"] += 1
        rec["total"] += offense_points(row)
    for rec in by_player.values():
        rec["ppg"] = rec["total"] / rec["games"] if rec["games"] else 0.0
    return by_player


def ranked_by_position(by_player: dict) -> dict:
    """position -> list of player records sorted by PPG desc, min-games filtered."""
    out: dict = {p: [] for p in POSITIONS}
    for rec in by_player.values():
        if rec["games"] >= MIN_GAMES:
            out[rec["position"]].append(rec)
    for p in out:
        out[p].sort(key=lambda r: r["ppg"], reverse=True)
    return out


def tier_ppg(ranked: list[dict], rank: int) -> float | None:
    """PPG of the player at 1-indexed positional rank, or None if not that deep."""
    if rank <= len(ranked):
        return ranked[rank - 1]["ppg"]
    return None


def mean_ppg_range(ranked: list[dict], lo: int, hi: int) -> float | None:
    """Mean PPG across positional ranks lo..hi inclusive (1-indexed)."""
    picks = [r["ppg"] for r in ranked[lo - 1 : hi]]
    return sum(picks) / len(picks) if picks else None


def fmt(v) -> str:
    return f"{v:.1f}" if v is not None else "n/a"


def build_report(ranked: dict) -> tuple[list[str], dict]:
    lines: list[str] = []
    computed: dict = {}

    lines.append(f"# 2025 positional value under league scoring (min {MIN_GAMES} games)")
    lines.append("")
    for pos in POSITIONS:
        rl = ranked[pos]
        lines.append(f"## {pos}  (qualified players: {len(rl)})")
        lines.append("")
        lines.append(f"| Tier | Player | PPG | Drop from prev tier |")
        lines.append("|---|---|---|---|")
        prev = None
        pos_rows = []
        for rank in TIERS[pos]:
            if rank <= len(rl):
                rec = rl[rank - 1]
                ppg = rec["ppg"]
                drop = f"-{prev - ppg:.1f}" if prev is not None else "-"
                lines.append(f"| {pos}{rank} | {rec['name']} | {ppg:.1f} | {drop} |")
                pos_rows.append({"tier": f"{pos}{rank}", "player": rec["name"], "ppg": ppg})
                prev = ppg
            else:
                lines.append(f"| {pos}{rank} | (not {rank} deep) | n/a | - |")
        lines.append("")
        computed[pos] = pos_rows

    # QB elite-vs-streamer swing
    qb = ranked["QB"]
    elite = mean_ppg_range(qb, 3, 5)
    streamer = mean_ppg_range(qb, 10, 14)
    lines.append("## QB elite-vs-streamer swing")
    lines.append("")
    if elite is not None and streamer is not None:
        gap = elite - streamer
        lines.append(f"- Mean PPG of QB3-5 (elite): {elite:.1f}")
        lines.append(f"- Mean PPG of QB10-14 (streamer): {streamer:.1f}")
        lines.append(f"- Per-game gap: {gap:.1f}")
        lines.append(f"- Per-season swing (x17 games): {gap * 17:.0f} points")
        computed["qb_swing"] = {
            "elite_ppg": elite,
            "streamer_ppg": streamer,
            "gap_ppg": gap,
            "season_swing_17": gap * 17,
        }
    else:
        lines.append("- Not enough qualified QBs to compute the QB3-5 vs QB10-14 gap.")
    lines.append("")

    return lines, computed


def main() -> int:
    off_path = RAW / "player_stats_weekly.csv"
    if not off_path.exists():
        print(f"{off_path} does not exist. Run pipeline/fetch_data.py first.", file=sys.stderr)
        return 1

    rows = load_rows(off_path)
    by_player = aggregate_2025_regular(rows)
    ranked = ranked_by_position(by_player)
    lines, _ = build_report(ranked)

    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
