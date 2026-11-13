# Google Sites embeds

HTML pasted into the class Google Site (Insert > Embed > Embed code). Google Sites keeps
its own copy, so after editing a file here, open the embed on the site (pencil icon) and
paste the new code in.

- `tools.html`: the launcher on the Tools page, listing all 15 tools.
- `topic-1.html` to `topic-4.html`: the resource cards on the four topic pages, written by `build_topic_embeds.py` (Drive file IDs and tool links are listed in that script).
- `handouts/`: source for the three notes-and-activities PDFs (external stability, labour market policies, limitations of economic policies) and the teacher answers. `python3 build.py` writes the PDFs with headless Chrome; the PDFs themselves live in the Shared Drive.
- Not kept here: the All past papers page cards and the Home page quick links. Their code can be copied from each embed on the site (select the embed, pencil icon).
- All card blocks use two fixed columns so the height set in Google Sites fits every screen width.
