Belongs to: [MCP Governance in a Microsoft ecosystem](mcp-governance-microsoft.html)

# Fact check: MCP Governance in a Microsoft ecosystem

Documentation checked: 2026-11-08.

## Completed statement audit, 2026-11-08

This audit supersedes conflicting conclusions and check counts in the historical entries below. All reader-facing prose, table cells, labels, diagram requirements, acceptance targets and evidence excerpts were reviewed. Product statements were compared with primary-source context; architecture choices remain explicit requirements, and operational results remain untested.

| Scope | Verdict and correction |
| --- | --- |
| Design, figures and objectives | Requirements, not deployed guarantees. Defined A and B in Controls. Qualified the released-only baseline and kept unverified automation out of production. |
| Inventory and pipeline | Proposed implementation. GitHub documents file deployment and roughly hourly propagation (new V90). Acceptance targets now wait for refresh. Power Platform MCP-specific API automation and the Foundry pipeline remain untested. |
| Power Platform | Verified whole MCP server blocking and absence of individual-tool blocking. ACP excludes custom and HTTP connectors; use classic data policies for those. The API tutorial has no MCP-specific example. Manual configuration is the fallback pending verification. |
| Foundry | Verified nonempty allowed_tools behavior; an empty list permits all tools. Removed the unsupported claim that no configuration method is documented. Scoped networking evidence to toolboxes and required separate egress controls. A per-connection tool list is not an enterprise server URL policy. |
| API Management, backend and identity | Verified exposure, JWT/key checks, managed identity, tier limits and Functions networking. Distinguished classic Consumption from Flex Consumption. Backend audience and caller validation are requirements, not an automatic bypass guarantee. |
| Client, cloud and local controls | Verified VS Code policies, GitHub matching and exemptions, Windows outbound limits and stdio subprocess transport. Qualified the cloud firewall statement to direct process filtering. Removed the misleading local-stdio mapping to the remote-only preview filter. |
| Agent 365 and AI Gateway | Verified separate gateway integration and BYO routes, consent scope, supported surfaces, static tool requirement, tier limitations, migration date, regions and networking limitations. Server blocking is runtime enforcement, not merely visibility. Frontend private endpoint limits do not mean private backends are impossible. |
| Threat protection and Foundry routing | Verified user-token requirement, licensing, fail-open/closed modes, server scope and post-call limitations. Tests now require an actual evaluation denial instead of assuming every risky input is detected. Defender mode selection is an implementation requirement based on the same policy article. Verified Foundry creation-time routing limits. |
| Order, fallback and open questions | Recommendations and decisions, not product guarantees. No tenant deployment or acceptance test was performed. |
| Sources and dates | All 90 excerpts matched live primary sources fetched during this audit. All 22 Microsoft Learn dates matched the source footer. Other documentation dates remain unspecified; Microsoft's Ignite blog is dated 2025-11-18. |

The release feed timed out and an encoded retry returned an error response. Replaced V80 with Microsoft's Ignite announcement and V81 with current API Management documentation, retaining their evidence anchors. Existing draft edits were preserved. The page remains in wip and has no published index entry, so no index change is needed.

Validation: page rebuilt with 90 quotes (50 baseline, 40 preview) and no length or anchor warnings. Quote checker: 90 quotes, 0 problems, using sources fetched in this audit. Presentation ledger: 83 distinct texts passed. Static HTML: unique IDs, all 90 evidence anchors, local links, exact Made with AI note and punctuation passed. No CSS or interaction code was changed; no fresh visual browser test or tenant execution was performed. Earlier browser results are historical.

## Method

Each product claim in the page has a quote in `scripts/mcp_governance_evidence.py`. `scripts/check-evidence-quotes.py` fetches each source and confirms the quote appears word for word. The page lists every quote and links it with a text fragment.

## Current claim audit, 2026-11-08

