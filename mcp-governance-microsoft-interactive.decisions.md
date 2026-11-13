Belongs to: [MCP governance in a Microsoft ecosystem, interactive](mcp-governance-microsoft-interactive.html)

# Decisions

## 2026-11-12, new page instead of editing the old one

- **Chose** a new file, `mcp-governance-microsoft-interactive.html`, over rewriting `mcp-governance-microsoft.html`. **Why:** the old page is published and linked; the request was a whole new page.
- **Chose** a hand-built SVG that the builder writes, with a small script that only adds selection and filters. **Why:** the page then reads without script, and the detail panels hold the text. The AKS page builds its SVG in the browser instead.
- **Chose** one detail panel under the diagram over a floating popover. **Why:** the control text is long, and a panel works at phone width.
- **Chose** lanes by client product (GitHub Copilot and VS Code, Copilot Studio, Foundry, Microsoft 365 Copilot), each with its policy target on the left. **Why:** each target governs exactly one client, which the old figure also showed.
- **Chose** to home each control on one box. Controls that the old table listed for "all clients" sit on the box that carries them: Gateway and Identity on the gateway, Approved inventory on the Git box, Logging and checks on its own box. **Why:** one authoritative home per fact.
- **Corrected** the scope of the device controls. The old figure showed three clients passing the client controls box. This page puts the Windows outbound limits on the managed Windows device that runs VS Code and GitHub Copilot, and the remote MCP URL allowlist on VS Code and GitHub Copilot, as the old controls table said. Copilot Studio and Foundry agents run in the cloud, so a device rule does not see their calls. Interpretation by AI, not tested.
- **Dropped** the static ASCII figures for this page. **Why:** the figures are interactive and the box panels hold the same text. The old page keeps its ASCII files.
- **Kept** the Defender product guardrails together on one box (Defender), and Defender on the Agent 365 path on the Agent 365 box, with a link between them.

## 2026-11-12, build

- Defender: all three Defender controls sit on the Defender box. This supersedes the earlier note to keep the Agent 365 Defender text on the Agent 365 box. Reason: one home per control, and the three share scope and layers.
- Builder reuses the first page's builder text (control rows, parts, gaps, rollout, preview tests, pilot) so wording and quotes stay identical. Only the layout is new.
- Hash links now scroll instantly and run again on load. Smooth scrolling lost the jump when a hidden panel had to be opened first.
- Boxes with a different gateway name or control count between designs show both variants and switch with the view.

## 2026-11-12, redesign for portrait and color

- **Superseded** "a hand-built SVG that the builder writes" and "one detail panel under the diagram". **Now:** the map is a CSS grid of boxes, and a script draws the lines into one SVG layer from the box positions. On wide screens the panel sits beside the map; on phones it sits below. **Why:** the 1226 px SVG forced sideways scrolling in portrait. The grid reflows at every width.
- **Chose** boxes as links (`#n-<id>`) over buttons. **Why:** each box is then shareable, and the page reads as a list of links without script.
- **Accepted** that the lines need script. Without it the boxes still read top to bottom in order, and the panels hold the full text.
- **Chose** color by meaning: amber for the approved list and the policy plane, blue for calls to the company server, red for blocked or preview routes, grey dotted for logging. Hatched boxes are preview. **Why:** a color per step would carry no information.
- **Chose** solid lines that stay solid when lit (thicker only), and dashed lines that animate. **Why:** turning a solid line dashed changed its meaning in the key. Animation stops under reduced motion.
- **Chose** a neutral grey rule above the panel body, not the node color. **Why:** colored bars on card tops read as a template.
- **Dropped** the separate node list. **Why:** the boxes are the list, and Previous and Next step through the panels.
- **Added** Follow a path chips (one per client, the preview route and the blocked direct call) and per-box filter counts ("k of n match").

## 2026-11-12, compact header

The page now uses a smaller title and less space above the contents bar and the first section, like the AKS page. Reason: on a laptop screen the large title filled the first screen and pushed the paths and the map below the fold. On a laptop, the path chips and filters now show on the first screen. The section anchors, the sticky bar and the view switch are unchanged.

## 2026-11-12, filters folded on phones

On screens 640px wide or less, the objective and call-layer filters start closed under "Filter by objective or call layer". Reason: on a phone the open filters took about 470px between the path chips and the map. Closed, the map follows the path chips. The fold shows how many filters are on, and the result line under it stays visible. On wider screens the fold starts open. Without script the fold stays open.

The filter result line also names layer gaps when layer 3 or 6 is selected. The first page states those gaps in its guardrails figure, and this page has no such figure.

