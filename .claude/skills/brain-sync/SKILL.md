---
name: brain-sync
description: >-
  Specialist-routine ↔ Brendan Brain exchange. Use at the START and END of any specialist
  robot run (Jobs Robot, FootyBot, Health Robot, Trading Robot) when ../brendan_brain is
  present, and whenever a specialist session needs shared context, wants to file a question
  for Brendan, or should export results to the shared queue/newspaper.
---
<!-- brendan-os-skill-version: 1.0.0 (2026-07-10) — canonical source: brendan_brain/.claude/skills/brain-sync
     Synced copies: DO NOT EDIT here; edit in brendan_brain and run tools/sync_skills.sh -->
# brain-sync

My domain is determined by which repo I'm in: operator-notebook→jobs, FootyBot→
fantasy_football, health-notebook→health, trading-notebook→investing.

If `../brendan_brain` does not exist: skip silently, but add one line to this run's
notebook CHANGELOG: "brain-sync: brendan_brain not in session; skipped." Never fetch it
another way. Version check: compare my header version's major number with
`../brendan_brain/skills/SKILL_REGISTRY.md`; on major mismatch, write a warning to the
outbox instead of guessing at formats.

## READ (run start, after the robot's own notebook read — adds ~1 min, read-only)
1. `../brendan_brain/preferences/CONFIRMED_RULES.md` — obey. On conflict with my own
   operating prompt, MY PROMPT WINS (it is domain-authoritative); note the conflict in
   my outbox export.
2. `../brendan_brain/queue/` — tasks with `domain: <mine>` and status
   triaged/active/scheduled: fold into this run's research if compatible with my prompt;
   log what I picked up in my `## Research Log` there (append, model-tagged).
3. Answered questions: `../brendan_brain/newspaper/questions/` with `status: answered`
   matching my domain — apply the answers; mark applied in the question file body.

## WRITE (run end, after my own notebook write — the Brain repo is a separate git repo:
commit/push it separately; my repo's push protocol is unchanged)
1. Append today's block to `../brendan_brain/queue/inbox/from-<robot>.md`
   (`from-jobs-robot.md`, `from-footybot.md`, `from-health-robot.md`, `from-trading-robot.md`):

   ```
   ## YYYY-MM-DD — <robot> run summary
   - headline: <1-3 lines, what changed>
   - newspaper_ready: <2-5 bullet items with confidence tiers, or "nothing meaningful">
   - questions_for_brendan: <each with enough context to answer cold, or "none">
   - proposed_durable_knowledge: <generic facts worth cross-domain memory, or "none">
   - predictions: <for trading/footy: dated, confidence-tagged, with horizon — or "none">
   - run_status: success | partial (<what failed>) | failed (<why>)
   ```

   HEALTH SANITIZATION (hard rule, PRIVACY_POLICY): export only generic research
   conclusions and decision-needed items. Never Brendan-specific values — labs, doses,
   symptoms, biometrics, personal context. When in doubt, export the question, not the data.
2. In `../brendan_brain`: `git pull --rebase origin main`, commit
   (`inbox: <robot> YYYY-MM-DD`), push, verify `git ls-remote origin main` matches HEAD.
   If the Brain push fails after 4 retries (2/4/8/16s): my own repo's push still proceeds;
   record "brain-sync: EXPORT FAILED <error>" in my notebook CHANGELOG so the next run
   retries (the dated-block format makes retries idempotent — same-day block gets replaced,
   not duplicated: check for an existing `## YYYY-MM-DD` heading first).
3. Never write anywhere else in the Brain from a robot run (triage into tasks/knowledge is
   the Chief of Staff's job, in the Brain).
