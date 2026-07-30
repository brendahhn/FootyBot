# Stress test — "Brendan Fantasy Draft Monte Carlo V1"

Status: adversarial review, 2026-07-30. Reviews two uploaded artifacts against this repo's
committed evidence:

- `Brendan_Fantasy_Monte_Carlo_V1.xlsx` + `..._Report.md` (the model under review)
- `Brendan_Fantasy_Operating_System_V11.xlsx` (the source workbook it was built from)

Ground truth used: `inputs/league-history/draft_history_master.csv` — 7 seasons (2019-2025) of
this league's **actual Yahoo draft boards**, 1,120 picks, 10 stable managers, already parsed and
committed. S-tier provenance. Every number below labelled "actual" is computed from that file.

---

## 1. Brendan's two questions, answered directly

> "lemme get this right u think first QB will be taken in the 50's?"

**No. The first QB has never been taken later than pick 41 in this league, in seven years.**

Actual first QB off the board, by season:

| Season | Pick | Round | Player | Taken by |
|---|---:|---:|---|---|
| 2019 | 22 | 3 | Patrick Mahomes | Jack |
| 2020 | 29 | 3 | Patrick Mahomes | Niko |
| 2021 | 30 | 3 | Patrick Mahomes | Nate |
| 2022 | 41 | 5 | Josh Allen | Nate |
| 2023 | 22 | 3 | Patrick Mahomes | Jack |
| 2024 | 32 | 4 | Jalen Hurts | Mattias |
| 2025 | 25 | 3 | Josh Allen | lucas |

**Median 29. Range 22-41. Round 3 in five of seven seasons.**

The model claims median **59**, with a 10th-90th percentile band of **53-64**. Its *10th
percentile* — the earliest it thinks a QB plausibly goes — is 12 picks later than the latest
first-QB ever recorded here. The model's entire distribution sits outside seven years of
observed reality. It assigns roughly 80% probability to an event that has happened 0 out of 7
times.

By pick 59, this league has historically already drafted **3 to 7 quarterbacks** (mean 4.7).

> "did u use my own rankings for how everyone else will be picking? if so this is not accurate"

**For 130 of 150 players, no. For all 20 quarterbacks, yes — and that is exactly what produced
pick 59.**

The `MODEL PARAMETERS` sheet states the rule in plain text:

> `QB room calibration | Room center cannot be earlier than Brendan pure rank + 3 | Calibrates first QB median to pick 59`

For non-QBs the room price is a genuine market blend (65% Fantasy Sanctuary rank + 35% median of
Underdog/Drafters/DraftKings), with no input from Brendan's board. I verified the arithmetic
reproduces the published `Room Center` to three decimals across the board.

For QBs, that market blend is computed and then **discarded** whenever it lands earlier than
Brendan's own board rank + 3. It binds on **17 of 20 QBs**:

| QB | Brendan board rank | Market blend says | Floor forces | Pushed later by |
|---|---:|---:|---:|---:|
| Josh Allen | 64 | **28.6** | **67.0** | **+38.5 picks** |
| Jordan Love | 131 | 113.1 | 134.0 | +20.9 |
| Lamar Jackson | 68 | 53.0 | 71.0 | +18.0 |
| Baker Mayfield | 132 | 116.2 | 135.0 | +18.8 |
| Patrick Mahomes | 106 | 94.1 | 109.0 | +14.9 |
| Tyler Shough | 129 | 118.9 | 132.0 | +13.1 |
| Dak Prescott | 85 | 78.4 | 88.0 | +9.6 |
| Caleb Williams | 75 | 69.3 | 78.0 | +8.7 |
| Drake Maye | 67 | 62.8 | 70.0 | +7.2 |
| Jayden Daniels | 69 | 65.7 | 72.0 | +6.3 |
| Jared Goff | 108 | 104.3 | 111.0 | +6.8 |
| Malik Willis | 130 | 127.3 | 133.0 | +5.7 |
| Joe Burrow | 66 | 64.7 | 69.0 | +4.4 |
| Trevor Lawrence | 83 | 82.5 | 86.0 | +3.5 |
| Jalen Hurts | 73 | 72.7 | 76.0 | +3.3 |
| Matthew Stafford | 107 | 100.6 | 110.0 | +9.4 |
| Kyler Murray | 109 | 109.8 | 112.0 | +2.2 |

