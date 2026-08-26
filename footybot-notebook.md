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

- **2026-07-15 (SCHEDULED RUN) — pushed to harness branch `claude/gracious-darwin-8ryyjz` per BRANCH RULE.**
  At run start local branch `claude/gracious-darwin-8ryyjz` == `origin/main` == `2665625` → FRESH read confirmed.
  Harness assigned working branch **`claude/gracious-darwin-8ryyjz`** (per BRANCH RULE — did NOT fork/improvise; note
  the remote branch did not yet exist, so pushed with `-u` to create it). Commit touches `newsletters/**` + research/
  notebook/idea-queue and does NOT touch `footybot-operating-prompt.md`, so the auto-merge Action's guard should pass
  and FF `main`. Pushed with `git push -u origin claude/gracious-darwin-8ryyjz`, verified with
  `git ls-remote origin claude/gracious-darwin-8ryyjz` = branch HEAD (exact hash in this run's push notification +
  STEP 9 output). IF `main` has NOT advanced by next run, a manual `git merge --ff-only` into `main` is needed.
  Brain repo pushed separately (see CHANGELOG brain-sync line).
- **2026-07-14 (WEEKLY SCHEDULED RUN) — memory loop HELD (3rd fresh-read run); pushed to harness branch per BRANCH RULE.**
  At run start local branch `claude/busy-knuth-cqbu6n` == `origin/main` == `03c8dc3` (the 07-12 edition) —
  FRESH read confirmed (auto-merge Action + Brain PR kept the loop). This is the weekly Monday run
  (Jul 13 PT → 2026-07-14 edition; 07-13 had no separate run). Harness assigned working branch
  **`claude/busy-knuth-cqbu6n`** (per BRANCH RULE — did NOT fork/improvise). Commit touches
  `newsletters/**` + research/notebook/idea-queue and does NOT touch `footybot-operating-prompt.md`,
  so the auto-merge Action's guard should pass and FF `main`. Pushed with
  `git push -u origin claude/busy-knuth-cqbu6n`, verified with `git ls-remote origin claude/busy-knuth-cqbu6n`
  = branch HEAD (exact hash in this run's push notification + STEP 9 output). IF `main` has NOT advanced
  by next run, a manual `git merge --ff-only origin/claude/busy-knuth-cqbu6n` into `main` is needed.
  Brain repo pushed separately (see CHANGELOG brain-sync line).
- **2026-07-12 (SCHEDULED RUN) — memory loop HELD (2nd fresh-read scheduled run); pushed to harness branch per BRANCH RULE.**
  At run start local branch `claude/dreamy-hamilton-pqv8fm` == `origin/main` == `506eabc` — fresh read
  (the auto-merge Action + the Brain-integration PR #1 kept `main` current; no stale-memory problem this
  run). Harness assigned working branch **`claude/dreamy-hamilton-pqv8fm`** (per BRANCH RULE — did NOT
  fork or improvise). This run touches `newsletters/**` + research/notebook and does NOT touch
  `footybot-operating-prompt.md`, so the auto-merge Action's guard should pass and FF `main` to this
  commit. Pushed with `git push -u origin claude/dreamy-hamilton-pqv8fm`, verified with
  `git ls-remote origin claude/dreamy-hamilton-pqv8fm` = branch HEAD. Exact commit hash in this run's
  push notification + STEP 9 run output. IF `main` has NOT advanced by the next run, a manual
  `git merge --ff-only origin/claude/dreamy-hamilton-pqv8fm` into `main` is needed. Brain repo pushed
  separately to its own `main` (verified independently — see CHANGELOG brain-sync line).
 At run
  start, local branch `claude/modest-gates-0apgi1` == `origin/main` == `6d275c9` — i.e. the 07-08
  auto-merge Action DID persist prior work to `main`, so this run read FRESH memory (first scheduled
  run to do so; the "stale every day" problem is fixed). Ran STEP 0 pipeline; caught that
  `predictive_stats.py` overwrote `predictive-stats.md` (74-line loss of accumulated analysis) and
  restored it via `git checkout` (base correlations byte-identical — see AUDIT_QUEUE). Pushed this
  run to the harness-assigned branch **`claude/modest-gates-0apgi1`** (per BRANCH RULE — did not fork
  or improvise). Verified with `git ls-remote origin claude/modest-gates-0apgi1` = branch HEAD. The
  commit touches `newsletters/**` and does NOT touch `footybot-operating-prompt.md`, so the
  auto-merge Action's guard passes and it should FF `main` to this commit — restoring the loop for
  the next run. NOTE for verification: at push time `origin/main` was still `6d275c9` (Action runs
  async / may be disabled in-sandbox); if `main` has NOT advanced by the next run, a manual
  `git merge --ff-only origin/claude/modest-gates-0apgi1` into `main` is needed. Exact commit hash is
  in this run's push notification + run output (STEP 9).
- **2026-07-08 (interactive) — v3.2 + coverage ledger PROMOTED TO `main` (32b83e6→3208f57).**
  Root-caused the "same newsletter every day": `main` had not moved since 07-02, so every
  scheduled run read stale memory. Tonight's 11:04 run (the July 8 edition Brendan pasted) was
  force-pinned to `claude/modest-gates-sezye0` (a THROWAWAY branch) and never reached `main` —
  the documented recurring harness pin. So nothing accumulated and the bot repeated CMC/Rice/
  Nabers/CeeDee-Pickens. Fix: fast-forwarded my v3.2 work onto `main` from this interactive
  session (interactive pushes to `main` DO work; only scheduled runs are pinned). Verified:
  `git ls-remote origin main` = 3208f57.
- **DURABLE FIX INSTALLED 2026-07-08: auto-merge GitHub Action** (`.github/workflows/footybot-automerge.yml`).
  Brendan chose the auto-merge option. On push to any `claude/**` branch that touched
  `newsletters/**` (i.e. a completed scheduled run), it fast-forwards `main` to that branch —
  SO SCHEDULED RUNS NOW PERSIST TO `main` and the memory loop self-sustains. Safety rails kept:
  it NEVER auto-merges if `footybot-operating-prompt.md` changed (human must review prompt diffs),
  and it is fast-forward-only (never force-pushes, never auto-resolves a conflict — it fails loudly
  and the branch waits for a manual merge). NOTE: the Action only fires for branches cut from a
  `main` that already contains it, so runs from tonight forward are covered; tonight's already-
  stranded `claude/modest-gates-sezye0` predates it and won't auto-merge. That branch has a real
  Cowboys coach-tendencies entry + Miami/Patullo audit resolution worth hand-salvaging into `main`
  (offered to Brendan — it's a real 3-way merge now since main has moved, so notebook/idea-queue
  conflicts are likely; do it deliberately).
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
  - `research/rb-draft-timing.md` — **NEW 2026-08-26, pipeline-computed + permutation-tested.**
    Answers Brendan's "RBs are incredibly valuable in my league" theory at his four cutoffs
    (RB through rounds 2/4/6/8). Verdict: NOT supported — direction is consistently
    RB-favorable in the standings but nothing survives multiplicity (best family-wise p=0.071),
    and the higher-powered return test (N≈560 picks) finds no RB-vs-WR difference at equal
    draft cost in any window. Only near-significant result runs against the theory: R7-8 RBs
    bust 16% vs WR 5% (p=0.051). Rebuild: `python3 pipeline/rb_draft_timing.py`.
    **Gated on 2024 standings for a sharper answer — see AUDIT_QUEUE.**
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

- **[2026-08-26, OPEN] Missing 2024 final standings.** `inputs/league-history/league_finishes.csv`
  covers 2019-2023 + 2025 only, so every draft-vs-outcome analysis silently drops 10 of 70
  manager-seasons (`draft_builds.py`, `rb_draft_timing.py`). This is **standing ask #2 in the
  Brain inbox, now raised a third time** — the last 2024 upload was a draft page, not the
  standings page. Get the real 2024 Yahoo standings page, then re-run `pipeline/build_league_finishes.py`
  and `pipeline/rb_draft_timing.py`. This is the cheapest available power increase for the
  whole draft-strategy line of research.

Items to re-verify or upgrade once conditions change (network policy widens, real data arrives).

- **`pipeline/predictive_stats.py` OVERWRITES `research/predictive-stats.md` (data-loss bug).**
  Flagged 2026-07-09. STEP 0 says run the pipeline unconditionally, but `predictive_stats.py`
  truncates the file to just its own base-correlation output, destroying the accumulated
  positional-stability (07-03) and positional-retention (07-07) sections that Lane A/deep-dives
  added below it. This run caught the 74-line deletion and restored via `git checkout` (base
  correlations were byte-identical, so nothing from the regen was lost). REAL FIX: make the script
  write its output between sentinel markers (e.g. `<!-- AUTOGEN:predictive-stats START/END -->`) and
  preserve everything outside them, OR write to a separate `predictive-stats-base.md` the manual
  analysis includes/links. Until fixed, every scheduled run must `git checkout research/predictive-stats.md`
  after the pipeline step if it doesn't intend to shorten the file. Low-risk to fix; do it in a
  reviewed session (touches a pipeline script).
- ~~**Bucky Irving & Javonte Williams ADP conflicts**~~ **RESOLVED 2026-07-12:** Bucky ~50 (40-55, A;
  old ~25 predated shoulder surgery), Javonte ~35 (30-42, A; DAL RB1). Formerly-unsourced also DONE
  2026-07-12: James Conner ~177 (cratered, Love landing), Ladd McConkey ~48-56, Rome Odunze ~53-63,
  Jerry Jeudy ~140-200 (ranking≠ADP trap). All on the board.
- **Dedupe/verify the 07-08 salvaged research union.** IN PROGRESS: `coach-tendencies.md` **Miami
  triplication CONSOLIDATED 2026-07-12** (3→1). **"Not yet covered" section DE-DUPLICATED 2026-07-14**
  (it had ~6 `git merge --union` copies of one paragraph + stray repeated fragments; rewritten clean,
  all RESOLVED notes + open leads preserved). **STILL PENDING: Dallas Cowboys 5-entry body-merge.**
  The 5 stacked `### Dallas Cowboys` entries (now at roughly lines 308 / 357 / 398 / 465 / 545 after
  tonight's edits — re-grep before editing) need a lossless 5→1 merge in a REVIEWED session. Did NOT
  attempt tonight: an atomic multi-hundred-line Edit surgery on the 55KB canonical file is fragile to
  run unattended (transcription-mismatch risk), and prior runs also deferred. **UNIQUE-FACT LIST to
  preserve (compiled 2026-07-14 so the merge is fast + safe):** entry-5 (lines ~545-611, dated 07-03)
  is the most complete → use as the base and fold in the few facts only the others have: (a) the 2025
  shared-season stats TABLE (Pickens 137 tgt/23% share, ~34% RZ / 93/1,429/9, WR5 PPR; Lamb 117/75/
  1,077/3, WR19 half-PPR / WR15 per-game); (b) the [S] pipeline cross-check (Pickens WR6 14.44 PPG /
  Lamb WR11 12.57 PPG / Dak QB5 22.0 PPG, from league-scoring-leaders.md); (c) Jake Ferguson
  front-loaded note (TE1 thru Wk7, TE22 after; 82 tgt); (d) Lamb 2023 sole-alpha baseline 135/1,749/12
  + 19.7% deep-route rate + slot-vs-X role detail; (e) the ~46%/54% career run/pass split; (f) the
  Chase-Higgins '25 and ARSB-Williams '25 coexistence comps; (g) the O-line "275 of 1,186 snaps
  together" figure; (h) the confound flag (3 of Lamb's missed games fed Pickens' counting stats).
  Everything else across the 5 is redundant. `predictive-stats.md` may still have 1-2 cosmetic
  duplicated table rows from the union.

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

### 2026-08-26 (INTERACTIVE, Brendan-directed) — RB-early-draft theory TESTED against 7 years of our own boards: NOT supported
Brendan asked directly: *"I have a theory RBs are incredibly valuable in my league — does drafting more RBs early
translate to success?"*, at four cutoffs (RB count through rounds 2/4/6/8). New: `pipeline/rb_draft_timing.py`
(stdlib, permutation-tested) + `research/rb-draft-timing.md`.
- **Verdict: undetectable, not disproven — and definitely not "incredibly valuable."** Two tests. (1) ALLOCATION
  (N=60 scored manager-seasons): all four RB cutoffs have the theory-friendly sign, WR mirrors all point the other
  way — but the best of them (RB@6 vs points-for, r=+0.298) has family-wise p=0.071 once you account for having
  tried four cutoffs. Nothing clears 0.05. (2) RETURN (N≈560 rounds-1-8 skill picks, our scoring on real nflverse
  weeks): **at equal draft cost, RB and WR have returned the same in every window** — R1-2 gap +9.5 VOR p=0.50,
  R3-4 +4.7 p=0.70, R5-6 -6.2 p=0.60, R7-8 -14.1 p=0.22.
- **Only near-significant finding is the OPPOSITE of the theory: R7-8 RBs bust (<50 pts all season) 16% vs WR 5%,
  p=0.051** (R5-8: 14% vs 6%, p=0.063). Same mean return late, much fatter left tail.
- Suggestive but unbankable: 5 of 6 champions had exactly 3 RBs through round 6; the RB@8 pattern *reverses* above
  3 (3 RBs by R8 = best cell, 4 = worse), so the shape is a hump, not "more is better."
- **Counter-story worth remembering before we lean RB on Aug 28:** Jack is the league's ONLY WR-first drafter
  (lowest RB@2, 0.83) and has the best mean finish (3.50). Across the 10 managers, career early-RB lean correlates
  *positively* with mean rank (r=+0.40 at RB@2 — RB-heavy crowd finishes slightly worse). N=10, so noise, but it
  kills "the RB-first drafters are the winners here" as a clean story.
- **Draft-day posture written into the research doc:** at #4 take the best player (if that's the RB, fine — but
  because he's the best player, not for a positional premium that isn't measurable); R3-4 position-agnostic; stop
  force-feeding RB from round 5.
- **BLOCKER on sharpening any of this: no 2024 standings on file.** 2024's drafts exist but are dropped from every
  join (60 of 70 manager-seasons scored). Getting the 2024 Yahoo standings page is the single cheapest way to
  improve every number here. → AUDIT_QUEUE.

### 2026-07-15 (SCHEDULED RUN) — Newsletter 2026-07-15; Walker→KC board correction (caught via take-check) + QB-wait math [S] + pick-4 tree + 2024 media retro
Fresh read (branch == origin/main == 2665625 at start). 44 days to draft. **Lane A run by orchestrator vs the
pipeline; Lanes B/C/D as 3 parallel subagents + reviewer (all 4 lanes ran, none skipped).** Compete mode did NOT
fire. Newsletter: `newsletters/2026-07-15.md`.
- **Headline / Lane C (winning lane): the pick-4 decision tree.** JT ≥ Chase; national ADP says Chase goes ~3rd but
  our RB-lean room slides him to 4 more often → if Chase gone take JT (zero rec-haircut workhorse), if Chase falls
  take Chase (only WR that beats the haircut), wildcard Achane. The countdown deliverable, 44 days out.
- **Biggest catch / reviewer verification: KENNETH WALKER IS A KANSAS CITY CHIEF, not a Seahawk [A, 6 sources].**
  The run's own lane briefs AND `player-board.md` had him stale as a Seahawk; grounding the Walker take-check (KNOW-
  CURRENT-REALITY discipline) surfaced the March FA signing (3yr/$43.05M). Corrected both board rows + Pacheco (now FA).
  This ALSO validated Brendan's 2026-07-01 take ("Chiefs, heavy usage") — he was ahead of us. Caveat logged: market
  already priced it to early-2nd (analysts call steep; Mahomes pass-funnel = high-end RB2, not workhorse).
