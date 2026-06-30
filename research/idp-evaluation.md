# IDP evaluation framework

Status: framework defined 2026-06-30 (conceptual — see "Next steps" for what needs the
blocked data pipeline). Scope per `docs/adr/0002-idp-scope.md`: this league starts exactly
**one** individual defensive player per week, in a roster slot flexible across DL/LB/DB.

## Scoring recap (from CONTEXT.md)

| Stat | Value |
|---|---|
| Tackle solo | 0.5 |
| Tackle assist | 0.25 |
| Sack | 4 |
| Interception | 6 |
| Forced fumble | 3 |
| Fumble recovery | 2 |
| Defensive TD | 6 |
| Pass defended | 3 |
| Tackle for loss | 0.5 |

The key structural fact: tackles are low-value-per-unit (0.5/0.25) but high-frequency:
a busy off-ball linebacker can rack up 8-12 solo tackles in a game (4-6 points) just from
volume, with no big play required. Sacks/INTs/forced fumbles are high-value but low-frequency
and position-concentrated. **This makes IDP scoring bimodal by position group**, which should
drive both draft strategy and weekly start/sit:

- **Volume/floor players (off-ball LBs, box safeties):** tackle-volume-driven, low weekly
  variance, weekly floor in the 5-10 point range for a true every-down player, low ceiling
  outside of an occasional turnover.
- **Big-play/ceiling players (edge rushers, interior DL, slot corners/free safeties):** boom-
  bust, a sack or pick can be worth as much as 4-6 solo tackles in one play, but a quiet week
  can be near zero. Higher variance, harder to start with confidence week to week.

## Positional volume hierarchy (general, pre-data-pipeline)

Ranked roughly by typical weekly tackle-volume ceiling, highest to lowest:

1. **Off-ball/inside linebackers in early-down, run-funnel defenses** — see every gap on
   early downs, often stay on the field in base personnel; highest, most stable tackle floor.
2. **Box safeties / "in the box" defenders** — high tackle volume when used as a near-LB
   run-defender, plus more INT/PD upside than a true linebacker since they're still in
   coverage on some snaps.
3. **3-down linebackers who stay on the field in nickel** — lower raw volume than #1 if they
   come off on passing downs, but added PD/coverage upside when they don't.
4. **Deep/free safeties** — lower tackle volume (they're defending the deep middle, not
   filling run gaps), but the highest per-snap INT odds on the defense.
5. **Cornerbacks (especially outside, non-slot)** — lowest tackle volume on this list, but
   PD (3 pts) is achievable at a decent per-snap rate for a CB who's targeted often; boom-bust
   like the DL group but for different reasons (target-share-into-the-defense-dependent, not
   scheme-dependent).
6. **Edge rushers / interior DL** — lowest tackle volume of all (run-support tackles are
   shared/credited differently at the line), but carry the sack (4) and TFL (0.5) upside —
   highest ceiling, lowest floor of any group.

Two confounds to watch once the pipeline can quantify this: (a) **bad run defenses can
inflate raw tackle counts** the same way bad rushing offenses inflate RB touches — more plays
run against a defense means more tackle opportunities, which isn't the same as a "good"
defensive player; (b) **scheme alignment (4-3 vs 3-4) changes which LB role accumulates
tackles** — a 3-4 "Mike"/inside role typically sees more two-gap run reps than a 4-3 "Will,"
who plays more in space and coverage.

## Draft strategy implications for a 1-flex-slot league

Because only one IDP slot exists, the marginal value of an elite IDP performance is capped at
one roster spot's worth of points — much lower marginal return than, say, a third RB who
could become a starter via injury. Implications:

- **Don't draft IDP early.** Prioritize a stable, every-down off-ball linebacker (group 1/2
  above) as a late-round IDP "starter" for floor, similar in roster logic to how you'd value
  a streaming DST — except an every-down LB's tackle floor is more predictable than team
  defense scoring, so a true 3-down LB is worth securing rather than purely streaming.
- **Stream the DL/CB matchup play if you want IDP ceiling.** Given only one slot, chasing
  sack/INT upside week-to-week (matchup-dependent DL vs. a bad pass-blocking line, or a CB
  facing a bad/turnover-prone offense) is a reasonable strategy *if* your primary IDP rostered
  player is already a stable floor option on bye/bad-matchup weeks — don't burn a bench spot
  on multiple IDPs unless the wire in this specific league is thin (commissioner-only invites,
  10-team league — check actual waiver-wire IDP availability once the season's roster data is
  visible).
- **Avoid paying draft capital for big-name pass rushers as your only IDP.** Their weekly
  floor is the worst of any group above; fine as a streaming/matchup play, bad as a "set and
  forget" single IDP starter in a format with no flex depth to smooth out a zero week.

## Next steps (blocked on data pipeline)

Once `pipeline/fetch_data.py` is unblocked, this doc should be replaced/supplemented with:
actual per-position tackle-rate-per-snap distributions from nflverse data (to confirm or
correct the hierarchy above with real numbers), defense-adjusted tackle opportunity (plays
run against each team), and a ranked list of 2026 IDP-eligible players by expected weekly
floor/ceiling under this league's exact scoring weights.
