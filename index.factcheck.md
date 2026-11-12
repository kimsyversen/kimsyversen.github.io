Belongs to [index.html](index.html).

# Fact check: site index

Checked 5 November 2026 for the index redesign. This checks the index against this repository's primary records. It does not repeat the underlying pages' technical fact checks or test their advice on real systems. The redesign introduces no new technical claims.

| Index statement | Primary record inspected on 5 Nov 2026 | Verdict |
| --- | --- | --- |
| Five pages, newest first | The five existing page links and stable IDs in the pre-change index; the five content HTML files in the repository | OK. The count and existing order are preserved. Newest refers to page addition order, not each page's most recent update. |
| Security guides, risk maps and reference designs, each on a single page | The five linked HTML pages | OK. Describes the local collection. |
| GitHub summary: two enterprises, three policy layers, shared operations and clickable boxes | `github/github-two-enterprise-interactive.html`; `github/design-notes.md`, introduction and sections 3, 5 and 7 | OK. Matches the reference design. The notes state that names are illustrative and document the documentation review. |
| Two editable draw.io versions, three pages and one page | Both linked `.drawio` files; `github/design-notes.md`, introduction | OK. Local files exist; their diagram counts match the labels. |
| Threat modeling: four questions, a drawing and fixes on a fictional claims portal | `threatmodelling.html`, introduction and four-question section | OK. The summary is unchanged. |
| Threat modeling checked in three passes | `threatmodelling.factcheck.md`, initial check, second pass and third pass sections | OK. Describes the recorded review; does not claim testing on a live system. |
| MCP summary and check note | `MCP-Risk-Map.html`; `MCP-Risk-Map.factcheck.md` | OK. Matches the page and its recorded source comparison. The existing statement that nothing was tested on a real system remains. |
| Workstation summary: ten risks involving editors, Git and AI agents | `Developer-WS.html`, introduction and risk list | OK. A summary of the page's prioritisation, not a new comparative security claim. |
| 965 statements checked, 35 fixed and 18 cut | `Developer-WS.factcheck.md`, What was found | OK. Matches the recorded totals. |
| AKS summary and documentation-only check limit | `AKS-sikkerhetsvurdering.html`, introduction, risk list, review and testing limits | OK. The existing statement that no cluster was examined remains. |
| Individual page update dates | Pre-change `index.html`; `index.decisions.md`, distinction between content updates and factual review dates | PRESERVED. This style change does not advance content or fact-check dates on those pages. |
| Last updated 5 Nov 2026 | Date of this index edit | OK. Same calendar date as the previous revision; now marked up as a semantic date. |
| Made with AI disclosure | Exact disclosure in the pre-change index and the site's shared wording | OK. Text is unchanged. |

## Design verification

- Browser inspection: desktop and 375px in light and dark palettes, plus intermediate and smaller widths. No horizontal document overflow in the inspected layouts.
- The browser does not expose colour-scheme emulation. Dark-palette inspection used a temporary local copy with the production dark media condition activated. The copy was removed; system preferences were not changed.
- Native footnote, browse and return anchors, keyboard focus and separate download hit areas checked in the browser. Local destinations and fragment IDs checked from the HTML.
- Body text, muted text and navigation colour pairs meet 4.5:1 contrast in both palettes. Paragraphs stay below 60 words.
- Console errors checked in the preview. No JavaScript was added. This repository has no build step.
- Not tested: physical mobile devices, print output, a screen reader, every browser engine or live infrastructure described by the content pages. External font delivery remains dependent on Google Fonts, with local serif and sans-serif fallbacks.

## Entry 08 check, 6 Nov 2026

| Text | Source | Verdict |
|---|---|---|
| "Intune and MCP" entry description | `Developer-WS2.html` and its own fact check | OK. Describes the page. Says every claim links to an exact quote, which that page does for its 70 quotes. |
| Updated 6 Nov 2026 | Page content date | OK. |
| 08 pages | Count of list items | OK. |

- Both index checks from `AGENTS.md` (missing pages, broken links) print nothing.
- Entry 08 inspected in the browser on 6 Nov 2026: desktop light, and 375px in dark mode (scroll width 375, no sideways scroll, drawing and text readable).
- Not tested: entry 08 at 375px in light mode, a screen reader, physical devices.

- Entry 09 description, checked 8 Nov 2026 against `mcp-governance-microsoft.html` and its fact check: it says "proposed" because the design is untested, and every product claim on that page does link to an exact quote (91 quotes).

## Entry 12 review, 12 Nov 2026

The revised MCP STRIDE description matches `mcp-governance-stride.html` and its row-by-row fact check: reviewed conditional scenarios, public evidence, explicit model limits, estimated DREAD scores and related controls. Entry number, URL and same-day content/footer dates are preserved. Link destinations are checked locally; browser rendering was blocked by the environment's URL policy in this session.
