# 2025 weekly fantasy profiles — draft-relevant players (this league's scoring)

Status: created 2026-07-04 (Lane A). **S-tier / pipeline-computed** from the committed weekly
nflverse data (`data/raw/player_stats_weekly.csv`, 2025 REG season only) scored with this
league's exact formula (`pipeline/league_scoring.py`). Reproducible:
`python3 pipeline/player_season_profile.py 2025 "<name>" ...`.

Why weekly, not season totals: several of Brendan's draft takes are about **consistency**
("I bank on him being good but he's not"), and the archetype work (`draft-tendencies.md`
Findings 4-5) is about buying suppressed prices. Season aggregates hide both. These columns
expose the week-to-week distribution a manager actually lived through.

**Known scoring gap (inherited):** 40+ yard-play bonuses (+2) and offensive fumble-return TDs
are not in weekly aggregate data, so every score slightly under-counts big-play weeks — a
small, boom-play-dependent undercount, documented not silent.

Columns: **G** games with a stat line · **PPG** mean over games played · **PP17** points
averaged over a full 17-game season (missed games = 0; the real cost of absences) · **MED**
median week · **SD** stdev (volatility) · **BOOM** weeks ≥20 (true WR1/RB1 week) · **START**
weeks ≥12 (startable) · **DUD** weeks <8 (unstartable, among games played) · **BEST/WORST** high/low week.

| Player | G | PPG | PP17 | MED | SD | BOOM | START | DUD | BEST | WORST |
|---|---|---|---|---|---|---|---|---|---|---|
| Puka Nacua | 16 | 19.4 | 18.3 | 18.7 | 8.8 | 6 | 13 | 1 | 40.5 | 3.8 |
| James Cook | 17 | 16.8 | 16.8 | 18.7 | 8.8 | 6 | 11 | 2 | 33.6 | 1.5 |
| Ja'Marr Chase | 16 | 15.7 | 14.8 | 15.2 | 8.4 | 5 | 11 | 5 | 30.1 | 3.6 |
| Amon-Ra St. Brown | 17 | 15.6 | 15.6 | 14.2 | 9.3 | 4 | 11 | 4 | 34.9 | 0.0 |
| Drake London | 12 | 14.0 | 9.9 | 12.4 | 9.8 | 4 | 6 | 4 | 34.3 | 0.9 |
| Chris Olave | 16 | 13.6 | 12.8 | 11.1 | 7.1 | 3 | 7 | 3 | 31.8 | 4.5 |
| Saquon Barkley | 16 | 13.4 | 12.6 | 13.5 | 6.8 | 2 | 8 | 5 | 31.4 | 4.7 |
| Ashton Jeanty | 17 | 12.8 | 12.8 | 10.9 | 8.3 | 3 | 7 | 6 | 32.5 | 3.9 |
| Nico Collins | 15 | 12.7 | 11.2 | 12.7 | 5.7 | 1 | 8 | 5 | 22.0 | 4.0 |
| CeeDee Lamb | 13 | 12.6 | 9.6 | 14.1 | 5.1 | 1 | 8 | 2 | 20.7 | 0.9 |
| Tee Higgins | 15 | 12.1 | 10.7 | 10.9 | 7.3 | 2 | 7 | 5 | 29.6 | 2.0 |
| Emeka Egbuka | 17 | 9.7 | 9.7 | 6.5 | 7.5 | 3 | 4 | 10 | 27.8 | 1.3 |
| Marvin Harrison Jr. | 12 | 8.9 | 6.3 | 8.3 | 5.8 | 0 | 4 | 6 | 19.1 | 0.0 |
| Xavier Worthy | 14 | 6.3 | 5.2 | 6.7 | 3.7 | 0 | 1 | 10 | 14.6 | 0.0 |

## What the distributions say (reads, not just numbers)

- **The pattern-alarm trio Brendan circles as pick-4-adjacent "upside" — Egbuka, MHJ, Worthy —
  were all low-end-to-unrosterable in 2025.** Egbuka: 10 dud weeks of 17, median 6.5, boom/bust
  WR3 line (the spikes are real — 3 booms, 27.8 high — but you weren't starting him most weeks).
  MHJ: zero boom weeks, missed 5 games, PP17 6.3. Worthy: **1 startable week all season**, 10
  duds, 0 booms, PP17 5.2 (a lost post-ACL year). This is the empirical backbone of the PATTERN
  ALARM (`draft-tendencies.md` Finding 5): these are genuine reclamation bets, not safe picks,
  and Brendan's realized history on exactly this profile is 0-for-6 post-injury / 33% second-year.
  The 2025 line doesn't kill the bet (suppression is the premise of a buy-low) — it prices it:
  demand a steep discount, don't pay an "upside" tax.
- **Tee Higgins — Brendan's "good but not [consistent]" take is DATA-CONFIRMED.** 12.1 PPG reads
  like a solid WR2, but a third of his games played (5 of 15) were duds (<8), he missed 2 more,
  and SD 7.3 with a 2.0 floor game — startable talent, unreliable delivery + availability. Not
  the every-week anchor an ADP near the WR1/2 line would imply.
- **James Cook — Brendan's "overvalued" take is NOT supported by his 2025 box score.** 16.8 PPG,
  played all 17, median 18.7, 6 booms, only 2 duds — that is a durable, consistent RB1 line, the
  opposite of overvalued *on last year's production*. The "overvalued" case has to rest on
  forward regression (2025 leaned on a rushing-title workload + a high TD count that tends to
  regress; Buffalo's new Payton-tree OC staff — see `coach-tendencies.md` Bills — could rebalance
  his volume), not on him being a weak player. That's a bet on change, not a read on quality.
- **Puka Nacua is the cleanest elite line in the set** (19.4 PPG, 13 startable of 16, one dud all
  year) — relevant to pick 4, where he's a live option alongside Chase. Chase's floor is spikier
  (5 duds) despite a similar ceiling.
- **Saquon Barkley: 13.4 PPG, only 2 boom weeks, 5 duds** — a down 2025 (consistent with the
  yards-before-contact collapse in `coach-tendencies.md`). Solid RB1 role, but the 2025 tape is a
  workhorse floor, not the 2024 ceiling — matches the "don't pay a 2024-ceiling price" read.

## Extend this

`pipeline/player_season_profile.py` takes any name list and any season present in the data
(2016-2025). Natural next passes: multi-year consistency (same player across 3 seasons), and a
league-wide scan for the highest-floor (fewest duds) vs highest-ceiling (most booms) profiles at
each position for tiering (Phase 2).
