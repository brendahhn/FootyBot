# Does drafting RBs early actually win in THIS league?

> Question from Brendan, 2026-08-26: *"I have a theory RBs are incredibly valuable in my
> league — does drafting more RBs early translate to success?"* Tested at the four cutoffs he
> named: RB count through rounds 2, 4, 6, 8.
>
> Reproduce: `python3 pipeline/rb_draft_timing.py`. Sources: `inputs/league-history/`
> (our own 2019-2025 draft boards + final standings) and `inputs/nflverse/` weekly stats
> scored with `pipeline/league_scoring.py` (this league's exact formula).

## Short answer

**No. Seven years of this league's own boards do not support it — at any of the four cutoffs.**

Two things are true at once, and the gap between them is the whole answer:

1. **Every RB signal in the standings points the theory's way** (more early RB → better rank,
   more points; the WR mirror points the other way, consistently). That directional consistency
   across eight independent tests is not nothing.
2. **Not one of those tests survives correction for having tried four cutoffs**, and the
   far better-powered test — what the picks actually *returned* — finds **no measurable
   difference between an RB and a WR taken at the same draft cost, in any round window**
   (all p > 0.21).

So the honest verdict is *"undetectable at this sample size"*, not *"disproven"* and certainly
not *"incredibly valuable."* If RBs carried a real premium here, ~560 picks should have shown
it, and it didn't.

**The one finding that nearly clears the bar is the opposite of the theory: RBs drafted in
rounds 7-8 bust three times as often as WRs taken there (16% vs 5%, p=0.051).**

**Practical read for Aug 28 at pick #4: draft RB early because the board hands you one, not
because the position pays a premium here — and stop force-feeding RB from round 5 on.**

## What was tested, and why two different tests

Two independent angles, because each has a fatal weakness alone:

| | Allocation test | Return test |
|---|---|---|
| Question | Do managers who draft more early RBs finish better? | At the same draft cost, does an RB out-earn a WR here? |
| Unit | manager-season | individual pick |
| N | **60** (2019-2023 + 2025 × 10 managers) | **~560** (rounds 1-8 skill picks, 2019-2025) |
| Weakness | tiny N; final rank ≈ points + schedule luck | ignores roster construction / scarcity |

There are 70 drafted manager-seasons but only 60 scored ones — **no 2024 standings are on
file**, so 2024's drafts are dropped from the join. Points-for is z-scored within season
(`pf_z`) so scoring drift between years can't manufacture a correlation. `pf_z` is the better
signal of the two outcomes: final rank in a 13-week season is points-for plus schedule luck.

Managers do vary enough to test this — through round 6, RB counts run 1 to 4 (mean 2.47);
through round 8, 1 to 5 (mean 3.09).

## Result 1 — allocation: the direction is right, the significance is not

Sign convention: for rank, **negative = RB-heavy finishes better**; for points, **positive =
RB-heavy scores more**. `r|slot` controls for draft slot (elite RBs are simply available at
pick 1-3). `within-mgr` demeans by manager, asking whether a manager going *more* RB-heavy
than his own norm does better — that removes "some managers are just good."

| Predictor | r vs rank | p | r vs pf_z | p | pf_z r\|slot | pf_z within-mgr |
|---|---|---|---|---|---|---|
| RB through R2 | -0.129 | 0.35 | +0.046 | 0.73 | +0.071 | +0.042 |
| RB through R4 | -0.064 | 0.65 | +0.013 | 0.93 | -0.005 | +0.054 |
| **RB through R6** | **-0.226** | 0.10 | **+0.298** | **0.02** | +0.271 | +0.310 |
| RB through R8 | -0.082 | 0.57 | +0.109 | 0.42 | +0.062 | +0.157 |
| WR through R6 (mirror) | +0.084 | 0.55 | -0.223 | 0.09 | -0.226 | -0.252 |

p-values are 20,000 within-season permutations (shuffling outcomes inside each year, so the
league structure — someone always finishes 1st — is held fixed).

**Every RB coefficient has the theory-friendly sign and every WR coefficient has the opposite
sign.** That consistency is the strongest thing in this analysis.

**But**: four cutoffs were tried against two outcomes. Testing the *best of the four* RB
cutoffs against chance — the honest correction — gives **p = 0.071 for points and p = 0.257
for rank**. Neither clears 0.05. One marginal hit out of eight tries is roughly what noise
produces.

### Bucket view (RB count through round 6)

| RBs by R6 | N | mean rank | mean pf_z | %top-3 | %champ | %bottom-3 |
|---|---|---|---|---|---|---|
| 1 | 4 | 6.25 | -0.53 | 25% | 25% | 50% | *(too thin)* |
| 2 | 23 | 6.17 | -0.22 | 26% | 0% | 35% |
| 3 | 30 | 5.07 | +0.13 | 33% | 17% | 27% |
| 4 | 3 | 3.67 | +1.05 | 33% | 0% | 0% | *(too thin)* |

Through round 8 the pattern **stops climbing and reverses**: 3 RBs by R8 is the best cell
(mean rank 4.94, pf_z +0.34, 39% top-3, N=31); 4 RBs by R8 is worse (6.00, -0.33, N=15).
The shape is a hump at ~3 RBs, not "more is better."

Narrowing to *where* the RBs were taken, only one window carries any signal at all —
**rounds 5-6** (r=+0.319 vs points, p=0.016 uncorrected). Rounds 1-2 are flat (+0.046) and
rounds 7-8 are negative (-0.198). That is a strange shape for a real scarcity effect, which
should be strongest at the top, and Result 2 does not corroborate it. Treat it as noise until
another season or two of standings says otherwise.

