# ADR 0004: Scheduled autonomous bot architecture

Status: confirmed 2026-06-30

## Decision

FootyBot adopts the same architecture as Brendan's other two scheduled bots (Jobs Robot on
`operator-notebook`, Health Research Robot on `health-notebook`):

- `footybot-operating-prompt.md` — behavior, edited only in a reviewed Claude Code session,
  must end in exactly `## END` (validation gate — see bootstrap note below).
- `footybot-notebook.md` — memory, read first/written last every run, the only thing that
  persists run-to-run.
- `footybot-idea-queue.md` — Brendan's unsorted backlog (Twitter/X likes, article links,
  questions), consumed by the bot over time, never blocking other work.
- `.claude/skills/safe-bot-edits/SKILL.md` — ported verbatim (plus a table-row addition for
  FootyBot) from `health-notebook`, since it already correctly encodes the topic-vs-behavior
  routing, diagnose-before-changing, diff-before-commit, and verify-the-push rules this project
  needs, and re-deriving them from scratch risked missing lessons already paid for on the other
  two bots.

The actual scheduled trigger (cron config, "thin bootstrap" pointing at the prompt file) has
**not** been created yet — that's a deliberate "browser step" left for Brendan, per
`safe-bot-edits`' own convention, until cadence/delivery are confirmed (see Open questions).

## Why

This was the explicit direction given by Brendan, via a handoff doc from a different session
that hadn't seen this session's actual Phase 1 progress (it described the FootyBot repo as
empty, which it wasn't, and slightly misstated the IDP scope, which `docs/adr/0002-idp-scope.md`
already had correct). Brendan confirmed: adopt the architecture, but use the actual correct
details already established in this session, not the handoff doc's restatement of them.

## What's preserved from Phase 1

Nothing was discarded. `CONTEXT.md`, ADRs 0001-0003, and all of `research/` and `pipeline/`
remain exactly as built — the notebook indexes them rather than duplicating their content, and
the operating prompt's research steps build on them directly.

## Consequence

`research/predictive-stats.md` is still gated on real data (Brendan's CSV upload or a network
policy change) — this architecture change doesn't solve that blocker, it just stops the bot from
treating it as a hard stop. The bot operates in WebSearch-corroborated mode in the meantime (see
`footybot-notebook.md` SANDBOX_CAPABILITIES) and queues the gap in AUDIT_QUEUE for when real data
becomes available.

## Open questions (not yet resolved, tracked in footybot-notebook.md STATUS)

- Run cadence (daily? weekly during season, more frequent near the Aug 28 draft?).
- Delivery channel (Gmail draft like the other two bots, or something else).
- No scheduled trigger exists yet — needs Brendan's input on the above before one is created.
