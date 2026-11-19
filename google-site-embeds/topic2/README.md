# Topic 2 "Charts and data" and "Extension" pages

Eight pages for the Google Site, one pair for each workbook section:

| Section | Charts and data | Extension |
|---|---|---|
| 2.1 Trade and financial flows | `charts-trade.html` | `extension-trade.html` |
| 2.2 Balance of payments | `charts-bop.html` | `extension-bop.html` |
| 2.3 Exchange rates | `charts-exchange-rates.html` | `extension-exchange-rates.html` |
| 2.4 External stability (Topic 3) | `charts-external-stability.html` | `extension-external-stability.html` |

Each page is embedded on its Sites page with the usual iframe loader, so a push to this folder shows up
without editing Sites.

## What updates by itself
- `data/series.json` is rewritten every day by `scripts/update_series.py` (a step in the
  "Update Economy at a Glance data" GitHub Action) from Reserve Bank statistical tables I1, H1, I5, F11,
  F11.1 and I2. Every chart marked **Live chart**, the tiles, the "What to notice" notes and the model
  answers in the Investigate tasks are worked out from that file when the page loads.
- The "Current case studies" lists read `evidence-finder/data/evidence.json` and show the four newest
  items tagged to the section (2A, 2B, 2C or 3D).

## What is checked by hand: `data/manual.json`
- `partners`: top five export markets and import sources (ABS calendar-year release, about February).
- `twi`: TWI weights (Reserve Bank, each January).
- `bop_latest` and `year`: dollar figures from the ABS balance of payments release (early March, June,
  September and December).

## Rebuilding
`python3 build_topic2.py` rewrites the eight pages. Rebuild only when wording, workbook page numbers or
slide numbers change (they are in `SEC` at the top). `site_pages.json` holds the Google Sites addresses
of the child pages so the pages can link to each other on the site. `t2.js` is the chart code (plain
SVG, no libraries) and `t2.css` the styles.

## Testing the data job
`python3 scripts/update_series.py --fixtures DIR --out /tmp/out.json` reads `<table>-data.csv` files
from DIR instead of rba.gov.au. The job never replaces a block with one that ends earlier or is much
shorter, and leaves a block alone if a table cannot be downloaded.
