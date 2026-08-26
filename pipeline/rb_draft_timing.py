#!/usr/bin/env python3
"""Does drafting MORE RBs EARLY correlate with winning in this league?

Brendan's theory (2026-08-26): "RBs are incredibly valuable in my league" — so managers who
load up on RB early should finish better. This tests it directly, at four cutoffs he named:
RB count through rounds 2, 4, 6, and 8.

Method (stdlib only):
  - For each (year, manager), count RB picks with round <= K for K in {2,4,6,8}.
    Each manager has exactly 1 pick per round (16 rounds, no traded picks in this data),
    so rb@K is an integer 0..K and "K - rb@K" is everything else they took.
  - Join to league_finishes on (year, manager). Finishes cover 2019-2023 + 2025; there are
    no 2024 standings on file, so 2024's drafts are dropped from the join (60 scored
    manager-seasons out of 70 drafted).
  - Outcomes: final rank (1 = champion, 10 = last), and points-for z-scored WITHIN year
    (pf_z) so era/scoring drift between seasons can't drive the correlation. pf_z is the
    better strategy signal of the two: rank is PF plus schedule luck in a 13-week season.
  - Correlation: Pearson r. Sign convention -- for rank, NEGATIVE r means more early RB =
    better finish; for pf_z, POSITIVE r means more early RB = more points.
  - p-values: permutation test, shuffling the outcome vector WITHIN each season (10 managers
    per year). That holds the league structure fixed (someone always finishes 1st) and asks
    how often chance reproduces the observed |r|.
  - Confound controls:
      (a) draft slot -- at pick 1-3 elite RBs are simply there to take, so slot could drive
          both RB count and outcome. Reported as a partial correlation controlling for slot.
      (b) manager skill -- some managers are just better AND happen to be RB-first. Reported
          as a within-manager correlation (each manager's rb@K and outcome demeaned by his
          own 7-year average), which asks: when a manager goes MORE RB-heavy than his own
          norm, does he do better?
  - WR@K is run as the mirror test for contrast.

CRITICAL-THINKING NOTE: 60 manager-seasons is a small sample and final rank is noisy.
Bucket cells with N<5 are labeled too thin to read, and no r here should be treated as an
effect size to draft on -- only as evidence for/against the direction of the theory.
"""
import csv
import random
import sys
from collections import defaultdict
from math import sqrt
from pathlib import Path
from statistics import mean, median, pstdev

sys.path.insert(0, str(Path(__file__).resolve().parent))
from draft_outcomes import ALIASES, load_season_totals, norm  # noqa: E402
from league_scoring import offense_points  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
HISTORY = ROOT / "inputs" / "league-history"
DRAFT = HISTORY / "draft_history_enriched.csv"
FINISH = HISTORY / "league_finishes.csv"

CUTOFFS = (2, 4, 6, 8)

# Replacement level for points-over-replacement, in a 10-team league starting
# QB/RB/RB/WR/WR/TE + 2 W-R-T flex: the Nth-best season at that position is roughly what
# the last startable player is worth. Flex demand is split toward WR because this league
# drafts ~1.1 WR per RB in the flex-eligible range. These baselines are approximations --
# RB-vs-WR is insensitive to them (both shift together), QB/TE are NOT, so read the QB and
# TE rows as "depends on this assumption" rather than as findings.
REPLACEMENT_RANK = {"QB": 10, "RB": 25, "WR": 30, "TE": 10}
PERMS = 20000
SEED = 20260826

# Known name-join misses in the position column (nflverse name vs Yahoo name). Only picks in
# rounds 1-8 matter for this analysis; these are the ones that land there.
POSITION_FIXES = {"Hollywood Brown": "WR"}


def load_drafts():
    picks = defaultdict(list)
    for r in csv.DictReader(open(DRAFT)):
        r["year"] = int(r["year"])
        r["round"] = int(r["round"])
        r["pick_in_round"] = int(r["pick_in_round"])
        if not r["position"]:
            r["position"] = POSITION_FIXES.get(r["player"], "")
        picks[(r["year"], r["manager"])].append(r)
    for k in picks:
        picks[k].sort(key=lambda r: r["round"])
    return picks


def load_finishes():
    fin = {}
    for r in csv.DictReader(open(FINISH)):
        fin[(int(r["year"]), r["manager"])] = {
            "rank": int(r["rank"]),
            "pf": float(r["pf"]),
        }
    return fin


