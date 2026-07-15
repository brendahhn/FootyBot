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
| Kenneth Walker | RB | **CHIEFS (signed 3yr/$43.05M FA — CORRECTED 2026-07-15, not Seahawks)**, lead back, Mahomes pass-funnel | ~40 | 240 | ~225 | ● (role up, price up) |
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
| Kenneth Walker III | RB **KC** | ~early-2nd, rising | B | **TEAM CORRECTED 2026-07-15: Chiefs, not Seahawks.** Clear lead back (Pacheco/Hunt gone); 15-18 carries + GL + pass role. Market bid up to early-2nd = analysts call it steep (efficiency-not-volume back in a Mahomes pass-funnel). High-end RB2. |
| Breece Hall | RB NYJ | ~28 | B | |
| Kyren Williams | RB LAR | ~29 | B | soft — TD-dependent, committee risk, weak ½-PPR floor |
| Rashee Rice | WR KC | ~30, falling | B | if he keeps sliding = BUY (cleared, WR5-PPG over 8 gms) |
| A.J. Brown | WR NE | ~32 | B | UP — alpha WR1 for ascending Maye; age-29 risk |
| Tetairoa McMillan | WR CAR | ~34 | B | |
| DeVonta Smith | WR PHI | ~36 | B | **VALUE at pick 37** — inherits AJB's ~121 tgt; capped by run-heavy PHI + rookie Makai Lemon |
| Luther Burden III | WR CHI | ~55 (WR24) | A | |
| Marvin Harrison Jr | WR ARI | ~56-64 (WR25) | A | QB-capped bounce-back (Brissett/Beck); don't pay ceiling |
| Jaylen Waddle | WR DEN | re-source | B | **TEAM CORRECTED 2026-07-12: traded MIA→Denver (March 2026)** — now a Broncos WR1 on a strong offense (upgrade); old ~62 was on the wrong team, re-source his DEN ADP |
| Brian Thomas Jr | WR JAX | ~64 (WR32) | A | biggest WR faller (WR8→WR32); TLaw-rebound value bet |
| Christian Watson | WR GB | ~73 (WR33) | A | |
| Xavier Worthy | WR KC | ~101 (WR46) | A | |
| Michael Wilson | WR ARI | unsourced | — | AVOID at 2025 price — purest ARI environment-rider (126 tgt on injury luck + NFL-top volume) |

**Unsourced / do not guess:** ~~James Conner, Ladd McConkey, Rome Odunze, Jerry Jeudy~~ — **ALL
SOURCED 2026-07-12, see section below.** **Conflicting, uncommitted:** ~~Bucky Irving (25 vs 45),
Javonte Williams (26 vs 74)~~ — **BOTH RESOLVED 2026-07-12 (Bucky ~50, Javonte ~35; see below).**

## NEWS added 2026-07-09 [do NOT re-lead unless it MOVES]
- Kyler Murray RELEASED by ARI [A]; reported Vikings interest [B]. → Brissett = ARI's 2026 starter;
  Murray→MIN would upgrade JJ's environment (watch, don't bank).
- Bijan extension "expected soon" [A, a report not a signature] — removes hold-in noise; still gone before 4.
- Jameson Williams "best offseason" per Lions WR coach [A/B camp narrative] — R3-4 WR, 40yd-bonus fit.
- Chris Olave extension talks stalled, hold-in on the table [B, ongoing] — durability/volume flag.
- Josh Jacobs legal: UNCHANGED [A] — DA "under review," no charge decision (WTMJ Jul 6).

## 2026-07-12 UPDATE (SCHEDULED RUN) — [S] his-scoring PPG + resolved ADP + corrections

### REAL 2025 PPG in his exact scoring [S] — pipeline-computed this run (replaces tier-C estimates)
Regular season only, 0.5-PPR + 6pt pass TD − 2 TO (40+yd bonus still uncomputable → slight
under-count). The "½-haircut" = pts/game lost vs full PPR = exactly 0.5 × rec/game.
`times_covered +1`, `last_covered: 2026-07-12` for all listed.

