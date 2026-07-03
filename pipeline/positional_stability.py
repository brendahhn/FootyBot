#!/usr/bin/env python3
"""Positional stability / predictability analysis for FootyBot's league scoring.

Question: Is elite RB or elite WR (or TE) production more stable / predictive
year-over-year under THIS league's exact scoring? Tests Brendan's belief that
"you can always scrounge a receiver, but not a running back."

Method (stdlib only -- pandas/numpy not installed):
  1. Score every REG-season weekly offense row with league_scoring.offense_points.
  2. Aggregate to (player_id, position, season): total league points, games, PPG.
     Require >= 6 games to count as a qualifying season.
  3. Per season, rank qualifying players WITHIN RB / WR / TE by total points.
     Tiers: top-12, top-24, top-36.
  4. RETENTION: of players top-12 (and top-24) at a position in season N, what
     fraction are still top-12 (top-24) at that position in season N+1?
     Pooled across all consecutive pairs 2016->2025. Reported per position w/ N.
  5. Median year-over-year Pearson r of season-N PPG -> season-N+1 PPG, per
     position (players with >= 6 games in BOTH seasons).

Known caveat: league_scoring.offense_points omits the +2 per 40+yd run/reception
bonus and fumble-return TDs (not computable from weekly aggregates). This
slightly understates big-play boom weeks for all positions symmetrically.
Injuries also confound RB "volatility" (the >=6 game filter partly mitigates).
"""
import csv
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from league_scoring import offense_points  # noqa: E402

CSV_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "data", "raw", "player_stats_weekly.csv",
)
POSITIONS = ("RB", "WR", "TE")
MIN_GAMES = 6
TIERS = (12, 24, 36)


