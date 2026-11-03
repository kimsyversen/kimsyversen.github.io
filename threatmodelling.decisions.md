# Decisions: threatmodelling (threatmodelling.html)

Belongs to [threatmodelling.html](threatmodelling.html). Plan: [threatmodelling.plan.md](threatmodelling.plan.md).

## 3 Nov 2026

- **Case: customer portal with document upload.** The slides use an API with consumers and a database in Azure. A portal with an external login and a document store gives the same shapes (entity, process, store, flows, one trust boundary) in a different setting.
- **Likelihood x impact (1 to 5 each) instead of DREAD.** DREAD has five scores that are hard to set consistently. Two numbers give 1 to 25 and fit a matrix. DREAD is kept as a collapsed note in step 3 C so readers of the slides can see why it was dropped.
- **Bands: high 15 or more, middle 8 to 14, low 7 or less.** Simple cut-offs, each tied to an action (fix before launch, plan, accept or watch).
- **STRIDE per element.** The page applies STRIDE per element type (entity: S R, process: all six, store: T I D, flow: T I D) instead of asking all six everywhere. It cuts the work and the table shows which letters apply where.
- **Four ways to respond: Fjern, Reduser, Flytt, Godta.** The slides only show controls. Naming the choice makes "accept" a visible decision.
- **Every control gets an owner and a test.** Added to the slides' method so step 4 can check that controls work.
- **Threat E handled with "Fjern", threat R with "Godta".** Gives the response cards a real example each, and shows residual risk (I goes from 20 to 5).
- **ASVS IDs checked against v4.0.3** on GitHub on 3 Nov 2026. The sources section names the version so the IDs stay valid.
- **Inline SVG instead of raster images.** Follows light and dark mode through CSS variables, scales on a phone, and the figures are clickable (shared `data-t` highlights the threat row).
- **Case and numbers are fictional.** The footer says so.
- **No storage and no keys.** The page is static. The click highlight lives only in memory.
- **File name and style follow the other pages.** `threatmodelling.html` in the repo root, same CSS tokens, fonts, 48rem column and sticky tab bar as MCP-Risk-Map.html.
- **Not committed.** Left for the user.

## 3 Nov 2026, redesign

- **English, one sheet.** The user asked for English and no separate sections. The page is now a single board of panels with no tab bar and no section headings in a long column. The four questions sit at the top as a strip, and each panel carries the number of the step it belongs to.
- **Merged the two data flow figures.** One diagram now shows the drawing and the threat markers together. Clicking a letter highlights the same threat in the register and the matrix.
- **One register instead of two tables.** The threat table and the score table are merged: threat sentence, likelihood, impact, score, response and first control.
- **Step colors.** Blue, red, amber and green for steps 1 to 4, with dark mode variants, so panels map to steps at a glance.
- **Case renamed to "claims portal"** (was "skadeportalen"). Same threats, scores and ASVS IDs as before.
- **Four responses renamed Remove, Reduce, Move, Accept**, each with an example from the case.
- **Wider layout (1200px)** instead of the 48rem reading column, because everything has to fit on one board. Fonts and color tokens still match the other pages.

## 3 Nov 2026, visual pass ("not AI generated")

- **Printed worksheet look instead of a card dashboard.** The user said the page looked generated, pointing at the colored line on top of the four question boxes. Dropped every template tell: colored top bars, rounded cards with soft shadows, the gradient and grid hero, pill chips, number badges, mono uppercase eyebrows and tinted callout boxes.
- **Paper, ink and one red.** Warm paper background, near-black ink, and red only for threats (STRIDE letters, markers, high scores, trust boundary). The four step colors are gone; panels say "Question 2" in plain text instead.
- **Structure from rules, not boxes.** Heavy rule on top of the masthead, ink rule above each panel, hairlines between columns. Tables use booktabs style (thick top and bottom, thin inside).
- **Loop drawn as a bracket.** A line under the four questions runs from 4 back to an arrow under 1. On phones it falls back to a text line.
- **STRIDE per element as a dot matrix** instead of letter pills, with an open dot for "only if it is a log".
- **Risk matrix in a red ramp** (paper, light red, red) instead of green, amber and red.
- **Score shown as a number plus a thin bar** out of 25.
- **Fonts unchanged** (Archivo, Public Sans, IBM Plex Mono) so the page still matches the other guides.
- Checked at 1280px light and dark, and at 375px (no sideways scroll). No console errors. Click highlight still links diagram, register and matrix.

## 3 Nov 2026, rename

- **File renamed to `threatmodelling.html`** at the user's request, since the page is now in English. The plan and decisions notes were renamed to match. No other page linked to the old name.
