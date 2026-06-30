#!/usr/bin/env python3
"""Year-over-year predictiveness of candidate stats, scored against this
league's actual formula (pipeline/league_scoring.py). Stdlib only -- see
docs/adr/0003-stdlib-pivot.md for why.

Reads data/raw/player_stats_weekly.csv and data/raw/player_stats_def_weekly.csv
(the output of pipeline/fetch_data.py). Writes research/predictive-stats.md.

Of the candidate stats named in the original goal -- target share, air yards,
snap%, red zone touches, aDOT, yards per route run, TD rate (offense) and
snap%, tackle rate, sack rate, pass-rush opportunity (IDP) -- only the ones
computable from nflverse's player_stats.csv / player_stats_def.csv are
included below. snap% (offense + IDP), red zone touches, and yards per route
run are NOT in these files and are explicitly skipped rather than faked; they
need snap_counts.csv, play-by-play red-zone splits, and participation data
respectively -- none of which have been provided yet.
"""
import csv
import sys
from pathlib import Path
from statistics import mean

from league_scoring import idp_points, offense_points

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
MIN_GAMES = 6  # exclude injury-shortened/cup-of-coffee seasons from correlation noise


def pearson_r(xs: list[float], ys: list[float]) -> float | None:
    n = len(xs)
    if n < 8:  # too few pairs to mean anything
        return None
    mx, my = mean(xs), mean(ys)
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    if vx == 0 or vy == 0:
        return None
    return cov / ((vx ** 0.5) * (vy ** 0.5))