The floor is asymmetric by construction — it can only ever push a QB **later**, never earlier.
And it bites hardest on precisely the elite QBs who determine when the first QB goes.

This matters because Brendan's board fades QBs harder than any other position relative to market:

| Position | Mean (board rank − market rank) | Biggest fade |
|---|---:|---|
| **QB** | **+5.9** | Josh Allen: board 64 vs market 29 |
| RB | +2.5 | Jadarian Price: 94 vs 64 |
| WR | −3.1 | Josh Downs: 113 vs 91 |
| TE | −3.1 | Travis Kelce: 148 vs 108 |

So: Brendan personally waits on QB (his own actual first-QB picks average 72.4 overall; he has
never taken one before pick 43), his board reflects that, and the model then imposed that
personal preference on all nine opponents as a hard price floor. The room was modelled as nine
copies of Brendan's QB habit.

**This also violates the source workbook's own Principle 1** — *"Separate pure rank, market price
and tactical click"* — and **Principle 2**, *"ADP is a price signal."* The one place the model
reached for pure rank to set a market price is the one place it broke.

---

## 2. What the corrected numbers are

I rebuilt the model's engine from its published parameters (center + per-position correlated
shock + per-player normal noise; availability = P(simulated draft position ≥ pick)). The
reconstruction reproduces the workbook's first-TE band **exactly** (13 / 18 / 22) and Josh
Allen's availability curve to within ~4pp, so it is faithful.

Then I removed the single bad parameter — the QB floor — and let QBs price off the same market
blend everyone else uses. Nothing else changed. No fitting to league history.

| | Model as shipped | **Floor removed** | League actual (7 yrs) |
|---|---:|---:|---:|
| First QB, 10th pct | 53 | **20** | 22 |
| First QB, **median** | **59** | **29** | **29** |
| First QB, 90th pct | 64 | **38** | 41 |

The corrected model is built from 2026 market prices and was never fitted to the league history,
so its agreement with the seven-year median is **an independent external consistency check, not
an out-of-sample validation** — the drafts span 2019-2025 and a different player pool, so this is
two independent estimators landing on the same value, not a train/test split. That is strong
evidence the market blend was sound and the floor was the only thing breaking it. It is *not*
evidence that any individual player's availability number is calibrated. (See §5, amendment A1.)

### The decision this actually inverts

Three related but **distinct** quantities, separated (see §5, amendment A3):

| Brendan's turn | Shipped: P(Allen avail) | **Corrected: P(no QB taken yet)** | **Corrected: P(Allen avail)** | **Actual: P(no QB taken yet)** |
|---|---:|---:|---:|---:|
| 2.07 (pick 17) | 100.0% | 94.9% | 94.9% | 100% (7/7) |
| 3.04 (pick 24) | 100.0% | **73.9%** | **73.9%** | **71% (5/7)** |
| 4.07 (pick 37) | 100.0% | **11.6%** | **11.6%** | **14% (1/7)** |
| 5.04 (pick 44) | 99.9% | **1.4%** | **1.4%** | **0% (0/7)** |
| 6.07 (pick 57) | 87.8% | **0.0%** | **0.0%** | **0% (0/7)** |

The two corrected columns are identical this year because Josh Allen's market price (28.6) sits
24 picks clear of the next QB (Lamar, 53.0), so the first QB taken is Allen in essentially every
simulation. They are still different quantities and must be tracked as separate fields — in a
year where QB1 and QB2 are close on price they will diverge sharply. Allen is also QB1 on *both*
Brendan's board (rank 64) and the market (rank 29), so the third possible definition collapses
into the same player as well. Convenient this year; not guaranteed.

