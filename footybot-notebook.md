# FOOTYBOT NOTEBOOK — persistent memory

Read FIRST, write LAST, every run (see `footybot-operating-prompt.md`). This file is the run
log and status board; the actual research content lives in `research/*.md` and `CONTEXT.md` —
this file indexes and tracks them, it doesn't duplicate them.

## SANDBOX_CAPABILITIES

Tested exhaustively 2026-06-30 (~15 distinct hosts probed). Do not re-test every run.

| Capability | Status | Notes |
|---|---|---|
| pip / PyPI / files.pythonhosted.org | BLOCKED | `host_not_allowed` |
| npm / registry.npmjs.org | BLOCKED | `host_not_allowed` |
| apt (archive.ubuntu.com, security.ubuntu.com) | BLOCKED | 403 |
| conda (repo.anaconda.com, conda.anaconda.org) | BLOCKED | CONNECT tunnel 403 |
| nflverse data hosts (release-assets.githubusercontent.com, objects.githubusercontent.com) | BLOCKED | CONNECT tunnel 403 |
| raw.githubusercontent.com | BLOCKED | CONNECT tunnel 403 |
| ESPN public API (site.api.espn.com, sports.core.api.espn.com) | BLOCKED | CONNECT tunnel 403 |
| Kaggle (kaggle.com) | BLOCKED | CONNECT tunnel 403 |
| WebFetch tool (any host, incl. example.com) | BLOCKED | environment-level, not site-specific |
| git clone of repos outside `brendahhn/*` | BLOCKED | session/environment git scope; confirmed via direct test (`nflverse/nflfastR-data` → 403) and `add_repo` cross-owner refusal |
| `github.com` canonical paths (releases page, release redirect issuance) | WORKS | redirect target (the CDN) is what's blocked, not github.com itself |
| WebSearch | WORKS | primary research channel |
| git push/pull/clone on `brendahhn/footybot` | WORKS | verified repeatedly |

**Operating consequence:** FootyBot runs in WebSearch-corroborated mode by default. Real
pipeline-computed numbers only happen when Brendan manually uploads nflverse CSVs to
`inputs/nflverse/` (see `pipeline/fetch_data.py` docstring for the exact verified URLs).

## VERIFICATION LOG

- 2026-06-30: `main` confirmed as the canonical branch. `git ls-remote origin main` returned
  `c5210986f157d309082589aa10040408eff4da53`, matching local `HEAD` exactly. No 403s or
  redirects seen on any push this session (5 successful pushes to `main`).

## STATUS

- **Phase 1 (research repo):** in progress.
  - `research/coach-tendencies.md` — first pass, ~10 teams, WebSearch-corroborated, not
    pipeline-verified. Needs expansion toward all 32 + re-verification once preseason tape exists.
  - `research/breakout-comps.md` — methodology + 3 worked examples, WebSearch-corroborated.
  - `research/idp-evaluation.md` — conceptual framework; core claim now backed by real numbers
    in `research/predictive-stats.md` (tackle rate r=0.504 vs. sack rate r=0.092).
  - `research/predictive-stats.md` — **done, pipeline-verified 2026-07-01.** Brendan uploaded
    `player_stats.csv`/`player_stats_def.csv` (zipped, 1999-2024 nflverse data). Both pipeline
    scripts exit 0 against real data. Raw CSVs and `data/raw/` output are gitignored
    (reproducible, not committed) — only the scripts and the final markdown are versioned.
- **Phase 2 (cheat sheets):** not started, blocked on Phase 1's predictive-stats analysis being
  real (or a deliberate scope decision to proceed without it).
- **Phase 3 (live draft assistant):** not started.
- **Draft date:** August 28, 2026.
- **Delivery/cadence:** confirmed 2026-06-30. Weekly (Mondays) until ~2 weeks before the draft,
  then daily. Gmail draft to brendanhamor@gmail.com (see operating prompt STEP 6 for format).
  Trigger `FootyBot Weekly` created 2026-06-30, cron `0 13 * * 1`. A reminder is scheduled for
  ~2026-08-14 to switch the cron to daily (`5 11 * * *` or similar) — if that reminder didn't
  fire for some reason, switch it manually once the draft is inside 2 weeks out.

## AUDIT_QUEUE

Items to re-verify or upgrade once conditions change (network policy widens, real data arrives).

- `research/coach-tendencies.md`: re-verify all entries against actual 2026 preseason/regular
  season tape once available — currently search-snippet-sourced only.
- `research/predictive-stats.md`: re-run once `snap_counts.csv` (offense/IDP snap%), red-zone
  play-by-play splits, or participation data (yards per route run) become available —
  explicitly skipped this run per the script's own docstring, not faked.
- `research/predictive-stats.md`: 40+ yard bonuses and offensive fumble-return TDs aren't
  computable from weekly aggregate data, so every PPG figure slightly under-counts real league
  points — re-run against play-by-play data if that ever becomes available to close this gap.
- `research/idp-evaluation.md`: still has the full conceptual positional hierarchy (6 groups,
  e.g. box safeties vs. deep safeties vs. CBs) that `predictive-stats.md` only partially
  confirms (solo tackles vs. sacks) — `player_stats_def.csv` doesn't have snap counts or
  position-group granularity to test the rest of the hierarchy; would need `snap_counts.csv`.

## CHANGELOG

### 2026-07-01 — Real data pipeline run (predictive-stats.md done)
Brendan uploaded `player_stats.csv` + `player_stats_def.csv` (zipped to get under the 30MB
chat limit; had to move the file off Google Drive to local storage on his Chromebook first
since ChromeOS won't zip a Drive-backed file directly). Ran `pipeline/fetch_data.py` (exit 0,
49161 + 86431 rows written, 2016-2024) then `pipeline/predictive_stats.py` (exit 0) →
`research/predictive-stats.md`. Critic-pass sanity check: results match known football-
analytics priors (target share/WOPR predictive, TD rate is noise, tackle rate predictive,
sack rate is not) — no red flags. Updated CONTEXT.md's Open Questions (pipeline blocker →
resolved) and this file's STATUS/AUDIT_QUEUE. Added `inputs/nflverse/*.csv` to `.gitignore`
(raw source files, 67MB, reproducible — not committed).

### 2026-06-30 — Initial setup (ported from prior session)
Built `CONTEXT.md`, ADRs 0001-0003, `research/coach-tendencies.md`,
`research/breakout-comps.md`, `research/idp-evaluation.md`, `pipeline/fetch_data.py`,
`pipeline/predictive_stats.py`, `pipeline/league_scoring.py`. Discovered and exhaustively
documented the network egress blocker (see SANDBOX_CAPABILITIES). Ported `safe-bot-edits` skill
and this three-file (prompt/notebook/idea-queue) architecture from `health-notebook`, matching
the proven Jobs Robot / Health Robot pattern. Branch verified as `main`. Cadence/delivery still
needs Brendan's confirmation before any scheduled trigger is created.
