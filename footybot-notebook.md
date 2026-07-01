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

**Operating consequence (updated 2026-07-01):** the raw nflverse CSVs are now committed directly
in `inputs/nflverse/` (no longer gitignored) so every clone — scheduled or interactive — has
real stats memory without needing a fresh upload. Run `pipeline/fetch_data.py` then
`pipeline/predictive_stats.py` every run unconditionally (operating prompt STEP 0). WebSearch
remains the channel for anything the pipeline can't compute (coaching, trades, depth charts).

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
- **2026-07-01 (2nd run today) — BRANCH RULE TRIGGERED AGAIN (#3), now a confirmed RECURRING
  pattern.** The scheduled harness for THIS run hard-pinned the working branch to
  `claude/modest-gates-4i3fc0` and again forbade pushing to `main` without explicit human
  permission. This is the 2nd consecutive scheduled run to be force-pinned off `main` — it is a
  structural configuration issue, not a one-off. Per BRANCH RULE #3 I did NOT silently fork or
  improvise onto a self-chosen branch: I pushed this run's work (Eagles coach-tendencies entry +
  idea-queue status + this notebook update) to the harness-assigned `claude/modest-gates-4i3fc0`
  and am surfacing it loudly. GOOD NEWS: the previous side branch (`claude/vigilant-cori-m5ojus`)
  WAS merged into `main` before this run — local branch was cut cleanly from `main` HEAD
  (87c5239), so memory was NOT stale this run. The merge-each-run workaround is holding, but it
  needs Brendan every run. **DURABLE FIX NEEDED (pick one):** (a) configure the scheduled
  runtime/trigger to allow pushing to `main` directly; or (b) accept the merge-each-run workflow
  as the standing process; or (c) repin the canonical branch in `footybot-operating-prompt.md`'s
  BRANCH RULE to whatever the scheduled harness actually allows. Until one of these lands, every
  scheduled run will keep force-forking and requiring a manual merge.
- **2026-07-01 (2nd run today) — DELIVERY GAP persists: Gmail draft again NOT created.** Same as
  earlier today — the connector exposed only `apply_sensitive_message_label` /
  `apply_sensitive_thread_label` (trash/spam); no compose/draft/send/search tool (re-confirmed via
  ToolSearch this run). This is now 2-for-2 on scheduled runs seeing a label-only Gmail connector,
  so STEP 6's "Gmail draft" delivery assumption is effectively broken for scheduled runs. Digest
  delivered via push-notification + run output instead. Needs a human call: either grant the
  scheduled connector compose scope, or change STEP 6 to a delivery channel scheduled runs can
  actually use.

## STATUS

