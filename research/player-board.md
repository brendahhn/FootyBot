# PLAYER BOARD — Brendan's league (0.5 PPR, 6pt pass TD, 40+ yd bonuses) — THE COVERAGE LEDGER

> This is the bot's living memory of the draft board AND its record of what it has already told
> Brendan. Ranked in HIS scoring, not PPR. Each player carries `last_covered` / `times_covered` so
> the newsletter STOPS repeating itself (see operating prompt STEP 1 "COVERAGE LEDGER IS LAW").
> Every run: deepen the least-covered players, work DOWN the board to ~pick 180, add new notes
> (never rewrite), keep ADP real (Sleeper-anchored) and sourced.
>
> **TIERS:** S pipeline-computed · A well-sourced · B thin · C archetype/estimate · Spec = labeled bet.
> **v1 seed (2026-07-06, interactive):** half-PPR points below are tier **C** — my arithmetic on
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
All 25 above: `times_covered: 1`, `last_covered: 2026-07-06` (this seed). Do NOT re-lead any of
them without something new. Rank ordering above is a v1 value estimate — refine with real ADP.

## WATCHLIST — must get worked in (Brendan-requested or under-covered)
- **Rounds 2-6 / picks 17-71 depth** — Brendan: stop parking on the top 12, dive into these.
- **Which BUILDS win in his league** (RB-RB-WR vs WR-WR-RB vs Zero-RB) — data exists
  (`draft_history_enriched.csv` × `league_finishes.csv`); run the correlation. Deep-dive candidate.
- **Pick-100-to-180 universe** — the board must extend past BTJ/Christian Watson (his complaint).
- **QB-environment regression** — e.g. "Jacoby Brissett passed at an all-time-high rate in 2025,
  will regress if/when he plays" — systematize QB up/downgrade → skill-player impact.
- **CeeDee splits** — Dak-on/off and Pickens-on/off before re-projecting (the lazy version skipped this).
- Real half-PPR ADP for every name above (Sleeper primary + FantasyPros/Underdog/RotoWire).

## SETTLED — do NOT re-litigate nightly (already covered; only revisit if NEW)
- Rashee Rice legal situation — priced in, out of jail ~full health per his notes. Settled 2026-07-06.
- Josh Jacobs / other lawsuit re-mentions — settled, stop repeating.
- David Montgomery traded to Houston (Gibbs = bell cow) — known fact, not a debate.
- A.J. Brown traded to New England — known fact.
- "Is CMC worth the pick" / "CeeDee vs Pickens" as a nightly debate — settled framing; only new data moves it.
