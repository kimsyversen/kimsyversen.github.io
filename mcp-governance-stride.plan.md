# MCP governance STRIDE and DREAD model: plan

Source page: mcp-governance-microsoft-interactive.html (read only, not edited).
Outputs: mcp-governance-stride.drawio (3 pages), .threats.tsv, .dfd.xml.
Rebuild: `python3 -I scripts/build-mcp-stride.py`. Data lives in scripts/mcp_stride_data.py.

## Done
- DFD with 4 external entities, 6 processes, 3 data stores, 5 flows, trust boundaries TB0 to TB7.
- STRIDE per element: 71 applicable cells, each with at least one threat (74 threats after three incident-based rows).
- DREAD score per threat: 14 High, 54 Medium, 6 Low (after the evidence lift).
- Evidence level per threat: 3 exploited, 12 disclosed, 59 theoretical. Links in OBSERVED in scripts/mcp_stride_data.py, checked 2026-11-12.
- SC-500 skill mapping per threat; 7 threats flagged outside SC-500.
- DFD rendered in draw.io; edge routing fixed (explicit waypoints, no edge through a shape).

## Open
- Page requested 2026-11-12: mcp-governance-stride.html, index entry 12.
- No threat is tested in a tenant. All scores are AI estimates.
- draw.io's own render of the final DFD was not seen. Open the .drawio file once to confirm label fit.
- Recheck the OBSERVED links, the CISA KEV file and the 208 source quotes when the model is next used (scripted check, see the fact check).

- 2026-11-12: threat ids renumbered by STRIDE letter (S1, T1 ...); the DFD shows each element's threat ids as chips coloured by DREAD rating (solid = public record); the register drops the SC-500 column. Rendered all 3 pages and checked them.
- 2026-11-12: external entities renamed EE1 to EE4 so they no longer clash with threat ids E1 to E7.

## Page (2026-11-12)
Owner asked for one interactive page: the DFD from the .drawio on top, click a threat for its detail, the DREAD register below.
- Builder: `python3 -I scripts/build-mcp-stride-page.py`. Reads node and boundary geometry and edge routes from page 1 of the .drawio, threat data from scripts/mcp_stride_data.py. Never hand edit the html.
- Diagram: inline SVG, chips are buttons. Selecting a chip opens a detail drawer (DREAD bars, evidence links, basis, page controls). Selecting an element box filters both views to it.
- Filters (STRIDE letter, rating, public record) apply to diagram and register together.
- Register: sortable table, row opens the same drawer. Deep link: #t-<id>.
- Checks: section_anchors --check, desktop and 375 px width, no sideways page scroll, no console errors, keyboard open and close.