The corrected simulation and seven years of actual drafts agree at every turn. The shipped model
disagrees with both.

**Practical consequence:** the model tells Brendan an elite QB is a near-certainty at pick 44 and
a coin-flip-plus at 57. In reality **pick 24 (3.04) is his last realistic shot at the QB1 of this
draft**, and by 4.07 he is drafting from whatever is left. If Brendan planned around the shipped
numbers he would pass at 24 believing he could not lose, and lose.

For the second QB tier the picture is less dire — under the corrected model Lamar is 90% at pick
44, Jayden Daniels / Burrow / Hurts are ~85-99% at pick 57. So *a* good QB is genuinely waitable.
*The* QB is not. That distinction is the entire decision, and the shipped model erases it.

---

## 3. Root cause — and it is upstream of the Monte Carlo

The Monte Carlo AI did not invent this. It faithfully implemented **Principle 41** from the
source Operating System workbook, marked **confidence: High**:

> **"The room historically lets QB slide** — The first QB usually appears around Round 7; Aaron
> and Lucas are the main early-QB threats."

And `NEW THREAD HANDOFF` repeats it as one of ~12 lines a fresh AI thread reads first:

> "Room historically attacks RB early; first QB usually appears around Round 7."

**The principle conflates a mean with a minimum.** Round ~7 is the average round at which *an
individual manager* takes *his own* first QB — which `research/draft-tendencies.md` Finding 1
confirms (league-wide average 7.0). But the first QB *off the board* is the **minimum across ten
managers**, not their average. With ten independent draws, the minimum lands far earlier than the
mean. Round 7 average → round 3 first QB.

This is a textbook min-vs-mean error, and it is sitting in the highest-authority document in the
stack, flagged High confidence, wired into the handoff protocol so it propagates to every new
thread. The Monte Carlo model is the first thing to have consumed it and turned it into a number.
It will not be the last unless the principle is fixed at source.

The same error repeats at manager level. "Aaron and Lucas are the main early-QB threats":

| Manager | Their own first QB, mean overall pick | Earliest ever | Times they took the draft's **first** QB |
|---|---:|---:|---:|
| Aaron | 45.9 | 30 | **0** |
| lucas | 47.9 | 25 | 1 |
| **Jack** | 58.3 | **22** | **2** |
| Niko | 58.9 | 26 | 1 |
| riley | 65.9 | 41 | 0 |
| **Mattias** | 67.6 | 29 | **1** |
| Brendan (us) | 72.4 | 43 | 0 |
| **Nate** | 78.6 | 30 | **2** |
| Connor | 79.0 | 44 | 0 |
| Dylan | 99.4 | 65 | 0 |

Aaron — the workbook's designated early-QB threat, and the man the Monte Carlo's
`MANAGER TENDENCIES` sheet flags as "Can take earlier" — has taken the draft's first QB **zero
times in seven years**. He is consistently early-*ish* and never first.

The actual QB1 snipers are **Jack** (picks 22 and 22; Mahomes twice) and **Nate** (2 of 7) — and
the Monte Carlo workbook labels Jack's QB timing **"Unknown"** and Nate's **"Waits."** Jack is
bimodal: 22, 107, 59, 67, 22, 99, 32. Averaging him produces 58.3 and hides the two years he took
the first QB in the room. **Five of the seven first-QBs came from managers the workbook classified
as late or unknown.**

Both errors are the same error: ranking managers by mean when the quantity that matters is a
minimum.

---

## 4. Findings ledger

### Critical

**C1 — First-QB estimate is a hard-coded assumption, not a simulation output.** Covered above.
The `Rationale` field says the parameter exists to "calibrate first QB median to pick 59." The
model cannot produce a QB before ~pick 50 regardless of evidence, which makes the finding
unfalsifiable — no amount of contrary market data can move it.

