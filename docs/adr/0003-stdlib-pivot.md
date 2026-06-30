# ADR 0003: Pivot from pandas to pure-Python stdlib for the data pipeline

Status: confirmed 2026-06-30

## Decision

`pipeline/` scripts use only the Python standard library (`csv`, `statistics`, `math`,
`json`) — no pandas, no pyarrow, no `nfl_data_py`/`nflreadpy`. Input data is read from
locally-provided CSV files in `inputs/nflverse/` (user-downloaded and uploaded, not fetched
over the network by the script itself). Intermediate/output data is written as CSV, not
parquet.

## Why this supersedes part of ADR 0001

ADR 0001 proposed Python + pandas + nflverse's Python wrappers, assuming normal internet
access. That assumption turned out to be false: this development environment's network
egress allowlist blocks PyPI, npm, apt, GitHub's release-asset CDN, and even the WebFetch
tool (confirmed via direct testing of ~15 distinct hosts, plus independent confirmation that
git/GitHub access itself is scoped to `brendahhn/*`-owned repos only — see chat history
2026-06-30). Across this user's other bots (JoBot, HealthBot, "Daily Operator" — checked via
`list_triggers`), the established pattern for this kind of restricted environment is: don't
fight the network policy, build around the channels that actually work. None of those bots
pip-install anything; they use WebSearch and sanctioned MCP connectors.

For FootyBot, neither WebSearch (snippets only, not structured bulk data) nor any available
MCP connector can supply 10-year weekly player stat tables. The actual fix is the user
downloading the specific nflverse files on their own (unrestricted) machine and uploading
them here — at which point pandas isn't needed at all; stdlib `csv` + manual statistics
(Pearson correlation, rank ordering, etc.) is entirely sufficient for this project's scale
(thousands of rows, not the millions a full play-by-play table would have).

## Consequence

`research/predictive-stats.md`'s "no fabricated numbers" requirement is satisfied by: real
files the user downloaded directly from nflverse's GitHub releases, parsed by a script that
prints exactly which rows/columns it used. If nflverse's CSV schema doesn't match what's
assumed here, the ingestion script is written defensively (reads the header row, checks for
expected columns, fails loudly rather than silently producing wrong numbers) rather than
hard-coding column positions.

## Revisit when

This environment's network egress allowlist is widened to include PyPI and nflverse's data
hosts, or the project moves to an environment without this restriction — at that point,
switching back to pandas for convenience is reasonable but no longer necessary.
