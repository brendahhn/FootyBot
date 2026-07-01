#!/usr/bin/env python3
"""Ingest user-supplied nflverse CSV exports into data/raw/.

This environment can't reach nflverse's data hosts over the network (see
docs/adr/0003-stdlib-pivot.md), so instead of downloading, this script reads
source files the user has placed in inputs/nflverse/ (downloaded directly
from https://github.com/nflverse/nflverse-data/releases) and writes a
filtered, validated copy to data/raw/. Stdlib only, no pandas.

Two source shapes are supported, because nflverse changed its file format
starting with the 2025 season:

- LEGACY (seasons up to 2024): two separate files, player_stats.csv (offense,
  uses "recent_team" and "interceptions") and player_stats_def.csv (IDP, uses
  "team"). This is what's in the combined multi-year release asset.
- UNIFIED (2025 onward): one file per season, stats_player_week_<year>.csv,
  with offense AND defense columns in the same row, using "team" (not
  "recent_team") and "passing_interceptions" (not "interceptions"). Drop
  future seasons' files in as stats_player_week_2026.csv etc. and this script
  picks them up automatically -- no code change needed for the next season.
"""
import csv
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "inputs" / "nflverse"
OUT_DIR = ROOT / "data" / "raw"

SEASON_MIN = 2016
SEASON_MAX = 2025

DEFENSIVE_POSITIONS = {
    "CB", "DB", "DE", "DL", "DT", "FS", "ILB", "LB", "MLB", "NT", "OLB", "S", "SAF",
}

LEGACY_SOURCES = {
    "player_stats.csv": {
        "required_columns": ["player_id", "season", "week", "recent_team", "position"],
    },
    "player_stats_def.csv": {
        "required_columns": ["player_id", "season", "week", "team"],
    },
}

# unified-file column renames needed to match the legacy offense-file schema
UNIFIED_OFFENSE_RENAMES = {
    "team": "recent_team",
    "passing_interceptions": "interceptions",
}


def load_rows(src_path: Path, required_columns: list[str]) -> tuple[list[str], list[dict]]:
    with src_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        missing = [c for c in required_columns if c not in fieldnames]
        if missing:
            raise ValueError(
                f"{src_path.name}: missing expected columns {missing}. "
                f"Actual columns: {fieldnames}"
            )
        rows = [row for row in reader]
    return fieldnames, rows


def filter_seasons(rows: list[dict]) -> list[dict]:
    out = []
    for row in rows:
        try:
            season = int(row["season"])
        except (KeyError, ValueError):
            continue
        if SEASON_MIN <= season <= SEASON_MAX:
            out.append(row)
    return out


def split_unified_file(src_path: Path) -> tuple[list[dict], list[dict]]:
    """Split a stats_player_week_<year>.csv (offense+defense combined) into
    (offense_rows, defense_rows), normalized to match the legacy schemas."""
    required = ["player_id", "season", "week", "team", "position"]
    with src_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        missing = [c for c in required if c not in fieldnames]
        if missing:
            raise ValueError(
                f"{src_path.name}: missing expected columns {missing}. "
                f"Actual columns: {fieldnames}"
            )
        rows = filter_seasons(list(reader))

    offense_rows = []
    defense_rows = []
    for row in rows:
        offense_row = dict(row)
        for old_key, new_key in UNIFIED_OFFENSE_RENAMES.items():
            if old_key in offense_row:
                offense_row[new_key] = offense_row.pop(old_key)
        offense_rows.append(offense_row)

        has_def_activity = any(
            row.get(k) not in (None, "", "0", "0.0")
            for k in row
            if k.startswith("def_")
        )
        if row.get("position") in DEFENSIVE_POSITIONS or has_def_activity:
            defense_rows.append(dict(row))

    return offense_rows, defense_rows


def write_merged(rows: list[dict], out_path: Path) -> list[str]:
    """Write rows to CSV using the union of all fieldnames seen (rows may come
    from different source schemas with slightly different column sets)."""
    fieldnames: list[str] = []
    seen = set()
    for row in rows:
        for k in row:
            if k not in seen:
                seen.add(k)
                fieldnames.append(k)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return fieldnames


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

    offense_rows: list[dict] = []
    defense_rows: list[dict] = []

    for src_name, cfg in LEGACY_SOURCES.items():
        src_path = SRC_DIR / src_name
        if not src_path.exists():
            print(f"SKIP: {src_path} not found.", file=sys.stderr)
            continue
        _, rows = load_rows(src_path, cfg["required_columns"])
        rows = filter_seasons(rows)
        target = offense_rows if src_name == "player_stats.csv" else defense_rows
        target.extend(rows)
        seasons = sorted({int(r["season"]) for r in rows})
        summary[src_name] = {"rows_used": len(rows), "seasons_covered": seasons}
        print(f"{src_name}: {len(rows)} rows ({SEASON_MIN}-{SEASON_MAX})")

    unified_files = sorted(glob.glob(str(SRC_DIR / "stats_player_week_*.csv")))
    for src_path_str in unified_files:
        src_path = Path(src_path_str)
        m = re.search(r"stats_player_week_(\d{4})\.csv$", src_path.name)
        year_tag = m.group(1) if m else "?"
        off_rows, def_rows = split_unified_file(src_path)
        offense_rows.extend(off_rows)
        defense_rows.extend(def_rows)
        summary[src_path.name] = {
            "year_tag": year_tag,
            "offense_rows_used": len(off_rows),
            "defense_rows_used": len(def_rows),
        }
        print(
            f"{src_path.name}: {len(off_rows)} offense rows + {len(def_rows)} "
            f"defense rows (unified {year_tag} format)"
        )

    if not summary:
        print("No expected source files were found/processed.", file=sys.stderr)
        return 1

    off_out = OUT_DIR / "player_stats_weekly.csv"
    def_out = OUT_DIR / "player_stats_def_weekly.csv"
    off_fields = write_merged(offense_rows, off_out)
    def_fields = write_merged(defense_rows, def_out)
    print(f"Wrote {len(offense_rows)} total offense rows to {off_out}")
    print(f"Wrote {len(defense_rows)} total defense rows to {def_out}")

    summary["_totals"] = {
        "offense_rows": len(offense_rows),
        "offense_seasons": sorted({int(r["season"]) for r in offense_rows if r.get("season")}),
        "defense_rows": len(defense_rows),
        "defense_seasons": sorted({int(r["season"]) for r in defense_rows if r.get("season")}),
        "offense_columns": off_fields,
        "defense_columns": def_fields,
    }

    summary_path = OUT_DIR / "fetch_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))
    print(f"Wrote summary to {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
