# Plan: fact-check of the Developer Workstation Risk Map (Developer-WS.html), 1 Nov 2026

Belongs to [Developer-WS.html](Developer-WS.html), named `Developer Workstation Risk Map.html` when this work was done. Other notes for the same page: [decisions](Developer-WS.decisions.md), [fact-check ledger](Developer-WS.factcheck.md).

Goal: check every statement, fix wrong ones, keep statements short so they age well. Report what was wrong and how it changed.

Working notes (repo is a public GitHub Pages site).

## Where the text lives
- HTML body: header, In short, diagram caption, Before you use the map, Top 10 intro, Current box, status definitions, D01 to D10 cards, response section, Review tab, Sources intro, footer.
- Script data: MORE (D11 to D17), PERSONAS, EVIDENCE, SOURCES, START (first controls), ZONES/COMP/ARROWS (diagram labels), PLACE (per-box risk notes), SHORT (D11 to D17 one-liners).

## Steps
1. Re-run the git claims locally (fsmonitor override, env override, -c, clone vs copied folder).
2. Verify claims per source batch: npm 12; GitSpawn; Plugin4Shell; package firewall; ChainDrop; s1ngularity; Amazon Q; GlassWorm; sandbox docs (Claude Code, VS Code, Codex); VS Code policies; Claude Code settings; Codex managed config; GitHub Copilot managed settings; MCP spec; Defender schema; GhostApproval; CVEs; Forever Security; Gen Digital; Mitiga; ClawHavoc; tunnels (Unit 42, SentinelLabs, Dev Tunnels); OWASP lists; source dates.
3. Fix wrong statements; shorten fragile ones.
4. Check the page renders (no script errors, tabs work).
5. Summary of corrections.
6. Claim-by-claim ledger: Developer-WS.factcheck.md lists every statement (965 rows after pass 9) with its source, verdict and the pass that changed it. Done 1 Nov.
7. Final checks after the last edit (pass 9): data arrays parse, no em or en dashes, render with 62 sources, tabs and map popover. Done 1 Nov.
8. Pass 9: no paragraph, list item, table cell or caption row over 60 words, measured on the source and on the rendered page. Done 1 Nov.
