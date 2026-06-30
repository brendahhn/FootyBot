# FootyBot

Fantasy football research & draft assistant for the 2026 season.

Built for one specific league (10-team, half-PPR, 1-IDP-flex, snake draft, pick slot #4)
rather than as a general-purpose product. See [`CONTEXT.md`](CONTEXT.md) for the full
requirements and [`docs/adr/`](docs/adr) for decisions made along the way.

This is a scheduled, unattended robot — same architecture as Brendan's Jobs Robot
(`operator-notebook`) and Health Research Robot (`health-notebook`). Its real behavior lives in
[`footybot-operating-prompt.md`](footybot-operating-prompt.md), its memory in
[`footybot-notebook.md`](footybot-notebook.md), and Brendan's research backlog in
[`footybot-idea-queue.md`](footybot-idea-queue.md). To change how it behaves, use the
[`safe-bot-edits`](.claude/skills/safe-bot-edits/SKILL.md) skill rather than editing the prompt
directly. See [`docs/adr/0004-scheduled-bot-architecture.md`](docs/adr/0004-scheduled-bot-architecture.md).

## Status

Phase 1: research repo + data pipeline. No rankings or draft-day tooling yet. No scheduled
trigger exists yet — cadence/delivery need to be confirmed first (see `footybot-notebook.md`
STATUS section).
