# Plan: threatmodelling (threatmodelling.html), 3 Nov 2026

Belongs to [threatmodelling.html](threatmodelling.html). Other notes for the same page: [decisions](threatmodelling.decisions.md).

Goal (Norwegian): one HTML page that explains threat modeling. Based on the method in six photographed slides (four questions, data flow diagram, STRIDE table, DREAD scoring, ASVS controls, retrospective). Reworded so it does not read as a copy. Improve where it helps. Keep it short and simple. New diagrams and a different case from the slides (the slides use API + consumers + database in Azure). Same look as the other pages in the repo.

## Steps
1. Read the six photos. Done.
2. Pick the new case: a customer portal where customers upload documents. Done.
3. Verify the ASVS 4.0.3 requirement IDs and the STRIDE-per-element table that the page cites. Done.
4. Build threatmodelling.html with the same CSS system as MCP-Risk-Map.html (tokens, fonts, dark mode, 48rem column, sticky nav). Inline SVG diagrams that follow the theme. Done.
5. Render check: light and dark, phone width, no console errors, no em or en dashes, no long paragraphs. Done.
6. Visual pass: replace the card-dashboard look with a printed worksheet look (see decisions). Done.

## Page outline
- Intro and the four questions as a loop (figure 1).
- Step 1: what are we working on (scope, assets, data flow diagram with trust boundaries, figure 2).
- Step 2: what can go wrong (STRIDE, applied per element, figure 3 with markers, threat table).
- Step 3: what do we do about it (likelihood x impact, matrix figure 4, four ways to respond, controls with owner and test).
- Step 4: did we do a good enough job (check, test, repeat when things change).
- Short checklist.
