# Updating the figures

The page reads four files in `data/`. Nothing else needs changing when figures change.

| File | What it holds |
|---|---|
| `data/glance.json` | The 32 boxes on booklet page 67 (`panel`: C, I, G or XM) |
| `data/scorecard.json` | The scorecard rows on pages 68–69 (latest, previous and earlier releases) |
| `data/policy_rates.json` | The bars in the policy-rates chart |
| `data/meta.json` | "Last updated" date, and which figures the daily job manages |

## Updated automatically every day (GitHub Action)

`scripts/update_rba.py` reads RBA statistical tables (which republish ABS data) at 6:23pm Sydney time
and updates these figures **only when a newer release is out**:

| Box / row id | Figure | RBA table · series |
|---|---|---|
| `unemp`, `unempsc` | Unemployment rate | H5 · GLFSURSA |
| `partic`, `particsc` | Participation rate | H5 · GLFSPRSA |
| `wpi` | Wage Price Index, year-ended | H4 · GWPIYP |
| `saving` | Household saving ratio | H2 · GGDPICHDISR |
| `debtinc` | Household debt to income | E2 · BHFDDIT |
| `gdp` (scorecard) | Real GDP growth, year-ended | H1 · GGDPCVGDPY |
| `tot`, `totsc` | Terms of trade, % change | H1 · GOPITT |
| `capct` | Current account, % of GDP | I1 · HCAGSCPGDP |
| `cash`, `lastchg`, `cashsc`, RBA bar | Cash rate target and changes | A2 · ARBAMPCNCRT, ARBAMPCCCR |
| `audchg`, `audsc` | AUD/USD and its change over the year | F11.1 · FXRUSD |
| `twi`, `twisc` | Trade-weighted index | F11.1 · FXRTWI |

The job never replaces a figure with an *older* one: `meta.json → auto.<id>.asOf` records the date
of the figure on show. When the job updates a box it rewrites that box's note too.

## Checked weekly (by Claude, or by hand)

Everything else: CPI and trimmed mean (monthly CPI isn't in the RBA tables the job reads),
underutilisation, minimum wage, population, capital expenditure, productivity, NAB business
confidence, company profits, all Government boxes (budget.gov.au), current account $b, China
growth, world growth, net foreign liabilities/debt, the other scorecard rows, and overseas policy rates.

### Rules for the weekly check

1. Look each figure up in its official release (ABS, RBA, budget.gov.au, NAB, Fair Work Commission,
   NBS, IMF WEO, Federal Reserve, ECB, Bank of England, Bank of Japan). Only change a figure when a
   newer release is out, and update its `period`, `note` and (for the scorecard) shift
   latest → previous → earlier.
2. In each box's `note`, put the previous figure in bold with `**…**`,
   e.g. `Up from **3.5%** in Jul.` The page shows it in bold.
3. Keep the existing formats: Unicode minus `−`, `%` on rates, `$…b` for billions, periods such as
   `Sep 2026`, `Jun qtr 2026`, `14 Oct 2026`.
4. Don't edit the auto-managed ids above unless the job has stopped working. If you do set one of
   them from a fresher source (e.g. monthly CPI), set its `meta.json → auto.<id>.asOf` to the
   period's end date so the job doesn't overwrite it with an older figure.
5. Set `meta.json → updated` to the current time (ISO 8601, UTC) and `weeklyCheck` to today's date.
6. Commit with a message listing what changed, and push to `main`. The push redeploys the site.

## Running the job by hand

GitHub → **Actions** → **Update Economy at a Glance data** → **Run workflow**.
Warnings (e.g. a table that couldn't be downloaded) appear on the run summary and in
`meta.json → updaterWarnings`; affected boxes keep their previous figures.