**Champions' actual builds** (6 title teams): RB@6 was 3, 3, 3, 3, 1, 3 — five of six champions
had exactly 3 RBs through six rounds. RB@2 was split 2/2/1/1/1/1. The one title team that
punted RB entirely (Niko 2023, 1 RB through 6 rounds) posted the *second-highest* points-for
in the sample (pf_z +1.19).

## Result 2 — return: at the same draft cost, RBs and WRs have returned the same

Every rounds-1-8 skill pick from 2019-2025, scored under this league's formula in the season it
was drafted for. **VOR** = points over positional replacement (the 25th RB / 30th WR season of
that year; RB-vs-WR is insensitive to the exact baseline since both move together).

| Window | Pos | N | mean pts | mean VOR | hit% | bust (<50 pts) |
|---|---|---|---|---|---|---|
| R1-R2 | **RB** | 80 | 217.2 | **+59.2** | 46% | 4% |
| R1-R2 | WR | 54 | 207.5 | +49.7 | 52% | 2% |
| R3-R4 | RB | 45 | 173.0 | +15.2 | 44% | 4% |
| R3-R4 | WR | 69 | 168.0 | +10.5 | 49% | 4% |
| R5-R6 | RB | 48 | 154.2 | -4.7 | 44% | **12%** |
| R5-R6 | WR | 61 | 157.3 | +1.5 | 49% | 8% |
| R7-R8 | RB | 43 | 125.5 | **-33.8** | 47% | **16%** |
| R7-R8 | WR | 65 | 137.2 | -19.6 | 46% | 5% |

The gaps look suggestive — RB ahead early, WR ahead late — so they were tested directly by
shuffling the position labels within each window (20,000 permutations):

| Window | RB − WR, VOR | p | RB − WR, bust rate | p |
|---|---|---|---|---|
| R1-R2 | +9.5 | 0.50 | +1.9pp | 0.65 |
| R3-R4 | +4.7 | 0.70 | +0.1pp | 1.00 |
| R5-R6 | -6.2 | 0.60 | +4.3pp | 0.53 |
| R7-R8 | -14.1 | 0.22 | **+11.7pp** | **0.051** |

**None of the points gaps is distinguishable from zero.** The rounds-1-2 RB edge — the one
result that would most support the theory — is +9.5 points over a *whole season*, under a
point a week, at p=0.50. That is a coin flip, not an edge. Do not draft on it.

The only near-significant thing in the table is **late-round RB bust risk**: 16% of RBs taken
in rounds 7-8 scored under 50 points all season, against 5% of WRs (p=0.051; widening to
rounds 5-8 gives 14% vs 6%, p=0.063). Same-cost RBs and WRs return the same *on average*
late, but the RB version fails outright far more often.

Note this contradicts the rounds-5-6 allocation blip above, on ~9× the sample. Believe this
table over that one.

*(The QB rows in the script's output show huge raw totals — that is the 6-point passing TD, and
it is misleading here: only one QB starts, so replacement level is high. QB/TE VOR depends
heavily on the assumed baseline; don't read those rows as findings. `research/positional-value.md`
is the place for that question.)*

## Confounds not removed

- **Draft slot** is controlled for (partial correlations barely move), but slot and RB
  availability are entangled in a snake draft in ways a linear control can't fully strip.
- **This measures allocation, not player quality.** "Took 3 RBs" says nothing about whether
  they were the right three. `pipeline/draft_outcomes.py` covers the quality side.
- **In-season management and schedule luck** move final rank independently. A prior finding in
  this repo measured draft value → PF at r≈+0.50 but draft value → final rank only r≈+0.31.
- **No 2024 standings.** Adding them would take the sample from 60 to 70 manager-seasons and is
  the single cheapest way to sharpen every number here.

## What this means for Brendan specifically

From the per-manager table: Brendan's career mean RB@2 is 1.00 (tied third-lowest) and RB@8 is
2.83 — the **second-lowest early-RB load in the league** — alongside the worst mean points-for (pf_z
-0.75) and a 6.67 mean finish. That is consistent with `research/draft-tendencies.md` Finding 3
(he is the WR-leaning one besides Jack).

Careful, though: **Jack is the league's only true WR-first drafter (RB@2 = 0.83, the lowest)
and has the best mean finish, 3.50.** Across the 10 managers, career early-RB lean correlates
*positively* with mean rank (r=+0.40 at RB@2 — i.e. the RB-heavy crowd finishes slightly
*worse*), while correlating near zero with points. With N=10 that is noise in the other
direction, but it does rule out "the RB-first drafters are the winners here" as a clean story.
Brendan's low finishes are more likely about pick quality than about RB allocation.

## Verdict on the theory

| Claim | Verdict |
|---|---|
| RBs are more valuable than WRs at the top of this draft | **Not detectable** — +9.5 VOR in R1-2, p=0.50 |
| More early RBs → better finish (R2 / R4 / R6 / R8) | **Not supported** — right sign at all four cutoffs, none survives correction (best family-wise p=0.071) |
| Loading up on RBs through rounds 5-8 helps | **Contradicted** — no points edge, and RB busts 3× more often in R7-8 (p=0.051) |
| Three RBs by round 6 is the sweet spot | **Suggestive only** — 5 of 6 champions did it, N is far too small to bank |

**Draft-day posture:** at #4, take the best player — if that is an RB, take the RB, but take
him because he is the best player, not because the position pays a premium here (it does not,
measurably). Treat rounds 3-4 as position-agnostic best-available. From round 5 on, stop
force-feeding RB: same expected return as a WR, much fatter left tail.

**What would change this verdict:** the theory is not disproven, it is unmeasurable at N=60
manager-seasons. Adding 2024's standings, and each new season going forward, is the only way
to resolve it. Re-run `pipeline/rb_draft_timing.py` when they land.

