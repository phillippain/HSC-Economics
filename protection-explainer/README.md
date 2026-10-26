# Protection explainer

Interactive student explainer for HSC Economics (Topic 1, Protection): consumer surplus, producer surplus and
deadweight loss under a tariff, a quota and a subsidy.

- **Page:** `index.html` is one self-contained file (no build step). Fonts load from Google Fonts; everything else is inline.
- **Published at:** `/protection-explainer/` on the GitHub Pages site, which deploys the whole repo on every push to `main`.

## The market

Demand `Q = 100 - P`, supply `Q = P`, world price `$20`, price in $, quantity in millions, surplus in $ millions.
Notation follows the Topic 1 deck: P1, Pw, Q1 to Q4, areas a to d, and "importers keep the extra revenue from the higher price" (not "quota rent").

| Tool | Setting | Consumer loss | Producer gain | Revenue or cost | Deadweight loss |
|---|---|---|---|---|---|
| Tariff | $15 | 1,087.5 | 412.5 | +450 government | 225 (b and d) |
| Quota | 30 | 1,087.5 | 412.5 | +450 importers | 225 (b and d) |
| Subsidy | $15 | 0 | 412.5 | -525 taxpayers | 112.5 (b) |

Formulas used in the script (`t` tariff, `s` subsidy, `P1` protected price): tariff DWL = t squared, revenue = t(100 - 2 x P1),
quota price P1 = (100 - quota) / 2, subsidy cost = s(20 + s), subsidy DWL = s squared / 2.

## Editing

All text, the question bank (`QUIZ`), the exam checklist (`CHK`) and the Australian cases are in `index.html`.
To change the market, edit `calc()` and the fixed values `20`, `80` and `100` in `drawPlot()` together, then re-check the
comparison table, the worked-example table and the "Try this" lines, which quote results for the default numbers.
