# Hostile peer review — the "fresh 2026 board" (rival AI) vs FootyBot's pipeline data

**Scoring:** 10-team, 0.5 PPR, 6pt pass TD, −2 turnovers, +2 for 40+ yd run/rec. Brendan drafts 4th.
**Verdict in one line:** *The rival quoted my predictive study (PPG r=0.818, TD-rate r=0.008) and then
didn't follow it.* It ranked players off Brendan's own optimistic **full-PPR projections** — the exact
tier-C numbers my board flags as "replace these" — while claiming to anchor on demonstrated PPG. I have
the demonstrated PPG. Below, every disputed call is settled against `research/positional-value.md`,
`predictive-stats.md`, and `draft-tendencies.md` — all pipeline-computed [S] from real nflverse weekly
data under this league's exact formula.

Anchor table — **2025 PPG, this league's scoring [S]** (the strongest forward signal we have, r=0.818):

CMC 21.51 · **JT 19.96** · Bijan 19.49 · Puka 19.41 · Gibbs 19.32 · Achane 18.08 · JSN 17.67 ·
Cook 16.81 · **Henry 16.00** · Chase 15.69 · ARSB 15.62 · Rice 15.45(8g) · McBride 14.88 ·
Jacobs 14.61 · Chase Brown 14.59 · Pickens 14.44 · **Kyren 14.43** · Javonte 14.08 · London 13.99(12g) ·
Saquon 13.36 · Nico 12.71(15g) · CeeDee 12.57(13g) · Higgins 12.14 · AJB 12.09(15g) · Bowers 12.02(12g) ·
Breece 11.98 · Walker 10.38 · DeVonta 9.61 · **JJ 9.38** · MHJ 8.94(12g).

---

## The one systemic error that infects the whole board

The rival's stated framework is correct and is *mine*: anchor on prior PPG, treat TD rate as noise,
adjust for context. But look at what it actually ranks on:

- Puka > Chase because "the supplied line projects **129 receptions and 1,686 yards**."
- CMC at 5 on a "**304-point projection, 77 catches**."
- Cook at 11 on a "**280-point projection, 1,430 rushing yards**."
- Breece demoted because "his supplied line projects **1,071 rushing yards, 53 catches**."

Those are **Brendan's own full-PPR projections** — my `player-board.md` labels them tier-C ("my
arithmetic on Brendan's *optimistic* PPR projections… Lane A must replace these with pipeline-computed
his-scoring numbers"). Ranking players by the projections we're supposed to be *testing* is circular,
and it's full-PPR: it triple-counts receptions the format only half-credits. Every reception-hog is
sitting ~2.6–4.0 PPG too high on this board, and every pure runner ~0.4–1.4 PPG too low. That's not a
rounding error at pick 4; it's the whole ballgame in half-PPR.

I don't have to argue projections. I have the receipts.

---

## The calls the rival got WRONG (with receipts)

### 1. Chase at 4 is a full-PPR artifact. He's the single most over-ranked player on the board.

Chase's **actual 2025 in this scoring: 15.69 PPG** — WR-tier, not overall-top-4. The players the rival
ranks *below* him:
- **JT 19.96** (+4.27), **Bijan 19.49**, **Puka 19.41**, **Gibbs 19.32**, all outscored Chase by ~3.6–4.3 PPG.

The rival's own case for Chase is "the better touchdown profile" — but TD rate is the **least sticky
input in the entire study (r=0.008)**. It literally quoted that number and then leaned on it. The *real*
Chase bull case in this format is the +2 deep bonus (uncomputed in the table, genuinely helps him), but
that's a boom-play tiebreaker worth maybe +1 PPG, not the 4 he needs to clear JT. And it cuts both ways:
Chase's 15.69 came with the boom/bust variance that produces multi-week duds.
**My pick-4 tree is explicit: preference order JT ≥ Chase.**
- **Move:** Chase 4 → **6.** **Failure condition in the rival's board:** a 2–3 week TD drought (which his
  profile guarantees a few of) craters a 15.7-PPG WR you paid a top-4 workhorse price for.

### 2. Henry under Saquon is backwards in *this* format.

