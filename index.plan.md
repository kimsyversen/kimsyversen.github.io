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

## Entry 08, 6 Nov 2026

20. Add `Developer-WS2.html` as entry 08 with description, drawing, category and updated date. Update the page count. Done.
21. Run the missing-page and broken-link checks from `AGENTS.md`. Done, both print nothing.

## Entry 09, 8 Nov 2026

22. Add `mcp-governance-microsoft.html` as entry 09 with description, drawing, category and updated date. Update the page count to 06. Done.
23. Check the new link and the index layout on desktop and a narrow viewport. See below.

## Redesign proposal, 14 Nov 2026

Status: proposed, not implemented. Scope: presentation and index summaries only.

### Direction: Security engineering

Keep the editorial character, but make the collection itself the focus. Use a compact introduction and a continuous list with stronger title hierarchy. Avoid a dashboard, card grid, featured-content duplication or new filtering controls for the current eight entries.

Proposed opening copy:

> Security engineering
>
> Guides, risk maps and reference designs for AI, development and cloud security.

This is proposed editorial copy, not a new claim about the underlying guidance being validated.

### Findings from the current source

Inspected `index.html`, `index.decisions.md` and `index.factcheck.md` on 14 Nov 2026.

- Eight entries are present, numbered 12, 11, 10, 05, 04, 03, 02 and 01. Permanent numbers are not the page count.
- The desktop heading reaches 160px. The list assigns separate columns to number, drawing, copy, metadata and arrow.
- Several descriptions include interaction instructions. The MCP Risk Map description also enumerates control options and risk counts.
- The collection is in descending entry-number order, not update-date order. “Newest first” can be misread as most recently updated.
- The existing decision record excludes the owner's name, source link, work log and working-note links from the visible page. Keep those exclusions.

Design judgment: reducing introductory height and auxiliary columns should give titles more space and bring more entries into view. Confirm this in a rendered prototype; it has not been measured.

### Page structure and visual specification

| Area | Job and proposed treatment |
| --- | --- |
| Introduction | Name the subject. Left-aligned heading, 56–72px desktop and 36–44px mobile, with one sentence below. Remove the extra eyebrow and visible Browse pages link; retain the keyboard skip link. |
| Pages | The sole catalogue, with every entry appearing once. Retain the Pages heading and show “8 pages”; omit the order caption. Preserve descending permanent-number order. |
| Entry | Small permanent number; prominent linked title; one sentence describing its scope; a quiet line containing the existing type and explicit Updated date. Use thin separators and about 24px vertical padding. |
| Footer | Last updated date, Back to top and the existing Made with AI disclosure verbatim. |

Retain warm ivory, charcoal and blue links. Keep serif titles with sans-serif descriptions, using the existing fonts and fallbacks. Limit the content width to approximately 1040px. Use a 32px number column and a flexible text column; place metadata below the description instead of in a dedicated right column. Remove decorative drawings and row arrows from the index so long titles have room. Do not change diagrams on destination pages.

On mobile, keep numbers beside titles and let descriptions and metadata wrap beneath the title. Use 20px side gutters and no fixed-height rows or truncated text. Retain automatic dark mode, visible keyboard focus and a distinct target state for linked entries.

### Proposed copy examples

These are draft reductions of existing index descriptions; verify against each destination before implementation.

| Entry | Proposed title | Proposed description |
| --- | --- | --- |
| 12 | MCP governance threat model | STRIDE scenarios, attack preconditions, public evidence and model limits for the MCP governance design. |
| 11 | MCP governance in Microsoft | A proposed governance design covering identity boundaries, policy enforcement and preview limits. |
| 03 | MCP Risk Map | Risks and checks for connecting AI agents to MCP servers, with general and Microsoft ecosystem views. |

Preserve meaningful qualifications such as “proposed” and “model limits”. Do not add “verified”, “production-ready”, confidence scores or review badges. Preserve other titles unless shortening them materially improves clarity.

### Implementation and acceptance