**C2 — The validation is circular.** `MODEL PARAMETERS` sets the floor *in order to* produce 59.
`VALIDATION` then reports: `First QB median | 59 | Pass with caveat | aligns with room history
around Round 7.` The output is validated against the assumption that generated it, and the
"room history" it is checked against is the Principle 41 error. Assumption → output → the output
confirms the assumption. Three failures stacked, and the sheet reads "Pass."

**C3 — Sensitivity analysis omits the one parameter doing the work.** The workbook tests seed
(<1pp), volatility ±20% (7-11pp), and direct intel on/off (8-9pp). It never tests the QB floor.
Removing it moves the headline number by **30 picks** — an order of magnitude beyond anything
reported. Sensitivity was run over the parameters the author was confident in, and not over the
assumption carrying the result.

**C4 — Precision is being reported as accuracy.** "100,000 simulations, deterministic seed
20260730, max cross-seed difference 0.99pp" measures Monte Carlo sampling error. It says nothing
about whether the center is right. 100,000 draws around a wrong mean give a very tight wrong
answer. The report leads with the simulation count; that number should not be in the headline.

### High

**H1 — The model declares its most valuable input missing when it is committed in this repo.**
`MANAGER TENDENCIES`: *"Remaining tendencies await historical draft logs."* `VALIDATION`: *"Full
seat-by-seat drafting agents require historical draft logs."* Those logs exist:
`inputs/league-history/draft_history_master.csv`, 1,120 picks, 7 seasons, joined to the 10 stable
managers, validated to 0 unmapped picks and exactly 16 picks/manager/year, plus
`draft_history_enriched.csv` with per-pick archetype flags. Everything the model called
"provisional pending data" is computable today. This is the single highest-leverage fix.

**H2 — Qualitative manager labels are falsified by that data.** Beyond the QB timing errors in
§3: the sheet lists Connor's RB bias as "Moderate" (actual: 18 RB / 14 WR in rounds 1-5, the
strongest RB lean in the league) and his risk appetite as "Moderate" (actual: aging veterans at
29% of his early picks, 2× league average — the most distinctive single trait any manager has).
The seat descriptions were carried over verbatim from the source workbook without being checked
against the history.

**H3 — Draft order: two contradictory orders, both attributed to Brendan.**

| Seat | Operating System V11 (`LEAGUE + ROOM`) | `research/mock-draft-2026.md` (given 2026-07-02) |
|---:|---|---|
| 1 | Connor | Lucas |
| 2 | Dylan | Nate |
| 3 | Lucas | Dylan |
| 4 | **Brendan** | **Brendan** |
| 5 | Riley | Connor |
| 6 | Jack | Niko |
| 7 | Mattias | Riley |
| 8 | Niko | Jack |
| 9 | Aaron | Mattias |
| 10 | Nate | Aaron |

Only Brendan's seat agrees. This does not change V1's math (V1 is a price model, seat-agnostic),
but it will drive **everything** in a seat-by-seat V2 — Jack and Mattias are the two seats
carrying direct intel, and they sit at 6/7 in one version and 8/9 in the other, which changes how
many times each picks inside Brendan's 1.04→2.07 window. **Brendan needs to confirm which is
live before any V2 work starts.** Yahoo also commonly randomizes order shortly before the draft,
so this may not be knowable yet — in which case V2 should marginalize over draft order rather
than assume one.

**H4 — The 150-player board contains zero defensive players, in a league with a mandatory
starting defensive slot.** *Scope note: this is a late-round and roster-legality defect. It does
not contribute to the early-round QB failure — the history shows ~0 non-offensive picks before
pick 104 (see M1), so picks 4-57 are unaffected. It is a V2 blocker for roster completion,
replacement-level values and season simulation, not a cause of the headline error.* Board
composition is WR 61 / RB 51 / QB 20 / TE 18 = 150, no IDP, no DST, no K. But this league starts one defender every week, and `CONTEXT.md` records it as
confirmed from league screenshots to be a **real 1-IDP flex slot, not a team defense** — while
Operating System V11's `LEAGUE + ROOM` sheet lists it as `DST`. Two consequences: (a) the model
has no way to plan a mandatory roster slot, and this repo already holds the relevant research
(`research/idp-evaluation.md`, plus the pipeline-verified finding that solo tackle rate predicts
at r=0.506); (b) the source workbook and this repo disagree on what the slot even is, and the
repo's version is screenshot-confirmed.

