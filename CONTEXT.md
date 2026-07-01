# CONTEXT.md

Living requirements doc for FootyBot, built via a grill-to-goal interview starting 2026-06-30.
Update this file as understanding changes; record one-way-door decisions as ADRs in `docs/adr/`.

## League

- Platform: Yahoo Fantasy Football
- 10-team league, snake draft, **our pick slot: #4**
- Draft date: **August 28, 2026**
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
6. **Opponent modeling / friend draft tendencies** (added 2026-07-01) — model how each of the
   9 leaguemates drafts, from 7 years of the league's own actual draft boards (2019-2025), to
   anticipate position runs, know who punts/reaches on QB (relevant given 6pt passing TDs), and
   know who competes for which archetype. Data + analysis: `inputs/league-history/` +
   `research/draft-tendencies.md`. This is a real scope addition beyond pure player research —
   it's about the humans in the draft room, not just the players.

### Phasing (agreed 2026-06-30)
- **Phase 1 (now):** research repo + data pipeline. Build out CONTEXT.md/ADRs, ingest free
  public data sources, ingest user-provided research dumps (see Inputs below), produce
  written findings/notes per topic above.
- **Phase 2 (pre-draft, closer to Aug 28):** CLI tooling that turns the Phase 1 research
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

- Format of the Twitter likes dump (TBD when the user provides it)
- Whether to pull live league/roster state via the Yahoo Fantasy API, or treat this as
  purely external research support
- **Resolved (2026-07-01): the quantitative data pipeline.** This dev environment's network
  egress allowlist blocks `pypi.org`, npm, apt, GitHub's release-asset CDN, and WebFetch (see
  `docs/adr/0003-stdlib-pivot.md`), so nflverse data can't be fetched automatically. Fix: the
  user downloaded `player_stats.csv` and `player_stats_def.csv` directly from nflverse's GitHub
  releases on their own machine and uploaded them (zipped, to get under the 30MB chat limit).
  Pipeline now runs end to end against real data — `pipeline/fetch_data.py` and
  `pipeline/predictive_stats.py` both exit 0, producing `research/predictive-stats.md` with
  real Pearson correlations, filtered to 2016-2025 per `pipeline/fetch_data.py`'s
  SEASON_MIN/MAX (2016-2024 from the legacy combined release, plus the full 2025 season —
  see below). Not committed to git: `inputs/nflverse/*.csv` (raw source, gitignored) and
  `data/raw/` (generated output, also gitignored) — both are reproducible from the pipeline
  scripts, so only the scripts and the final `research/predictive-stats.md` are versioned.
- **Note (2026-07-01): nflverse changed its file format starting with the 2025 season** —
  offense and defense stats are now combined in one per-season file
  (`stats_player_week_<year>.csv`), using `team`/`passing_interceptions` instead of the old
  `recent_team`/`interceptions`. `pipeline/fetch_data.py` now handles both the legacy
  multi-year combined files AND this new per-season unified format (auto-detected via
  filename glob), normalizing columns before merging. Next season's data
  (`stats_player_week_2026.csv`) should drop in and get picked up with no code change needed.

## Research produced so far (Phase 1 — see `research/`)

- `research/predictive-stats.md` — **pipeline-verified**, real nflverse data, 2016-2025
  (includes the full 2025 season, regular + postseason). Notable results: target share
  (r=0.350) and WOPR (r=0.280) meaningfully predict next-season PPG; TD rate is ~noise
  (r=0.008) — matches conventional football-analytics wisdom, a good sanity check. IDP: solo
  tackle rate is strongly predictive (r=0.506), sack rate is not (r=0.091) — confirms the
  volume-vs-boom-bust framing in `research/idp-evaluation.md` with real numbers. (Results are
  stable vs. the pre-2025 run — correlations moved by ~0.01, as expected from adding one more
  season rather than something being broken.)
- `research/coach-tendencies.md` — first-pass coverage of 2026's highest-impact coaching
  changes (Raiders, Cardinals, Browns, Bills, Ravens, Steelers, Dolphins; Jaguars/Chiefs
  flagged as non-changes). Not all 32 teams yet — still WebSearch-corroborated, not
  pipeline-verified (coaching tendencies aren't in the player-stats data).
- `research/breakout-comps.md` — methodology + 3 worked examples (Luther Burden III ↔ Tee
  Higgins, Emeka Egbuka ↔ A.J. Brown, Christian Watson archetype). Still WebSearch-corroborated.
- `research/idp-evaluation.md` — positional volume hierarchy and draft-strategy framework;
  its core claim (tackle volume = floor, sacks = boom-bust) is now backed by
  `research/predictive-stats.md`'s real correlation numbers above.