- **Phase 1 (research repo):** in progress.
  - `research/coach-tendencies.md` — 13 new-playcaller teams covered (Raiders, Cardinals,
    Browns, Bills, Ravens, Steelers, Dolphins, Chargers, Titans, Falcons, Buccaneers, Eagles)
    + 2 flagged non-changes (Jaguars, Chiefs). **Eagles entry substantially deepened 2026-07-01
    (interactive session, after Brendan flagged the scheduled run's first pass as too thin):**
    added the A.J. Brown trade to New England (the single biggest fact the first pass missed —
    a personnel trade, not a coaching change), the Wicks trade + Makai Lemon 1st-round pick, and
    the Jeff Stoutland (longtime O-line coach) departure. **Going forward every team entry must
    cover coaching/scheme + roster moves + O-line + RB depth + QB room, not just coaching/scheme
    — see operating prompt STEP 3 checklist (v2026-07-01).** Remaining entries (Chargers through
    Buccaneers) were written before this checklist existed and may be missing the same
    dimensions — re-pass them before assuming they're complete. Continue expansion (Giants,
    Cardinals-OC, Commanders/Cowboys/Broncos) + re-verify once preseason tape exists. Audit lead:
    Kevin Patullo (fired Eagles OC) reportedly went to the Dolphins — confirm his role there vs.
    our Bobby-Slowik Miami entry.
  - `research/breakout-comps.md` — methodology + 3 worked examples, WebSearch-corroborated.
  - `research/idp-evaluation.md` — conceptual framework; core claim now backed by real numbers
    in `research/predictive-stats.md` (tackle rate r=0.506 vs. sack rate r=0.091).
  - `research/predictive-stats.md` — **done, pipeline-verified, includes full 2025 season**
    (updated 2026-07-01). Brendan uploaded `player_stats.csv`/`player_stats_def.csv`
    (2016-2024) plus `stats_player_week_2025.csv` (nflverse's new unified per-season format).
    Both pipeline scripts exit 0 against real data, 2016-2025. Raw CSVs and `data/raw/` output
    are gitignored (reproducible, not committed) — only the scripts and the final markdown
    are versioned.
  - `research/draft-tendencies.md` — **NEW 2026-07-01, opponent modeling (Goal item 6).**
    Built from 7 years of the league's real draft boards (2019-2025), `inputs/league-history/`
    → `draft_history_master.csv` (1,120 picks, validated join to 10 stable managers, positions
    from nflverse). Key findings: Dylan always punts QB (round 7+ every year); Aaron/lucas
    draft QBs earliest; Jack is the only WR-first R1 drafter; Brendan is the most WR-heavy early
    drafter (confirms his own "RBs overvalued here" read). S-tier by provenance (league's own
    history). Pipeline: `pipeline/extract_yahoo_mhtml.py` + `pipeline/build_draft_history.py`.
- **Phase 2 (cheat sheets):** not started, blocked on Phase 1's predictive-stats analysis being
  real (or a deliberate scope decision to proceed without it).
- **Phase 3 (live draft assistant):** not started. NOTE: the draft-tendencies opponent model is
  a direct input to Phase 3 (live pick suggestions should account for who's likely to take what).
- **Draft history note:** raw Yahoo MHTML exports (61MB, 14 files) are NOT committed; the small
  extracted `.txt` intermediates in `inputs/league-history/extracted/` are, and fully rebuild
  the CSV. Brendan may send more seasons — drop them in `extracted/` and re-run the build.
- **Draft date:** August 28, 2026.
- **Delivery/cadence (superseded 2026-07-02 — now the DAILY NEWSLETTER):** Brendan set the
  routine to nightly ~11:30pm PT himself in the routine settings. Each run writes
  `newsletters/YYYY-MM-DD.md` (dated for the next morning) + a push notification with the
  headlines. Full architecture: `docs/daily-newsletter-spec.md` (4 lanes + reviewer, hybrid
  compete mode, "checking your takes"). Gmail is broken for routines (label-only connector,
  2-for-2 runs) — diagnosis given to Brendan (reconnect Gmail in claude.ai connector settings
  with full permissions); each run makes ONE quick ToolSearch check and adds a Gmail draft only
  if compose ever appears. The old ~2026-08-14 "switch to daily" reminder is moot (already
  daily); if it fires, just confirm the cadence is still what Brendan wants and dismiss.

## AUDIT_QUEUE

Items to re-verify or upgrade once conditions change (network policy widens, real data arrives).

- `research/coach-tendencies.md`: **Miami OC cross-check.** Search this run surfaced that Kevin
  Patullo (fired Eagles OC) reportedly landed with the Dolphins, but our Miami entry lists Bobby
  Slowik as OC. Verify Patullo's actual Miami title (could be a lower role, OR the Slowik entry
  may be wrong) with a targeted search next run before trusting the Miami entry.
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
- ~~`research/draft-tendencies.md`: rookie/"flashy new guy" tendency per manager~~ — **DONE
  2026-07-02** as Finding 4 (`pipeline/draft_archetypes.py`, experience-at-pick reconstructed
  from committed 1999-2025 nflverse data; enriched CSV committed). Spot-check validated.
- `research/draft-tendencies.md` NEW: **realized outcomes of archetype bets** — did Brendan's
  post-injury picks (CMC '21, Kupp '23) return value? Did Dylan's breakout-chases hit? All
  computable from the same data (compare pick's season-of-draft PPG vs same-round
  alternatives). Strong newsletter deep-dive candidate for Lane A or D.
- `research/draft-tendencies.md`: reach-vs-value per manager needs historical ADP per season to
  compare each pick against where the player was going — no ADP source yet.
- `research/draft-tendencies.md`: 3 skill players (Hollywood Brown, Kenny Gainwell, Joshua
  Palmer) don't auto-match a position via nflverse name-join (suffix/nickname quirks); currently
  hand-corrected in the writeup but left blank in the CSV. Minor. A small alias map in
  `build_draft_history.py` would fix it if it ever matters.

## CHANGELOG

### 2026-07-02 (interactive session, follow-up) — Archetype layer: what managers were THINKING
Brendan: positional tendencies are great, but he wants the thought-process at the time —
"did this friend take the risky RB? The solid breakout receiver from the year before? The
rookie?" — and needs the database accessible to the routine. Built:
- `pipeline/draft_archetypes.py` — reconstructs what every drafted player looked like ON THAT
  DRAFT DAY from the committed nflverse history (experience-at-pick, prior-season PPG/games,
  weekly variance under THIS league's scoring), derives archetype flags (ROOKIE, SECOND_YEAR,
  BREAKOUT_CHASE, POST_INJURY, BOOM_BUST, AGING_VET, STEADY; thresholds documented+tunable).
- `inputs/league-history/draft_history_enriched.csv` — committed, so every scheduled run has
  it (the DB-accessibility ask; the whole league-history dir was already committed 2026-07-01).
- `research/draft-tendencies.md` Finding 4 — per-manager archetype table + personality reads +
  pick-4 exploits. Spot-check validated (Niko's rookies incl. R1 Bijan; Connor's Julio×3/old
  Kelce; Brendan's CMC-'21/Kupp-'23 post-injury R1s; Dylan's McLaurin/JT/CeeDee/Claypool
  breakout-chases). Headline reads: lucas has taken ZERO rookies in rounds 1-8 in 7 years;
  Nate has ZERO post-injury picks; Connor doubles the league rate on aging vets; Brendan
  himself is the league's biggest discount-rack shopper (lowest STEADY share, most
  post-injury) — and his 2025 mock targets (Egbuka/MHJ/Worthy) fit the same pattern, which the
  newsletter should pressure-test.
