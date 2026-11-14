# Reference notes, What's New and "Updated" stamps (14 November 2026)

## Reference notes on eight sub-topic pages
Each page has two parts, side by side on a computer and stacked on a phone:

- **Text** (`ref-<page>-text.html`): pasted into a normal Google Sites text box, so it reflows on phones.
- **Key data** (`ref-<page>-charts.html`): stat tiles, charts and tables as one embed (Insert > Embed > Embed code).
  It is drawn 400 px wide and scaled to fit, so it keeps its shape at every width.

| File prefix | Site page |
|---|---|
| `ref-technology` | Topic 1 > Technology, Transport & Communication |
| `ref-division-of-labour` | Topic 1 > International division of labour |
| `ref-international-organisations` | Topic 1 > Role of international organisations |
| `ref-local-content` | Topic 1 > Protection > Methods > Local Content Rules |
| `ref-trade-financial-flows` | Topic 2 > VCD of Australia's trade & financial flows |
| `ref-protection-policy` | Topic 2 > Free trade & protection |
| `ref-free-trade-agreements` | Topic 2 > Free Trade Agreements |
| `ref-environment-context` | Topic 4 > National & global context for environmental management |

To update: edit `content_ref.py` (text and figures) and `STAMP` in `build_reference.py`, run
`python3 build_reference.py`, then replace the text box contents and the embed code on the page.
Google Sites keeps an embed's height in proportion to its width, so after changing the amount of
content, drag the embed's bottom handle until nothing is cut off.

Figures to re-check when updating: the passenger car tariff steps (1987 to 2010) and the internet
use series before 2025 were written from general knowledge, not from a page fetched in the session.
Source links point to each organisation's home page, not to a specific report page.

## What's New box on the Home page
`home-whats-new.html`. Edit the dated lines and the date in the heading, then paste over the embed code.

## "Updated" stamps on the card pages
Tools, Topic 1 to 4 and All past papers show "Updated 14 November 2026" at the top right. It is this
at the end of each embed, plus two CSS rules before `</style>`:

    .u{position:absolute;top:3px;right:6px;font-size:11px;font-weight:700;color:#5a6580;letter-spacing:0;text-transform:none}h2:first-child{padding-right:175px}
    <div class="u">Updated 14 November 2026</div>
