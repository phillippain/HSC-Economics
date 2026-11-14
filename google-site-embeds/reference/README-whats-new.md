# What's New box (updates by itself)

The Home page box reads `whats-new.json` from the repo root each time the page opens
(`https://phillippain.github.io/HSC-Economics/whats-new.json`). The Google Site never needs editing for it.

To add an entry: put a new line at the top of `items` in `whats-new.json`, commit and push.

    {"date": "2026-11-20", "text": "New: Topic 3 revision quiz on the Tools page."}

- Newest first. Date as YYYY-MM-DD. The box shows the five newest and takes "updated" from the first one.
- Keep each text under about 110 characters, in plain words for students.
- If the file cannot be loaded, the box shows the five entries written into `home-whats-new.html`.

`home-start-here.html` is the six-tool "Start here" column that sits beside it.
Both are drawn 420 px wide and scaled to fit, and sit side by side (six columns each) on the Home page.

Site theme: custom theme "Cobalt and Gold" (#1C3FB0, #FFD24A, #122A7A, Manrope). The earlier
"HSC Economics" theme is still in the Themes panel.
