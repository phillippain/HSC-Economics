# Topic explainer pages (Topics 2, 3 and 4)

One page per syllabus heading. Each page has two parts, side by side on a computer and stacked on a phone:

- `<page>-text.html`: the textbook-style explanation (800 to 1,200 words), pasted into a normal Google Sites text box.
- `<page>-figures.html`: numbered figures as one embed (live headline tiles, data chart, diagrams, flow chart, table).
  The text refers to them as Figure 1, Figure 2 and so on.

Figure 1 tiles load from `economy-at-a-glance/data/glance.json` each time the page opens, so they stay current
with the daily data update. The values written into the HTML are only a fallback.

Build: `python3 build_explainer.py inflation` (needs the hsc-econ-diagrams script on the path). Content for each
page lives in `page_<name>.py`.

The Sites embed is only a small loader: it fetches `<page>-figures.html` from GitHub Pages, so a new or changed
figures file appears on the site after a push, with no edit in Google Sites. The last block of the figures file is the
'Practise with the tools' buttons, which reuse the icons from `build/build_sitemenu.py`.

Pilot page: Inflation (Topic 3), 14 November 2026.

## More resources heading

`more-resources.html` is the icon heading (gold folder on a cobalt square, "MORE RESOURCES") used above the slides, textbook chapter and other links at the foot of every explainer page. Paste its code into Insert > Embed > Embed code, set it to half width (6 columns) and drag the height down as far as it goes. It is self-contained, so it does not need a push to work.
