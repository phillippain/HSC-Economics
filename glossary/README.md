# Economics Glossary

A web version of the topic glossaries in the Year 12 Economics Booklet 2027 (pages 21 to 37), with later additions: look up, flashcards,
a quiz and a printable term list, in the same look as the Evidence Finder and the Extended Response Builder.

- **Page:** `index.html` is one self-contained file (built, do not edit by hand).
- **Published at:** `/glossary/` on the GitHub Pages site, which deploys the whole repo on every push to `main`.
- **Embedding:** `…/glossary/?embed=1`, with `theme=light|dark`.

## The one list

`data/glossary.json` holds every term: `id`, `term`, `topics` (`T1` to `T4`) and `def`. To add, fix or reword
a term, edit it there, then run:

```
python3 glossary/build.py           # write index.html
python3 glossary/build.py --check   # change nothing; fail if index.html is out of date
```

The build refuses an entry with no definition, a duplicate `id`, or a topic that is not `T1` to `T4`.

The booklet lists nine terms under more than one topic (for example *Cash rate* in Topics 1 and 4). Each is
held once and tagged with every topic it appears in; where the booklet's wording differed slightly between
topics, the fuller wording is kept. That is why 228 booklet rows became 219 terms, before the additions.

## Changes from the booklet

`suggested-additions.md` records where the site differs from the printed booklet: the 45 terms added and the
8 entries revised on 13 November 2026. Those entries carry `"added"` or `"revised"` in `glossary.json`.
`data/suggested.json` is the place for future draft terms; nothing in it is shown on the site.

## Links

- In: `glossary/#term=cash-rate`, `#t=T3`, `#q=tariff`, `#view=cards`, `#view=quiz`, `#view=list`.
- Out: every term links to a search for it in the Evidence Finder.

Flashcard progress is kept in the browser (`localStorage`, key `econ-gloss-known`).