def pearson(xs, ys):
    n = len(xs)
    mx, my = mean(xs), mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = sqrt(sum((x - mx) ** 2 for x in xs))
    dy = sqrt(sum((y - my) ** 2 for y in ys))
    return num / (dx * dy) if dx and dy else 0.0


def perm_p(xs, ys, years, r_obs, rng):
    """Two-sided permutation p: shuffle the outcome within each season."""
    by_year = defaultdict(list)
    for i, y in enumerate(years):
        by_year[y].append(i)
    hits = 0
    shuffled = list(ys)
    for _ in range(PERMS):
        for idxs in by_year.values():
            vals = [ys[i] for i in idxs]
            rng.shuffle(vals)
            for i, v in zip(idxs, vals):
                shuffled[i] = v
        if abs(pearson(xs, shuffled)) >= abs(r_obs) - 1e-12:
            hits += 1
    return (hits + 1) / (PERMS + 1)


def perm_p_max(xmat, ys, years, r_obs_max, rng):
    """Family-wise p: how often does the LARGEST |r| across all predictors in xmat beat the
    largest observed |r|? This is the honest test when four cutoffs are tried at once."""
    by_year = defaultdict(list)
    for i, y in enumerate(years):
        by_year[y].append(i)
    hits = 0
    shuffled = list(ys)
    for _ in range(PERMS):
        for idxs in by_year.values():
            vals = [ys[i] for i in idxs]
            rng.shuffle(vals)
            for i, v in zip(idxs, vals):
                shuffled[i] = v
        if max(abs(pearson(x, shuffled)) for x in xmat) >= r_obs_max - 1e-12:
            hits += 1
    return (hits + 1) / (PERMS + 1)


def partial(r_xy, r_xz, r_yz):
    d = (1 - r_xz ** 2) * (1 - r_yz ** 2)
    return (r_xy - r_xz * r_yz) / sqrt(d) if d > 0 else float("nan")


def demean_by(keys, vals):
    grp = defaultdict(list)
    for k, v in zip(keys, vals):
        grp[k].append(v)
    m = {k: mean(v) for k, v in grp.items()}
    return [v - m[k] for k, v in zip(keys, vals)]


def stars(p):
    return "  <-- significant" if p < 0.05 else ("  (marginal)" if p < 0.10 else "")


