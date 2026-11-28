# Worksheet Maker

Builds printable Economics worksheets as PDFs, with a matching answer copy: HSC (2009 syllabus, or Year 12 of the
2025 syllabus) and, from 28 November 2026, Year 11 (Preliminary) of the 2025 syllabus. The teacher (or a student)
chooses the course, dot points and skills, the types of question and where they come from, then sets the page
layout and downloads the files.

- **Page:** `index.html` (built from `template.html`; do not edit by hand). It loads `data.json`, the PDF
  maker in `lib/` and the fonts in `fonts/` from this folder, and the past-paper figures from
  `../hsc-question-finder-site/figs/`, so it must stay beside the Question Finder.
- **Published at:** `/worksheet-maker/` on the GitHub Pages site. **For teachers only at present (27 November
  2026):** it is not in the Other tools menu, the Google Site's Tools page, What's New or the Question Finder, and
  the page asks search engines not to list it (`noindex`). Anyone who has the address can still open it, because
  GitHub Pages has no sign-in. If it is embedded in a Google Site page later, an **Open in a new tab** button
  appears inside the embed, because some browsers block downloads from embedded pages.
- **To list it for students later:** uncomment its line in `SITES` in `build/build_sitemenu.py` and run that
  script; run `build/link_worksheet_maker.py` (without `--remove`) to put the Question Finder's **Make a PDF
  worksheet ↗** button back; add its card to `google-site-embeds/tools.html`; and add a What's New line.
- **From the Question Finder:** while the button is out, use **Add my Question Finder ticks** inside this page.
  It reads the ticks when the Question Finder is open at its own address (not inside the Google Site) in the same
  browser. An address in the form `?qf=I2019Q1,II2019Q21(a),...` still opens the page with those questions.
- **Other links in:** `?embed=1`, `?theme=light|dark`.

## The three steps

| Step | What it does |
|---|---|
| 1 Choose questions | Choose the course at the top (**2009 HSC**, **2025 Year 11** or **2025 Year 12**), then tick 2009 dot points or 2025 sections; optionally narrow to skills (calculation, diagram, explain, the syllabus “learn to” points and so on); set how many of each of the 17 question types; choose the sources and the level. **Make the worksheet** spreads the picks across the dot points. Each question can be moved, swapped, edited or removed; past HSC questions have **Look-alike**. **Pick questions one by one** searches everything. |
| 2 Layout and print | Four page styles (HSC exam, workbook, adapted, compact) and settings for the header, order, marks, sources, dot points, part breaks, answer space (lines, dots, box or none, and how much), extended response pages, a planning box, word banks, sentence starters, one or two columns, diagram tasks on blank axes or the starting diagram, answers at the end, and Version B (questions and options reordered). The preview is the real PDF, drawn with pdf.js. |
| My worksheets | Saved in this browser (`localStorage`, key `econ-worksheet-maker-v1:saved`); save to and open from a file to move them between computers. |

## Year 11 (2025 syllabus)

The **2025 Year 11** switch shows the six Year 11 focus areas (`y11` in `evidence-finder/data/syllabus.json`) as
28 sections to tick. A Year 11 worksheet uses only material tagged to the Year 11 course:

- **The Year 11 bank** (`bank/y11-*.txt`, written 28 November 2026, not yet reviewed): 311 questions (147
  multiple choice, 78 short answer and data, 12 extended responses, 32 draw and 6 label tasks, 14 sort, 8 compare,
  8 spot the error, 6 cause and effect chains) and 126 true/false statements, tagged to the Year 11 dot points
  (`c: P2e.3`); every one of the 134 points has at least one. They are reviewed on the Question review page like
  the HSC bank.
- **News** tagged to Year 11 in the Evidence Finder (`about.y11`).
- **Key terms and calculations** that Year 11 uses: Glossary terms and Calculation Trainer skills carry Year 11
  dot points as well as 2009 ones in `bank/maps.json`.
