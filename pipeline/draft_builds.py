#!/usr/bin/env python3
"""Which opening-draft BUILD correlates with winning in this league?

Brendan's premise: "RBs get overvalued here; you can scrounge a WR not an RB." This tests
whether the SHAPE of a manager's opening draft (their first few picks by overall_pick order)
actually correlates with final standings.

Method (stdlib only):
  - For each (year, manager) read the position of their first N picks in DRAFT ORDER
    (overall_pick ascending). Classify the OPENING BUILD from the first 3 picks primarily,
    with first-2 and first-4 variants for robustness. Also compute boolean flags:
      ZERO_RB  = no RB in first 3 picks
      HERO_RB  = exactly 1 RB in first 3 picks
      RB_HEAVY = 2+ RB in first 3 picks
      TE_EARLY = a TE in first 3 picks
      QB_EARLY = a QB in first 3 picks
  - Join to league_finishes on (year, manager). NOTE: finishes cover 2019-2023 + 2025
    (no 2024 standings), so 2024 drafts have no outcome and are dropped from the join.
  - Report per archetype: N, mean rank, median rank, mean points-for, %top-3, %champ.

CRITICAL-THINKING NOTE (printed at end too): outcome != strategy quality. The sample is tiny
(6 scored seasons x 10 managers = up to 60 manager-seasons; each archetype cell is far
smaller). Single-digit rank gaps between cells are noise. Confounds we cannot remove:
draft-value-at-pick, in-season management, and schedule luck all move final rank independently
of build shape. A prior finding measured draft value -> PF r~+0.50 but draft value -> final
rank only r~+0.31, and in-season move count -> rank ~0.00. So do NOT read a build as "winning"
off a thin cell. Cells with N<5 are labeled too thin to read.
"""
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parent.parent
HISTORY = ROOT / "inputs" / "league-history"
DRAFT = HISTORY / "draft_history_enriched.csv"
FINISH = HISTORY / "league_finishes.csv"

# Positions that count as a "real" opening pick for build shape. K/DST/IDP in the first
# few rounds are exotic but we still record the raw position; only RB/WR/QB/TE drive the
# archetype label.
CORE = {"RB", "WR", "QB", "TE"}


def load_drafts():
    rows = list(csv.DictReader(open(DRAFT)))
    for r in rows:
        r["overall_pick"] = int(r["overall_pick"])
        r["year"] = int(r["year"])
    picks = defaultdict(list)  # (year, manager) -> [rows]
    for r in rows:
        picks[(r["year"], r["manager"])].append(r)
    for k in picks:
        picks[k].sort(key=lambda r: r["overall_pick"])
    return picks


def load_finishes():
    fin = {}
    for r in csv.DictReader(open(FINISH)):
        fin[(int(r["year"]), r["manager"])] = {
            "rank": int(r["rank"]),
            "pf": float(r["pf"]),
            "moves": int(r["moves"]),
        }
    return fin


def pos_seq(rows, n):
    """First n pick positions in draft order (raw position strings)."""
    return [r["position"] for r in rows[:n]]


def label3(seq3):
    """Coarse archetype from the first-3 position sequence. Order-sensitive first two,
    then collapses the rest. Non-core (K/DST/IDP) shown as their raw code."""
    a, b = seq3[0], seq3[1]
    return f"{a}-{b}-x"


def flags(seq3):
    rb = seq3.count("RB")
    f = {
        "ZERO_RB": rb == 0,
        "HERO_RB": rb == 1,
        "RB_HEAVY": rb >= 2,
        "TE_EARLY": "TE" in seq3,
        "QB_EARLY": "QB" in seq3,
    }
    return f


def summarize(cells, fin, key_of):
    """cells: dict archetype -> list of (year, manager). Returns list of stat dicts."""
    out = []
    for arch, ms in cells.items():
        scored = [fin[(y, m)] for (y, m) in ms if (y, m) in fin]
        if not scored:
            continue
        ranks = [s["rank"] for s in scored]
        pfs = [s["pf"] for s in scored]
        n = len(scored)
        out.append({
            "arch": arch,
            "n": n,
            "mean_rank": mean(ranks),
            "med_rank": median(ranks),
            "mean_pf": mean(pfs),
            "pct_top3": 100.0 * sum(1 for r in ranks if r <= 3) / n,
            "pct_champ": 100.0 * sum(1 for r in ranks if r == 1) / n,
            "thin": n < 5,
        })
    return out


def ptable(title, stats, sort_key="mean_rank"):
    print(f"\n### {title}")
    print(f"{'archetype':<16} {'N':>3} {'meanRk':>7} {'medRk':>6} {'meanPF':>8} "
          f"{'%top3':>6} {'%champ':>7}  note")
    for s in sorted(stats, key=lambda s: s[sort_key]):
        note = "TOO THIN (N<5)" if s["thin"] else ""
        print(f"{s['arch']:<16} {s['n']:>3} {s['mean_rank']:>7.2f} {s['med_rank']:>6.1f} "
              f"{s['mean_pf']:>8.1f} {s['pct_top3']:>5.0f}% {s['pct_champ']:>6.0f}%  {note}")


