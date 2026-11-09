Belongs to [index.html](index.html). Plan: [index.plan.md](index.plan.md).

# Decisions: site index (index.html)


5 Nov 2026

- (Superseded.) **Old front page moved to `Kstech.html`, content unchanged.** The name matches the page's own title. `git mv` keeps its history. The site root URL now shows the index, and no page in the repo linked to the old address by name.
- (Superseded.) **A contents page, not a card grid.** One numbered row per page, newest first, set out like the contents of a printed report. Cards with coloured tops would look like a template, which is what this site avoids.
- **Numbers are permanent.** A page keeps its number for good and a new page takes the next one, so a number can be used to refer to a page.
- **Small line drawings instead of screenshots.** Screenshots go stale whenever a page changes. A drawing shows the idea of the page and stays true. Red marks the risk, the same meaning as the accent elsewhere.
- (Superseded.) **Same printed look as `threatmodelling.html`.** Same fonts and colour tokens, so the index reads as part of the site.
- **Plain HTML and CSS, no script.** There is nothing to filter on six rows, and without a script there is nothing to break.
- **Each row says how the page was checked.** That is the most useful thing to know before trusting a page.
- (Superseded.) **Note links go to GitHub, not to relative paths.** Pages serves `.md` files as raw text, and GitHub shows them properly. These links only work once the notes are on `master`.
- (Superseded.) **The Work log is written by hand from the notes and git history.** 12 entries, one per real change. Each date was checked against the notes and `git log`.
- **"Updated" in a row is the last content change. "Current as of" on a page is the last fact check.** The two can differ: the AKS page was translated on 3 Nov, while its facts were last checked on 1 Nov.
- **`AGENTS.md` is uppercase.** That is the file name agent tools look for.
- (Superseded.) **Title sized to fit the column.** The first version ran into the text beside it at 1280px. The first column now takes the width of the word, and the font size is capped so the text beside it keeps room.
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
- **"Source on GitHub" removed from the footer.** The owner does not want it on the page.
- **Name removed and Last updated moved to the footer.** The owner asked for both. The line at the top held only those two things, so it went too, and `AGENTS.md` now says the date is at the bottom. The name stays in the browser tab title, which is not on the page.

5 Nov 2026, redesign at the owner's request

- **The index has its own look.** The owner said it looked the same as the threat modeling page. `AGENTS.md` now says content pages copy that look and the index does not. The bans on template looks still apply to every page.
- (Superseded.) **One sentence with footnotes.** The list of pages is the headline, so the design comes from the content and not from decoration. The details sit in footnotes, under the numbers the pages already had.
- **A technical drawing sheet was considered and not built.** Its frame and ruled grid sit close to the grid look this site avoids.
- (Superseded.) **Titles appear twice, in the sentence and the footnote.** That is the cost of this design: a new page needs two edits. `AGENTS.md` says so.
- (Superseded.) **One blue ink on warm paper, set only in EB Garamond.** No other page uses these. Dark mode swaps ink and paper. Red still marks risk in the drawings and nothing else.
- (Superseded.) **File names no longer show.** Readers do not need them, since the links go there. "Newest first" moved into the sentence. The "Pages" heading stays for screen readers but is hidden.
- (Superseded.) **Footnote marks jump at once.** With smooth scrolling on, a link to `#n3` stayed near the top in the preview pane. Without it, the jump landed correctly. The target footnote's title is filled so a reader sees where they landed.
- (Superseded.) **Hover on the big links thickens the underline.** The filled block used elsewhere cut into the line above at this type size.


5 Nov 2026, second redesign at the owner's request

