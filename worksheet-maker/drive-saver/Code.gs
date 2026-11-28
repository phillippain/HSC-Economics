/**
 * Worksheet saver for the HSC Economics Worksheet Maker and the Lesson Register.
 *
 * It runs in your own school Google account and does three things when the Worksheet Maker asks:
 *   ping  check the key and that it can reach each Worksheets folder's parent folder
 *   save  save a worksheet's student copy, answer copy and editable file into the topic's Worksheets folder
 *   list  list the worksheets saved there, for the Lesson Register
 *
 * Set up once (the Worksheet Maker's "Set up Google Drive…" dialog walks you through it):
 *   1. New project at script.google.com, paste this whole file over Code.gs, Save.
 *   2. Deploy > New deployment > Web app. Execute as: Me. Who has access: Anyone
 *      (or "Anyone within NSW Department of Education" if that is all your account offers).
 *   3. Copy the Web app URL into the Worksheet Maker.
 *
 * The key below is private: only someone with it can save into or list your folders.
 * The Worksheet Maker fills it in when you copy this script; do not post this file anywhere with the key in it.
 */
const KEY = '__WORKSHEET_SAVER_KEY__';
const VERSION = 1;

// Pages allowed to receive answers through the hidden-frame route (used when the web app is limited to school accounts).
const ORIGINS = ['https://phillippain.github.io'];

// The folder made inside each place below.
const FOLDER = 'Worksheets';

// Where each course's worksheets go. `student` is the folder that gets a Worksheets folder for the student copies.
// `teacher` is where the answer copy and the editable file go: a folder ID, [parent folder ID, subfolder name]
// (made if missing; a Worksheets folder is made inside it), or null for the same Worksheets folder as the student copy.
// `answers` is added to the answer copy's file name. `share` opens the student copy to NSW DoE accounts (Viewer).
const ZZ_TEACHER_ONLY = '1J2lsRmzcACD1QnYezK1jbPt-1W52FzZM'; // HSC_Economics_SSCBWB / zzTeacher Only
const PLACES = [
  // HSC Economics, shared drive HSC_Economics_SSCBWB
  { id: 'hsc-t1', course: 'hsc', topic: 1, label: 'Topic 1 The Global Economy',
    student: '1cRSC7E6gJUIp05DVymWZZWgCA5zg5pH6', // Topic 1 - Global Economy
    teacher: [ZZ_TEACHER_ONLY, 'Topic 1'], answers: ' (answers)', share: true },
  { id: 'hsc-t2', course: 'hsc', topic: 2, label: "Topic 2 Australia's Place in the Global Economy",
    student: '1kw4diqkeTnCXhRnulOHUTD7RcMC4QH5B', // Topic 2 - Australia's Place in the Global Economy (resources)
    teacher: [ZZ_TEACHER_ONLY, 'Topic 2'], answers: ' (answers)', share: true },
  { id: 'hsc-t3', course: 'hsc', topic: 3, label: 'Topic 3 Economic Issues',
    student: '1aoWK4cP2GGKb2WPLhI1T8eEunMlaao-h', // Topic 3 - Economic Issues (resources)
    teacher: '14JZV-AzOiU5IwJNzqysMF8wJaCHQTwd9', // zzTeacher Only / Topic 3
    answers: ' (answers)', share: true },
  { id: 'hsc-t4', course: 'hsc', topic: 4, label: 'Topic 4 Economic Policies and Management',
    student: '1xRvLXinF09t3Pn88OZpzq_HleuGQRphz', // Topic 4 - Economic Policies & Management
    teacher: '1gaz_XPCiw_FNt77pwKKfCY6XXaGj96Yz', // zzTeacher Only / Topic 4
    answers: ' (answers)', share: true },
  // Year 11 Economics, shared drive Prelim_Eco_SSCBWB: 2027 Syllabus / 0N … / New resources (2027).
  // Teacher copies sit beside the student copies there, as the drive's other new resources do.
  { id: 'y11-p1', course: 'y11', area: 'P1', label: '01 Introduction to Economics',
    student: '19_l9MSfK39lld_S9Zk-2UwsDMTdHqF88', teacher: null, answers: ' – Teacher', share: true },
  { id: 'y11-p2', course: 'y11', area: 'P2', label: '02 Markets',
    student: '1BS8GT51X7cltWVDvFH5Lmxad-wCxhxPQ', teacher: null, answers: ' – Teacher', share: true },
  { id: 'y11-p3', course: 'y11', area: 'P3', label: '03 Household and Business Sector',
    student: '1M1KDWcLzVH8BTXOxsTsdd1yYEsCOkGy7', teacher: null, answers: ' – Teacher', share: true },
  { id: 'y11-p4', course: 'y11', area: 'P4', label: '04 Financial Sector',
    student: '1FyG3EtWMBqo9eRCfNDbAG_nAXiX0OnLW', teacher: null, answers: ' – Teacher', share: true },
  { id: 'y11-p5', course: 'y11', area: 'P5', label: '05 Government Sector',
    student: '1xrqLelnx-1IL-0I_Apo0-hHPcPvhtcbd', teacher: null, answers: ' – Teacher', share: true },
  { id: 'y11-p6', course: 'y11', area: 'P6', label: '06 International Sector',
    student: '1zseb6pk6w8fTDpj6_SbtvrEQ3YpN1GxJ', teacher: null, answers: ' – Teacher', share: true }
];