def main():
    picks = load_drafts()
    fin = load_finishes()

    # Build per (year, manager) descriptors
    desc = {}
    for (y, m), rows in picks.items():
        seq4 = pos_seq(rows, 4)
        seq3 = seq4[:3]
        seq2 = seq4[:2]
        desc[(y, m)] = {
            "seq2": seq2, "seq3": seq3, "seq4": seq4,
            "flags": flags(seq3),
        }

    # ---- League-wide raw first-3 sequence frequency (context) ----
    print("=" * 74)
    print("OPENING BUILD vs FINISH  --  10-team league, snake, 0.5-PPR")
    print("Draft years 2019-2025; SCORED years (joined to standings): "
          "2019-2023 + 2025 (no 2024 standings on file).")
    print("rank: 1 = league champion, 10 = last.  meanPF = mean regular-season points-for.")
    print("=" * 74)

    seq3_freq = defaultdict(int)
    for d in desc.values():
        seq3_freq[tuple(d["seq3"])] += 1

    # ---- First-2 archetype (order-sensitive) ----
    cells2 = defaultdict(list)
    for k, d in desc.items():
        cells2["-".join(d["seq2"])].append(k)
    ptable("FIRST-2 PICKS build (order-sensitive)", summarize(cells2, fin, None))

    # ---- First-3 collapsed: RB count buckets (the cleanest, biggest cells) ----
    cells_rb = defaultdict(list)
    for k, d in desc.items():
        rb = d["seq3"].count("RB")
        wr = d["seq3"].count("WR")
        bucket = {0: "ZeroRB (0 RB/3)", 1: "HeroRB (1 RB/3)"}.get(rb, "RBheavy (2+ RB/3)")
        cells_rb[bucket].append(k)
    ptable("FIRST-3 PICKS by RB count (primary lens)", summarize(cells_rb, fin, None))

    # Also WR-count buckets to test Brendan's "scrounge a WR" directly
    cells_wr = defaultdict(list)
    for k, d in desc.items():
        wr = d["seq3"].count("WR")
        bucket = {0: "0 WR/3", 1: "1 WR/3", 2: "2 WR/3"}.get(wr, "3 WR/3")
        cells_wr[bucket].append(k)
    ptable("FIRST-3 PICKS by WR count", summarize(cells_wr, fin, None))

    # ---- First-3 order-sensitive top archetypes (first two + x) ----
    cells3 = defaultdict(list)
    for k, d in desc.items():
        cells3[label3(d["seq3"])].append(k)
    # only show archetypes with any scored season
    ptable("FIRST-3 PICKS build (first two positions, order-sensitive)",
           summarize(cells3, fin, None))

    # ---- Boolean flags ----
    flag_cells = defaultdict(list)
    for k, d in desc.items():
        for fname, val in d["flags"].items():
            if val:
                flag_cells[fname + " = TRUE"].append(k)
            else:
                flag_cells[fname + " = FALSE"].append(k)
    ptable("OPENING FLAGS (first 3 picks)", summarize(flag_cells, fin, None))

    # ---- League baseline for reference ----
    all_scored = [fin[k] for k in desc if k in fin]
    br = [s["rank"] for s in all_scored]
    bpf = [s["pf"] for s in all_scored]
    print(f"\n### League baseline (all scored manager-seasons)")
    print(f"N={len(all_scored)}  mean rank={mean(br):.2f}  median rank={median(br):.1f}  "
          f"mean PF={mean(bpf):.1f}  (%top3 fixed at 30% by construction, %champ 10%)")

    # ---- Brendan's own build history ----
    print("\n" + "=" * 74)
    print("BRENDAN'S OPENING BUILDS BY YEAR")
    print("=" * 74)
    print(f"{'year':>4} {'first-3 positions':<22} {'first-4':<28} {'rank':>4} {'pf':>8}  flags")
    for y in sorted(set(k[0] for k in desc)):
        k = (y, "Brendan")
        if k not in desc:
            continue
        d = desc[k]
        s3 = "-".join(d["seq3"])
        s4 = "-".join(d["seq4"])
        f = fin.get(k)
        rank = f"{f['rank']}" if f else "n/a"
        pf = f"{f['pf']:.1f}" if f else "n/a"
        on = [name for name, v in d["flags"].items() if v]
        print(f"{y:>4} {s3:<22} {s4:<28} {rank:>4} {pf:>8}  {','.join(on)}")

    # Brendan aggregate
    bk = [(y, "Brendan") for y in sorted(set(k[0] for k in desc)) if (y, "Brendan") in fin]
    if bk:
        bruk = [fin[k]["rank"] for k in bk]
        print(f"\nBrendan scored seasons N={len(bruk)}  mean rank={mean(bruk):.2f}  "
              f"median={median(bruk):.1f}  best={min(bruk)}  worst={max(bruk)}")

    print("\n" + "=" * 74)
    print("READ HONESTLY: cells marked TOO THIN (N<5) cannot be read. Compare each cell's")
    print("mean rank to the league baseline mean rank (~5.5); gaps under ~1.0 rank are noise")
    print("given confounds (draft value, in-season play, schedule luck).")
    print("=" * 74)


if __name__ == "__main__":
    main()