1. Build the proposed layout on `dev`, preserving all eight destination URLs, list values and existing anchors, including `#top`, `#pages` and `#n12` through the currently present entry IDs. Do not reuse retired numbers.
2. Keep plain HTML and CSS with no framework, JavaScript, new storage or dependencies. Retain semantic headings and full-row link focus behavior.
3. Review all summary edits against their destination pages, then record verdicts in `index.factcheck.md`. Record accepted design decisions in `index.decisions.md`, marking conflicting older decisions superseded.
4. Preserve destination content dates for a presentation-only redesign. Advance an entry date only if its actual content changes; update the index footer for the redesign.
5. Check links and fragments, keyboard navigation and full-row click targets. Run `python3 -I scripts/section_anchors.py --check`.
6. Inspect desktop and 375px mobile layouts in light and dark modes, including the longest title. Check horizontal overflow, console errors, readable contrast and wrapping. Test 200% zoom. Record any untested cases.

No layout has been implemented or browser-tested for this proposal. The existing uncommitted index date changes and MCP Risk Map work are outside this proposal and remain untouched.

### Reviewable HTML, 14 Nov 2026

Created `index-redesign.html` beside the current index as a separate design proposal. It retains all eight entry destinations, numbers and anchors, the original update dates and AI disclosure. The original `index.html` was not changed by this preview work. The proposal is deliberately absent from the published catalogue and carries `noindex` metadata.

The preview implements the compact heading, two-column numbered rows, inline metadata, shorter summaries and removal of decorative drawings. Summary changes reduce existing index copy without adding technical claims; the Microsoft proposal retains explicit manual policy steps and preview limits. Source checks included the destination's scope and preview controls.

Validation: local destination links, fragment targets, permanent numbers and the repository section-anchor check passed. Browser inspection was blocked because the browser security policy disallows local file URLs. Desktop/mobile rendering, dark mode, console output, keyboard interaction and 200% zoom therefore remain untested for this proposal.

### Creative revision, 14 Nov 2026

At the owner's request for a more creative direction, `index-redesign.html` now uses a split editorial composition: a sticky forest-black masthead, acid-lime italic “mapped.” lettering, abstract orbital decoration, and a two-column catalogue with oversized permanent numbers. Hover and fragment targets highlight the complete entry in lime. At intermediate widths the catalogue becomes a numbered list; on mobile the masthead returns to normal document flow above it. This supersedes the preview's earlier compact ivory-list treatment, not the published index decisions.

All eight entries still appear once and their destinations, numbers and dates remain unchanged. No new technical claims, scripts, storage or dependencies were added. Anchor, local link and whitespace checks passed again. The previously recorded browser restriction remains; responsive rendering, dark mode and interactions have not been visually verified.

### Illustrated catalogue revision, 14 Nov 2026

The owner rejected the dark split-layout proposal. Replaced that preview with a light architectural catalogue: compact header, cool neutral background, blue navigation, and two columns of illustrated page cards. Each card reuses its page's existing decorative SVG from the current index, set against a subtle dot field, with the permanent number, title, summary, type and date. On narrow screens cards stack into one column. The full-height sidebar, lime palette, oversized numbers and orbital artwork are removed. This replaces the rejected proposal only; `index.html` remains untouched.

Local links, fragments, permanent numbers, eight retained SVGs, section anchors and whitespace checks passed. Browser visual checks remain unperformed under the previously recorded local-file restriction. This is a review draft, not an accepted replacement for the published index.

### Expandable list revision, 14 Nov 2026

The owner approved the colours and requested an innovative list instead of tiles. The preview now presents eight continuous numbered rows with type, linked title, date and a plus/minus disclosure control. Native `details` elements reveal each existing illustration and summary beneath its row; the first is initially open to demonstrate the treatment. Multiple rows can remain open. Titles navigate directly to the original pages. The accepted palette, header, content dates and footer remain unchanged; no scripts or saved settings were introduced.

Static checks passed for all eight disclosure structures, page destinations, permanent numbers, fragments and section anchors. The browser restriction still prevents rendered desktop/mobile and keyboard interaction checks; those remain outstanding. The published index is unchanged.
