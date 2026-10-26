# Protection explainer

Interactive student explainer for HSC Economics (Topic 1, Protection): consumer surplus, producer surplus and
deadweight loss under a tariff, a quota and a subsidy.

- **Page:** `index.html` is one self-contained file (no build step). Fonts load from Google Fonts; everything else is inline.
- **Published at:** `/protection-explainer/` on the GitHub Pages site, which deploys the whole repo on every push to `main`.

## The market

Demand `Q = 100 - P`, supply `Q = P`, world price `$20`, price in $, quantity in millions, surplus in $ millions.
Notation follows the Topic 1 deck: P1, Pw, Q1 to Q4, areas a to d. Quotas are taught without importers' extra revenue or an S+quota curve (not "quota rent").

| Tool | Setting | Consumer loss | Producer gain | Revenue or cost | Deadweight loss |
|---|---|---|---|---|---|
| Tariff | $15 | 1,087.5 | 412.5 | +450 government | 225 (b and d) |
| Quota | 30 | 1,087.5 | 412.5 | none shown | 225 (b and d) |
| Subsidy | $15 | 0 | 412.5 | -525 taxpayers | 112.5 (b) |

Formulas used in the script (`t` tariff, `s` subsidy, `P1` protected price): tariff DWL = t squared, revenue = t(100 - 2 x P1),
quota price P1 = (100 - quota) / 2, subsidy cost = s(20 + s), subsidy DWL = s squared / 2.

## Two ways to draw a quota

The quota tab has a "Quota drawing" switch (state `qs`). **Price line** (default) draws the new price like the tariff diagram. **Vertical line** reproduces textbook Figure 2.8: only D and vertical supply lines S, S1 (increase in quota) and S2 (decrease in quota),
with P, P1, P2 and Q, Q1, Q2. The quota is the whole supply, so price = 100 - quota (state `qv`, slider 38 to 70). This style shows prices and quantities only (no surplus or deadweight loss).
The price-line quota diagram has no revenue rectangle (c) and the comparison table compares tools on prices, quantities and imports only.

## Editing

All text, the question bank (`QUIZ`), the exam checklist (`CHK`) and the Australian cases are in `index.html`.
To change the market, edit `calc()` and the fixed values `20`, `80` and `100` in `drawPlot()` together, then re-check the
comparison table, the worked-example table and the "Try this" lines, which quote results for the default numbers.

- **Related page:** `../diagram-lab/` is the shading-free practice lab for the same market. The two pages link to each other from the header, the lab section (explainer) and the footer.