- Reopened the Microsoft Learn sources for Power Platform advanced connector policies, the programmatic policy tutorial, API Management MCP governance, Agent 365 gateway and BYO server routes, Foundry networking and gateway routing, API Management MCP features, GitHub managed settings and firewall, Global Secure Access, Intune firewall policy, Windows Firewall dynamic keywords, Azure Functions networking, and tool threat protection. Reopened the MCP transport specification for the stdio wording.
- Corrected the Power Platform scope. Advanced connector policies support MCP connectors for server-level blocking, but not individual MCP tools (pp-block). Certified connectors are supported; custom and HTTP connector types are not (pp-certified, pp-custom). The previous broad wording that policies cover certified connectors only is superseded because the current page lists MCP connectors separately as supported.
- Replaced V77's quote with the supported-connector table wording, "First-party and certified third-party connectors." The source also has a broader certified-only limitation, but separately lists MCP connectors as supported. This avoids presenting the ambiguous phrase without that context.
- Separated two Agent 365 routes. The API Management integration discovers MCP servers registered with the connected gateway and can block servers and, on supported tiers, tools (pv-disc, pv-a365-ctrl). Its no-auto-routing limit is now scoped to that integration. The BYO route uses developer registration and admin approval, requires a publicly accessible server endpoint, supports four client surfaces during preview, and has BYO tool-level blocking planned for a future release (pv-byo-route, pv-byo-approval, pv-byo-endpoint, pv-byo-surf, pv-byo-tool-plan). The previous wording that treated BYO tool blocking as rolling out for that route is superseded.
- Removed the unsupported idea that the pipeline syncs a fourth server list to Agent 365. The API Management integration discovers gateway registrations; BYO servers use their separate registration flow. The page no longer describes either as a pipeline write.
- Tightened the GitHub cloud firewall statement to its documented scope: it does not directly control MCP server processes (gh-fw). Replaced the stdio inference with the specification's transport description: a client launches a subprocess, and stdio communicates over standard input and standard output (stdio, stdio-io). Client and endpoint controls remain design requirements.
- Clarified that the repository list and pipeline apply Objective B, while backend isolation for Objective A is separate. Described Azure AI Gateway as a separate preview resource type, not a separate product. Preview test steps now name the API Management integration they cover.
- Removed the objective labels and objective summary from The design section and both figures. Moved the repository and pipeline status note from the released-only figure caption to the top of the page, below the lead.
- Reworded the diagrams so their unreferenced text is architecture requirements and labels. Product capability details remain in the tables with evidence IDs.
- V85-V88 were compared with the current Microsoft Learn text; V89 was compared with the current MCP transport specification. The full shell quote checker was attempted but could not fetch pages because this environment could not resolve external hosts. The previous 84-quote, zero-problem run predates the new quotes and V77's changed text.

This audit supersedes the earlier certified-only statement and the earlier description of BYO tool blocking. The API tutorial text was searched in the current fetched page and contains no MCP-specific example; the page now treats API support for MCP policy entries as something to confirm in the tenant.

## Follow-up audit, 2026-11-08

- Compared current source contexts in Microsoft Learn, GitHub Docs, VS Code documentation, Intune documentation, the MCP specification, and Microsoft's release communications with the page wording. Confirmed the currently cited behavior for API Management MCP exposure, tiers, authentication, policy controls and telemetry; Power Platform MCP connector scope; Foundry tool allowlists, network isolation and gateway routing; GitHub managed MCP lists and cloud-agent firewall scope; Agent 365 API Management and BYO routes; AI Gateway preview limits; Windows and Intune outbound filtering; Global Secure Access MCP inspection; and stdio transport.
- The Microsoft Learn Agent 365 integration page currently confirms that v2 tiers support inventory and server blocking, while tool-level blocking, tool telemetry and threat protection are limited to the AI Gateway tier. It also requires a static allowed-tools list for Agent 365 tool-level controls, excludes v1 tiers, and says the integration does not automatically route agents through the gateway. These match the draft.
- The current BYO page says individual-tool blocking is rolling out for supported Agent 365 servers, then explicitly says BYO support is planned for a future release. Expanded V44 to quote both clauses together; the draft's statement that BYO tool blocking is not yet available matches that scope.
- Intune's cited default outbound block is a Windows Firewall setting. Qualified the policy row, control requirement, diagram and open question as Windows-specific. The Global Secure Access preview firewall remains an optional filter for remote MCP traffic.
- Microsoft's AI Gateway overview is reachable from `/azure/api-management/ai-gateway-overview`, which redirects to `/azure/ai-gateway/overview`. Updated the V62 and V76 evidence links to use the reachable route. The article shows a last-updated date of 2026-10-28.
- Changed “The controls table lists all preview limits” to “The controls table lists the preview limits relevant to this design.” The broader “all” claim was unsupported by the table's limited scope.
- Static internal-link check after these edits: 113 IDs, no duplicate IDs, no missing local link targets, and all 89 evidence IDs present. The shell quote checker still cannot fetch source pages due DNS resolution failure. This pass has not yet rechecked every source quote through that checker.

