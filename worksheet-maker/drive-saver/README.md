# Worksheet saver (Google Apps Script)

The Worksheet Maker and the Lesson Register are web pages on GitHub Pages, so they can't write to Google Drive
themselves. The **Worksheet saver** is a small Google Apps Script web app that runs in the teacher's own school
Google account and does it for them:

- **save**: the worksheet's student copy, answer copy and editable file go into a **Worksheets** folder in the
  topic's resources (it makes the folder the first time);
- **list**: the worksheets in those folders, for the Lesson Register;
- **ping**: checks the key and that each folder can be reached.

`Code.gs` is the whole script. Where each course's worksheets go is the `PLACES` list near the top (Drive folder IDs
of the topic resource folders on `HSC_Economics_SSCBWB` and of `2027 Syllabus / 0N … / New resources (2027)` on
`Prelim_Eco_SSCBWB`). The key line holds a placeholder: the Worksheet Maker writes the teacher's own key into the
copy it gives them, so the real key is never in this repository.

## Set it up (about 10 minutes, once)

1. In the Worksheet Maker, go to **Layout and print › Save to Google Drive** and press **Copy the saver script**.
2. Open [script.google.com](https://script.google.com/home/projects/create), signed in with the school account
   that can open both shared drives. A new project opens: name it **Worksheet saver**.
3. In **Code.gs**, select everything, paste the script over it, and press **Save**.
4. Press **Deploy › New deployment**, click the cog beside “Select type” and choose **Web app**:
   - **Execute as:** Me
   - **Who has access:** Anyone. The key in the script keeps it private. If the account offers only
     “Anyone within NSW Department of Education”, choose that: it then works only in a browser signed in to the
     school Google account.
   Press **Deploy**, then **Authorize access**, choose the school account and allow it to see and manage Drive files.
5. Copy the **Web app URL** (it ends in `/exec`), paste it into the Worksheet Maker's dialog and press
   **Check and save**. The dialog lists the ten folders; any it can't reach are marked.

**Another computer, or the Lesson Register on another device:** in the dialog press **Copy a connection code** and
paste it into the Worksheet Maker there (*Set up on another computer already?*) or into the Lesson Register's
*Worksheets from the Worksheet Maker* box. The code holds the key, so send it only to yourself.

## Updating the script

When `Code.gs` changes in this repository, copy it again from the dialog (it keeps the same key), paste it over
Code.gs, then **Deploy › Manage deployments › Edit (the pencil) › Version: New version › Deploy**. Editing the
existing deployment keeps the same web app address, so nothing else needs changing.

## How the pages talk to it

- **Web app open to Anyone:** `fetch()` POSTs JSON as plain text (no preflight). Apps Script answers with a redirect
  to `script.googleusercontent.com`, which allows any origin to read the JSON.
- **Web app limited to school accounts:** that `fetch()` is refused, so the page posts a hidden form (field `p`)
  into a hidden frame. `doPost` then returns a small page that sends the answer by `postMessage` to each enclosing
  window, addressed to the origins in `ORIGINS` (`https://phillippain.github.io`). The page accepts it only with the
  nonce it sent and only from inside its own frame.
- Requests carry the key; a wrong or missing key gets `bad-key`. File names lose `\ / : * ? " < > |`. A name already
  used in the folder gets ` (2)`, ` (3)` and so on: nothing is ever replaced, so links in lesson records stay right.
- The student copy is opened to the domain (`DOMAIN_WITH_LINK`, Viewer); if the shared drive doesn't allow that, the
  save still works and says so. The answer copy and editable file are left restricted.
- A note of each saved worksheet (title, dot points, answer copy) is kept in the script's properties for `list`.

## Tested

Against a stand-in for the Apps Script services that runs this `Code.gs` in Node (key checks, ping, saving to the HSC
and Year 11 folders, second saves, a folder the account can't reach, sharing refused, listing, the hidden-frame page
and its escaping), and end to end from the Worksheet Maker and the Lesson Register in headless Chrome through a
stand-in for Google's web app hosting (both routes). Not yet run in Google itself.
