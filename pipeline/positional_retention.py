"""Year-over-year positional RETENTION under this league's exact scoring.

Decision question (Brendan's identity bet): "you can always scrounge a WR but
not a RB." If elite RB production is LESS stable year over year (more attrition /
injury / bust) than elite WR, RB scarcity is real and you draft RB early. If
elite WRs are just as replaceable, the scarcity argument weakens.

Method (all stdlib, csv.DictReader only -- pandas may be blocked):
  * REG season only. Aggregate each player-season: total league points and
    games played (one weekly row = one game). PPG = points / games.
  * Require >= 6 games in BOTH seasons of a pair to enter a ranking (matches
    predictive_stats.py convention).
  * For each consecutive season pair (N, N+1) and each position, rank players
    with >=6 games in season N by PPG. Take the top TIER. Then measure:
      - retention: fraction of top-tier(N) that are ALSO top-tier(N+1)
      - survival:  fraction of top-tier(N) that even played >=6 games in N+1
      - ppg dropoff: tier mean PPG in N  minus  mean PPG in N+1 among survivors
  * Pool across all pairs (2016-17 ... 2024-25).

Scoring comes from pipeline/league_scoring.py (same known 40+ bonus gap).

IDP bonus: same retention for top-12 IDP (this scoring), plus whether prior-year
solo-tackle rate ranks predict next-year top-12 IDP membership.
"""

import csv
import os
from collections import defaultdict

from league_scoring import offense_points, idp_points

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OFF_CSV = os.path.join(ROOT, "data", "raw", "player_stats_weekly.csv")
DEF_CSV = os.path.join(ROOT, "data", "raw", "player_stats_def_weekly.csv")

MIN_GAMES = 6
OFF_POS = ("QB", "RB", "WR", "TE")


def fnum(x):
    try:
        return float(x or 0)
    except (ValueError, TypeError):
        return 0.0


def load_offense():
    """Return agg[(pos, season, pid)] = {name, pts, games}."""
    agg = defaultdict(lambda: {"name": "", "pts": 0.0, "games": 0})
    with open(OFF_CSV, newline="") as f:
        for r in csv.DictReader(f):
            if r.get("season_type") != "REG":
                continue
            pos = r.get("position_group")
            if pos not in OFF_POS:
                continue
            key = (pos, r["season"], r["player_id"])
            a = agg[key]
            a["name"] = r.get("player_display_name") or r.get("player_name") or ""
            a["pts"] += offense_points(r)
            a["games"] += 1
    return agg


def load_defense():
    """Return agg[(season, pid)] = {name, pos, pts, solo, games}."""
    agg = defaultdict(lambda: {"name": "", "pos": "", "pts": 0.0, "solo": 0.0, "games": 0})
    with open(DEF_CSV, newline="") as f:
        for r in csv.DictReader(f):
            if r.get("season_type") != "REG":
                continue
            key = (r["season"], r["player_id"])
            a = agg[key]
            a["name"] = r.get("player_display_name") or r.get("player_name") or ""
            a["pos"] = r.get("position") or ""
            a["pts"] += idp_points(r)
            a["solo"] += fnum(r.get("def_tackles_solo"))
            a["games"] += 1
    return agg


def season_ppg_table(agg_pos):
    """agg for one position -> {season: {pid: (ppg, name)}} for >=MIN_GAMES."""
    out = defaultdict(dict)
    for (season, pid), a in agg_pos.items():
        if a["games"] >= MIN_GAMES:
            out[season][pid] = (a["pts"] / a["games"], a["name"])
    return out


def retention_for_position(agg, pos, tier):
    """Pool retention/survival/dropoff across all consecutive season pairs."""
    # collapse to this position: {(season,pid): a}
    sub = {(s, pid): a for (p, s, pid), a in agg.items() if p == pos}
    table = season_ppg_table(sub)  # {season:{pid:(ppg,name)}}
    seasons = sorted(table.keys(), key=int)

    n_tier = 0
    retained = 0
    survived = 0
    tier_ppg_sum = 0.0
    surv_next_ppg_sum = 0.0
    for i in range(len(seasons) - 1):
        s0, s1 = seasons[i], seasons[i + 1]
        rank0 = sorted(table[s0].items(), key=lambda kv: kv[1][0], reverse=True)
        top0 = rank0[:tier]
        rank1 = sorted(table[s1].items(), key=lambda kv: kv[1][0], reverse=True)
        top1_ids = set(pid for pid, _ in rank1[:tier])
        for pid, (ppg0, _name) in top0:
            n_tier += 1
            tier_ppg_sum += ppg0
            if pid in top1_ids:
                retained += 1
            if pid in table[s1]:  # played >=6 games next year
                survived += 1
                surv_next_ppg_sum += table[s1][pid][0]
    ret = retained / n_tier if n_tier else 0.0
    surv = survived / n_tier if n_tier else 0.0
    tier_ppg = tier_ppg_sum / n_tier if n_tier else 0.0
    surv_next = surv_next_ppg_sum / survived if survived else 0.0
    return {
        "pos": pos, "tier": tier, "n": n_tier,
        "retention": ret, "survival": surv,
        "tier_ppg": tier_ppg, "surv_next_ppg": surv_next,
        "dropoff": tier_ppg - surv_next,
    }