## Mechanical quote check

Historical run on 2026-11-08: 83 quotes, 0 problems (including the check that the built page lists every quote). A later recorded run checked 84 quotes, 0 problems: 48 back the released-only path and 36 back the preview additions. The current page has 89 quotes: 49 back the released-only path and 40 back preview additions. The latest shell rerun could not fetch sources because external DNS lookup failed. V77 and V85-V88 were compared with live Microsoft Learn text; V89 with the live MCP specification. A current static check confirms all 89 quote rows and internal links are present. A successful quote check proves words exist on the source page, not that the claim built on them is right.

## Verdicts

- APIM can validate Entra ID tokens, subscription keys, and sign in to the backend with a managed identity: supported by quotes.
- Backend isolation (access restrictions, private endpoints, no private endpoints on Consumption plan): supported.
- Agent 365 does not route agents through a customer gateway by itself: supported.
- VS Code allow, deny and managed-only policies: supported.
- GitHub allowlist by URL, block of non-matching servers, exemptions for custom agent profiles and the built-in GitHub server, varying coverage: supported.
- GitHub cloud agent firewall does not apply directly to MCP server processes: supported.
- Microsoft says "consider placing it behind" APIM. The page does not claim Microsoft recommends it.
- Foundry: network isolation and private endpoint for the toolbox are sourced. "An agent cannot call arbitrary external MCP servers" is **cut from the page** (no source).
- Copilot Studio: blocking connectors also blocks MCP tools is sourced. A per-URL allowlist is **cut from the page** (no source).
- stdio: the client launches the server as a subprocess; Global Secure Access sees remote servers only: supported. Sandboxing local servers is **cut from the page** (no source).
- Global Secure Access MCP firewall is preview: supported. It is now an optional row on the preview path only.
- Intune outbound default block and its limits: supported. Using it as the second layer is **inference**.
- "Backend still checks the token" is a design requirement. Labelled inference.
- Unmanaged workstation cannot be enforced: **inference**.
- "MCP over HTTPS looks like web traffic": **inference**.

### Preview path (added 2026-11-08)

- Agent 365 API Management integration discovery, server blocking, static tool list, no v1 support, v2 lacks tool-level control: supported by quotes.
- Agent 365 consent role and read/write policy scope: supported.
- AI Gateway resource type change (14 Oct 2026), 15 Jan 2027 deadline, new domain, Bearer header: supported.
- AI Gateway no private endpoints, fixed subnet, no content safety policy, regions during public preview: supported.
- Tool threat protection (user token, no app-only, licence, Audit fails open, Block fails closed, per-server scope, no undo after the call): supported.
- Agent 365 BYO server route (client surfaces, separate Tooling Gateway, admin approval, BYO tool blocking planned for a future release) and Foundry gateway routing for new tools only: supported (pv-byo-route, pv-byo-approval, pv-byo-surf, pv-byo-tool-plan, pv-fy-prev, pv-fy-new).
- Preview features not meant for production: supported.
- GitHub managed settings set the approved and denied server list by URL for GitHub Copilot clients: supported (gh-url, gh-block, gh-profiles). GitHub's own settings do not reach Foundry or Copilot Studio (fy-gov, studio); the pipeline design covers them (see Policy sync). That the GitHub and Agent 365 lists can drift apart is **inference**.
- Shared backend credential carries backend permissions, uneven coverage across paths: **inference**.

