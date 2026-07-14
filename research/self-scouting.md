# SELF-SCOUTING — Brendan's real draft tendencies (receipts-based)

> Supersedes the old `draft-tendencies.md` Finding 5 "superpower/leak" framing, which Brendan
> flagged 2026-07-08 as obsessive and small-sample. RULE: never invoke a "leak" or "superpower"
> in the newsletter without showing the actual pick list and the sample size, in that moment.
> Every pattern here is DIRECTIONAL, not a law. Source: `inputs/league-history/draft_history_enriched.csv`
> (his real 2019-2025 picks + archetype flags). Re-age every player to the CURRENT season before
> applying any of this.

## The "second-year leak" is largely a MYTH — do not tag young players by age

Brendan's actual picks entering their 2nd NFL year (`experience_at_pick == 1`):

**Hits (several are among his best picks ever):**
- A.J. Brown, 2020, pick 41 — smash
- Jaylen Waddle, 2022, pick 45 — smash
- De'Von Achane, 2024, pick 18 — smash (league-winner)
- Chris Olave, 2023, pick 23 — solid
- DeVonta Smith, 2022, pick 136 — hit (cheap)

**Busts:**
- Kyle Pitts, 2022, pick 36 — bust
- Brian Thomas Jr., 2025, pick 13 — bust (his worst pick, per draft_outcomes)
- Clyde Edwards-Helaire, 2021, pick 20 — disappointing
- Kerryon Johnson, 2019, pick 25 — bust
- Jahan Dotson, 2023, pick 63 — bust
- Laviska Shenault, 2021, pick 101 — bust (cheap)

**Verdict:** ~a coin flip, and the hit side contains multiple league-winners. "Brendan flops on
second-year players" is the bot cherry-picking the busts and ignoring Achane/AJB/Waddle/Olave.
The ONLY version with thin signal: *expensive* (rounds 1-3) year-2 picks bought purely on a
NARRATIVE leap with weak underlying usage (Pitts, BTJ, CEH). Even that is not robust. **Never
stamp the bust-pattern on a current young player by age alone.** Jeanty (2026 sophomore) is a
situation-improvement bet with a proven rookie volume floor (1300 YFS behind the worst OL) — a
DIFFERENT archetype from a narrative leap. Nabers is entering Year 3, not even second-year.

## The real, narrower leak that survives the receipts: expensive POST_INJURY picks

His `POST_INJURY`-flagged picks:
- Cooper Kupp, 2023, pick 5 — expensive bust
- Christian McCaffrey, 2021, pick 1 — injured that year
- Courtland Sutton, 2021, pick 80 — down year
- Devonta Freeman, 2019, pick 36 — bust
- Will Fuller, 2019, pick 76 — injury-shortened
- Kareem Hunt, 2022, pick 76 — meh
- Elijah Mitchell, 2023, pick 118 — bust
- (Cam Newton 2020, Brandon Aiyuk 2025 — late/cheap)

**Verdict:** this one holds, especially the EXPENSIVE ones (Kupp 1.05, CMC 1.01). When Brendan
circles a post-injury star early, flag it and demand the extra round of discount. This is the
leak worth naming — not the second-year thing.

## "Superpowers" that are really small-sample footnotes — STOP obsessing

- **Aging vets "4-for-4":** Larry Fitzgerald (R11), Tom Brady (R9), Davante Adams ×2 (pick 16 / R6),
  Keenan Allen (R4), James Conner (R6), Mark Ingram (R12), Mahomes-as-vet (R10). These are mostly
  LATE, low-risk picks that were fine. n≈4-8 of cheap vets ≠ an identity. Brendan himself: "it's
  Davante twice plus DHop once… you're obsessive over it." Do not lead with this.
- **Mid-round QB "superpower":** Lamar/Mahomes/Herbert — real, but n≈3. Directionally his best
  category; still a footnote, not a nightly talking point. The structural version worth citing is
  the MARKET fact (his league under-drafts QB vs 6pt passing TDs — measured in draft-tendencies.md),
  not "Brendan is a QB genius."

## THE UNIFYING LENS (added 2026-07-14) — he wins buying manufactured discounts, loses paying for hype

This reframes the same data more usefully than the leak/superpower list. Pairing his real 2025
pick-value deltas [S, `draft_outcomes.py`] with the draft-time media narrative on each pick [B,
WebSearch] shows one clean pattern **at the extremes** of his 2025 draft:

**His HITS were all "depressed price + identifiable catalyst" — discounts the media had manufactured:**
- **Patrick Mahomes, R10 (value):** media literally ran *"Why you should fade Mahomes"* (QB11 two
  years running, Wk15 '24 ACL/LCL). He bought the best QB alive in round 10.
- **Davante Adams, R6 (+73.9):** priced WR16 on the age curve (32); he banked the Stafford reunion →
  led the NFL in receiving TDs (14).
- **Kenneth Walker III, R4 (+56.2):** discounted for a timeshare + 3.7 YPC; he bought the Kubiak/
  Shanahan scheme upgrade.

**His MISSES were the mirror image — paying up on consensus ceiling with NO discount:**
- **Brian Thomas Jr., R2 (−142.0 = his worst pick ever [S]):** consensus ~WR8, Nabers-tier, a
  *2,000-yd* ceiling floated; pure ascending-alpha hype at a round-2 price. Cratered to 707/2.
- **Tank Bigsby, R7 (−77.6):** paid ~R7 for a back the market had ~R11 (overpaid vs ADP).

**Verdict:** his edge is **price discipline as a buyer of manufactured discounts**, not any age/
position "leak." Aggregate career data agrees: STEADY/value picks **+9.1/pick**; the one true leak is
paying up (expensive POST_INJURY **0-for-6**, and BTJ = an expensive year-2 *narrative leap at full
price*, the exact sub-pattern this file already flagged as the only one with signal). **Decision rule
for the newsletter:** when a player has a real discount AND a concrete catalyst → his wheelhouse,
press it. When he reaches above ADP because the ceiling story is fun → that's the −142 replaying.
CAVEAT: 2025 is n=16, small-sample — directional, and it holds cleanest at the extremes (mid-picks
like Jeanty/Hampton/Sutton are neutral). Not a law; a tendency that rhymes with the multi-year data.

### 2025 draft-time media-narrative retrospective [B/C — the queued "media narratives" TOPIC, started 2026-07-14]
Sourced this run (see `newsletters/2026-07-14.md` for the per-player receipts + outlets):
- BTJ: WR8 consensus, WR2-from-Wk13-on rookie thesis, Coen-offense hype, 2,000-yd ceiling floated.
- Jeanty: No.6 NFL pick, RB6 ADP, "set up to smash." **Re-age for 2026: sophomore with a proven
  volume floor (321 touches/1,321/10 as a rookie behind a bad LV ecosystem) — a situation-improvement
  bet, NOT a BTJ-style narrative leap. Do not conflate.**
- Walker: value + Kubiak scheme catalyst. Davante: new-team/Stafford reboot. Mahomes: active fade
  narrative. Bigsby: cheap telegraphed lottery ticket. Kraft: "next breakout TE" (was hitting, Wk9 ACL).
  Sutton: safe WR3 floor capped by age/young WRs.
- **Backlog (slow burn, a few picks/run):** next do his 2024 board, then the league's biggest hits/busts.

## How to use this

Mention a pattern ONLY when (a) a live take/pick actually fits it AND (b) it's material to a real
decision at his pick slot. Show the receipts + sample size when you do. Never repeat a pattern for
its own sake. Update this file as new drafts/outcomes arrive.