def load_season_totals():
    """Return {(player_id, position, season): {'pts': float, 'games': int}}."""
    agg = defaultdict(lambda: {"pts": 0.0, "games": 0})
    with open(CSV_PATH, newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            if row.get("season_type") != "REG":
                continue
            pos = row.get("position")
            if pos not in POSITIONS:
                continue
            try:
                season = int(row["season"])
            except (ValueError, TypeError):
                continue
            key = (row["player_id"], pos, season)
            agg[key]["pts"] += offense_points(row)
            agg[key]["games"] += 1
    return agg


def build_season_tables(agg):
    """Return:
      seasons: sorted list of seasons present
      ranked: {(pos, season): [(player_id, total_pts, ppg), ...]} ranked desc,
              qualifiers only (>= MIN_GAMES)
      ppg: {(pos, season): {player_id: ppg}} qualifiers only
    """
    by_pos_season = defaultdict(list)
    for (pid, pos, season), v in agg.items():
        if v["games"] < MIN_GAMES:
            continue
        ppg = v["pts"] / v["games"]
        by_pos_season[(pos, season)].append((pid, v["pts"], ppg))

    ranked = {}
    ppg = {}
    seasons = set()
    for (pos, season), lst in by_pos_season.items():
        lst.sort(key=lambda t: t[1], reverse=True)
        ranked[(pos, season)] = lst
        ppg[(pos, season)] = {pid: p for pid, _, p in lst}
        seasons.add(season)
    return sorted(seasons), ranked, ppg


def tier_ids(ranked, pos, season, n):
    lst = ranked.get((pos, season), [])
    return set(pid for pid, _, _ in lst[:n])


def retention(seasons, ranked):
    """{pos: {tier: (retained_fraction, n_players_evaluated)}}."""
    out = {}
    for pos in POSITIONS:
        out[pos] = {}
        for tier in (12, 24):
            retained = 0
            total = 0
            for i in range(len(seasons) - 1):
                s0, s1 = seasons[i], seasons[i + 1]
                if s1 != s0 + 1:
                    continue
                top0 = tier_ids(ranked, pos, s0, tier)
                top1 = tier_ids(ranked, pos, s1, tier)
                if not top0 or not top1:
                    continue
                for pid in top0:
                    total += 1
                    if pid in top1:
                        retained += 1
            frac = retained / total if total else float("nan")
            out[pos][tier] = (frac, total)
    return out


def pearson(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    if sxx == 0 or syy == 0:
        return None
    return sxy / (sxx * syy) ** 0.5


def median(vals):
    vals = sorted(vals)
    n = len(vals)
    if n == 0:
        return float("nan")
    if n % 2:
        return vals[n // 2]
    return (vals[n // 2 - 1] + vals[n // 2]) / 2


def yoy_correlation(seasons, ppg):
    """{pos: (median_r, n_pairs_of_seasons, sample_note_list)}.

    For each consecutive season pair, correlate season-N PPG vs season-N+1 PPG
    across players qualifying (>= MIN_GAMES) in BOTH seasons. Return median of
    the per-pair Pearson r's, plus list of (pair, r, n_players).
    """
    out = {}
    for pos in POSITIONS:
        rs = []
        detail = []
        for i in range(len(seasons) - 1):
            s0, s1 = seasons[i], seasons[i + 1]
            if s1 != s0 + 1:
                continue
            d0 = ppg.get((pos, s0), {})
            d1 = ppg.get((pos, s1), {})
            common = set(d0) & set(d1)
            if len(common) < 3:
                continue
            xs = [d0[p] for p in common]
            ys = [d1[p] for p in common]
            r = pearson(xs, ys)
            if r is None:
                continue
            rs.append(r)
            detail.append((f"{s0}->{s1}", r, len(common)))
        out[pos] = (median(rs), len(rs), detail)
    return out


def main():
    agg = load_season_totals()
    seasons, ranked, ppg = build_season_tables(agg)
    ret = retention(seasons, ranked)
    corr = yoy_correlation(seasons, ppg)

    print("=" * 70)
    print("FootyBot positional stability -- league-scored, REG only, >=6 games")
    print(f"Seasons: {seasons[0]}-{seasons[-1]}  |  min games/season: {MIN_GAMES}")
    print("=" * 70)

    # Qualifier counts per position-season (context)
    print("\nQualifying players per position per season (>=6 games):")
    print(f"{'season':>8}" + "".join(f"{p:>8}" for p in POSITIONS))
    for s in seasons:
        print(f"{s:>8}" + "".join(
            f"{len(ranked.get((p, s), [])):>8}" for p in POSITIONS))

    print("\n" + "-" * 70)
    print("TIER RETENTION (top-N in season N still top-N in season N+1)")
    print("pooled across all consecutive pairs; N = player-seasons evaluated")
    print("-" * 70)
    print(f"{'pos':>5}{'top-12 retain':>18}{'(N)':>7}"
          f"{'top-24 retain':>18}{'(N)':>7}")
    for pos in POSITIONS:
        f12, n12 = ret[pos][12]
        f24, n24 = ret[pos][24]
        print(f"{pos:>5}{f12*100:>16.1f}%{n12:>7}"
              f"{f24*100:>16.1f}%{n24:>7}")

    print("\n" + "-" * 70)
    print("YoY PPG PREDICTABILITY (median Pearson r, season-N -> season-N+1)")
    print("players qualifying (>=6 games) in BOTH seasons")
    print("-" * 70)
    print(f"{'pos':>5}{'median r':>12}{'season-pairs':>15}")
    for pos in POSITIONS:
        mr, npairs, _ = corr[pos]
        print(f"{pos:>5}{mr:>12.3f}{npairs:>15}")

    print("\nPer-pair detail (pair, r, n_players):")
    for pos in POSITIONS:
        _, _, detail = corr[pos]
        print(f"  {pos}:")
        for pair, r, n in detail:
            print(f"     {pair}  r={r:+.3f}  n={n}")

    print("\n" + "=" * 70)
    print("CAVEAT: scores omit +2 per 40+yd run/rec bonus & fumble-return TDs")
    print("(not computable from weekly aggregates). Applies to all positions.")
    print("Injuries confound RB volatility; >=6 game filter partly mitigates.")
    print("=" * 70)


if __name__ == "__main__":
    main()
