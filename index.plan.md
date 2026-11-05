Belongs to [index.html](index.html). Other notes for the same page: [decisions](index.decisions.md).

# Plan: site index (index.html), 5 Nov 2026


Goal: move the old Kstech landing page off `index.html`, give the site root a good-looking index of every page and the work done in this repo, and add an AGENTS.md with the five most useful upkeep rules.

## Steps
1. Read every page and its notes. Check how GitHub Pages serves this repo. Done.
2. `git mv index.html Kstech.html`. No content change. Done.
3. Build the new `index.html`: plain HTML and CSS, no script, same fonts and paper look as threatmodelling.html. Done.
4. Page outline: masthead, contents list (one numbered row per page, newest first, with what it is, how it was checked, links to notes and a small drawing), work log, footer with the Made with AI note. Done.
5. Write AGENTS.md from what the notes and pages already show. Done.
6. Render check: light, dark, 375px wide, no console errors, no em or en dashes, every link resolves. Done 5 Nov.

## Changes later the same day
7. Remove the work log. Done.
8. Remove `Kstech.html` and its row, and move the numbers down by one. Done.
9. Stop showing plans, decisions and fact checks to readers: links, legend, footer link and the MCP page's mention. Done.
10. Remove "Source on GitHub" and the name, and move Last updated to the footer. Done.

## Redesign, 5 Nov 2026
Goal: give the index a look of its own, since it matched `threatmodelling.html`.

11. Concept: a page from a book, printed in one ink. One large sentence names every page, each with a footnote number. The footnotes carry the details. A colophon at the end holds the date and the Made with AI note. Done.
12. Replace the fonts and colours. Keep the five small drawings. Done.
13. Update `AGENTS.md`, since it says to copy the look of `threatmodelling.html` and speaks of rows. Done.
14. Render check: light, dark, 375px wide, no console errors, no em or en dashes, every link resolves. Done.


## Second redesign, 5 Nov 2026
Goal: make the design beautiful and functional while keeping existing URLs and the site's upkeep rules.

15. Replace the oversized sentence and footnote grid with a distinct editorial introduction and one continuous numbered list. Done.
16. Retain every page, permanent number, illustration, summary, check note and download. Keep the shared AI disclosure verbatim. Done.
17. Add native browse, skip and return anchors, visible row focus, semantic dates and responsive metadata. Done.
18. Inspect desktop and mobile layouts in light and dark palettes, verify links and keyboard navigation, and check text contrast and paragraph length. Done. The dark palette was activated in a temporary preview copy without changing system settings.
19. Record the design decisions and index-specific fact check. Done. This is a static page with no build step and no added JavaScript.
