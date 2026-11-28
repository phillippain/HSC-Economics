# Filing a new item

Each item is one object in `data/evidence.json`. Put the PDF (if any) in `files/YYYY-MM/`, add the record, then run `python3 build/build_site.py`.

## From the inbox

Items dropped in `HSC_Economics_SSCBWB / Evidence Finder / inbox` are listed by `python3 build/ingest.py status`. For each one, choose the id, then `python3 build/ingest.py file "<inbox name>" <id> --label "Original article"`: it puts the PDF in `files/YYYY-MM/`, moves the original to `filed/` on the drive and prints the `file` block to paste into the record. The daily news task also drops its summaries here with an index (`_index-<date>.json`); `status` then shows which PDFs are the same story (`SAME STORY as`) and any `possible existing card`. For a pair, file the HSC summary with `file`, then the Year 11 one with `file "<name>" <same id> --as year11`, which prints the `file11` block. If the story already has a card, add the new PDF to that card (`--as year11` with the card's id) or `archive` it; do not make a second card. Use `archive` for a dropped link or note once its story is filed, and for duplicates. Finish with `python3 build/ingest.py refresh --commit "<message>"`. See the README for more.

## A record

```json
{
  "id": "2026-10-19-china-q3-gdp",
  "title": "China's growth beats forecasts, but investment slump deepens",
  "date": "2026-10-19",
  "dateText": "16–19 Oct 2026",
  "type": "news",
  "outlets": ["Reuters", "SCMP", "ABC News"],
  "summary": "One sentence on why it matters for an answer.",
  "lede": "Two sentences on what happened.",
  "about":  {"h09": ["1E.1", "1A.8"], "y12": ["Y3e.3"], "y11": []},
  "also":   {"h09": ["2D.4"],         "y12": ["Y3c.4"], "y11": ["P6a.2"]},
  "issues": ["global", "trade", "growth"],
  "levers": ["trade"],
  "diagrams": ["flow"],
  "figures": [
    {"label": "China GDP growth, year to Sept quarter", "value": "4.5%", "asAt": "Sept qtr 2026 (forecast 4.4%)", "issue": "growth", "source": "Reuters via Investing.com"}
  ],
  "terms": [{"term": "Terms of trade", "def": "Export prices divided by import prices."}],
  "angle": "How to use it in an answer.",
  "questions": [{"q": "Outline what is meant by a 'balance-sheet recession'.", "marks": 2}],
  "extended": "Optional extended-response question.",
  "note": "Optional caveat, such as 'secondary report; check the original'.",
  "file": {"path": "files/2026-10/2026-10-19-china-q3-gdp.pdf", "label": "Student handout", "pages": 3},
  "links": [{"label": "Reuters via Investing.com, China's economic growth accelerates, 19 Oct 2026", "url": "https://..."}]
}
```

A card can carry a second document, `file11`, for the Year 11 version of the same story:

```json
  "file11": {"path": "files/2026-10/2026-10-19-china-q3-gdp-year11.pdf", "label": "Year 11 version", "pages": 1}
```

One story is one card. When a story has both an HSC summary and a Year 11 summary, the HSC summary is `file` and the Year 11 summary is `file11`; tag the card in all three syllabuses. A Year 11-only story uses its Year 11 summary as `file`. The card shows both buttons, with the Year 11 one first in the Year 11 view.

Required: `id`, `title`, `date`, `type`, `outlets`, `summary`, `lede`, `about`, `also`, `issues`, `levers`, `diagrams`, `figures`, `terms`, `links`, `file`. Use empty lists where nothing applies. `dateText`, `angle`, `questions`, `extended` and `note` are optional.

## Tagging

- **`about`** means the evidence answers that dot point directly. Keep it to the few dot points an examiner would reach for it on. These drive the coverage map.
- **`also`** means it helps but is really about something else. One sentence in an answer, not a paragraph.
- Tag against all three syllabuses where you can (`h09`, `y12`, `y11`). If an item is only tagged in one, it still appears in the others at section level through the crosswalk, with a note that it is not yet tagged there.
- Dot point codes are in `data/syllabus.json`. 2009 codes look like `3C.3`, Year 12 (2025) like `Y1c.4`, Year 11 (2025) like `P2d.1`.

## Vocabularies

| Field | Values |
|---|---|
| `type` | `news`, `stats`, `report`, `graph`, `case` |
| `issues` and each figure's `issue` | `growth`, `employment`, `inflation`, `rates`, `fx`, `trade`, `investment`, `housing`, `budget`, `inequality`, `environment`, `productivity`, `global` |
| `levers` | `fiscal`, `monetary`, `micro`, `labour`, `environmental`, `trade`, `global` |
| `diagrams` | `adas`, `ds`, `phillips`, `fx`, `flow`, `chart`, `compare` |

New values go in `build/make_syllabus.py`, then rebuild both files.

## Figures

Add the statistics worth quoting, with `asAt` (the period or date it describes) and `source`. Keep `value` short and put qualifiers in brackets, for example `"4.7% (trend 4.6%)"`: the part before the bracket is shown large, the rest small. Figures feed the Statistics tab.

## Checking

`build_site.py` rejects unknown tags and missing files. After building, open `index.html`, find the new card, and check that it appears under the dot points you tagged and that its links work.