- **An editorial index with one row per page.** The oversized opening sentence and two-column footnotes made the collection difficult to scan. A separate title, short introduction and continuous ruled list give each page a clear place.
- **Warm ivory and charcoal, with blue for navigation.** The earlier all-blue page competed with its links. Dark mode uses charcoal paper and pale blue links. Red retains its existing meaning in the drawings: risk.
- **Serif titles and sans-serif details.** EB Garamond keeps the index distinct from the content pages. Public Sans makes descriptions, check notes and dates easier to read at smaller sizes. Both have system fallbacks.
- **The sentence and permanent numbers remain.** Shorter topic links lead directly to the same pages. Their superscript numbers still jump to `n5` through `n1`. Each topic and number wraps as one unit. Explicit list values keep the semantic order consistent with the numbers.
- **A visible Pages heading and aligned metadata.** Readers can scan titles, types and update dates. The count and newest-first label explain the order without requiring readers to parse the introduction. Mobile moves metadata above each title and retains the drawings.
- **Whole-row links with separate download links.** A title's link covers its row, with an arrow showing the action. The two draw.io links stay above that hit area. Hover underlines the title; keyboard focus outlines the row. A footnote target gets a quiet background and underlined title.
- **Native navigation, no script.** Browse pages, Skip to pages and Back to top use normal anchors. There is no search or filtering for a collection of five pages. No animation, state storage or new dependency is needed.
- **The earlier content stays.** Page summaries, check notes, destinations, stable IDs and individual update dates are unchanged. The shared AI disclosure remains verbatim. The owner's name, source link, working notes and work log stay off the page.
- **Verification.** Light and dark palettes were inspected at desktop and 375px widths. The dark check used an untracked temporary copy activating the production dark CSS, then removed it. Intermediate and smaller widths, keyboard focus, footnote navigation, local links, text contrast and paragraph lengths were also checked. See `index.factcheck.md` for scope and limits.


5 Nov 2026, entry 06

- Add "Enterprise AI agent security" as entry 06, category Recommendation, updated 5 Nov 2026. The count reads 06 pages. Existing entries keep their numbers and ids.
- The drawing shows five stacked layers with a red dashed line down the side for the feedback and kill path.


6 Nov 2026, entry 08

- Add "Intune and MCP" as entry 08, category Design, updated 6 Nov 2026. The count reads 08 pages. Existing entries keep their numbers and ids.
- The drawing shows three stepped boxes (deliver, enforce, detect) with a red dashed line along the bottom for the re-apply loop.

## 8 Nov 2026, work in progress pages moved to wip/
- Moved `enterprise-ai-agent-governance-summary`, `enterprise-ai-agent-security-recommendation` and `Developer-WS2`, with all their notes, into `wip/`. Removed their three cards from the index. The index now lists 05 pages. The other pages keep their numbers 1 to 5.
- Reason: the user asked to move them to the work-in-progress folder and hide them from the index.
- Old URLs at the site root no longer work. The pages still open at `wip/<name>.html` if someone has the link. Moving the folder to `master` makes them public there too.
- Scripts under `scripts/` now read these pages from `wip/`. `Developer-WS2` links to `../Developer-WS.html`.

8 Nov 2026, entry 09

- Add "MCP governance in a Microsoft ecosystem" as entry 09, category Reference design, updated 8 Nov 2026. The count reads 06 pages. Entry numbers 6 to 8 belonged to pages moved to `wip/`, so they are not reused: old `#n6` to `#n8` anchors stay unused. Existing entries keep their numbers.
- The drawing shows client, gateway and backend boxes with a red dashed line for the bypass route the design blocks.

9 Nov 2026, at the owner's request

- **Every section is linkable.** Each section and each h2 and h3 has an id, and each h2 and h3 is a link to it. The link sits around the heading text, so the heading's text does not change and the checks that read it still pass. The `#` shows on hover or focus, and always faintly on touch screens.
- **One script adds the ids and links, `scripts/section_anchors.py`.** It never changes an id that exists, because old ids are public anchors. The three builders call it, so a rebuild keeps the links. `--check` fails if a section is missing one.
- **Tab ids are reserved.** On the three tabbed pages the address `#basics` means a tab. A section id equal to a tab id would switch tabs instead of scrolling, so new ids skip those names.
- **A link to a section inside a hidden tab opens that tab first.** The tab script on AKS, Developer-WS and MCP-Risk-Map now does this, at load and on address change.
- **Headings that are links to another page are left alone.** The index entries already have ids on their rows (n1 to n9).
- **Index dates not moved.** Ids and links add no content, so no entry date or footer date changed.

