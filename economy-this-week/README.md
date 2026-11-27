# The Economy This Week: archive page

`index.html` is the student page for the weekly 4-page news summary. It is embedded on the Google Site
(News & reading > The Economy This Week) by an iframe loader, so a push updates the Site with no edit in Sites.

- **This week:** the newest edition (cover, summary, big exam idea, stories with page numbers).
- **All editions:** a card for every edition, newest first.
- **Story index:** every story, searchable by headline, lead, key terms and the 'Try this' question.
- **Topic 1 to 4 filter** works on all three views. **Read here** opens a page-by-page reader (page images in
  `pages/`); **Open in Drive** opens the student copy on the shared drive (school accounts only);
  **PDF** downloads the copy in `editions/`.
- Deep links: `#tab=all`, `#tab=index&topic=2&q=tariff`, `#e=2026-11-27&p=2` (edition and page).

## Adding an edition (the Friday run does this)
```
cd HSC-Economics/economy-this-week
python3 build.py --import "<the Friday output folder>"
```
This copies the new PDF into `editions/` (the plain file name, or the newest `_auto` variant if there is no plain one),
copies it to `HSC_Economics_SSCBWB/The Economy This Week/` on the shared drive, reads its Drive ID into `drive.json`,
renders the page images, and rebuilds `editions.json` and `index.html`. Then commit, add a line to `whats-new.json`,
and push. Run it again a minute later if the Drive ID was not ready (the build prints `drive NO`).

Corrections the parser cannot work out (for example the older October layout) go in `overrides.json`.
`python3 build.py --check` fails if an edition has no stories or no Drive ID.

Needs python3 and poppler (`pdftotext`, `pdftoppm`) only. Google Analytics tag G-11YGV11ZES is in `template.html`.

## On the Google Site
Page: News & reading > The Economy This Week (header "Title only"). One full-width embed (Insert > Embed > Embed code) holding only:
```
<style>html,body{margin:0;height:100%;overflow:hidden}iframe{border:0;width:100%;height:100%;display:block}</style><iframe src="https://phillippain.github.io/HSC-Economics/economy-this-week/" title="The Economy This Week"></iframe>
```
Drag the embed's bottom handle so it is about 1.2 times as tall as it is wide; the page scrolls inside the frame.
Shared-drive folder: `HSC_Economics_SSCBWB/The Economy This Week` (Drive folder ID `19NQB-HZz0OXAveivlRed-qj4rnGLBCwF`).
Share it once with the NSW Department of Education domain as Viewer so students can open the Drive copies.
