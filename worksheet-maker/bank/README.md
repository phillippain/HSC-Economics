# The Worksheet Maker's question bank

Plain-text files, one question after another. Edit them in any text editor, then run
`python3 worksheet-maker/build.py`. The build stops and names the file and line if anything is wrong.

Every question starts with a heading line, `=== <type> <id>`, followed by details, then the body.
Files named `y11-*.txt` hold the Year 11 (2025 syllabus) questions; the rest are HSC.
The id must be unique (letters, numbers, dots and hyphens). Lines starting with `#` are comments.

## Details (all types)

| Line | Meaning |
|---|---|
| `c: 2C.2 2C.3` | Dot points (required): 2009 syllabus HSC dot points, matched to 2025 Year 12 sections through the crosswalk; or 2025 Year 11 dot points such as `P2e.3` (the `y11-*.txt` files) |
| `m: 4` | Marks (each type has a sensible default) |
| `lv: 2` | Level: 1 foundation, 2 HSC standard, 3 extension (Band 6) |
| `k: explain diagram` | Skills, using the Question Finder's names: calc, diagram, graph, table, extract, case, define, explain, analyse, evaluate, discuss, compare, outline, stimulus, recall |
| `ss: S2.6` | Syllabus "students learn to" skills |
| `like: II2019Q24(a)` | Question Finder ids this question is modelled on (used by **Look-alike**) |
| `checked: yes` | The teacher has checked this question (removes "not yet reviewed") |

A file whose first line is `# reviewed` has been checked as a whole.

Most reviewing happens on the **Question review** page (staff Tools site), which saves the teacher's decisions to
`reviews.json` in this folder: `ok` approved, `fix` needs a fix (with a `note`), `out` removed. Each decision
holds the question's fingerprint `h`, so editing a question sends it back for review. To fix a flagged question,
edit it here from the note and rebuild; to drop a removed one for good, delete it here and its entry in
`reviews.json`.

## The body, by type

**Multiple choice** (`mc`)
```
Q: the stem
A: option   B: option   C: option   D: option     (one per line)
ANS: B
WHY: why B is right
```

**Short answer** (`sa`): one question, or several parts sharing a lead-in and table.
```
LEAD: optional sentence introducing the data
TABLE: optional caption
| heading | heading |
| cell | cell |
Q: the question                    or   PART (a) 2: the question
PTS:                                    PTS:
- a marking point (1)                   - ...
ANS: optional model answer              ANS: ...
```

**Extended response** (`er`): `Q:`, then `PTS:` (what a Band 6 response includes) and `PLAN:` (paragraph ideas).
A `LEAD:` and `TABLE:` make it a Section III-style question.

**Draw a diagram** (`draw`) and **label a diagram** (`label`)
```
DIA: adas AD left          (the diagram codes are listed at the top of build/diagrams.py)
Q: the event and the instruction
ANS: what the answer diagram shows and why
```
Add `given` to the code (`fx D right given`) to print the starting diagram instead of blank axes.

**Read a diagram** (`read`): `DIA: fig1` (numbered figures fig1, fig2, fig3, fig6, fig7, fig8), `LEAD:`, then `PART`s.

**Sort and classify** (`sort`)
```
Q: the instruction
CATS: Heading 1 | Heading 2 | Heading 3
- an item => Heading 1
```

**Compare** (`compare`)
```
Q: the instruction
COLS: Thing 1 | Thing 2
- Row heading => answer for thing 1 | answer for thing 2
```
Start a cell with `!` to print it on the student copy as a hint.

**Spot the error** (`error`)
```
Q: This paragraph answers: "..."
TEXT: a paragraph in which each mistake is written [[the mistaken words => the correct words]]
```

**True or false statements** (`tf`): not a question on its own; the page draws 6 to 10 statements for the
chosen dot points.
```
- T: a true statement => optional reason
- F: a false statement => the corrected statement
```

**Cause and effect chain** (`chain`)
```
TITLE: short title
TRIGGER: the event
- the variable that changes => up | why it rises
- the next variable => down | why it falls
```

## House rules

Australian spelling; NESA key verbs with marks to suit; **AS** for the aggregate supply curve (SRAS only when
LRAS is on the diagram); no "quota rent" (the importers keep the extra revenue from the higher price); developing
and emerging economies always treated separately; real statistics only with their source and date.
