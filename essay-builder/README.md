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

## Layout: one step at a time (redesigned 23 November 2026)
The builder is a wizard. Only the current step shows; the four step buttons at the top and the Back / Next buttons at the bottom move between steps, and choosing a question opens step 2.
- **Step 2** has two parts: A "Understand the question" and B "Plan your introduction". The thesis steps, ideas and model thesis open only when asked for.
- **Step 3 (essays)** opens with an **essay map**: a block for the introduction, each paragraph and the conclusion, with a dot for each move that fills in when the move is done. One paragraph shows at a time. Each paragraph has a **flow chart of its moves** (Point → Explain → Diagram → Evidence → Link & judge, with Stimulus in Section III and up to three Explain–Diagram–Evidence cycles); clicking a move shows only that move. Help for the move sits beside it under **Questions, Ideas and Model** tabs, according to the support level. The evidence list shows only on the Evidence move.
- **Chains as flow charts**: an Explain chain typed with → between steps and ↑ or ↓ after a variable is drawn as linked boxes (green for a rise, red for a fall) as the student types, and in the ideas, model and review page.
- **Step 3 (Section II)** has a map of the parts and shows one part at a time; ideas and the model are folded away.
- Each move and each support level has its own icon and colour, used the same way everywhere.

Code in `template.html`: `applyStep` / `goStep` (wizard), `essayMap`, `pflowHTML`, `movePanel`, `mvList` / `mvState`, `flowHTML`, `ICON`. A plan remembers the open paragraph (`open`) and each paragraph's current move (`mv`).

## Your own evidence (added 23 November 2026)
The evidence list in step 3 has a third tab, **My evidence**. A student adds a **statistic** (figure, what it measures, source, date), a **case study** fact (economy, defaulting to China), **stimulus** from the question's paper (offered only when the question has stimulus, and kept with that question) or another **example**. Items are saved in the browser as a personal bank and offered in every plan; they can be edited, deleted, and saved to or loaded from a backup file (`my-economics-evidence.json`) to move between devices. In the plan they are marked "your own" or "from the stimulus", and the plan check asks that each of the student's own statistics has a source and a date.

## Levels of support (added 23 November 2026)
A switch above step 2 lets the student choose how much help they see. Each level adds to the one before.
0. **On my own**: prompts and examples only (the builder as it was).
1. **Sentence starters**: starters and linking words under each box, fitted to the directive; a click drops one into the box.
2. **Guiding questions**: questions for each move, and five steps that join the student's answers into a draft thesis. The reasons can be dropped into a paragraph's Point.
3. **Suggested ideas**: possible points for the syllabus section, cause and effect chains from the Chain Builder (a click fills the Explain box) and the best-matching Evidence Finder statistics.
4. **Worked model**: a model thesis and a model paragraph (plan beside the written paragraph, each move marked) for a different question in the topic; a model short answer in Section II.

The suggested points and the worked models are in `data/support.json` and are meant to be edited: `points` by 2009 syllabus section, `models` (each lists the sections it is shown for) and `s2`. The models quote dated figures (`asAt`), so refresh them each term. The chains are read from `chain-builder/data/chains.json`. Run `build.py` after changing either file. The starters and guiding questions are in `template.html` (`starters`, `guideQs`).

## Choosing by topic and section (added 23 November 2026)
Under the Section II / III / IV buttons, a **Topic** list and a **Section** list narrow the questions to one part of the syllabus, for example Topic 1 > 1E Case study. Each entry shows how many questions it holds in the paper section chosen. Picking a section also sets its topic. The lists follow the syllabus switch (2009 sections such as 1E, or the 2025 focus areas matched through the crosswalk), and the switch clears them. A heading above the list gives the count. A link can open the picker on a section: `essay-builder/?s=IV&sec=1E` (paper section and syllabus section id; `Y3d` and similar open the 2025 lists).

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
