# Chain Builder

Cause and effect chains for HSC Economics: how an event or a policy flows through the economy, one link at a time.
It is the Economics counterpart of the Legal Studies Court Process Explorer, and it feeds the **Explain** step of
the booklet's economics paragraph ("a chain of cause and effect, in precise economic terms").

- **Page:** `index.html` is one self-contained file (built, do not edit by hand).
- **Published at:** `/chain-builder/` on the GitHub Pages site.
- **Embedding:** `…/chain-builder/?embed=1`, with `theme=light|dark` and `fw=h09|y12`.
- **Links in:** `#chain=cash-rate-rise`, `#view=build|predict|compare`.

## The four views

| View | What the student does |
|---|---|
| Explore | Reads the flow chart: trigger, the channels side by side, and where they join. Selecting a box shows why that step happens. The side panel gives the dot points, how long the chain takes, where it can break (for Link & judge), the diagram to draw, the latest statistics and past questions that need the chain. |
| Build it | Builds the chain one link at a time from three options. The flow chart grows with each right answer, and the reason is shown. |
| Predict | Chooses rise or fall for every link, then checks. Eight chains can be reversed (a rate cut, an appreciation, and so on). |
| Compare | Puts any two chains side by side. |

## The one list

`data/chains.json` holds the twelve chains. Each has a `trigger`, an optional `stem` (links before the channels
split), `strands` (the channels), an optional `tail` (links after they join) and an optional `overall` line.
A link is `v` (what changes), `d` (`1` rises, `-1` falls, `0` neither) and `why`. `reverse` names the opposite
trigger, or is `null` when the chain does not simply run backwards. `codes` are 2009 syllabus dot points. `lab` names the matching diagram in the Macro Diagram Lab (`adas`, `fx`, `labour`, `lorenz`, `extern`) or `protection` for the Protection Diagram Lab.

```
python3 chain-builder/build.py           # write index.html
python3 chain-builder/build.py --check   # change nothing; fail if index.html is out of date
```

The build refuses a dot point that is not in the syllabus and a link with no reason. It pulls in, without holding
copies: past questions from the Question Finder (opened in the Extended Response Builder), statistics from the
Evidence Finder (refreshed each time the live page opens), hover definitions from the Glossary, and the syllabus
trees and 2009 to 2025 crosswalk.

The page embeds a snapshot of recent evidence, so `--check` reports it out of date after new evidence is filed.
That is harmless: the live page fetches the current evidence itself. Rebuild when a chain or the template changes.

The chains are simplified teaching models written for this tool, not taken from the booklet or the textbook.