### Medium

**M1 — "Round 16 is not covered" is false, and the recommended fix is the wrong fix.** Both the
report (finding 8) and `DATA QUALITY` state that pick 157 sits outside a Top-150 board, with the
recommended fix "extend the player pool to 220-250." But picks are not all spent on the offensive
board. Actual mean count of offensive players gone by each of Brendan's late turns:

| Brendan's pick | 104 | 117 | 124 | 137 | 144 | **157** |
|---|---:|---:|---:|---:|---:|---:|
| Offensive players actually gone | 102.6 | 114.9 | 120.4 | 130.3 | 134.7 | **142.1** |
| Non-offensive picks absorbed | 0.4 | 1.1 | 2.6 | 5.7 | 8.3 | **13.9** |

By pick 157 only ~142 offensive players are off the board. **A 150-player offensive board already
covers pick 157 with room to spare** — it reaches roughly pick 165 in real terms. The actual
defect is that the model assumes all 156 prior picks come from its 150-man offensive pool, which
systematically **understates** late-round availability by up to ~14 picks of board depth. The fix
is to model the ~9-14 non-offensive picks (declining trend: 15, 17, 13, 10, 9, 11, 6 across
2019-2025), not to add 100 more offensive players.

**M2 — TE is mis-calibrated in the same direction, without the floor to blame.** Model: median
18, band 13-22. Actual: **median 14, range 8-30** (Kelce six straight years, Bowers in 2025). The
model is ~4 picks late, and its nominal 80% band covers only **4 of 7** seasons — it misses low
in 2021 (9) and 2023 (8) and misses high in 2024 (30). So the band is simultaneously biased late
*and* too narrow. Since no floor applies to TEs, this points at a second, independent problem:
the volatility formula understates genuine year-to-year room variance. Worth checking whether the
same under-dispersion affects the RB/WR numbers that Brendan is actually going to act on.

**M3 — The headline 1.04 table is an arithmetic identity presented as a simulation result.**
Puka 42.9% / Bijan 25.6% / Gibbs 20.0% / Chase 11.6% sums to 100%. It has to. Brendan's board top
4 is Gibbs, Bijan, Puka, Chase; three players are taken ahead of pick 4; therefore at least one
of the top 4 always survives, and best-available is always one of those four names — in every
simulation, under every parameter setting, with probability exactly 1. No simulation was needed
to learn that. Only the *split* among the four is informative, and that split is a pure
restatement of the four market ranks. The report's hedge ("this is not a ranking recommendation")
does not flag that the 100% is structurally forced.

**M4 — No substitution or satiation.** Position shocks (`RB 1.5, WR 1.5, TE 2.0, QB 4.0`) create
correlated runs, but demand is never *satisfied*. In a real draft, once the room's RB-hungry
managers have their backs, RB demand collapses and the next RB falls further than any static
model predicts. This league runs RB hard and early (9 of 10 managers lean RB in round 1 per
`research/draft-tendencies.md`), so satiation is a first-order effect here, not a refinement. All
tier-survival numbers inherit the omission.

**M5 — "Returns next turn" conditions on a single static draw.** Each player gets one simulated
draft position; `P(returns) = P(pos ≥ next pick | pos ≥ current pick)`. This treats a player
surviving to 2.07 as carrying no information about the room's behaviour in *this* draft, when in
reality an unexpected fall is informative. **The defect is the missing belief update; the
direction of the resulting bias is not universal** — a fall can mean a room-wide fade (raises
future survival), a transient positional run that is about to reverse (lowers it), or earlier
roster construction shifting later demand (either way), or nothing at all. My earlier claim that
return probabilities are "biased low" overstated this: the sign is player- and mechanism-specific
and should be measured against the seven committed drafts, not asserted. What is safe to say is
that the "now or never" labels are computed from a model that cannot condition on board state,
so their error bars are wider than presented. (See §5, amendment A4.)

