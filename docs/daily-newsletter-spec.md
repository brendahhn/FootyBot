# FootyBot Daily Newsletter — spec (v1, 2026-07-02)

Agreed with Brendan via interview 2026-07-01 (two rounds of questions). This is the plan the
operating prompt (`footybot-operating-prompt.md` v2026-07-02) executes. Change this spec and
the prompt together, in a reviewed session, per `safe-bot-edits`.

## The product

A **daily morning newsletter** — full-analysis length (10+ min read), written overnight
(routine fires ~11:30pm PT nightly; Brendan set the schedule in his routine settings), dated
for the following morning, with everything in service of one goal: **win the league**
(draft: Aug 28, 2026, pick 4 of 10; scoring quirks: half-PPR, 6pt passing TD, -2 turnovers,
40+ yd bonuses, 1 flex IDP — see CONTEXT.md).

### Delivery (decided, with fallback history)
- **Primary: repo file** — `newsletters/YYYY-MM-DD.md` (dated for the morning it's read).
- **Plus: push notification** with the 3-5 headline findings and the file path.
- **Gmail: broken for routines right now** — scheduled runs twice received a label-only Gmail
  connector (no compose/draft). Diagnosis given to Brendan: reconnect Gmail in claude.ai →
  Settings → Connectors with full permissions. Each run makes ONE quick ToolSearch check for a
  compose tool; if it ever appears, ALSO deliver as a Gmail draft. Don't burn run time beyond
  that one check.

## Architecture: 4 specialist lanes + reviewer (hybrid compete mode)

Every nightly run spawns **4 specialist research agents in parallel** (Task/subagent tool),
then a **reviewer pass** with kill authority synthesizes the newsletter:

| Lane | Beat | Grounding |
|---|---|---|
| A — Data | One quantitative question per night off the real nflverse data (committed in-repo); keeps `research/predictive-stats.md` current; extends the predictive-stat work | `pipeline/`, `inputs/nflverse/` |
| B — News | What changed yesterday: camp/beat reports, injuries, depth charts, signings, holdouts | WebSearch, A-tier outlets |
| C — Market | ADP movement + where the market disagrees with our research; **pick-4 draft-strategy countdown** using the opponent model of the 9 leaguemates | WebSearch + `research/draft-tendencies.md` |
| D — Rabbit hole | One deep investigation per night: predictive angles, scheme fits, breakout comps, "this profile rhymes with X's 2021" — chased to a conclusion, not parked | AUDIT_QUEUE, curiosity, all research files |

- **Compete mode (bot decides):** when a genuinely contested, high-stakes question surfaces
  (e.g. "who at pick 4," "is this ADP faller a trap"), the run spawns 2-3 competing takes on
  that one question and the reviewer judges a winner. Not every day — only when a question
  deserves it.
- **Reviewer:** hostile second read of every lane's output (the critic pass, elevated).
  Kill/downgrade authority. Picks the day's strongest finding and names the winning lane in
  the newsletter footer. What got killed and why is also reported (trust is built by showing
  the cuts).
- **Fallback:** if subagents are unavailable in a given scheduled environment, the run works
  the four lanes sequentially itself — lanes may be shorter, but no lane is skipped silently.

## Newsletter format (full analysis daily)

Sections, in order:
1. **Headline** — the single most draft-relevant finding of the day, one paragraph.
2. **What changed yesterday** — news/camp/injury sweep with fantasy implications (Lane B).
3. **Market watch** — ADP movers, value flags for picks 4/17/24/37..., days-to-draft counter,
   and as Aug 28 nears: round-by-round scenario planning against the friends' modeled
   tendencies (Lane C).
4. **Deep dive** — the day's rabbit hole, fully worked with receipts (Lane D, or Lane A when
   the data question is the day's best content).
5. **Checking your takes** — pressure-test Brendan's own opinions (from idea-queue dumps,
   mock-draft voice memos) against data. **Challenge hard** — his explicit instruction.
   Agree or disagree with receipts, no nitpicking marginal calls, no softening real ones.
6. **Footer** — confidence-tier legend, what the reviewer killed today, winning lane, and
   compete-mode verdicts if it fired.

Every claim carries a confidence tier (S = pipeline-computed; A = well-sourced fact; B = thin
sourcing; C = archetype reasoning; Speculative = labeled bet). The verification rails from the
original prompt are unchanged: no invented stats, no unnamed sources, cut when in doubt.

## What this replaces / keeps

- Replaces the "weekly research run" framing; the research files (`research/*.md`) remain the
  durable knowledge base the newsletter draws from and writes back to. The newsletter is the
  daily delivery vehicle, not a replacement for the research corpus.
- Keeps: catch-up backlog priority, idea-queue processing, branch rule (merge-each-run
  workaround until the harness branch pin is fixed), notebook memory loop, safe-bot-edits.

## Open risks (tracked, not hidden)

1. **Branch pin:** scheduled runs are still force-pinned to `claude/*` side branches; a human
   merge into `main` is needed after each run (or a durable fix in routine settings). If a
   newsletter run's branch isn't merged before the next run, the next run won't see
   yesterday's newsletter/memory (it reads `main`).
2. **Subagent availability in scheduled runs is unproven** — first night will tell. Fallback
   is sequential lanes.
3. **Gmail connector** — see Delivery above; on Brendan to reconnect when he wants email.
4. **Offseason news volume varies** — some July days are dead. A dead news day means Lane B is
   short and honest about it, and the deep dive carries the edition; never pad with junk.
