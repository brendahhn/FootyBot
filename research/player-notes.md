# PLAYER NOTES — per-player reads (draft-relevant)

Created 2026-07-06. A durable home for player-level findings that don't fit coach-tendencies
(team/scheme) or draft-tendencies (opponent modeling) — buy/fade reads, status-of-record on
situational risks, and pipeline-computed scoring profiles under THIS league's exact rules
(half-PPR, 6pt pass TD, -2 turnovers, +2 on 40+ yд plays, 1 flex IDP). Tiers: S = pipeline;
A = well-sourced fact; B = thin/single-source; C = archetype reasoning; Speculative = labeled bet.

## Pick-4-relevant WR scoring profiles — 2025 regular season, OUR scoring (S, pipeline)

Computed 2026-07-06 from committed nflverse data via `pipeline/league_scoring.py`. `target_share`
and `wopr` are per-game averages; PPG under this league's formula. **This is not public PPR — it's
our exact rules, which is the point.**

| WR | G | PPG | tgt% | WOPR | rec/tgt | recTD | PPG stdev |
|---|---|---|---|---|---|---|---|
| Puka Nacua | 16 | **19.4** | 30.1 | 0.69 | 129/166 | 10 | 8.8 |
| Jaxon Smith-Njigba | 17 | 17.7 | 36.8 | 0.90 | 119/163 | ? | 6.7 |
| Ja'Marr Chase | 16 | 15.7 | 32.1 | 0.74 | 125/185 | 8 | 8.4 |
| Amon-Ra St. Brown | 17 | 15.6 | 31.7 | 0.75 | 117/172 | — | 9.3 |
| George Pickens | 17 | 14.4 | 22.5 | 0.56 | 93/137 | — | 8.3 |
| Drake London | 12 | 14.0 | 29.7 | 0.73 | 68/112 | — | 9.8 |
| CeeDee Lamb | 13 | 12.6 | 25.1 | 0.61 | 75/117 | — | 5.1 |
| Justin Jefferson | 17 | **9.4** | 30.7 | 0.74 | 84/141 | **2** | 4.6 |

Reads:
- **Puka Nacua was the WR1 under our scoring in 2025** (19.4 PPG; 1,715 yds / 10 TD / 16 g) —
  ahead of Chase (15.7; 1,412 / 8 / 16 g). So at pick 4, Puka is not a downgrade from Chase; if
  anything the 2025 tape favors him. **Caveat:** one season; 2026 consensus ADP has Chase slightly
  ahead (elite target hog, 185 tgt). Take whoever's there at 4 — do NOT treat drawing Puka as a
  consolation. (Confidence S on 2025 numbers; the "going forward" ordering is deliberately NOT
  claimed — held to what the data says about the season that happened.)
- **JSN's 36.8% target share + 0.90 WOPR are the highest in this group** and his 6.7 stdev is the
  2nd-steadiest — elite, efficient volume. Consensus already top-5; priced in.
