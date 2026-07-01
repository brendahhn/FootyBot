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
