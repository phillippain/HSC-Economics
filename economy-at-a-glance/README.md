# Economy at a glance

Live page: **https://phillippain.github.io/HSC-Economics/economy-at-a-glance/**

Latest Australian economic indicators for HSC Economics: the economy at a glance
(AD = C + I + G + (X − M), booklet p. 67), central bank policy rates, and the economic
scorecard (pp. 68–69). ABS and RBA figures refresh automatically each day; see
[UPDATING.md](UPDATING.md) for what updates when and how to edit figures by hand.

## Embedding it

Paste this wherever your site accepts HTML (Google Sites → Embed → *Embed code*,
Canvas/Moodle/Schoology HTML editor, a WordPress Custom HTML block). The frame resizes
itself to fit the page.

```html
<iframe id="economy-at-a-glance"
  src="https://phillippain.github.io/HSC-Economics/economy-at-a-glance/?embed=1"
  title="Economy at a glance" loading="lazy"
  style="width:100%;height:4200px;border:0"></iframe>
<script>
  addEventListener("message", function (e) {
    if (e.data && e.data.type === "economy-at-a-glance:height")
      document.getElementById("economy-at-a-glance").style.height = e.data.height + "px";
  });
</script>
```

If your platform strips `<script>` tags, keep just the `<iframe>` and set the height by hand
(about 4200px for the full page, 2500px with the scorecard hidden).

### Options (add to the link after `?embed=1`, joined with `&`)

| Option | Effect |
|---|---|
| `embed=1` | Tighter top and bottom spacing for use inside another page |
| `theme=light` or `theme=dark` | Force a colour scheme (default follows the viewer's device) |
| `hide=scorecard` | Hide the scorecard tables; combine with commas, e.g. `hide=scorecard,rates,header` |

Example — just the four AD panels, always light:
`…/economy-at-a-glance/?embed=1&theme=light&hide=scorecard,rates`

## Files

- `index.html` — the page (reads `data/*.json`; d3 is bundled as `d3.min.js`, so no CDN needed)
- `data/` — the figures
- `scripts/update_rba.py` — the daily updater, run by `.github/workflows/update-economy-data.yml`