- **Past HSC questions** only if **Past HSC questions** is ticked under step 3 (its own switch for Year 11, off
  at first): the Year 12 questions the class crosswalk links to a Year 11 section (`P6a`–`P6d`, `P1e`, `P2h`,
  `P4c`, `P5b`, `P5c`).

Making a new worksheet in Year 11 sets **Course** (under *Layout and print*, top of the first page) to *Year 11
Economics*, which names the sheet, its footer and its file details; HSC courses use *HSC Economics*. The skills
chips, levels (*Year 11 standard*) and Claude's prompts (Year 11 course, sections such as `P2e`, Year 11 school
exam level, examples from the Year 11 bank) follow the switch. The Year 12 and 2009 choices are kept separately.

New diagram codes for Year 11 (in `build/diagrams.py`): `tax` (per-unit tax: revenue and deadweight loss),
`extern pos` (positive externality in consumption), `ped` and `pes` with `elastic`, `inelastic`, `unit`,
`perfectly-elastic`, `perfectly-inelastic`, `along D fall|rise` and `along S rise|fall` (movements along a curve),
`funds` (loanable funds), `lrac`, `cycle` (business cycle), `ppf points`, and label sets `sd`, `tax`, `pos`, `lrac`,
`cycle`.

## The 17 question types

| Group | Types | Where they come from |
|---|---|---|
| HSC exam formats | Multiple choice, short answer, source-based, extended response | Past HSC papers (Question Finder), the new bank, the Evidence Finder's questions on news items |
| Diagrams and calculations | Calculations, draw a diagram, label a diagram, read a diagram | The Calculation Trainer's generators (new numbers each time); the bank, drawn with `build/econ_diagrams.py` |
| Knowledge checks | Match terms, fill the gaps, define, true or false | Made fresh from the Glossary (terms matched to dot points in `bank/maps.json`); true/false from the Chain Builder, `bank/tf.txt` and `bank/y11-tf.txt` |
| Thinking tasks | Cause and effect chain, put in order, sort and classify, compare, spot the error | The Chain Builder, the Topic Map's pathways, and the bank |

## Building

```
python3 worksheet-maker/build.py            # write data.json, index.html, review.html and review-data.json
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
until the teacher checks it.

**Reviewing them.** The **Question review** page on the staff Tools site
(`phillippain.github.io/Tools/question-review/`) shows every bank question and statement with its answer, and
one click each to **Approve**, flag as **Needs a fix** (with a note) or **Remove**. With a GitHub token connected
once per computer, it saves the decisions to `bank/reviews.json` in this repository (a commit on `main`), and
this page reads that file when it opens:

| Decision | In the Worksheet Maker |
|---|---|
| Approved (`ok`) | Loses **not yet reviewed** |
| Needs a fix (`fix`) | Left out of new worksheets and *Pick questions one by one*; labelled *flagged: needs a fix* on a saved sheet that has it. Ask Claude to fix it from the note, then review it again. |
| Removed (`out`) | Left out the same way; labelled *removed from the bank* |

A decision counts only while the question is unchanged: each one stores the question's fingerprint (`h`, from
`build/bank.py`), so a question edited after it was approved or flagged goes back to **not yet reviewed**. The
build writes `review-data.json` (every bank question with its fingerprint and answer) for the review page.
Without a token the page keeps the decisions in that browser and offers **Copy decisions for Claude**.
`review.html` (a plain list of the unreviewed questions) still works and links to the review page.

You can still mark a whole file as checked by making its first line `# reviewed`, or one question by adding
`checked: yes` under its heading.

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
| `build.py` | Gathers every source into `data.json` and writes `index.html`, `review.html` and `review-data.json` |
| `build/bank.py` | Reads the bank files, fingerprints each question; writes the review list and the Question review page's data |
| `bank/reviews.json` | The teacher's decisions from the Question review page (saved there; don't edit by hand unless asked) |
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
