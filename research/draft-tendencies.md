# League draft tendencies — opponent modeling (2019-2025)

Status: first pass 2026-07-01, built from **real data** — 7 seasons of this league's actual
Yahoo draft boards (2019-2025), 1,120 total picks, joined to the 10 stable managers and
enriched with player positions from the committed nflverse data. Source dataset:
`inputs/league-history/draft_history_master.csv`; reproducible via
`pipeline/extract_yahoo_mhtml.py` → `pipeline/build_draft_history.py`. This is **S-tier by
provenance** (the league's own history, not a projection) — the only soft spots are noted inline.

## What this is for

Brendan drafts 4th in 2026 and wants to model how each of his 9 leaguemates drafts — so he can
anticipate runs, know who will let a QB slide, and know who he's actually competing with for a
given archetype. This is opponent modeling, a scope beyond pure player research (see
`CONTEXT.md` — added as a Goal item 2026-07-01).

The 10 managers (stable across all 7 years): Aaron, Brendan (us), Connor, Dylan, Jack, lucas,
Mattias, Nate, Niko, riley. Team nicknames change yearly; managers don't — the join is keyed on
the per-year Managers page, validated to 0 unmapped picks and exactly 16 picks/manager/year.

Data caveats (kept honest): position is matched for ~96% of picks; the ~4% unmatched are team
defenses, kickers, and IDP (correctly not RB/WR/QB/TE) plus 3 skill players with name-suffix
quirks (Hollywood Brown, Kenny Gainwell, Joshua Palmer — hand-corrected in the analysis below).
Positional counts below are reliable for the skill positions that matter for draft strategy.

## Finding 1 — QB draft timing (this is the big one, given 6pt passing TDs)

Average round each manager takes their **first** QB, across the 7 drafts (lower = earlier):

| Manager | Avg first-QB round | Earliest | Latest | Read |
|---|---|---|---|---|
| Aaron | 5.0 | 3 | 7 | **Earliest QB drafter** — will grab a QB before you if you both want one |
| lucas | 5.3 | 3 | 9 | Early-QB lean |
| Niko | 6.1 | 3 | 13 | Middle, but capable of a round-3 reach |
| Jack | 6.3 | 3 | 11 | Middle |
| Mattias | 7.1 | 3 | 11 | Middle |
| riley | 7.1 | 5 | 9 | Middle, consistent (never earlier than 5) |
| **Brendan (us)** | 7.7 | 5 | 12 | We wait on QB — worth knowing about ourselves |
| Connor | 8.3 | 5 | 13 | Late-QB lean |
| Nate | 8.3 | 3 | 14 | Late on average but *has* reached round 3 — high variance |
| **Dylan** | **10.3** | **7** | 13 | **The QB-punter — never taken a QB before round 7, ever** |

**Actionable:** in a 6pt-passing-TD league, QB value is elevated vs. standard, but this league
has NOT historically adjusted for that — most managers still wait (league-wide first QB averages
round ~7). **Dylan reliably punts QB to round 7+**, so an elite QB will almost never be taken by
him early. **Aaron and lucas are the two to watch** if you're deciding whether to reach for a QB
— they're the only two who consistently move in the round 5 range. If you (Brendan) ever want to
zag and take a top QB early to exploit the 6pt scoring, the board history says you'd be doing it
2-3 rounds ahead of the field, i.e. you could likely wait longer than instinct suggests and still
get a top-5 QB. (Verify against 2026 ADP closer to the draft — behavior can shift.)

## Finding 2 — Round 1 position tendency (7 first-round picks each)

| Manager | Round 1 picks (7 drafts) | Read |
|---|---|---|
| Aaron | RB 6, WR 1 | Hardcore RB-first |
| lucas | RB 5, WR 2 | RB-first |
| Connor | RB 5, WR 1, TE 1 | RB-first (and the rare R1 TE) |
| Niko | RB 4, WR 2, TE 1 | RB-lean (and the rare R1 TE) |
| Brendan (us) | RB 4, WR 3 | Slight RB-lean |
| Dylan | RB 4, WR 3 | Slight RB-lean |
| Mattias | RB 4, WR 3 | Slight RB-lean |
| Nate | RB 4, WR 3 | Slight RB-lean |
| riley | RB 4, WR 3 | Slight RB-lean |
| **Jack** | **WR 5, RB 2** | **The ONLY WR-first drafter in the league** |

**Actionable:** this quantitatively confirms Brendan's own instinct from his mock-draft voice
memo ("running backs in my league get so much more valued... you can always scrounge a receiver,
but not so much a running back"). **9 of 10 managers lean RB in round 1; only Jack bucks it.**
That means: (a) the RB run comes early and hard — elite RBs will not slide; (b) WRs are
systematically slightly devalued at 1.x, so an elite WR is more likely to fall to you at pick 4
than an elite RB is. At pick 4 specifically, expect the top 3 to skew RB-heavy, leaving a strong
WR (or the best-available RB) for you — which matches how the 2025 board actually fell (Chase,
Bijan, Gibbs, then Saquon at 4).

## Finding 3 — Early-draft (rounds 1-5) RB vs WR identity

| Manager | RB | WR | TE | QB | Early lean |
|---|---|---|---|---|---|
| Connor | 18 | 14 | 2 | 1 | Strong RB |
| Niko | 17 | 14 | 1 | 3 | RB |
| Dylan | 16 | 16 | 3 | 0 | Balanced (and 0 early QBs — see Finding 1) |
| Aaron | 15 | 11 | 4 | 5 | RB + earliest QBs + most early TEs |
| Mattias | 15 | 15 | 3 | 2 | Balanced |
| lucas | 15 | 14 | 2 | 4 | Balanced, QB-forward |
| Nate | 15 | 16 | 2 | 2 | Slight WR |
| Jack | 14 | 15 | 3 | 3 | Slight WR (consistent with his R1 WR lean) |
| **Brendan (us)** | 14 | 18 | 2 | 1 | **Most WR-heavy early build in the league** |
| riley | 13 | 17 | 3 | 2 | WR-lean |

**Actionable (self-scouting):** Brendan is the **most WR-heavy early drafter** in the league
(18 WR / 14 RB in rounds 1-5 across 7 years) *and* one of the latest QB drafters. Worth being
honest with ourselves about: in a league where everyone else prioritizes RB, our WR-heavy build
is a real market-inefficiency play (we let the RB run happen and scoop the falling WR value) —
but it also means we're often thin at RB, the position this league treats as scarce. The mock
where Brendan wanted "Saquon + Chase" is notable precisely *because* it would break his own
pattern toward securing RB early.

## Next steps / open threads

- **[data]** More draft years if available would tighten the QB-timing averages (7 is enough for
  a lean, not for high confidence on the high-variance managers like Nate).
- **[analysis]** Rookie/"flashy new guy" tendency — Brendan specifically asked whether certain
  managers reach for shiny rookies (e.g. "Bucky Irving, Brian Thomas" types) vs. reliable vets.
  Computing this needs each player's NFL experience-at-draft-time (rookie vs. veteran), which
  isn't in the current dataset — would need a draft-year/rookie-year lookup per player. Flagged
  in AUDIT_QUEUE.
- **[analysis]** Reach vs. value — join each pick to that year's ADP to see who consistently
  reaches vs. who waits for value. Needs historical ADP data (not yet available).
- **[caveat]** All of this is descriptive of 2019-2025 behavior; people change. Re-weight toward
  recent years (2023-2025) if a manager's style has visibly shifted, and re-verify against 2026
  behavior once this year's draft happens.
