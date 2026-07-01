#!/usr/bin/env python3
"""Enrich each historical league draft pick with what the player LOOKED LIKE at the time
of that draft — the "thought process" layer of opponent modeling.

For a pick of player P in fantasy year Y, we reconstruct P's profile entering Y from the
committed nflverse data (1999-2025, inputs/nflverse/), scored with THIS league's formula:

  - experience_at_pick: Y - first NFL season with stats (0 = rookie/never played)
  - g_prev / ppg_prev:  games + league-scoring PPG in season Y-1
  - ppg_prev2:          PPG in season Y-2 (for trajectory)
  - cv_prev:            weekly coefficient of variation in Y-1 (boom/bust-ness)

And derive archetype flags (definitions are explicit choices, documented here, not claims
of ground truth — tune them in one place below):

  ROOKIE          no NFL stats before Y (skill positions only)
  SECOND_YEAR     exactly 1 prior season (the "year-2 leap" bet)
  BREAKOUT_CHASE  Y-1 was the player's first startable season (ppg_prev >= 11, >= 8 games,
                  and ppg_prev2 < 8 or no Y-2) -- i.e. drafting last year's breakout
  POST_INJURY     established player coming off a lost/shortened year
                  (g_prev <= 9 but >= 8 games in Y-2)
  BOOM_BUST       high weekly variance in Y-1 (cv_prev >= 0.75, >= 8 games, ppg_prev >= 8)
  AGING_VET       8+ prior seasons (RB: 7+)
  STEADY          >= 12 games in Y-1, cv_prev <= 0.55, ppg_prev >= 10 -- the "safe" pick

Flags are not mutually exclusive (a pick can be BREAKOUT_CHASE and BOOM_BUST).
Writes inputs/league-history/draft_history_enriched.csv and prints per-manager profiles
for rounds 1-8 (the rounds where a pick reflects a real decision, not a dart throw).
Stdlib only.
"""
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean, pstdev

sys.path.insert(0, str(Path(__file__).resolve().parent))
from league_scoring import offense_points

ROOT = Path(__file__).resolve().parent.parent
NFLVERSE = ROOT / "inputs" / "nflverse"
HISTORY = ROOT / "inputs" / "league-history"
SKILL = {"QB", "RB", "WR", "TE"}

# --- tunable archetype thresholds (documented in module docstring) ---
BREAKOUT_PPG, BREAKOUT_MIN_G, BREAKOUT_PRIOR_PPG = 11.0, 8, 8.0
INJURY_MAX_G, INJURY_PRIOR_MIN_G = 9, 8
BOOMBUST_CV, BOOMBUST_MIN_G, BOOMBUST_MIN_PPG = 0.75, 8, 8.0
AGING_EXP, AGING_EXP_RB = 8, 7
STEADY_MIN_G, STEADY_MAX_CV, STEADY_MIN_PPG = 12, 0.55, 10.0
ANALYSIS_MAX_ROUND = 8


def norm(n: str) -> str:
    n = re.sub(r"\b(jr|sr|ii|iii|iv|v)\.?$", "", n.strip().lower()).strip()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z ]", "", n)).strip()


ALIASES = {"hollywood brown": "marquise brown", "kenny gainwell": "kenneth gainwell",
           "joshua palmer": "josh palmer"}


def load_weekly_points() -> dict:
    """norm(name) -> season -> list of weekly league-scoring points (REG season only)."""
    out: dict = defaultdict(lambda: defaultdict(list))
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
                out[nm][season].append(offense_points(row))
    return out


def season_summary(weeks: list) -> tuple:
    g = len(weeks)
    ppg = mean(weeks) if weeks else 0.0
    cv = (pstdev(weeks) / ppg) if g >= 2 and ppg > 0 else None
    return g, ppg, cv


