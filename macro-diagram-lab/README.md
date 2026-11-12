# Macro Diagram Lab

Interactive diagrams for HSC Economics beyond protection: **AD–AS**, the **market for the Australian dollar**,
the **labour market** (with a minimum wage), the **Lorenz curve** and a **negative externality**. It sits beside
the Protection Diagram Lab (`../diagram-lab/`), which keeps tariffs, quotas and subsidies.

- **Page:** `index.html` is one self-contained file (built, do not edit by hand).
- **Published at:** `/macro-diagram-lab/` on the GitHub Pages site.
- **Embedding:** `…/macro-diagram-lab/?embed=1`, with `theme=light|dark`.
- **Links in:** `#d=adas|fx|labour|lorenz|extern`, `&view=scenarios`.

## The two views

| View | What the student does |
|---|---|
| Experiment | Moves sliders to shift the curves (or change the Gini coefficient, the external cost, the tax). The diagram redraws in the house diagram style: original curve and point in grey, new ones in red, dashed guides to both axes. Under it is **the sentence that earns the mark**, rewritten for the diagram as it stands, with a copy button. "What shifts each curve?" and an exam checklist sit beside it. |
| Scenarios | Reads an event, predicts which curve shifts, which way, and what happens to each axis variable, then checks. The diagram and its sentence are revealed with the reason. 29 scenarios in all. |

## Curve labels

The switch in the masthead chooses between `AD₁ → AD₂` (the style of the class diagram sheets and news explainers)
and `AD → AD₁` (the style of the worked example on booklet page 43). The choice is remembered in the browser.

## The models

The diagrams are conceptual and not to scale. Curves are straight lines in a 0 to 100 space with slope 0.8, so a
shift of one curve moves price and quantity in the textbook directions. The Lorenz curve is a smooth curve with
exactly the chosen Gini coefficient (the average of x^k and its mirror image, where Gini = (k − 1) ÷ (k + 1));
the quintile shares shown are read from that curve and are not ABS figures. The two "Australia" buttons use the
booklet data bank's Gini coefficients (0.307 income, 0.606 wealth, ABS 2022–23).

## Editing

Everything is in `template.html`, in the `DG` object: names, axis labels, the factors that shift each curve, the
exam checklist and the scenarios. A shift scenario is `[text, 'dn' or 'up' (which curve), 1 or -1 (right or left),
reason]`; the right answers for price and quantity are worked out from that. Then:

```
python3 macro-diagram-lab/build.py           # write index.html
python3 macro-diagram-lab/build.py --check   # change nothing; fail if index.html is out of date
```
