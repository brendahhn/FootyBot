# 2025 scoring leaders under THIS league's exact rules

Status: created 2026-07-08 (newsletter Lane A). **Tier S — pipeline-computed** from
`data/raw/player_stats_weekly.csv` (nflverse weekly, 2025 `season_type=REG` only), scored with
`pipeline/league_scoring.py` (half-PPR, 6pt passing/rushing/receiving TD, -2 INT/fumble,
10 yd/pt rush+rec, 25 yd/pt pass). PPG = total points ÷ games played.

**Known undercount (same caveat as `predictive-stats.md`):** the +2 bonuses for 40+ yard
runs/receptions and offensive fumble-return TDs are NOT in these weekly aggregates (need
play-level data), so every figure below slightly under-credits big-play players (Achane, Chase,
JSN). Directional, not exact, at the margin.

**Housekeeping:** this table is currently hand-placed from a one-off Lane A query script. It should
be folded into `pipeline/predictive_stats.py` (or a small `pipeline/scoring_leaders.py`) so it
regenerates every run instead of going stale — logged in the notebook AUDIT_QUEUE.

## Overall top 6 (2025) — all quarterbacks

The 6-pt passing-TD rule sweeps QBs to the top of the overall board:
Stafford 26.0 · Allen 25.9 · Maye 24.3 · Lawrence 23.3 · Prescott 22.0 · C. Williams 21.8 (PPG).
This is why waiting on QB is genuinely costlier here than in a standard 4-pt-pass league — but
replacement level still governs *when* to draft one (see `draft-tendencies.md` Finding 1/5).

### Full 2025 QB spread [S] — the "cost of waiting," quantified (added 2026-07-15, Lane A)
Same scoring, reg season, games ≥ 8 (per-game; low-games QBs noisy):
QB1 Stafford 26.0 · QB2 Allen 25.9 · QB3 Maye 24.3 · QB4 Purdy 24.2 (9g) · QB5 Mahomes 23.5 (14g) ·
QB6 Lawrence 23.3 · QB7 Prescott 22.0 · QB8 Hurts 21.9 · QB9 Caleb Williams 21.8 · QB10 Goff 21.5 ·
QB11 Herbert 21.2 · QB12 Burrow 21.1 (8g) · QB13 Bo Nix 20.9 · QB14 D.Jones 20.3 · QB15 Lamar 19.8 (13g) ·
QB16 Brissett 19.5 · QB17 Dart 19.4 · QB18 Mayfield 19.1.
**Nuance that refines the "waiting is costlier" line above:** the edge is concentrated in the **top ~3**
(Stafford/Allen/Maye ~24-26; Allen *undercounted* — the +2/40-yd bonus we can't compute helps rushing QBs most).
The gap from **QB6 (23.3) to QB18 (19.1) is only ~4.2 ppg across twelve QBs** — a shallow, streamable band.
So: waiting IS costlier than a 4-pt league *only if you skip the elite tier*; the QB7-18 pack is tight enough that
the ~pick-95-110 streamer names (Caleb Williams QB9, Bo Nix QB13) capture most of the value. Take a top-3 QB only if
one falls to a slot you'd actually spend; otherwise wait and stream. Don't spend picks 17/24 on a passer.

## Top 15 RBs — 2025 PPG (our scoring)

| Rk | RB | PPG | Total | G |
|---|---|---|---|---|
| 1 | Christian McCaffrey | 21.51 | 365.6 | 17 |
| 2 | Jonathan Taylor | 19.96 | 339.3 | 17 |
| 3 | Bijan Robinson | 19.49 | 331.3 | 17 |
| 4 | Jahmyr Gibbs | 19.32 | 328.4 | 17 |
| 5 | De'Von Achane | 18.08 | 289.3 | 16 |
| 6 | James Cook | 16.81 | 285.7 | 17 |
| 7 | Derrick Henry | 16.00 | 272.0 | 17 |
| 8 | Josh Jacobs | 14.61 | 219.1 | 15 |
| 9 | Chase Brown | 14.59 | 248.1 | 17 |
| 10 | Cam Skattebo | 14.46 | 115.7 | 8 |
| 11 | Kyren Williams | 14.43 | 245.3 | 17 |
| 12 | Javonte Williams | 14.08 | 225.3 | 16 |
| 13 | Travis Etienne | 13.88 | 235.9 | 17 |
| 14 | Saquon Barkley | 13.36 | 213.8 | 16 |
| 15 | Omarion Hampton | 13.30 | 119.7 | 9 |

Note: **CMC was RB1 on a full 17 games** (102 rec / 924 rec yd / 7 rec TD + 1202 rush / 10 rush
TD = 17 total TDs) — he did NOT miss time in 2025. **Saquon regressed to RB14** (1140 rush yd,
9 TD, 37 catches) — not the 2024 all-timer.

## Top 15 WRs — 2025 PPG (our scoring)

| Rk | WR | PPG | Total | G |
|---|---|---|---|---|
| 1 | Puka Nacua | 19.41 | 310.5 | 16 |
| 2 | Jaxon Smith-Njigba | 17.67 | 300.4 | 17 |
| 3 | Ja'Marr Chase | 15.69 | 251.1 | 16 |
| 4 | Amon-Ra St. Brown | 15.62 | 265.5 | 17 |
| 5 | Rashee Rice | 15.45 | 123.6 | 8 |
| 6 | George Pickens | 14.44 | 245.4 | 17 |
| 7 | Drake London | 13.99 | 167.9 | 12 |
| 8 | Davante Adams | 13.78 | 192.9 | 14 |
| 9 | Chris Olave | 13.62 | 218.0 | 16 |
| 10 | Nico Collins | 12.71 | 190.7 | 15 |
| 11 | CeeDee Lamb | 12.57 | 163.4 | 13 |
| 12 | Tee Higgins | 12.14 | 182.1 | 15 |
| 13 | A.J. Brown | 12.09 | 181.3 | 15 |
| 14 | Malik Nabers | 12.03 | 48.1 | 4 |
| 15 | Zay Flowers | 11.78 | 200.3 | 17 |

## Pick-4 WR candidates — with predictive usage stats

Target share = player targets ÷ team targets (over played weeks); WOPR = 1.5·(target share) +
0.7·(air-yards share). Both computed from the weekly columns. Per `predictive-stats.md`, target
share (r=0.350) and WOPR (r=0.280) are the year-over-year sticky signals; TD rate is noise
(r=0.008).

| WR | PPG | Total | G | Tgt share | WOPR |
|---|---|---|---|---|---|
| Puka Nacua | 19.41 | 310.5 | 16 | 30.3% | 0.677 |
| Jaxon Smith-Njigba | 17.67 | 300.4 | 17 | 35.8% | 0.888 |
| Ja'Marr Chase | 15.69 | 251.1 | 16 | 32.2% | 0.743 |
| Amon-Ra St. Brown | 15.62 | 265.5 | 17 | 31.3% | 0.734 |
| CeeDee Lamb | 12.57 | 163.4 | 13 | 25.3% | 0.629 |
| Justin Jefferson | 9.38 | 159.5 | 17 | 30.1% | 0.722 |

**The buy-low read (S-tier usage + non-predictive TD variance):** Justin Jefferson finished
*outside the top 15 WRs* on PPG despite a 30.1% target share, 0.722 WOPR, 141 targets and 1048
receiving yards — his collapse was **2 touchdowns all season** (pure TD variance, the least sticky
stat). CeeDee Lamb (WR11, only 3 TDs on 1077 yds, 3 games missed) is a milder version of the same
signal. Usage says both rebound in 2026; the risk on Jefferson is Minnesota's QB play, not his role.
