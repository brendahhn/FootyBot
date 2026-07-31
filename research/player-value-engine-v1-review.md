# Stress test — "Brendan Player Value Engine V1"

Status: adversarial review, 2026-07-30. Reviews `Brendan_Player_Value_Engine_V11.xlsx` (25
sheets), the VOR/projection board built in response to finding N6 of
`research/monte-carlo-v1-review.md` ("availability is solved, value is not").

Ground truth: `inputs/league-history/` (7 seasons, 1,120 actual picks),
`inputs/nflverse/stats_player_week_2025.csv`, and `research/positional-value.md`.

---

## Verdict

This is a real step up. It answers the question it was built to answer, the core engine is
**exactly reproducible from its own published parameters**, and it carries the V1 fix forward
correctly. It is the best artifact in this stack.

It also has a single point of failure that its own sensitivity analysis does not touch, and that
failure sits on exactly the decision the engine was commissioned to resolve. **Josh Allen's true
rank moves from #24 to #50 on one hand-entered number**, which flips him from "worth pick 24" to
"let him go." That is not a reason to distrust the engine. It is a reason to nail down one input
before August 28.

---

## 1. What it gets right — verified, not taken on trust

**The V1 bug is genuinely fixed and correctly propagated.** The Market Board prices Josh Allen at
room center **28.5**, median pick **28** — the market blend, not the old `Brendan pure rank + 3`
floor of 67.0. Availability at pick 24 reads **73.6%**, against my corrected model's 73.9% and
the league's actual 71% (5 of 7 seasons). Three independent estimates within 3 points. The fix
took.

**The True Value formula reproduces exactly.** I recomputed it from the published weights
(`median_vor 0.52, p80_vor 0.19, p20_vor 0.10, top6 12, top12 7, scarcity 0.10, spike 6,
fragility −0.16, confidence 0.03`) against the `Value Components` sheet:

> **Maximum absolute error: 0.000000 across all 150 players.**

Every score is a documented weighted sum of published components. After V1 — where the headline
number came from an undisclosed floor buried in a parameter sheet — this is the single most
important improvement in the workbook. It is why everything below was findable.

**It answers N6 directly.** Allen at true rank 24 against market rank 29 = "Fair price." The
availability answer (pick 24 is the last realistic shot) and the value answer (he's worth roughly
pick 24) now agree. That was the open question and it is closed, conditional on §2.