Rival: Saquon 14, Henry 15. Reality: **Henry 16.00 > Saquon 13.36** — Henry outscored him by **2.6 PPG
in 2025**, takes a smaller half-PPR haircut (−0.44 vs −1.16), *and* uniquely banks the +2 40-yard bonus
that the table can't even see (so his real edge is larger than 2.6). My board flags Henry verbatim: "NOT
a trap in THIS scoring — riser." The only thing true in the rival's writeup is the age cliff, which
applies to *both* 31-year-old backs.
- **Move:** flip them — Henry **11**, Saquon **15.** **Failure condition:** a run-script league where
  Henry's 14-TD, 40-yd-bonus profile is exactly what wins your specific format got left a full round
  behind a receiving back whose PPG was lower.

### 3. Bowers buried under McBride is a PPR read in a half-PPR league.

Rival: McBride 24 (TE1), Bowers 26. The counting-stat gap is real (McBride 14.88 vs Bowers 12.02), but
**McBride's value is 169 targets the format half-credits** — his half-PPR haircut is **−3.71**, the
biggest at the position, and my board and `qb-environment.md` both flag ARI's 649-attempt pass volume as
a mirage that regresses. Bowers scored his 12.02 on **TDs and big plays that survive the haircut**, as a
rookie, through bad QB play. My board's own note: "your Bowers > McBride take is *more* right in
half-PPR." The two-tier gap the rival draws should be near-zero.
- **Move:** Bowers 26 → **22**, essentially level with McBride. **Failure condition:** ARI's historic
  volume regresses (my base case), McBride slides toward 12 PPG, and you paid TE1 freight for a
  reception profile the format discounts — while the TD/big-play TE went two picks later.

### 4. Kyren-fade is correct — for a reason the rival never states, and I can prove it.

Rival ranks Breece 27, Kyren 35 (8 spots). On raw 2025 PPG that looks *wrong*: **Kyren 14.43 actually
outscored Breece 11.98.** The rival gets to the right answer by feel. Here's the proof it needed:
Kyren's 14.43 was **touchdown-fueled**, and TD rate is the single most useless predictor in the study
(**r=0.008** — indistinguishable from zero). Breece's number rests on a receiving three-down role that
survives both the format *and* regression. So the fade is right, but only because Kyren's production was
built on the one input we know doesn't carry. Cite the 0.008, don't hand-wave.
- **Verdict:** agree with the ranking, **fortified.** (This is what a better bot does — not just
  contradict, but supply the missing evidence for the calls that happen to be right.)

### 5. Jefferson at 10 undersells the cleanest buy-low on the board.

