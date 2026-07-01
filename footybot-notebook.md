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
- **2026-07-01 — BRANCH RULE TRIGGERED (#3): this run did NOT write to `main`.** The runtime
  harness for this scheduled run hard-pinned the working branch to `claude/vigilant-cori-m5ojus`
  and explicitly forbade pushing to any other branch without explicit human permission. Per the
  operating prompt's BRANCH RULE #3, I did NOT silently fork or improvise — I pushed this run's
  work (coach-tendencies expansion + breakout-comps Egbuka cross-update + this notebook update)
  to `claude/vigilant-cori-m5ojus` and am surfacing it loudly instead. **Consequence: the memory
  loop is broken for the next scheduled run**, which reads `main` and will NOT see this work.
  ACTION NEEDED FROM BRENDAN: either merge `claude/vigilant-cori-m5ojus` into `main`, or repin
  the canonical branch in `footybot-operating-prompt.md`. The branch was cut from current `main`
  (notebook content identical), so a merge/fast-forward should be clean. Do this before the next
  Monday run or that run starts from stale memory.
- **2026-07-01 — DELIVERY GAP: Gmail draft NOT created this run.** The Gmail connector in this
  scheduled run exposed only sensitive-label tools (`apply_sensitive_message_label`,
  `apply_sensitive_thread_label` = trash/spam) — no create-draft / compose / send / search tool
  was available (confirmed via repeated ToolSearch). So STEP 6's digest email could not be
  drafted. This run's digest was delivered via the run's push-notification + run output instead.
  If future scheduled runs keep seeing a label-only Gmail connector, the operating prompt's
  "Gmail draft" delivery assumption needs revisiting (different connector scope in scheduled vs.
  interactive sessions?). Surfaced to Brendan this run.

## STATUS

- **Phase 1 (research repo):** in progress.
  - `research/coach-tendencies.md` — expanded 2026-07-01. Now covers 11 new-playcaller teams
    (added Chargers/McDaniel, Titans/Saleh-Daboll, Falcons/Stefanski-Rees, Buccaneers/Zac
    Robinson — all A-tier sourcing) + 2 flagged non-changes (Jaguars, Chiefs). Ravens & Browns
    entries re-verified this run against fresh sources (a broad-search summary tried to swap
    Monken→Falcons / Minter→Chargers; both wrong — Monken=Browns HC, Minter=Ravens HC). Still
    WebSearch-corroborated, not pipeline-verified. Continue expansion (Giants, Cardinals-OC,
    Commanders/Cowboys/Broncos/Eagles) + re-verify once preseason tape exists.
  - `research/breakout-comps.md` — methodology + 3 worked examples, WebSearch-corroborated.
  - `research/idp-evaluation.md` — conceptual framework; core claim now backed by real numbers
    in `research/predictive-stats.md` (tackle rate r=0.506 vs. sack rate r=0.091).
  - `research/predictive-stats.md` — **done, pipeline-verified, includes full 2025 season**
    (updated 2026-07-01). Brendan uploaded `player_stats.csv`/`player_stats_def.csv`
    (2016-2024) plus `stats_player_week_2025.csv` (nflverse's new unified per-season format).
    Both pipeline scripts exit 0 against real data, 2016-2025. Raw CSVs and `data/raw/` output
    are gitignored (reproducible, not committed) — only the scripts and the final markdown
    are versioned.
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
- `research/coach-tendencies.md`: Cardinals OC — a broad-search summary said Nathaniel Hackett
  was hired as Arizona OC, but it's unconfirmed whether Hackett or HC Mike LaFleur calls plays.
  NOT written into the doc this run (single low-quality source). Verify with a targeted search
  next run before adding.
- `research/coach-tendencies.md`: Giants thread — HC John Harbaugh (left Baltimore, which is why
  the Ravens hired Minter) + OC reported as Frank Reich. Corroborated enough to note as a lead,
  not yet worked into a full entry. Do next run.
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

### 2026-07-01 — Coach-tendencies expansion (+4 teams) + critic pass caught a bad-data swap
Focus item this run: expand `research/coach-tendencies.md` (highest-value queued lane; idea-queue
INBOX empty, no new nflverse data in `inputs/nflverse/`, so predictive-stats.md left untouched
per STEP 3 lane-4 discipline). Added 4 high-fantasy-impact 2026 new-playcaller teams, all A-tier
(named team-site + national sourcing): **Chargers** (OC Mike McDaniel calling plays under
Harbaugh; efficiency-up-not-necessarily-volume-up framing to avoid overselling a pass funnel vs.
Harbaugh's run lean), **Titans** (HC Saleh / OC Daboll; Cam Ward Y2-leap tagged Speculative, not
a lean), **Falcons** (HC Stefanski / OC Tommy Rees *calls plays* — flagged the common
Stefanski-calls-plays error; Bijan wide-zone fit as the headline, with honest "already
high-usage / could cap pass volume" caveat), **Buccaneers** (new OC Zac Robinson, McVay tree).
Cross-updated `research/breakout-comps.md`: the Bucs OC change is a real scheme change that
weakens the Egbuka↔A.J. Brown comp's "no scheme change needed" leg — downgraded that comp's
continuity assumption.

CRITIC-PASS KILLS this run (the point of STEP 3C):
- **Killed a data swap that would have corrupted two correct entries.** Two broad opening
  searches returned an internally contradictory summary placing Todd Monken as *both* Browns and
  Falcons HC, and Jesse Minter as *both* Ravens and Chargers HC — contradicting the (correct)
  existing doc. Targeted single-fact verification (team sites, ESPN, Wikipedia) confirmed:
  Monken = **Browns** HC (Kevin Stefanski, the fired Browns HC, went to the **Falcons** — that's
  the conflation); Minter = **Ravens** HC (came *from* Chargers DC; John Harbaugh left Baltimore
  for the Giants, opening the job). Existing entries held; nothing was overwritten. Worst failure
  mode seen: a fast search-summarizer merging multiple coaching-carousel states into one garbled
  paragraph — exactly the bad-data risk this project guards against.
- **Cut Cardinals OC Nathaniel Hackett** from being written — single low-quality source, and
  playcaller role (Hackett vs. HC LaFleur) unclear. Deferred to AUDIT_QUEUE for targeted verify.
- **Downgraded** the Cam Ward "Year-2 breakout" from a lean to Speculative (2nd-year-QB
  projection + worst-in-league 2025 offense = high variance, not something to bank a pick on).

BRANCH: this run was forced onto `claude/vigilant-cori-m5ojus` by the harness, NOT `main` — see
VERIFICATION LOG 2026-07-01. Memory loop needs a human merge/repin before next run.

### 2026-07-01 — Added 2025 season data (nflverse's format changed)
Brendan correctly flagged that the first pipeline run only covered through 2024 -- 2025 (the
most important season for 2026 prep) was missing. Re-downloading the same combined
`player_stats.csv`/`player_stats_def.csv` didn't help (that release asset is stale, last
updated ~May 2025, before the season). The actual fix: nflverse now publishes 2025+ data in a
new per-season unified format (`stats_player_week_2025.csv`, offense+defense combined in one
row, columns renamed `team`/`passing_interceptions` instead of `recent_team`/`interceptions`).
Updated `pipeline/fetch_data.py` to auto-detect and normalize this new format (glob for
`stats_player_week_*.csv`, rename columns, split into offense/defense projections) alongside
the legacy multi-year files, so next season's file drops in with no code change needed.
Re-ran both scripts (exit 0, 2016-2025, includes full 2025 season through the Super Bowl).
Correlations barely moved (~0.01 shift) vs. the pre-2025 run -- good stability check.
Side notes for future runs: (1) two of Brendan's upload attempts came through as empty
iOS file-provider bookmark placeholders rather than real content -- if an uploaded file's
content looks like `bplist00`/`NSKeyedArchiver` XML instead of real data, it didn't actually
transfer, ask for a re-upload after the user taps the file open in the Files app first; (2)
nflverse's release assets aren't all kept in sync at the same cadence -- check actual season
coverage in the data itself (`csv.DictReader`, not file size/name) rather than trusting a
release's "last updated" claim from search results alone.

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