### Parts table (added 2026-11-08)

- API Management MCP servers: management features are listed by tier (mcp-tiers). Microsoft announced general availability in Nov 2025, available across classic and v2 tiers, Developer tier and self-hosted gateway: supported by the Microsoft release feed (apim-ga, apim-ga-tiers). An older Azure update that calls v2 support a public preview is superseded by that GA. Rate limiting and JWT validation policies: supported (mcp-rate, mcp-authn).
- AI Gateway: Entra access or a gateway API key authorizes callers, policies include consumption limits, telemetry covers tool usage: supported (pv-aig-caller, pv-aig-limits, pv-aig-tel). The page now says only "Yes for callers" and "Partly" for these. The earlier statements that a per-tool rule, a request rate limit and logging of every call are not named are **cut from the page**.
- Table cells are not read by the label check. The one new heading ("Parts of the design") is in the ledger as a label.

### Policy sync (added 2026-11-08)

- GitHub managed settings can be hosted on GitHub as a server-managed deployment: supported (gh-deploy). They are a file (`copilot/managed-settings.json`) changed by commit and push to the default branch: supported (gh-file, gh-commit). That a pipeline can make that commit follows from this: **inference**, nothing was tested.
- (Superseded by the current claim audit above.) Power Platform advanced connector policies cover certified connectors only; custom and HTTP connectors are not yet supported: supported (pp-certified, pp-custom). This omitted the separate MCP connector support documented at pp-block.
- Power Platform ACP supports whole-server MCP blocking, not individual MCP tools (pp-block). The current API tutorial has no MCP-specific example, so API automation of MCP connector entries needs tenant verification (pp-pipe, checked by search of the fetched tutorial text).
- Foundry MCP tool: nonempty allowed tool list restricts tools, an empty list allows all: supported (fy-allowed). A rule that blocks one MCP server URL across Foundry was not found in any source; the page says so only in the gaps and does not rely on it.
- Agent 365 does not list Foundry as a supported client surface for registered servers: supported (pv-byo-surf).
- Drift between the repository and a target, and the fourth copy of the list in Agent 365: **inference**.
- Release status of the API Management MCP features: sourced from Microsoft's release communications feed (apim-ga, apim-ga-tiers). The earlier third-party mirror is no longer used.
- Agent 365 and Foundry against the new resource type: not tested. The page says so as a limit, not as a product claim.

### Claim check, 2026-11-08 (second pass)

Each quote was read in its source context and compared with the page wording, not only matched mechanically. The page date column was compared with "Last updated on" on all 22 Microsoft Learn pages, fetched live: all 22 match. The other sources show no date or are the mirror (2025-11-18).

Changed because the wording went further than the source:

- Copilot Studio policy blocks a whole server, not a single tool, and covers certified connectors only. Added pp-certified and pp-custom. A company server may fall outside it: **inference**.
- Shared backend credential: now sourced (pv-shared-cred), no longer inference.
- Old tier removal: now sourced (pv-res-removed, "permanently removed").
- GitHub pipeline write: was unverified, now **inference** from gh-file and gh-commit.
- API Management release status: apim-ga and apim-ga-tiers now come from Microsoft's own release feed (id 527626, status Launched, GA 2025-11, modified 2025-11-18). The checker reads the feed as JSON and uses a curl user agent because the feed refuses a browser name.
- Outbound limits: "can be considered for certain highly secure environments" and "limits with proxies and some VPN tunnels" now follow dk-secure and dk-limits.
- Gateway row: "Microsoft suggests API Management" follows gw-consider; "Clients go through it so the backend is not silently redirected" follows gw-redirect.

Cut from the page in the third pass because no source supports them (the stop condition says every statement must be verified):