| Player | 2025 PPG [S] | ½-haircut | Player | 2025 PPG [S] | ½-haircut |
|---|---|---|---|---|---|
| CMC (RB) | 21.51 | −3.00 | Chase Brown (RB) | 14.59 | −2.03 |
| J. Taylor (RB) | 19.96 | −1.35 | George Pickens (WR) | 14.44 | −2.74 |
| Bijan (RB) | 19.49 | −2.32 | Kyren Williams (RB) | 14.43 | −1.06 |
| Puka (WR) | 19.41 | −4.03 | Javonte Williams (RB) | 14.08 | −1.09 |
| Gibbs (RB) | 19.32 | −2.26 | Drake London (WR) | 13.99 (12g) | −2.83 |
| De'Von Achane (RB) | 18.08 | −2.09 | Saquon (RB) | 13.36 | −1.16 |
| JSN (WR) | 17.67 | −3.50 | Nico Collins (WR) | 12.71 (15g) | −2.37 |
| James Cook (RB) | 16.81 | −0.97 | CeeDee (WR) | 12.57 (13g) | −2.88 |
| Derrick Henry (RB) | 16.00 | −0.44 | Bucky Irving (RB) | 12.35 (10g) | −1.50 |
| Ja'Marr Chase (WR) | 15.69 | −3.91 | Tee Higgins (WR) | 12.14 (15g) | −1.97 |
| ARSB (WR) | 15.62 | −3.44 | A.J. Brown (WR) | 12.09 (15g) | −2.60 |
| Trey McBride (TE) | 14.88 | −3.71 | Brock Bowers (TE) | 12.02 (12g) | −2.67 |
| Josh Jacobs (RB) | 14.61 (15g) | −1.20 | Breece Hall (RB) | 11.98 | −1.00 |

**Deep-board upside darts all scored UNDER 10 PPG in his scoring in 2025 [S]** — their value is a
projected 2026 leap, not seen production; price as bets not floors: Christian Watson 11.49 (10g),
K. Walker 10.38, Rome Odunze 10.34 (12g), DeVonta Smith 9.61, Justin Jefferson **9.38** (2-TD
outage → buy-low), Ladd McConkey 9.24 (16g), James Conner 9.77 (**3g only**), MHJ 8.94 (12g),
BTJ 8.20 (14g), Luther Burden III 6.96 (rookie), Xavier Worthy 6.35, Jerry Jeudy 5.63.
**Read:** in his scoring 2025's top 6 were 5 RBs + Puka; pure runners lose almost nothing to the
½-haircut, reception WRs/TE lose 2.6–4.0/game. One-season [S] snapshot, not a law — but aligns with
the 7/9 build study. Don't punt RB.

### ADP conflicts RESOLVED [A]
- **Bucky Irving (RB TB) → ~50 (40-55).** Underdog 47.3, DK 54.5, Drafters 50.0, RotoWire R5. Old ~25
  predated offseason shoulder surgery. ~RB24; creeps to ~40 if 100% by camp.
- **Javonte Williams (RB DAL) → ~35 (30-42).** FP 3.11/RB20, FFC 36.9. Clear DAL RB1 (2025: 1,201/11/
  4.8). Old ~74 stale; market actually calls him *expensive* here, not cheap.

### Newly-sourced deep board [B unless noted] — pushes toward pick 180 (WATCHLIST progress)
George Kittle TE SF ~40 (TE1) · Ladd McConkey WR LAC ~48-56 · Rome Odunze WR CHI ~53-63 · Sam LaPorta
TE DET ~59 · Tony Pollard RB TEN ~64 · Isiah Pacheco RB KC ~69 · T.J. Hockenson TE MIN ~79 (tied to
Murray now) · David Njoku TE CLE ~83 · Zach Charbonnet RB SEA ~96.
- **📉 James Conner RB ARI → ~177 CRATERED [B, 4for4].** ARI drafted **Jeremiyah Love 3rd overall**;
  Conner's workhorse role gone (Love + Benson + Demercado). Dart only.
- **⚠️ Jerry Jeudy WR CLE — ranking ≠ ADP TRAP.** ESPN *ranking* ~WR47 but real redraft ADP **~140-200**
  (CLE drafted 2 WRs top-39). Round-13 flyer, NOT mid-round. Do not let the ranking mislead the board.
- **Clay-rank ordering proxies only (NOT ADP numbers):** Aaron Jones, RJ Harvey (both ~RB29-32 rank),
  Calvin Ridley, Jordan Addison, Khalil Shakir, Jayden Reed. Use as order, not point ADP.

### Achane verdict REFINED (was "boom/bust" → now high-floor/capped)
4yr/$64M ext (3rd-highest-paid RB) = locked workload → **high floor**, but Willis QB (scrambler, cuts
checkdowns → dents his 0.5-PPR receiving edge) + worst-WR-room box-loading + goal-line vulturing
**cap the ceiling**. High-floor volume RB1 with more downside variance than ADP-13; value only if he
slides past pick 4, not a target at 4.

