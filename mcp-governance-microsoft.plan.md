Belongs to: [MCP Governance in a Microsoft ecosystem](mcp-governance-microsoft.html)

# Plan: MCP Governance in a Microsoft ecosystem

## Goal

A short, sound design to govern MCP in the Microsoft ecosystem. Make Azure API Management (APIM) the only way to reach a company MCP backend, and limit managed clients to approved MCP addresses.

## Page order

1. (Removed 2026-11-08, now the "In short" line in The design.) The answer. Two objectives: A (every request to a company backend passes APIM) and B (no AI client talks to an MCP server outside APIM).
2. The design. One diagram: clients, client and network controls, APIM, private backend.
3. Four controls: backend isolation, identity, client allowlist, outbound limits.
4. What works in each environment (seven rows).
5. Acceptance tests (target outcomes, none run).
6. Known gaps and what has not been tested.
7. Open questions.
8. Evidence: exact quotes with links.

## Two paths (added 2026-11-08)

Safe choice (default) and preview-enabled choice (safe plus Agent 365, Azure AI Gateway, tool threat protection). Added sections: Choose a path, Order of work, Fallback (preview only). Preview-only blocks carry class `opt-preview`, safe-only blocks `opt-safe`. Sources: `~/Downloads/enterprise-mcp-governance-solution.md` and `enterprise-mcp-governance-preview-enabled.md`.

## Policy source and sync (added 2026-11-08)

A Git repository holds the approved and denied MCP servers. A reviewed pull request changes it. On merge a pipeline we build applies the list to Power Platform (Copilot Studio), GitHub managed settings, Foundry, and on the preview path Agent 365. Both figures show repository, pipeline, targets and the clients each target governs, with the limit of each target as status text. The figures are ASCII text files built into the page. Not built or tested. Sources added: pp-block, pp-api, pp-pipe, pp-deny, fy-allowed, gh-deploy (70 quotes at that time, 39 on the safe path; now 84 and 48).

## Rules

- Same look as `enterprise-ai-agent-governance-summary.html` (copied from it by the builder).
- Every product fact has a quote in `scripts/mcp_governance_evidence.py`. Design choices are labelled recommendation. Gaps in the sources are labelled inference or unverified.
- The safe path needs no preview feature. The preview path labels every preview feature and keeps the safe design underneath.
- Paragraphs and cells at most 60 words. No em or en dashes.

## Figures

Edit `mcp-governance-microsoft.figure-safe.txt` or `.figure-preview.txt`, then rebuild. `[red]...[/red]` marks red text. Update the reviewed-text ledger in the fact check when wording changes.

## Build

```bash
python3 -I scripts/build-mcp-governance.py
python3 -I scripts/check-evidence-quotes.py <cache-dir> mcp_governance_evidence mcp-governance-microsoft.html
python3 -I scripts/check-enterprise-agent-labels.py mcp-governance-microsoft.html
```

## Steps

- [x] Collect and verify quotes
- [x] Build page
- [x] Write notes and ledger
- [x] Merge both markdown files and add the path selector
- [x] Browser check both paths: light, 375px, console
- [x] Moved out of `wip/` and listed in the index as entry 09 (2026-11-08)

- Parts table added 2026-11-08 under The design (20 rows, released and with preview). Preview gateway box in the figure aligned with the table (done).
- Follow-up pass 2026-11-08: lead, Objectives and Designs lines, wording (path, Evidence), fact check column widths, headings, new open question 1, phone sticky switch. Done and checked.
- Claim check 2026-11-08 (second pass): every claim re-read against its source context, 8 quotes added (84 total), wording trimmed where it overstated a source. See the fact check.
- Live verification 2026-11-08 (third pass): 90 of 91 quotes matched live, V80 read in a browser, 22 of 22 dates matched, V91 added, ledger repaired. See the fact check.
