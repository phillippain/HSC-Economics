# Protection diagram lab

Independent student site for HSC Economics (Topic 1, Protection). It lets students experiment with a tariff, a quota and a subsidy
using the diagram only: there is no consumer surplus, producer surplus or deadweight loss shading anywhere.
Related page: `../protection-explainer/` (the surplus and deadweight loss explainer, which uses the same market).

- **Page:** `index.html` is one self-contained file with no build step. Fonts load from Google Fonts; everything else is inline.
- **Published at:** `/diagram-lab/` on the GitHub Pages site, which deploys the whole repo on every push to `main`.
- **Direct links:** `#experiment`, `#predict`, `#challenges`, `#build`.

## The four parts

| Part | What the student does |
|---|---|
| Experiment | Chooses a tool, moves the world price and the tariff, quota or subsidy, and toggles layers (quantity labels and guide lines, import brackets, revenue or cost rectangle for tariff and subsidy, point letters). A "Show numbers" switch hides every value so values must be read from the axes. |
| Predict | Six preset scenarios. Student predicts the change in six measures (consumer price, producer price, domestic output, consumption, imports, and for a tariff or subsidy where the money goes; five measures for a quota), then checks. Each answer has a reason; the finished diagram appears after checking. |
| Challenges | Eight targets with a slider, readout, hint and check (for example, cut imports to 40, find the revenue-maximising tariff, find the quota that matches a $10 tariff). |
| Build it | Student drags a handle (or uses the buttons or arrow keys) to draw the new price line (tariff), the quota (price line or vertical line, see below) or the shifted supply curve S1 (subsidy). When correct, the rest of the diagram is added one piece at a time. |

## The market

Demand `Q = 100 - P`, supply `Q = P`, world price `Pw` (default $20, adjustable from $10 to $40). Price in $, quantity in millions.
No-trade price is $50. Free-trade quantities: Q1 = Pw (domestic output) and Q2 = 100 - Pw (consumption).

| Tool | Setting | New price P1 | Q3 (output) | Q4 (consumption) | Imports | Money |
|---|---|---|---|---|---|---|
| Tariff t | 0 to 50 - Pw | Pw + t | P1 | 100 - P1 | 100 - 2 x P1 | revenue = t x imports after |
| Quota q | 0 to 100 - 2 x Pw | (100 - q) / 2 | P1 | 100 - P1 | q | none (no rectangle for quotas) |
| Subsidy s | 0 to min(40, 100 - 2 x Pw) | consumers still pay Pw; producers receive Pw + s | Pw + s | 100 - Pw | 100 - 2 x Pw - s | cost = s x (Pw + s) |

Wording follows the Topic 1 deck: P1, Pw, Q1 to Q4. Quotas have no S+quota curve and no importers' extra revenue, and "quota rent" is not used.

## Two ways to draw a quota

Every part that shows a quota has a "Quota drawing" switch (shared variable `qstyle`). **Price line** (default) draws the new price like a tariff; in Build it the handle moves up the price axis.
**Vertical line** draws a vertical line at Q4, the total quantity once the quota applies, and the price is read where it meets D (adapted from the textbook figure with vertical supply lines); in Build the handle moves along the quantity axis.
Changing the switch in Build resets the quota drawing.

## Point letters (assumption to check)

For a tariff, A, B, C, D are the corners of the revenue rectangle going clockwise from the top left (on a quota diagram, where there is no rectangle, the same four points mark the ends of the import gap):
A = (Q3, P1) on S, B = (Q4, P1) on D, C = (Q4, Pw), D = (Q3, Pw).
For a subsidy, A = (Q3, Pw + s) on S and B = (Q3, Pw) on S1, so AB is the subsidy per unit.
If the teacher's protection sheets letter the corners differently, change the `letter` calls near the end of `drawDiagram()` in `index.html`.

## Editing

- Scenarios: `SC` (Predict), `BS` (Build it), `CH` (Challenges, each with a check function `ok`, hint and worked answer).
- Reasons shown after a Predict check: `why()`.
- The model is `model(tool, w, amt)` and the ranges are `ranges(tool, w)`. The diagram is drawn by `drawDiagram()`.
- If the demand or supply equations change, update `model()`, `ranges()` and the fixed quantities in the challenge text and answers together.

- **Links:** the header and footer link to `../protection-explainer/index.html`, and that page links back here. If either folder is renamed, update the `href`s in both pages.
