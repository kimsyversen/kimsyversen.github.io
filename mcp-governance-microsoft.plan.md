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
- Built-in GitHub server check 2026-11-09: gap and open question 5 reworded, 5 quotes added (96 total). Still open: test the MCP servers in Copilot policy and Registry only against the built-in server in a pilot enterprise.
- Guardrails by layer 2026-11-11: new last section with a flow figure per path and a 16-row table, Defender and Agent 365 runtime protection included (preview path), 33 quotes added (130 total), all matched. Fact check moved below it, collapsed by default. All 53 ledger texts for the section reviewed by hand, which fixed four unsupported claims and the layer 5 header. Browser check: see below. Still open: tenant tests, guardrail gaps marked none found, Agent 365 preview label is interpretation by AI.
- Browser check 2026-11-11 (final): built-in browser on the file. Released only: 14 table rows. With preview: 16 rows, Defender line in the flow figure. Fact check is last and collapsed on load, opens on a quote link and on a `#ev-V121` hash. No sideways page scroll at 375px or desktop. Only console error came from the test script itself.
- Browser check 2026-11-11 (rerun after the hand review, over localhost because the file preview drops the hash): Fact check is closed on load with no hash. Open on load for `#ev-V129` (safe path) and for `?path=preview#ev-V121` and `#ev-V125` (preview path, desktop and 375px, row scrolled into view). Opens on a quote link click. 14 table rows released only, 16 with preview. Figure box lines all 96 wide, layer 5 shows Foundry only lines. No sideways scroll at 375px, no console errors. A plain reload at 375px keeps the earlier scroll position instead of jumping to the hash, which is browser behaviour.

## Browser check 2026-11-11, quote links on load (third check)
- Localhost server, 131 `#ev-V` links, both paths, 986 px and 375 px, loaded in iframes: 524 of 524 had the Fact check open, the row visible, the row in view and no sideways scroll (after the fix to the jump; before it 0 of 262 were scrolled into view).
- Open: not tried on a real phone or in Safari.

## Guardrails by layer, verification pass 2026-11-11
- [x] Reread every source of the section live. No old statement wrong.
- [x] Added what was missing: 30 quotes (V132 to V161, 161 total), table now 25 rows (20 released only), both figures redrawn with the VS Code column filled.
- [x] Quote check 161 of 161, label check 151 texts, anchor check.
- Open: tenant and device tests. Three unverified items (Copilot Studio ask-before-running for MCP tools, VS Code hooks for MCP calls, default result review). See the fact check.
- Browser check 2026-11-11 (localhost, built-in browser): released only 20 table rows, with preview 25 rows, one figure shown per path, 0 dead quote links in the section. No sideways page scroll at 1280 px or 375 px on both paths. No console errors. Not tried on a real phone or in Safari.

## Control planes 2026-11-11
- [x] Four policy targets by control plane in both figures, Microsoft 365 Copilot as target and client, Agent 365 line in the released-only figure, preview figure boxes aligned.
- [x] Control planes table (7 rows), two Controls rows, 19 quotes (V162 to V180, 180 total).
- [x] Cross-cutting approval boundaries and guardrails: translate the shared inventory into target-specific policies; re-review capability changes; document GitHub and Power Platform coverage limits; enforce identity at the service; verify and audit the path. Existing evidence IDs were rechecked against current primary product documentation on 2026-11-11.
- [x] Quote, label and anchor checks.
- [ ] Browser check at desktop and 375 px for this pass. Not done.
- Open: tenant tests. Unverified items are listed in the fact check.

## Agent inventory and approval workflow 2026-11-11
- [x] Show separate all-agent inventory, MCP Tools registry status and Requests (preview) views in the preview design.
- [x] Add a reviewed Git decision followed by the separate Agent 365 BYO server request, Entra consent, and approve/reject/revoke steps.
- [x] Add source quotes V181 to V193 and update the page fact check and decisions note.
- [x] Builder, section anchors and reviewed-text checks.
- [ ] Browser check at desktop and 375 px. No tenant check; acceptance tests are listed as not run.

## URL allowlist scope 2026-11-11
- [x] Both design figures specify managed VS Code and GitHub Copilot; accessibility descriptions and fact-check ledger updated.
- [x] Builder, section-anchor, reviewed-label and diff whitespace checks passed.
- [ ] Desktop and narrow browser check not run: local server could not bind and browser blocks local file URLs.
