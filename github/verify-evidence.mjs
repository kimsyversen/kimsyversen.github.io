// Checks the per-claim evidence of github-two-enterprise-interactive.html.
//   node github/verify-evidence.mjs           fetch every source, check every quote, check the inline copy
//   node github/verify-evidence.mjs --write   also rewrite the inline EVID block from the TSV
//   node github/verify-evidence.mjs --list-r  also print every sentence treated as a design requirement or label
//   node github/verify-evidence.mjs --init-outside  write the reviewed list of outside texts (new texts get a guessed verdict: review them)
// Rules: a "D" row needs a source from that box's source list and a quote that appears
// in the fetched page, word for word. An "I" row marks an [inference] sentence.
// A sentence with no row is a design requirement or label: it makes no factual claim.
import fs from 'node:fs';
import vm from 'node:vm';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const HTML = path.join(here, 'github-two-enterprise-interactive.html');
const TSV = path.join(here, 'github-two-enterprise-interactive.evidence.tsv');
const OUT = path.join(here, 'github-two-enterprise-interactive.outside.tsv');
const args = new Set(process.argv.slice(2));

const problems = [];
const bad = (m) => problems.push(m);

// ---- page data (same code the page runs) ----
const html = fs.readFileSync(HTML, 'utf8');
const m = html.match(/<script>\n\(function\(\)\{([\s\S]*?)\/\* ---------- state ---------- \*\//);
if (!m) { console.error('cannot find page script'); process.exit(2); }
const sb = { document: { querySelector() { return null; }, querySelectorAll() { return []; }, createElement() { return {}; } }, window: {}, console };
vm.createContext(sb);
vm.runInContext(m[1] + '\n;globalThis.__out={D:D,ORDER:ORDER,SOURCES:SOURCES,DEV:DEV,FLOWTEXT:FLOWTEXT};', sb);
const { D, ORDER, SOURCES, DEV, FLOWTEXT } = sb.__out;
// The four design-choice notes are checked like box descriptions, as pseudo boxes DEV.1 to DEV.4.
// Their allowed sources are the sources of the boxes that carry that note.
for (const k of Object.keys(DEV)) {
  const id = `DEV.${k}`;
  D[id] = { d: DEV[k] };
  SOURCES[id] = [];
  for (const b of ORDER.slice()) if (String(D[b].dev) === k) for (const s of SOURCES[b] || []) if (!SOURCES[id].some((x) => x[1] === s[1])) SOURCES[id].push(s);
  ORDER.push(id);
}
const sentences = (id) => D[id].d.split(/(?<=[.!?])\s+/);
const bare = (s) => s.replace(/^\[inference\]\s*/, '');

// ---- normalising ----
const ent = { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ', rsquo: "'", lsquo: "'", ldquo: '"', rdquo: '"', ndash: '-', mdash: '-', hellip: '...' };
const unescapeHtml = (t) => t.replace(/&(#x[0-9a-f]+|#\d+|[a-z]+);/gi, (a, e) => {
  if (e[0] === '#') { const c = e[1].toLowerCase() === 'x' ? parseInt(e.slice(2), 16) : parseInt(e.slice(1), 10); return String.fromCodePoint(c); }
  return ent[e.toLowerCase()] ?? a;
});
const norm = (t) => unescapeHtml(t)
  .replace(/[’‘]/g, "'").replace(/[“”]/g, '"').replace(/ /g, ' ')
  .replace(/[\u2013\u2014]/g, '-')
  .replace(/\s+/g, ' ')
  .replace(/\s+([,.;:)])/g, '$1').replace(/\(\s+/g, '(')
  .trim();
const pageText = (raw) => {
  let t = raw;
  for (const tag of ['script', 'style', 'noscript', 'svg', 'nav', 'header', 'footer']) {
    t = t.replace(new RegExp('<' + tag + '\\b[\\s\\S]*?</' + tag + '>', 'gi'), ' ');
  }
  t = t.replace(/<\/?(p|li|h1|h2|h3|h4|tr|div|br|td|th|pre)\b[^>]*>/gi, '\n').replace(/<[^>]+>/g, ' ');
  return norm(t);
};

// ---- TSV ----
const lines = fs.readFileSync(TSV, 'utf8').split('\n').filter(Boolean);
if (lines.shift().split('\t')[0] !== 'box') bad('TSV header missing');
const rows = lines.map((l, i) => {
  const c = l.split('\t');
  if (c.length !== 5) bad(`TSV line ${i + 2}: expected 5 columns, got ${c.length}`);
  return { box: c[0], prefix: c[1], kind: c[2], url: c[3], quote: c[4] };
});

// ---- fetch sources ----
const urls = [...new Set(rows.filter((r) => r.kind === 'D').map((r) => r.url))];
const pages = new Map();
async function get(u) {
  for (let a = 0; a < 3; a++) {
    try {
      const r = await fetch(u, { redirect: 'follow', headers: { 'user-agent': 'Mozilla/5.0 (evidence check)' }, signal: AbortSignal.timeout(40000) });
      if (r.ok) return pageText(await r.text());
      if (a === 2) return 'HTTP ' + r.status;
    } catch (e) { if (a === 2) return 'ERR ' + e.message; }
  }
}
let next = 0;
await Promise.all(Array.from({ length: 6 }, async () => {
  while (next < urls.length) { const u = urls[next++]; pages.set(u, await get(u)); }
}));
for (const [u, t] of pages) if (/^(HTTP|ERR) /.test(t) || t.length < 500) bad(`source did not load: ${u} (${t.slice(0, 40)})`);

// ---- quotes ----
const parts = (q) => q.split('~').map(norm);
function present(text, q) {
  const [a, b] = parts(q);
  const i = text.indexOf(a);
  if (i < 0) return false;
  if (b === undefined) return true;
  const j = text.indexOf(b, i);
  return j >= 0 && j - i < 900;
}
const simple = (w) => /^[A-Za-z0-9]+$/.test(w);
function run(words, fromEnd) {
  const w = fromEnd ? [...words].reverse() : words;
  let k = 0; while (k < w.length && !simple(w[k])) k++;
  const out = [];
  while (k < w.length && simple(w[k]) && out.length < 4) out.push(w[k++]);
  return (fromEnd ? out.reverse() : out).join(' ');
}
function fragment(q) {
  const [a, b] = parts(q);
  const aw = a.split(' ');
  const bw = (b ?? a).split(' ');
  const s = run(aw, false), e = run(bw, true);
  const enc = (x) => encodeURIComponent(x).replace(/-/g, '%2D');
  if (!s || !e) return '';
  if (s === e || (b === undefined && aw.length <= 8 && aw.every(simple))) return '#:~:text=' + enc(b === undefined && aw.every(simple) ? a : s);
  return '#:~:text=' + enc(s) + ',' + enc(e);
}

// ---- row checks ----
const covered = new Map(); // box -> Set(sentence index)
const evid = {};
const titleOf = (box, url) => (SOURCES[box] || []).find((s) => s[1] === url)?.[0];
for (const r of rows) {
  if (!D[r.box]) { bad(`unknown box ${r.box}`); continue; }
  const hit = sentences(r.box).map((s, i) => [bare(s), i]).filter(([s]) => s.startsWith(r.prefix));
  if (hit.length !== 1) { bad(`${r.box}: "${r.prefix}" matches ${hit.length} sentences`); continue; }
  const [text, idx] = hit[0];
  const tagged = /^\[inference\]/.test(sentences(r.box)[idx]);
  if (r.kind === 'I' && !tagged) bad(`${r.box}: I row but sentence has no [inference] tag: ${text.slice(0, 50)}`);
  if (r.kind === 'D' && tagged) bad(`${r.box}: D row on an [inference] sentence: ${text.slice(0, 50)}`);
  if (!covered.has(r.box)) covered.set(r.box, new Set());
  covered.get(r.box).add(idx);
  evid[r.box] = evid[r.box] || [];
  let e = evid[r.box].find((x) => x[0] === r.prefix);
  if (!e) { e = [r.prefix, r.kind, []]; evid[r.box].push(e); }
  if (r.kind === 'D') {
    if (!titleOf(r.box, r.url)) bad(`${r.box}: source not in its source list: ${r.url}`);
    const t = pages.get(r.url);
    if (!t || !present(t, r.quote)) bad(`QUOTE NOT FOUND ${r.box} "${r.prefix}": ${r.quote.slice(0, 90)}`);
    const q = parts(r.quote).join(' ... ');
    const frag = fragment(r.quote);
    if (!frag) bad(`${r.box}: no usable text fragment for ${r.quote.slice(0, 60)}`);
    e[2].push([q, r.url + frag, titleOf(r.box, r.url) || r.url]);
  }
}
// sentences tagged [inference] must have an I row
for (const id of ORDER) {
  if (!D[id].d) continue;
  sentences(id).forEach((s, i) => { if (/^\[inference\]/.test(s) && !(covered.get(id)?.has(i))) bad(`${id}: [inference] sentence has no I row: ${s.slice(0, 60)}`); });
}
// paragraph length (same split the popup uses)
for (const id of ORDER) {
  if (!D[id].d) continue;
  let p = '';
  for (const s of sentences(id)) {
    if ((p + ' ' + s).trim().split(/\s+/).length > 60 && p) p = '';
    p += (p ? ' ' : '') + s;
    if (p.split(/\s+/).length > 60) bad(`${id}: paragraph over 60 words`);
  }
}

// ---- text outside the descriptions ----
// Card summaries, chips, flow steps, flow banners and the page lead have no evidence list.
// They may hold design requirements and labels only. Any claim about what GitHub or another
// product does belongs in a description, where it gets a number and a quote. This catches
// wording that usually states such a claim; it cannot prove a sentence is a requirement.
const FACTY = /\b(cannot|can not|can't|does not|do not support|not support\w*|supports?|synchroni[sz]\w*|syncs?|never|always|by default|requires?|available|automatic\w*|enforces?|prevents?)\b/i;
const outside = [];
for (const id of ORDER) {
  const n = D[id];
  if (n.s) outside.push([`${id} summary`, n.s]);
  if (n.t) outside.push([`${id} title`, n.t]);
  (n.chips || []).forEach((c, i) => outside.push([`${id} chip ${i + 1}`, c[1]]));
  (n.steps || []).forEach((c, i) => outside.push([`${id} step ${i + 1}`, String(c)]));
}
for (const k of Object.keys(FLOWTEXT)) outside.push([`flow banner ${k}`, FLOWTEXT[k]]);
const lead = html.match(/<p class="lead">([\s\S]*?)<\/p>/g) || [];
lead.forEach((l, i) => outside.push([`page text ${i + 1}`, l.replace(/<[^>]+>/g, ' ')]));
for (const [where, text] of outside) if (FACTY.test(text)) bad(`${where} has fact-style wording (move the claim to a description with a source, or reword): ${text.slice(0, 90)}`);
console.log(`text outside descriptions checked for fact-style wording: ${outside.length} items`);


// ---- every text outside the descriptions must have a recorded review ----
// The list is github-two-enterprise-interactive.outside.tsv: verdict, where, text.
//   R = design requirement or test step (no claim about a product)
//   L = label, title or interface text
//   N = code token that is never shown as text (class names, ids)
// A text that is not in the list, or whose wording changed since it was reviewed, fails the run.
// The check proves a person recorded a verdict for the exact current wording. It does not
// prove the verdict is right: that is a review, logged in the page's decisions note.
function literals(src) {
  const out = []; let i = 0, prev = ''; const n = src.length;
  while (i < n) {
    const c = src[i];
    if (c === '/' && src[i + 1] === '*') { const j = src.indexOf('*/', i + 2); i = j < 0 ? n : j + 2; continue; }
    if (c === '/' && src[i + 1] === '/') { const j = src.indexOf('\n', i); i = j < 0 ? n : j; continue; }
    if (c === "'" || c === '"') {
      let j = i + 1, t = '';
      while (j < n && src[j] !== c) {
        if (src[j] === '\\') { const e = src[j + 1]; t += e === 'n' ? '\n' : e === 't' ? '\t' : e === 'u' ? String.fromCharCode(parseInt(src.slice(j + 2, j + 6), 16)) : e; j += e === 'u' ? 6 : 2; }
        else { t += src[j]; j++; }
      }
      out.push(t); i = j + 1; prev = '"'; continue;
    }
    if (c === '`') { let j = i + 1; while (j < n && src[j] !== '`') { if (src[j] === '\\') j++; j++; } out.push(src.slice(i + 1, j)); i = j + 1; prev = '"'; continue; }
    if (c === '/' && ('(,=:[!&|?{};'.includes(prev) || prev === '')) {
      let j = i + 1, cls = false;
      while (j < n) { if (src[j] === '\\') j += 2; else { if (src[j] === '[') cls = true; else if (src[j] === ']') cls = false; else if (src[j] === '/' && !cls) break; j++; } }
      i = j + 1; while (/[a-z]/.test(src[i] || '')) i++; prev = ')'; continue;
    }
    if (!/\s/.test(c)) prev = c;
    i++;
  }
  return out;
}
const visibleOf = (raw) => {
  const found = [];
  for (const a of raw.matchAll(/\b(?:title|aria-label|alt|placeholder)="([^"]*)"/g)) found.push(a[1]);
  const body = raw.replace(/<[^>]*>/g, ' ');
  found.push(body);
  return found.map((t) => unescapeHtml(t).replace(/\s+/g, ' ').trim()).filter((t) => /[A-Za-z]{2}/.test(t) && !/^https?:/.test(t));
};
const outsideMap = new Map(); // text -> where
const note = (text, where) => { if (!outsideMap.has(text)) outsideMap.set(text, where); };
// where-hints from the structured data
for (const id of ORDER) {
  const n = D[id];
  if (!n.d && !n.t) continue;
  if (n.t) note(n.t, `${id} title`);
  if (n.s) note(n.s, `${id} summary`);
  if (n.v) note(n.v, `${id} proposed check`);
  (n.chips || []).forEach((c) => note(c[1], `${id} chip`));
  (n.steps || []).forEach((c) => note(String(c), `${id} step`));
  if (n.lane) { if (n.lane.note) note(n.lane.note, `${id} lane note`); (n.lane.steps || []).forEach((c) => note(c[1], `${id} lane step`)); }
}
for (const k of Object.keys(FLOWTEXT)) note(FLOWTEXT[k], `flow banner ${k}`);
// description sentences with no evidence row (design requirements or labels) are reviewed too
for (const id of ORDER) {
  if (!D[id].d) continue;
  sentences(id).forEach((s, i) => { if (!rows.some((r) => r.box === id && bare(s).startsWith(r.prefix))) note(s, `${id} description[${i}]`); });
}
const descSet = new Set(ORDER.map((i) => D[i].d).filter(Boolean));
const scriptSrc = html.match(/<script>\n(\(function\(\)\{[\s\S]*?)<\/script>/)[1].replace(/\/\* EVID:begin \*\/[\s\S]*?\/\* EVID:end \*\//, '');
for (const lit of literals(scriptSrc)) {
  if (descSet.has(lit) || /^https?:/.test(lit) || lit === 'use strict') continue;
  for (const t of visibleOf(lit)) if (!descSet.has(t)) note(t, 'script');
}
const bodyHtml = html.replace(/<script\b[\s\S]*?<\/script>/gi, ' ').replace(/<style\b[\s\S]*?<\/style>/gi, ' ').replace(/<svg\b[\s\S]*?<\/svg>/gi, ' ');
for (const blk of bodyHtml.split(/<\/?(?:p|h1|h2|h3|li|div|figcaption|nav|header|footer|figure|section|body|html|head|span|b|a)\b[^>]*>/i)) for (const t of visibleOf(blk)) note(t, 'page text');
for (const a of bodyHtml.matchAll(/\b(?:title|aria-label)="([^"]*)"/g)) note(unescapeHtml(a[1]), 'page text');
const guessVerdict = (text, where) => {
  if (/^[a-z0-9]+([ .-][a-z0-9]+)*$/.test(text) && !/\s/.test(text.trim().replace(/-/g, ''))) return 'N';
  if (/^[A-Za-z]+(\.[A-Za-z0-9]+)+$/.test(text)) return 'N';
  if (/ (summary|proposed check)$/.test(where)) return 'R';
  return 'L';
};
const header = 'verdict\twhere\ttext\n';
if (args.has('--init-outside')) {
  const old = new Map();
  if (fs.existsSync(OUT)) for (const l of fs.readFileSync(OUT, 'utf8').split('\n').slice(1).filter(Boolean)) { const c = l.split('\t'); old.set(c.slice(2).join('\t'), c[0]); }
  const lines2 = [...outsideMap].map(([t, w]) => `${old.get(t) ?? guessVerdict(t, w)}\t${w}\t${t}`);
  fs.writeFileSync(OUT, header + lines2.join('\n') + '\n');
  console.log(`wrote ${lines2.length} outside texts (${lines2.filter((l) => !old.has(l.split('\t').slice(2).join('\t'))).length} new: review their verdicts)`);
}
{
  const reviewed = new Map();
  if (!fs.existsSync(OUT)) bad(`missing ${path.basename(OUT)} (run with --init-outside, then review it)`);
  else {
    const ls = fs.readFileSync(OUT, 'utf8').replace(/\r/g, '').split('\n').filter(Boolean);
    if (ls.shift() !== header.trim()) bad('outside list header must be: verdict, where, text');
    for (const l of ls) {
      const c = l.split('\t');
      if (c.length !== 3) { bad(`outside list line has ${c.length} columns: ${l.slice(0, 60)}`); continue; }
      if (!['R', 'L', 'N'].includes(c[0])) bad(`outside list: verdict must be R, L or N: ${l.slice(0, 60)}`);
      if (reviewed.has(c[2])) bad(`outside list: duplicate text: ${c[2].slice(0, 60)}`);
      reviewed.set(c[2], c[0]);
    }
  }
  let unreviewed = 0, stale = 0;
  for (const [t, w] of outsideMap) if (!reviewed.has(t)) { unreviewed++; bad(`NOT REVIEWED or changed since review (${w}): ${t.slice(0, 100)}`); }
  for (const t of reviewed.keys()) if (!outsideMap.has(t)) { stale++; bad(`outside list entry no longer on the page (remove it): ${t.slice(0, 100)}`); }
  const cnt = { R: 0, L: 0, N: 0 };
  for (const v of reviewed.values()) cnt[v] = (cnt[v] || 0) + 1;
  console.log(`outside texts: ${outsideMap.size} found, ${reviewed.size} reviewed (R ${cnt.R}, L ${cnt.L}, N ${cnt.N}), ${unreviewed} unreviewed, ${stale} stale`);
}

// ---- inline copy ----
const block = '/* EVID:begin */\n  var EVID = {\n' +
  Object.keys(evid).sort().map((k) => '    ' + JSON.stringify(k) + ': ' + JSON.stringify(evid[k])).join(',\n') + '\n  };\n  /* EVID:end */';
const cur = html.match(/\/\* EVID:begin \*\/[\s\S]*?\/\* EVID:end \*\//);
if (args.has('--write') && !problems.length) {
  if (cur) fs.writeFileSync(HTML, html.replace(cur[0], () => block));
  else { console.error('no EVID markers in the page: add /* EVID:begin */ /* EVID:end */ once'); process.exit(2); }
  console.log('inline EVID written');
} else if (!cur || cur[0] !== block) bad('inline EVID is missing or differs from the TSV (run with --write)');

// ---- summary ----
let nD = 0, nI = 0, nR = 0;
for (const id of ORDER) {
  if (!D[id].d) continue;
  sentences(id).forEach((s, i) => {
    const rowsHere = rows.filter((r) => r.box === id && bare(s).startsWith(r.prefix));
    if (!rowsHere.length) { nR++; if (args.has('--list-r')) console.log(`R ${id}[${i}] ${s}`); }
    else if (rowsHere[0].kind === 'I') nI++; else nD++;
  });
}
console.log(`sentences: ${nD} sourced (D), ${nI} inference (I), ${nR} design requirement or label (R)`);
console.log(`quotes checked: ${rows.filter((r) => r.kind === 'D').length} against ${urls.length} pages`);
if (problems.length) { console.log('\nPROBLEMS (' + problems.length + ')'); problems.forEach((p) => console.log(' - ' + p)); process.exit(1); }
console.log('OK');
