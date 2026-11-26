# Worksheet Maker

Builds printable HSC Economics worksheets as PDFs, with a matching answer copy. The teacher (or a student)
chooses dot points and skills, the types of question and where they come from, then sets the page layout
and downloads the files.

- **Page:** `index.html` (built from `template.html`; do not edit by hand). It loads `data.json`, the PDF
  maker in `lib/` and the fonts in `fonts/` from this folder, and the past-paper figures from
  `../hsc-question-finder-site/figs/`, so it must stay beside the Question Finder.
- **Published at:** `/worksheet-maker/` on the GitHub Pages site. Embed it in the Google Site with the usual
  iframe loader; inside an embed an **Open in a new tab** button appears, because some browsers block
  downloads from embedded pages.
- **From the Question Finder:** its **Make a PDF worksheet ↗** button (added by
  `build/link_worksheet_maker.py`) opens this page with the ticked questions, as `?qf=I2019Q1,II2019Q21(a),...`.
  **Add my Question Finder ticks** does the same from inside this page when both run in the same browser.
- **Other links in:** `?embed=1`, `?theme=light|dark`.

## The three steps

| Step | What it does |
|---|---|
| 1 Choose questions | Tick 2009 dot points (or 2025 sections through the crosswalk); optionally narrow to skills (calculation, diagram, explain, the syllabus “learn to” points and so on); set how many of each of the 17 question types; choose the sources and the level. **Make the worksheet** spreads the picks across the dot points. Each question can be moved, swapped, edited or removed; past HSC questions have **Look-alike**. **Pick questions one by one** searches everything. |
| 2 Layout and print | Four page styles (HSC exam, workbook, adapted, compact) and settings for the header, order, marks, sources, dot points, part breaks, answer space (lines, dots, box or none, and how much), extended response pages, a planning box, word banks, sentence starters, one or two columns, diagram tasks on blank axes or the starting diagram, answers at the end, and Version B (questions and options reordered). The preview is the real PDF, drawn with pdf.js. |
| My worksheets | Saved in this browser (`localStorage`, key `econ-worksheet-maker-v1:saved`); save to and open from a file to move them between computers. |

## The 17 question types

| Group | Types | Where they come from |
|---|---|---|
| HSC exam formats | Multiple choice, short answer, source-based, extended response | Past HSC papers (Question Finder), the new bank, the Evidence Finder's questions on news items |
| Diagrams and calculations | Calculations, draw a diagram, label a diagram, read a diagram | The Calculation Trainer's generators (new numbers each time); the bank, drawn with `build/econ_diagrams.py` |
| Knowledge checks | Match terms, fill the gaps, define, true or false | Made fresh from the Glossary (terms matched to dot points in `bank/maps.json`); true/false from the Chain Builder and `bank/tf.txt` |
| Thinking tasks | Cause and effect chain, put in order, sort and classify, compare, spot the error | The Chain Builder, the Topic Map's pathways, and the bank |

## Building

```
python3 worksheet-maker/build.py            # write data.json, index.html and review.html
python3 worksheet-maker/build.py --check    # change nothing; fail if any of them is out of date
python3 worksheet-maker/build.py --report   # also list how many questions each dot point has, by group
python3 worksheet-maker/build.py --artifact <folder>   # also write the Claude copy (see below)
```

Rebuild after the Question Finder, the Glossary, the Chain Builder, the Topic Map, the Calculation Trainer,
the multiple-choice explanations or the bank change. News filed in the Evidence Finder after a build still
appears: the page reads `../evidence-finder/data/evidence.json` when it opens.

The build stops with a message if a bank question is malformed, a dot point code is unknown, a glossary term
has no dot point in `bank/maps.json`, or a diagram code cannot be drawn.

## The new question bank

`bank/*.txt` holds the questions written for this tool (335 at 26 November 2026, plus 101 true/false
statements). They are plain text; `bank/README.md` explains the format. Every one shows **not yet reviewed**
until the teacher checks it: `review.html` lists them all with their answers. Mark a checked file by making its
first line `# reviewed`, or one question by adding `checked: yes` under its heading.

## Writing new questions with Claude

