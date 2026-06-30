# ADR 0002: IDP is in scope

Status: confirmed 2026-06-30

## Decision

The league's single `D` roster slot starts one individual defensive player per week
(positionally flexible across DL/LB/DB), not a team-defense slot. IDP player evaluation
(tackle volume, role stability, scheme fit, pass-rush opportunity) is therefore in scope
for FootyBot, not dead weight from Yahoo's default scoring template.

## Why this needed confirming

The league's scoring settings include a full IDP stat table (solo/assist tackles, sacks,
INTs, forced fumbles, etc.) but only one `D` roster slot — which on its own is ambiguous:
many Yahoo leagues carry these default values without ever using them because there's no
roster slot for individual defenders. Confirmed directly with the user that this league
does use it.

## Consequence

The data pipeline and breakout-comp work need to cover defensive players, not just offense
— a meaningfully different evaluation problem (tackle opportunity/role rather than
target share/red zone touches).
