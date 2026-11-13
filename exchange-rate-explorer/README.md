# Exchange Rate Explorer

One shock, four exchange rate systems. Students hit the Australian dollar with a shock (commodity prices, a global downturn, interest rate gaps, imports, speculation, foreign investment, inflation) and see what happens under a **floating rate, a managed float, a flexible peg and a fixed rate**. Every shock is applied to all four systems at once.

- **Experiment:** one system in detail: the demand and supply diagram, the rate over time, reserves, what the central bank does and what it means for the economy. "Predict before you see the result" is on by default.
- **Compare the four:** the same shocks side by side, with a table of the rate, reserves and central bank action.
- **The four systems:** who sets the rate, advantages, disadvantages, examples.
- **Australia and the HSC:** Australia's exchange rate history and the past HSC questions tagged 2C.4 and 2C.5.

## The model (illustrative, not real data)

Straight-line demand and supply; A$1 = US 70 cents and US$60 billion of reserves at the start. Managed float: the central bank closes half the gap to the market rate each period. Flexible peg: defended every period, reset to the market rate when it is 6 cents or more away or reserves fall below US$20 billion. Fixed: defended until reserves run out, then it collapses (a currency crisis). The constants are at the top of the script in `template.html`; shock sizes are in `data/systems.json`.

## Files

`data/systems.json` (systems, shocks, timeline), `template.html`, `build.py` (also writes `review.html`, a printable sheet of all the written content), `index.html` (built).

```
python3 exchange-rate-explorer/build.py
python3 exchange-rate-explorer/build.py --check
```

Rebuild after the Question Finder changes. Fixed, flexible and managed rates are 2009 syllabus content (2C.4, HSC to 2027); the 2025 syllabus covers the float and Reserve Bank intervention.
