"""Lane A helper: per-player single-season fantasy profile under THIS league's
scoring, from the committed weekly nflverse data (data/raw/player_stats_weekly.csv,
produced by fetch_data.py). Computes week-to-week consistency, not just totals --
the point is to test claims like "player X is good but not consistent" with real
weekly distributions rather than season aggregates.

Usage:
    python3 pipeline/player_season_profile.py 2025 "Tee Higgins" "James Cook" ...

Metrics per player (REG season only):
  G        games with a recorded weekly stat line
  PPG      mean league points over games played
  PP17     league points averaged over a full 17-game season (missed games = 0),
           i.e. what a manager who rostered him all year actually banked per week
  MED      median weekly league points
  SD       stdev of weekly league points (raw volatility)
  BOOM     # weeks >= 20 league pts (true WR1/RB1 week)
  START    # weeks >= 12 league pts (startable)
  DUD      # weeks < 8 league pts (unstartable, among games played)
  BEST/WORST  high and low weekly scores

Known scoring gap (inherited from league_scoring.py): 40+ yд bonuses and
offensive fumble-return TDs are not in weekly aggregate data, so every score
slightly under-counts big-play weeks. Documented, not silent.
"""
import csv
import statistics
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from league_scoring import offense_points  # noqa: E402

WEEKLY = "data/raw/player_stats_weekly.csv"


def profile(season, names):
    want = {n.lower(): n for n in names}
    # player_display_name -> list of weekly points (REG only)
    weeks = {n.lower(): [] for n in names}
    matched_name = {}
    with open(WEEKLY) as f:
        for row in csv.DictReader(f):
            if row["season"] != str(season):
                continue
            if (row.get("season_type") or "REG") != "REG":
                continue
            disp = (row.get("player_display_name") or "").strip()
            key = disp.lower()
            for wkey in want:
                if wkey == key or wkey in key:
                    weeks[wkey].append(offense_points(row))
                    matched_name[wkey] = disp
    rows = []
    for wkey, orig in want.items():
        pts = weeks[wkey]
        if not pts:
            rows.append((orig, None))
            continue
        g = len(pts)
        rows.append((matched_name.get(wkey, orig), {
            "G": g,
            "PPG": round(sum(pts) / g, 1),
            "PP17": round(sum(pts) / 17, 1),
            "MED": round(statistics.median(pts), 1),
            "SD": round(statistics.pstdev(pts), 1) if g > 1 else 0.0,
            "BOOM": sum(1 for p in pts if p >= 20),
            "START": sum(1 for p in pts if p >= 12),
            "DUD": sum(1 for p in pts if p < 8),
            "BEST": round(max(pts), 1),
            "WORST": round(min(pts), 1),
        }))
    return rows


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return
    season = sys.argv[1]
    names = sys.argv[2:]
    rows = profile(season, names)
    hdr = ["Player", "G", "PPG", "PP17", "MED", "SD", "BOOM", "START", "DUD", "BEST", "WORST"]
    print("  ".join(hdr))
    print("-" * 90)
    for name, m in rows:
        if m is None:
            print(f"{name:<24}  (no {season} REG games found)")
            continue
        print(f"{name:<24}{m['G']:>3}{m['PPG']:>7}{m['PP17']:>7}{m['MED']:>7}"
              f"{m['SD']:>7}{m['BOOM']:>6}{m['START']:>7}{m['DUD']:>6}{m['BEST']:>7}{m['WORST']:>7}")


if __name__ == "__main__":
    main()