def idp_retention(agg, tier=12):
    """{(season,pid): a} already position-agnostic. Rank by IDP PPG."""
    table = defaultdict(dict)   # season -> pid -> ppg
    solo_rate = defaultdict(dict)  # season -> pid -> solo/game
    meta = {}
    for (season, pid), a in agg.items():
        if a["games"] >= MIN_GAMES:
            table[season][pid] = a["pts"] / a["games"]
            solo_rate[season][pid] = a["solo"] / a["games"]
            meta[(season, pid)] = (a["name"], a["pos"])
    seasons = sorted(table.keys(), key=int)

    n_tier = retained = survived = 0
    tier_ppg_sum = surv_next_ppg_sum = 0.0
    # Floor question: of the prior-year top-24 by SOLO RATE (high-volume,
    # every-down tacklers), what fraction land in next-year top-K IDP? Compare
    # to selecting by prior-year IDP PPG. K in {12,24,36}. Also a random
    # baseline = K / (pool size that year).
    floor_thresh = (12, 24, 36)
    solo_hit = {k: 0 for k in floor_thresh}
    ppg_hit = {k: 0 for k in floor_thresh}
    sel_n = 0
    base_hit = {k: 0.0 for k in floor_thresh}  # expected under random pick
    for i in range(len(seasons) - 1):
        s0, s1 = seasons[i], seasons[i + 1]
        rank_ppg = sorted(table[s0].items(), key=lambda kv: kv[1], reverse=True)
        top0 = rank_ppg[:tier]
        top1_ids = set(pid for pid, _ in sorted(table[s1].items(), key=lambda kv: kv[1], reverse=True)[:tier])
        for pid, ppg0 in top0:
            n_tier += 1
            tier_ppg_sum += ppg0
            if pid in top1_ids:
                retained += 1
            if pid in table[s1]:
                survived += 1
                surv_next_ppg_sum += table[s1][pid]
        # floor: select 24 by prior-yr solo rate vs by prior-yr IDP PPG
        rank_s1 = sorted(table[s1].items(), key=lambda kv: kv[1], reverse=True)
        pool1 = len(rank_s1)
        topK = {k: set(pid for pid, _ in rank_s1[:k]) for k in floor_thresh}
        SEL = 24
        solo_sel = [pid for pid, _ in sorted(solo_rate[s0].items(), key=lambda kv: kv[1], reverse=True)[:SEL]]
        ppg_sel = [pid for pid, _ in rank_ppg[:SEL]]
        sel_n += SEL
        for k in floor_thresh:
            base_hit[k] += SEL * (min(k, pool1) / pool1) if pool1 else 0
            for pid in solo_sel:
                if pid in topK[k]:
                    solo_hit[k] += 1
            for pid in ppg_sel:
                if pid in topK[k]:
                    ppg_hit[k] += 1
    return {
        "n": n_tier,
        "retention": retained / n_tier if n_tier else 0.0,
        "survival": survived / n_tier if n_tier else 0.0,
        "tier_ppg": tier_ppg_sum / n_tier if n_tier else 0.0,
        "surv_next_ppg": surv_next_ppg_sum / survived if survived else 0.0,
        "sel_n": sel_n,
        "solo_floor": {k: solo_hit[k] / sel_n for k in floor_thresh} if sel_n else {},
        "ppg_floor": {k: ppg_hit[k] / sel_n for k in floor_thresh} if sel_n else {},
        "base_floor": {k: base_hit[k] / sel_n for k in floor_thresh} if sel_n else {},
    }


def main():
    off = load_offense()
    print("=== OFFENSE year-over-year retention (this league's scoring, REG, >=6 gms both yrs) ===")
    print(f"{'pos':>4} {'tier':>4} {'N':>4} {'retain%':>8} {'surv%':>7} {'tierPPG':>8} {'nextPPG':>8} {'drop':>6}")
    # standard tiers
    standard = [("RB", 12), ("WR", 24), ("QB", 12), ("TE", 12)]
    for pos, tier in standard:
        r = retention_for_position(off, pos, tier)
        print(f"{r['pos']:>4} {r['tier']:>4} {r['n']:>4} {r['retention']*100:>7.1f}% {r['survival']*100:>6.1f}% {r['tier_ppg']:>8.2f} {r['surv_next_ppg']:>8.2f} {r['dropoff']:>6.2f}")
    print("--- matched-depth comparison (RB vs WR at same tier size) ---")
    for pos, tier in [("RB", 12), ("WR", 12), ("RB", 24), ("WR", 24)]:
        r = retention_for_position(off, pos, tier)
        print(f"{r['pos']:>4} {r['tier']:>4} {r['n']:>4} {r['retention']*100:>7.1f}% {r['survival']*100:>6.1f}% {r['tier_ppg']:>8.2f} {r['surv_next_ppg']:>8.2f} {r['dropoff']:>6.2f}")

    print()
    print("=== IDP retention (top-12 by this scoring) ===")
    d = load_defense()
    ir = idp_retention(d, 12)
    print(f"top12  N={ir['n']}  retain={ir['retention']*100:.1f}%  surv={ir['survival']*100:.1f}%  tierPPG={ir['tier_ppg']:.2f}  nextPPG={ir['surv_next_ppg']:.2f}  drop={ir['tier_ppg']-ir['surv_next_ppg']:.2f}")
    print(f"FLOOR: pick 24 in yr N, hit-rate into next-yr top-K IDP (N_selections={ir['sel_n']})")
    print(f"{'K':>4} {'by SOLO-rate':>13} {'by IDP-PPG':>11} {'random base':>12}")
    for k in (12, 24, 36):
        print(f"{k:>4} {ir['solo_floor'][k]*100:>12.1f}% {ir['ppg_floor'][k]*100:>10.1f}% {ir['base_floor'][k]*100:>11.1f}%")


if __name__ == "__main__":
    main()