- Per-URL block of one MCP server in Foundry or Copilot Studio ("no source shows it" remains in the gaps as a statement about the sources checked, and the design does not rely on it).
- "An agent cannot call arbitrary external MCP servers" in Foundry, sandboxing local stdio servers, AI Gateway per-tool authorization, request rate limit and logging of every call, "No source says which endpoint telemetry to collect", "Older examples can be stale".
- The unverified and inference tags are gone from the page. Every deduction was either reworded to what a quote says, or turned into a design requirement (recommendation, our choice, no source needed), or cut. See the fourth pass below.

### Fourth pass, no inference left

Fifteen inference labels were resolved. Reworded to the quotes: Agent 365 client surfaces (pv-byo-surf), Foundry routes only new MCP tools made in the portal without managed OAuth (pv-fy-prev), API Management v2 has no tool-level access control (pv-a365-v2), stdio is a subprocess (stdio), and the resource migration line, which was already sourced. Turned into recommendations: Foundry and Copilot Studio get the list from the pipeline, the backend re-checks the token, the pipeline overwrites drift or alerts, a fourth copy of the list is compared after every run, an unmanaged workstation is assumed to have no client rules, check which capabilities remain before a switch. Cut: that GitHub managed settings reach GitHub clients only, that tool blocking is not universal, that tool-level blocking "may not remain". The Environment cell "Apply to other MCP clients" now says only that these are VS Code policies.

Checks after the edits: quote check 84 quotes, 0 problems; label check 90 texts, no paragraph or cell over 60 words; no em or en dashes in the page. Browser check after these edits (localhost, 2026-11-08): at 375px in light and dark mode the page is 375 wide on both paths, no sideways scroll, no console errors, no dead in-page links. Re-run after the third pass: 48 fact check rows on Released only and 84 with preview, the word "unverified" appears nowhere on the page.

## Not checked / nothing tested on a real system

- Visual and behaviour check of both paths on 2026-11-08 (localhost): the chooser and the Safe/Preview control switch the path; `?path=preview` restores it; a link into hidden content (`#fallback`, `#ev-V40`) switches the path; safe showed 33 evidence rows and preview 64 at that time (now 42 and 76); at 375px no sideways scroll on either path; no console errors from the page; no dead in-page links. Earlier check: desktop width and 375px wide, no sideways page scroll, no console errors, no dead in-page links. Dark mode was not viewed: the browser pane renders local files in light only. The dark tokens are copied from the governance summary page.
- ASCII figures (repository, pipeline, targets, clients) checked on 2026-11-08 over localhost on both paths: render as written, red text shows, no console errors. At 375px the page does not scroll sideways and the figure scrolls inside its box. Dark mode not viewed. The pipeline itself is not built or tested. Re-checked after the bold titles and the "Company MCP server" rename: both paths render, bold titles and red lines show, at 375px the page is 375 wide and the figure scrolls inside its 343px box, no console errors. Label check and quote check passed at that time (counts are now 92 texts and 76 quotes). After moving Agent 365 under the gateway: preview figure re-viewed on desktop, no console errors. 375px not re-checked for this change (figure width unchanged at 84). After the path rename: desktop and 375px checked, the two buttons fit (right edge 359), page 375 wide, no console errors. After removing "The answer": the design intro viewed on desktop, no console errors; 375px not re-checked.
- Parts table viewed on 2026-11-08 on both paths: 20 rows each, no dead evidence links (16 released, 32 preview), no console errors. At 375px the page is 375 wide and the table scrolls inside its 343px box. Dark mode not viewed. Label check 92 texts and quote check 76 quotes pass.
- Preview figure with the two added gateway items checked on 2026-11-08: desktop renders as written, at 375px the page is 375 wide, no console errors. Dark mode not viewed. Label check (92 texts, no new text) and quote check (76 quotes, 0 problems) pass.
- Full-width text change checked on 2026-11-08: desktop paragraphs, lists and captions fill the section, at 375px the page is 375 wide, no console errors. Dark mode not viewed. Label check (92 texts) and quote check (76 quotes, 0 problems) pass after the rename.
- Summary box and chooser removal checked on 2026-11-08: the switch changes the path and sets `?path=preview`, the label "Select design" shows, at 375px the page is 375 wide and the switch wraps below the links, no console errors. Dark mode not viewed. Label check (91 texts) and quote check (76 quotes, 0 problems) pass.
- Text-fragment links on the evidence table were not clicked one by one.

