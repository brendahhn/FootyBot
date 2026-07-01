#!/usr/bin/env python3
"""Realized outcomes: did each manager's picks -- and each archetype of pick -- actually
return value in the season they were drafted for?

Value metric: the player's REG-season TOTAL fantasy points (this league's scoring) in the
draft year, compared to the MEDIAN total points of all players drafted in that same round
that same year ("round-relative delta"). Total points (not PPG) on purpose: missing games IS
part of the realized outcome of a pick. "Hit" = beat the round median.

This measures DRAFT-VALUE success, not league standings (we don't have final standings data;
if Brendan supplies standings pages, correlate directly). Rounds 1-8, skill positions only.
Recency note: per Brendan 2026-07-02, weight 2025 heaviest when describing CURRENT habits --
the habit tables print both all-years and 2024-2025-only views for that reason. Stdlib only.
"""
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path
from statistics import median

sys.path.insert(0, str(Path(__file__).resolve().parent))
from league_scoring import offense_points

ROOT = Path(__file__).resolve().parent.parent
NFLVERSE = ROOT / "inputs" / "nflverse"
HISTORY = ROOT / "inputs" / "league-history"
SKILL = {"QB", "RB", "WR", "TE"}
MAX_ROUND = 8
FLAGS = ["ROOKIE", "SECOND_YEAR", "BREAKOUT_CHASE", "POST_INJURY", "BOOM_BUST",
         "AGING_VET", "STEADY"]


def norm(n: str) -> str:
    n = re.sub(r"\b(jr|sr|ii|iii|iv|v)\.?$", "", n.strip().lower()).strip()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z ]", "", n)).strip()


ALIASES = {"hollywood brown": "marquise brown", "kenny gainwell": "kenneth gainwell",
           "joshua palmer": "josh palmer"}


def load_season_totals() -> dict:
    """norm(name) -> season -> REG-season total points under league scoring."""
    out: dict = defaultdict(lambda: defaultdict(float))
    for fn in ["player_stats.csv", "stats_player_week_2025.csv"]:
        path = NFLVERSE / fn
        if not path.exists():
            continue
        with path.open(newline="") as f:
            for row in csv.DictReader(f):
                if (row.get("season_type") or "REG") != "REG":
                    continue
                nm = norm(row.get("player_display_name") or "")
                if not nm:
                    continue
                try:
                    season = int(row["season"])
                except (KeyError, ValueError):
                    continue
                out[nm][season] += offense_points(row)
    return out


def main() -> int:
    totals = load_season_totals()
    picks = [r for r in csv.DictReader((HISTORY / "draft_history_enriched.csv").open())
             if int(r["round"]) <= MAX_ROUND and r["position"] in SKILL]

    # realized points for each pick, and round medians per (year, round)
    by_year_round = defaultdict(list)
    for r in picks:
        key = ALIASES.get(norm(r["player"]), norm(r["player"]))
        pts = totals.get(key, {}).get(int(r["year"]), 0.0)
        r["_pts"] = pts
        by_year_round[(r["year"], r["round"])].append(pts)
    medians = {k: median(v) for k, v in by_year_round.items()}
    for r in picks:
        med = medians[(r["year"], r["round"])]
        r["_delta"] = r["_pts"] - med
        r["_hit"] = r["_pts"] > med

    def profile(subset, label):
        print(f"\n=== {label} ===")
        print("manager | picks | hit rate | avg round-relative delta (pts)")
        for m in sorted(set(r["manager"] for r in subset)):
            mine = [r for r in subset if r["manager"] == m]
            hits = sum(r["_hit"] for r in mine)
            avg = sum(r["_delta"] for r in mine) / len(mine)
            print(f"{m:9}| {len(mine):3}  | {100*hits/len(mine):4.0f}%   | {avg:+6.1f}")

    profile(picks, "MANAGER DRAFT-VALUE, all years 2019-2025 (rounds 1-8, skill)")
    recent = [r for r in picks if r["year"] in ("2024", "2025")]
    profile(recent, "MANAGER DRAFT-VALUE, 2024-2025 only (recency view)")

    print("\n=== ARCHETYPE OUTCOMES, league-wide ===")
    print("flag | picks | hit rate | avg delta")
    for fl in FLAGS:
        sub = [r for r in picks if fl in (r["flags"] or "")]
        if not sub:
            continue
        hits = sum(r["_hit"] for r in sub)
        avg = sum(r["_delta"] for r in sub) / len(sub)
        print(f"{fl:15}| {len(sub):3} | {100*hits/len(sub):4.0f}% | {avg:+6.1f}")

    print("\n=== BRENDAN'S ARCHETYPE OUTCOMES (vs league) ===")
    print("flag | his picks | his hit rate | his avg delta | league hit rate")
    for fl in FLAGS:
        sub_all = [r for r in picks if fl in (r["flags"] or "")]
        sub_b = [r for r in sub_all if r["manager"] == "Brendan"]
        if not sub_b:
            continue
        hb = sum(r["_hit"] for r in sub_b)
        ha = sum(r["_hit"] for r in sub_all)
        avg_b = sum(r["_delta"] for r in sub_b) / len(sub_b)
        print(f"{fl:15}| {len(sub_b):2} | {100*hb/len(sub_b):4.0f}% | {avg_b:+6.1f} | {100*ha/len(sub_all):4.0f}%")

    print("\n=== BRENDAN'S 10 BEST AND WORST PICKS (round-relative) ===")
    mine = sorted([r for r in picks if r["manager"] == "Brendan"], key=lambda r: -r["_delta"])
    for r in mine[:10]:
        print(f'  +{r["_delta"]:6.1f}  {r["year"]} R{r["round"]:>2} {r["player"]} [{r["flags"] or "-"}]')
    print("  ...")
    for r in mine[-10:]:
        print(f'  {r["_delta"]:+7.1f}  {r["year"]} R{r["round"]:>2} {r["player"]} [{r["flags"] or "-"}]')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