## 2026-11-12, estimated layers marked on the page

The preview controls whose layer the first page does not give now read "layer 4, AI estimate" in their panel heading. Reason: the site rule is to label interpretation by AI where the reader sees it, not only in the fact check. The layer filter still includes them, so a layer 4 filter shows every gateway-side preview control.

## 2026-11-12, Purview audit control

Added "Purview audit of agent tool calls" on the Logging and checks box. Reason: the owner noted Purview was missing. Purview records agent-to-tools interactions for Agent 365 agents, which is the only released Purview feature found that touches tool calls. DLP was left out as a control because Purview DLP for Agent 365 does not list tool calls; the panel states that limit instead.

Its six quotes live in this page's builder, numbered V203 to V208 (V208 is the Foundry audit quote) after the shared list. Reason: the first page and its committed quote list stay unchanged. Cost: the shared quote checker does not recheck them, so the fact check says to recheck by hand.

The box is now titled "Logging, checks and Purview", not a Purview box of its own. Reason: it also holds the shared logging control (gateway logs, device telemetry, list review, acceptance tests), so "Purview" alone would hide those. A separate box would need a new grid slot for one control. The id `n-log` stays, so old links work.

## 2026-11-12, layer gaps on the client boxes

The Foundry agents and Copilot Studio boxes now say which layers have no released guardrail. Reason: before this, the gaps showed only in the filter result when layer 3 or 6 was selected, so a reader who never filtered missed a fact the first page states in its controls table. The filter line stays, because it answers the filter the reader chose.

## 2026-11-12, intro labels in their own column

The In short, Scope, Objectives and Baseline labels now sit in a small caps column beside their text on wide screens, and above it on phones, with more line height and space between lines. Reason: the owner found the labels ran into the text and were hard to read.

## 2026-11-12, ways to build the gateway as options

The Gateway panel opens with one sentence saying there are two ways to build the gateway (three in With preview), then one section per way: Option 1 API Management with AI gateway capabilities, Option 2 AI Gateway integrated with Foundry, Option 3 dedicated AI Gateway (preview, With preview only). Reason: the panel listed two and left out the dedicated resource, the Foundry entry did not say that routing MCP tools through it is preview, and a table of the same facts scrolled sideways inside the panel and repeated the sections below it. The resource type column was dropped with the table; the AI Gateway product and resource control still states it. The SKU of the dedicated resource is stated as not found because no source read names it.

## 2026-11-12, logic and consistency audit

Edited the page file directly; the builder script was behind the page at the time. Superseded below: the builder now reproduces the page. Fixes:

- The figure description said a pipeline writes to four targets, one "set by hand". Now three by pipeline, the Microsoft 365 admin center by hand, as the Sync pipeline box and the path notes already said.
- With preview said AI Gateway replaces the API Management gateway, yet the Agent 365 integration, the server-block test and the pilot all use API Management v2. Now AI Gateway is an option that can replace it, and the Agent 365 integration is the addition. The single-tool block test now names the AI Gateway product, the only gateway with tool blocking (V42).
- "Untrusted results" was tagged as a layer 6 product guardrail while the Foundry box says no released guardrail covers layer 6. It is advice, so it is now labelled guidance. The control count is unchanged.
- Result review: V154 describes granting post-approval (no review), not post-approval as a check. Reworded.
- Agent 365 BYO tool level: "authorize at the gateway" contradicted a route that skips the gateway. Now "at the server".
- Policy sync, Foundry: added that a tool list does not stop a developer adding another server, matching the Foundry network box.
- Acceptance tests: the merge and hand-edit tests now name pipeline targets only, since the Microsoft 365 admin center is changed by hand.
- Tag key: the unverified row claimed the tag marks names from a control plane list; it is also used for untested behavior. Now "Not confirmed in a quoted source."
- Smaller: "covers them" in the first gap; the Defender for Endpoint row no longer points at "rules above".
- Second pass, claim by claim against the cited quotes: the request queue sentence now cites V182 (Requests tab), not V181 (Registry tab). The cloud agent gap sentence "Only the client allowlist applies" is not in V23, so it is tagged inference. The backend lock step says "frontend private endpoints", matching V47. The fact check rows for V102 and V103 say preview, as the quotes do. The label ledger was repaired (4 stale rows removed, 6 added).

## Builder reconciled with the page (2026-11-12)

