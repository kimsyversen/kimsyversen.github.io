Belongs to [MCP-Risk-Map.html](MCP-Risk-Map.html). Other notes for the same page: [decisions](MCP-Risk-Map.decisions.md), [fact check](MCP-Risk-Map.factcheck.md).

# Plan: MCP risk map (MCP-Risk-Map.html), 2 Nov 2026

Goal (from /goal, Norwegian): a new page based on Developer-WS.html that covers only MCP and its risks, with the same kind of risk diagram. Every statement verified and correct. Low detail, because exceptions are acceptable.

Working notes (repo is a public GitHub Pages site).

## Steps
1. Read the template (Developer-WS.html): CSS, tabs, diagram data (ZONES, COMP, ARROWS, PLACE), status tracker. Done.
2. Verify every MCP claim against a primary source on 2 Nov 2026: OWASP MCP Top 10, MCP spec (transports 2025-06-18, security best practices draft), Mitiga, Claude Code managed MCP, Codex requirements.toml, VS Code policies. Done.
3. Write these notes. Done.
4. Build MCP-Risk-Map.html from the template with 8 risks (M01 to M08), each mapped to an OWASP MCP ID.
5. Render check: no console errors, tabs, diagram popover, status tracker, narrow width, no em or en dashes, no paragraph over 60 words.
6. Write the claim ledger (MCP-Risk-Map.factcheck.md).

## Scope rules
- MCP only. Plugin4Shell is about plugin pinning, so it is out.
- Where no MCP incident was verified, the page says so instead of implying one.
- Spec and OWASP statements are labelled draft or beta where the source is.
- Local storage keys use an mcp- prefix so the page does not share state with Developer-WS.html on the same origin.

## 5 November 2026 review

Read all page statements, including generated diagram and evidence text. Reopened primary sources, corrected unsupported generalizations and recorded the current statement ledger. Historical completion claims above describe the earlier review, not independent proof of today's content. Product configuration and exploit reproduction remain untested; browser checks are separate.

## Microsoft scope toggle (8 Nov 2026)

Goal (from /goal): one risk map with a toggle that switches between a general view and a Microsoft ecosystem view. The toggle changes the risks, the diagram, the controls, the start table, the evidence and the sources.

Microsoft ecosystem here means MCP as used through VS Code, Visual Studio, GitHub Copilot, Copilot Studio, Windows, Azure and Microsoft Entra. Third-party servers connected inside these clients still apply.

Steps
1. Research each Microsoft surface against its primary page and copy the exact quote. Done on 8 Nov 2026.
2. Write these notes and the decisions. Done.
3. Add the toggle (segmented control, `data-scope` on `html`, `mcp-scope` in localStorage, `&s=ms` or `&s=g` in the hash). Keep tab ids, risk ids (M01 to M08) and component ids.
4. Make the data per scope: diagram labels, placements, start table, evidence, sources, risk card text, header and "In short".
5. Keep a separate status record per scope (`mcp-status` for General, `mcp-status-ms` for Microsoft).
6. Add the "Other Microsoft surfaces" table under the VS Code tab, each row with a quote and a source link.
7. Show the exact quote and a text-fragment link for each Microsoft diagram placement.
8. Write `scripts/check-mcp-risk-map.py`: fetch every Microsoft source, confirm each quote word for word, and compare the Microsoft presentation text with a reviewed list.
9. Browser test: light, dark, 375px, both scopes, real clicks, saved hash restore.
10. Update the fact check, the index dates and the notes.

Not tested: no setting or command was run on a managed machine. Several Microsoft features are in preview and may change.

## Status, 8 Nov 2026
All ten steps done. The check script passes with 0 problems. Index dates updated. Not committed. Open: a real click on every box under every filter (a sample was clicked, the rest scripted).

## Design principles pass, 8 Nov 2026
Applied AGENTS.md rule 6 to the Microsoft start table and the checks that pointed at preview features or an extra service. See the decisions file.


## 9 November 2026 review completed

Reviewed both views and all generated content against freshly retrieved primary sources. Corrected enforcement exceptions and research scope, added general diagram evidence, and updated the fact-check inventory and index. Quote, layout, JavaScript, link, shared-scope and saved-status checks passed. Product enforcement and exploit reproduction remain outside this documentation review.