const MAX_BYTES = 25 * 1024 * 1024;
const COURSE_NAMES = { hsc: 'HSC Economics', y11: 'Year 11 Economics' };

/* ------------------------------------------------------------------ web app entry points */

function doGet() {
  let who = '';
  try { who = Session.getEffectiveUser().getEmail(); } catch (e) { }
  return HtmlService.createHtmlOutput(
    '<div style="font:16px/1.5 system-ui,sans-serif;max-width:560px;margin:40px auto;padding:0 16px">' +
    '<h1 style="font-size:20px">Worksheet saver</h1><p>The saver is running' + (who ? ' as ' + esc_(who) : '') + '.</p>' +
    '<p>Go back to the Worksheet Maker or the Lesson Register and try again.</p></div>').setTitle('Worksheet saver');
}

function doPost(e) {
  // Two ways in: fetch() sends the request as the body (web app open to Anyone), and the hidden-frame route
  // sends it as the form field "p" and gets the answer back by postMessage (web app limited to school accounts).
  const framed = !!(e && e.parameter && e.parameter.p);
  let req = {}, res;
  try {
    req = JSON.parse(framed ? e.parameter.p : (e && e.postData && e.postData.contents) || '{}') || {};
    res = handle_(req);
  } catch (err) {
    res = { ok: false, error: 'failed', message: msg_(err) };
  }
  if (framed) return frame_(res, req);
  return ContentService.createTextOutput(JSON.stringify(res)).setMimeType(ContentService.MimeType.JSON);
}

function handle_(req) {
  if (!KEY || KEY.indexOf('__') === 0 || KEY.length < 20) return { ok: false, error: 'no-key' };
  if (!same_(String(req.key || ''), KEY)) return { ok: false, error: 'bad-key' };
  if (req.action === 'ping') return ping_();
  if (req.action === 'save') return save_(req);
  if (req.action === 'list') return list_(req);
  return { ok: false, error: 'bad-action' };
}

/* ------------------------------------------------------------------ actions */

function ping_() {
  let who = '';
  try { who = Session.getEffectiveUser().getEmail(); } catch (e) { }
  const places = PLACES.map(p => {
    const out = { id: p.id, course: p.course, topic: p.topic || null, area: p.area || null, label: p.label };
    try {
      const f = DriveApp.getFolderById(p.student);
      out.folder = { name: f.getName(), url: f.getUrl() };
      out.teacher = p.teacher ? (Array.isArray(p.teacher) ? DriveApp.getFolderById(p.teacher[0]).getName() + ' › ' + p.teacher[1] : DriveApp.getFolderById(p.teacher).getName()) : null;
    } catch (err) {
      out.error = msg_(err);
    }
    return out;
  });
  return { ok: true, version: VERSION, user: who, folder: FOLDER, places: places };
}