- **Chose** to make `scripts/build-mcp-governance-interactive.py` reproduce the hand-edited page again. **Why:** a rebuild had been silently undoing the 2026-11-12 fixes (title, tag key, wording).
- Title, heading, footer with the tag key, and the tag key and Control label styles now live in the builder source.
- The wording edits made by hand to shared content are listed in `scripts/mcp_governance_interactive_edits.py` and applied after the page is built. Each must match exactly once or the build stops. **Why:** that text comes from the first page's builder, which this page must not change. Move an edit into the source when its wording is next touched.
- V102 and V103 are labelled Preview in their source, so the quote table now marks them preview and the header counts are 132 released and 76 preview (the committed table already marked them preview but still said 134 and 74).
- **Removed** the Rollout "Goal" sentence ("API Management alone does not guarantee objectives A and B") and the closing note under the design panels ("Agent approval and lifecycle are separate from this page's MCP server workflow"). **Why:** the owner found them wrong or unneeded. The first page keeps them.

## Second logic audit (2026-11-12)

- **Superseded** the gateway lead in "ways to build the gateway as options" ("Choose one to front the company MCP server"). **Now:** Option 1 fronts the server, Option 3 (preview) can replace it, and Option 2 is the gateway Foundry uses for its model deployments, which can be the same instance. **Why:** Option 2's own text says it is not used for MCP tools in the released design (V60), so it was not a choice for fronting the server. The two and three options structure stays.
- **Added** a new gap, `gap-foundry-prompt-agents`, instead of a new control. **Why:** V101 says the Foundry Network control does not affect prompt agents outside the Copilot harness, and no released control found closes that. The Foundry policy sync sentence links to it.
- **Chose** to fix "7 Later deny" in the builder source and the shared wording through edit pairs, as before. **Why:** the first page must not change.
- **Kept** the acceptance test order. **Why:** the threat model cites acceptance test 12 by number.
- **Left** the device "Managed URL policies" wording as is. The VS Code allowlist set through Intune is a device policy that the pipeline does not write; whether it conflicts with the GitHub managed settings file was not checked, and the page does not claim either way.

## Holistic review (2026-11-12)

- Supersedes the earlier baseline placement of Foundry's Network guardrail: it is preview. Keep released toolbox networking and preview guardrails separate, preserving the original anchor and adding `ctrl-foundry-egress`.
- Supersedes direct Agent 365 BYO access to the private backend. Retain the public path/node IDs as an excluded alternative, with a rejected line. Gateway-fronted composition needs its own compatibility test.
- Use manual Power Platform MCP policy until the actual API adapter is verified; Git review and policy sync do not imply interchangeable policy targets.
- Preserve the shared original page. Isolate interactive evidence and review corrections in two small modules, with exact-match checks so rebuilds cannot silently undo the corrections. V195 remains an explicitly unverified historical anchor, unused by current claims. **Superseded** 2026-11-12 below.

- Require Power Platform mixed mode while classic policies protect connector types unsupported by ACP; ACP-only mode would discard those protections.
- Document preview tool threat protection's discovery/session exclusions and avoid automatic retries after a result is withheld; neither post-call inspection nor a successful HTTP response proves a write did not execute.

- Qualify ACP inclusion in the released-only deployment by workload-specific general availability (V216); keep classic connector policies until coverage is established. Do not present unrun acceptance tests as guarantees.

## Second holistic review (2026-11-12)

- **Restored** V195 as a verified quote and cited it wherever the page calls AI Gateway a separate product. **Why:** its source was reachable on 2026-11-12, and V196 alone describes the built-in API Management capabilities, not the separate product.
- **Kept** "separate AI Gateway product" wording even though Agent 365 pages call it "the AI Gateway tier in Azure API Management". **Why:** the overview (V195) and the resource type change (V45) are the primary sources for what it is; the Agent 365 pages name it but do not describe its resource.
- **Split** the Microsoft 365 and Power Platform manual steps in the order of work. **Why:** Microsoft 365 agent access has no API option (V171), so it is manual by design, while Power Platform is manual only until its API path is verified.

- 2026-11-12: removed "This is a proposed architecture. Neither objective is proven in a tenant." from the lead and relabelled the line Coverage. The owner asked for no blanket untested disclaimers on design pages; test status stays on the tests and on single gap items.
- ~~2026-11-12: removed the Approval lock's `unverified` tag through the review module, not the shared builder.~~ Superseded the same day: the owner approved fixing the first page, so the tag is now removed in the shared builder and the review-module replacement is gone.

- 2026-11-13: the cloud agent gap now names the built-in Playwright server as the one MCP server the firewall covers, because the source changed. **Why:** the old sentence said the firewall does not filter MCP server processes, which is now too broad. The page-only evidence module overrides V23 and V176 so the first page and the shared module stay as they were.