def main() -> int:
    weekly = load_weekly_points()
    first_season = {nm: min(seasons) for nm, seasons in weekly.items() if seasons}

    picks = list(csv.DictReader((HISTORY / "draft_history_master.csv").open()))
    enriched = []
    for r in picks:
        year = int(r["year"])
        key = norm(r["player"])
        key = ALIASES.get(key, key)
        pos = r["position"] or ""
        e = dict(r)
        e.update({"experience_at_pick": "", "g_prev": "", "ppg_prev": "", "ppg_prev2": "",
                  "cv_prev": "", "flags": ""})
        if pos in SKILL and key in weekly:
            fs = first_season.get(key, year)
            exp = max(0, year - fs)
            g1, ppg1, cv1 = season_summary(weekly[key].get(year - 1, []))
            g2, ppg2, _ = season_summary(weekly[key].get(year - 2, []))
            flags = []
            if exp == 0:
                flags.append("ROOKIE")
            elif exp == 1:
                flags.append("SECOND_YEAR")
            if (g1 >= BREAKOUT_MIN_G and ppg1 >= BREAKOUT_PPG
                    and (ppg2 < BREAKOUT_PRIOR_PPG or g2 == 0) and exp >= 1):
                flags.append("BREAKOUT_CHASE")
            if exp >= 2 and g1 <= INJURY_MAX_G and g2 >= INJURY_PRIOR_MIN_G:
                flags.append("POST_INJURY")
            if (cv1 is not None and g1 >= BOOMBUST_MIN_G and ppg1 >= BOOMBUST_MIN_PPG
                    and cv1 >= BOOMBUST_CV):
                flags.append("BOOM_BUST")
            if exp >= (AGING_EXP_RB if pos == "RB" else AGING_EXP):
                flags.append("AGING_VET")
            if (g1 >= STEADY_MIN_G and cv1 is not None and cv1 <= STEADY_MAX_CV
                    and ppg1 >= STEADY_MIN_PPG):
                flags.append("STEADY")
            e.update({
                "experience_at_pick": exp, "g_prev": g1, "ppg_prev": f"{ppg1:.1f}",
                "ppg_prev2": f"{ppg2:.1f}",
                "cv_prev": f"{cv1:.2f}" if cv1 is not None else "",
                "flags": "|".join(flags),
            })
        elif pos in SKILL and key not in weekly:
            # skill player with zero NFL stats ever before or during -- true rookie at pick
            e.update({"experience_at_pick": 0, "flags": "ROOKIE"})
        enriched.append(e)

    out = HISTORY / "draft_history_enriched.csv"
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(enriched[0].keys()))
        w.writeheader()
        w.writerows(enriched)
    print(f"Wrote {out} ({len(enriched)} picks)")

    # --- per-manager archetype profile, rounds 1-ANALYSIS_MAX_ROUND, skill picks only ---
    mgr_flags = defaultdict(lambda: defaultdict(int))
    mgr_n = defaultdict(int)
    for e in enriched:
        if int(e["round"]) > ANALYSIS_MAX_ROUND or e["position"] not in SKILL:
            continue
        m = e["manager"]
        mgr_n[m] += 1
        for fl in (e["flags"].split("|") if e["flags"] else []):
            mgr_flags[m][fl] += 1

    all_flags = ["ROOKIE", "SECOND_YEAR", "BREAKOUT_CHASE", "POST_INJURY", "BOOM_BUST",
                 "AGING_VET", "STEADY"]
    print(f"\nPer-manager archetype shares, rounds 1-{ANALYSIS_MAX_ROUND}, skill picks only")
    print("manager | n | " + " | ".join(all_flags))
    league_tot = defaultdict(int)
    league_n = 0
    for m in sorted(mgr_n):
        n = mgr_n[m]
        league_n += n
        cells = []
        for fl in all_flags:
            c = mgr_flags[m][fl]
            league_tot[fl] += c
            cells.append(f"{c} ({100*c/n:.0f}%)")
        print(f"{m:9}| {n:2} | " + " | ".join(cells))
    print(f"{'LEAGUE':9}| {league_n} | " + " | ".join(
        f"{league_tot[fl]} ({100*league_tot[fl]/league_n:.0f}%)" for fl in all_flags))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