function save_(req) {
  const place = placeOf_(req.place);
  if (!place) return { ok: false, error: 'bad-place' };
  const name = clean_(req.name);
  if (!name) return { ok: false, error: 'bad-name' };
  const student = bytes_(req.student), answers = bytes_(req.answers);
  if (!student) return { ok: false, error: 'no-file' };
  if (student.length + (answers ? answers.length : 0) > MAX_BYTES) return { ok: false, error: 'too-big' };
  const meta = req.meta || {};

  const lock = LockService.getScriptLock();
  lock.waitLock(30000); // two saves at once must not pick the same file name
  try {
    const sFolder = child_(DriveApp.getFolderById(place.student), FOLDER);
    const tFolder = place.teacher ? child_(teacherParent_(place), FOLDER) : sFolder;
    const base = freeName_(name, [[sFolder, '.pdf'], [tFolder, place.answers + '.pdf'], [tFolder, '.worksheet.json']]);
    const out = { ok: true, name: base, place: place.id, label: place.label, folder: info_(sFolder), teacherFolder: info_(tFolder) };

    const sf = sFolder.createFile(Utilities.newBlob(student, 'application/pdf', base + '.pdf'));
    sf.setDescription(desc_(meta, 'Student copy'));
    out.student = info_(sf);
    if (answers) {
      const af = tFolder.createFile(Utilities.newBlob(answers, 'application/pdf', base + place.answers + '.pdf'));
      af.setDescription(desc_(meta, 'Answer copy (teachers only)'));
      out.answers = info_(af);
    }
    if (req.sheet && typeof req.sheet === 'object') {
      const jf = tFolder.createFile(Utilities.newBlob(JSON.stringify(req.sheet), 'application/json', base + '.worksheet.json'));
      jf.setDescription('Open this in the Worksheet Maker (My worksheets > Open a file) to change the worksheet.');
      out.sheet = info_(jf);
    }
    if (place.share) {
      try { sf.setSharing(DriveApp.Access.DOMAIN_WITH_LINK, DriveApp.Permission.VIEW); out.shared = true; }
      catch (err) { out.shared = false; out.warning = 'The student copy is saved but could not be opened to NSW DoE accounts: ' + msg_(err); }
    }
    remember_(sf.getId(), {
      a: out.answers ? out.answers.id : '', j: out.sheet ? out.sheet.id : '',
      t: String(meta.title || base).slice(0, 160), c: String(meta.course || place.course).slice(0, 8),
      k: (Array.isArray(meta.codes) ? meta.codes : []).slice(0, 30).map(String), n: +meta.count || 0, m: +meta.marks || 0,
      at: new Date().toISOString()
    });
    return out;
  } finally {
    lock.releaseLock();
  }
}

function list_(req) {
  const want = Array.isArray(req.places) && req.places.length ? PLACES.filter(p => req.places.indexOf(p.id) >= 0) : PLACES;
  const props = PropertiesService.getScriptProperties().getProperties();
  const hide = {};
  Object.keys(props).forEach(k => {
    if (k.indexOf('w:') !== 0) return;
    try { const v = JSON.parse(props[k]); if (v.a) hide[v.a] = 1; if (v.j) hide[v.j] = 1; } catch (e) { }
  });
  const items = [], problems = [];
  want.forEach(p => {
    let folder = null;
    try { folder = find_(DriveApp.getFolderById(p.student), FOLDER); }
    catch (err) { problems.push({ place: p.id, label: p.label, error: msg_(err) }); return; }
    if (!folder) return; // nothing saved there yet
    const files = folder.getFiles();
    while (files.hasNext()) {
      const f = files.next();
      if (f.isTrashed() || f.getMimeType() !== 'application/pdf' || hide[f.getId()]) continue;
      const nm = f.getName().replace(/\.pdf$/i, '');
      if (p.answers && nm.slice(-p.answers.length) === p.answers) continue; // a teacher copy put there by hand
      let v = null;
      try { v = props['w:' + f.getId()] ? JSON.parse(props['w:' + f.getId()]) : null; } catch (e) { }
      items.push({
        id: f.getId(), url: f.getUrl(), name: nm, title: (v && v.t) || nm, place: p.id, label: p.label, course: p.course,
        topic: p.topic || null, area: p.area || null, at: (v && v.at) || f.getDateCreated().toISOString(),
        answers: v && v.a ? 'https://drive.google.com/file/d/' + v.a + '/view' : null,
        codes: (v && v.k) || [], count: (v && v.n) || null, marks: (v && v.m) || null, maker: !!v
      });
    }
  });
  items.sort((a, b) => (a.at < b.at ? 1 : a.at > b.at ? -1 : 0));
  return { ok: true, items: items.slice(0, 600), problems: problems };
}