**The honesty holds up.** `Validation` self-reports the 0.913 Spearman correlation with Brendan's
inherited board rather than burying it, and uses `PARTIAL` / `PASS WITH CAVEAT` / `PASS
DIRECTIONALLY` where warranted. `Remaining Data Gaps` lists the IDP board (#6) and unresolved
draft order (#7) — both carried over correctly from the prior review. Approval status is
"Directionally useful with explicit caveats," not "ready."

**Distributions instead of point estimates.** P20/P80, Top-6%, Top-12%, spike/killing week rates,
explicit injury and role-loss branches with probabilities summing to 1.0. This is the right shape
for a draft-decision object.

---

## 2. The headline finding: the QB board is a readout of 21 hand-entered numbers

`Model Configuration` contains 21 `qb_pass_td_assumptions` entries. They are the only QB-specific
inputs, they are hand-set, and at 6 points per passing TD they dominate every QB projection.

Checked against real 2025 data (`stats_player_week_2025.csv`, REG only, projected to a 17-game
pace so injury-shortened seasons are compared fairly):

| QB | Assumed 2026 | 2025 per-17 pace | 2025 games | Delta |
|---|---:|---:|---:|---:|
| Jayden Daniels | 27 | 19.4 | 7 | **+7.6** |
| **Josh Allen** | **34** | **26.6** | **16** | **+7.4** |
| Kyler Murray | 25 | 20.4 | 5 | +4.6 |
| Patrick Mahomes | 31 | 26.7 | 14 | +4.3 |
| Baker Mayfield | 30 | 26.0 | 17 | +4.0 |
| Lamar Jackson | 29 | 27.5 | 13 | +1.5 |
| Joe Burrow | 36 | 36.1 | 8 | −0.1 |
| Jared Goff | 30 | 34.0 | 17 | −4.0 |
| Matthew Stafford | 33 | 46.0 | 17 | **−13.0** |

**15 of 17 QBs are projected at or above their 2025 pace**; mean delta +1.7 TD, median +2.9 TD.
That is a mild systematic upward tilt — roughly +10 to +17 points per season on the average QB —
and because it is systematic it lifts *all* QB VOR relative to RB/WR.

Individually these are defensible. Allen has thrown 40+ before and 2025 (25 TD in 16 games) was a
down year, so regressing up is reasonable. Stafford's 46 was league-leading and regressing him to
33 is correct. **The problem is not the numbers. It is that they are load-bearing, unverifiable
from this repo, and absent from the sensitivity sweep.**

### How load-bearing

Re-scoring the board with QB pass-TD assumptions set to each QB's 2025 per-17 pace:

| QB | Engine rank | At 2025 pace | Swing |
|---|---:|---:|---:|
| **Josh Allen** | **24** | **50** | **−26** |
| Jayden Daniels | 71 | 143 | −72 |
| Lamar Jackson | 52 | 68 | −16 |
| Drake Maye | 50 | 55 | −5 |
| Joe Burrow | 42 | 41 | +1 |
| Matthew Stafford | 103 | 24 | **+79** |

Regressing **Allen alone** — changing one cell from 34 to 26.6 — moves him from **#24 to #50**.
Stacking the replacement-level correction from §3 on top puts him at **#45**.

*(These estimates are conservative. I applied the shift only to the three VOR terms — 0.81 of the
weight. A −44 point move would also reduce Allen's Top-6%, Top-12% and spike probabilities, which
carry another 25 points of weight. The true fall is somewhat larger than #50.)*

### Why this matters, and the exact parallel to V1

| Allen's true rank | Market rank | Verdict | Action at 3.04 |
|---|---|---|---|
| **#24** | 29 | Fair price | Defensible click |
| **#50** | 29 | Below market — market trap | **Let him go** |

The engine's entire answer to "is Allen worth pick 24" rests on whether he throws 34 TDs or 27.

And `sensitivity_modes` is `["ceiling_heavy", "floor_heavy", "tighter_replacement",
"low_injury_penalty", "no_evidence_adj"]` — **none of which perturb the pass-TD assumptions.**

This is structurally the same failure as V1's QB floor: a hand-set, QB-specific input, excluded
from the sensitivity sweep, determining the headline. The mechanism is entirely different and far
more defensible — a projection assumption is a legitimate modeling choice in a way that a
rank-based price floor never was. But the lesson from the last review applies unchanged: **the
parameter you didn't sweep is the one carrying the answer.** A sixth sensitivity mode —
`pass_td_regression` — closes it.

---

## 3. Replacement levels: a real error that does not change the QB answer

`Replacement Levels` sets QB12, RB36, WR45, TE12 for a 10-team league starting 1 QB / 2 RB /
2 WR / 1 TE / 2 FLEX. Measured as depth past the last starter:

| Pos | Starters | Baseline | Flex depth implied |
|---|---:|---:|---:|
| QB | 10 | 12 | 2 |
| TE | 10 | 12 | 2 |
| RB | 20 | 36 | **16** |
| WR | 20 | 45 | **25** |
| | | | **Total 45** |

**The league has 20 flex slots. These baselines imply 45.** The stated rationale for RB36 is "Two
RB plus two flex demand," which cannot produce 36 when WR45 has already consumed 25 of the 20
available flex slots. The numbers contradict their own justification.

**But it does not move the QB conclusion.** I re-scored the whole board under three conventions:

| Convention | Baselines | Allen's true rank |
|---|---|---:|
| A — engine as shipped | QB12 / RB36 / WR45 / TE12 | **24** |
| B — starter demand, 20 flex correctly allocated | QB11 / RB29 / WR32 / TE12 | **24** |
| C — empirical, this room's actual rostering | QB18 / RB57 / WR63 / TE15 | 32 |

Under the corrected starter-demand baselines, **Allen stays at #24**. The flex over-allocation
inflates RB, WR and QB VOR in roughly proportional amounts and largely cancels. Convention C is
derived from this league's own drafts (last 3 years: 17 QB, 56 RB, 62 WR, 14 TE rostered per
season, so replacement ≈ drafted + 1) but is arguably the wrong definition — RB57 projects 82
points and is a bench flier you would never start. Starter demand is the defensible standard, and
under it nothing moves.

**So: fix it for correctness, but it is not a decision bug for QB.**

### Where it *is* a decision bug: RB vs WR at 1.04

| Convention | WRs in top 10 | Nacua | Chase | JSN | Jeanty | Taylor |
|---|---:|---:|---:|---:|---:|---:|
| A — engine | 3 | **3** | **6** | 8 | 10 | 4 |
| B — starter demand | 3 | 3 | 5 | 8 | 10 | 4 |
| C — empirical | **1** | **9** | **12** | 16 | 7 | 3 |

Between the engine's convention and this room's actual rostering behaviour, Puka Nacua moves
from **#3 to #9** and Ja'Marr Chase from **#6 to #12**, while the RBs rise. That is a complete
inversion of Brendan's most important pick — and 1.04 is precisely the RB-vs-WR call the whole
project exists to get right.

The two defensible conventions (A and B) agree, so the engine's answer is probably fine. But the
workbook never states which convention it uses, never justifies it, and its
`tighter_replacement` sensitivity mode never reports that the RB/WR ordering at the top of the
board is the thing that moves. **The replacement convention is the most load-bearing unstated
choice in the engine after the pass-TD slate.**

---

## 4. The WR replacement baseline is a torn-ACL player

`Replacement Levels` names **Malik Nabers** as the WR45 baseline at 157.3 points. The same
workbook lists Nabers on `Below Market` at true rank **114**, classified **"Market trap /
Scenario Riser / Avoid at Cost,"** citing Reuters (2026-07-30): *"no target date to return."*

The engine is using a player it flags as uniquely broken to define what a normal replacement WR
looks like. His median is already injury-depressed, which lowers the WR baseline and mechanically
inflates every WR's VOR.

The numeric damage is small — the local gradient is gentle (WR41 through WR49 spans only 13
points, 165.6 → 152.5), so the baseline would barely move if he were excluded. But a replacement
level should be a **role**, not a named player, and never a named player the model has separately
declared an outlier. Take the median of WR42-48, or exclude players carrying an explicit
injury-scenario flag from baseline calculation.

---

## 5. The projection dependency is now the biggest unverifiable in the stack

Across three reviews, every claim I have checked has been checkable against committed repo data.
**The Draft Sharks projections are not.** They are the foundation of the entire True Value board
and I cannot audit them from here.

Two things follow.

**First, a project-constraint question for Brendan.** `CONTEXT.md` records a decision from
2026-06-30: *"free public sources only — no paid data subscriptions (FantasyPros, PFF, etc.)."*
The engine's A-tier projection prior is Draft Sharks, a paid product, and FantasyPros ECR appears
as market cross-check. That may be a fine trade — projections are genuinely hard to build from
free sources and the engine uses them honestly — but it reverses a documented project decision
and should be Brendan's explicit call, recorded as an ADR, not adopted silently.

**Second, what I could check, checks out.** Allen's median of 456.8 points over 17 games is
26.9 PPG, against `research/positional-value.md`'s pipeline-computed 2025 QB1 (Stafford, 26.0
PPG) under this league's exact scoring formula. The 6-point passing TD adjustment is applied and
the scale is right. The projections are not obviously wrong — they are simply outside my ability
to verify, which is a different and more uncomfortable status than anything else in this stack.

---

## 6. Smaller findings

**6.1 — The 0.913 correlation with Brendan's board deserves a sharper test than it gets.**
`Validation` reports Spearman 0.913 between True Value rank and the inherited board and calls it
`PASS WITH EXPECTED CORRELATION`. That is the right call — common football reasoning genuinely
produces correlation, and the alternative (a board uncorrelated with informed opinion) would be
worse. But "independent" is being asserted rather than demonstrated. The value of an independent
board lives entirely in its **disagreements** — the ~25 names each on `Above Market` and `Below
Market`. Those are the rows that should carry the heaviest sensitivity treatment, and currently
they carry the same treatment as everything else.

**6.2 — The `-0.716` commentary-bias correlation is largely mechanical.** `Validation` reports
Spearman −0.716 between evidence-row count and True Value. Given the prior review established
r = −0.647 between Brendan's board rank and ledger evidence count, and True Value correlates
0.913 with that board, a correlation near −0.65 is arithmetically forced. It is not independent
evidence that attention bias was avoided. Not a defect — the diagnostic just proves less than it
appears to.

**6.3 — The QB run-rate finding (N2 of the prior review) is still open.** The Market Board prices
QBs off the market blend alone: Lamar median pick 52, Maye 62, Daniels 65. This league's recent
three drafts had **5.67 QBs gone by pick 57** (up from 2.50 in 2019-22). The engine has no
mechanism to see that acceleration, so its mid-round QB availability remains optimistic. Carried
forward unfixed.

**6.4 — The click board's answer at 3.04 is good and worth reading closely.** At pick 24 it ranks
Allen **7th** (73.6% available, urgency 0.797) behind Henry, Achane, Nico Collins, Bowers,
McBride and Jeremiyah Love. That is a defensible, nuanced output: Allen is worth taking, and
there are six things worth taking more. Combined with the fact that Allen returns at ~0% by pick
44, the urgency term is doing real work. This is the engine at its best.

---

## 7. Fix list

1. **Add a `pass_td_regression` sensitivity mode.** Sweep the 21 QB assumptions toward a
   multi-year pace baseline and report the resulting rank band for every QB. Publish Allen as a
   range (#24-#50), not a point. This is the one item that changes a draft-day decision.
2. **Justify Allen at 34 TDs explicitly**, against his multi-year pace rather than 2025 alone,
   with the Bills' 2026 personnel and pace as stated evidence. If it survives, the #24 stands and
   is much stronger for having been challenged.
3. **Fix the replacement ranks** to allocate exactly 20 flex slots (≈ QB11 / RB29 / WR32 / TE12),
   and state the convention and its rationale on the sheet.
4. **Report the RB/WR sensitivity at the top of the board**, not just per-player rank stability —
   that is where the replacement convention actually bites, and it is the 1.04 decision.
5. **Define replacement as a role, not a player.** Median of WR42-48; exclude players carrying an
   explicit injury-scenario flag.
6. **Record the paid-source decision as an ADR** (`docs/adr/`), reversing or amending the
   2026-06-30 free-sources-only decision in `CONTEXT.md`.
7. **Stress the disagreements hardest.** Above/Below Market rows are the engine's entire claim to
   independence; they should carry a heavier sensitivity and evidence burden than consensus rows.
8. **Carry the QB run-rate correction into the Market Board** (prior review, N2) — recency-weight
   the room's accelerating QB demand rather than pricing off market blend alone.

---

## 8. The pattern across three artifacts

V1's headline was wrong because of an undisclosed hand-set QB parameter that the sensitivity
analysis did not sweep. The Player Value Engine is a much better piece of work — reproducible to
six decimal places, honest about its gaps, and correct on the thing it was built to fix. Its
headline is now uncertain because of **a disclosed hand-set QB parameter that the sensitivity
analysis does not sweep.**

The disclosure is the improvement, and it is a large one — this finding took an afternoon rather
than being undiscoverable. But the standing rule from the last review has not yet been absorbed:

> **Any hand-set input that materially moves the headline must be in the sensitivity sweep, and
> its range must be reported alongside the point estimate.**

Applied here, that means one thing before August 28: **Josh Allen is a #24-to-#50 player until
someone defends 34 passing touchdowns.** Everything else in this workbook is in good shape.
