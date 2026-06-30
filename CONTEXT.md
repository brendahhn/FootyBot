# CONTEXT.md

Living requirements doc for FootyBot, built via a grill-to-goal interview starting 2026-06-30.
Update this file as understanding changes; record one-way-door decisions as ADRs in `docs/adr/`.

## League

- Platform: Yahoo Fantasy Football
- 10-team league, snake draft, **our pick slot: #4**
- Draft date: not yet scheduled by the commissioner; planning around **late August 2026** as a placeholder
- League visibility: private (not publicly viewable), commissioner-only invites
- Roster: QB, WR, WR, RB, RB, TE, W/R/T, W/R/T, D, BN x7, IR (16 total slots)
- Fractional points: on
- Negative points: on
- Benched players: not locked (can swap after games start)

## Scoring (Yahoo league settings, confirmed from screenshots 2026-06-30)

### Offense
| Stat | Value |
|---|---|
| Passing yards | 25 yards / point |
| Passing TD | 6 |
| Interceptions thrown | -2 |
| Rushing yards | 10 yards / point |
| Rushing TD | 6 |
| Receptions | 0.5 (half-PPR) |
| Receiving yards | 10 yards / point |
| Receiving TD | 6 |
| Return TD | 6 |
| 2-point conversion | 2 |
| Fumbles lost | -2 |
| Offensive fumble return TD | 6 |
| 40+ yard run | +2 bonus |
| 40+ yard reception | +2 bonus |

Notable scoring implications: passing is **not** the standard 4pt/25yd — it's 6pt TD but still
25yd/pt, so volume passers are valued closer to rushers/receivers than in standard leagues.
Turnovers are punished harder than standard (-2/-2 vs typical -1/-2). Big plays (40+) get
extra bonus on top of yardage, rewarding explosive/boom-or-bust players.

### Individual Defensive Players (IDP)
| Stat | Value |
|---|---|
| Tackle (solo) | 0.5 |
| Tackle (assist) | 0.25 |
| Sack | 4 |
| Interception | 6 |
| Forced fumble | 3 |
| Fumble recovery | 2 |
| Defensive TD | 6 |
| Pass defended | 3 |
| Tackle for loss | 0.5 |

**Confirmed (2026-06-30): this is a real 1-IDP-flex league.** The roster's single `D` slot
starts one individual defensive player per week, with positional flexibility (not locked to
DL/LB/DB specifically) — not a team-defense slot, and not dead Yahoo-default settings. IDP
evaluation (tackle volume, role, scheme fit) is in scope.

## Goal

Build research + tooling to dial in draft and in-season roster decisions for this specific
league, going well beyond generic rankings. Specifically:

1. **Coach/scheme tendencies** — how each team's coaching staff actually uses personnel:
   shotgun vs. under-center rate, pass/run split by down and distance, target distribution
   by formation/alignment, pace. Track **2026 coaching changes** (new HCs/OCs) and what their
   tendencies were at previous stops, since that's a leading indicator before new-team play
   data exists.
2. **Player performance under coaches/schemes** — historical pattern: how does a given
   player's production shift when his coach, OC, or scheme changes (e.g. zone vs gap rushing
   scheme fit, slot vs outside usage under different OCs)?
3. **Predictive-stat research** — empirically determine which underlying stats are
   year-over-year predictive of fantasy output (e.g. target share, air yards, snap %, red
   zone touches, aDOT) versus noisy/unstable ones (e.g. TD rate, contested-catch rate) —
   for this league's specific scoring weights, not generic PPR.
4. **Breakout-profile comps** — given a player's current-season usage trend, draft capital,
   athletic profile, and situation, surface historically similar breakout seasons (e.g.
   "this player's 2026 profile rhymes with Player X's 2021 breakout") to support late-round/
   waiver-wire targeting.
5. **IDP evaluation** — since this league starts one flexible IDP slot, evaluate individual
   defenders (volume/role stability, scheme fit, opportunity) alongside offensive players.

### Phasing (agreed 2026-06-30)
- **Phase 1 (now):** research repo + data pipeline. Build out CONTEXT.md/ADRs, ingest free
  public data sources, ingest user-provided research dumps (see Inputs below), produce
  written findings/notes per topic above.
- **Phase 2 (pre-draft, closer to late Aug):** CLI tooling that turns the Phase 1 research
  into ranked cheat sheets / tiers tailored to this league's scoring and roster.
- **Phase 3 (draft day):** live draft-day assistant — given picks made so far and our roster
  needs, suggest who to take, pick by pick.

## Data sources

- **Decision (2026-06-30): free public sources only** — no paid data subscriptions
  (FantasyPros, PFF, etc.) planned. Primary candidates: nflverse / nflfastR play-by-play and
  player stats (via `nfl_data_py` or `nflreadpy`), Pro Football Reference, official
  NFL/ESPN/Yahoo public stat pages. Yahoo Fantasy API is a candidate for syncing actual
  league/roster state later, since this is a Yahoo league.
- **User-provided research dumps**: the user has manual findings and a Twitter "likes" export
  that are relevant (player notes, coach tendency takes, etc. they've already curated by
  liking). Format of the Twitter export is not yet known. Land these in `inputs/` as they're
  provided; do not block other work waiting on them.

## Open questions / not yet resolved

- Exact draft date (placeholder: late Aug 2026)
- Format of the Twitter likes dump (TBD when the user provides it)
- Whether to pull live league/roster state via the Yahoo Fantasy API, or treat this as
  purely external research support
