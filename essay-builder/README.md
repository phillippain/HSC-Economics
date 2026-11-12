# Extended Response Builder

A planning tool for HSC Economics Sections II, III and IV. The student chooses a past question, unpacks it,
plans each paragraph (or each short-answer part) with statistics from the Evidence Finder and a suggested
diagram, then checks, copies or prints the plan. It plans a response; it does not write one.

- **Page:** `index.html` is one self-contained file (built, do not edit by hand).
- **Published at:** `/essay-builder/` on the GitHub Pages site, which deploys the whole repo on every push to `main`.
- **Embedding:** same pattern as the other tools: `…/essay-builder/?embed=1`, with `theme=light|dark` and `fw=h09|y12`.

## The four steps

| Step | What the student does |
|---|---|
| 1 Choose a question | Filters by section, topic, directive or search. Section II is chosen as a whole question with all its parts. |
| 2 Unpack it | Sees the directive words (NESA glossary), the dot points examined, the time guide, the stimulus description and the top-band criteria. Essays: key terms, a judgement scale when the directive calls for one, and a thesis. |
| 3 Plan | **Sections III and IV:** the booklet's economics paragraph (p. 43): Point, then one to three Explain → Diagram → Evidence cycles, a Stimulus line in Section III, then Link & judge. **Section II:** a plan sized to the marks, using the booklet's Outline and Explain key word scaffolds; calculations get formula, working and answer. |
| 4 Review | Outline of the plan, a checklist, copy as text, print or save as PDF. |

## Where the content comes from

Nothing is held twice. `build.py` reads:

- `../hsc-question-finder-site/index.html`: every Section II, III and IV question (2002 to 2025), its dot points, stimulus description and band criteria (2009 to 2025), and the paper links.
- `../evidence-finder/data/evidence.json` and `syllabus.json`: the evidence items, their statistics, the two HSC syllabus trees and the 2009 to 2025 crosswalk.
- `../evidence-finder/build/fonts.css`: the fonts, inlined.

On the live site the page also fetches `../evidence-finder/data/evidence.json` each time it opens, so new evidence
appears without a rebuild. A rebuild is only needed when the Question Finder changes or the template is edited.

```
python3 essay-builder/build.py           # write index.html
python3 essay-builder/build.py --check   # change nothing; fail if index.html is out of date
```

## The syllabus switch

Past questions carry 2009 dot points. On **2025 syllabus** the tags show the nearest 2025 sections through the
crosswalk, and evidence is matched on its 2025 tags at section level.

## Editing

All in `template.html`:

- `MOVES`: the paragraph scaffold, with the booklet's wording and examples.
- `VERB`: the directive words and which ones call for a judgement.
- `DG`: the diagram catalogue (sketch, what it is for, what to label). `SUG` maps each 2009 syllabus section to the diagrams suggested for it.
- `scaf()` and `nPts()`: how a short-answer part is given its scaffold and number of points.

Plans are kept in the browser (`localStorage`, key `econ-er-builder-v1`), one per question.
