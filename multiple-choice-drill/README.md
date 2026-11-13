# Multiple Choice Drill

Every HSC Economics Section I question from 2009 to 2025 (340 questions, 17 papers) as interactive practice.

- **Page:** `index.html` is one self-contained file (built, do not edit by hand). Figure images are loaded from `../hsc-question-finder-site/figs/`, so the two folders must stay side by side.
- **Published at:** `/multiple-choice-drill/` on the GitHub Pages site.
- **Embedding:** `…/multiple-choice-drill/?embed=1`, with `theme=light|dark` and `fw=h09|y12`.
- **Links in:** `#view=paper`, `#view=results`.

## The three views

| View | What the student does |
|---|---|
| Drill | Chooses a topic (and a part of it), which questions (all, not yet right, never tried, wrong last time), calculations only, papers from a given year, and how many. Questions come at random; after each answer the correct option is shown with what the question tested, its dot points, and links to the Calculation Trainer (for calculation questions), the Evidence Finder and the Glossary. Ends with a score by topic, the questions to go over, and "Redo the ones I missed". Keys A to D answer. |
| Past paper | Sits one year's Section I in paper order, with a 35-minute countdown (optional). Questions can be answered in any order and changed; nothing is marked until the paper is handed in. |
| My results | Latest result for every question tried: totals, a bar for each topic, and dot points listed weakest first with a "Drill it" button each. "Drill everything I have not got right" builds a set from past mistakes. |

Results are kept in the browser (`localStorage`, key `econ-mc-drill-v1`).

## Where the content comes from

Nothing is held twice. `build.py` reads, from the Question Finder page: each question's text and four options,
its tables, option tables and figure images, NESA's answer key, its dot points and the one-line note on what it
examined. The build stops if a question lacks four options or a well-formed key.

- **Two accepted answers:** NESA accepted two options for 2010 Q16, 2020 Q7 and 2022 Q7. Either is marked right, and the feedback says so.
- **No explanations:** NESA publishes the key only, so feedback says what a question tested, not why each wrong option is wrong.
- **Syllabus switch:** questions carry 2009 dot points. On "2025 syllabus" the topic filter and tags use the nearest 2025 sections through the Evidence Finder's crosswalk.

```
python3 multiple-choice-drill/build.py           # write index.html
python3 multiple-choice-drill/build.py --check   # change nothing; fail if index.html is out of date
```

Rebuild after the Question Finder changes (for example when the 2026 paper and its key are added).