Claude can write new questions for the chosen dot points, with answers:

- **More like my worksheet** (the first choice under *What to write*): new questions in the same style as those
  already on the worksheet for the dot point picked under *Dot point*, or as past HSC and bank questions on it when
  the worksheet has none yet. It keeps the mix of types (as many again of each, shared out across *How many*),
  and Claude copies each example's format, marks, NESA verb, difficulty and kind of stimulus with new scenarios
  and data. Calculations and key-term tasks are made by the page itself (the same skills with new numbers, or new
  terms); Claude does not write label-a-diagram tasks.
- **A set of one type**: any of ten types, at one of three levels.
- On each question card: **Look-alike by Claude** and **Simpler wording** (plain English, about Year 7).
- Every Claude question is marked **check before printing** in the list (not on the printed sheet) and stays in
  the worksheet, not in the bank.

Where Claude comes from:

- **On the website**, a teacher sets it up once on each computer with their own **Anthropic API key**
  (**Set up Claude…** in the panel, or *Claude settings*). The page checks the key with a one-line request,
  then keeps it in that browser only: `localStorage` key `econ-worksheet-maker-v1:claude-key`, or
  `sessionStorage` (gone when the browser closes) when *Remember the key* is off. The key is sent only to
  `api.anthropic.com` (Messages API, `anthropic-version: 2026-10-21`, the
  `anthropic-dangerous-direct-browser-access` header that allows calls from a web page, effort `medium`, and
  `anthropic-workspace-id` when a workspace ID is given for a key that has no workspace). Create the key at
  `platform.claude.com/settings/keys` and choose a workspace for it (Default is fine). Each
  batch is charged to the key's account; Sonnet 5.5 is the default (Opus 5.5 and Haiku 5.5 can be chosen).
  Only question text and syllabus wording are sent. Without a key the panel just offers the set-up, and the
  Claude buttons stay hidden, so students see no change. Every page on `phillippain.github.io` shares that
  browser storage, so set it up only on a computer you trust, and use *Forget my key* on any other.
- **The Claude copy** (a claude.ai artifact, **HSC Economics Worksheet Maker**) uses Claude in the page instead
  (the `sample` capability) and offers no key set-up. To republish it after a rebuild, run the build with
  `--artifact <folder>` and ask Claude to publish that folder to the existing artifact; it needs the `sample`
  and `downloads` capabilities. Artifacts may load scripts only from a few sites, so the copy loads pdfmake and
  pdf.js from `cdn.jsdelivr.net` (the same pinned versions as `lib/`) and runs pdf.js on the page rather than
  in a worker. The build marks it with `window.WM_ARTIFACT = true`.

Error messages name the usual causes: a key that is not accepted, an account out of credit, Claude busy, or a
network that blocks `api.anthropic.com` (some school networks do).

## Files

| File | What it is |
|---|---|
| `template.html` | The page: HTML, CSS and the app. The calculation generators are copied in at build time between the `/*__CALC__*/` markers. |
| `build.py` | Gathers every source into `data.json` and writes `index.html` and `review.html` |
| `build/bank.py` | Reads the bank files; writes the review page |
| `build/diagrams.py`, `build/econ_diagrams.py` | Diagram codes → SVG in the house style |
| `build/fonts.py` | How the font files were cut (run once; not part of the build) |
| `bank/` | The new questions, and `maps.json` (glossary terms, Topic Map nodes and calculation skills → dot points) |
| `lib/` | pdfmake 0.2.23 (MIT) and pdf.js 3.11.174 (Apache 2.0), with their licences |
| `fonts/` | Liberation Sans (exam style), Carlito (workbook and compact), Lexend (adapted), DejaVu Sans (symbols): SIL Open Font Licence / Bitstream Vera licence |

Tested in headless Chrome: every question type in all four styles, student and answer copies, answers at the
end, Version B, the 2025 syllabus, Question Finder import, browse, edit, swap, look-alike, save and reopen,
and phone width. The Claude features were tested against a stand-in for the API (key check, More like my
worksheet, one type, errors, Stop, remembering and forgetting the key), not against Anthropic itself. Not
tested by students, on the school network or inside the Google Site.
