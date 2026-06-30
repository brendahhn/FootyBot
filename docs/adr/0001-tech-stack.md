# ADR 0001: Tech stack

Status: proposed 2026-06-30 (default choice, not yet confirmed by user)

## Decision

Python, using `nfl_data_py` (or `nflreadpy`) for nflverse play-by-play and player stats,
`pandas` for analysis, plain markdown/CSV for research output in Phase 1.

## Rationale

- nflverse's official Python wrappers make free public data the path of least resistance.
- pandas is the standard tool for the kind of year-over-year stat predictiveness analysis
  this project needs (Phase 1, item 3 in CONTEXT.md).
- No need to commit to a CLI framework or web stack until Phase 2 (cheat sheets) — Phase 1
  output is research notes, not a running program.

## Revisit when

Moving into Phase 2 (ranked cheat sheets) — pick a CLI framework then. Revisit entirely if
the user wants a different language.
