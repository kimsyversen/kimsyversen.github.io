# Decisions: site index (index.html)

Belongs to [index.html](index.html). Plan: [index.plan.md](index.plan.md).

5 Nov 2026

- (Superseded.) **Old front page moved to `Kstech.html`, content unchanged.** The name matches the page's own title. `git mv` keeps its history. The site root URL now shows the index, and no page in the repo linked to the old address by name.
- **A contents page, not a card grid.** One numbered row per page, newest first, set out like the contents of a printed report. Cards with coloured tops would look like a template, which is what this site avoids.
- **Numbers are permanent.** A page keeps its number for good and a new page takes the next one, so a number can be used to refer to a page.
- **Small line drawings instead of screenshots.** Screenshots go stale whenever a page changes. A drawing shows the idea of the page and stays true. Red marks the risk, the same meaning as the accent elsewhere.
- **Same printed look as `threatmodelling.html`.** Same fonts and colour tokens, so the index reads as part of the site.
- **Plain HTML and CSS, no script.** There is nothing to filter on six rows, and without a script there is nothing to break.
- **Each row says how the page was checked.** That is the most useful thing to know before trusting a page.
- (Superseded.) **Note links go to GitHub, not to relative paths.** Pages serves `.md` files as raw text, and GitHub shows them properly. These links only work once the notes are on `master`.
- (Superseded.) **The Work log is written by hand from the notes and git history.** 12 entries, one per real change. Each date was checked against the notes and `git log`.
- **"Updated" in a row is the last content change. "Current as of" on a page is the last fact check.** The two can differ: the AKS page was translated on 3 Nov, while its facts were last checked on 1 Nov.
- **`AGENTS.md` is uppercase.** That is the file name agent tools look for.
- **Title sized to fit the column.** The first version ran into the text beside it at 1280px. The first column now takes the width of the word, and the font size is capped so the text beside it keeps room.
- **Made with AI note added to the GitHub page.** It was the only page without one.
- **Two older AKS notes got a "Belongs to" line.** `AGENTS.md` asks for one on every note, and those two were the only ones without it.
- **No links back to the index from other pages.** Not asked for, and it would touch every page.

5 Nov 2026, later the same day, at the owner's request

- **`Kstech.html` removed.** The owner no longer needs it. It stays in git history. The drawing and row went with it.
- **Numbers moved down by one, once.** The index had not gone live, so nobody relied on a number, and a list ending at 2 would look like a mistake. From now on numbers stay put, as `AGENTS.md` says.
- **The index shows pages only.** Plans, decisions and fact checks are working notes, not for readers. Their links and the legend that explained them are gone, and so is the Design notes link. The draw.io links stay because a reader can use those files.
- **`AGENTS.md` link removed from the footer.** It is for whoever works on the site, the same as the notes.
- **Work log removed.** The owner does not want it on the page. Git history keeps the record.
- **The one-line check note stays on each row.** It links to nothing, and it is where a reader sees limits such as "Nothing tested on a real system". The workstation line no longer says "ledger", which readers would not know.
- **`MCP-Risk-Map.html` no longer names its fact check file.** Its date is unchanged, since this is not a content change.
- **The GitHub page keeps its link to `design-notes.md`.** That is where the page lists its sources, so cutting the link would hide them.
- **`github/` committed at the owner's request.** It was held back because promoting publishes it and it discusses classified work. All names in it are illustrative, a scan found no tokens or email addresses, and row 5 and its draw.io links need these files to work.