- No acceptance test was run. No tenant, managed laptop or hosted agent runtime was used.
- No source shows a URL-level block for one MCP server in Foundry or Copilot Studio. Copilot Studio blocks a whole server through Power Platform policy; Foundry limits tools per agent. Nothing beyond the quotes listed was checked.
- Page dates come from the source pages. Four sources show none.

## Reviewed presentation text

The checker proves a verdict was recorded for the exact wording, not that the verdict is right. It reads each run of words in the ASCII figures as one text. Verdicts were set by hand: label, requirement or code token.

<!-- Begin reviewed presentation text -->
```text
label	MCP Governance in a Microsoft ecosystem
label	Platform and security owners
requirement	See the design and its controls.
label	Architects
label	See what works in each Microsoft environment.
label	Decision makers
label	recommendation
label	preview
label	The design
requirement	Design target: a Git repository holds the approved and denied MCP servers. A reviewed pull request changes it. After merge, a pipeline applies the list to three targets: Power Platform policy for Copilot Studio, GitHub managed settings, and Foundry. Each target points to the clients it governs. The clients then pass through client controls, Windows outbound firewall rules where applicable, API Management and the company MCP server, which only the gateway can reach. A direct call from a client to the server is blocked.
label	SOURCE OF TRUTH
label	APPLY ON MERGE
label	GIT REPOSITORY
label	PIPELINE
label	Change by pull request
label	Runs after merge
label	COPILOT STUDIO
label	GITHUB MANAGED SETTINGS
label	FOUNDRY
label	Policy target
requirement	Approved list
requirement	Approved tools
label	MCP CLIENTS
label	Copilot Studio
label	VS Code
label	Foundry agents
label	GitHub Copilot
label	CLIENT CONTROLS
label	API MANAGEMENT
label	COMPANY MCP SERVER
label	URL allowlist
requirement	Check identity
requirement	Gateway only (target)
requirement	Windows egress limits
requirement	Authorize requests
requirement	Sign-in required
requirement	Log every call
requirement	Limit request rate
requirement	Unlisted server denied
label	MCP clients
label	Company MCP server
requirement	Blocked. Only the gateway may call the server
requirement	Design target: the released-only design with preview additions. A Git repository holds the approved and denied MCP servers. After a reviewed merge, a pipeline applies the list to Power Platform policy for Copilot Studio, GitHub managed settings and Foundry. Each target points to the clients it governs. The clients then pass through client controls, Windows outbound firewall rules where applicable, Azure AI Gateway with tool threat protection, and a company MCP server that only the gateway can reach. A direct call from a client to the server is blocked. The design connects the Agent 365 admin view below the gateway.
label	AI GATEWAY, PREVIEW
requirement	Publish MCP endpoints
requirement	Tool threat protection
requirement	Connect gateway
label	AGENT 365, PREVIEW
label	Admin view
label	Gateway integration
label	Added with preview preview
label	Acceptance tests
label	Order of work
label	Preview pilot, after the baseline preview
label	Known gaps and what has not been tested
label	Bad news first
label	Open questions
requirement	Which comes first: developer workstations or hosted agents?
requirement	Workstations call for client rules and, on Windows, outbound limits. Hosted agents call for network isolation and data policies. Start where the more sensitive backends are. See the environment table.
requirement	Is a default outbound block on managed Windows laptops acceptable?
requirement	Decide before rollout. The effect on other traffic is in the gaps.
requirement	Who reviews list changes and owns the pipeline?
requirement	Name the reviewers of the repository, the pipeline owner and the person called when a target fails to update.
requirement	Who approves and reviews the Agent 365 consent?
requirement	The consent lets the service write API policies. Name an approver and a reviewer. See the controls.
requirement	What ends the pilot?
requirement	Set the exit evidence now: terms accepted, features released, clients covered. Without it the pilot has no end. See the fallback.
requirement	Does a gateway with no private endpoints fit the network rules?
requirement	The new resource has no private endpoints. Check the rules before building. See the gaps.
requirement	Which Agent 365 route will the pilot use?
requirement	Choose the API Management gateway integration or the separate BYO server registration route. See the controls.
label	Fact check
label	Parts of the design
requirement	A proposed design for governing MCP servers across GitHub Copilot, VS Code, Foundry and Copilot Studio. Select Released only or With preview. Nothing is built or tested yet.
requirement	Choices: never, in a sandbox only, or later. Require released features for production. The proposed pipeline and cross-client enforcement still need validation.
label	Controls
requirement	Are preview features allowed at all?
label	Environments
label	Fallback
requirement	Released only is the baseline. Compare it with the preview design, then read the open questions.
requirement	Design requirements and supporting evidence are below
requirement	The repository list is the design's source of truth. The pipeline is a design requirement, and none of it is built or tested. Control requirements and evidence follow below.
requirement	With preview, connect the API Management gateway to Agent 365 and test tool threat protection in a sandbox. The BYO server route is separate; its limits are listed below.
```
<!-- End reviewed presentation text -->

