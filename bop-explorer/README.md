# Balance of Payments Explorer

- **Sort and build:** 24 transactions to place in the right account as a credit or debit. Each one is added to a running balance of payments; with all 24 in, the current account (−5) and the capital and financial account (+5) sum to zero. The build checks that the set balances.
- **Shock and trace:** eight changes (terms of trade, global downturn, depreciation, interest rates, domestic boom, mining investment boom, national saving, world interest rates), each shown "at first" and "later", with the reason each account moves.
- **Australia's record:** real data, years to June 1984 to 2026: trade balance, net income and current account balance as a per cent of GDP.
- **How it fits together:** the structure, three rules, and past HSC questions tagged 2B.

## Data

`data/bop.json`: `tx` (transactions), `shocks`, `base`, `history`. The transactions and shock sizes are a teaching model. The history is from the **RBA Statistical Table I1** (ABS data; published 3 September 2026, retrieved 13 November 2026): each financial year is the average of its four quarterly ratios, and net income is the current account balance minus the trade balance. To update it, add a row `[year ending June, trade balance % GDP, current account % GDP]` and change `source`.

```
python3 bop-explorer/build.py           # also writes review.html
python3 bop-explorer/build.py --check
```

Rebuild after the Question Finder changes.
