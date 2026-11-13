# Calculation Trainer

Randomised practice for every calculation HSC Economics asks for, with the working shown after each answer.
Calculations were one of the weak spots this suite was built to address, and the booklet's examiner notes call
them "easy marks for the students who get them correct".

- **Page:** `index.html` is one self-contained file (built, do not edit by hand).
- **Published at:** `/calculation-trainer/` on the GitHub Pages site.
- **Embedding:** `…/calculation-trainer/?embed=1`, with `theme=light|dark`.
- **Links in:** `#skill=mult` (any skill id below), `#view=quiz`, `#view=sheet`.

## The fifteen skills

| Topic | Skills (id) |
|---|---|
| 1 | Real growth rate (`growth`), real GDP per capita (`percap`), tariff imports and revenue (`tariff`) |
| 2 | Current account balance (`cab`), balance of payments identity (`bop`), terms of trade (`tot`), exchange rate changes (`fx`) |
| 3 | Real GDP and real growth from nominal GDP (`realgdp`), net foreign liabilities (`nfl`), the simple multiplier (`mult`), leakages and injections (`leak`), unemployment and participation rates (`labour`), inflation rate (`infl`), Gini coefficient (`gini`) |
| 4 | Budget outcome (`budget`) |

Most skills have several question types (the multiplier has seven), chosen at random, so 39 question types in all.
The formulas are worded as in the course booklet's "Calculations in Economics" pages.

## The three views

| View | What the student does |
|---|---|
| Practise | Picks a skill and answers question after question with fresh numbers. "Show the formula" is available before answering. After checking: right or wrong for each part, the full working, and the error to watch for. A tally and a streak are kept for each skill in the browser. |
| Mixed quiz | Ten questions, one each from ten different skills, with no formula hints, then a score and buttons to practise the ones missed. |
| Formula sheet | Every formula on one printable page, with the HSC questions that examined it. |

Answers accept `$`, `%`, commas and a minus sign. A one-decimal answer is accepted within rounding. Pressing
Enter checks the answer.

## How the questions are made

Each skill is an entry in the `SK` list in `template.html` with a `gen()` function that picks numbers, chosen so
answers come out clean, and returns the question, the answer parts, the worked steps and a "watch for" line.
To change a skill's wording or number ranges, edit it there. `build.py` inlines the fonts and adds the "examined"
lists, read from the Question Finder's questions tagged as calculations (the `CODES` map in `build.py` says which
dot points belong to which skill).

```
python3 calculation-trainer/build.py           # write index.html
python3 calculation-trainer/build.py --check   # change nothing; fail if index.html is out of date
```

Terms of trade is included although the booklet marks it "not needed in the current syllabus", because it was
examined in 2020 and 2025; the page says so.
