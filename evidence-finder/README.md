# HSC Economics Evidence Finder

News stories, statistics and documents for HSC and Year 11 Economics, filed against the syllabus dot points they answer.

Live page: **https://phillippain.github.io/HSC-Economics/evidence-finder/**

Open `index.html` to use it locally. It is one self-contained file (fonts, data and code are inside), so it works offline and on restricted school networks. The PDFs it links to sit in `files/`.

## What it does

- **Three syllabus views.** HSC on the 2009 syllabus (current Year 12 to the HSC in 2027), HSC on the 2025 syllabus (from the 2028 HSC), and Year 11 on the 2025 syllabus (from 2027). Evidence tagged in one syllabus still appears in the others through a section crosswalk.
- **Coverage map.** One square per dot point. Dark means more evidence, hatched means supporting only, dashed means nothing yet. Click a square to jump to that dot point.
- **Four ways in.** Syllabus, issues and indicators, policy levers, and a statistics bank that lists every figure with its date and source. Plus search, and filters for type, diagram and source.
- **Lists to print.** Tick items for an evidence sheet (one entry per item) or an evidence map (sorted by dot point).
- **Shareable links.** The address bar always matches the view, for example `#fw=y12&sel=section:Y2c`.

## Embedding

Same pattern as `economy-at-a-glance`. Paste where your site accepts HTML:

```html
<iframe src="https://phillippain.github.io/HSC-Economics/evidence-finder/?embed=1"
  title="Economics Evidence Finder" loading="lazy" style="width:100%;height:1400px;border:0"></iframe>
```

Options after `?embed=1`, joined with `&`: `theme=light` or `theme=dark`, and `fw=h09`, `fw=y12` or `fw=y11` to open on a syllabus.

## Files

```
index.html                 the site (built, do not edit by hand)
data/evidence.json         one record per item: the only file edited when filing new evidence
data/syllabus.json         the three syllabus trees, vocabularies and the 2009 to 2025 crosswalk (built)
data/syl2025.json          2025 dot points parsed from the NESA PDF
data/qf_taxonomy.json      2009 dot points, shared with the Question Finder so codes match
files/YYYY-MM/             the PDFs the cards link to
build/build_site.py        checks every tag, then writes index.html
build/ingest.py            Drive inbox -> files/: status, file, archive, rebuild, commit
data/ingest-log.jsonl      what was filed from the inbox, and where the original went
build/make_syllabus.py     rebuilds data/syllabus.json (vocabularies and crosswalk live here)
build/template.html        the page
build/parse_sources.py     pulls source links out of a handout or digest PDF
build/parse_syl2025.py     rebuilds data/syl2025.json from the NESA syllabus PDF text
```

## Adding evidence: drop it in the inbox

New material goes into **`HSC_Economics_SSCBWB / Evidence Finder / inbox`** on the shared drive, from any device: drag in a PDF from a browser, email or phone. A link can be dropped too, as a text file or note with the web address in it. Nothing else is needed from whoever drops it.

Filing is then one Claude session with the **add-economics-evidence** skill ("file what's in the Economics inbox"). Claude reads what is waiting, writes the record and its syllabus tags, rebuilds the page and commits. `build/ingest.py` is what it drives, and it works by hand as well:

```sh
python3 build/ingest.py status                                   # what is waiting
python3 build/ingest.py file "RBA SMP Nov.pdf" 2026-11-10-rba-smp-november --label "RBA report"
python3 build/ingest.py archive "link.txt"                       # clear a link, note or duplicate
python3 build/ingest.py refresh --commit "Evidence Finder: file inbox (3 new)"
```

`file` copies the document to `files/YYYY-MM/<id>.pdf` in the repo, which is the copy the site links to, and moves the original to `Evidence Finder / filed / YYYY-MM /` on the drive, so an empty inbox means everything has been dealt with. Nothing is deleted. `data/ingest-log.jsonl` records each move. Then push (GitHub Desktop, Push origin).

Unlike the Legal Studies finder there is no Apps Script and no Drive id map, because the cards link to the copy in the repo and not to Drive.

## Rebuilding

Python 3 only, no packages:

```sh
python3 build/make_syllabus.py   # only if vocabularies or the crosswalk changed
python3 build/build_site.py      # checks the data and rewrites index.html
```

`build_site.py` stops with a list of problems if any record uses an unknown dot point, issue, lever or diagram, or points to a file that is missing. See [ADDING.md](ADDING.md) for how to file an item.

Pushing to `main` publishes it through the repository's Pages workflow.

## Notes on the syllabus data

- 2009 HSC: 106 dot points across four topics, plus the "students learn to" skills statements, which are filed but not counted in the coverage totals.
- 2025: 142 Year 12 dot points and 134 Year 11 dot points. Formulas in the NESA PDF extract as fragments, so ten formula dot points were restated in plain text in `build/parse_syl2025.py`. Check them against curriculum.nsw.edu.au if wording matters.
- The crosswalk is section to section, not dot point to dot point. It is a judgement about which sections cover the same ground, and it can be changed in `build/make_syllabus.py`.
- Syllabus content is © NSW Education Standards Authority / Board of Studies NSW and used here for non-commercial educational purposes.
