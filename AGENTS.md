# Keeping this site up to date

Five rules for anyone changing this repo, person or agent. The site is hand-written HTML with no build step, so nothing updates itself. If you change something, you update what points at it.

## 1. Keep the index true

`index.html` is written by hand. Change it in the same commit as the page.

- New page: put it first in the sentence at the top, with a footnote mark, and add its footnote at the top of Pages. Both take the next number. A page keeps its number for good.
- Removed page: delete it from the sentence and delete its footnote. The others keep their numbers.
- Content change: update the Updated date in its footnote. Style fixes and footer notes do not count.
- Any edit to the index: update its Last updated date at the bottom.

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
- Plans, decisions and fact checks are for whoever works on the site, not for readers. Do not link or name them on a page.
- Add to decisions as you go, with the reason. When a decision is replaced, mark the old one "(Superseded.)" and leave it in place. The history is the point.

## 3. Every claim has a source and a date

- Compare each factual claim with its primary source on the day, and log it in the page's fact check with a verdict.
- No source? Cut the claim, or label it `[unverified]` or `[inference]`.
- Say plainly what was not tested. "Nothing tested on a real system" is a finding, not a weakness.
- "Current as of" on a page means the day the facts were last checked. Move it only after a recheck, and update the ledger at the same time.
- Keep each paragraph to 60 words or fewer, so each claim can be checked on its own.
- In a diagram, the reader must be able to verify every factual claim from the diagram itself, in a few clicks. Each claim that rests on a source shows that source beside it, with the exact quote and a link that opens the page at that passage. A box-level list of sources is not enough. Design requirements and labels are marked as such, with no source needed. A claim with no verifiable source is cut or labelled `[unverified]` or `[inference]`.
- Text with no evidence list (card summaries, titles, chips, flow steps, banners, page lead) holds design requirements and labels only. A claim about what a product does goes in a description, where it gets a number, a quote and a link. A script should fail when such text uses fact-style wording. Keep a reviewed list of every such text with a verdict (requirement, label or code token). A script should fail when a text is missing from the list or changed since it was reviewed. The script proves a verdict was recorded for the exact wording, not that the verdict is right, so say that in the notes.
- Check the quotes mechanically: fetch each source and confirm the quote appears in it, word for word. Re-run this before you move "Current as of". A quote that no longer matches means the claim must be rechecked.

## 4. Do not break URLs or saved state

- File names are public URLs, and they are case sensitive. Rename only when asked, and search for links to the file first.
- Tab and box ids appear in URL hashes. Renaming one breaks links people have shared.
- All pages share one origin, so every `localStorage` key starts with a page prefix: `aks-`, `dev-`, `mcp-`. A new page needs its own. Changing a key loses what readers have saved.

## 5. Check before you call it done, and remember it is public

- Look at the page in light mode, in dark mode and at 375px wide. No sideways scroll, no console errors.
- Interactive diagrams: test the behavior, not only the look. With each filter on, open every highlighted box and click every link in its popup (sources, Part of, Related). Each link must do what its label says and leave the right filter, popup and URL hash. Use real mouse clicks for a sample, because script clicks can hide bugs. Check each source URL loads, and test that a saved `#f=` or `#n=` link restores the same state. Log what you tested in the page's decisions or fact check.
- Pages are in English. Every page carries the same Made with AI note, word for word. No em or en dashes.
- Content pages copy the look of `threatmodelling.html`: rules, thin lines, plain tables, one accent colour with a clear meaning. The index has its own look. On every page: no colored bars on cards, rounded shadow cards or gradient banners.
- Work on `dev`. `master` is the live site, and the owner moves work there.
- Everything that reaches `master` is public, including notes and this file. No secrets, no customer data.