JJ's **9.38 PPG looks damning until you see why: a 2-TD outage on a 30.1% target share** — TD variance
(r=0.008) suppressing an intact alpha role. And the context moved: **Kyler Murray signed with Minnesota
and is the reported Week-1 starter** — a QB upgrade. This is a target-share (r=0.350, the #2 signal) buy
against a noise-driven down year. He belongs *above* the ARSB/CeeDee cluster the rival stacks over him,
not below.
- **Move:** JJ 10 → **~8.** **Failure condition:** the Murray/McCarthy competition and the TD regression
  both break wrong — but you're buying a 30% target share at a WR-dead-cat price, exactly the asymmetry
  the rival's own framework says to chase.

---

## The calls the rival got RIGHT (credit where it's due — this isn't reflexive)

- **JSN at 7.** Dead-on. **17.67 PPG, 35.8% target share, 0.888 WOPR** — elite and sticky. Over the
  ARSB/CeeDee/JJ tier is correct; his number simply is higher and target share is the #2 predictor.
- **Pickens > Rice.** Correct and format-aware: Pickens' **14.44 (WR6 2025)** full-season deep role banks
  the +2 bonus; Rice's **15.45 is elite per-game but on 8 games / 11-in-two-years** with a July knee
  checkpoint. Availability discount is right.
- **Chase Brown > Walker.** Correct. **CB 14.59 established receiving role** vs **Walker 10.38**
  Seattle-capped. My board agrees Walker is a high-end RB2, not a workhorse.
- **"RB adjustment is supply, not stability."** This is exactly my positional-stability finding and the
  rival nailed the nuance most sources botch: elite RB retention (47.2% top-12) actually *edges* WR
  (39.8%), YoY PPG correlations are equal (RB .682 / WR .702 / TE .712), and the real asymmetry is the WR
  pool being ~50% deeper. Good.

Where it's **half-right:** Achane at 12. The rank is fine, the reasoning is incomplete. The rival cites
"Miami scoring environment / weak goal line." The sharper, format-specific knife it missed: **Malik
Willis is a scrambler who cuts checkdowns, which dents Achane's 0.5-PPR *receiving* floor** — the exact
part of his profile this format is supposed to reward. My refined verdict: high-floor/capped volume RB1,
value only if he slides past 4. So — right number, better reason available.

---

## FootyBot's top 40 (his-scoring anchored)

Ranked on 2025 PPG [S], adjusted for 2026 role/health/age, the +2 bonus, and replacement value.
`†` = moved ≥ a tier from the rival board with cause.

| # | Player | Pos | Anchor / why |
|--:|--------|-----|--------------|
| 1 | Jahmyr Gibbs | RB | 19.32; bell cow (Montgomery→HOU), rush+rec+bonus, age 24 |
| 2 | Bijan Robinson | RB | 19.49; cleanest workload, age 24 (1–2 is a coin flip) |
| 3 | Puka Nacua | WR | 19.41; WR1, target hog — beats Chase by ~3.7 in *this* format |
| 4 | Jonathan Taylor | RB† | 19.96; workhorse, near-zero haircut, +2 breakaways, RB scarcity |
| 5 | Christian McCaffrey | RB | 21.51 (highest of anyone) discounted for age-30 + ~450 touches — see assumptions |
| 6 | Ja'Marr Chase | WR† | 15.69 + elite deep/bonus profile; boom ceiling, not a top-4 floor |
| 7 | Jaxon Smith-Njigba | WR | 17.67, 35.8% tgt, 0.888 WOPR |
| 8 | Justin Jefferson | WR† | 9.38 = 2-TD-outage buy-low on 30.1% tgt + Murray QB upgrade |
| 9 | De'Von Achane | RB | 18.08 locked workload; Willis dents receiving floor |
| 10 | Amon-Ra St. Brown | WR | 15.62; pure volume, biggest haircut already baked in |
| 11 | Derrick Henry | RB† | 16.00; format-perfect, +40yd bonuses uncounted |
| 12 | James Cook | RB | 16.81; fine not elite (bid to RB6, don't chase past this) |
| 13 | CeeDee Lamb | WR | 12.57(13g) alpha; the real risk is Dak's volume, not Pickens |
| 14 | Nico Collins | WR | 12.71; HOU WR1 target hog, VALUE at pick 17 |
| 15 | Saquon Barkley | RB | 13.36; aging, receiving keeps a floor |
| 16 | Ashton Jeanty | RB | ~14.3 rookie behind the worst OL; situation-improvement bet, proven volume |
| 17 | Drake London | WR | 13.99(12g); role locked (paid), open Penix/Tua QB is the risk |
| 18 | A.J. Brown | WR | 12.09; Maye alpha, age-29 |
| 19 | George Pickens | WR | 14.44 (WR6); deep-bonus fit, weekly volatility |
| 20 | Chase Brown | RB | 14.59; established receiving role survives bad scripts |
| 21 | Trey McBride | TE | 14.88 TE1; +5 over TE6 — but −3.71 haircut + ARI volume regresses |
| 22 | Brock Bowers | TE† | 12.02; TDs/big plays survive the haircut, level with McBride here |
| 23 | Rashee Rice | WR | 15.45(8g) elite per-game; availability is the whole bet |
| 24 | Kenneth Walker III | RB | 10.38 but locked KC lead back; price (early-2nd) is the risk, not role |
| 25 | Omarion Hampton | RB | 9-game rookie upside, ankle fracture, pass-pro questions |
| 26 | Jeremiyah Love | RB | rookie, ARI 3rd-overall + receiving; projected, not banked |
| 27 | Tee Higgins | WR | 12.14; fine WR2 |
| 28 | Josh Jacobs | RB | 14.61; volume/TD, unresolved DA legal review |
| 29 | Breece Hall | RB | 11.98; three-down/receiving beats Kyren's TD-fueled line |
| 30 | Chris Olave | WR | alpha profile; Dec-2025 lung clot — monitor camp |
| 31 | DeVonta Smith | WR | 9.61; inherits AJB's ~121 targets, capped by run-heavy PHI |
| 32 | Zay Flowers | WR | explosive-bonus adjustment |
| 33 | Malik Nabers | WR | 30%+ tgt ceiling BUT opens PUP (~Wk3), blank start — Brendan's 0-for-6 archetype |
| 34 | Garrett Wilson | WR | targets without an elite finish yet |
| 35 | Ladd McConkey | WR | 9.24; projection-dependent |
| 36 | Javonte Williams | RB | 14.08; clear DAL RB1 (market calls him expensive, not cheap) |
| 37 | Kyren Williams | RB | 14.43 but TD-dependent (r=0.008 non-sticky), weak ½-PPR floor |
| 38 | Colston Loveland | TE | TE upside below the McBride/Bowers price |
| 39 | Christian Watson | WR | 11.49(10g); deep/TD format boost |
| 40 | Davante Adams | WR | productive but age + TD-dependence narrow the ceiling |

**MHJ stays out** — 8.94 PPG, ~21% career target share, QB-capped by Brissett. "Year-3 breakout" is a
narrative, and it's Brendan's documented 0-for-6 archetype. Agree with the rival here.

---

## The strategy layer the rival didn't have (Brendan-specific, [S] provenance)

The rival cited "9 of 10 lean RB, you're the most WR-heavy" — correct, that's my `draft-tendencies.md`
Findings 2–3. But it stopped there and missed the parts that actually change the pick:

1. **Zero-RB has NEVER podiumed in this league** (Finding 7, N=5, 0% top-3). RB-RB opens post the best
   mean rank (4.67, 50% top-3). Brendan's **only podium (2021) was his one RB-RB open**; his **one
   Zero-RB year (2023) produced his lowest points-for ever.** So "Puka/Chase at 4 doesn't force RB" is
   true, but "secure a real RB by pick 17, don't punt the position" is the stronger, data-backed rule.
2. **Brendan's one durable leak is expensive POST_INJURY picks: 0-for-6, −46 points/pick** (Kupp 1.05,
   CMC 1.01). The board's injury-discount names — **Nabers (PUP), MHJ, Worthy** — *are* that archetype.
   Demand the extra round of discount; do not let a Nabers "ceiling" pull him into the top 30.
3. **CMC 2026 is NOT that archetype** — the bounce-back already happened (healthy 17-game RB1 2025).
   His bear case is **age-30 + ~450 touches**, not injury. And note: Brendan's 4-for-4 aging-vet hits
   were **all WRs** (Davante ×2, Hopkins) — that eye does *not* transfer to a 30-year-old RB.

---

## The five assumptions most likely to be wrong by September

1. **That Chase belongs in the top 4 in *this* scoring.** His 15.69 base + boom/bust means a short TD
   drought tanks a top-4 price; the deep-bonus case is real but uncomputed and volatile.
2. **That CMC's 21.51 repeats at 30 off ~450 touches.** The number is a ceiling, not a floor; RB aging +
   workload erosion is the live risk, and Brendan's aging-vet success doesn't transfer to an RB.
3. **That Rashee Rice plays enough games.** 15.45 per-game is elite; 11 games in two years + a late-July
   knee checkpoint is the actual bet. Availability, not talent.
4. **That the Year-3 receivers (Nabers, MHJ) arrive on schedule.** Nabers opens PUP (~Wk3 debut on a
   pitch count); MHJ is QB-capped by Brissett. Both are Brendan's 0-for-6 injury/hype archetype.
5. **That the ATL/MIA/KC role projections hold.** London's QB is an open Penix(ACL)/Tua battle; Achane's
   0.5-PPR receiving floor depends on Willis not cutting checkdowns; Walker's early-2nd price assumes a
   workhorse in a Mahomes pass-funnel that may resolve to efficiency-not-volume RB2.

*Generated by FootyBot from `research/positional-value.md`, `predictive-stats.md`, `draft-tendencies.md`,
`self-scouting.md`, and `player-board.md` — all [S] pipeline-computed under this league's exact scoring.*