def load_rows(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def f(row: dict, key: str) -> float:
    try:
        return float(row.get(key) or 0)
    except ValueError:
        return 0.0


def aggregate_offense_by_player_season(rows: list[dict]) -> dict:
    """player_id -> season -> {games, ppg, target_share, air_yards_share, wopr, adot, td_rate}"""
    by_ps: dict = {}
    for row in rows:
        try:
            season = int(row["season"])
        except (KeyError, ValueError):
            continue
        pid = row.get("player_id")
        if not pid:
            continue
        key = (pid, season)
        by_ps.setdefault(key, []).append(row)

    out: dict = {}
    for (pid, season), weeks in by_ps.items():
        games = len(weeks)
        pts = [offense_points(w) for w in weeks]
        targets = sum(f(w, "targets") for w in weeks)
        carries = sum(f(w, "carries") for w in weeks)
        air_yards = sum(f(w, "receiving_air_yards") for w in weeks)
        tds = sum(f(w, "receiving_tds") + f(w, "rushing_tds") for w in weeks)
        touches = targets + carries
        out.setdefault(pid, {})[season] = {
            "games": games,
            "ppg": sum(pts) / games if games else 0.0,
            "target_share": mean([f(w, "target_share") for w in weeks if w.get("target_share")])
            if any(w.get("target_share") for w in weeks)
            else None,
            "air_yards_share": mean(
                [f(w, "air_yards_share") for w in weeks if w.get("air_yards_share")]
            )
            if any(w.get("air_yards_share") for w in weeks)
            else None,
            "wopr": mean([f(w, "wopr") for w in weeks if w.get("wopr")])
            if any(w.get("wopr") for w in weeks)
            else None,
            "adot": (air_yards / targets) if targets > 0 else None,
            "td_rate": (tds / touches) if touches > 0 else None,
        }
    return out


def aggregate_idp_by_player_season(rows: list[dict]) -> dict:
    by_ps: dict = {}
    for row in rows:
        try:
            season = int(row["season"])
        except (KeyError, ValueError):
            continue
        pid = row.get("player_id")
        if not pid:
            continue
        by_ps.setdefault((pid, season), []).append(row)

    out: dict = {}
    for (pid, season), weeks in by_ps.items():
        games = len(weeks)
        pts = [idp_points(w) for w in weeks]
        solo = sum(f(w, "def_tackles_solo") for w in weeks)
        sacks = sum(f(w, "def_sacks") for w in weeks)
        out.setdefault(pid, {})[season] = {
            "games": games,
            "ppg": sum(pts) / games if games else 0.0,
            "tackle_rate": solo / games if games else None,
            "sack_rate": sacks / games if games else None,
        }
    return out


def yoy_pairs(by_player: dict, stat_key: str) -> tuple[list[float], list[float]]:
    xs, ys = [], []
    for pid, by_season in by_player.items():
        for season, vals in by_season.items():
            nxt = by_season.get(season + 1)
            if not nxt:
                continue
            if vals["games"] < MIN_GAMES or nxt["games"] < MIN_GAMES:
                continue
            x = vals.get(stat_key)
            if x is None:
                continue
            xs.append(x)
            ys.append(nxt["ppg"])
    return xs, ys


def main() -> int:
    off_path = RAW / "player_stats_weekly.csv"
    def_path = RAW / "player_stats_def_weekly.csv"
    if not off_path.exists() and not def_path.exists():
        print(
            f"Neither {off_path} nor {def_path} exist. Run pipeline/fetch_data.py "
            "against real input files first.",
            file=sys.stderr,
        )
        return 1

    lines = ["# Predictive stats — year-over-year correlation with next season's PPG", ""]
    lines.append(
        f"Generated by `pipeline/predictive_stats.py` from real nflverse data "
        f"(see `data/raw/fetch_summary.json` for exact row counts/seasons). "
        f"Minimum {MIN_GAMES} games in both seasons required per player-season pair to "
        f"reduce small-sample noise. Correlation = Pearson r between the stat in season N "
        f"and points-per-game in season N+1, under this league's exact scoring formula "
        f"(`pipeline/league_scoring.py`), pooled across all available season pairs."
    )
    lines.append("")
    lines.append(
        "**Known gap:** league scoring's 40+ yard run/reception bonuses and offensive "
        "fumble return TDs are NOT included (not computable from weekly aggregate data) "
        "-- every PPG figure below under-counts real league points by a small, "
        "boom-play-dependent amount."
    )
    lines.append("")
    lines.append(
        "**Not computed (data not yet available):** snap% (offense + IDP), red zone "
        "touches, yards per route run. These need `snap_counts.csv`, play-by-play "
        "red-zone splits, and participation data respectively -- none provided yet."
    )
    lines.append("")

    if off_path.exists():
        off_rows = load_rows(off_path)
        by_player = aggregate_offense_by_player_season(off_rows)
        offense_candidates = {
            "target_share": "Target share",
            "air_yards_share": "Air yards share",
            "wopr": "WOPR (weighted opportunity rating)",
            "adot": "aDOT (avg depth of target)",
            "td_rate": "TD rate (TDs per touch)",
            "ppg": "PPG itself (baseline -- is points just sticky?)",
        }
        results = []
        for key, label in offense_candidates.items():
            xs, ys = yoy_pairs(by_player, key)
            r = pearson_r(xs, ys)
            results.append((label, key, r, len(xs)))
        results.sort(key=lambda t: (t[2] is None, -(abs(t[2]) if t[2] is not None else 0)))

        lines.append("## Offense")
        lines.append("")
        lines.append("| Stat | Pearson r (season N -> N+1 PPG) | N pairs |")
        lines.append("|---|---|---|")
        for label, key, r, n in results:
            r_str = f"{r:.3f}" if r is not None else "n/a (insufficient data)"
            lines.append(f"| {label} | {r_str} | {n} |")
        lines.append("")

    if def_path.exists():
        def_rows = load_rows(def_path)
        by_player_def = aggregate_idp_by_player_season(def_rows)
        idp_candidates = {
            "tackle_rate": "Solo tackles per game",
            "sack_rate": "Sacks per game",
            "ppg": "IDP PPG itself (baseline)",
        }
        results_d = []
        for key, label in idp_candidates.items():
            xs, ys = yoy_pairs(by_player_def, key)
            r = pearson_r(xs, ys)
            results_d.append((label, key, r, len(xs)))
        results_d.sort(key=lambda t: (t[2] is None, -(abs(t[2]) if t[2] is not None else 0)))

        lines.append("## IDP")
        lines.append("")
        lines.append("| Stat | Pearson r (season N -> N+1 PPG) | N pairs |")
        lines.append("|---|---|---|")
        for label, key, r, n in results_d:
            r_str = f"{r:.3f}" if r is not None else "n/a (insufficient data)"
            lines.append(f"| {label} | {r_str} | {n} |")
        lines.append("")

    out_path = ROOT / "research" / "predictive-stats.md"
    out_path.write_text("\n".join(lines) + "\n")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
