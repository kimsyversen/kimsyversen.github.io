# Keeping this site up to date

Five rules for anyone changing this repo, person or agent. The site is hand-written HTML with no build step, so nothing updates itself. If you change something, you update what points at it.

## 1. Keep the index true

`index.html` is written by hand. Change it in the same commit as the page.

- New page: add a row at the top of Pages with the next number. A page keeps its number for good.
- Content change: update the row's Updated date and add a Work log line, newest first. Style fixes and footer notes do not count.
- Any edit to the index: update its Last updated date at the top.
- Notes: link them by their GitHub address, because Pages shows a `.md` file as raw text.

Find pages missing from the index:

```bash
for f in *.html github/*.html; do [ "$f" = index.html ] || grep -q "href=\"$f\"" index.html || echo "missing from index: $f"; done
```

Find broken links in the index:

```bash
grep -o 'href="[^"#:]*\.\(html\|drawio\)"' index.html | cut -d'"' -f2 | while read -r f; do [ -f "$f" ] || echo "broken link: $f"; done
```

## 2. Keep notes beside their page

- Name notes after the page: `<Page>.plan.md`, `<Page>.decisions.md`, `<Page>.factcheck.md`. If a page is renamed, rename its notes too.
- Start each note with a "Belongs to" line that links the page.
- Add to decisions as you go, with the reason. When a decision is replaced, mark the old one "(Superseded.)" and leave it in place. The history is the point.

## 3. Every claim has a source and a date

- Compare each factual claim with its primary source on the day, and log it in the page's fact check with a verdict.
- No source? Cut the claim, or label it `[unverified]` or `[inference]`.
- Say plainly what was not tested. "Nothing tested on a real system" is a finding, not a weakness.
- "Current as of" on a page means the day the facts were last checked. Move it only after a recheck, and update the ledger at the same time.
- Keep each paragraph to 60 words or fewer, so each claim can be checked on its own.

## 4. Do not break URLs or saved state

- File names are public URLs, and they are case sensitive. Rename only when asked, and search for links to the file first.
- Tab and box ids appear in URL hashes. Renaming one breaks links people have shared.
- All pages share one origin, so every `localStorage` key starts with a page prefix: `aks-`, `dev-`, `mcp-`. A new page needs its own. Changing a key loses what readers have saved.

## 5. Check before you call it done, and remember it is public

- Look at the page in light mode, in dark mode and at 375px wide. No sideways scroll, no console errors.
- Pages are in English. Every page carries the same Made with AI note, word for word. No em or en dashes.
- Copy the look of `threatmodelling.html`: rules, thin lines, plain tables, one accent colour with a clear meaning. No colored bars on cards, rounded shadow cards or gradient banners.
- Work on `dev`. `master` is the live site, and the owner moves work there.
- Everything that reaches `master` is public, including notes and this file. No secrets, no customer data.