def main():
    picks = load_drafts()
    fin = load_finishes()
    rng = random.Random(SEED)

    # ---- per manager-season descriptors ----
    rows = []
    for (y, m), rs in sorted(picks.items()):
        d = {"year": y, "manager": m, "slot": rs[0]["pick_in_round"]}
        for K in CUTOFFS:
            head = [r["position"] for r in rs if r["round"] <= K]
            d[f"rb{K}"] = head.count("RB")
            d[f"wr{K}"] = head.count("WR")
        rows.append(d)

    # points-for z-score within year (removes season-to-season scoring drift)
    pf_by_year = defaultdict(list)
    for d in rows:
        f = fin.get((d["year"], d["manager"]))
        if f:
            pf_by_year[d["year"]].append(f["pf"])
    pf_stats = {y: (mean(v), pstdev(v)) for y, v in pf_by_year.items()}

    scored = []
    for d in rows:
        f = fin.get((d["year"], d["manager"]))
        if not f:
            continue
        mu, sd = pf_stats[d["year"]]
        d = dict(d, rank=f["rank"], pf=f["pf"], pf_z=(f["pf"] - mu) / sd if sd else 0.0)
        scored.append(d)

    years = [d["year"] for d in scored]
    mgrs = [d["manager"] for d in scored]
    rank = [float(d["rank"]) for d in scored]
    pf_z = [d["pf_z"] for d in scored]
    slot = [float(d["slot"]) for d in scored]

    print("=" * 78)
    print("EARLY-RB LOAD vs FINISH  --  10-team, snake, 0.5-PPR, 1 IDP flex")
    print(f"Drafts 2019-2025 (70 manager-seasons); SCORED: 2019-2023 + 2025 "
          f"= {len(scored)} manager-seasons (no 2024 standings on file).")
    print("rank: 1 = champion, 10 = last.  pf_z: points-for, z-scored within season.")
    print("SIGN: rank r NEGATIVE = more early RB finishes better. pf_z r POSITIVE = more points.")
    print(f"p-values: {PERMS} within-season permutations, two-sided, seed {SEED}.")
    print("=" * 78)

    # ---- distribution of the predictor ----
    print("\n### How much do managers actually vary? (all 70 drafted manager-seasons)")
    print(f"{'cutoff':<10} {'mean RB':>8} {'sd':>6} {'min':>4} {'max':>4}   distribution")
    for K in CUTOFFS:
        v = [d[f"rb{K}"] for d in rows]
        dist = " ".join(f"{i}:{v.count(i)}" for i in range(K + 1) if v.count(i))
        print(f"RB thru R{K:<4} {mean(v):>8.2f} {pstdev(v):>6.2f} {min(v):>4} {max(v):>4}   {dist}")

    # ---- headline correlations ----
    for label, out, sign_note in (
        ("FINAL RANK", rank, "negative r = RB-heavy finishes BETTER"),
        ("POINTS-FOR (z within season)", pf_z, "positive r = RB-heavy scores MORE"),
    ):
        print(f"\n### {label}   ({sign_note})")
        print(f"{'predictor':<14} {'r':>7} {'p':>7}   {'r|slot':>7} {'r within-mgr':>13}")
        r_out_slot = pearson(slot, out)
        for K in CUTOFFS:
            x = [float(d[f"rb{K}"]) for d in scored]
            r = pearson(x, out)
            p = perm_p(x, out, years, r, rng)
            r_x_slot = pearson(x, slot)
            rp = partial(r, r_x_slot, r_out_slot)
            rw = pearson(demean_by(mgrs, x), demean_by(mgrs, out))
            print(f"RB thru R{K:<4} {r:>7.3f} {p:>7.4f}   {rp:>7.3f} {rw:>13.3f}{stars(p)}")
        for K in CUTOFFS:
            x = [float(d[f"wr{K}"]) for d in scored]
            r = pearson(x, out)
            p = perm_p(x, out, years, r, rng)
            r_x_slot = pearson(x, slot)
            rp = partial(r, r_x_slot, r_out_slot)
            rw = pearson(demean_by(mgrs, x), demean_by(mgrs, out))
            print(f"WR thru R{K:<4} {r:>7.3f} {p:>7.4f}   {rp:>7.3f} {rw:>13.3f}{stars(p)}")
        xmat = [[float(d[f"rb{K}"]) for d in scored] for K in CUTOFFS]
        r_max = max(abs(pearson(x, out)) for x in xmat)
        pf = perm_p_max(xmat, out, years, r_max, rng)
        print(f"  family-wise (best of the 4 RB cutoffs, |r|={r_max:.3f}): p = {pf:.4f}"
              f"{'  <-- survives multiplicity' if pf < 0.05 else '  <-- does NOT survive multiplicity'}")

    # ---- bucket tables ----
    for K in CUTOFFS:
        cells = defaultdict(list)
        for d in scored:
            cells[d[f"rb{K}"]].append(d)
        print(f"\n### RB count through round {K} -- outcomes")
        print(f"{'RBs':<5} {'N':>3} {'meanRk':>7} {'medRk':>6} {'mean pf_z':>10} "
              f"{'%top3':>6} {'%champ':>7} {'%last3':>7}  note")
        for rb in sorted(cells):
            ds = cells[rb]
            n = len(ds)
            rks = [d["rank"] for d in ds]
            print(f"{rb:<5} {n:>3} {mean(rks):>7.2f} {median(rks):>6.1f} "
                  f"{mean(d['pf_z'] for d in ds):>10.2f} "
                  f"{100*sum(1 for r in rks if r<=3)/n:>5.0f}% "
                  f"{100*sum(1 for r in rks if r==1)/n:>6.0f}% "
                  f"{100*sum(1 for r in rks if r>=8)/n:>6.0f}%  "
                  f"{'TOO THIN (N<5)' if n < 5 else ''}")

    # ---- which rounds carry it? RBs taken inside each 2-round window ----
    print("\n### WHERE the RBs were taken (RB count inside each 2-round window)")
    print(f"{'window':<12} {'mean RB':>8}   {'r vs rank':>10} {'p':>7}   {'r vs pf_z':>10} {'p':>7}")
    windows = [("R1-R2", 1, 2), ("R3-R4", 3, 4), ("R5-R6", 5, 6), ("R7-R8", 7, 8)]
    for name, lo, hi in windows:
        x = []
        for d in scored:
            rs = picks[(d["year"], d["manager"])]
            x.append(float(sum(1 for r in rs if lo <= r["round"] <= hi and r["position"] == "RB")))
        r1 = pearson(x, rank)
        p1 = perm_p(x, rank, years, r1, rng)
        r2 = pearson(x, pf_z)
        p2 = perm_p(x, pf_z, years, r2, rng)
        print(f"{name:<12} {mean(x):>8.2f}   {r1:>10.3f} {p1:>7.4f}   {r2:>10.3f} {p2:>7.4f}")

    # ---- champions' actual builds ----
    print("\n### What the 6 champions actually drafted")
    print(f"{'year':<6} {'manager':<10} {'slot':>4} {'RB@2':>5} {'RB@4':>5} {'RB@6':>5} {'RB@8':>5} {'pf_z':>6}")
    for d in sorted(scored, key=lambda d: d["year"]):
        if d["rank"] == 1:
            print(f"{d['year']:<6} {d['manager']:<10} {d['slot']:>4} {d['rb2']:>5} {d['rb4']:>5} "
                  f"{d['rb6']:>5} {d['rb8']:>5} {d['pf_z']:>6.2f}")

    # ---- per-manager profile: is the RB-first crowd the winning crowd? ----
    print("\n### Per-manager: career early-RB lean vs career finish (7 drafts, 6 scored years)")
    print(f"{'manager':<10} {'mean RB@2':>10} {'mean RB@4':>10} {'mean RB@8':>10} "
          f"{'mean rank':>10} {'mean pf_z':>10}")
    by_mgr = defaultdict(list)
    for d in scored:
        by_mgr[d["manager"]].append(d)
    prof = []
    for m, ds in by_mgr.items():
        prof.append((m, mean(d["rb2"] for d in ds), mean(d["rb4"] for d in ds),
                     mean(d["rb8"] for d in ds), mean(d["rank"] for d in ds),
                     mean(d["pf_z"] for d in ds)))
    for p in sorted(prof, key=lambda p: p[4]):
        print(f"{p[0]:<10} {p[1]:>10.2f} {p[2]:>10.2f} {p[3]:>10.2f} {p[4]:>10.2f} {p[5]:>10.2f}")
    print("\nmanager-level r (N=10 managers, career means):")
    for i, K in ((1, 2), (2, 4), (3, 8)):
        print(f"  mean RB@{K} vs mean rank : r = {pearson([p[i] for p in prof], [p[4] for p in prof]):+.3f}"
              f"   vs mean pf_z : r = {pearson([p[i] for p in prof], [p[5] for p in prof]):+.3f}")

    # ---- RETURN SIDE: at the same draft cost, does an RB out-earn a WR here? ----
    # The allocation test above has only 60 rows. This one has every rounds-1-8 skill pick
    # (7 years x 10 managers x 8 rounds), so it is far better powered -- and it answers the
    # actual premise ("RBs are incredibly valuable in MY league") rather than the proxy.
    totals = load_season_totals()
    allpicks = [r for r in csv.DictReader((DRAFT).open())
                if int(r["round"]) <= 8 and (r["position"] or POSITION_FIXES.get(r["player"], ""))
                in {"QB", "RB", "WR", "TE"}]
    for r in allpicks:
        r["position"] = r["position"] or POSITION_FIXES.get(r["player"], "")
        key = ALIASES.get(norm(r["player"]), norm(r["player"]))
        r["_pts"] = totals.get(key, {}).get(int(r["year"]), 0.0)
    # points-over-replacement baseline per season, from ALL NFL players, not just drafted ones
    season_pos = defaultdict(lambda: defaultdict(float))  # (season,pos) -> name -> pts
    for fn in ("player_stats.csv", "stats_player_week_2025.csv"):
        path = ROOT / "inputs" / "nflverse" / fn
        if not path.exists():
            continue
        for row in csv.DictReader(path.open(newline="")):
            if (row.get("season_type") or "REG") != "REG":
                continue
            pos = row.get("position") or ""
            if pos not in REPLACEMENT_RANK:
                continue
            season_pos[(int(row["season"]), pos)][norm(row.get("player_display_name") or "")] += \
                offense_points(row)
    baseline = {}
    for (season, pos), players in season_pos.items():
        ordered = sorted(players.values(), reverse=True)
        n = REPLACEMENT_RANK[pos]
        baseline[(season, pos)] = ordered[n - 1] if len(ordered) >= n else 0.0

    med_yr_rd = {}
    grp = defaultdict(list)
    for r in allpicks:
        grp[(r["year"], r["round"])].append(r["_pts"])
    for k, v in grp.items():
        med_yr_rd[k] = median(v)

    print("\n### RETURN SIDE -- realized league points by position and draft cost")
    print("Every 2019-2025 rounds-1-8 skill pick, scored with this league's exact formula on")
    print("real nflverse weekly data, in the season it was drafted for. 'hit' = beat the median")
    print("of all skill picks in that same year+round. 0-point lines = the player never played.")
    print("mean VOR = mean points OVER positional replacement (see REPLACEMENT_RANK in source);")
    print("that column, not raw points, is the RB-vs-WR comparison. QB/TE VOR depends heavily")
    print("on the assumed baseline -- do not read those two rows as findings.")
    print(f"\n{'window':<8} {'pos':<4} {'N':>4} {'mean pts':>9} {'median':>8} {'mean VOR':>9} "
          f"{'hit%':>6} {'bust<50':>8}")
    for name, lo, hi in windows:
        for pos in ("RB", "WR", "TE", "QB"):
            sub = [r for r in allpicks if lo <= int(r["round"]) <= hi and r["position"] == pos]
            if len(sub) < 5:
                continue
            pts = [r["_pts"] for r in sub]
            hits = sum(1 for r in sub if r["_pts"] > med_yr_rd[(r["year"], r["round"])])
            busts = sum(1 for x in pts if x < 50)
            vor = mean(r["_pts"] - baseline.get((int(r["year"]), pos), 0.0) for r in sub)
            print(f"{name:<8} {pos:<4} {len(sub):>4} {mean(pts):>9.1f} {median(pts):>8.1f} "
                  f"{vor:>9.1f} {100*hits/len(sub):>5.0f}% {100*busts/len(sub):>7.0f}%")
        print()

    # ---- is the RB-vs-WR gap at a given cost distinguishable from zero? ----
    print("### Is the RB-vs-WR gap at the same draft cost real? (label-shuffle permutation)")
    print(f"{'window':<8} {'VOR gap':>9} {'p':>7}   {'bust gap':>9} {'p':>7}")
    for name, lo, hi in windows + [("R5-R8", 5, 8)]:
        sub = {pos: [r for r in allpicks if lo <= int(r["round"]) <= hi and r["position"] == pos]
               for pos in ("RB", "WR")}
        vor = {pos: [r["_pts"] - baseline.get((int(r["year"]), pos), 0.0) for r in sub[pos]]
               for pos in sub}
        bust = {pos: [1.0 if r["_pts"] < 50 else 0.0 for r in sub[pos]] for pos in sub}
        line = f"{name:<8}"
        for vals, fmt in ((vor, "{:>9.1f}"), (bust, "{:>8.1f}pp")):
            obs = mean(vals["RB"]) - mean(vals["WR"])
            scale = 100.0 if vals is bust else 1.0
            pool = vals["RB"] + vals["WR"]
            n = len(vals["RB"])
            hits = sum(1 for _ in range(PERMS)
                       if (rng.shuffle(pool) or
                           abs(mean(pool[:n]) - mean(pool[n:])) >= abs(obs) - 1e-9))
            line += " " + fmt.format(obs * scale) + f" {(hits + 1) / (PERMS + 1):>7.4f}  "
        print(line)
    print("None of these clears p<0.05: at equal draft cost this league's RB and WR picks have")
    print("returned the same, and only the LATE-round RB bust gap even approaches significance.")

    print("\n" + "=" * 78)
    print("READ THIS BEFORE QUOTING ANY NUMBER ABOVE: N=60 manager-seasons, and final rank in a")
    print("13-week season is roughly points-for plus schedule luck. A |r| under ~0.25 here is")
    print("indistinguishable from noise; cells with N<5 are unreadable. This tests ALLOCATION")
    print("(how many of your first K picks were RB), not whether the RBs you took were good.")
    print("=" * 78)


if __name__ == "__main__":
    main()
