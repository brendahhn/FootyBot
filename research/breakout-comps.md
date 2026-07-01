# Breakout-profile comps — methodology

Status: methodology defined 2026-06-30, with 3 worked examples. The fully numeric version of
this (matching this league's actual scoring-weighted production curves against historical
breakout seasons) needs the blocked data pipeline — see `CONTEXT.md` open questions. Until
that's unblocked, comps below are built from real, sourced situational/efficiency facts
(via WebSearch) plus well-documented historical analogues from general NFL knowledge, not
from a quantitative similarity score.

## Methodology

A "breakout profile" comp asks: does this player's *current* situation rhyme with a player
who broke out in a prior season, based on factors that are knowable **before** the breakout
happens (not just "he had a big year," which is hindsight)? The factors that matter, roughly
in order of predictive value for this league's scoring (half-PPR, big-play bonuses, TD-heavy):

1. **Opportunity trajectory, not just opportunity level.** A player whose target share/snap
   share is *rising* game-over-game (especially after a depth-chart change: injury, trade,
   release of the player ahead of him) is a stronger signal than a player who already has a
   large but flat target share.
2. **Per-opportunity efficiency on his current (limited) volume.** Yards per route run (YPRR)
   and yards per target are far more stable year-over-year than counting stats like TDs, and
   they're visible even when raw volume is low — this is the single best "is the talent
   already showing through a small sample" signal. See `research/predictive-stats.md` once
   the data pipeline can produce it; until then, use YPRR/YPT figures reported by analysts.
3. **A concrete, named catalyst for more volume.** "He's talented" is not a breakout case;
   "the WR1 ahead of him left in free agency" or "the starting RB is on a rookie-friendly
   contract about to expire and the backup is outproducing him in camp" is.
4. **Scheme fit with the playcaller** — cross-reference `research/coach-tendencies.md`. A
   zone-run team's backs and motion-heavy offenses' slot receivers have a different breakout
   shape than gap-scheme/under-center teams.
5. **Draft capital / situation quality** as a tiebreaker, not a primary signal — it correlates
   with opportunity but lags behind 1-3 once a player has NFL snaps to evaluate.

A comp is "fully worked" when it names the specific historical player, the specific shared
factors (not vague similarity), and the specific way the comp could break (where the situations
actually differ) — a comp without a stated failure mode is just a vibes-based player comp,
which is exactly what this project is trying to avoid.

## Worked example 1: Luther Burden III (CHI) ↔ Tee Higgins (CIN, 2020→2021)

- **Current situation (sourced 2026-06-30):** Burden posted an elite 2.69 yards per route
  run as a rookie in 2025 despite a limited target share in a crowded Bears WR room (DJ
  Moore, Rome Odunze, plus TE Colston Loveland). Moore has since departed, freeing up a large
  chunk of vacated target share for 2026 between Burden and Odunze.
- **Historical comp:** Higgins was a 2020 rookie who flashed real per-target efficiency
  behind a clear WR1 (A.J. Green) in a run-funnel-adjacent context; Green left for Arizona in
  free agency after that season, and Higgins' role and target share expanded materially in
  2021, when he posted his first 1,000-yard season as a clear co-WR1.
- **Shared factors:** rookie-year efficiency-over-volume profile, a named WR1 departure
  opening a specific, quantifiable chunk of vacated targets, and an existing offense/QB that
  didn't need to be rebuilt around the breakout candidate.
