# PLAYER BOARD — Brendan's league (0.5 PPR, 6pt pass TD, 40+ yd bonuses) — THE COVERAGE LEDGER

> This is the bot's living memory of the draft board AND its record of what it has already told
> Brendan. Ranked in HIS scoring, not PPR. Each player carries `last_covered` / `times_covered` so
> the newsletter STOPS repeating itself (see operating prompt STEP 1 "COVERAGE LEDGER IS LAW").
> Every run: deepen the least-covered players, work DOWN the board to ~pick 180, add new notes
> (never rewrite), keep ADP real (Sleeper-anchored) and sourced.
>
> **TIERS:** S pipeline-computed · A well-sourced · B thin · C archetype/estimate · Spec = labeled bet.
> **v1 seed (2026-07-08, interactive):** half-PPR points below are tier **C** — my arithmetic on
> Brendan's own PPR projections (subtract ~0.5 × projected receptions, add back for explosive
> 40+ yd profiles), NOT independent projections. Lane A must replace these with pipeline-computed
> his-scoring numbers. ADP column is TO BE SOURCED by Lane C (Sleeper half-PPR primary) — WebFetch
> is blocked so hard numbers weren't pullable from search snippets this session; do NOT treat the
> round tiers below as real ADP, they're placeholders until sourced.

## THE HALF-PPR RESCORE (the correction Brendan asked for)

His projections were full-PPR. In 0.5 PPR the reception-hogs take 40-88 pt haircuts while pure
runners barely move — this reshuffles the board toward RB.

| Player | Pos | 2026 situation (current-reality) | ~Rec | His PPR # | ~Half-PPR (C) | Move vs PPR |
|---|---|---|---|---|---|---|
| Jonathan Taylor | RB | Colts, workhorse | ~40 | 350 | **~330** | ▲ big riser |
| Derrick Henry | RB | Ravens, near-pure rush + 40yd bonuses | ~15 | 275 | **~272** | ▲ big riser |
| Jahmyr Gibbs | RB | Lions, **Montgomery TRADED to HOU → bell cow** | ~52 | 360 | ~340 | ▲ (baseline, not upside) |
| Bijan Robinson | RB | Falcons, Allgeier gone, Stefanski run game | ~60 | 355 | ~325 | ▲ |
| Ashton Jeanty | RB | Raiders, Kubiak zone + Linderbaum, sophomore | ~40 | 300 | ~285 | ▲ riser |
| Saquon Barkley | RB | Eagles, more under-center | ~45 | 275 | ~255 | ▲ riser |
| CMC | RB | 49ers, age 30, health-gated | ~85 | 350 | ~305 | ● (health) |
| Puka Nacua | WR | Rams, target hog, Stafford health | ~110 | 335 | ~285 | ▼ |
| JSN | WR | Seahawks, Klint gone/Shaheed in | ~100 | 330 | ~280 | ▼ |
| Ja'Marr Chase | WR | Bengals, boom/bust + deep bonuses | ~120 | 310 | ~258 | ▼ faller |
| Rashee Rice | WR | Chiefs, health/games-gated, legal SETTLED | ~90 | 300 | ~255 | ▼ |
| Chase Brown | RB | Bengals, role-fragile | ~55 | 275 | ~250 | ● |
| Omarion Hampton | RB | w/ Mike McDaniel scheme (per notes) | ~45 | 270 | ~250 | ▲ |
| Amon-Ra St. Brown | WR | Lions, pure reception volume | 140-175 | 320 | **~235-250** | ▼▼ biggest faller |
| CeeDee Lamb | WR | Cowboys, Dak health is the real risk (not Pickens) | ~95 | 280 | ~232 | ▼ |
| Kenneth Walker | RB | Seahawks, explosive + Mahomes-return upside | ~35 | 240 | ~225 | ● |
| Justin Jefferson | WR | Vikings, Kyler? (per notes) + deep bonuses | ~95 | 290 | ~248 | ▼ |
| Jeremiah Love | RB | rookie (Spec), Cardinals landing per notes | ~40 | 265 | ~245 | Spec |
| Nico Collins | WR | Texans (+Montgomery now), deep bonuses, health flags | ~75 | 275 | ~245 | ▼ |
| Brock Bowers | TE | Raiders, Kubiak (fed JSN 1800/10), better OL | ~90 | 300 | ~255 | ● holds (TD/big-play) |
| De'Von Achane | RB | Dolphins, Willis QB, boom/bust, offense-gated | ~80 | 300 | ~265 | ▼ (checkdown floor halved) |
| Drake London | WR | Falcons, Stefanski + Tua, spiky | ~95 | ~255 | ~210 | ▼ |
| A.J. Brown | WR | **Patriots (TRADED), Drake Maye, McDaniel spreads it** | ~75 | 250 | ~215 | ▼ + wider range |
| Trey McBride | TE | Cardinals, pure reception volume | ~100 | 250 | **~200** | ▼▼ biggest TE faller |