/* ------------------------------------------------------------------ helpers */

function placeOf_(id) { for (let i = 0; i < PLACES.length; i++) if (PLACES[i].id === id) return PLACES[i]; return null; }

function teacherParent_(place) {
  if (Array.isArray(place.teacher)) return child_(DriveApp.getFolderById(place.teacher[0]), place.teacher[1]);
  return DriveApp.getFolderById(place.teacher);
}

function find_(parent, name) {
  const it = parent.getFoldersByName(name);
  while (it.hasNext()) { const f = it.next(); if (!f.isTrashed()) return f; }
  return null;
}

function child_(parent, name) { return find_(parent, name) || parent.createFolder(name); }

function taken_(folder, fileName) {
  const it = folder.getFilesByName(fileName);
  while (it.hasNext()) if (!it.next().isTrashed()) return true;
  return false;
}

// "Name", then "Name (2)", "Name (3)"… so a new save never replaces a file a lesson record may already link to.
function freeName_(name, slots) {
  for (let n = 1; n < 100; n++) {
    const cand = n === 1 ? name : name + ' (' + n + ')';
    if (!slots.some(s => taken_(s[0], cand + s[1]))) return cand;
  }
  return name + ' (' + new Date().getTime() + ')';
}

function bytes_(part) {
  if (!part || typeof part.b64 !== 'string' || !part.b64) return null;
  return Utilities.base64Decode(part.b64);
}

function info_(f) { return { id: f.getId(), name: f.getName(), url: f.getUrl() }; }

function clean_(s) {
  return String(s || '').replace(/[\\/:*?"<>|\u0000-\u001f]+/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 120);
}

function desc_(meta, kind) {
  const when = Utilities.formatDate(new Date(), 'Australia/Sydney', 'd MMM yyyy');
  const bits = [kind + ' made with the HSC Economics Worksheet Maker, ' + when + '.'];
  const course = COURSE_NAMES[meta.course] || '';
  const size = [meta.count ? meta.count + ' questions' : '', meta.marks ? meta.marks + ' marks' : ''].filter(String).join(', ');
  if (course || size) bits.push([course, size].filter(String).join(': ') + '.');
  if (Array.isArray(meta.codes) && meta.codes.length) bits.push('Dot points: ' + meta.codes.slice(0, 30).join(', ') + '.');
  return bits.join(' ').slice(0, 1500);
}

// Script properties hold a little about each saved worksheet (its title, dot points and the answer copy) for list_.
function remember_(id, v) {
  const sp = PropertiesService.getScriptProperties();
  sp.setProperty('w:' + id, JSON.stringify(v));
  const all = sp.getProperties(), keys = Object.keys(all).filter(k => k.indexOf('w:') === 0);
  if (keys.length > 1500) { // keep well inside the 500 KB limit: forget the oldest
    const at = k => { try { return JSON.parse(all[k]).at || ''; } catch (e) { return ''; } };
    keys.sort((a, b) => (at(a) < at(b) ? -1 : 1)).slice(0, keys.length - 1200).forEach(k => sp.deleteProperty(k));
  }
}

function same_(a, b) {
  if (a.length !== b.length) return false;
  let d = 0;
  for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return d === 0;
}

function msg_(err) { return String((err && err.message) || err || 'error').slice(0, 300); }

function esc_(s) { return String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c])); }

// The hidden-frame route: hand the answer to the page that asked, by postMessage to each enclosing window.
// Only a window at one of ORIGINS receives it, and it checks the nonce it sent.
function frame_(res, req) {
  const origin = ORIGINS.indexOf(req.origin) >= 0 ? req.origin : ORIGINS[0];
  const msg = JSON.stringify({ worksheetSaver: 1, nonce: String(req.nonce || '').slice(0, 64), result: res })
    .replace(/</g, '\\u003c').replace(/[\u2028\u2029]/g, c => '\\u' + c.charCodeAt(0).toString(16));
  const js = '(function(){var m=' + msg + ',o=' + JSON.stringify(origin) + ',w=window;' +
    'for(var i=0;i<10&&w;i++){try{w.postMessage(m,o)}catch(e){}if(w===w.parent)break;w=w.parent}})();';
  return HtmlService.createHtmlOutput('<!DOCTYPE html><html><head><meta charset="utf-8"></head><body><script>' + js + '</script></body></html>')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}
