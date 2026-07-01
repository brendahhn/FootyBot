# inputs/league-history/

The league's own historical draft boards (2019-2025), for opponent modeling — see
`research/draft-tendencies.md` for the analysis and `CONTEXT.md` for how it fits the goal.

## Files

- `draft_history_master.csv` — **the deliverable.** Every pick from 2019-2025 (1,120 rows):
  `year, overall_pick, round, pick_in_round, player, team_name, manager, position`. Managers
  are the stable identity across years; `position` is joined from `inputs/nflverse/`.
- `extracted/` — the intermediate text pulled from the saved Yahoo pages, per season:
  - `<year>_order.txt` — draft board text (players in pick order)
  - `<year>_order_teamnames.txt` — full team name per pick, in pick order
  - `<year>_managers.txt` — that season's Managers page (team nickname → real manager)

## Provenance / reproducibility

Brendan saved each season's Yahoo "Draft Results" and "Managers" pages as MHTML and uploaded
them (2026-07-01). Those raw ~4MB MHTML files are NOT committed (61MB total, messy HTML); the
small extracted `.txt` above preserve everything the pipeline needs. To rebuild the CSV:

```
python3 pipeline/extract_yahoo_mhtml.py <saved_page>.mhtml   # only when re-adding raw pages
python3 pipeline/build_draft_history.py                       # joins extracted/ -> master CSV
```

`build_draft_history.py` validates the join (0 unmapped managers, 16 picks/manager/year) and
reports any pick it can't resolve rather than dropping it silently.

## Adding more seasons

Drop a new season's extracted `<year>_order.txt`, `<year>_order_teamnames.txt`, and
`<year>_managers.txt` into `extracted/` and re-run `build_draft_history.py` — it globs by year,
no code change needed.