- **Lane A / Data [S]:** full 2025 QB spread in his exact scoring. QB6→QB18 = only ~4.2 ppg across 12 QBs; edge is in
  the top ~3. Our streamer names (Caleb Williams QB9 21.8, Bo Nix QB13 20.9) already QB1-adjacent → wait & stream QB
  unless a top-3 falls. Written into `league-scoring-leaders.md` (reconciles the old "waiting is costlier" line).
- **Deep dive / Lane D:** queued media-narrative retro on Brendan's **2024 draft** (backlog: 2024 now DONE). Winning
  half of the lens replicates emphatically (Mahomes R5 = cleanest wheelhouse; Achane R2 = the receipt vs the "2nd-year
  bust" myth — polarizing/"Case Against"/BR "bust to avoid" → league-winner); NO paid-for-hype bust in 2024 (Brooks
  R10 = on-process injury-discount pick killed by a re-torn ACL, opposite of BTJ). Reframes BTJ-2025 as the deviation.
  **Refined the lens language: "manufactured discount" → "buys AGAINST the prevailing negative narrative"** (Achane/Nico
  were expensive — it's the narrative, not the price). Written into `self-scouting.md`.
- **Lane C / Market:** AJB ADP reconciled (board had both "16" and "32" → ~25, range 22-32, WR8-13, rising). Risers:
  Q.Johnston ~78/WR37 [A], Rodgers up ~2 rds, R.White ~109, Brooks lead back (craters Hubbard). Fallers: Conner ~177,
  Kamara ~152, Aiyuk (relative only). Jeanty volatile ~10-22. New ~180 darts: Adonai Mitchell ~176, Greg Dulcich
  ~185-194 [A], Shough, Okonkwo ~146, Flournoy ~168, Jordan James (CMC handcuff). Killed garbled "Alec Downs."
- **Lane B / News:** genuinely quiet pre-camp lull (first reports ~Jul 22). Nabers tone up (Harbaugh "on schedule,"
  ~Wk3 debut floated — still PUP start); Diggs 5-team interest (watch); Montgomery "three-down" color (freshness
  unconfirmed → held B); IDP blank (Parsons PUP, old). Killed: no fresh Rice/Jacobs/Mahomes movement.
- **Checking your takes:** Kenneth Walker → **RIGHT, and ahead of us** (see catch above); only caveat is price.
- **Reviewer:** caught the stale Walker board fact (the headline correction); reconciled the AJB "16 vs 32"
  contradiction rather than leave both; held QB finding as 2025-actuals-not-projections + noisy low-games QBs; did NOT
  overstate Nabers (still PUP) or Montgomery color (freshness). Killed garbled "Alec Downs."
- **Pipeline note (AUDIT_QUEUE, unchanged bug):** `predictive_stats.py` again OVERWROTE `predictive-stats.md` (−74 ln);
  caught it, restored via `git checkout` after confirming base correlations byte-identical (74 del / 0 add). Still needs
  the sentinel-marker fix in a reviewed session.
- **brain-sync:** READ done (only FF-relevant CONFIRMED_RULE = Gmail-drafts-only, obeyed; no open FF queue tasks/
  answered questions). WRITE done (block appended to brendan_brain `queue/inbox/from-footybot.md`, pushed separately —
  see VERIFICATION LOG / brain-sync line).

### 2026-07-14 (WEEKLY RUN) — Newsletter 2026-07-14; self-scouting "discount vs hype" lens + 2025 media-narrative retrospective; Waddle re-priced; Falcons QB + coach-tendencies cleanup
Weekly Monday run (first since 07-12). Fresh read (branch == origin/main == 03c8dc3). 45 days to draft.
**Lane A run by orchestrator against the pipeline; Lanes B/C/D as 3 parallel subagents + reviewer (all
4 lanes ran, none skipped).** Compete mode did NOT fire. Newsletter: `newsletters/2026-07-14.md`.
- **Headline / Lanes A+D (winning lanes): decoded Brendan's OWN 2025 draft.** Pairing his real
  pick-value deltas [S, `draft_outcomes.py`] with draft-time media narratives [B, WebSearch] → clean
  pattern at the extremes: HITS = "manufactured discount + catalyst" (Mahomes R10 = active fade
  narrative; Davante R6 +73.9 = age-discount + Stafford; Walker R4 +56.2 = timeshare-discount + Kubiak),
  MISSES = "paid-up on consensus hype" (**BTJ R2 −142.0 = his worst pick ever**; Bigsby R7 −77.6
  overpaid vs ADP). Reframes his edge as PRICE DISCIPLINE buying manufactured discounts, not any
  age/position leak. Written into `self-scouting.md` (new "unifying lens" section + 2025 retrospective).
  Delivers the queued [TOPIC] "media narratives on drafted players" (2025 started; 2024 next).
- **Deep dive / Lane D:** per-player 2025 draft-time media narrative (BTJ WR8/2000-yd hype, Jeanty
  RB6 "smash," Walker/Davante/Mahomes discount cases, Bigsby/Kraft/Sutton lighter) — receipts + outlets.
- **Lane C / Market:** **Waddle re-sourced as a Bronco → ~39-53 (WR19-21), co-WR1 w/ Sutton under Bo
  Nix** (not a runaway alpha). Pushed deep board to ~180: Warren ~78, Dowdle ~90, Caleb Williams ~98,
  Gainwell ~100, Bo Nix ~107, Keon Coleman ~120, **Josh Downs ~123 (value)**, Ferguson ~127, Goedert
  ~136, Spears ~142→155 (IR-bound), Kamara ~152, **Tank Bigsby ~166 (now a PHI Saquon handcuff)**.
  QB-streamer tier ~95-110 forming (6pt-pass edge). Risers: AJB No.16, JSN, Gainwell, Pollard(Spears IR).
  Fallers: Hubbard (Brooks lead back), Kamara, Conner. Still no direct Sleeper (JS-hidden).
- **Lane B / News:** quiet camp-eve week. Mover: **Nabers opening camp on PUP** (2nd knee scope, Oct
  debut in play — injury discount; he's Year 3). Risk trio firmed not resolved (Rice/Jacobs/Mahomes).
  Vikings QB O'Connell noncommittal [B] → JJ stays firmer-not-lock. Killed: Olave (no July update),
  Bijan ext (non-event), no new suspensions.
- **Checking your takes:** **"Drake London — real QB now?" → HALF-RIGHT.** Role ($141M ext) + coaching
  (Stefanski/Rees) real upgrades; "real QB" shaky — **open Penix(ACL)/Tua competition**, not settled.
  Corrects our stale "Penix vs Cousins." ("McDaniel merchant" frame wrong — he's LAC OC now.)
- **Housekeeping DONE:** corrected the **Falcons entry** (Penix-ACL vs Tua open battle + London $141M);
  **de-duplicated the badly-unioned "Not yet covered" section** of coach-tendencies.md. **Dallas 5→1
  body-merge STILL PENDING** — compiled the unique-fact list into AUDIT_QUEUE so a reviewed session can
  do it fast/safely; did not risk a fragile unattended surgery on the canonical file.
- **Reviewer:** capped the self-scouting headline at "directional, n=16"; kept BTJ as a *process*
  lesson not a 2026 downgrade; re-aged Jeanty (sophomore volume bet ≠ BTJ narrative leap); held the
  Vikings QB item as single-source; flagged Waddle's Sleeper number as secondhand. Did NOT lead with
  aging-vet/mid-QB "superpowers" (Davante/Mahomes appear as discount EXAMPLES, not standalone claims).
- **Pipeline note (AUDIT_QUEUE, unchanged bug):** `predictive_stats.py` again OVERWROTE
  `predictive-stats.md` (−74 ln); caught it, restored via `git checkout` after confirming base
  correlations byte-identical. Still needs the real sentinel-marker fix in a reviewed session.
- **brain-sync:** READ done (only FF-relevant CONFIRMED_RULE = Gmail-drafts-only, already obeyed; no
  open fantasy_football queue tasks or answered questions to apply). WRITE done (block appended to
  brendan_brain inbox, pushed separately — see VERIFICATION LOG / brain-sync line below).

### 2026-07-12 (SCHEDULED RUN) — Newsletter 2026-07-12; board rebuilt on [S] his-scoring numbers; 2 ADP conflicts + Miami dedup resolved
First run since 07-09 (07-10/07-11 did NOT run — 3-day gap; not stranded, just absent). At run start
local branch `claude/dreamy-hamilton-pqv8fm` == `origin/main` == `506eabc` → read FRESH memory (the
auto-merge Action + Brain-integration PR held the loop). 47 days to draft. **Lane A run by orchestrator
directly against the pipeline; Lanes B/C/D as 3 parallel subagents + reviewer (all 4 lanes ran, none
skipped).** Compete mode did NOT fire. Newsletter: `newsletters/2026-07-12.md`.
- **Headline / Lane A [S]:** replaced the board's tier-C half-PPR estimates with pipeline-computed
  **2025 regular-season PPG in his exact scoring** for ~40 players (0.5/rec, 6pt pass TD, −2 TO; 40yd
  bonus still uncomputable). Validated against prior [S] anchors (CMC 21.51, Puka 19.41, JSN 17.67,
  Saquon 13.36, CeeDee 12.57, JJ 9.38 — all byte-match). Findings: 2025 top-6 in his scoring = 5 RBs +
  Puka; ½-haircut = exactly 0.5×rec/g (Henry −0.44 … Puka −4.03); deep-board WR darts (MHJ 8.94, BTJ
  8.20, Worthy 6.35, McConkey 9.24, Jeudy 5.63) ALL <10 PPG in 2025 → price as 2026-leap bets. Written
  into `player-board.md` as a new [S] section. Reviewer caveat: one-season snapshot, not a law.
- **Lane C / Market:** RESOLVED both standing ADP conflicts — Bucky Irving ~50 (40-55, A; old ~25
  predated shoulder surgery), Javonte Williams ~35 (30-42, A; DAL RB1, market calls him expensive).
  Sourced ~11 new deep-board names (Kittle ~40, McConkey ~48-56, Odunze ~53-63, LaPorta ~59, Pollard
  ~64, Pacheco ~69, Hockenson ~79, Njoku ~83, Charbonnet ~96). **James Conner CRATERED to ~177**
  (ARI drafted Jeremiyah Love 3rd overall). **Jeudy ranking≠ADP trap flagged** (ESPN rank ~WR47 vs real
  ADP ~140-200). No Sleeper (JS-hidden, honestly flagged — nothing fabricated).
- **Lane B / News:** quiet camp-eve window (real camp news ~Jul 22-28). MOVER: **Kyler Murray signed
  MIN + projected starter over McCarthy [A]** → firms the JJ buy-low (reviewer held it "firmer" not
  "lock"). Fresh: Brandon Aiyuk headed for SF release (undraftable, ACL). Sharpened: Olave's real risk
  is the Dec-2025 lung blood clot clearance, not the contract. IDP: James Pearce Jr 8+ game susp.
- **Lane D / Rabbit hole:** Miami audit (already resolved 3× — I mis-scoped it) RE-CONFIRMED A-tier and
  produced current Achane data: **4yr/$64M extension** (3rd-highest-paid RB) = high FLOOR, but Willis
  QB + worst-WR-room + goal-line vulturing CAP the ceiling → refined board from "boom/bust" to
  "high-floor/capped, value-only-if-slides, not a pick-4 target." Deep dive.
- **Checking your takes:** "James Conner — cool opportunity vs Jeanty" → **REFUTED** (Love drafted 3rd
  overall, Conner buried + cratered to ~177; Jeanty is the cleaner bet). Take went stale on draft capital.
- **Housekeeping DONE:** consolidated the **triplicated Miami entry** in coach-tendencies.md → 1 canonical
  entry, lossless (677→660 ln). **Board correction:** Jaylen Waddle was listed as a Dolphin — he's a
  **Denver Bronco** (traded March 2026); fixed on the board, ADP to re-source.
- **Reviewer kills:** held Murray→JJ as firmer-not-locked; tagged Conner ~177 B/directional; flagged
  Jeudy ranking≠ADP; used Clay-rank names as ordering only; did NOT assert "Tua→Atlanta" (unverified);
  caveated "5 of top 6 are RBs" as one-season snapshot.
- **Pipeline note (AUDIT_QUEUE, unchanged bug):** `predictive_stats.py` again OVERWROTE
  `predictive-stats.md` (−74 ln); caught it, restored via `git checkout` after confirming base
  correlations byte-identical. Still needs the real sentinel-marker fix in a reviewed session.
- **brain-sync:** READ done (version 1.0.0 match; CONFIRMED_RULES all consistent with prompt, no
  conflicts; no fantasy_football queue tasks or answered questions to apply). WRITE done (block appended
  to brendan_brain inbox, pushed separately — see VERIFICATION LOG).

### 2026-07-09 (SCHEDULED RUN) — Newsletter 2026-07-09; builds-that-win + QB-environment; board pushed to picks 100+
First scheduled run reading a fresh `main` (auto-merge Action worked: local branch == origin/main
== 6d275c9 at start; the memory loop is finally self-sustaining). 50 days to draft. All 4 lanes ran
as parallel subagents (NOT fallback) + reviewer. Compete mode did NOT fire. Newsletter:
`newsletters/2026-07-09.md`.
- **Headline / Lane A (winning lane): "which BUILD wins" — WATCHLIST #1, now DONE.** New
  `pipeline/draft_builds.py` + Finding 7 in `draft-tendencies.md`. 60 manager-seasons (2019-23,25).
  Verdict: mostly a wash; RB-heavy opens best (RB-RB N=18, mean rank 4.67, 50% top-3), Zero-RB worst
  (N=5, 0% top-3, too thin) — but the edge is INSIDE the noise band and can't be separated from pick
  quality (draft-value→rank only r≈+0.31, Finding 6). Reported as a weak tiebreaker that gently
  REFUTES Brendan's "RBs overvalued, scrounge a WR" premise, NOT a law. His own history: best finish
  (3rd '21) = only RB-RB open; worst PF ('23) = WR-WR-WR Zero-RB.
- **Deep dive / Lane D: QB-environment regression — WATCHLIST item, DONE.** New
  `research/qb-environment.md`. Brissett/ARI 2025 = computed NFL-top 649 att / 63.9% rate, ~10pt
  franchise outlier (garbage-time: 1-11, def last, Conner 3 gms, MHJ hurt) → FADE the counting stats:
  McBride (still TE1, but 169 tgt won't repeat — explains our board's TE crater), Michael Wilson
  (AVOID, purest rider), MHJ (QB-capped bounce-back). ANTI-FADE flag: do NOT fade Chase for "Bengals
  volume regression" — 185 tgt / 1,412 with Burrow out 9 games = own-role. Also DeVonta up / NE
  incumbents down. Stale-premise fix: Murray released, Brissett IS the 2026 starter (regression from
  run game + defense, not from Brissett sitting).
- **Market / Lane C: real ½-PPR ADP, rounds 2-6 + into pick 100+** (BTJ ~64, C.Watson ~73, Worthy
  ~101 — closes Brendan's "stop capping at BTJ/C.Watson" complaint). Written into `player-board.md`.
  Honest limit: Sleeper per-player #s are JS-hidden + WebFetch blocked, so could NOT anchor on
  Sleeper — most rows tier B (single ESPN mock), a few tier A (Underdog aggregate). Did NOT fabricate.
- **News / Lane B: quiet camp-eve week.** Kyler Murray released (A) + Vikings interest (B, → JJ
  tailwind if real); Bijan extension "expected" (report not signed); Jameson Williams camp buzz;
  Olave hold-in friction; Jacobs legal unchanged.
- **Checking your takes: "Bucky Irving = Liam Coen merchant" → REFUTED [S].** Coen left for JAX HC
  after 2024; Grizzard ran 2025. Irving held 12.35 PPG w/o Coen vs 12.99 with (pipeline). Talent
  traveled. Real caution = shoulder procedure + 3rd playcaller in 3 yrs + snap-share, not the scheme.
- **Reviewer kills:** overruled Lane C's "Henry @18 trap" (contradicts our board — he's a ½-PPR
  riser in THIS scoring); held Bucky/Javonte ADP unresolved (source conflicts, no number committed);
  tiered board B (no Sleeper, didn't fabricate); refused to make builds a law; Murray→MIN kept as B.
- **Pipeline note (see AUDIT_QUEUE):** `predictive_stats.py` OVERWRITES `predictive-stats.md`,
  wiping the accumulated positional-stability (07-03) + positional-retention (07-07) sections. Caught
  it (74-line deletion), restored via `git checkout` after confirming the base correlations were
  byte-identical. Logged for a real fix.

### 2026-07-08 (interactive, follow-up 2) — Salvaged 7 stranded nightly runs (07-02→07-08) to main
All seven nightly runs since main froze (07-02) had branched off the same frozen `main` in
PARALLEL and stranded on `claude/modest-gates-*` branches — main had ZERO newsletters (only a
README), so the bot never saw its own prior editions (a major repeat driver on top of the missing
ledger). Recovered everything WITHOUT touching the v3.2 prompt / player-board / self-scouting /
notebook:
- **All 7 newsletters** (`newsletters/2026-07-02.md` … `07-08.md`) → main now has the record of
  what's been covered, so "don't repeat yesterday" finally has a yesterday.
- **4 new pipeline scripts** (positional_value, positional_stability, player_season_profile,
  positional_retention) + **3 new research files** (positional-value.md, player-profiles-2025.md,
  league-scoring-leaders.md) — pure additive, unique filenames.
- **Unioned the shared research** each night had extended from the same base (`git merge-file
  --union`, lossless): coach-tendencies.md (7 nights → 677 ln), draft-tendencies.md (4 → 403),
  predictive-stats.md (2 → 101), player-notes.md (2 → 159). mock-draft-2026.md = took latest
  (07-08). Verified: no conflict markers; only cosmetic dups are markdown table separators.
- Two 07-08 runs existed (sezye0, f1u7kg); took sezye0's newsletter + unioned f1u7kg's coach
  entries. Nothing from any night was dropped.
The auto-merge Action prevents this recurring from tonight forward.

### 2026-07-08 (interactive session, follow-up) — v3.2 overhaul: fixed the stale/lazy newsletter
Brendan came in hot: the nightly output was repetitive (debated CMC / CeeDee-vs-Pickens / Rice &
Jacobs lawsuits every night), used self-fabricated ADP that capped at ~pick 100 (BTJ/Christian
Watson), obsessed over a small-sample "aging vets" read, mis-applied a "second-year leak" to
sophomores, and argued current-reality facts wrong (claimed Philly a good AJB environment "they won
a SB" — the Eagles OFFENSE struggled last year and AJB was TRADED to New England; treated a
Montgomery trade as "upside" when he was already dealt to Houston — WebSearch-confirmed this run).
He revised the plan then said full send. Reviewed PATH-B prompt edit + two new research files:

1. **Prompt → v3.2** (`## END` verified, rails untouched). Six changes: (a) COVERAGE LEDGER is law
   (`research/player-board.md` with last_covered/times_covered/WATCHLIST/SETTLED — never re-lead a
   covered player/news item unless something moved); (b) BOARD DISCIPLINE — advance DOWN the board
   to his real pick slots (4,17,24,37,44,51,64,71,84,91…) and out to ~pick 180, stop parking on the
   top 12; (c) Lane C = REAL multi-source half-PPR ADP anchored on Sleeper (+FantasyPros/Underdog/
   RotoWire), never fabricated, mark stale/unknown if unsourced; (d) PATTERN ALARM recalibrated —
   no leak/superpower without pick-list + sample size, re-age players to current season, stop the
   obsessive repetition, anti-yes-man on data he sends; (e) KNOW CURRENT REALITY + don't manufacture
   pushback (the Eagles/AJB + Montgomery lessons, in STEP 3C); (f) STEP 7 maintains the ledger.
2. **`research/self-scouting.md`** (new, supersedes draft-tendencies Finding 5's framing) — receipts
   from `draft_history_enriched.csv`: the "second-year leak" is a MYTH (his year-2 picks are ~a coin
   flip and include A.J. Brown '20, Waddle '22, Achane '24, Olave '23 = some of his best ever); the
   REAL narrower leak is expensive POST_INJURY (Kupp 1.05, CMC, Sutton, Freeman, Fuller); aging-vet
   "4-for-4" and mid-QB "superpower" are late-pick n≈3-4 footnotes to stop obsessing over.
3. **`research/player-board.md`** (new, the coverage ledger + v1 board) — all 25 of his mock players
   rescored to 0.5 PPR (tier C, my arithmetic on his projections): reception-hogs crater (ARSB
   ~320→~245, McBride ~250→~200, CeeDee, JSN, London, Chase), pure runners rise (Henry, Jonathan
   Taylor, Jeanty, Saquon). WATCHLIST seeds the real gaps (builds-that-win study, picks 100-180,
   QB-regression layer, CeeDee splits, real ADP); SETTLED seeds the anti-repeat list.

CONCEDED to Brendan (logged so the bot learns): AJB/Eagles current-reality error; pushing back on
CeeDee for no reason; treating his MOCK ORDER as his rankings (he asked me to HELP rank); dinging
his back-and-forth notes as contradictions when they're just pros/cons to synthesize. Still on the
side branch `claude/fantasy-football-discussion-nawczx` — needs merge to `main` before it helps a run.

### 2026-07-08 (interactive session) — Sparred Brendan's ChatGPT "2026 Draft Brain" doc
Brendan pasted a long ChatGPT-authored draft-strategy summary and asked me to pressure-test it
("mental spar, pushback encouraged"), NOT to build anything. He explicitly declined the top-75
table. Value to persist = the critical framings, which sharpen the newsletter reviewer /
"checking your takes" lane. No prompt edit made (these are memory, not new operating rules — a
behavior change would go through the prompt with a diff review). The six that survived scrutiny:

1. **IDP is over-invested for what it is: ONE streamable roster slot.** The lineup has a single
   "D" (IDP-scored) starter. `research/idp-evaluation.md` + Parts 2-3 of the doc spend huge
   analytical energy reverse-engineering "number-1-overall edge molds" for a slot you draft late
   and stream all year — and our own `predictive-stats.md` (tackle rate r=0.506 sticky, sack rate
   r=0.091 not) says the position is streamable by design. Correct prep: draft it late, stream the
   matchup, reallocate effort to the two FLEX spots + RB depth. Flag any future run (or Brendan
   take) that treats the one IDP pick as a marquee decision.
2. **"Mid-round QB is my superpower" is n=3 survivorship — bank the market inefficiency, not the
   self-narrative.** Finding 5 has Lamar '22 / Mahomes '24 / Herbert '23 as his 3 best picks ever,
   which is real, but 3 hits over 7 years of mid-round QB stabs ≈ base rate + memory of winners.
   The REPEATABLE edge is the structural one we already measured: the league under-drafts QB vs.
   6-pt passing TDs (first-QB round 7.7→6.3 then relaxed to 7.1 — edge shrank, didn't close).
   Frame it as "the pocket exists," not "I'm the guy who hits it."
3. **Post-injury 0-for-6: the leak is PRICE discipline, not the archetype.** Buying injury
   discounts is +EV in aggregate (market overreacts); his misses came from paying near-full price
   and/or the role not surviving. The PATTERN ALARM should fire on "full price for an injury/2nd-
   year STORY," not on the mere presence of the archetype — otherwise it wrongly dings genuinely
   good injury buys. Real test per player: does the role survive if the body does, and is the
   market pricing the injury twice?
4. **Don't over-frame the scoring as exotic.** Half-PPR + 6-pt pass TD + big-play bonuses is a
   common home-league setup, not a fingerprint. Believing it's exotic is how you rationalize
   reaches off consensus. The real edges are behavioral (room tendencies) + discipline; scoring-fit
   is a marginal tiebreaker worth ~half a round, not the alpha.
5. **TD-rate contradiction still live in the doc's archetypes.** `predictive-stats.md` says TD rate
   is noise, yet the doc's WR/RB checklists still ask "10+ TD path" / "TD hammer." Reframe every
   "TD path" bullet as "owns the volume/red-zone ROLE that produces TDs" — role projects, rate
   doesn't. Newsletter should catch this when Brendan's takes lean on last year's TD total.
6. **"Stress-tested lens vs. generic rankings" is a false binary.** The lens is a filter +
   discipline layer applied ON TOP of a calibrated consensus baseline, not a replacement. Deviating
   from consensus without a concrete room-behavior or stable-role reason IS the failure mode. His
   own sharpened one-liner: start from consensus, deviate only for a concrete reason, never because
   the story is fun.

Affirmed as his genuine alpha (already in `draft-tendencies.md`): the room model + self-scouting,
not the scoring or archetypes. Draft date still Aug 28; all specific name/ADP lists in the doc are
July snapshots and disposable — the method is the asset.

### 2026-07-02 (interactive session, follow-up 3) — Final standings + the decomposition
Brendan sent 7 standings MHTMLs (6 usable; 2024 was accidentally a draft page — re-send
requested). Built `pipeline/build_league_finishes.py` → `league_finishes.csv` (60
manager-seasons, 0 unmapped) and Finding 6 in draft-tendencies.md, honoring his explicit
caveat ("it's not all about draft… so much nuance behind picks"): we DECOMPOSED instead of
claiming causation. Measured: draft value → points-for r≈+0.50; PF → rank +0.59; draft value →
rank only +0.31; in-season move COUNT → rank +0.03 (noise; count ≠ quality — transaction logs
requested to measure quality). 2 of 6 champions won with below-median draft value. Finishes:
Jack best sustained (3.5 avg), Dylan 2 titles incl. 2025, Brendan 8th of 10 (6.7 avg, 0
titles, 1 top-3) — his draft-value leak and his standings are consistent, though his 3rd-place
2021 with a busted draft shows real in-season skill. CRITICAL-THINKING PRINCIPLE added to the
operating prompt's reviewer step (outcome ≠ strategy quality; decompose; name confounds).
Prompt remains v2026-07-02b lineage; `## END` verified.

### 2026-07-02 (interactive session, follow-up 2) — Outcomes, QB trend, narratives, memory rule
Brendan's asks, all delivered or wired into the routine:
1. **Which habits WIN** → `pipeline/draft_outcomes.py` + Finding 5 in draft-tendencies.md.
   League-wide: STEADY is the only strongly positive archetype (+20.9/pick); POST_INJURY is
   the worst (33% hit). Leaderboard: Niko +26.1 and lucas +20.4 best; Dylan hottest recent
   (75% hit 2024-25); Nate coldest recent (-30.1). Brendan: 52% hit but -7.0 avg — frequent
   singles, catastrophic strikeouts, and the strikeouts cluster in exactly his signature
   habits: POST_INJURY 0-for-6 (-46/pick) and SECOND_YEAR busts (BTJ '25 -142 = his worst
   ever). His superpower: mid-round QBs (Lamar '22 +127, Mahomes '24 +110, Herbert '23 +88 =
   his 3 best picks ever) + aging vets 4-for-4.
2. **"League catching on to QBs?"** → tested: first-QB avg round 7.7→6.3 across 2019-2024
   (real acceleration in '23-'24), relaxed back to 7.1 in 2025. Edge shrank, didn't close.
3. **Media narratives, not just stats** → standing MEDIA-NARRATIVE LAYER in the prompt
   (current coverage labeled as narrative + slow-burn retrospective on historical picks,
   2025-weighted) + ACTIVE QUEUE item.
4. **Recency weighting** → 2025 heaviest for habit claims, in prompt + outcomes script.
5. **"Get in my brain / call out good vs bad"** → PATTERN ALARM added to checking-your-takes:
   flag when his live takes fit a losing archetype (Egbuka/MHJ/Worthy = post-injury pattern),
   reinforce when they fit a winning one.
6. **"Continuously add to memory"** → STANDING MEMORY RULE in STEP 7: anything sent/learned
   gets committed same-session; nothing lives only in chat.
7. **True standings correlation** → blocked on data we don't have; requested final-standings
   MHTMLs from Brendan (idea queue, PENDING FROM BRENDAN).
Prompt bumped to v2026-07-02b, `## END` verified.

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
