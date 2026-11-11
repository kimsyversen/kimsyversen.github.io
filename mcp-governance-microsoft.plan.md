Belongs to: [MCP Governance in a Microsoft ecosystem](mcp-governance-microsoft.html)

# Plan: MCP Governance in a Microsoft ecosystem

## Goal

A short, sound design to govern MCP in the Microsoft ecosystem. Make Azure API Management (APIM) the only way to reach a company MCP backend, and limit managed clients to approved MCP addresses.

## Page order (rewritten 2026-11-11, simplified for a skilled audience)

1. The design: lead with the answer, one figure per design (switch), one table "Parts and control planes" (10 rows).
2. Controls: one table by call layer, with the guardrails figure. Released-only content.
3. Rollout and tests: order of work, acceptance tests.
4. Gaps and open questions (open questions 1 to 5).
5. With preview: added controls, approval and denial workflow, guardrails added, tests added, pilot.
6. Footer: Made with AI note, then a link to `mcp-governance-microsoft.factcheck.md`, which holds the 202 source quotes (V1 to V202).

## Released and preview content (rewritten 2026-11-11)

The path switch is gone. The page has no hidden content. Released-only design first, preview in its own section. Rule: a preview-only quote is cited only in With preview (the builder's `ev()` stops the build otherwise). Sources: `~/Downloads/enterprise-mcp-governance-solution.md` and `enterprise-mcp-governance-preview-enabled.md`.

## Policy source and sync (added 2026-11-08)

A Git repository holds the approved and denied MCP servers. A reviewed pull request changes it. On merge a pipeline we build applies the list to Power Platform (Copilot Studio), GitHub managed settings, Foundry, and in the preview design Agent 365. Both figures show repository, pipeline, targets and the clients each target governs, with the limit of each target as status text. The figures are ASCII text files built into the page. Not built or tested. Sources added: pp-block, pp-api, pp-pipe, pp-deny, fy-allowed, gh-deploy (70 quotes at that time, 39 on the safe path; now 84 and 48).

## Rules

- Same look as `enterprise-ai-agent-governance-summary.html` (copied from it by the builder).
- Every product fact has a quote in `scripts/mcp_governance_evidence.py`. Design choices are labelled recommendation. Gaps in the sources are labelled inference or unverified.
- The released-only design needs no preview feature. The With preview section labels every preview feature and keeps the released-only design underneath.
- Paragraphs and cells at most 60 words. No em or en dashes.

## Figures

Edit `mcp-governance-microsoft.figure-safe.txt`, `.figure-preview.txt`, `.figure-approval.txt` or `.figure-guardrails-safe.txt`, then rebuild. `[red]...[/red]` marks red text. Update the reviewed-text ledger in the fact check when wording changes.

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

## Client and backend control labels 2026-11-11
- [x] Both figures distinguish client sign-in from gateway identity and authorization, identify Windows egress as Intune-managed, and say the backend accepts calls only from the gateway.
- [x] Updated accessibility descriptions, fact-check ledger and decisions note.
- [x] Builder, section-anchor, reviewed-label and diff whitespace checks.
- [ ] Quote source check not verified: all 193 fetches failed because source hosts did not resolve. Desktop and narrow browser check not run: local server could not bind and browser blocks local file URLs.

## Gateway preview status 2026-11-11
- [x] Diagram distinguishes supported MCP capabilities in the API Management service from the separate AI Gateway public preview product.
- [x] Diagram and component map clarify preview-only Agent 365 tool controls and tool threat protection; Foundry gateway integration and remote MCP firewall are named as separate preview features.
- [x] Read current primary Microsoft Learn sources for API Management MCP support, AI gateway terminology, AI Gateway, Agent 365 integration and tool threat protection.
- [x] Builder, section-anchor, reviewed-label (208 texts) and whitespace checks passed.
- [ ] Automated quote fetch: all 196 requests failed because source hosts did not resolve. Browser layout check not run: local server cannot bind and browser blocks local file URLs.

## Which gateway 2026-11-11
- [x] Source-checked the AI Gateway integrated with Foundry (6 quotes, V197 to V202, 202 total).
- [x] "Which gateway" table under The design, gap-one-gateway, link from Parts.
- [x] Repaired nine older quotes that no longer matched the live sources.
- Open: test one v2 instance as both Foundry AI Gateway and company MCP gateway. Tenant tests.
- Browser check 2026-11-11 (localhost, built-in browser): Which gateway table shows 3 rows on both paths, heading link present, 0 dead links in it, no sideways page scroll at 1280 px or 375 px, no console errors. Not tried on a real phone or in Safari.

## One-page simplification 2026-11-11
- [x] Source quotes moved to `mcp-governance-microsoft.factcheck.md` (table between the Begin and End source quotes markers, generated by the builder). Quote marks on the page link to it. Old `#ev-V` links redirect there.
- [x] Three design tables merged into "Parts and control planes". Controls and Guardrails are one section. All preview content is in "With preview". Tail sections merged into Rollout and tests, and Gaps and open questions.
- [x] Path switch removed. `?path=preview` still scrolls to With preview. Old ids kept as empty anchors, except `seg-lbl`.
- [x] Page 13,785 words to 8,023 (visible text, nav and footer included), 221 KB to 142 KB.
- [x] Checks: builder, anchor check, label check (200 texts), quote check (202 quotes, 0 problems; the older governance page's check still passes, 88 quotes). `check-evidence-quotes.py` now checks the factcheck.md table when it has the markers.
- [x] Browser check (localhost, built-in browser): no sideways scroll at desktop and 375 px, no console errors, 0 dead in-page links, every h2 and h3 has an id and link, `#preview` and `#controls` jump correctly.
- [ ] Not checked: the `#ev-V` redirect and the quote links (they point to the GitHub copy of the fact check on master, so they work only after the owner publishes master; anchor behavior on GitHub not tested). Not tried on a real phone or in Safari.

## One table by call layer 2026-11-11
- [x] The Controls table (by design requirement) and the "What each guardrail does" table (by layer) are one table, "Controls by call layer": 30 rows under 9 group rows (Whole path, layers 1 to 8). Columns: Control, Applies to, Design requirement, What Microsoft and GitHub document. The Label column is gone; the recommendation tag sits in the requirement cell.
- [x] Merged: Data policy into Policy sync, Power Platform; Tool list into Policy sync, Foundry; Allow and deny lists into Client allowlist. The Foundry toolbox network text moved to a new anchor, `ctrl-foundry-network`, at layer 5. The Microsoft 365 Copilot note became a Write approval row at layer 3.
- [x] Old ids kept: `guardrails`, `h-guardrails`, `what-each-guardrail-does` are empty anchors. All `ctrl-*` anchors work.
- [x] Checks: builder, anchor check, label check (199 texts), quote check (202, 0 problems), no dashes, no lost id except the ones removed earlier, 0 dead links. Browser (localhost): no sideways scroll at 1280 and 375 px, no console errors.
- [ ] Not checked on a real phone or in Safari. The `#ev-V` links still go to the GitHub copy on master.

## 2026-11-11: show what preview adds

Done: the With preview figure is now the released design with the preview additions shaded (underlined and tinted, so it does not rely on color). Added items: Global Secure Access MCP firewall, AI Gateway (separate product, public preview, Agent 365 tool block, tool threat protection), Agent 365 admin view, BYO server route box. A legend sits under the figure.
Open: nothing drawn for Foundry gateway routing or the Defender checks (legend points to the tables). Not tried on a real phone or in Safari.

## 2026-11-11: cut obvious statements

Done: removed sentences that only restated the section, the heading or another line (listed in decisions). Left in place: scope notes, legends for the unverified and inference tags, and every caveat.

## 2026-11-11: both designs at the top

Done: "Select design: Released only | With preview" is back in the contents bar. It switches the figure and the Scope line in The design. The preview figure moved from the With preview section to the top; that section links to it. The shared link `?path=preview` selects the preview design again.
Open: the switch changes only The design. Controls, Rollout and Gaps are not filtered by it. Not tried on a real phone or in Safari.

## 2026-11-11: simplify for a skilled audience

Owner's ask: simplify, keep the essentials, readers are skilled. Fact check off the page (link under the Made with AI note). No open questions for the preview.

- [x] Fact check section removed. Link in the footer. `#evidence` kept as an anchor there.
- [x] Open questions for the preview removed. Ids kept as empty anchors.
- [x] "Start by role" links removed (the contents bar does the same job).
- [x] "Where each control applies" and "Where the preview controls apply" removed. The Applies to column already says it. The cloud agent firewall fact moves to Gaps.
- [x] "Approval boundaries and cross-cutting guardrails" removed. Every fact in it is already in the controls table. The one new rule (re-review on change) moves to the Approved inventory row.
- [x] Parts table: MCP clients row removed.
- [x] Tests: Result column removed, one line says none have run. Preview Label column removed.
- [x] Preview: Fallback removed, pilot cut to the steps that are specific to the preview.
- [x] Checks: builder, anchors, labels, dashes, dead links, browser at desktop and 375 px.
- Browser check (localhost, built-in browser, dark theme): contents bar has five links, footer shows the fact check link, design switch works, no sideways page scroll at 1024 px (both designs) and 375 px, no console errors. Old anchors `#env`, `#evidence` and `#preview-open` scroll to their new places. The jump on page load was seen for `#env` only, and only after the pane got a click (the pane delays smooth scrolling). Not tried on a real phone, in Safari or in light theme. The fact check link points to the GitHub copy on master, so it shows this pass only after publishing.

## 2026-11-11: cut content guardrails

- [x] Remove old layers 1 and 8, Agent over model and Content moderation from the controls table
- [x] Redraw the guardrails figure with six layers and renumber every layer reference
- [x] Move the Copilot Studio prompt attack block to tool response
- [x] Update the ledger, fact check and decisions

## 2026-11-11: remove open questions

- [x] Remove the Open questions block, rename the section Gaps, update the ledger and notes