### NEWS added 2026-07-12 [do NOT re-lead unless it MOVES]
- **Kyler Murray SIGNED with Minnesota [A]** (1yr vet-min, done March; ARI eats salary) and **reported
  projected Week-1 starter over J.J. McCarthy.** → firms the **Justin Jefferson buy-low** (from "watch"
  to firmer; not a lock — McCarthy competition + Murray health). Addison/Hockenson tie to Murray now.
- **Brandon Aiyuk (SF) headed for release [A/B]** — won't return to SF, release expected, rehabbing ACL.
  UNDRAFTABLE until he lands somewhere healthy with a role. Watchlist only.
- **Chris Olave [B]:** real risk is medical — **not fully cleared from Dec-2025 lung blood clot**, not
  the contract (no actual hold-in). Monitor camp participation.
- **James Pearce Jr (ATL edge) [B]:** reported 8+ game suspension — fade in IDP calc until length official.
- Bijan unsigned but staying ATL (Falcons extended London 4yr/$141M + Pitts). RJ Harvey full-go post-labrum.

### TAKES CHECKED 2026-07-12 [do NOT re-litigate without NEW evidence]
- **"James Conner — Arizona's O-line better, cool opportunity vs Jeanty" → REFUTED [A+B].** ARI drafted
  Jeremiyah Love 3rd overall; Conner cratered to ~177, buried in a committee; 31 y/o, 3 games in 2025
  (9.77 PPG [S]). Opportunity gone. **Jeanty is the cleaner bet;** Love (not Conner) holds that
  backfield's value. Take can go stale on draft capital — re-check depth charts before committing.

### SETTLED FACTS added 2026-07-12
- Bucky Irving ADP ~50 / Javonte Williams ADP ~35 (both resolved — do not re-run the conflict).
- Jaylen Waddle is a **Denver Bronco** (traded March 2026), not a Dolphin. Tyreek Hill released (FA,
  injured). Tua released; **Malik Willis** is Miami's QB. McDaniel fired → **Chargers OC**; Slowik = MIA OC.

## 2026-07-14 UPDATE (WEEKLY RUN) — Waddle re-priced, deep board 100-180, London QB resolved
`times_covered +1`, `last_covered: 2026-07-14` for every player named in this section.

### Waddle ADP RESOLVED as a Bronco [A]
- **Jaylen Waddle (WR DEN) → ~39-53 (WR19-21).** FantasyPros ~39/WR19; Yahoo ~53/WR21; secondhand
  Sleeper ~46/WR23 (soft, unconfirmed). **Co-WR1 with Courtland Sutton, not a runaway alpha** (Bo Nix
  spreads it — Mims/Franklin/Engram; neither DEN WR may clear 1,000). High-end WR3 / WR2 upside; don't
  reach above ADP. Replaces the old MIA ~62. *(fantasypros, sharpfootball, CBS, fantasylife.)*

