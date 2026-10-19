# HSC Legal Studies Question Finder

A past-paper question finder for HSC Legal Studies, built on the same architecture as the
HSC Economics finder in the parent folder. Questions are organised by syllabus content point,
by themes and challenges, and by directive verb and demand band.

Open `index.html`. It is a single self-contained file — no build step needed to use it.

## What is in it

Every extended-response question from 2011 to 2025, the life of the 2009 syllabus:

| Section | Topic | Questions |
|---|---|---|
| II Part B | Crime | 15 — one per year, no (a)/(b) alternative |
| III | Family (Option 3) | 30 — fifteen years × parts (a) and (b) |
| III | Shelter (Option 5) | 30 — fifteen years × parts (a) and (b) |

Still to come: Section I objective response (20 marks — **15 from Crime, 5 from Human Rights**)
and the Human Rights short answers of Section II Part A, plus NESA marking guidelines and
sample answers.

## How questions are tagged

Each question carries a **core** focus — the elements it is built on, which you cannot answer
without — and **supporting** elements, expected as evidence or context. This mirrors the
●/○ coverage matrices in the three survey documents under `source-documents/`, and the tags
were extracted from those matrices rather than re-derived.

Extended responses are tagged at **section level** (`crime.4` Sentencing and punishment), not
at individual dot point, because a 15- or 25-mark answer draws on a whole section. Selecting a
dot point therefore shows its section's questions, marked with an arrow on the count so the
inheritance is visible. Dot-point-level tagging arrives with the objective-response questions.

## Files

```
index.html                  the site — open this
data/syllabus.json          tag taxonomy: topics, themes, sections, dot points, directives
data/items-extended.json    one record per question, with core[]/support[] tag arrays
build/extract_surveys.py    reads source-documents/ -> data/items-extended.json
build/build_site.py         syllabus.json + items -> index.html
build/template.html         the page, with __DATA__ as the data placeholder
source-documents/           the three 2026 survey documents the tags come from
```

## Rebuilding

```sh
pip install python-docx pdfplumber
python3 build/extract_surveys.py     # re-reads the survey documents, verifies the tallies
python3 build/build_site.py          # rewrites index.html
```

`extract_surveys.py` finishes by recomputing each survey's core-focus tally from the extracted
tags and comparing it against the tally printed in that document. All 42 elements across the
three documents match. If a tally ever disagrees, the matrix was misread — fix that before
trusting the output.

## Notes on the source documents

- The Shelter survey is a PDF. Its matrix alternates the year label between columns 0 and 1,
  and the rotated column headers extract as reversed text, so the reader aligns on the last
  fourteen columns and asserts the column order from the document's own column key.
- The Crime and Family surveys are `.docx`; their matrices are read directly from the tables.
- Question stems are taken from the first paragraph of each cell; the coloured tag line beneath
  is redundant with the matrix and is discarded.

Questions and papers © NSW Education Standards Authority. Content points and themes from the
Legal Studies Stage 6 Syllabus (Board of Studies NSW, 2009).
