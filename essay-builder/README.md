# Extended Response Builder

A planning tool for HSC Economics Sections II, III and IV. The student chooses a past question, unpacks it,
plans each paragraph (or each short-answer part) with statistics from the Evidence Finder and a suggested
diagram, then checks, copies or prints the plan. It plans a response; it does not write one.

- **Page:** `index.html` is one self-contained file (built, do not edit by hand).
- **Published at:** `/essay-builder/` on the GitHub Pages site, which deploys the whole repo on every push to `main`.
- **Links in:** `#q=IV-2025-28` (section, year, question number) opens that question; the Chain Builder uses this.
- **Embedding:** same pattern as the other tools: `…/essay-builder/?embed=1`, with `theme=light|dark` and `fw=h09|y12`.

## The four steps

| Step | What the student does |
|---|---|
| 1 Choose a question | Filters by section, topic, directive or search. Section II is chosen as a whole question with all its parts. |
| 2 Unpack it | Sees the directive words (NESA glossary), the dot points examined, the time guide, the stimulus description and the top-band criteria. Essays: key terms, a judgement scale when the directive calls for one, and a thesis. |
| 3 Plan | **Sections III and IV:** the booklet's economics paragraph (p. 43): Point, then one to three Explain → Diagram → Evidence cycles, a Stimulus line in Section III, then Link & judge. **Section II:** a plan sized to the marks, using the booklet's Outline and Explain key word scaffolds; calculations get formula, working and answer. |
| 4 Review | A list of every diagram in the response, then the outline of the plan, a checklist, copy as text, print or save as PDF. |

## Planning diagrams (added 19 November 2026)

Each Explain → Diagram → Evidence cycle (and each Section II part that asks for a diagram) has a **diagram plan**:

1. **Model:** choose from the catalogue, with suggestions from the question's syllabus tags.
2. **What changes?** (AD–AS, demand and supply, dollar, labour market, negative externality, Phillips curve, PPF, Lorenz curve): the sketch redraws with the original curve, the new curve in red, equilibrium points, guides and axis labels.
3. **Cause:** what in the Explain chain moves the curve (a prompt lists typical causes).
4. **Caption:** "Use the suggested caption" writes the Figure sentence from the chosen shift (the student can edit it).
5. **In the text:** where the response refers to the figure.
6. **Draw it:** for AD–AS, the dollar, the labour market, the externality and the Lorenz curve, the button opens the Macro Diagram Lab with the chosen shift and the label style already set (`LABQ` in `template.html` maps each shift to the lab's preset address; the lab reads it in `readHash`). Tariff, quota and subsidy link to the Protection Diagram Lab without a preset; the Phillips curve and PPF have no lab yet.

Figures are numbered in reading order across the response. The labels switch between **AD₁ → AD₂** (default) and **AD → AD₁** (booklet p. 43 style); AS is the upward-sloping curve, called SRAS only when LRAS is drawn. Step 3 and step 4 both show an overview (thumbnail, shift, paragraph, and whether the cause, caption and text reference are done), with notes on paragraphs that have no diagram and on a model used more than twice. The plan check, copy text and print page carry the same detail.

To add a shift or diagram, edit `SC` (shifts, causes and captions), `MKT` (two-curve markets) or `CAP` (diagrams with one standard caption) in `template.html`. Sketches are drawn by `mktBody`, `phBody`, `ppfBody` and `lzBody`. Plans saved before this change load unchanged.

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