- **Justin Jefferson is a BUY-LOW, not a fade (S + A).** 9.4 PPG looks alarming, but it's driven by
  **just 2 receiving TDs** on 84/1,048 with a 30.7% target share and 0.74 WOPR. Per our OWN
  pipeline, **TD rate is noise (r=0.008 next-year) while target share is predictive (r=0.350)** —
  so the volume (elite, sticky) is real and the TD outage (unlucky, non-sticky) will regress up.
  His depressed 2025 fantasy finish reflects Minnesota's QB/offense, not his skill. Buy at the
  discount, don't avoid. This directly checks Brendan's take ("kinda a Kyler fan, he's had shitty
  QBs") — he's right about the cause, but the correct conclusion is buy-low, not fade.
- Pickens (14.4) > Lamb (12.6) corroborates the Cowboys 1a/1b read in `coach-tendencies.md`.

(Some receiving-TD cells left `—`/`?` where not separately verified this run — the PPG, target
share, WOPR, and rec/tgt are the pipeline outputs; fill TD counts on a future pass if needed.)

## Christian McCaffrey (SF RB) — pick-4 verdict: TRAP for THIS owner (A + C, compete-mode)

Full compete-mode analysis 2026-07-06 (3 angles: data-value / situation-skeptic / market). Verdict:
- **The market is not offering CMC at pick 4** — consensus 2026 ADP has him **RB3-ish, going
  6-9 overall** (Footballguys 6th, CBS #7, Underdog 7.2, DraftKings 6.2; PFF board Gibbs/Bijan/CMC).
  So "if he falls to 4" misframes it: taking him at 4 is a **reach above ADP**, not a value catch.
  The value-case agent's "he's priced at 8, so 4 is a discount" argument is inverted and was killed.
- **Why the market fades him (rational, not recency bias):** turns 30 (June 2026); came off a
  career-high ~413-touch season (led NFL) sitting on ~2,280+ career touches; "Curse of 370" (only
  ~1 of 11 RBs since 2016 to top 370 touches repeated top-5 next year); a 30-instance 350+-touch
  study found median next-year finish RB12; and CMC has personally lived the touch-cliff twice
  (403 touches 2019 → lost 2020; 417 in 2023 → 4 games in 2024). The market saw his huge, healthy
  2025 in full and *still* only moved him to RB3 — calibrated, not emotional.
- **The honest counter (kept, not buried):** this same framework was applied to CMC into 2025 and
  the market was WRONG — he fell to RB4/5 and returned a top-2 RB season. His 2025 per-touch
  efficiency showed no decline; even a "down" year likely lands RB12-15 (usable). So he's not
  washed. The claim is narrower: **pick 4 pays for his 90th-percentile outcome on the board's
  highest-variance profile, at an age/mileage/injury combo where the downside voids a top-4 pick.**
- **Owner-specific PATTERN ALARM:** CMC-at-4 is the exact **POST_INJURY-discount-at-a-premium-pick**
  archetype that is Brendan's single worst habit — Finding 5, `draft-tendencies.md`: **0-for-6,
  -46 pts/pick.** This is the loudest "don't" the profile can produce. If he insists, demand the
  extra round of discount the pattern requires — which at pick 4 doesn't exist.

## Status-of-record on situational risks (A — as of 2026-07-06, re-verify closer to camp)

- **Rashee Rice (KC WR):** OUT of jail — served a 30-day probation-violation sentence, **released
  June 16, 2026.** No NFL suspension pending (the 2024 street-racing suspension was already served
  in 2025; the DV allegation was reviewed, no violation found; THC positives aren't suspendable).
  Minor knee-debridement rehab; expected to report to camp on time. **Draftable as a full-season
  Chiefs WR.** ADP fell to early-3rd-round (buy-the-dip candidate). Corrects Brendan's stale "that
  dude's in jail." Sources: NFL.com, ESPN, CBS, Yahoo.
- **Josh Jacobs (GB RB):** Arrested May 26, 2026 (Brown County WI, incl. felony strangulation
  allegation); released May 27, **DA has NOT filed formal charges** (requested more investigation;
  nothing newer surfaced). Practicing full with the Packers ("business as usual" — LaFleur). No NFL
  suspension (matter is pre-charges, so PCP review not triggered). **Draftable at normal ADP; live
  risk if the DA later charges — re-check closer to camp.** Sources: ESPN, NFL.com, CBS, local WI.
- **Malik Nabers (NYG WR):** the real yellow flag of the offseason recoveries — needed a **second
  cleanup surgery** on the repaired ACL, described "behind schedule." GM Schoen projects Week 1 but
  hedges ("these things take time"); Giants stacked the WR room (Beckham, Mooney, Austin III, rookie
  Fields) as insurance. Treat as a Round 3-4 value with real Week 1 risk, **not a clean top-12 lock.**
- **Xavier Worthy (KC WR):** torn labrum (Wk 1 2025) surgically repaired; still in a **non-contact
  yellow jersey** through June minicamp, working as de facto WR1 with Rice out. Expected full-go by
  preseason — modest confidence shave until seen in pads.
- **Marvin Harrison Jr. (ARI WR):** back from a stacked 2025 injury list (appendicitis, two heel
  injuries, concussion); practiced in OTAs, says he doesn't expect lingering effects (B — self-report
  on an A-tier fact that he's practicing).
- **Patrick Mahomes (KC QB):** ACL/LCL recovery "way ahead of schedule" (GM Veach); cleared for
  individual work, deliberately held out of 11-on-11 through minicamp. Trending to a normal Week 1
  (Sept 8 MNF vs. DEN) but the held-out-of-team-drills note keeps him a late-round QB dart, not a
  locked QB1 price — and in this 6pt-pass-TD league, mid-round QB is Brendan's best habit anyway.
