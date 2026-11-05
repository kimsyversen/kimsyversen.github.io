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
