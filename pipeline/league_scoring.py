"""This league's exact scoring formula (see CONTEXT.md "Scoring"), applied to a
single nflverse player_stats.csv weekly row (offense) or player_stats_def.csv
weekly row (IDP).

Known approximation: the 40+ yard run / 40+ yard reception bonuses (+2 each)
and offensive fumble return TDs (+6) are NOT computable from these weekly
aggregate files -- they require play-level data (which fields are
"play resulted in a 40+ yard gain", not available in a season/week rollup).
Every score this module produces is missing those bonus points. This is a
known, documented gap, not a silent omission -- see research/predictive-stats.md
once it exists.
"""


def offense_points(row: dict) -> float:
    def f(key: str) -> float:
        try:
            return float(row.get(key) or 0)
        except ValueError:
            return 0.0

    points = 0.0
    points += f("passing_yards") / 25.0
    points += f("passing_tds") * 6
    points += f("interceptions") * -2
    points += f("rushing_yards") / 10.0
    points += f("rushing_tds") * 6
    points += f("receptions") * 0.5
    points += f("receiving_yards") / 10.0
    points += f("receiving_tds") * 6
    points += f("special_teams_tds") * 6  # return TDs
    points += (
        f("passing_2pt_conversions")
        + f("rushing_2pt_conversions")
        + f("receiving_2pt_conversions")
    ) * 2
    points += (
        f("sack_fumbles_lost") + f("rushing_fumbles_lost") + f("receiving_fumbles_lost")
    ) * -2
    return points


def idp_points(row: dict) -> float:
    def f(key: str) -> float:
        try:
            return float(row.get(key) or 0)
        except ValueError:
            return 0.0

    points = 0.0
    points += f("def_tackles_solo") * 0.5
    points += f("def_tackle_assists") * 0.25
    points += f("def_tackles_for_loss") * 0.5
    points += f("def_sacks") * 4
    points += f("def_interceptions") * 6
    points += f("def_fumbles_forced") * 3
    points += f("def_fumble_recovery_own") * 2 if "def_fumble_recovery_own" in row else 0.0
    points += f("def_tds") * 6
    points += f("def_pass_defended") * 3
    return points
