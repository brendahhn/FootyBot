# League draft tendencies — opponent modeling (2019-2025)

Status: first pass 2026-07-01, built from **real data** — 7 seasons of this league's actual
Yahoo draft boards (2019-2025), 1,120 total picks, joined to the 10 stable managers and
enriched with player positions from the committed nflverse data. Source dataset:
`inputs/league-history/draft_history_master.csv`; reproducible via
`pipeline/extract_yahoo_mhtml.py` → `pipeline/build_draft_history.py`. This is **S-tier by
provenance** (the league's own history, not a projection) — the only soft spots are noted inline.

## What this is for

Brendan drafts 4th in 2026 and wants to model how each of his 9 leaguemates drafts — so he can
anticipate runs, know who will let a QB slide, and know who he's actually competing with for a
given archetype. This is opponent modeling, a scope beyond pure player research (see
`CONTEXT.md` — added as a Goal item 2026-07-01).

The 10 managers (stable across all 7 years): Aaron, Brendan (us), Connor, Dylan, Jack, lucas,
Mattias, Nate, Niko, riley. Team nicknames change yearly; managers don't — the join is keyed on
the per-year Managers page, validated to 0 unmapped picks and exactly 16 picks/manager/year.

Data caveats (kept honest): position is matched for ~96% of picks; the ~4% unmatched are team
defenses, kickers, and IDP (correctly not RB/WR/QB/TE) plus 3 skill players with name-suffix
quirks (Hollywood Brown, Kenny Gainwell, Joshua Palmer — hand-corrected in the analysis below).
Positional counts below are reliable for the skill positions that matter for draft strategy.

## Finding 1 — QB draft timing (this is the big one, given 6pt passing TDs)

Average round each manager takes their **first** QB, across the 7 drafts (lower = earlier):

| Manager | Avg first-QB round | Earliest | Latest | Read |
|---|---|---|---|---|
| Aaron | 5.0 | 3 | 7 | **Earliest QB drafter** — will grab a QB before you if you both want one |
| lucas | 5.3 | 3 | 9 | Early-QB lean |
| Niko | 6.1 | 3 | 13 | Middle, but capable of a round-3 reach |
| Jack | 6.3 | 3 | 11 | Middle |
| Mattias | 7.1 | 3 | 11 | Middle |
| riley | 7.1 | 5 | 9 | Middle, consistent (never earlier than 5) |
| **Brendan (us)** | 7.7 | 5 | 12 | We wait on QB — worth knowing about ourselves |
| Connor | 8.3 | 5 | 13 | Late-QB lean |
| Nate | 8.3 | 3 | 14 | Late on average but *has* reached round 3 — high variance |
| **Dylan** | **10.3** | **7** | 13 | **The QB-punter — never taken a QB before round 7, ever** |

**Actionable:** in a 6pt-passing-TD league, QB value is elevated vs. standard, but this league
has NOT historically adjusted for that — most managers still wait (league-wide first QB averages
round ~7). **Dylan reliably punts QB to round 7+**, so an elite QB will almost never be taken by
him early. **Aaron and lucas are the two to watch** if you're deciding whether to reach for a QB
— they're the only two who consistently move in the round 5 range. If you (Brendan) ever want to
zag and take a top QB early to exploit the 6pt scoring, the board history says you'd be doing it
2-3 rounds ahead of the field, i.e. you could likely wait longer than instinct suggests and still
get a top-5 QB. (Verify against 2026 ADP closer to the draft — behavior can shift.)

## Finding 2 — Round 1 position tendency (7 first-round picks each)

| Manager | Round 1 picks (7 drafts) | Read |
|---|---|---|
| Aaron | RB 6, WR 1 | Hardcore RB-first |
| lucas | RB 5, WR 2 | RB-first |
| Connor | RB 5, WR 1, TE 1 | RB-first (and the rare R1 TE) |
| Niko | RB 4, WR 2, TE 1 | RB-lean (and the rare R1 TE) |
| Brendan (us) | RB 4, WR 3 | Slight RB-lean |
| Dylan | RB 4, WR 3 | Slight RB-lean |
| Mattias | RB 4, WR 3 | Slight RB-lean |
| Nate | RB 4, WR 3 | Slight RB-lean |
| riley | RB 4, WR 3 | Slight RB-lean |
| **Jack** | **WR 5, RB 2** | **The ONLY WR-first drafter in the league** |

**Actionable:** this quantitatively confirms Brendan's own instinct from his mock-draft voice
memo ("running backs in my league get so much more valued... you can always scrounge a receiver,
but not so much a running back"). **9 of 10 managers lean RB in round 1; only Jack bucks it.**
That means: (a) the RB run comes early and hard — elite RBs will not slide; (b) WRs are
systematically slightly devalued at 1.x, so an elite WR is more likely to fall to you at pick 4
than an elite RB is. At pick 4 specifically, expect the top 3 to skew RB-heavy, leaving a strong
WR (or the best-available RB) for you — which matches how the 2025 board actually fell (Chase,
Bijan, Gibbs, then Saquon at 4).

## Finding 3 — Early-draft (rounds 1-5) RB vs WR identity

| Manager | RB | WR | TE | QB | Early lean |
|---|---|---|---|---|---|
| Connor | 18 | 14 | 2 | 1 | Strong RB |
| Niko | 17 | 14 | 1 | 3 | RB |
| Dylan | 16 | 16 | 3 | 0 | Balanced (and 0 early QBs — see Finding 1) |
| Aaron | 15 | 11 | 4 | 5 | RB + earliest QBs + most early TEs |
| Mattias | 15 | 15 | 3 | 2 | Balanced |
| lucas | 15 | 14 | 2 | 4 | Balanced, QB-forward |
| Nate | 15 | 16 | 2 | 2 | Slight WR |
| Jack | 14 | 15 | 3 | 3 | Slight WR (consistent with his R1 WR lean) |
| **Brendan (us)** | 14 | 18 | 2 | 1 | **Most WR-heavy early build in the league** |
| riley | 13 | 17 | 3 | 2 | WR-lean |

**Actionable (self-scouting):** Brendan is the **most WR-heavy early drafter** in the league
(18 WR / 14 RB in rounds 1-5 across 7 years) *and* one of the latest QB drafters. Worth being
honest with ourselves about: in a league where everyone else prioritizes RB, our WR-heavy build
is a real market-inefficiency play (we let the RB run happen and scoop the falling WR value) —
but it also means we're often thin at RB, the position this league treats as scarce. The mock
where Brendan wanted "Saquon + Chase" is notable precisely *because* it would break his own
pattern toward securing RB early.

## Finding 4 — Archetype profiles: what each manager was THINKING at the time (added 2026-07-02)

Built by reconstructing what every drafted player **looked like on that draft day** from the
committed nflverse history (1999-2025) scored with this league's formula: rookie or vet,
coming off a first breakout, coming off a lost/injury year, boom/bust weekly profile, aging.
Pipeline: `pipeline/draft_archetypes.py` → `inputs/league-history/draft_history_enriched.csv`
(every pick now carries experience-at-pick, prior-season games/PPG, weekly variance, and
archetype flags). **S-tier provenance** (computed from real weekly data, this league's actual
picks); the flag *definitions* are explicit tunable choices documented in the script — e.g.
"BREAKOUT_CHASE" = drafting a player right after his first startable season (≥11 PPG over ≥8
games with <8 PPG the year before).

Shares of each manager's skill-position picks in rounds 1-8 (56 picks each, 7 drafts).
League-average column for contrast:

| Manager | Rookie | 2nd-yr | Breakout-chase | Post-injury | Boom/bust | Aging vet | Steady |
|---|---|---|---|---|---|---|---|
| League avg | 6% | 14% | 13% | 6% | 7% | 14% | 44% |
| Aaron | 4% | 20% | **21%** | 7% | 11% | 11% | **52%** |
| Brendan (us) | 5% | **21%** | 18% | **11%** | 11% | 7% | **38% (lowest)** |
| Connor | 4% | 11% | 14% | 11% | 7% | **29% (2× league)** | 46% |
| Dylan | **13%** | 13% | **22% (highest)** | 4% | 9% | 11% | 40% |
| Jack | 4% | **5%** | **4%** | 9% | 11% | 14% | 45% |
| Mattias | 4% | 20% | 15% | 5% | 4% | 15% | 47% |
| Nate | 4% | 18% | 7% | **0%** | 5% | 12% | 46% |
| Niko | **14% (highest)** | 9% | 14% | 4% | 4% | 7% | 43% |
| lucas | **0%** | 11% | 14% | 5% | 4% | 16% | 46% |
| riley | 5% | 9% | 5% | 4% | 7% | 18% | 36% |

Spot-check validation (flags catch exactly the right players): Niko's ROOKIE picks = Bijan
(R1!), Etienne, Swift, Jacobs, Brian Thomas, TreVeyon Henderson, T-Mac, Egbuka. Connor's
AGING_VET = Julio 3 straight years, old Kelce R1, old Hopkins, Keenan, T.Y. Hilton. Brendan's
POST_INJURY = 2021 R1 CMC (off the 3-game year), 2023 R1 Kupp (off the 9-game year), Fuller,
Sutton, Freeman. Dylan's BREAKOUT_CHASE = McLaurin, JT, CeeDee, Claypool, Chark, Kyren — all
drafted immediately after their first big year.

### Manager personalities (the "thought process" reads)

- **Niko — the rookie reacher.** Highest rookie rate (14%, incl. an R1 rookie), lowest
  boom/bust — he takes *young*, not *volatile*. If you want a rookie at pick 4, Niko is the
  primary race.
- **Dylan — chases last year's breakout.** Highest breakout-chase (22%) + high rookie rate +
  never takes a QB early. The shiniest recent production owns his board.
- **lucas — will NEVER take your rookie.** Zero rookies in rounds 1-8 across seven drafts.
  Rookie values don't get eaten by him, ever.
- **Jack — buys established only.** Rock-bottom rookie/2nd-year/breakout-chase (4/5/4%) — he
  pays for multi-year track records (fits his WR-first R1 profile). Youth falls past him.
- **Connor — the aging-brand-name guy.** 29% aging-vet, double the league rate. He will
  overpay for the declining big name — let him have it, don't fight that bid.
- **Nate — allergic to damaged goods and hype.** ZERO post-injury picks in 7 years, and
  near-lowest breakout-chase (7%). Injury-discounted players fall further than ADP implies
  partly because of him.
- **Aaron — proven production, early QB.** Highest steady share (52%) + high breakout-chase:
  he buys players who scored *last year*, whatever the profile, and takes QBs earliest.
- **Mattias — quietly risk-averse.** Low boom/bust (4%), no strong tilts, balanced everything.
- **riley — hardest to model.** Lowest steady share alongside Brendan, elevated aging-vet, low
  breakout-chase; no dominant pattern (consistent with his mid-pack, low-variance QB timing).
- **Brendan (us) — the discount-rack shopper.** LOWEST steady share in the league (38%),
  tied-most post-injury picks (2021 R1 CMC, 2023 R1 Kupp), high 2nd-year rate. We buy
  suppressed prices on talent coming off bad years — upside-seeking, floor-light. Notably:
  in the 2025-07-01 mock memo, the players he circled (Egbuka, MHJ, Worthy post-ACL) are…
  post-injury/2nd-year discounts again. It's a durable personality, so the question the
  newsletter should pressure-test: **has the injury-discount habit actually paid off?**
  (→ AUDIT_QUEUE: compute realized outcomes of those picks vs. same-round alternatives.)

### Draft-day exploits at pick 4 (2026)

1. Rookie you love? Beat **Niko** (and secondarily Dylan) to him — nobody else competes early.
2. Post-injury discount targets last longer than market ADP suggests here — **Nate never bids**
   and most of the league is near league-average; main competition for those is… ourselves.
3. Aging brand names will go earlier than value — **Connor's bid** — never reach to beat him.
4. Last year's breakout WR/RB will be gone sooner than ADP — **Dylan and Aaron** both chase.

## Finding 5 — Which habits actually WIN: realized outcomes (added 2026-07-02)

Metric: each pick's REG-season **total** league-scoring points in its draft year vs the median
of all picks in that same round that year ("round-relative delta"; total, not PPG, because
missed games ARE the outcome of a pick). Rounds 1-8, skill positions, 558 picks. Pipeline:
`pipeline/draft_outcomes.py`. **S-tier provenance; one honest limitation:** this measures
draft-value, not league standings — we don't have final standings data yet (requested from
Brendan; see open threads). Draft value ≈ but ≠ winning (waivers/trades/luck matter).

### League-wide: which archetypes return value

| Archetype | Picks | Hit rate | Avg delta | Verdict |
|---|---|---|---|---|
| STEADY | 245 | 55% | **+20.9** | **Boring wins. The only strongly positive archetype.** |
| BOOM_BUST | 40 | 50% | +3.5 | Volatility itself isn't the trap |
| ROOKIE | 31 | 52% | -1.8 | Roughly fair-priced in this league |
| SECOND_YEAR | 76 | 42% | -5.5 | The year-2-leap bet slightly loses |
| AGING_VET | 78 | 46% | -5.9 | Slightly loses (Connor's habit) |
| BREAKOUT_CHASE | 75 | 43% | -7.1 | Chasing last year's breakout loses |
| POST_INJURY | 33 | **33%** | -7.4 | **The worst archetype in the league's history** |

### Manager draft-value leaderboard

All-years avg delta: **Niko +26.1** and **lucas +20.4** clearly best (notably: the rookie-reacher
AND the zero-rookies guy — opposite styles, both disciplined); Jack +10.7, Dylan +10.3 (and
Dylan is 75% hit rate in 2024-25 — hottest recent drafter), riley +8.8, Connor +5.2, Mattias
+0.9, Nate -6.4 (**-30.1 in 2024-25, coldest recent**), Brendan -7.0, Aaron -10.1.

### The QB question — "is the league catching on?" (Brendan's hunch, tested)

Avg round of each manager's first QB by year: 2019: 7.7 → 2020: 7.5 → 2021: 7.1 → 2022: 8.0 →
**2023: 6.4 → 2024: 6.3** (7 QBs gone by R6 both years, vs ~4 historically) → **2025: 7.1**
(back to 5 by R6). Verdict: the league DID speed up in 2023-24, then relaxed in 2025 — the
edge shrank but did not close. And the payoff is real: **Brendan's three best value picks in
seven years are all mid-round QBs** — Lamar R6 2022 (+127), Mahomes R5 2024 (+110), Herbert R6
2023 (+88). In a 6pt-passing league where most of the room still waits, the round 5-6 elite-QB
window has been his single most profitable move. Keep exploiting it until the room actually
closes it.

### Brendan: good points vs bad points (he asked for this straight — receipts attached)

**What works (keep doing):**
- **Mid-round QBs — your superpower.** Top-3 best picks ever, all this move. (See above.)
- **Aging vets: 4-for-4, +48.0 avg** (Davante ×2, old Hopkins) — your best per-pick archetype.
  You beat the league's 46% at 100%. Small sample, but your old-guy eye is genuinely good.
- **STEADY picks: 67% hit, +9.1** — above the league's 55%. When you draft boring, you win.
- **BOOM_BUST: 67% hit** — you pick volatile players well (Diontae '20 +88).

**What doesn't (the leak, and it's your signature move):**
- **POST_INJURY: 0-for-6, average -46 points per pick.** CMC '21 (R1, -98), Kupp '23, Fuller,
  Sutton, Freeman, Hunt — not one beat its round median. The discount rack is a trap league-wide
  (33% hit) and it is YOUR most distinctive habit (tied-most such picks).
- **SECOND_YEAR: 33% hit, -32.6 avg** — CEH '21 (-113), Kerryon '19 (-127), Kyle Pitts '22
  (-86), Brian Thomas '25 (-142, your single worst pick in seven years).
- Net: 52% hit rate (fine) but -7.0 avg delta — **you hit singles often and strike out
  catastrophically**; the misses cluster in exactly two archetypes: post-injury + second-year
  "upside."
- **Live warning for Aug 28:** your 2025-07-01 mock memo circles Egbuka (injury-shortened),
  MHJ (injury-shortened), Worthy (post-ACL) — that's the same pattern that's 0-for-6. Doesn't
  mean those players are wrong; means the *price you'll happily pay* for them is historically
  ~46 points too high. Demand an extra round of discount on injury-story players.
- 2024-25 recency view: 62% hit, -2.3 — trending better.

## Finding 6 — Draft vs. in-season vs. luck: what actually decides finishes (added 2026-07-02)

Brendan sent final standings for 6 seasons (2019-2023, 2025; the 2024 upload was a draft page
by mistake — re-send pending). `pipeline/build_league_finishes.py` →
`inputs/league-history/league_finishes.csv` (rank, W-L, PF/PA, waiver, in-season move count
per manager-season; ranks are FINAL, playoffs included). 60 manager-seasons.

**Brendan's explicit methodological caveat, honored:** "if a guy drafts an RB 1 overall and
wins, that doesn't mean RB is the best pick — lots of guys make moves throughout the season."
So we don't claim causation; we DECOMPOSE. Spearman correlations across the 60 manager-seasons:

| Relationship | r | Read |
|---|---|---|
| Draft value → points-for | **+0.50** | Drafting well genuinely drives scoring (~25% of variance) |
| Points-for → final rank | +0.59 | Scoring drives finishing — but far from fully (schedule luck is real) |
| Draft value → final rank | +0.31 | By the time playoffs/luck filter it, draft explains only ~10% of finish |
| In-season MOVE COUNT → final rank | **+0.03** | Waiver churn volume is pure noise for finishing |
| Move count → points-for | -0.16 | If anything, high churn associates with LOWER scoring (likely reverse causation: bad teams churn) |

**The honest decomposition:** the draft matters (it's the biggest single controllable input to
points-for) but is nowhere near destiny — 2 of the 6 champions (Mattias '19, Jack '20) won with
*below-median* draft value, while 4 of 6 (Dylan ×2, Connor '22, Niko '23) drafted strongly
positive. And the thing everyone thinks matters — "making moves" — has ZERO correlation with
finishing in this league by count. Caveat on the caveat: move *count* ≠ move *quality*; a
manager making 3 great pickups beats one making 40 sideways ones, and count can't see that.
Measuring move quality needs transaction-level data (who was added/dropped when) — flagged as
an open thread if Brendan can export transaction logs.

### Finishes by manager (6 seasons)

| Manager | Avg finish | Titles | Top-3s | Trajectory |
|---|---|---|---|---|
| Jack | **3.5** | 1 | 2 | Best sustained — never worse than 6th |
| Dylan | 4.2 | **2** | 3 | Two titles including 2025 — reigning champ + hottest drafter |
| lucas | 4.8 | 0 | 3 | Always competitive, no ring |
| Niko | 4.8 | 1 | 2 | Boom-bust standings profile |
| Connor | 4.8 | 1 | 3 | Improved sharply 2022-2025 |
| riley | 6.0 | 0 | 2 | Declining: 2→3→5→7→9→10, five straight years worse |
| Mattias | 6.2 | 1 | 2 | Feast or famine: a title + three last-places |
| **Brendan** | **6.7** | **0** | **1** | 8th of 10. Finishes: 9,5,3,8,7,8 |
| Nate | 6.8 | 0 | 0 | Never top-3 in six seasons |
| Aaron | 7.2 | 0 | 0 | Never top-3; worst avg |

**Brendan reality check (he asked for straight talk):** no titles, one top-3, 8th-best average
finish — AND below-median draft value (Finding 5). The two aren't independent: his
draft-value leak (post-injury/second-year busts) directly costs points-for, and points-for is
the strongest rank driver we measured. One nuance in his favor: his best finish (3rd, 2021)
came in the year his R1 pick (post-injury CMC) was a -98 bust — meaning his in-season
management carried a broken draft to a podium. The skill is there; the draft keeps burying it.
Fixing the two leak archetypes is, by this data, the single highest-leverage change available.

### Cross-check vs. archetype habits (correlation ≠ causation, stated plainly)

The two best sustained finishers (Jack, Dylan) map to opposite draft styles — Jack buys
established/WR-first, Dylan chases breakouts and rookies — so no single archetype "wins the
league." What they share: both are top-4 in realized draft VALUE (Finding 5). The common
thread is drafting well *by their own method*, not a magic archetype. The losing common
thread is real though: the league's worst finishers (Aaron, Nate, Brendan) are all bottom-3
in draft value too. Draft value ≈ floor; in-season play + luck decide the ceiling.

## Next steps / open threads

- **[data]** More draft years if available would tighten the QB-timing averages (7 is enough for
  a lean, not for high confidence on the high-variance managers like Nate).
- **[analysis — DONE 2026-07-02]** Rookie/"flashy new guy" tendency — built as Finding 4 above
  (`pipeline/draft_archetypes.py`, enriched CSV). Remaining refinement: flag thresholds are
  tunable choices; revisit if any personality read feels off against known history.
- **[analysis — NEW]** Realized outcomes of archetype bets: did Brendan's post-injury picks
  (CMC '21, Kupp '23…) actually return value vs. same-round alternatives? Did Dylan's
  breakout-chases hit? Computable from the same data — strong newsletter deep-dive candidate.
- **[analysis]** Reach vs. value — join each pick to that year's ADP to see who consistently
  reaches vs. who waits for value. Needs historical ADP data (not yet available).
- **[caveat]** All of this is descriptive of 2019-2025 behavior; people change. Re-weight toward
  recent years (2023-2025) if a manager's style has visibly shifted, and re-verify against 2026
  behavior once this year's draft happens.
