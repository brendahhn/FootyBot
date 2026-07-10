<!-- version: 1.0.0 (2026-07-10) — Brendan OS integration surface. Additive only: nothing
     in this repo's existing prompt, notebook, research, or queue changed. -->
# Brain Integration — FootyBot ↔ brendan_brain

**Domain: `fantasy_football`.**

## What this is
The shared Brendan Brain (`brendahhn/brendan_brain`) holds Brendan's cross-domain memory:
research queue, preferences, questions-for-Brendan, morning newspaper. This robot exchanges
with it via the `brain-sync` skill (`.claude/skills/brain-sync/SKILL.md` — synced copy;
canonical lives in brendan_brain, never edit here).

## Enabling (one-time, Brendan)
1. Add `brendan_brain` to this routine's repository selection so `../brendan_brain`
   exists during scheduled runs.
2. Apply the two-line prompt addition in `proposed-prompt-change.md` via a safe-bot-edits
   session (robot prompts are never edited silently — including by this build).
Until both happen, nothing changes about how this robot runs.

## Per-run behavior (once enabled) — full protocol in the brain-sync SKILL.md
- **Run start (read-only, after the notebook read):** obey Brain CONFIRMED_RULES (this
  robot's prompt wins on conflict; conflicts get reported in the export); pick up open
  Brain tasks with `domain: fantasy_football`; apply Brendan's answers from the Brain's questions folder.
- **Run end (after the notebook write):** append a dated block to
  `../brendan_brain/queue/inbox/from-footybot.md`, then commit/push the Brain repo separately. Brain
  push failure never blocks this robot — log in CHANGELOG, retry next run (idempotent by
  dated block).

Note: exports are the newsletter's 3-5 headline findings with confidence tiers, [BEHAVIOR] items needing Brendan, and dated predictions (with horizon) for the Brain's prediction/outcome tracker. The existing auto-merge Action ignores these root files (it triggers on newsletters/**), so integration does not interact with it.

## Files this integration added to this repo
`BRAIN_INTEGRATION.md`, `proposed-prompt-change.md`,
`.claude/skills/brain-sync/SKILL.md`, `.claude/skills/brain-ops/SKILL.md` (synced copies).
Nothing else was modified.
