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
- **Rounds 2-6 / picks 17-71 player dossiers** — STARTED 2026-07-09 (ADP + situational notes for
  ~24 names sourced, see below). Keep deepening pros/cons + comps per player.
- **Pick-100-to-180 universe** — STARTED 2026-07-09 (BTJ ~64, Christian Watson ~73, Worthy ~101
  now sourced). Push deeper to 120-180 next.
- ~~**Which BUILDS win in his league**~~ — **DONE 2026-07-09**, Finding 7 in `draft-tendencies.md`
  + `pipeline/draft_builds.py`. Verdict: mostly a wash; RB-heavy opens edged the field, Zero-RB/
  WR-heavy never podiumed — but inside the noise band; pick quality >> build shape. Don't punt RB.
- ~~**QB-environment regression layer**~~ — **DONE 2026-07-09**, `research/qb-environment.md`
  (Brissett/ARI 649-att mirage → McBride/Wilson/MHJ fades; Chase anti-fade; DeVonta up). Extend
  to more teams as QB situations settle.
- **Real half-PPR ADP** — rounds 2-6 sourced 2026-07-09 (tier B, single ESPN mock + tier A Underdog
  aggregate). **STILL OPEN: Sleeper** — its per-player numbers are JS-hidden and WebFetch is blocked,
  so scheduled runs can't anchor on Sleeper. Needs a Brendan-pasted Sleeper export to upgrade B→A.
  Also unresolved: Bucky Irving (25 vs 45) + Javonte Williams (26 vs 74) ADP conflicts.

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
- **Which build wins (2026-07-09):** decided — no build "wins"; pick quality dominates shape. Don't
  punt RB (Zero-RB never podiumed). Take elite WR value at 4, secure a real RB by 17. Do not re-run.
- **Bucky Irving "Coen merchant" (2026-07-09):** REFUTED — held 12.35 PPG in 2025 without Coen
  (Grizzard OC) vs 12.99 with him. Not a scheme artifact. Real caution = shoulder procedure +
  3rd playcaller in 3 yrs + snap-share, NOT the merchant angle. Do not re-litigate the merchant take.
- **Chase "Bengals volume regression" fade (2026-07-09):** REFUTED — 185 tgt / 125-1,412-8 with
  Burrow out 9 games = own-role, not environment. Do NOT fade Chase for volume regression.

## ROUNDS 2-6 / DEEP BOARD — sourced half-PPR ADP (added 2026-07-09, Lane C)
`times_covered: 1`, `last_covered: 2026-07-09` for all below unless already on the top board.
Tier B = single dated ESPN 10-team ½-PPR mock (~Jul 2026); tier A = Sharp Football aggregated
Underdog ½-PPR ADP (~Jul 2026). Sleeper NOT extractable this run (JS-hidden + WebFetch blocked) —
do not treat any of these as Sleeper/consensus; they are one real datapoint each.

| Player | Pos/Team 2026 | ½-PPR ADP | Tier | Note |
|---|---|---|---|---|
| Jonathan Taylor | RB IND | ~7 | B | |
| Justin Jefferson | WR MIN | ~11 | B | buy-low (2-TD outage regresses); Murray→MIN rumor = QB tailwind if real |
| Ashton Jeanty | RB LV | ~12 (Sleeper ~9) | B | |
| De'Von Achane | RB MIA | ~13 | B | |
| Drake London | WR ATL | ~16-20 | B | |
| Nico Collins | WR HOU | ~17 | B | **VALUE at pick 17** — HOU WR1 target hog |
| Derrick Henry | RB BAL | ~18 | B | NOT a trap in THIS scoring (40yd bonus + 6pt rush TD, ½-credit rec) — riser. Fine RB fallback at 17 |
| Omarion Hampton | RB LAC | ~19 | B | |
| Chase Brown | RB CIN | ~21 | B | |
| Trey McBride | TE ARI | ~22 (TE1) | B | modest FADE off 2025 counting stats (169 tgt won't repeat, ARI volume regresses) — still TE1 |
| Josh Jacobs | RB GB | ~23 | B | legal tail-risk unresolved (DA reviewing) |
| Brock Bowers | TE LV | ~24 (TE2) | B | **VALUE at pick 24** — elite young TE |
| Kenneth Walker III | RB SEA | ~19-26 (thin) | B | |
| Breece Hall | RB NYJ | ~28 | B | |
| Kyren Williams | RB LAR | ~29 | B | soft — TD-dependent, committee risk, weak ½-PPR floor |
| Rashee Rice | WR KC | ~30, falling | B | if he keeps sliding = BUY (cleared, WR5-PPG over 8 gms) |
| A.J. Brown | WR NE | ~32 | B | UP — alpha WR1 for ascending Maye; age-29 risk |
| Tetairoa McMillan | WR CAR | ~34 | B | |
| DeVonta Smith | WR PHI | ~36 | B | **VALUE at pick 37** — inherits AJB's ~121 tgt; capped by run-heavy PHI + rookie Makai Lemon |
| Luther Burden III | WR CHI | ~55 (WR24) | A | |
| Marvin Harrison Jr | WR ARI | ~56-64 (WR25) | A | QB-capped bounce-back (Brissett/Beck); don't pay ceiling |
| Jaylen Waddle | WR MIA | ~62 | B | |
| Brian Thomas Jr | WR JAX | ~64 (WR32) | A | biggest WR faller (WR8→WR32); TLaw-rebound value bet |
| Christian Watson | WR GB | ~73 (WR33) | A | |
| Xavier Worthy | WR KC | ~101 (WR46) | A | |
| Michael Wilson | WR ARI | unsourced | — | AVOID at 2025 price — purest ARI environment-rider (126 tgt on injury luck + NFL-top volume) |

**Unsourced / do not guess:** James Conner (RB ARI), Ladd McConkey (WR LAC), Rome Odunze (WR CHI),
Jerry Jeudy (WR CLE). **Conflicting, uncommitted:** Bucky Irving (25 vs 45), Javonte Williams (26 vs 74).

## NEWS added 2026-07-09 [do NOT re-lead unless it MOVES]
- Kyler Murray RELEASED by ARI [A]; reported Vikings interest [B]. → Brissett = ARI's 2026 starter;
  Murray→MIN would upgrade JJ's environment (watch, don't bank).
- Bijan extension "expected soon" [A, a report not a signature] — removes hold-in noise; still gone before 4.
- Jameson Williams "best offseason" per Lions WR coach [A/B camp narrative] — R3-4 WR, 40yd-bonus fit.
- Chris Olave extension talks stalled, hold-in on the table [B, ongoing] — durability/volume flag.
- Josh Jacobs legal: UNCHANGED [A] — DA "under review," no charge decision (WTMJ Jul 6).