- Operating prompt Lane C + spec updated to use both layers. New AUDIT_QUEUE item: realized
  outcomes of archetype bets (did the discount-shopping actually pay off?).

### 2026-07-02 (interactive session) — v3: DAILY NEWSLETTER architecture
Brendan's ask: "the ultimate data driven fantasy football research tool… runs every day…
output: a morning newsletter… spawn n agents and a reviewer." Interviewed him (2 rounds,
8 questions) and built it:
- Decisions: repo file + push notification delivery (Gmail broken for routines — reconnect
  diagnosis given, one quick check per run thereafter); hybrid agent design (4 specialist
  lanes: Data / News / Market / Rabbit-hole + reviewer with kill authority); compete mode
  fires at the bot's judgment on contested high-stakes questions; full-analysis length daily;
  all four content pillars (camp/beat, ADP, deep dive, draft countdown); **"checking your
  takes" — challenge Brendan hard, with receipts**; schedule already set by Brendan (~11:30pm
  PT nightly), newsletter dated for the next morning.
- Artifacts: `docs/daily-newsletter-spec.md` (the agreed spec), `footybot-operating-prompt.md`
  fully rewritten to v2026-07-02 (`## END` verified intact), `newsletters/` created.
- Unchanged rails: verification discipline, tiers, critic pass (now the reviewer), catch-up
  priority, rabbit holes, branch rule + merge-each-run workaround, safe-bot-edits.