**M6 — Principle 42 is the live strategic risk, and it is downstream of Principle 41.**
*"Do not force an early QB — take an elite QB only after a material fall; otherwise exploit the
late-QB pool."* If the first QB actually goes at 29, there is no material fall to wait for and no
late-QB pool at the elite tier. Principle 42 is sound reasoning built on a false premise, and it
is the premise that needs fixing, not the reasoning.

**M7 — Unexamined tension with this league's own scoring.** Principle 40 correctly notes 6-point
passing TDs raise pocket passers. `research/positional-value.md` (pipeline-computed from real
2025 weekly data under this league's exact formula) puts **QB1 at 26.0 PPG vs RB1 21.5 and WR1
19.4** — QB is the highest-scoring position in this league by a wide margin, and QB12 (21.1)
roughly equals RB1. Raw PPG is not value-over-replacement, so this does not by itself argue for
an early QB. But it does mean the direction of the scoring rules pushes QBs *earlier*, while the
model's only QB-specific mechanism pushes them *later*. Nobody reconciled the two. A proper VOR
pass against the league formula is the missing analysis.

### What the model got right — this should be kept

Credit where it is due, because most of this workbook is good and the fix is narrow:

- **The data-quality section is honest and numerically accurate.** I verified the two checkable
  claims independently: pure-rank vs ledger-evidence correlation computes to **−0.647** (reported
  −0.65) and the movement-confidence census is exactly **130 Unrated / 10 High / 9 Medium / 1
  Low** (reported 130 unrated). Flagging its own evidence base as attention-biased is genuinely
  good practice.
- **Refusing to output championship equity is the correct call**, and the closing framing —
  "Player X is the more urgent click because his return probability is materially lower" versus
  "+0.8pp championship probability" — is exactly the right register for what this model can
  support.
- **The non-QB price blend is transparent and reproducible.** I re-derived `Room Center` from the
  published weights across all 150 players and reproduced the first-TE band exactly. A model that
  a reviewer can rebuild from its own parameter sheet is a well-documented model, and that is
  precisely why this error was findable.
- **Excluding FFPC from the Yahoo-compatible center is right** given the TE format mismatch.
- The click-window framing (available / returns / tier-returns) is the right decision object.

The problem is not the architecture. It is one parameter, and one upstream principle.

---

## 5. Amendments after author response (2026-07-30)

The V1 author accepted the core findings and raised five objections. **All five are legitimate.**
Three are conceded outright, one corrects a real analytical sloppiness on my part, and one is
conceded *and* tested. None change the headline conclusion — and rather than assert that, I
tested the two objections that are testable.

**A1 — "Out of sample" was too strong. Conceded.** Corrected in §2. The right description is an
independent external consistency check: 2026 market prices and 2019-2025 draft history are two
independent estimators that agree on ~29. It is not a train/test split and does not certify
individual player calibration.

**A2 — Seven seasons is a small sample; manager tendencies need shrinkage. Conceded, and
tested.** The objection is correct and I under-weighted it. Two tests:

*(i) What does n=7 actually support?* Fitting a posterior predictive to the seven observed
first-QB picks (flat prior, full parameter uncertainty — not the naive normal):

| | Next-season first QB |
|---|---|
| Median | 29 |
| 80% band | 18-39 |
| 95% band | **11-46** |
| P(later than pick 50) | **1.2%** |
| P(later than pick 53) | **0.7%** |

So the honest small-sample answer is a *wide* band — but its 95% upper bound (pick 46) still
sits below the shipped model's 10th percentile (53). The model asserted a median of 59, i.e. it
put >50% on an event the history supports at ~1%. Proper humility about n=7 widens the interval
substantially and does not rescue the model.

*(ii) Does the min-vs-mean finding survive full shrinkage?* I re-ran it with **zero
manager-specific information** — pooling all 70 manager-seasons and treating all ten managers as
identical draws:

| | Value |
|---|---|
| Pooled per-manager first-QB pick | mean **67.4**, median **62** |
| Minimum of 10 identical managers | median **26**, 10-90 band **22-41** |
| Actually observed first QB | median **29**, range **22-41** |

The simulated band reproduces the observed range essentially exactly, using no per-manager
estimates whatsoever. **The min-vs-mean conclusion requires no manager-level inference at all**,
so it is immune to the shrinkage objection. It also shows the error's fingerprint directly: the
per-manager mean is ~62-67 (Round 7 — precisely where Principle 41 came from, now confirmed
numerically) while the draft minimum is ~26. **A 36-to-41-pick gap between the mean and the
minimum.** The model's answer of 59 sits close to the per-manager mean, not the minimum, which is
the signature of exactly this confusion.

The author's constructive point stands for V2: agents should blend own-history, league-wide
priors, current ADP, player-specific evidence and recency weighting — not memorise seven drafts.
Jack's two first-QB grabs at pick 22 are real signal, but 2 of 7 carries a very wide interval and
should be shrunk toward the league prior.

**A3 — "First QB available" conflated distinct quantities. Conceded; this was a real error on my
part.** My original table compared P(Josh Allen available) against P(no QB taken yet) as though
they were one thing. They are three separate fields — P(no QB selected yet), P(market QB1
available), P(board QB1 available) — and §2 now reports them separately. Computed properly, the
first two are identical this year (94.9 / 73.9 / 11.6 / 1.4% at picks 17/24/37/44) because Allen
is 24 picks clear of QB2 on market price, and the third collapses too because Allen is QB1 on
both boards. So the conclusion is unaffected — but the objection is methodologically correct and
the fields must stay separate, because in a year with a tight QB1/QB2 they will diverge.

**A4 — M5's bias direction is not universally guaranteed. Conceded.** Corrected in M5. The
missing belief update is a genuine defect; the sign of its effect is mechanism-dependent and
should be measured, not declared.

**A5 — IDP matters later, not for picks 4-57. Conceded.** Correct, and my own M1 data supports
it (~0 non-offensive picks before pick 104). H4 is now explicitly scoped as a late-round and
roster-legality blocker, not a contributor to the QB failure. My severity label was fine; the
framing invited the wrong inference.

### Sharpened practical QB guidance

The author's summary — "QB1 gone by 3.04, QB2-QB6 waitable into 44-57" — is directionally right
but needs splitting. Corrected-model availability at Brendan's turns:

| QB | 2.07 (17) | 3.04 (24) | 4.07 (37) | 5.04 (44) | 6.07 (57) | 7.04 (64) |
|---|---:|---:|---:|---:|---:|---:|
| **Josh Allen** | 94.9% | **73.9%** | 11.6% | 1.4% | 0.0% | 0.0% |
| **Lamar Jackson** | 100% | 100% | 98.9% | **90.1%** | **27.9%** | 5.5% |
| Drake Maye | 100% | 100% | 100% | 99.7% | **80.6%** | 43.1% |
| Joe Burrow | 100% | 100% | 100% | 99.8% | **85.2%** | 53.4% |
| Jayden Daniels | 100% | 100% | 100% | 99.9% | **89.2%** | 59.7% |
| Jalen Hurts | 100% | 100% | 100% | 100% | 98.7% | 89.2% |
| Justin Herbert | 100% | 100% | 100% | 100% | 99.9% | 98.6% |

Three distinct decision windows, not two:

1. **Allen — 3.04 or never.** 74% at pick 24, 12% at 37. There is no second chance.
2. **Lamar — 5.04 is the cliff, not 6.07.** 90% at pick 44 but **28%** at 57. Lumping him into a
   "waitable to 57" tier is the same mistake one tier down.
3. **Maye / Burrow / Daniels — genuinely available at 6.07** (81-89%), coin-flip at 7.04.
   Hurts and Herbert are comfortable even at 7.04. This is where "exploit the late-QB pool" is
   actually true.

The author's final framing is right and worth preserving verbatim: Brendan's personal QB fade
should govern *whether he wants Allen at pick 24* — it should never have governed *whether the
other nine managers let Allen reach pick 57*. These caveats sharpen the numbers; they do not
soften the conclusion that the shipped headline was backwards.

---

## 6. Fix list, in priority order

1. **Delete the QB floor.** Price QBs off the same market blend as every other position. This one
   change moves the first-QB median from 59 to 29 and brings the model into agreement with seven
   years of actual drafts at every one of Brendan's turns.
2. **Rewrite Principle 41 in the source workbook** — it is the root cause and it is set to
   propagate. Suggested replacement, computed from the league's own boards:
   > *The first QB off the board goes in round 3 (median pick 29, range 22-41, round 3 in 5 of 7
   > seasons). Individual managers average round 7 for their own first QB — do not confuse the
   > two. The QB1 snipers are Jack (2 of 7, both at pick 22) and Nate (2 of 7); Aaron and lucas
   > are consistently early but have taken the draft's first QB once between them in seven years.
   > Dylan is the only reliable punter — never before pick 65.*
   Update `NEW THREAD HANDOFF` to match, or the old claim keeps propagating to every new thread.
3. **Re-examine Principle 42** once 41 is fixed. "Exploit the late-QB pool" is still defensible
   for the QB3-QB8 tier (Daniels/Burrow/Hurts are 85-99% at pick 57 under the corrected model);
   it is not defensible for QB1. Split the principle in two.
4. **Feed the model the draft history it says it lacks.** `draft_history_master.csv` +
   `draft_history_enriched.csv` support real per-seat agents: positional propensity by round,
   first-QB hazard, archetype preference, reach/value tendency. Replace the qualitative
   `MANAGER TENDENCIES` sheet with fitted numbers. Model each seat's first-QB pick as a
   distribution and take the minimum — never the mean.
5. **Reconcile the draft order** (H3) and **the D-slot definition** (H4 — the repo's
   screenshot-confirmed IDP reading should win over V11's `DST`) before V2.
6. **Add the ~9-14 non-offensive picks** to the pick-consumption model instead of extending the
   board to 220-250. Then re-derive late-round availability; pick 157 is already coverable.
7. **Re-run sensitivity over the assumptions, not just the parameters.** Every hand-set rule
   should get the treatment volatility got — including any replacement for the QB rule.
8. **Widen the volatility formula** or re-fit it so nominal 80% bands actually cover ~80% of
   observed seasons. Backtest against the 7 committed drafts: for each season, check whether the
   actual first-QB / first-TE / positional-run picks land inside the predicted band. That
   backtest is now cheap and is the validation this model never had.

---

## 7. The transferable lesson

The failure mode here is not bad math — the math is clean and reproducible. It is that a
**hand-set assumption was tuned to produce a target output, and then the output was cited as
evidence the assumption was sound**, while the sensitivity analysis swept every parameter except
that one. The workbook's own rationale field says out loud that the parameter exists to hit pick
59; nothing downstream treated that as a warning.

Two guardrails would have caught it, and should be standing rules for anything built on this
stack:

- **Any parameter whose stated rationale is "calibrates output X to value Y" is an assumption,
  not a finding.** It must be excluded from the results section and included in the sensitivity
  sweep.
- **Before shipping a probability about this league, check it against
  `inputs/league-history/`.** Seven years of the room's actual behaviour is sitting in the repo.
  A one-line check against it would have flagged "median 59" in seconds — the observed range is
  22-41 and the model's own 10th percentile was outside it.

And the specific statistical trap, worth naming because it appears twice in the same document:
**when the decision depends on the earliest anyone acts, the average of what everyone does is the
wrong statistic.** Ten managers averaging round 7 produce a first QB in round 3. That gap — four
rounds — is the entire error.
