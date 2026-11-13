# Policy Simulator

"You be the Reserve Bank Board and the Treasurer." The student reads the briefing decision-makers had in a real
episode, diagnoses the problem, sets the cash rate and the budget, then compares with what the RBA and the
government did and what happened next. It is the Economics counterpart of the Legal Studies Sentencing Simulator.

- **Page:** `index.html` is one self-contained file (built, do not edit by hand).
- **Published at:** `/policy-simulator/` on the GitHub Pages site.
- **Embedding:** `…/policy-simulator/?embed=1`, with `theme=light|dark`.
- **Links in:** `#ep=gfc|covid|tightening|now`, `#view=guide`.

## The four episodes

| Episode | Decision date | What the student decides |
|---|---|---|
| The Global Financial Crisis | 7 October 2008 | Cash rate from 7.00%; the first stimulus package |
| The COVID-19 pandemic | 19 March 2020 | Cash rate from 0.50% and unconventional measures; the fiscal response |
| The 2022–23 inflation surge | 3 May 2022 | Cash rate from 0.10%; what to do with a revenue windfall |
| The 2026 inflation episode | 3 November 2026 | Cash rate from 4.60% with inflation high and unemployment rising. Marked "still unfolding" |

## The steps

1. **Read the briefing:** the situation and six indicators as known on the day.
2. **Diagnose:** the biggest threat, where the problem comes from, the stance policy should take.
3. **Decide:** a cash rate option and a budget option, plus an optional one-sentence reason.
4. **Compare:** the diagnosis with explanations; the student's choices beside the actual ones, with a note on whether theirs was tighter or more expansionary; the reasoning; a chart of the cash rate through the episode; what happened next; what worked and the limits (evidence for "assess" and "evaluate" questions); links to the Chain Builder, Macro Diagram Lab and Extended Response Builder; sources.

There is no score for the decisions, only for the diagnosis: real decisions are contested (the Board split 6 to 3 in November 2026).

## The one list

`data/episodes.json` holds everything. For each episode: `situation`, `indicators` (label, value, note, flag
`high|low|ok|warn`), `diag` (answers and explanations), `monetary` and `fiscal` (`options` ordered from most
expansionary to tightest, `actual` index, `did`, `why`), `path` (cash rate steps for the chart), `next`
(outcomes), `judge` (`worked`, `limits`), `chain`, `lab`, `sources`, and `live: true` for an episode still unfolding.

```
python3 policy-simulator/build.py           # write index.html
python3 policy-simulator/build.py --check   # change nothing; fail if index.html is out of date
```

## Keeping the 2026 episode current

When the outcome is known, edit the `now` episode: update `next`, `judge` and `path`, and remove `"live": true`.
A newer decision can be added as a fifth episode by copying an entry and giving it a new `id`.

## Where the figures come from

Cash rate changes are from the RBA's cash rate table. Other figures are from the RBA explainers and Statements
on Monetary Policy, Treasury final budget outcomes and, for 2026, the class Evidence Finder; each episode lists
its sources on the page. `FIGURES-TO-CHECK.md` lists every figure with how it was verified.