## Browser check, 2026-11-08, follow-up pass

Local server, light mode only (the pane cannot render dark mode, so dark mode is still not viewed).

- Desktop 1134px: lead, Objectives and Designs lines, switch with "Select design" label and "Released only" button render. Fact check columns measure 72, 668, 242 and 120px. No console errors.
- 375px: page width 375, no sideways scroll. After scrolling 1800px the switch bar is pinned at the top (46px high) and the contents links have scrolled away.
- Switch tested by script clicks only, not real mouse clicks. Released only shows open questions 1 to 4. With preview shows 1 to 8, one figure, and sets `?path=preview`. Switching back removes it.
- Not tested: the quote text-fragment links by mouse, dark mode.
- Label check: 92 distinct texts, all with a verdict. The script proves a verdict exists for the exact wording, not that it is right. It does not read the In short, Objectives, Designs and How to read lines, table cells or the red text legend, so those were checked by eye against the labelling rule.
- Quote check: 76 quotes, 0 problems. Quote text was not changed.

## Dark mode check, 2026-11-08

Claude in Chrome was not connected. The built-in browser can emulate `prefers-color-scheme: dark` on a localhost page, so the check used that (earlier notes said it could not; it can).

- Page background rgb(21, 20, 15). Both designs and the 375px layout were viewed. No console errors. Page width 375 at 375px, no sideways scroll.
- Text contrast measured by script on body text, goals, notes, table cells and headers, contents links, switch, figure text, red text and the badges: lowest is 6.7 (unverified and preview badges, red figure text). All above 4.5. The recommendation badge sits on a 5% overlay and was measured at 2.2 by mistake against the overlay colour itself. Its text is the same muted grey as the other body notes (6.9 on the page background).
- At 375px the pinned switch bar is 46px high with the dark page background.
- Not tested: real mouse clicks on the switch, the quote links, a real phone.

## Current generated page checks, 2026-11-08

- The latest build has 89 evidence quotes: 49 released-only and 40 preview. It reported no paragraph-length warnings. The wording checker passed for 83 distinct presentation texts.
- A static check found all 89 quote rows and quote text in the page, no broken internal anchors, no broken evidence links, and no em or en dashes.
- The current shell quote-checker run could not fetch any source because external DNS lookup failed. The source text for V77 and V85-V88 was compared with current Microsoft Learn pages; V89 was compared with the MCP specification.
- The desktop browser refused to open the local file URL, so the current build was not viewed in light or dark mode or at 375px, and the current interactions were not retested. Earlier browser notes describe a previous build.