- First night's open questions: do subagents work in the scheduled environment (fallback:
  sequential lanes), and the recurring branch pin still needs a merge after each run.

### 2026-07-01 (interactive session) — Built the opponent-modeling dataset from 7 yrs of drafts
Brendan sent 7 seasons of the league's actual Yahoo draft boards + Managers pages (2019-2025) as
saved MHTML. Built the whole thing end to end this session:
- `pipeline/extract_yahoo_mhtml.py` — decode/strip saved Yahoo MHTML to clean text + title attrs
  (the title attrs hold the full team name per pick, since Yahoo truncates them in the visible
  board). Reusable for future exports.
- `pipeline/build_draft_history.py` — join players×teams×managers per year, enrich with position
  from the committed nflverse data. Validated hard: 1,120 picks, 0 unmapped managers, exactly 16
  picks/manager/year, and it correctly split three near-identical 2019 team names ("peeks for
  playoffs" / "Peeks for playoffs" / "Peeks for PlayoffsV2" → Niko/Connor/Nate) by exact case.
- `inputs/league-history/draft_history_master.csv` + `extracted/` intermediates + README.
- `research/draft-tendencies.md` — real findings (QB timing, R1 position lean, early RB/WR
  identity per manager). Confirmed Brendan's own instinct with data: 9/10 managers lean RB in
  R1, only Jack is WR-first; Brendan himself is the most WR-heavy early drafter + a late-QB guy.
- `CONTEXT.md` Goal item 6 added (opponent modeling — a real scope expansion beyond player
  research, now that the data exists to support it).
Committed the small extracted `.txt` (not the 61MB of raw MHTML) so the CSV is reproducible.
This is a direct input to Phase 3 (live draft assistant). Rabbit-hole depth here was the point —
went past "here's a CSV" to actual validated tendencies and self-scouting.

### 2026-07-01 (interactive session, follow-up) — Catch-up priority + "rabbit holes" instruction
Brendan: "catch up first, when I'm not feeding it ideas, I need it going down rabbit holes."
Revised `footybot-operating-prompt.md` again (version-date → 2026-07-01b, `## END` re-verified):
STEP 2 is now explicitly ordered — (1) catch-up backlog (the 12 pre-checklist coach-tendencies
entries) before any new team, (2) idea queue, (3) if both are clean, chase secondary leads to
an actual conclusion instead of deferring everything to AUDIT_QUEUE ("going down rabbit holes"),
still bound by the same verification/critic-pass rails. Next run's real test: does it actually
re-pass Chargers/Cardinals/Browns/Bills/Ravens/Steelers/Dolphins/Titans/Falcons/Buccaneers
against the new checklist before touching anything new, and does it chase at least one lead
(e.g. the Kevin Patullo→Dolphins audit item) to a real conclusion rather than re-logging it.

### 2026-07-01 (interactive session) — Fixed the two things Brendan called out as broken
Two merges + a real prompt revision, prompted by direct, sharp feedback that the scheduled runs
were producing too little (one narrow angle per run) and couldn't do real stats analysis at all.

1. **Merged both stranded scheduled-run branches into `main`.** `claude/vigilant-cori-m5ojus`
   (already merged earlier) and **`claude/modest-gates-4i3fc0`** (the Eagles-entry run) had
   diverged from `main` by then (my CSV commit landed in between), so this one needed a real
   merge, not a fast-forward — came through clean, no conflicts (disjoint files). Both scheduled
   runs' work is now on `main`.
2. **Committed the raw nflverse CSVs.** They were gitignored as "reproducible, not committed" —
   reasonable for a normal software repo, wrong call for a bot whose scheduled runs clone fresh
   every time and therefore never had the data. Removed from `.gitignore`, committed ~72MB
   directly. Re-ran `pipeline/fetch_data.py` + `pipeline/predictive_stats.py` from the committed
   files to confirm it still works end to end (exit 0, same row counts as before).
3. **Rewrote the Eagles entry with real depth**, filling in what the scheduled run's narrow
   "coaching change + one Saquon stat" pass missed: the **A.J. Brown trade to New England**
   (a bigger fantasy fact than the OC hire — completely missing from the first pass), the Wicks
   trade + Makai Lemon 1st-round pick, and the Jeff Stoutland O-line-coach departure.
4. **Revised `footybot-operating-prompt.md`** (version-date bumped 2026-06-30 → 2026-07-01,
   `## END` re-verified intact): STEP 2 now requires 3-5 substantial items per run instead of
   one ("depth over breadth" was my scoping mistake, not a bug); STEP 3 adds a mandatory
   checklist for every coach-tendencies entry (coaching/scheme + roster moves/trades + O-line +
   RB depth + QB room); STEP 0 now runs the pipeline unconditionally every run since the data is
   always present, instead of conditionally checking for an upload.

Brendan also said he may run this every other day going forward instead of weekly — noted, no
prompt change needed for that (it's a schedule/cadence setting, not a behavior change), but
worth watching whether coach-tendencies coverage (finite, ~32 teams) runs out of genuinely new
ground at that cadence faster than expected.

### 2026-07-01 (2nd run today) — Eagles coach-tendencies entry (highest-value queued item)
Focus this run: worked the single highest-value `queued` [TOPIC] from the idea-queue INBOX — a
full **Eagles** entry for `research/coach-tendencies.md`. Chosen (depth over breadth) because it
directly serves Brendan's stated pick-#4 plan (he wants a Saquon + Chase pairing) and was the
last-named open thread in the doc. Freshly re-verified via WebSearch this run (NOT reused from
last session's same-session answer): NFL.com, NBC Sports Philadelphia, ESPN, CBS Sports, SI/onsi,
Philadelphia Inquirer.

Key corrected fact: this is an **OC-only change** — Nick Sirianni is RETAINED as HC; Sean Mannion
replaces fired OC Kevin Patullo. Mannion is a **first-time playcaller who has never called plays
at any level** — so the whole entry is tiered B on scheme tendencies (stated intentions + lineage
inference, no observed sample), A only on the hard facts (the hire, Saquon's 2025 stat line, the
YPC splits, the RB-run-rate trend).

CRITIC-PASS this run:
- **Downgraded the "major bounceback" narrative to Speculative**, not a lean. The CBS Fantasy
  framing is real but it's preseason optimism resting on a first-time playcaller executing. Honest
  correlation-vs-causation read written into the entry: Saquon's 2025 dip (5.8→4.1 YPC) tracks a
  **yards-before-contact collapse (3.8→1.7)**, which implicates blocking/scheme under Patullo as
  much as his age-29 decline — the former is what new zone concepts *could* fix, the latter they
  can't. Mechanism plausible, conclusion Speculative. Told Brendan: strong RB1 on talent/role, do
  NOT pay a 2024-ceiling price.
- **Added two explicit failure modes** to the entry (first-time-playcaller risk; Hurts reportedly
  resisting the under-center shift / "rigid preferences") rather than a clean bull case.
- **Did NOT write** a Miami change off the "Patullo → Dolphins" tidbit (role unverified; our Miami
  entry has Slowik as OC) — logged to AUDIT_QUEUE to verify next run instead of guessing.

Idea-queue: marked the Eagles [TOPIC] thread **done**; the mock-draft dump stays `exploring`
(other [TOPIC] threads — Cowboys/Pickens, Rashee Rice status, Packers/Jacobs player-note — remain
queued for future runs).

BRANCH: forced onto `claude/modest-gates-4i3fc0` by the harness again (2nd consecutive scheduled
run off `main`) — see VERIFICATION LOG. Prior side branch was merged to `main` before this run so
memory was current; but the recurring force-fork needs a durable fix. Gmail still label-only, no
draft created — digest via push-notification + run output.

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
