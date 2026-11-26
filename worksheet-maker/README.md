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

## The Claude copy

The same page, published as a claude.ai artifact, can also ask Claude to write new questions for the chosen
dot points (any of ten types, three levels, Year 12 or plain-English wording), a look-alike of any question, or
a plain-English rewording. Claude's questions are marked **check before printing** and are kept in the
worksheet, not in the bank. To republish it after a rebuild, run the build with `--artifact <folder>` and ask
Claude to publish that folder to the existing artifact (**HSC Economics Worksheet Maker**); it needs the `sample` and
`downloads` capabilities. Artifacts may load scripts only from a few sites, so the copy loads pdfmake and pdf.js from
`cdn.jsdelivr.net` (the same pinned versions as `lib/`) and runs pdf.js on the page rather than in a worker.

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
and phone width. Not tested by students, on the school network or inside the Google Site.
