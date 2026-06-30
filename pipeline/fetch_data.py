#!/usr/bin/env python3
"""Ingest user-supplied nflverse CSV exports into data/raw/.

This environment can't reach nflverse's data hosts over the network (see
docs/adr/0003-stdlib-pivot.md), so instead of downloading, this script reads
source files the user has placed in inputs/nflverse/ (downloaded directly
from https://github.com/nflverse/nflverse-data/releases) and writes a
filtered, validated copy to data/raw/. Stdlib only, no pandas.
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "inputs" / "nflverse"
OUT_DIR = ROOT / "data" / "raw"

SEASON_MIN = 2016
SEASON_MAX = 2025

SOURCES = {
    "player_stats.csv": {
        "out": "player_stats_weekly.csv",
        "required_columns": ["player_id", "season", "week", "recent_team", "position"],
    },
    "player_stats_def.csv": {
        "out": "player_stats_def_weekly.csv",
        "required_columns": ["player_id", "season", "week", "team"],
    },
}


def load_and_filter(src_path: Path, required_columns: list[str]) -> tuple[list[str], list[dict]]:
    with src_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        missing = [c for c in required_columns if c not in fieldnames]
        if missing:
            raise ValueError(
                f"{src_path.name}: missing expected columns {missing}. "
                f"Actual columns: {fieldnames}"
            )
        rows = []
        for row in reader:
            try:
                season = int(row["season"])
            except (KeyError, ValueError):
                continue
            if SEASON_MIN <= season <= SEASON_MAX:
                rows.append(row)
    return fieldnames, rows


def main() -> int:
    if not SRC_DIR.exists() or not any(SRC_DIR.glob("*.csv")):
        print(
            f"No source files found in {SRC_DIR}. Download player_stats.csv and "
            "player_stats_def.csv from "
            "https://github.com/nflverse/nflverse-data/releases/tag/player_stats "
            "and place them there before running this script.",
            file=sys.stderr,
        )
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    summary = {}

    for src_name, cfg in SOURCES.items():
        src_path = SRC_DIR / src_name
        if not src_path.exists():
            print(f"SKIP: {src_path} not found.", file=sys.stderr)
            continue

        fieldnames, rows = load_and_filter(src_path, cfg["required_columns"])
        out_path = OUT_DIR / cfg["out"]
        with out_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        seasons = sorted({int(r["season"]) for r in rows})
        summary[src_name] = {
            "rows_in": src_path.stat().st_size,
            "rows_out": len(rows),
            "seasons_covered": seasons,
            "columns": fieldnames,
            "written_to": str(out_path.relative_to(ROOT)),
        }
        print(f"{src_name}: wrote {len(rows)} rows ({SEASON_MIN}-{SEASON_MAX}) to {out_path}")

    if not summary:
        print("No expected source files were found/processed.", file=sys.stderr)
        return 1

    summary_path = OUT_DIR / "fetch_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))
    print(f"Wrote summary to {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