- **Where it could break:** Higgins had no internal competition for the vacated share once
  Green left (Chase hadn't arrived yet); Burden splits Moore's vacated targets with Odunze
  *and* a receiving TE (Loveland), so the per-player share gained is smaller than Higgins'
  was. Diluted upside vs. the comp.

## Worked example 2: Emeka Egbuka (TB) ↔ A.J. Brown (TEN, 2019→2020)

- **Current situation (sourced 2026-06-30):** Egbuka was playing at a WR3-in-PPR pace through
  the first five weeks of 2025 (5 TDs in that stretch) before a hamstring injury derailed his
  season; in games without Mike Evans, his target share, catches, yards, and PPG all rose
  noticeably (8.5 targets/g vs 6.25, 12.3 PPG vs 10.4) — i.e., when given the role, he
  produced like a true WR1, but the sample was injury-shortened.
- **Historical comp:** Brown's 2019 rookie season was limited in raw volume (run-heavy Titans
  offense, shared backfield with Corey Davis as the "other" outside receiver) but he was
  already elite on a per-target basis; once 2020 gave him a fuller, healthier role in the same
  system, he broke out as a top-5 fantasy WR without a scheme change — the talent and
  efficiency were already visible, volume was the only thing missing.
- **Shared factors:** flashed true-WR1 efficiency in a limited/interrupted sample, the
  limitation was opportunity (health/role) rather than ability, and no scheme change is
  required for the breakout — just more snaps in the existing offense.
- **Where it could break:** Brown's limiter was scheme/role allocation, not recurring injury
  risk; if Egbuka's 2025 absence reflects an injury-prone profile rather than a one-off, the
  comp's "just needs more snaps" thesis is weaker — health, not target competition, is the
  swing factor here, and that's inherently less predictable.
- **Update 2026-07-01 (weakens the comp's "no scheme change" leg):** Tampa Bay hired a new
  play-caller for 2026 — Zac Robinson (McVay tree, ex-Falcons OC), replacing fired 2025 OC Josh
  Grizzard (A-tier: buccaneers.com/ESPN/NFL.com — see `research/coach-tendencies.md`). The A.J.
  Brown comp explicitly rested on "no scheme change required, just more snaps in the *existing*
  offense." That leg no longer holds: Egbuka's flashes came in the 2025 system, and a new
  scheme means new alignment/usage patterns, so rookie-year per-route efficiency doesn't
  transfer 1:1. Net: the comp's *talent/efficiency* leg still stands, but its *continuity* leg
  is now a question mark — downgrade confidence until 2026 usage under Robinson is visible.
  (Mild offsetting positive: a McVay-tree motion offense can be slot/YAC-friendly, and Egbuka
  profiles as that type — but that's a new, unproven bet, not the original thesis.)

## Worked example 3: Christian Watson (GB) — field-stretcher gaining volume from offensive necessity

- **Current situation (sourced 2026-06-30):** Even in a 10-game 2025 season, Watson posted
  elite per-play efficiency (17.5 YPC, 11.1 yards/target, 2.28 YPRR). Green Bay's receiving
  corps is reportedly less crowded entering 2026, and uncertainty in the run game could push
  more pass volume to Jordan Love.
- **Comp framing (lighter-confidence, general archetype rather than one named player):** this
  matches the recurring "big-play field-stretcher whose offense is forced to pass more than
  its identity suggests" pattern seen across several run-funnel-into-passing situations
  league-wide — efficiency was never the question, offensive context (run-game health, scheme
  pass rate) was. Cross-reference `research/coach-tendencies.md` once Green Bay's 2026
  offensive identity (pass rate, shotgun rate) is confirmed in camp — this comp is weaker than
  comps 1-2 until that's verified, since it depends on team-level offensive philosophy, not
  just Watson's individual role.
- **Where it could break:** "uncertain run game forces more passing" is a circumstantial bet,
  not a structural one (unlike Burden's vacated-target-share or Egbuka's health-only-limiter
  stories) — if Green Bay's run game is fine, this comp doesn't materialize.

## Next steps (blocked on data pipeline)

Once `pipeline/fetch_data.py` is unblocked, replace the "sourced via WebSearch" efficiency
figures above with pipeline-computed numbers, and extend this methodology to a systematic
scan (every player with rising opportunity + above-median YPRR on <50% snap share) rather
than hand-picked candidates.