## KEY RESHUFFLES vs Brendan's PPR mock order
- **Risers (pure/low-rec runners): Jonathan Taylor, Derrick Henry, Jeanty, Saquon.** Henry & JT
  especially — their value is rush yards + TDs + 40yd bonuses, almost untouched by the haircut.
- **Fallers (reception-hogs): ARSB (biggest, −70 to −88), McBride, CeeDee, London, JSN, Chase.**
- **ARSB "solid 320" is really ~245 in your league** — half his value was the 140-175 catches Yahoo
  only half-credits. "ARSB over Cook for sure" is NOT for sure; it's close.
- **Bowers holds / gains relative** — TDs + big plays, not empty catches. Your Bowers>McBride take
  is *more* right in half-PPR.
- Reminder: these inherit Brendan's own (optimistic) projections. Lane A to compute independently.

## COVERAGE LEDGER (times_covered / last_covered)
All 25 above: `times_covered: 1`, `last_covered: 2026-07-08` (this seed). Do NOT re-lead any of
them without something new. Rank ordering above is a v1 value estimate — refine with real ADP.

## REAL 2025 PPG ANCHORS [S] — pipeline-computed, this league's scoring (from 2026-07-08 run)
Do NOT re-run or re-explain these; build on them. CMC RB1 21.51 · Puka WR1 19.41 · JSN WR2 17.67
(35.8% tgt share, 0.888 WOPR) · Chase 15.69 · Rashee Rice 15.45 (8 gms) · James Cook 16.81 ·
Saquon RB14 13.36 · CeeDee WR11 12.57 · George Pickens WR6 14.44 · Justin Jefferson 9.38 (2 TDs,
30.1% tgt share — TD-variance buy-low) · Tee Higgins WR12 12.14. Under 6pt-pass scoring the top 6
overall 2025 scorers were all QBs.

## WATCHLIST — must get worked in NEXT (Brendan-requested / under-covered / NEW ground only)
The next run must go HERE, not back to the top-12 names above (all covered 2026-07-08).
- **Rounds 2-6 / picks 17-71 player dossiers NOT yet written** — build them out. Priority.
- **Pick-100-to-180 universe** — extend the board past BTJ/Christian Watson (his direct complaint).
- **Which BUILDS win in his league** (RB-RB-WR vs WR-WR-RB vs Zero-RB) — `draft_history_enriched.csv`
  × `league_finishes.csv`; run the correlation. Top deep-dive candidate — NOT yet done.
- **QB-environment regression layer** — e.g. "Jacoby Brissett passed at an all-time-high rate in
  2025, regresses if/when he plays"; systematize QB up/downgrade → skill-player impact. NOT done.
- **Real half-PPR ADP** for every name (Sleeper primary + FantasyPros/Underdog/RotoWire) — the
  2026-07-08 run pulled top-6 shape only; extend it and attach a sourced number per player.

## NEWS ALREADY REPORTED [do NOT re-lead unless it MOVES] — through 2026-07-08
- Rashee Rice: cleared, no 2026 suspension, released Jun 16, knee scope ~6wk (TC-ready). Only NEW
  monitor = the late-July knee checkpoint.
- Malik Nabers: 2nd knee scope, Week-1/PUP risk, played 4 games in 2025. Injury-discount siren.
- Patrick Mahomes: 2025 ACL, targeting Wk1 but likely opens PUP.
- JSN: 4yr/$168.6M extension (March) — no holdout/drama.
- David Montgomery → Houston (Gibbs = bell cow); A.J. Brown → New England (Maye, McDaniel spreads it).

## TAKES ALREADY CHECKED [do NOT re-litigate without NEW evidence] — through 2026-07-08
- "James Cook overvalued" → AGREE (bid up to ~RB6; 16.81 PPG = fine not elite). Don't chase at 17.
- "CMC is a post-injury trap" → RETIRED. Healthy RB1 in 2025 (17 gms). Fade is age/workload only;
  may be VALUE at 6-7. Pass at 4 on positional-value grounds, not injury.
- "CeeDee vs Pickens / fade one" → RESOLVED by 2025 shared-field data: both startable (Lamb led
  tgts 116-99), coexist; Pickens caps Lamb's ceiling not value; the REAL risk is Dak's health/
  volume (correlated bet if you draft both). DO NOT re-deep-dive this.
- "Tee Higgins — bank on him but he's not [good]" → WR2, fine (12.14). Marginal, don't re-litigate.
- Injury-discount PATTERN ALARM → made repeatedly. Raise ONLY when he circles a NEW specific
  injury name, with the extra-round-of-discount ask; do not re-run the generic warning.

## SETTLED FACTS — known, not debates
- Montgomery→HOU, AJB→NE (above). Rice legal closed. "Is CMC worth pick 4" = decided (pass, value reason).