### NEW deep-board ADP [B unless noted] — pick ~100-180 (WATCHLIST progress)
Jaylen Warren RB PIT ~78 (RB28, standalone flex) · Rico Dowdle RB PIT ~90 (committee) · Caleb Williams
QB CHI ~98 (streamer, rush ceiling) · Kenneth Gainwell RB TB ~100 (riser) · Bo Nix QB DEN ~107 (QB15,
streamer) · Keon Coleman WR BUF ~120 · **Josh Downs WR IND ~123 (VALUE — 80% snaps late '25, Pittman
gone)** · Jake Ferguson TE DAL ~127 (TE12) · Dallas Goedert TE PHI ~136 (TE15, 11 TD) · Tyjae Spears RB
TEN ~142→155 (**IR-bound, fading**) · Alvin Kamara RB NO ~152 (aging/faller) · **Tank Bigsby RB PHI
~166 (cheap Saquon handcuff — NOTE he's an Eagle now, not a Jaguar)**.
- Buried past 180 (confirm, don't draft): Trey Benson ARI ~290, James Conner ARI ~177, Braelon Allen NYJ ~205.
- **QB-STREAMER TIER forming ~pick 95-110** (Caleb Williams ~98, Bo Nix ~107, + late Lawrence/Mayfield):
  the 6pt-pass-TD wait-on-QB edge. Do NOT spend 17/24 on a QB.

### RISERS / FALLERS (this week)
- 📈 A.J. Brown → No. 16 (NE alpha for Maye, top value-riser); JSN → ~32-37; Gainwell → top 100;
  Tony Pollard rising (Spears IR).
- 📉 Chuba Hubbard falling (NFLN: Panthers expect Jonathon Brooks lead back); Kamara −5 → ~152;
  Conner −10 → ~177.

### NEWS added 2026-07-14 [do NOT re-lead unless it MOVES]
- **Malik Nabers (NYG) opening camp on PUP** after a 2nd knee procedure — October debut in play [A].
  Injury discount siren; he's Year 3, so this is injury, not any age pattern.
- Risk-discount trio firmed, none resolved [A on quotes]: Rice (Reid expects on-time report, "no
  indication" of suspension — easing not gone), Jacobs (DA case still open, practicing), Mahomes ("way
  ahead of schedule," Wk1 trend + PUP contingency). Draft all three at a discount, not clean price.
- Vikings QB1: O'Connell noncommittal on Murray vs McCarthy [B, non-denial] — JJ stays *firmer buy-low*, not a lock.
- **Drake London PAID [A]:** 4yr/$141M ext (~$35.25M AAV, 3rd among WRs). Role locked.

### TAKE CHECKED 2026-07-14 [do NOT re-litigate without NEW evidence]
- **"Drake London — real QB now, is this the year?" → HALF-RIGHT [A/B].** Role + coaching (Stefanski/
  Rees) are real upgrades; "real QB" is the shaky leg — Atlanta is an **open Penix (ACL, aiming Wk1 not
  guaranteed) vs. Tua (1yr vet-min insurance) competition**, not a settled QB. Draft London as a
  secured-role WR1 with an *upside-bet* QB, not a settled breakout. ("McDaniel merchant" frame is wrong —
  McDaniel's in LAC; the real variable is QB availability.) Corrects our stale "Penix vs. Cousins" note.

### SETTLED FACTS added 2026-07-14
- Atlanta QB 2026 = open Penix(ACL)/Tua competition (NOT Cousins — stale; NOT settled). London extended 4yr/$141M.
- Waddle DEN ADP ~39-53 (resolved). Tank Bigsby is a Philadelphia Eagle (Saquon handcuff), not a Jaguar.
- Rashid Shaheed is on Seattle (our JSN note already had this — confirmed correct).

## 2026-07-15 UPDATE (SCHEDULED RUN) — Walker→KC correction, QB-wait math [S], pick-4 tree, ADP reconciles
`times_covered +1`, `last_covered: 2026-07-15` for every player named in this section.

### ⚠️ BOARD CORRECTION — Kenneth Walker III is a KANSAS CITY CHIEF [A, 6 sources]
Signed **3yr/$43.05M** with KC in March FA (Super Bowl LX MVP for SEA in 2025). Our board had him as a
Seahawk in a committee — DEAD. In KC he is the **clear lead back**: Pacheco (FA) + Hunt gone; KC added
only 3rd-down Demercado + 5th-rd rookie Emmett Johnson. Projected **15-18 carries + goal-line + expanded
pass role** (his words: "used more in the pass game"). 2025 **10.38 PPG [S]** was Seattle-committee-capped;
KC role removes the cap. **PRICE CAVEAT:** ADP bid up to **early-2nd** = PFN/SI call it steep — efficiency-
not-volume back (career 4.6 YPC) in a Mahomes pass-funnel = **high-end RB2 / low-end RB1, not a workhorse.**
Press only in the RB2 range (~pick 24); don't pay the early-2nd ceiling. *(ESPN, NFL.com, Yahoo, Spotrac, PFN, SI.)*
- **Isiah Pacheco (KC ~69, from 07-12) is STALE** — he's a free agent now, undraftable until he lands a role.
- **Zach Charbonnet (SEA):** torn ACL (Feb surgery), out into the 2nd half; SEA backfield now a rookie
  (Jadarian Price)/Wilson/Holani committee. Charbonnet's ~96 is a deep dart at best.

### QB-WAIT MATH [S] — full 2025 QB ranking in his exact scoring (Lane A, new)
6pt pass TD, 25yd/pt, −2 INT, rush; reg season, g≥8. The spread, not the top, is the point:
QB1 Stafford 26.0 · QB2 Allen 25.9 · QB3 Maye 24.3 · QB6 Lawrence 23.3 · QB8 Hurts 21.9 · **QB9 Caleb
Williams 21.8** · QB10 Goff 21.5 · QB11 Herbert 21.2 · QB12 Burrow 21.1(8g) · **QB13 Bo Nix 20.9** · QB18
Mayfield 19.1. **Gap QB6→QB18 = ~4.2 ppg across 12 QBs.** Edge is concentrated in the **top ~3** (Allen
undercounted — 40yd bonus uncomputed helps rushing QBs). Our streamer names (Caleb ~98, Bo Nix ~107) already
scored QB1-adjacent. **VERDICT: wait & stream the ~pick-95-110 QB tier unless a top-3 QB falls to a spot you'd
spend. Don't burn 17/24 on a passer.** (2025 actuals ≠ 2026 projections; low-games QBs noisy.) Reconciles the
`league-scoring-leaders.md` "waiting is costlier" note: true only for the elite top-3, not QB7-18.

### PICK-4 DECISION TREE (countdown content, 44 days out) [A/reasoning]
1-2 = Gibbs/Bijan coin flip (both RBs). Pick 3 is the swing: national ADP says **Chase WR1 goes ~3rd**, but our
room's RB-lean + only-Jack-is-WR-first means **Chase slides to 4 more often than national ADP.**
- **Chase gone → take Jonathan Taylor** (pure workhorse, zero rec-haircut, +2 breakaways, RB scarcity).
- **Chase falls → take Chase** (top-3 talent at 4; the one WR that beats the haircut). The single spot to bend the RB tilt.
- **Both gone (double-RB run + WR-first steal) → De'Von Achane (~13)** over volatile Jeanty.
Preference order **JT ≥ Chase**; the room decides.

### A.J. Brown ADP RECONCILED [A/B]
Board carried both "No. 16" (07-14) and "~32" (table) — contradiction. Truth between: **~pick 22-28, WR8-13,
rising** (Underdog WR8 ~22.5; FantasyPros WR13 ~R3). "No. 16" was WR-rank/overall ambiguity. **USE ~25 (range 22-32).**

### RISERS / FALLERS + NEW deep names (Lane C, this run) [B unless noted]
- 📈 **Quentin Johnston (LAC WR) → ~78 / WR37 [A]** (+36 DK since May, McDaniel YAC scheme) · Aaron Rodgers
  (PIT QB) up ~2 rounds (fits QB-wait thesis) · Rachaad White (TB) up a round → ~109 (Bucky still TB lead) ·
  Jonathon Brooks (CAR) = reported **lead back**, craters Hubbard.
- 📉 Conner ~177 (−10, confirms) [A] · Kamara ~152 (−5) [A] · Aiyuk plummeting on ACL (relative only, no abs #) ·
  **Jeanty volatile ~10 (ESPN)–22 (Yates)** off a 14.3-PPG rookie yr — a RANGE, not a point.
- NEW toward ~180: **Adonai Mitchell (NYJ WR) ~176/WR71** (Jets buzz — cleanest new ~180 dart) · **Greg Dulcich
  (MIA TE) ~185-194 [A consensus]** (best late-TE value, open MIA tree) · Tyler Shough (NO QB) ~QB19 (wait-QB fit) ·
  Chig Okonkwo (TEN TE) ~146 · Ryan Flournoy (DAL WR3) ~168 · **Jordan James (SF RB) — premium CMC handcuff** (CMC 30, led NFL in carries).
- KILLED: "Alec Downs" = garbled Josh Downs/Alec Pierce snippet — NOT a real name, disregard.

### NEWS added 2026-07-15 [do NOT re-lead unless it MOVES]
- **Malik Nabers (NYG, Yr3):** HC Harbaugh "on schedule… better every day," should practice as camp opens; still
  opens PUP but beat floats **~Week 3 debut on a pitch count** (vs prior "Oct debut"). [A quote] — floor firms marginally; still a WR2-with-a-blank-start.
- **Stefon Diggs (FA WR):** Fowler — "5+ teams checking in," unsigned 2 wks pre-camp [B]. Watch-the-signing trigger;
  a WR-thin landing compresses an incumbent's targets. Not actionable at 4.
- Montgomery (HOU) "three-down back" coach color [B, freshness unconfirmed] — props RB2 floor, directional only.
- IDP: blank 24-48h window. Micah Parsons (GB edge) opens PUP, ~Wk5 (old news) — don't start him early; stream the slot.

### TAKE CHECKED 2026-07-15 [do NOT re-litigate without NEW evidence]
- **"Kenneth Walker — polarizing, loves him, Chiefs had zero run game, could see heavy usage" → RIGHT, and ahead
  of us [A].** He IS a Chief (KC's 2025 run game WAS broken — Pacheco knee); he IS the clear lead back (15-18
  carries + GL + pass role). Called the landing AND the why. **Only caveat = PRICE:** market bid him to early-2nd,
  analysts call it steep (efficiency-not-volume in a Mahomes pass-funnel = high-end RB2). Right on thesis; watch the price.

### SETTLED FACTS added 2026-07-15
- Kenneth Walker III = **Kansas City Chief** (3yr/$43.05M FA), clear lead back. Pacheco = FA (gone from KC).
  Charbonnet (SEA) torn ACL, out into 2nd half. Do not re-litigate the team.
- A.J. Brown redraft ADP ~25 (22-32, WR8-13, rising) — the "16 vs 32" contradiction is resolved.
