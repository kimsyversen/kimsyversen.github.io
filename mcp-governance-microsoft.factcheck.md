Belongs to: [MCP Governance in a Microsoft ecosystem](mcp-governance-microsoft.html)

# Fact check: MCP Governance in a Microsoft ecosystem

Documentation checked: 2026-11-11.

## 2026-11-11, one-page simplification pass

Asked: can the page be made much smaller without losing information, and are the statements still true after the merge? Method: rebuilt the page, reread every section of the built text, reran the quote, label and anchor checks, and compared element ids with the old page.

- **Moved.** The source quotes (V1 to V202) now live only in this file, in the table under "Source quotes". The page links each quote mark to its row. The earlier entries that say "the page lists every quote" or describe the path switch and the collapsed fact check on the page are superseded by this entry; they stay for history.
- **Merged.** Three design tables into one, Controls and Guardrails into one section, all preview content into "With preview". Each fact has one home: preview-only quotes are cited only in With preview (128 quotes back the released-only design, 74 the preview additions; the builder stops if a preview-only quote is cited in the released part).
- **Wording fixed on reread.** "Path" in reader text and figure descriptions changed to "design", because the path switch is gone. Two ledger entries were updated.
- **Dropped on purpose.** The preview guardrail figure (replaced by a delta table with the same facts) and the "tool call and response" row in the released guardrail table (preview only, so it is in With preview).
- **Result.** Quote check 202 quotes, 0 problems against the live sources on 2026-11-11. Label check 200 texts. Anchor check passes. Every old id kept except `seg-lbl`. No em or en dashes. Words on the page 13,785 to 8,023.
- **Not checked.** The quote links and the `#ev-V` redirect go to the GitHub copy on master, so they cannot be tested until it is published, and GitHub's anchor behavior was not tested. Nothing was tested in a tenant. Not tried on a real phone or in Safari.

## 2026-11-11, which gateway pass

Asked: Microsoft uses "AI gateway" for three configurations (API Management with AI gateway capabilities, AI Gateway integrated with Foundry, dedicated AI Gateway preview). Which does the page use, and what follows? Method: the Foundry gateway configuration page was read live on 2026-11-11 (page date 2026-08-03); the Foundry tools governance page was reread.

- **Finding.** The page used the first on the released-only path and the third on the preview path. The second was only a preview control row and was not named as its own kind of gateway.
- **Verified for the second kind.** It runs on Azure API Management (V197). Create new makes a Basic v2 instance (V198). An existing instance must be a v2 tier (V199) in the same tenant and subscription as the Foundry resource (V200). Microsoft suggests Standard v2 or Premium v2 for production (V201). It supports only MCP tools (V202). Routing MCP tools through it is preview (V60).
- **Changed on the page.** New "Which gateway" table under The design (3 rows), a link to it from the Gateway product row in Parts, one gap (gap-one-gateway). Recommendation added: choose a v2 tier on the released-only path and connect Foundry to that instance.
- **Interpretation by AI.** That one v2 instance can be both the Foundry AI Gateway and the gateway for the company MCP server. The source lists requirements for an existing instance, not this combined use. Not tested.
- **Not checked.** The SKU names in the list the page was checked against, beyond what the quotes say. Networking limits of Basic v2 for a private backend. Nothing was tested in a tenant.
- **Nine older quotes repaired.** The quote check failed for V181, V182, V183, V186, V187, V188, V193, V194 and V196 against the live sources. Each was replaced with the exact live wording that backs the same sentence on the page. Two real wording differences: V193 now reads "publish or reject it" (was "approve or reject the request"), and V188 no longer contains the sentence about BYO support being planned; that claim on the page rests on the preview BYO quote cited beside it. V181 and V182 are now the navigation steps to the Registry and Requests (preview) tabs, because the "centralized view" sentence is not on the page served today.
- **Result.** 202 quotes, 0 problems. Label check and anchor check: see the plan.

## 2026-11-11, remote MCP URL allowlist scope

- **Asked.** Clarify whether the design's URL allowlist belongs to VS Code and is synced through GitHub settings into Intune.
- **Method.** Rechecked the current VS Code enterprise policy, GitHub enterprise managed settings and deployment documentation on 2026-11-11.
- **Finding.** The figures now label the remote MCP URL allowlist for managed VS Code and GitHub Copilot. VS Code has its own enterprise policies. GitHub managed `allowedMcpServers` supports remote server URL matchers and local server command matchers. GitHub settings can be delivered through GitHub or separately through MDM; the design's pipeline writes to GitHub managed settings and does not describe propagation into Intune. Device egress rules are separate.
- **Verification.** This wording describes the proposed control scope, not a tested tenant configuration. Sources: [VS Code enterprise policies](https://code.visualstudio.com/docs/enterprise/policies), [GitHub managed settings](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings), [GitHub deployment methods](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/deploy-managed-settings).
- **Reviewed presentation text.** Added the two-line figure label and clarified its scope in each figure's accessibility description. See the ledger below.

## 2026-11-11, client and backend control labels

- **Asked.** Make client sign-in, Windows egress enforcement and the backend's gateway-only access explicit in both design figures.
- **Changed.** The figures now label client sign-in separately from gateway identity checks and authorization, identify Windows egress as an Intune-managed control, and state that the backend accepts calls only from the gateway. Accessibility descriptions explain the same boundaries.
- **Basis.** These labels express design requirements. The Windows Firewall administration claim is supported by the existing Intune/Windows firewall evidence in this page; gateway identity and authorization requirements are described in the API Management and backend control sections. The remote MCP URL allowlist remains explicitly scoped to managed VS Code and GitHub Copilot.
- **Verification.** Builder, section-anchor, reviewed-label and diff whitespace checks passed. The quote checker was attempted but could not resolve source hosts in this environment (193 fetch failures). A browser layout check could not be performed because the local server could not bind and the browser blocks local file URLs.

## 2026-11-11, API Management AI gateway versus AI Gateway product

- **Asked.** Make the diagram clear about which gateway functionality is supported in API Management and which belongs to a preview product or integration; verify the distinction against current Microsoft documentation.
- **Method.** Read the current Microsoft Learn pages for API Management MCP servers, API Management AI gateway capabilities, AI Gateway, Agent 365 integration and tool threat protection on 2026-11-11.
- **Finding.** Microsoft uses "AI gateway" for capabilities in the existing API Management service and also names a distinct product "AI Gateway." The API Management page says its AI gateway extends the existing API gateway and is not a separate offering; the AI Gateway overview separately calls AI Gateway a dedicated product with a different resource type. API Management MCP management is listed for classic Developer, Basic, Standard and Premium, and v2 Basic, Standard and Premium tiers; actual capabilities vary by tier. AI Gateway is in public preview. The Agent 365 integration is labeled preview: its capability table lists inventory and server block/unblock for API Management v2 and AI Gateway, while tool-level blocking, tool activity observability and tool threat protection are listed only for AI Gateway. Tool threat protection itself is documented as preview. The earlier API Management AI Gateway SKU is being replaced by the new AI Gateway resource type by 15 January 2027.
- **Changed.** The released-only figure now names supported API Management tiers. The preview figure names AI Gateway as a separate product and public preview. The component map and accessible descriptions distinguish the two gateway meanings and state which Agent 365 controls are limited to AI Gateway. Foundry gateway integration and remote MCP firewall filtering remain separately identified as preview features.
- **Sources.** [API Management MCP availability](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview), [AI gateway capabilities in API Management](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities), [AI Gateway overview](https://learn.microsoft.com/en-us/azure/ai-gateway/overview), [Agent 365 with API Management](https://learn.microsoft.com/en-us/azure/api-management/agent-365), [AI Gateway tool threat protection](https://learn.microsoft.com/en-us/azure/ai-gateway/policy-tool-threat).
- **Verification.** These current source pages were read directly on 2026-11-11. New exact quotes V194 to V196 were added without changing existing evidence IDs. Builder, section-anchor, reviewed-label (208 texts) and whitespace checks passed. The automated quote checker could not resolve source hosts (196 fetch failures); the quoted statements were compared with the live Microsoft Learn pages above. Browser layout check not run: the local server cannot bind in this environment and the browser blocks local file URLs.

## 2026-11-11, Microsoft 365 agent inventory and approval workflow

- **Asked.** Show the Microsoft 365 admin center agent inventory, MCP tool/server states and Requests (preview) in the design, and explain how approve and deny decisions work.
- **Method.** Read current Microsoft Learn pages for the Tools page, MCP server approval, the Agent Registry, agent details and agent requests on 2026-11-11. Added 13 quotes, V181 to V193, 193 total.
- **Finding.** These are related but distinct admin views: Agents > All agents > Registry inventories agents; Agents > Tools > Registry lists tools and shows Available or Blocked status; Agents > Tools > Requests (preview) reviews tool and MCP server registration requests. Agent details can show Data & tools metadata, but it is read-only and is missing for some agents. Approval of an agent publication is a separate workflow from approval of an MCP server registration.
- **Approval flow added as a recommendation.** Review the server and its declared tools through an internal Git pull request first. If it passes, merge the inventory change and register the server through the Agent 365 BYO preview route. A Microsoft 365 administrator separately approves or rejects the request. Approval alone does not make the server available: the required Microsoft Entra tenant consent must also be granted. On rejection, keep the server unavailable and record the reason. For later revocation, block the server, mark it denied in Git, remove it from each target policy and test that calls fail. Microsoft admin-center actions do not update the other targets automatically.
- **Tool-level limit.** Individual tool controls are rolling out for supported Agent 365 server types. Microsoft says BYO server tool-level blocking is planned, so this workflow requires server-level blocking plus backend authorization for the BYO route until per-tool support is available.
- **Changed.** Preview design diagram now shows the separate agent inventory, tool registry status and Requests queue. The control-planes table names both agent and MCP server views. A new workflow figure, steps and acceptance tests describe the two approval gates and deny path.
- **Reviewed presentation text.** Added the heading and figure labels to the machine-readable ledger below. The labels describe navigation or the proposed flow. Product claims link to V181 to V193 and existing Agent 365 evidence. The new acceptance tests are targets and remain Not run.
- **Verification.** Builder, section-anchor check and reviewed-text check passed. No tenant or browser test was run. The local quote-fetch script cannot reach documentation hosts in this environment; the current source pages were read in the web research results.

## 2026-11-11, approval boundaries and cross-cutting guardrails

- **Asked.** Add crucial cross-cutting points after comparing approval, server governance and guardrails across the four targets.
- **Method.** Rechecked the cited primary Microsoft and GitHub documentation on 2026-11-11. The new subsection uses existing quote IDs; no new product claims or quote IDs were added.
- **Verification limits.** Anchor and reviewed-text checks passed. The local quote-fetch check could not reach documentation hosts from the execution environment, so it could not validate all stored quotes. No tenant or browser test was run for these recommendations.
- **Added.** One reviewed inventory must map to each target's different policy type; re-review server URL, authentication, permissions and exposed-tool changes; record the GitHub built-in server and custom agent profile exceptions and Power Platform's server-level-only blocking; require authentication and authorization at the gateway and backend; test denied server, tool and identity cases; verify policy sync and retain logs.
- **Reviewed text.**

| Text | Verdict | Basis |
|---|---|---|
| Approval boundaries and cross-cutting guardrails | label | Subsection heading. |
| Keep one reviewed inventory, but translate it into each target's control. A server allowlist, an agent's tool allowlist, and a federated connector audience are different settings. | requirement | Proposed governance model. The target-specific controls are described in the Control planes table and the policy sync rows. |
| Re-review a server when its URL, authentication, permissions, or exposed tools change. | requirement | Change review requirement for the approved inventory. |
| Keep Foundry's `allowed_tools` list nonempty. An empty list permits all tools. | requirement | Foundry MCP tool evidence V69. |
| GitHub's allow and deny lists do not block the built-in GitHub MCP server and do not apply to servers in custom agent profiles. | product claim | GitHub evidence V20 and V21. |
| Power Platform blocks MCP servers as a whole, not individual tools. | product claim | Power Platform evidence V65. |
| Require authentication and authorize each request at the gateway and backend. | requirement | Identity control design. Microsoft IP allowlist limitation V174 and gateway identity evidence support the requirement. |
| Network allowlisting and a client approval prompt do not grant permission to read or change data. | requirement | Security design principle; the server remains responsible for identity and authorization. Microsoft explicitly states IP allowlisting does not replace authentication or authorization (V174). |
| Test that an unapproved server, an unapproved tool, and an unauthorized identity are denied. | requirement | Proposed acceptance criteria. |
| Check that each policy target received the current inventory. | requirement | Proposed sync verification for the target-specific pipeline. |
| Retain gateway logs and review connector activity in Purview where applicable. | requirement | Gateway logging evidence V3; Purview activity audit evidence V165. |

## 2026-11-11, control planes pass

Asked: given five control planes (Agent 365, GitHub Enterprise AI Controls, Power Platform, Foundry Control Plane, Microsoft 365 Copilot controls), make the design cover every plane where MCP must be governed. Method: the Microsoft 365 Copilot connector pages and the Agent 365 pages were read live on 2026-11-11.

- **Finding.** The design figures had three policy targets and no Microsoft 365 Copilot. Microsoft 365 Copilot connects to MCP servers through federated connectors (V162), governed in the Microsoft 365 admin center (V163). It was missing as a policy target and as a client.
- **Added (19 quotes, V162 to V180, 180 total, 0 problems in the quote check).**
  - Microsoft 365 Copilot: federated connectors use MCP (V162); admins control availability (V163, V168); a custom connector starts with an MCP server (V166) and needs Global Administrator or AI Administrator (V167); every setting must allow the user (V169); tool and connector blocking (V172); write tools need user approval (V164); audit in Purview (V165).
  - No automation: Agent and plugin access has no PowerShell or API option (V171). The figures mark this target "By hand".
  - Network path: MCP calls use fixed outbound addresses (V173); a server that filters by source address must allow them (V170); allow listing does not replace sign-in or authorization (V174); the list can change with seven days' notice (V175).
  - Agent 365: generally available since 1 May 2026 (V176); the Tools registry in the Microsoft 365 admin center is the source of truth for MCP servers in the tenant (V177); BYO registration (V178) and the tools gateway are preview features (V179, V180). So the released-only figure leaves Agent 365 out and says why.
- **Changed on the page.** Both design figures redrawn from a script: four policy targets named by control plane, each with its admin surface and how the list is applied; Microsoft 365 Copilot as a fourth client that reaches the gateway from the Microsoft cloud. New "Control planes" table (7 rows). Two new Controls rows, one Environments row, three acceptance tests (not run), two gaps, one line in open question 4, one note in Guardrails by layer. The misaligned box lines in the old preview figure are gone.
- **Interpretation by AI.** That device URL policy and Windows firewall rules do not see Microsoft 365 Copilot calls, because they leave from the Microsoft cloud. That federated connectors are released: the pages carry no preview label for them (only a note on Work IQ Dev Tools). That Azure API Management and device management count as control planes for MCP. That the Microsoft 365 admin center is a fourth policy target.
- **Unverified, not tested.** The admin surface names "Power Platform admin center" and "Foundry portal" are not quoted from a source. Whether a custom federated connector can be created by API. Whether blocking under Agents > Tools needs an Agent 365 licence. Declarative agents that carry their own MCP server were not read in depth. Viewing a connector's tools in the admin center is listed as coming soon. Nothing was tested in a tenant.
- **Reviewed text.** 21 new or changed texts, 6 removed. Each was read against the figure and the sources:

| Text | Verdict | Basis |
|---|---|---|
| A proposed design for governing MCP servers across GitHub Copilot, VS Code, Foundry, Co... | requirement | Figure description or page text. It states the design; product facts in it are sourced in Controls and the Control planes table. |
| Agent 365 not drawn: company servers join it through preview features | label | Scope note for the released-only figure. The claim is sourced in the Control planes table (V176, V179, V180). |
| Approved connectors | requirement | Design requirement: only approved servers become custom federated connectors. |
| By hand | requirement | Design requirement. Backed in Controls by V171 (no PowerShell or API for Agent and plugin access). |
| By pipeline | requirement | Design target. The pipeline is proposed and not built. The Power Platform path is marked unverified in Controls. |
| Control planes | label | Heading. |
| Design target: a Git repository holds the approved and denied MCP servers. A reviewed p... | requirement | Figure description or page text. It states the design; product facts in it are sourced in Controls and the Control planes table. |
| Design target: the released-only design with preview additions. A Git repository holds ... | requirement | Figure description or page text. It states the design; product facts in it are sourced in Controls and the Control planes table. |
| Foundry portal | label | Admin surface name. Marked unverified in the Control planes table. |
| GITHUB ENTERPRISE | label | Box title. Replaces GITHUB MANAGED SETTINGS. |
| MICROSOFT 365 | label | Box title, new fourth target. |
| Managed settings | label | Admin surface, first line. Sourced by V55 and the managed settings quotes in Controls. |
| Microsoft 365 Copilot | label | Client name. |
| Microsoft 365 admin | label | Admin surface name, first line. Sourced in the Control planes table (V163). |
| Microsoft cloud, fixed outbound addresses | label | Path label. Sourced in Controls (V173). That device controls do not see these calls is interpretation by AI. |
| Name the reviewers of the repository, the pipeline owner and the person called when a t... | requirement | Figure description or page text. It states the design; product facts in it are sourced in Controls and the Control planes table. |
| POWER PLATFORM | label | Box title. Replaces COPILOT STUDIO as the target name; Copilot Studio stays as the client. |
| Power Platform admin | label | Admin surface name, first line. From the control plane list the page was checked against. Marked unverified in the Control planes table. |
| TARGETS | label | Row label for the policy targets. |
| center | label | Second line of an admin surface name. |
| repository | label | Second line of the managed settings surface. |


## 2026-11-11, guardrails by layer, verification pass

Asked: are the statements in "Guardrails by layer" correct, and is important information missing. Method: every source page of the section was read again live on 2026-11-11, then the product documentation was searched for guardrails the section did not name.

- **Existing statements.** All 131 earlier quotes matched live. No statement in the old 16 rows was found wrong. Two were too narrow and are widened below (Foundry approval, VS Code confirmation dialog).
- **Missing, now added (30 quotes, V132 to V161, 161 total, 0 problems in the quote check).**
  - Foundry: agent guardrails are in preview (V134). With no agent guardrail the agent inherits the guardrail of its model deployment (V135). `require_approval` can also be `never` or a list of tools that skip approval (V136). Preview: controls take no effect for tools outside the supported list (V132), and the tool response control scans for indirect prompt injection (V133).
  - Copilot Studio: tool setting "Ask the end user before running", off by default (V137). Fills layer 3, which said None found. Preview threat detection: generative orchestration only (V138), error behaviour can be set to block (V139), data is shared with the provider (V140).
  - Defender real-time protection (preview path): blocking scenarios (V141 to V143 and the earlier email quote), email scenario only at the tool request (V144), rule scope only for agents with a Microsoft Entra agent ID (V145), local agents are covered by Defender for Endpoint instead (V146).
  - Defender for Endpoint runtime protection (preview path): prerelease (V148), blocks before an action runs when the inspection method allows it (V147), Windows (preview) table lists the VS Code GitHub Copilot extension (V149, V150). No layer stated for this client.
  - VS Code: Manual permissions is the default and asks for confirmation (V151), Allow all skips confirmation (V152), Assisted permissions uses an LLM judge (V153), post-approval and result review (V154, V155), policy and managed setting that lock approval (V156, V157), server trust decision (V158), preToolUse hook (V159) and its stated limit (V160).
  - GitHub Copilot Chat: a content filter "may" scan prompts and responses (V161). The page marks this as weak wording, interpretation by AI.
- **Interpretation by AI.** Which layer each new control sits at (the sources name no layer numbers). That the GitHub content filter is not a control to count on. That on the released-only path the Foundry controls should sit on the model deployment. That the Foundry supported-tool list not naming MCP means the tool call and tool response controls should not be relied on for MCP (unchanged).
- **Unverified, not tested.** Whether Copilot Studio offers "Ask the end user before running" for MCP tools. Whether a VS Code preToolUse hook sees MCP tool calls. Which VS Code tools ask for a result review by default. The VS Code approval policy on a managed device. Nothing in this section was tested in a tenant or on a device.
- **None found.** Now only Copilot Studio at layer 7 (tool response). Defender for Copilot Studio covers tool invocations only (V119, V120). Not proof that no guardrail exists.
- **Result.** Table: 25 rows, 20 on the released-only path. Label checker: 151 distinct texts, 0 missing, 0 stale. Ledger rows for the 18 new or changed figure texts are in the table of the next section. Three texts were removed from the figure ("if a call needs approval", "(documented for VS Code)", and the old descriptions).
- **Superseded in the section below.** The counts (16 rows, 131 quotes, 135 texts, 53 ledger texts) and the list of None found cells are history.

## 2026-11-11, guardrails by layer section

- **Scope.** Last section "Guardrails by layer", then the collapsed "Fact check" section (moved to the bottom, collapsed by default, opens on a link to a quote). Two figure files, `.figure-guardrails-safe.txt` and `.figure-guardrails-preview.txt`, drawn as one flow: a tool call goes down through layers 1 to 6, the response comes back up through layers 7 and 8. The table has 16 rows, 14 on the released-only path. 33 quotes added (V97 to V130), 130 in all.
- **Live check.** All 131 quotes matched their sources on 2026-11-11 (0 problems), so the documentation date moved from 8 to 11 Nov.
- **Defender and Agent 365 runtime protection.** Read the page "Protect AI agents in real time using Microsoft Defender" (checked 2026-10-15, V117 to V125 and the Defender quote V116). Foundry agents (Preview) are checked at user request, agent response, tool invocation and tool response. Copilot Studio agents (Preview) are checked at tool invocation. Agent 365 covers tool invocations, including customer MCP tools onboarded to Agent 365; unsupported tools and agents are not covered. The default rule only audits, custom rules block. Shown on the preview path only. The Agent 365 line is not labelled preview on the page, but its MCP path is called preview in the sources, so the preview label is interpretation by AI.
- **Foundry tool call and tool response guardrails do not cover MCP.** The intervention points page lists the supported tools (Azure AI Search, Azure Functions, OpenAPI, Sharepoint Grounding, Fabric Data Agent, Bing Grounding, Bing Custom Search, Browser Automation). MCP is not on it (V104, V105). The page never says "MCP is not supported", so the figure marks this as interpretation by AI.
- **Protected material.** Annotate only, with a flag in the annotation response (V99, V126). It does not block.
- **"None found" cells are not proof.** They mean the pages read on 2026-11-11 do not describe a guardrail at that layer: VS Code and GitHub Copilot at layers 1, 4, 7 and 8; Copilot Studio at layers 3 and 7. Not tested in a tenant.
- **Copilot Studio content moderation (V111).** The source does not say at which layer, so the figure has an "ANY LAYER" line and the table has its own row.
- **Foundry default approval (V106).** The page text says the default is `always`, while one REST sample sets `never`. The page cites the stated default only.
- **Browser check.** See "Browser check 2026-11-11" in `.plan.md`.
- **Second method, claim words against quote text (script, 2026-11-11).** For each of the 16 table rows, every sentence was split into content words and each word was looked up in the text of the quotes the row cites. 56 sentences, 31 had words not in the quotes. All 31 were read by hand: paraphrase verbs ("checks", "scans", "limits", "shows"), names ("Microsoft") or sentences marked as interpretation by AI. Four were real gaps and were fixed: Data policy "not per tool" now also cites V65 (granular control over individual MCP tools isn't available); Allow and deny lists named "managed settings" for VS Code, but VS Code calls them policies, so the row and the figure label now say "VS Code policies and GitHub managed settings", and the deny-wins claim for GitHub has its own quote (new V131); Protected material "annotate only" was not in V99, so V99 now starts with "Action: Annotate only"; V128 now starts with the full sentence about the two ways to edit a control. The script also asserts key phrases in 14 quotes (for example V105 does not name MCP). Limit: it matches words, not meaning, so a sentence that reuses the quote's words with the wrong sense would pass. The hand review above covers that.
- **Quote links on load (browser, localhost, 2026-11-11).** All 131 `#ev-V` links were loaded on both paths at 986 px and 375 px (524 loads): the Fact check opened, the row existed and was visible, the row was inside the viewport, and the page had no sideways scroll. The first run failed 262 of 262 in-view checks: the jump on load was a smooth scroll that the browser cancelled while loading, so the page stayed at the top. Fixed with an instant jump plus one repeat after the load event. After the fix 524 of 524 passed. Not tested: a real phone, Safari.
- **Reviewed text, by hand.** The first ledger lines for this section were set by script. They were all reviewed again on 2026-11-11, one by one, against the figure, the table and the quote text in the sources, not only the 20 new ones. The table below has the verdict and basis for all 53 texts. The review found and fixed these:
  - Four table claims had no quote that contained them: prompt attack check "blocks" (new V127), harm controls "cannot be deleted" (V128), approval "every call" (V129), Copilot Studio "blocks attacks" (V130).
  - Layer 5 was headed "same for every client" but listed Foundry only lines (VM sandbox, Network control). The header is gone and the lines now say Foundry only or Agent 365 path only. The section goal and the figure description were fixed to match.
  - Layer 6 and its description stated "only the gateway can call it" as fact. It is a design target, now ledgered as `requirement` and worded that way.
  - "No reply in 1 s: allowed" now says by default (V114). "per tool call (VS Code)" overstated V115 and now says if a call needs approval, documented for VS Code.
  - Copilot Studio prompt attack protection: the source names no layer. The figure and table now say the layer is interpretation by AI (AI estimate).
  - Verdict corrections: `allowed_tools list` and `require_approval` are `code token`, not `label`.
  The label checker counts 135 distinct texts, 0 missing, 0 stale. That proves only that each text has a verdict. The review itself is the table.

| Text (start) | Verdict | Basis |
| --- | --- | --- |
| 1 USER INPUT | label | Layer name. Order of layers is the call path, interpretation by AI. |
| 2 WHICH SERVER | label | Layer name. |
| 3 PERSON APPROVES | label | Layer name. |
| 4 CALL CONTENT | label | Layer name. |
| 5 NETWORK AND GATEWAY | label | Layer name. Old suffix 'same for every client' removed: the layer lists Foundry only lines, so it was wrong. |
| 6 COMPANY MCP SERVER | label | Layer name. |
| 7 TOOL RESPONSE | label | Layer name. |
| 8 FINAL ANSWER | label | Layer name. |
| FOUNDRY AGENT | label | Column title. |
| VS CODE, GITHUB COPILOT | label | Column title. Rows cover VS Code (V115) and GitHub Copilot managed settings (V14, V16, V19). |
| GUARDRAILS ALONG ONE MCP TOOL CALL (request goes down, response comes  | label | Figure title. |
| Guardrails by layer | label | Section heading. |
| What each guardrail does | label | Table heading. |
| response comes back | label | Arrow caption. |
| (Preview) | label | Status marker. Foundry tool call and response V102, V103. Copilot Studio threat detection V112. Defender Foundry V117, Copilot Studio V119. |
| Preview only | label | Released-only path marker for features that are preview (V102, V103, V112, V113). |
| Preview: tool threat protection | label | Name of a preview gateway control from the design above (Controls: tool threat protection, V58, V59). |
| unverified | label | Badge for the None found note. Defined by the sentence next to it. |
| None found | label | Gap marker. Now only Copilot Studio at layer 7. Not proof that no guardrail exists. Explained under the figure. |
| Not stated | label | Gap marker. The source gives no layer (V111). |
| (see below) | label | Points to the ANY LAYER line under the figure. |
| ANY LAYER: Copilot Studio content moderation. The sources checked do n | label | Names a gap: no layer stated. V111. |
| Harm levels | label | Name of a control. V98. Cannot be deleted, only overridden: V128. |
| Prompt attack check | label | Name of a control. V97. Blocks the input: V127. |
| Protected material (flag) | label | Name of a control. Annotate only, with a flag: V99, V126. |
| allowed_tools list | code token | Parameter name. V69. |
| (empty = all tools) | code token | Qualifier of allowed_tools. V69. |
| require_approval | code token | Parameter name. V106. |
| (default: always) | label | V106. Meaning (developer approves every call): V129. |
| Tool call guardrail | label | Name of a preview intervention point. V102. |
| Tool response guardrail | label | Name of a preview intervention point. V103. |
| MCP is not on its list | label | Interpretation by AI: the supported-tool list does not name MCP (V104, V105). The next line says so. |
| (interpretation by AI) | label | Marks the line above as interpretation by AI. Basis: V104, V105. |
| Built-in prompt attack | label | Name of a control. V110. |
| block (UPIA, XPIA) | label | V130 (runtime blocks these attacks), V110 (names UPIA, XPIA). |
| (layer: AI estimate) | label | Says the layer of this control is interpretation by AI. V110 names no layer. |
| Data policy: whole server | label | Summary of V27: blocking connectors blocks the tools of connected MCP servers, per server, not per tool. |
| Threat detection (Preview) | label | Name of a preview control. V112, V113. |
| No reply in 1 s: allowed | label | Summary of V114: the call goes ahead if there is no reply within one second. |
| (by default) | label | Qualifier from V114 ('by default'). |
| Defender rule (Preview) | label | Name of a preview control. Foundry layers 1, 4, 7, 8: V117, V118. Copilot Studio layer 4: V119, V120. |
| Allow and deny lists | label | Name of a control. V14, V16, V19. |
| (policy, managed settings) | label | Where the lists are set: VS Code policy (V14, V16), GitHub managed settings (V19, V131). |
| Confirmation dialog | label | Name of a control. V115, V151. |
| Every client, from the design above: | requirement | Design target. The design above applies to every client behind the gateway. Not a product claim. |
| Outbound rules, then API Management: check identity, authorize, limit  | requirement | Design target from the main design. Not a product claim. |
| Agent 365 path only: Defender rule checks tool calls to MCP tools onbo | label | Summary of V121, V122. Marked 'only' because it applies to that path alone. |
| Foundry only: hosted agents run in a VM sandbox | label | Summary of V109 (per-session VM-isolated sandboxes). Marked Foundry only. |
| Foundry only: Network control limits outbound traffic for hosted and C | label | Summary of V101. Marked Foundry only. |
| Design target: only the gateway can call it. See the design above | requirement | Design target. It was a `label` before this review. Corrected. |
| GitHub content filter | label | Name of a control. V161: Copilot Chat may include a content filter that scans prompts and responses. |
| may scan prompts | label | V161 says 'may', at layer 1. Weak wording kept on purpose. |
| may scan answers | label | V161 says 'may', at layer 8. |
| (source says 'may') | label | Qualifier. V161 uses 'At times' and 'may'. Interpretation by AI: not a control to count on. |
| Server trust prompt | label | Name of a control. V158. |
| Can be set to never | label | V136: a list of tools can skip approval, and require_approval takes never. |
| Ask user before running | label | Name of a tool setting. V137. |
| Off by default | label | V137: the option is off by default. |
| (for MCP: unverified) | label | Marks a gap. V137 covers tools in general, V159 names supported tools. Not checked for MCP tools. |
| (default: Manual) | label | V151: Manual permissions is the default level and asks for confirmation. |
| Allow all skips it | label | V152: Allow all runs all tool calls without confirmation. |
| Policy can lock it | label | V156 (policy turns off global auto-approval), V157 (managed setting disables Allow all). Not tested on a managed device. |
| preToolUse hook can deny | label | V159. V160: hooks are not a substitute for enforced permissions or enterprise controls. |
| Result review before it | label | First half of a two-line cell. V154, V155. |
| enters the chat context | label | Second half. V154: post-approval adds the result to the chat context without review. |
| Can be switched off | label | V154: post-approval skips the review. |
| FOUNDRY: agent guardrails (Preview). With none set, the agent uses its | label | V134 (preview), V135 (inherits the guardrail of the model deployment). |
| VS CODE: Defender for Endpoint runtime protection (Preview, Windows).  | label | Preview path only. V146, V148, V149, V150. No layer stated for this client. |
| Guardrails by layer for one MCP tool call, in three columns: Foundry a | label | Text alternative of the figure, both paths. Rewritten and read sentence by sentence against the new figures on 2026-11-11 (second pass). Each sentence restates one cell that has a row above. |

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

## Built-in GitHub MCP server, check of 2026-11-09 (latest)

A pasted answer said three things could block the built-in GitHub MCP server. I fetched the cited pages on 2026-11-09 and compared each claim.

- "Registry only blocks the built-in server if it is left off the list": not supported. The GitHub page says "Only servers from the registry may run, so users can't use Copilot connectors" and never mentions the built-in server. The same docs call the registry method a "Public preview, not prioritized for development" and say users can bypass it by editing configuration files. Verdict: not shown, low weight.
- "The MCP servers in Copilot policy turns off all MCP": supported as written ("defines whether MCP servers can run at all across Copilot clients"). The docs do not say whether it also turns off the built-in server. It also stops every approved server, so it is not a targeted control. Verdict: possible, untested.
- "A VS Code `deniedMcpServers` entry with `serverUrl: github-mcp-server` blocks it": not supported. The VS Code page shows `deniedMcpServers` with full URLs, and `github-mcp-server` is not a URL. The GitHub reference says first-party servers "are exempt from deny rules and cannot be blocked", and the allowlist page says built-in default servers are always allowed first. Verdict: contradicted by the sources, not tried in a client.
- Page change: the gap and open question 5 now say the allow and deny lists cannot block it (V21 and the new V92), name the two untested switches, and no longer say "client policy cannot block it" in general. Five quotes added (V92 to V96); the checker reports 96 quotes, 0 problems on live pages.
- Not tested: no client was tried with any of these settings.

## Live verification pass, 2026-11-08 (latest, supersedes counts above)

- Network worked this time. The quote checker fetched every source: 90 of 91 quotes matched word for word on the live pages (V1 to V79, V81 to V91). V80 (Microsoft Ignite blog) returns HTTP 403 to curl, the fetch tool and a fetch agent. It was read in the built-in browser: the passage "API Management brings policy-driven governance for MCP endpoints (GA)" is on the page, dated Nov 18, 2025 (matches the page date). That text was copied from the browser into the checker's cache for V80, and the checker then reported 91 quotes, 0 problems. V80 is therefore verified by browser text, not by a script fetch.
- All 22 Microsoft Learn page dates match "Last updated on" in the live pages. The other sources show no date.
- Context re-read for claims that go beyond a quote: Intune default outbound block (setting is "Block outbound connections", default allows), Windows-only; AI Gateway preview regions (exactly East US 2 and Sweden Central); GitHub managed settings file lives in the `.github-private` repository and refreshes within about an hour; ACP supports MCP server-level blocking, not custom or HTTP connectors, which stay on classic data policies; Foundry gateway routing covers new portal tools only; tool threat protection modes are set in Defender, not at the gateway; post-call denial cannot undo the call. All match the page.
- One wording gap found and fixed: the page said individual-tool control needs the AI Gateway tier, but the quote cited (V37) says only "on supported tiers". Added V91, "This capability is only available for MCP Servers registered in the AI Gateway tier in Azure API Management service." and cited it. The cell was trimmed to stay under 60 words.
- Ledger repaired: 4 new page texts given verdicts (lead line, open question 5 and its `inference` tag), 6 stale entries removed. Label check: 81 distinct texts pass.
- Static checks: 91 evidence rows and anchors, no duplicate IDs, no dead in-page links, no en or em dashes.
- Browser (localhost, 2026-11-08): both paths at 375px, page 375 wide, no console errors, 50 evidence rows on Released only and 91 with preview. Dark mode at 375px: page 375 wide, no console errors, no text under 4.5:1 contrast. Real mouse clicks: the Released only and With preview buttons switch the path and the URL (`?path=preview`); a quote link opened Microsoft Learn and scrolled to the quoted passage.
- Still untested: nothing was built or run in a tenant. The acceptance tests on the page read "Not run" on purpose. They are design targets, and the page says so. They cannot pass or fail until a tenant exists.

## Method

Each product claim in the page has a quote in `scripts/mcp_governance_evidence.py`. `scripts/check-evidence-quotes.py` fetches each source and confirms the quote appears word for word. The page lists every quote and links it with a text fragment.

## Current claim audit, 2026-11-08

- Reopened the Microsoft Learn sources for Power Platform advanced connector policies, the programmatic policy tutorial, API Management MCP governance, Agent 365 gateway and BYO server routes, Foundry networking and gateway routing, API Management MCP features, GitHub managed settings and firewall, Global Secure Access, Intune firewall policy, Windows Firewall dynamic keywords, Azure Functions networking, and tool threat protection. Reopened the MCP transport specification for the stdio wording.
- Corrected the Power Platform scope. Advanced connector policies support MCP connectors for server-level blocking, but not individual MCP tools (pp-block). Certified connectors are supported; custom and HTTP connector types are not (pp-certified, pp-custom). The previous broad wording that policies cover certified connectors only is superseded because the current page lists MCP connectors separately as supported.
- Replaced V77's quote with the supported-connector table wording, "First-party and certified third-party connectors." The source also has a broader certified-only limitation, but separately lists MCP connectors as supported. This avoids presenting the ambiguous phrase without that context.
- Separated two Agent 365 routes. The API Management integration discovers MCP servers registered with the connected gateway and can block servers and, on supported tiers, tools (pv-disc, pv-a365-ctrl). Its no-auto-routing limit is now scoped to that integration. The BYO route uses developer registration and admin approval, requires a publicly accessible server endpoint, supports four client surfaces during preview, and has BYO tool-level blocking planned for a future release (pv-byo-route, pv-byo-approval, pv-byo-endpoint, pv-byo-surf, pv-byo-tool-plan). The previous wording that treated BYO tool blocking as rolling out for that route is superseded.
- Removed the unsupported idea that the pipeline syncs a fourth server list to Agent 365. The API Management integration discovers gateway registrations; BYO servers use their separate registration flow. The page no longer describes either as a pipeline write.
- Tightened the GitHub cloud firewall statement to its documented scope: it does not directly control MCP server processes (gh-fw). Replaced the stdio inference with the specification's transport description: a client launches a subprocess, and stdio communicates over standard input and standard output (stdio, stdio-io). Client and endpoint controls remain design requirements.
- Clarified that the repository list and pipeline apply Objective B, while backend isolation for Objective A is separate. Described Azure AI Gateway as a separate preview resource type, not a separate product. **Superseded 2026-11-11:** current Microsoft documentation describes AI Gateway as a dedicated product distinct from AI gateway capabilities in the API Management service. Preview test steps now name the API Management integration they cover.
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

## Source quotes

<!-- Begin source quotes -->
Generated by `scripts/build-mcp-governance.py`. Do not edit by hand. 202 quotes, checked 2026-11-11: 128 back the released-only design and 74 back the preview additions. Links request the quoted passage with browser text fragments. Page date is the date the source page shows.

| Id | Quote | Source | Page date | Design |
|---|---|---|---|---|
| <a id="ev-V1"></a>V1 | consider placing it behind Azure API Management (APIM) as an enforcement gateway | [Microsoft Learn, Azure MCP Server security](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security#:~:text=consider%20placing%20it%20behind%20Azure%20API%20Management%20%28APIM%29%20as%20an%20enforcement%20gateway) | 2026-07-31 | released |
| <a id="ev-V2"></a>V2 | APIM can validate Entra ID tokens before requests reach your Azure MCP Server | [Microsoft Learn, Azure MCP Server security](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security#:~:text=APIM%20can%20validate%20Entra%20ID%20tokens%20before%20requests%20reach%20your%20Azure%20MCP%20Server) | 2026-07-31 | released |
| <a id="ev-V3"></a>V3 | Use APIM policies to limit how often callers can make requests, restrict allowed tool paths, and log every request for audit purposes. | [Microsoft Learn, Azure MCP Server security](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security#:~:text=Use%20APIM%20policies%20to%20limit%20how,log%20every%20request%20for%20audit%20purposes.) | 2026-07-31 | released |
| <a id="ev-V4"></a>V4 | A gateway provides a single choke point for access control and observability across multiple downstream MCP tools. | [Microsoft Learn, Azure MCP Server security](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security#:~:text=A%20gateway%20provides%20a%20single%20choke,observability%20across%20multiple%20downstream%20MCP%20tools.) | 2026-07-31 | released |
| <a id="ev-V5"></a>V5 | When using APIM, route clients through the gateway so the backing endpoint can't be silently redirected. | [Microsoft Learn, Azure MCP Server security](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security#:~:text=When%20using%20APIM%2C%20route%20clients%20through,be%20silently%20redirected.) | 2026-07-31 | released |
| <a id="ev-V6"></a>V6 | MCP clients can present OAuth tokens or JWTs issued by Microsoft Entra ID by using an Authorization header and validated by API Management. | [Microsoft Learn, secure access to MCP servers in API Management](https://learn.microsoft.com/en-us/azure/api-management/secure-mcp-servers#:~:text=MCP%20clients%20can%20present%20OAuth%20tokens,header%20and%20validated%20by%20API%20Management.) | 2026-09-11 | released |
| <a id="ev-V7"></a>V7 | MCP clients can present the key in incoming requests, and API Management validates the key. | [Microsoft Learn, secure access to MCP servers in API Management](https://learn.microsoft.com/en-us/azure/api-management/secure-mcp-servers#:~:text=MCP%20clients%20can%20present%20the%20key,and%20API%20Management%20validates%20the%20key.) | 2026-09-11 | released |
| <a id="ev-V8"></a>V8 | Use the authentication-managed-identity policy to authenticate with a backend service using the managed identity. | [Microsoft Learn, API Management authentication-managed-identity policy](https://learn.microsoft.com/en-us/azure/api-management/authentication-managed-identity-policy#:~:text=Use%20the%20authentication%2Dmanaged%2Didentity%20policy%20to%20authenticate,backend%20service%20using%20the%20managed%20identity.) | 2026-10-22 | released |
| <a id="ev-V9"></a>V9 | To prevent direct access, restrict MCP server connectivity so the gateway is the only permitted caller or use private networking or network-level access controls when supported. | [Microsoft Learn, API Management with Agent 365](https://learn.microsoft.com/en-us/azure/api-management/agent-365#:~:text=To%20prevent%20direct%20access%2C%20restrict%20MCP,or%20network%2Dlevel%20access%20controls%20when%20supported.) | 2026-10-06 | released |
| <a id="ev-V10"></a>V10 | Microsoft Agent 365 doesn't automatically route agents through a customer-hosted gateway. | [Microsoft Learn, API Management with Agent 365](https://learn.microsoft.com/en-us/azure/api-management/agent-365#:~:text=Microsoft%20Agent%20365,route%20agents%20through%20a%20customer%2Dhosted%20gateway.) | 2026-10-06 | released |
| <a id="ev-V11"></a>V11 | To keep the public endpoint and allow or deny selected sources, use inbound access restrictions | [Microsoft Learn, Azure Functions networking options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options#:~:text=To%20keep%20the%20public%20endpoint%20and,selected%20sources%2C%20use%20inbound%20access%20restrictions) | 2026-09-16 | released |
| <a id="ev-V12"></a>V12 | To expose the app through a private IP address in your virtual network, use a private endpoint | [Microsoft Learn, Azure Functions networking options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options#:~:text=To%20expose%20the%20app%20through%20a,virtual%20network%2C%20use%20a%20private%20endpoint) | 2026-09-16 | released |
| <a id="ev-V13"></a>V13 | Private endpoints aren't supported on the Consumption plan | [Microsoft Learn, Azure Functions networking options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options#:~:text=Private%20endpoints,supported%20on%20the%20Consumption%20plan) | 2026-09-16 | released |
| <a id="ev-V14"></a>V14 | When set, only servers matching an entry may be installed or run; omit entirely to allow all servers (subject to the deny list). | [VS Code Docs, enterprise policies](https://code.visualstudio.com/docs/enterprise/policies#:~:text=When%20set%2C%20only%20servers%20matching%20an,servers%20%28subject%20to%20the%20deny%20list%29.) | none shown | released |
| <a id="ev-V15"></a>V15 | Use only the enterprise-managed MCP allowlist when deciding which servers may run. | [VS Code Docs, enterprise policies](https://code.visualstudio.com/docs/enterprise/policies#:~:text=Use%20only%20the%20enterprise%2Dmanaged%20MCP%20allowlist%20when%20deciding%20which%20servers%20may%20run.) | none shown | released |
| <a id="ev-V16"></a>V16 | Servers matching any entry are blocked from being installed or run, even if they also match the allow list; deny rules always take precedence. | [VS Code Docs, enterprise policies](https://code.visualstudio.com/docs/enterprise/policies#:~:text=Servers%20matching%20any%20entry%20are%20blocked,list%3B%20deny%20rules%20always%20take%20precedence.) | none shown | released |
| <a id="ev-V17"></a>V17 | Supports &#42; wildcards for subdomains or path prefixes | [GitHub Docs, enterprise managed settings reference](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings#:~:text=Supports%20%2A%20wildcards%20for%20subdomains%20or%20path%20prefixes) | none shown | released |
| <a id="ev-V18"></a>V18 | Matches the exact command and each argument for a local server | [GitHub Docs, enterprise managed settings reference](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings#:~:text=Matches%20the%20exact%20command%20and%20each%20argument%20for%20a%20local%20server) | none shown | released |
| <a id="ev-V19"></a>V19 | any MCP server that doesn't match an entry is blocked | [GitHub Docs, configure the enterprise MCP allowlist](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-enterprise-allowlist#:~:text=any%20MCP%20server%20that,match%20an%20entry%20is%20blocked) | none shown | released |
| <a id="ev-V20"></a>V20 | allowedMcpServers and deniedMcpServers apply to MCP servers defined in user settings and repository settings, but don't apply to MCP servers defined in repository custom agent profiles. | [GitHub Docs, enterprise managed settings reference](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings#:~:text=allowedMcpServers%20and%20deniedMcpServers%20apply%20to%20MCP,defined%20in%20repository%20custom%20agent%20profiles.) | none shown | released |
| <a id="ev-V21"></a>V21 | First-party Copilot servers, such as the built-in GitHub MCP server, are exempt from deny rules and cannot be blocked. | [GitHub Docs, enterprise managed settings reference](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings#:~:text=First%2Dparty%20Copilot%20servers%2C%20such%20as%20the,deny%20rules%20and%20cannot%20be%20blocked.) | none shown | released |
| <a id="ev-V22"></a>V22 | Coverage of policies and enterprise managed settings currently varies between environments. | [GitHub Docs, enterprise managed settings reference](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings#:~:text=Coverage%20of%20policies%20and%20enterprise%20managed,managed%20settings%20currently%20varies%20between%20environments.) | none shown | released |
| <a id="ev-V23"></a>V23 | It does not apply directly to Model Context Protocol (MCP) server processes or processes started in configured Copilot setup steps. | [GitHub Docs, customize the Copilot cloud agent firewall](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-firewall#:~:text=It%20does%20not%20apply%20directly%20to,started%20in%20configured%20Copilot%20setup%20steps.) | none shown | released |
| <a id="ev-V24"></a>V24 | The networking configuration of the Microsoft Foundry project that hosts the toolbox governs all network access. | [Microsoft Learn, network isolation for a Foundry toolbox](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/toolbox-network-isolation#:~:text=The%20networking%20configuration%20of%20the%20Microsoft,the%20toolbox%20governs%20all%20network%20access.) | 2026-10-26 | released |
| <a id="ev-V25"></a>V25 | agents reach the toolbox MCP endpoint through the project's private endpoint. | [Microsoft Learn, network isolation for a Foundry toolbox](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/toolbox-network-isolation#:~:text=agents%20reach%20the%20toolbox%20MCP%20endpoint,private%20endpoint.) | 2026-10-26 | released |
| <a id="ev-V26"></a>V26 | Tool connectivity depends on where the downstream service is hosted. | [Microsoft Learn, network isolation for a Foundry toolbox](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/toolbox-network-isolation#:~:text=Tool%20connectivity%20depends%20on%20where%20the%20downstream%20service%20is%20hosted.) | 2026-10-26 | released |
| <a id="ev-V27"></a>V27 | Blocking Power Platform connectors also blocks access to tools in connected MCP servers, which rely on Power Platform connectors for connectivity. | [Microsoft Learn, Copilot Studio data loss prevention](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention#:~:text=Blocking%20Power%20Platform%20connectors%20also%20blocks,on%20Power%20Platform%20connectors%20for%20connectivity.) | 2026-10-22 | released |
| <a id="ev-V28"></a>V28 | The client launches the MCP server as a subprocess. | [Model Context Protocol specification 2025-06-18, transports](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#:~:text=The%20client%20launches%20the%20MCP%20server%20as%20a%20subprocess.) | none shown | released |
| <a id="ev-V29"></a>V29 | The MCP firewall is currently in preview. | [Microsoft Learn, Global Secure Access MCP firewall](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-mcp-firewall#:~:text=The%20MCP%20firewall%20is%20currently%20in%20preview.) | 2026-08-06 | preview |
| <a id="ev-V30"></a>V30 | Create allow-lists or deny-lists of MCP servers based on server URL patterns. | [Microsoft Learn, Global Secure Access MCP firewall](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-mcp-firewall#:~:text=Create%20allow%2Dlists%20or%20deny%2Dlists%20of%20MCP%20servers%20based%20on%20server%20URL%20patterns.) | 2026-08-06 | preview |
| <a id="ev-V31"></a>V31 | Only remote MCP servers are inspected. Local MCP servers that run on a device aren't visible to Global Secure Access. JSON-RPC batches aren't inspected. | [Microsoft Learn, Global Secure Access MCP firewall](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-mcp-firewall#:~:text=Only%20remote%20MCP%20servers%20are%20inspected.,inspected.) | 2026-08-06 | preview |
| <a id="ev-V32"></a>V32 | All outbound connections that don't match an outbound rule are blocked. | [Microsoft Learn, Intune endpoint security firewall settings](https://learn.microsoft.com/en-us/intune/device-configuration/endpoint-security/ref-firewall-settings#:~:text=All%20outbound%20connections%20that,match%20an%20outbound%20rule%20are%20blocked.) | 2026-04-15 | released |
| <a id="ev-V33"></a>V33 | The default configuration of Blocked for Outbound rules can be considered for certain highly secure environments. | [Microsoft Learn, Windows Firewall dynamic keywords](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/dynamic-keywords#:~:text=The%20default%20configuration%20of%20Blocked%20for,considered%20for%20certain%20highly%20secure%20environments.) | 2025-04-07 | released |
| <a id="ev-V34"></a>V34 | Limitations include: websites accessed via proxy, secure DNS services, certain VPN tunnel configurations, cached IPs on the endpoint | [Microsoft Learn, Windows Firewall dynamic keywords](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/dynamic-keywords#:~:text=Limitations%20include%3A%20websites%20accessed%20via%20proxy%2C,configurations%2C%20cached%20IPs%20on%20the%20endpoint) | 2025-04-07 | released |
| <a id="ev-V35"></a>V35 | Preview features aren't meant for production use and might have restricted functionality. | [Microsoft Learn, Agent 365 tools gateway](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-tools-gateway#:~:text=Preview%20features,use%20and%20might%20have%20restricted%20functionality.) | 2026-11-06 | preview |
| <a id="ev-V36"></a>V36 | Connect Azure AI Gateway or a LiteLLM gateway to Microsoft Agent 365 to discover and govern the Model Context Protocol (MCP) servers registered with the gateway. | [Microsoft Learn, Agent 365 tools gateway](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-tools-gateway#:~:text=Connect%20Azure%20AI%20Gateway%20or%20a,%28MCP%29%20servers%20registered%20with%20the%20gateway.) | 2026-11-06 | preview |
| <a id="ev-V37"></a>V37 | Block or unblock MCP servers. Control access to individual tools on supported tiers. | [Microsoft Learn, API Management with Agent 365](https://learn.microsoft.com/en-us/azure/api-management/agent-365#:~:text=Block%20or%20unblock%20MCP%20servers.%20Control%20access%20to%20individual%20tools%20on%20supported%20tiers.) | 2026-10-06 | preview |
| <a id="ev-V38"></a>V38 | To enable tool-level controls from Microsoft Agent 365, ensure each MCP server has a static list of allowed tools configured | [Microsoft Learn, API Management with Agent 365](https://learn.microsoft.com/en-us/azure/api-management/agent-365#:~:text=To%20enable%20tool%2Dlevel%20controls%20from%20Microsoft,static%20list%20of%20allowed%20tools%20configured) | 2026-10-06 | preview |
| <a id="ev-V39"></a>V39 | A customer administrator grants the A365 MCP Gateway Policy Operator Azure role at the tenant level with a one-time consent. | [Microsoft Learn, API Management with Agent 365](https://learn.microsoft.com/en-us/azure/api-management/agent-365#:~:text=A%20customer%20administrator%20grants%20the%20A365,tenant%20level%20with%20a%20one%2Dtime%20consent.) | 2026-10-06 | preview |
| <a id="ev-V40"></a>V40 | Read API-scoped policies. Write API-scoped policies. | [Microsoft Learn, API Management with Agent 365](https://learn.microsoft.com/en-us/azure/api-management/agent-365#:~:text=Read%20API%2Dscoped%20policies.%20Write%20API%2Dscoped%20policies.) | 2026-10-06 | preview |
| <a id="ev-V41"></a>V41 | Azure API Management v1 tiers aren't supported. | [Microsoft Learn, API Management with Agent 365](https://learn.microsoft.com/en-us/azure/api-management/agent-365#:~:text=Azure%20API%20Management%20v1%20tiers,supported.) | 2026-10-06 | preview |
| <a id="ev-V42"></a>V42 | Azure API Management v2 tiers don't support tool-level access control or Tool threat protection policies | [Microsoft Learn, API Management with Agent 365](https://learn.microsoft.com/en-us/azure/api-management/agent-365#:~:text=Azure%20API%20Management%20v2%20tiers,control%20or%20Tool%20threat%20protection%20policies) | 2026-10-06 | preview |
| <a id="ev-V43"></a>V43 | Supported client surfaces during preview are Copilot Studio, Visual Studio Code, Claude Code, and GitHub Copilot CLI. Azure AI Foundry and Microsoft 365 Declarative Agents aren't supported. | [Microsoft Learn, Agent 365 bring-your-own MCP server](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-byo-mcp-server#:~:text=Supported%20client%20surfaces%20during%20preview%20are,supported.) | 2026-11-05 | preview |
| <a id="ev-V44"></a>V44 | An admin can allow or block individual tools within a BYO server instead of the whole server. This capability is rolling out for supported MCP servers registered on Agent 365. Support for BYO MCP servers is planned for a future release. | [Microsoft Learn, Agent 365 bring-your-own MCP server](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-byo-mcp-server#:~:text=An%20admin%20can%20allow%20or%20block,is%20planned%20for%20a%20future%20release.) | 2026-11-05 | preview |
| <a id="ev-V45"></a>V45 | Starting October 14, 2026, Azure API management is changing the resource type for AI Gateway (preview) from Microsoft.ApiManagement/service to Microsoft.ApiManagement/aigateways | [Microsoft Learn, AI Gateway resource type change](https://learn.microsoft.com/en-us/azure/ai-gateway/ai-gateway-resource#:~:text=Starting%20October%2014%2C%202026%2C%20Azure%20API,Gateway%20%28preview%29%20from%20Microsoft.ApiManagement%2Fservice%20to%20Microsoft.ApiManagement%2Faigateways) | 2026-10-28 | preview |
| <a id="ev-V46"></a>V46 | Complete the migration before January 15, 2027. | [Microsoft Learn, AI Gateway resource type change](https://learn.microsoft.com/en-us/azure/ai-gateway/ai-gateway-resource#:~:text=Complete%20the%20migration%20before%20January%2015%2C%202027.) | 2026-10-28 | preview |
| <a id="ev-V47"></a>V47 | Private endpoints aren't supported. | [Microsoft Learn, AI Gateway resource type change](https://learn.microsoft.com/en-us/azure/ai-gateway/ai-gateway-resource#:~:text=Private%20endpoints,supported.) | 2026-10-28 | preview |
| <a id="ev-V48"></a>V48 | You can't change the virtual network or subnet after the gateway is created. | [Microsoft Learn, AI Gateway resource type change](https://learn.microsoft.com/en-us/azure/ai-gateway/ai-gateway-resource#:~:text=You,subnet%20after%20the%20gateway%20is%20created.) | 2026-10-28 | preview |
| <a id="ev-V49"></a>V49 | Content safety policy isn't supported. | [Microsoft Learn, AI Gateway resource type change](https://learn.microsoft.com/en-us/azure/ai-gateway/ai-gateway-resource#:~:text=Content%20safety%20policy,supported.) | 2026-10-28 | preview |
| <a id="ev-V50"></a>V50 | Applications receive a new runtime URL with the domain ai.gateway.azure.com | [Microsoft Learn, AI Gateway resource type change](https://learn.microsoft.com/en-us/azure/ai-gateway/ai-gateway-resource#:~:text=Applications%20receive%20a%20new%20runtime%20URL%20with%20the%20domain%20ai.gateway.azure.com) | 2026-10-28 | preview |
| <a id="ev-V51"></a>V51 | authenticating by using keys should use the Authorization header with a Bearer scheme | [Microsoft Learn, AI Gateway resource type change](https://learn.microsoft.com/en-us/azure/ai-gateway/ai-gateway-resource#:~:text=authenticating%20by%20using%20keys%20should%20use%20the%20Authorization%20header%20with%20a%20Bearer%20scheme) | 2026-10-28 | preview |
| <a id="ev-V52"></a>V52 | During public preview, AI Gateway is available in the following regions: United States - East US 2 Europe - Sweden Central | [Microsoft Learn, AI Gateway concepts](https://learn.microsoft.com/en-us/azure/ai-gateway/concepts#:~:text=During%20public%20preview%2C%20AI%20Gateway%20is,US%202%20Europe%20%2D%20Sweden%20Central) | 2026-10-28 | preview |
| <a id="ev-V53"></a>V53 | Tool threat protection requires a delegated Microsoft Entra ID user token. | [Microsoft Learn, Protect tool calls with tool threat protection in AI Gateway (preview)](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-policy-tool-threat#:~:text=Tool%20threat%20protection%20requires%20a%20delegated%20Microsoft%20Entra%20ID%20user%20token.) | 2026-10-28 | preview |
| <a id="ev-V54"></a>V54 | App-only service-to-service calls aren't supported because OBO requires a delegated user token. | [Microsoft Learn, Protect tool calls with tool threat protection in AI Gateway (preview)](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-policy-tool-threat#:~:text=App%2Donly%20service%2Dto%2Dservice%20calls,OBO%20requires%20a%20delegated%20user%20token.) | 2026-10-28 | preview |
| <a id="ev-V55"></a>V55 | the system fails open to prevent user disruption while logging the behavior | [Microsoft Learn, Protect tool calls with tool threat protection in AI Gateway (preview)](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-policy-tool-threat#:~:text=the%20system%20fails%20open%20to%20prevent%20user%20disruption%20while%20logging%20the%20behavior) | 2026-10-28 | preview |
| <a id="ev-V56"></a>V56 | This mode behaves strictly as a fail-close mechanism. | [Microsoft Learn, Protect tool calls with tool threat protection in AI Gateway (preview)](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-policy-tool-threat#:~:text=This%20mode%20behaves%20strictly%20as%20a%20fail%2Dclose%20mechanism.) | 2026-10-28 | preview |
| <a id="ev-V57"></a>V57 | Microsoft Defender or Microsoft Purview license. | [Microsoft Learn, Protect tool calls with tool threat protection in AI Gateway (preview)](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-policy-tool-threat#:~:text=Microsoft%20Defender%20or%20Microsoft%20Purview%20license.) | 2026-10-28 | preview |
| <a id="ev-V58"></a>V58 | The policy applies to every tool and caller that uses that server. You can't configure it at gateway scope or for an individual tool. | [Microsoft Learn, Protect tool calls with tool threat protection in AI Gateway (preview)](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-policy-tool-threat#:~:text=The%20policy%20applies%20to%20every%20tool,scope%20or%20for%20an%20individual%20tool.) | 2026-10-28 | preview |
| <a id="ev-V59"></a>V59 | A post-invocation denial can't undo actions that the tool already completed. | [Microsoft Learn, Protect tool calls with tool threat protection in AI Gateway (preview)](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-policy-tool-threat#:~:text=A%20post%2Dinvocation%20denial,actions%20that%20the%20tool%20already%20completed.) | 2026-10-28 | preview |
| <a id="ev-V60"></a>V60 | This feature is in preview. Only new MCP tools created in the Foundry portal that don't use managed OAuth are routed through an AI gateway. | [Microsoft Learn, Foundry tools governance](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/governance#:~:text=This%20feature%20is%20in%20preview.%20Only,are%20routed%20through%20an%20AI%20gateway.) | 2026-08-19 | preview |
| <a id="ev-V61"></a>V61 | Gateway routing is applied only at tool creation. Existing tools aren't automatically mediated with AI gateways. | [Microsoft Learn, Foundry tools governance](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/governance#:~:text=Gateway%20routing%20is%20applied%20only%20at,automatically%20mediated%20with%20AI%20gateways.) | 2026-08-19 | preview |
| <a id="ev-V62"></a>V62 | Combine tools from remote MCP servers, OpenAPI-described APIs, and built-in connectors behind gateway MCP endpoints. | [Microsoft Learn, AI Gateway overview](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-overview#:~:text=Combine%20tools%20from%20remote%20MCP%20servers%2C,built%2Din%20connectors%20behind%20gateway%20MCP%20endpoints.) | 2026-10-28 | preview |
| <a id="ev-V63"></a>V63 | Expose your existing REST APIs as MCP servers, and support passthrough to MCP servers. | [Microsoft Learn, API Management AI gateway capabilities](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities#:~:text=Expose%20your%20existing%20REST%20APIs%20as%20MCP%20servers%2C%20and%20support%20passthrough%20to%20MCP%20servers.) | 2026-05-29 | released |
| <a id="ev-V64"></a>V64 | Capability availability varies by API Management service tier. | [Microsoft Learn, API Management AI gateway capabilities](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities#:~:text=Capability%20availability%20varies%20by%20API%20Management%20service%20tier.) | 2026-05-29 | released |
| <a id="ev-V65"></a>V65 | administrators can see MCP servers listed alongside other connector types and can choose to block an entire MCP server. As of now, granular control over individual MCP tools (endpoints and actions) within an MCP server isn't available. | [Microsoft Learn, Power Platform advanced connector policies](https://learn.microsoft.com/en-us/power-platform/admin/advanced-connector-policies#:~:text=administrators%20can%20see%20MCP%20servers%20listed,available.) | 2026-09-09 | released |
| <a id="ev-V66"></a>V66 | The Power Platform API provides publicly documented APIs so you can build automated scenarios such as creating new policies, updating policies, and moving environments into groups for management at scale. | [Microsoft Learn, Power Platform advanced connector policies](https://learn.microsoft.com/en-us/power-platform/admin/advanced-connector-policies#:~:text=The%20Power%20Platform%20API%20provides%20publicly,into%20groups%20for%20management%20at%20scale.) | 2026-09-09 | released |
| <a id="ev-V67"></a>V67 | Automating ACP is useful when you standardize governance across many environment groups, replicate a baseline policy between groups, or manage policies as part of a deployment pipeline. | [Microsoft Learn, manage advanced connector policies programmatically](https://learn.microsoft.com/en-us/power-platform/admin/programmability-tutorial-manage-advanced-connector-policies#:~:text=Automating%20ACP%20is%20useful%20when%20you,as%20part%20of%20a%20deployment%20pipeline.) | 2026-10-02 | released |
| <a id="ev-V68"></a>V68 | A connector that isn't in AllowedConnectorList is blocked (default-deny). | [Microsoft Learn, manage advanced connector policies programmatically](https://learn.microsoft.com/en-us/power-platform/admin/programmability-tutorial-manage-advanced-connector-policies#:~:text=A%20connector%20that,in%20AllowedConnectorList%20is%20blocked%20%28default%2Ddeny%29.) | 2026-10-02 | released |
| <a id="ev-V69"></a>V69 | To restrict tool access, set allowed&#95;tools to a nonempty list of tool names. An empty list ( &#91;&#93; ) allows all tools exposed by the MCP server, not zero tools. | [Microsoft Learn, Foundry MCP tool](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol#:~:text=To%20restrict%20tool%20access%2C%20set%20allowed_tools,the%20MCP%20server%2C%20not%20zero%20tools.) | 2026-10-28 | released |
| <a id="ev-V70"></a>V70 | you hosted your managed settings on GitHub. This is a server-managed deployment. | [GitHub Docs, deploy enterprise managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/deploy-managed-settings#:~:text=you%20hosted%20your%20managed%20settings%20on%20GitHub.%20This%20is%20a%20server%2Dmanaged%20deployment.) | none shown | released |
| <a id="ev-V71"></a>V71 | MCP server management features are available in the following API Management service tiers | [Microsoft Learn, about MCP servers in API Management](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview#:~:text=MCP%20server%20management%20features%20are%20available%20in%20the%20following%20API%20Management%20service%20tiers) | 2026-09-11 | released |
| <a id="ev-V72"></a>V72 | Limit the number of requests per time period to the MCP server's tools, and set usage quotas for clients or subscriptions. | [Microsoft Learn, about MCP servers in API Management](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview#:~:text=Limit%20the%20number%20of%20requests%20per,usage%20quotas%20for%20clients%20or%20subscriptions.) | 2026-09-11 | released |
| <a id="ev-V73"></a>V73 | Require and validate incoming requests by using JSON web tokens (JWT) issued by Microsoft Entra ID or other identity providers for secure access. | [Microsoft Learn, about MCP servers in API Management](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview#:~:text=Require%20and%20validate%20incoming%20requests%20by,other%20identity%20providers%20for%20secure%20access.) | 2026-09-11 | released |
| <a id="ev-V74"></a>V74 | Microsoft Entra runtime access or a gateway runtime API key authorizes applications and agents. | [Microsoft Learn, AI Gateway concepts](https://learn.microsoft.com/en-us/azure/ai-gateway/concepts#:~:text=Microsoft%20Entra%20runtime%20access%20or%20a,API%20key%20authorizes%20applications%20and%20agents.) | 2026-10-28 | preview |
| <a id="ev-V75"></a>V75 | Policies apply shared controls to model and tool traffic, such as consumption limits and tool protection. | [Microsoft Learn, AI Gateway concepts](https://learn.microsoft.com/en-us/azure/ai-gateway/concepts#:~:text=Policies%20apply%20shared%20controls%20to%20model,as%20consumption%20limits%20and%20tool%20protection.) | 2026-10-28 | preview |
| <a id="ev-V76"></a>V76 | Use telemetry to understand model and tool usage and investigate requests. | [Microsoft Learn, AI Gateway overview](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-overview#:~:text=Use%20telemetry%20to%20understand%20model%20and%20tool%20usage%20and%20investigate%20requests.) | 2026-10-28 | preview |
| <a id="ev-V77"></a>V77 | First-party and certified third-party connectors. | [Microsoft Learn, Power Platform advanced connector policies](https://learn.microsoft.com/en-us/power-platform/admin/advanced-connector-policies#:~:text=First%2Dparty%20and%20certified%20third%2Dparty%20connectors.) | 2026-09-09 | released |
| <a id="ev-V78"></a>V78 | Custom connectors and HTTP connectors aren't yet supported. | [Microsoft Learn, Power Platform advanced connector policies](https://learn.microsoft.com/en-us/power-platform/admin/advanced-connector-policies#:~:text=Custom%20connectors%20and%20HTTP%20connectors,yet%20supported.) | 2026-09-09 | released |
| <a id="ev-V79"></a>V79 | With a shared backend connection, authorized callers use the permissions of that connection. | [Microsoft Learn, AI Gateway concepts](https://learn.microsoft.com/en-us/azure/ai-gateway/concepts#:~:text=With%20a%20shared%20backend%20connection%2C%20authorized,use%20the%20permissions%20of%20that%20connection.) | 2026-10-28 | preview |
| <a id="ev-V80"></a>V80 | API Management brings policy-driven governance for MCP endpoints (GA) | [Microsoft Apps on Azure Blog, Ignite 2025](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-app-platform-at-ignite-2025-new-innovations-for-all-your-apps-and-agents/4470759#:~:text=API%20Management%20brings%20policy%2Ddriven%20governance%20for%20MCP%20endpoints%20%28GA%29) | 2025-11-18 | released |
| <a id="ev-V81"></a>V81 | You can also use the API Management self-hosted gateway to manage MCP servers in your own infrastructure. | [Microsoft Learn, about MCP servers in API Management](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview#:~:text=You%20can%20also%20use%20the%20API,MCP%20servers%20in%20your%20own%20infrastructure.) | 2026-09-11 | released |
| <a id="ev-V82"></a>V82 | In the repository, create or update copilot/managed-settings.json | [GitHub Docs, deploy enterprise managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/deploy-managed-settings#:~:text=In%20the%20repository%2C%20create%20or%20update%20copilot%2Fmanaged%2Dsettings.json) | none shown | released |
| <a id="ev-V83"></a>V83 | Commit and push your changes to the default branch. | [GitHub Docs, deploy enterprise managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/deploy-managed-settings#:~:text=Commit%20and%20push%20your%20changes%20to%20the%20default%20branch.) | none shown | released |
| <a id="ev-V84"></a>V84 | Resources of type Microsoft.ApiManagement/service with the AIGateway SKU are permanently removed. | [Microsoft Learn, AI Gateway resource type change](https://learn.microsoft.com/en-us/azure/ai-gateway/ai-gateway-resource#:~:text=Resources%20of%20type%20Microsoft.ApiManagement%2Fservice%20with%20the,the%20AIGateway%20SKU%20are%20permanently%20removed.) | 2026-10-28 | preview |
| <a id="ev-V85"></a>V85 | BYO MCP server addresses this problem by routing registered servers through the Agent 365 Tooling Gateway, giving IT admins control via the Microsoft 365 admin center and security teams the observability data they need. | [Microsoft Learn, Agent 365 bring-your-own MCP server](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-byo-mcp-server#:~:text=BYO%20MCP%20server%20addresses%20this%20problem,teams%20the%20observability%20data%20they%20need.) | 2026-11-05 | preview |
| <a id="ev-V86"></a>V86 | Support for BYO MCP servers is planned for a future release. | [Microsoft Learn, Agent 365 bring-your-own MCP server](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-byo-mcp-server#:~:text=Support%20for%20BYO%20MCP%20servers%20is%20planned%20for%20a%20future%20release.) | 2026-11-05 | preview |
| <a id="ev-V87"></a>V87 | An IT admin reviews the request in the Microsoft 365 admin center and approves or rejects it. | [Microsoft Learn, Agent 365 bring-your-own MCP server](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-byo-mcp-server#:~:text=An%20IT%20admin%20reviews%20the%20request,center%20and%20approves%20or%20rejects%20it.) | 2026-11-05 | preview |
| <a id="ev-V88"></a>V88 | Your MCP server has a publicly accessible endpoint. | [Microsoft Learn, Agent 365 bring-your-own MCP server](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-byo-mcp-server#:~:text=Your%20MCP%20server%20has%20a%20publicly%20accessible%20endpoint.) | 2026-11-05 | preview |
| <a id="ev-V89"></a>V89 | communication over standard in and standard out | [Model Context Protocol specification 2025-06-18, transports](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#:~:text=communication%20over%20standard%20in%20and%20standard%20out) | none shown | released |
| <a id="ev-V90"></a>V90 | Updated settings are applied automatically within about an hour. | [GitHub Docs, deploy enterprise managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/deploy-managed-settings#:~:text=Updated%20settings%20are%20applied%20automatically%20within%20about%20an%20hour.) | none shown | released |
| <a id="ev-V91"></a>V91 | This capability is only available for MCP Servers registered in the AI Gateway tier in Azure API Management service. | [Microsoft Learn, API Management with Agent 365](https://learn.microsoft.com/en-us/azure/api-management/agent-365#:~:text=This%20capability%20is%20only%20available%20for,tier%20in%20Azure%20API%20Management%20service.) | 2026-10-06 | preview |
| <a id="ev-V92"></a>V92 | Always allow built-in default servers, such as the built-in GitHub MCP server. | [GitHub Docs, configure the enterprise MCP allowlist](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-enterprise-allowlist#:~:text=Always%20allow%20built%2Din%20default%20servers%2C%20such%20as%20the%20built%2Din%20GitHub%20MCP%20server.) | none shown | released |
| <a id="ev-V93"></a>V93 | The MCP servers in Copilot policy defines whether MCP servers can run at all across Copilot clients. | [GitHub Docs, MCP server usage in your company](https://docs.github.com/en/copilot/concepts/enterprise/mcp-management#:~:text=The%20MCP%20servers%20in%20Copilot%20policy,run%20at%20all%20across%20Copilot%20clients.) | none shown | released |
| <a id="ev-V94"></a>V94 | Only servers from the registry may run, so users can't use Copilot connectors. | [GitHub Docs, restrict MCP access based on a registry](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/restrict-based-on-registry#:~:text=Only%20servers%20from%20the%20registry%20may,use%20Copilot%20connectors.) | none shown | released |
| <a id="ev-V95"></a>V95 | Public preview, not prioritized for development | [GitHub Docs, MCP server usage in your company](https://docs.github.com/en/copilot/concepts/enterprise/mcp-management#:~:text=Public%20preview%2C%20not%20prioritized%20for%20development) | none shown | released |
| <a id="ev-V96"></a>V96 | Users can bypass the restriction by editing configuration files. | [GitHub Docs, MCP server usage in your company](https://docs.github.com/en/copilot/concepts/enterprise/mcp-management#:~:text=Users%20can%20bypass%20the%20restriction%20by%20editing%20configuration%20files.) | none shown | released |
| <a id="ev-V97"></a>V97 | the user's input is scanned by a classification model that detects jailbreak attacks. | [Microsoft Learn, Foundry guardrail intervention points](https://learn.microsoft.com/en-us/azure/foundry/guardrails/intervention-points#:~:text=the,classification%20model%20that%20detects%20jailbreak%20attacks.) | 2026-03-02 | released |
| <a id="ev-V98"></a>V98 | such as Violence, Hate, Sexual, and Self-harm controls on user inputs and outputs. | [Microsoft Learn, create a Foundry guardrail](https://learn.microsoft.com/en-us/azure/foundry/guardrails/how-to-create-guardrails#:~:text=such%20as%20Violence%2C%20Hate%2C%20Sexual%2C%20and%20Self%2Dharm%20controls%20on%20user%20inputs%20and%20outputs.) | 2026-10-15 | released |
| <a id="ev-V99"></a>V99 | Action: Annotate only When this control is specified, the final content meant to be displayed to the user is scanned for certain types of copyrighted text. | [Microsoft Learn, Foundry guardrail intervention points](https://learn.microsoft.com/en-us/azure/foundry/guardrails/intervention-points#:~:text=Action%3A%20Annotate%20only%20When%20this%20control,for%20certain%20types%20of%20copyrighted%20text.) | 2026-03-02 | released |
| <a id="ev-V100"></a>V100 | For agents, the agent's guardrail overrides the model's guardrail. | [Microsoft Learn, create a Foundry guardrail](https://learn.microsoft.com/en-us/azure/foundry/guardrails/how-to-create-guardrails#:~:text=For%20agents%2C%20the,guardrail.) | 2026-10-15 | released |
| <a id="ev-V101"></a>V101 | The Network control configures network egress controls for hosted agents and prompt agents that use the Microsoft Copilot harness. It doesn't affect other prompt agents or model deployments. | [Microsoft Learn, create a Foundry guardrail](https://learn.microsoft.com/en-us/azure/foundry/guardrails/how-to-create-guardrails#:~:text=The%20Network%20control%20configures%20network%20egress,other%20prompt%20agents%20or%20model%20deployments.) | 2026-10-15 | released |
| <a id="ev-V102"></a>V102 | Tool call (Preview) The next action the agent is proposing to take, as generated by its underlying model. | [Microsoft Learn, Foundry guardrail intervention points](https://learn.microsoft.com/en-us/azure/foundry/guardrails/intervention-points#:~:text=Tool%20call%20%28Preview%29%20The%20next%20action,as%20generated%20by%20its%20underlying%20model.) | 2026-03-02 | released |
| <a id="ev-V103"></a>V103 | Tool response (Preview) The content sent back by a tool, internal to an agent's orchestration | [Microsoft Learn, Foundry guardrail intervention points](https://learn.microsoft.com/en-us/azure/foundry/guardrails/intervention-points#:~:text=Tool%20response%20%28Preview%29%20The%20content%20sent,orchestration) | 2026-03-02 | released |
| <a id="ev-V104"></a>V104 | Tool call and tool response intervention points require moderation support from the tool itself. | [Microsoft Learn, Foundry guardrail intervention points](https://learn.microsoft.com/en-us/azure/foundry/guardrails/intervention-points#:~:text=Tool%20call%20and%20tool%20response%20intervention,moderation%20support%20from%20the%20tool%20itself.) | 2026-03-02 | preview |
| <a id="ev-V105"></a>V105 | Currently, the following tools support moderation: Azure AI Search, Azure Functions, OpenAPI, Sharepoint Grounding, Fabric Data Agent, Bing Grounding, Bing Custom Search, and Browser Automation. | [Microsoft Learn, Foundry guardrail intervention points](https://learn.microsoft.com/en-us/azure/foundry/guardrails/intervention-points#:~:text=Currently%2C%20the%20following%20tools%20support%20moderation%3A,Bing%20Custom%20Search%2C%20and%20Browser%20Automation.) | 2026-03-02 | preview |
| <a id="ev-V106"></a>V106 | The default value is always | [Microsoft Learn, Foundry MCP tool](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol#:~:text=The%20default%20value%20is%20always) | 2026-10-28 | released |
| <a id="ev-V107"></a>V107 | Treat tool descriptions, annotations, and results from remote MCP servers as untrusted input. | [Microsoft Learn, Foundry MCP tool](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol#:~:text=Treat%20tool%20descriptions%2C%20annotations%2C%20and%20results,remote%20MCP%20servers%20as%20untrusted%20input.) | 2026-10-28 | released |
| <a id="ev-V108"></a>V108 | Require approval for high-risk operations, especially tools that write data or change resources. | [Microsoft Learn, Foundry MCP tool](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol#:~:text=Require%20approval%20for%20high%2Drisk%20operations%2C%20especially,that%20write%20data%20or%20change%20resources.) | 2026-10-28 | released |
| <a id="ev-V109"></a>V109 | Hosted agents run in per-session VM-isolated sandboxes. | [Microsoft Learn, Foundry hosted agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents#:~:text=Hosted%20agents%20run%20in%20per%2Dsession%20VM%2Disolated%20sandboxes.) | 2026-11-09 | released |
| <a id="ev-V110"></a>V110 | They include built-in protection against various threats, such as user prompt-injection attacks (UPIA) and cross-domain prompt injection Attacks (XPIA). | [Microsoft Learn, Copilot Studio external threat detection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-provider#:~:text=They%20include%20built%2Din%20protection%20against%20various,and%20cross%2Ddomain%20prompt%20injection%20Attacks%20%28XPIA%29.) | 2026-06-01 | released |
| <a id="ev-V111"></a>V111 | Copilot Studio provides content moderation for predefined harmful-content categories | [Microsoft Learn, Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance#:~:text=Copilot%20Studio%20provides%20content%20moderation%20for%20predefined%20harmful%2Dcontent%20categories) | 2026-09-24 | released |
| <a id="ev-V112"></a>V112 | This article is prerelease documentation and is subject to change. | [Microsoft Learn, Copilot Studio external threat detection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-provider#:~:text=This%20article%20is%20prerelease%20documentation%20and%20is%20subject%20to%20change.) | 2026-06-01 | preview |
| <a id="ev-V113"></a>V113 | The threat detection system analyzes the data and returns a decision to either allow or block the tool invocation. | [Microsoft Learn, Copilot Studio external threat detection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-provider#:~:text=The%20threat%20detection%20system%20analyzes%20the,allow%20or%20block%20the%20tool%20invocation.) | 2026-06-01 | preview |
| <a id="ev-V114"></a>V114 | within one second, by default, it proceeds to allow the tool to execute as planned. | [Microsoft Learn, Copilot Studio external threat detection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-provider#:~:text=within%20one%20second%2C%20by%20default%2C%20it%20proceeds%20to%20allow%20the%20tool%20to%20execute%20as%20planned.) | 2026-06-01 | preview |
| <a id="ev-V115"></a>V115 | For a tool call that requires approval, expand the confirmation dialog to review its input parameters. | [VS Code Docs, use tools with agents](https://code.visualstudio.com/docs/copilot/agents/agent-tools#:~:text=For%20a%20tool%20call%20that%20requires,dialog%20to%20review%20its%20input%20parameters.) | none shown | released |
| <a id="ev-V116"></a>V116 | Real-time protection inspects AI agent activity throughout the agentic loop and blocks risky actions before they execute. | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=Real%2Dtime%20protection%20inspects%20AI%20agent%20activity,blocks%20risky%20actions%20before%20they%20execute.) | 2026-10-15 | preview |
| <a id="ev-V117"></a>V117 | Foundry agents (Preview) | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=Foundry%20agents%20%28Preview%29) | 2026-10-15 | preview |
| <a id="ev-V118"></a>V118 | Protection evaluates user requests, agent responses, tool invocations, and tool responses. | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=Protection%20evaluates%20user%20requests%2C%20agent%20responses%2C%20tool%20invocations%2C%20and%20tool%20responses.) | 2026-10-15 | preview |
| <a id="ev-V119"></a>V119 | Copilot Studio agents (Preview) | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=Copilot%20Studio%20agents%20%28Preview%29) | 2026-10-15 | preview |
| <a id="ev-V120"></a>V120 | Protection evaluates tool invocations, which doesn't depend on Work IQ MCP. | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=Protection%20evaluates%20tool%20invocations%2C%20which,depend%20on%20Work%20IQ%20MCP.) | 2026-10-15 | preview |
| <a id="ev-V121"></a>V121 | Defender integrates with Work IQ MCP to evaluate tool invocations before they run, including invocations of customer MCP tools onboarded to Agent 365 | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=Defender%20integrates%20with%20Work%20IQ%20MCP,MCP%20tools%20onboarded%20to%20Agent%20365) | 2026-10-15 | preview |
| <a id="ev-V122"></a>V122 | Agents that rely on unsupported tools or don't integrate with Work IQ MCP aren't covered. | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=Agents%20that%20rely%20on%20unsupported%20tools,covered.) | 2026-10-15 | preview |
| <a id="ev-V123"></a>V123 | Audits all agents, recording matching activity as a behavior without stopping the action. | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=Audits%20all%20agents%2C%20recording%20matching%20activity%20as%20a%20behavior%20without%20stopping%20the%20action.) | 2026-10-15 | preview |
| <a id="ev-V124"></a>V124 | Block matching actions before they execute and record the behavior. | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=Block%20matching%20actions%20before%20they%20execute%20and%20record%20the%20behavior.) | 2026-10-15 | preview |
| <a id="ev-V125"></a>V125 | A tool call identified as sending email to an unsafe domain is blocked before the tool executes. | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=A%20tool%20call%20identified%20as%20sending,is%20blocked%20before%20the%20tool%20executes.) | 2026-10-15 | preview |
| <a id="ev-V126"></a>V126 | If detected, there is a flag in the annotation response for the API used to call this model or agent. | [Microsoft Learn, Foundry guardrail intervention points](https://learn.microsoft.com/en-us/azure/foundry/guardrails/intervention-points#:~:text=If%20detected%2C%20there%20is%20a%20flag,to%20call%20this%20model%20or%20agent.) | 2026-03-02 | released |
| <a id="ev-V127"></a>V127 | If an attack is detected, the user's input is blocked from being sent to the model, halting the interaction. | [Microsoft Learn, Foundry guardrail intervention points](https://learn.microsoft.com/en-us/azure/foundry/guardrails/intervention-points#:~:text=If%20an%20attack%20is%20detected%2C%20the,to%20the%20model%2C%20halting%20the%20interaction.) | 2026-03-02 | released |
| <a id="ev-V128"></a>V128 | There are two ways to edit a control: deleting it and adding a new one, or overriding an existing control. The latter is the only way to edit a control that can't be deleted, such as Violence, Hate, Sexual, and Self-harm controls on user inputs and outputs. | [Microsoft Learn, create a Foundry guardrail](https://learn.microsoft.com/en-us/azure/foundry/guardrails/how-to-create-guardrails#:~:text=There%20are%20two%20ways%20to%20edit,controls%20on%20user%20inputs%20and%20outputs.) | 2026-10-15 | released |
| <a id="ev-V129"></a>V129 | A developer needs to provide approval for every call. | [Microsoft Learn, Foundry MCP tool](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol#:~:text=A%20developer%20needs%20to%20provide%20approval%20for%20every%20call.) | 2026-10-28 | released |
| <a id="ev-V130"></a>V130 | At runtime, the agent blocks attacks of these types, reducing the risk of data exfiltration. | [Microsoft Learn, Copilot Studio external threat detection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-provider#:~:text=At%20runtime%2C%20the%20agent%20blocks%20attacks,reducing%20the%20risk%20of%20data%20exfiltration.) | 2026-06-01 | released |
| <a id="ev-V131"></a>V131 | Because deny rules take precedence, you can combine the wildcard allowlist entry with denylist entries to allow all connectors except the ones you block. | [GitHub Docs, configure the enterprise MCP allowlist](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-enterprise-allowlist#:~:text=Because%20deny%20rules%20take%20precedence%2C%20you,connectors%20except%20the%20ones%20you%20block.) | none shown | released |
| <a id="ev-V132"></a>V132 | If you configure controls at tool call or tool response intervention points but your agent uses tools not in this list, those controls won't take effect for those specific tools. | [Microsoft Learn, Foundry guardrail intervention points](https://learn.microsoft.com/en-us/azure/foundry/guardrails/intervention-points#:~:text=If%20you%20configure%20controls%20at%20tool,take%20effect%20for%20those%20specific%20tools.) | 2026-03-02 | preview |
| <a id="ev-V133"></a>V133 | the full payload sent back from each tool to this agent is scanned for attempted indirect prompt injection attacks. | [Microsoft Learn, Foundry guardrail intervention points](https://learn.microsoft.com/en-us/azure/foundry/guardrails/intervention-points#:~:text=the%20full%20payload%20sent%20back%20from,for%20attempted%20indirect%20prompt%20injection%20attacks.) | 2026-03-02 | preview |
| <a id="ev-V134"></a>V134 | Agent guardrails are in preview. | [Microsoft Learn, Foundry guardrails and controls overview](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview#:~:text=Agent%20guardrails%20are%20in%20preview.) | 2026-10-20 | released |
| <a id="ev-V135"></a>V135 | If no custom guardrail is assigned, the agent inherits the guardrail of its underlying model deployment. | [Microsoft Learn, Foundry guardrails and controls overview](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview#:~:text=If%20no%20custom%20guardrail%20is%20assigned%2C,guardrail%20of%20its%20underlying%20model%20deployment.) | 2026-10-20 | released |
| <a id="ev-V136"></a>V136 | You provide a list of tools that don't require approval. | [Microsoft Learn, Foundry MCP tool](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol#:~:text=You%20provide%20a%20list%20of%20tools,require%20approval.) | 2026-10-28 | released |
| <a id="ev-V137"></a>V137 | In the end user chat experience, ask the agent for confirmation before running the tool. This option is set to No by default. | [Microsoft Learn, add tools to Copilot Studio custom agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent#:~:text=In%20the%20end%20user%20chat%20experience%2C,is%20set%20to%20No%20by%20default.) | 2026-10-01 | released |
| <a id="ev-V138"></a>V138 | External threat detection is only called on generative agents that use generative orchestration. External threat detection is skipped for classic agents. | [Microsoft Learn, Copilot Studio external threat detection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-provider#:~:text=External%20threat%20detection%20is%20only%20called,detection%20is%20skipped%20for%20classic%20agents.) | 2026-06-01 | preview |
| <a id="ev-V139"></a>V139 | but you can also chose the Block the query option to further reduce risk. | [Microsoft Learn, Copilot Studio external threat detection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-provider#:~:text=but%20you%20can%20also%20chose%20the%20Block%20the%20query%20option%20to%20further%20reduce%20risk.) | 2026-06-01 | preview |
| <a id="ev-V140"></a>V140 | the agent shares data with the external security provider during its run. | [Microsoft Learn, Copilot Studio external threat detection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-provider#:~:text=the%20agent%20shares%20data%20with%20the%20external%20security%20provider%20during%20its%20run.) | 2026-06-01 | preview |
| <a id="ev-V141"></a>V141 | Interactions containing detected malicious content are blocked. | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=Interactions%20containing%20detected%20malicious%20content%20are%20blocked.) | 2026-10-15 | preview |
| <a id="ev-V142"></a>V142 | Interactions identified as secret exfiltration are blocked. | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=Interactions%20identified%20as%20secret%20exfiltration%20are%20blocked.) | 2026-10-15 | preview |
| <a id="ev-V143"></a>V143 | Interactions containing detected evasion techniques are blocked. | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=Interactions%20containing%20detected%20evasion%20techniques%20are%20blocked.) | 2026-10-15 | preview |
| <a id="ev-V144"></a>V144 | This scenario is evaluated only at the tool request intervention point. | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=This%20scenario%20is%20evaluated%20only%20at%20the%20tool%20request%20intervention%20point.) | 2026-10-15 | preview |
| <a id="ev-V145"></a>V145 | Only agents with a Microsoft Entra agent ID appear in the list. | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=Only%20agents%20with%20a%20Microsoft%20Entra%20agent%20ID%20appear%20in%20the%20list.) | 2026-10-15 | preview |
| <a id="ev-V146"></a>V146 | Covered through endpoint runtime protection in Microsoft Defender for Endpoint | [Microsoft Learn, Protect AI agents in real time using Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/real-time-agent-protection-during-runtime#:~:text=Covered%20through%20endpoint%20runtime%20protection%20in%20Microsoft%20Defender%20for%20Endpoint) | 2026-10-15 | preview |
| <a id="ev-V147"></a>V147 | audit them, and block actions before they run when the inspection method allows it. | [Microsoft Learn, AI agent runtime protection with Defender for Endpoint (Preview)](https://learn.microsoft.com/en-us/defender-endpoint/ai-agent-runtime-protection-overview#:~:text=audit%20them%2C%20and%20block%20actions%20before%20they%20run%20when%20the%20inspection%20method%20allows%20it.) | 2026-10-08 | preview |
| <a id="ev-V148"></a>V148 | Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. | [Microsoft Learn, AI agent runtime protection with Defender for Endpoint (Preview)](https://learn.microsoft.com/en-us/defender-endpoint/ai-agent-runtime-protection-overview#:~:text=Some%20information%20in%20this%20article%20relates,commercially%20released.) | 2026-10-08 | preview |
| <a id="ev-V149"></a>V149 | Windows (preview) The following tables list agent and inspection method combinations on Windows. | [Microsoft Learn, Defender for Endpoint AI agent support matrix](https://learn.microsoft.com/en-us/defender-endpoint/ai-agent-support-matrix#:~:text=Windows%20%28preview%29%20The%20following%20tables%20list,and%20inspection%20method%20combinations%20on%20Windows.) | 2026-11-02 | preview |
| <a id="ev-V150"></a>V150 | VS Code GitHub Copilot extension | [Microsoft Learn, Defender for Endpoint AI agent support matrix](https://learn.microsoft.com/en-us/defender-endpoint/ai-agent-support-matrix#:~:text=VS%20Code%20GitHub%20Copilot%20extension) | 2026-11-02 | preview |
| <a id="ev-V151"></a>V151 | Actions that are not auto-approved require your confirmation. | [VS Code Docs, permissions and approvals](https://code.visualstudio.com/docs/agents/run/approvals#:~:text=Actions%20that%20are%20not%20auto%2Dapproved%20require%20your%20confirmation.) | 2026-11-04 | released |
| <a id="ev-V152"></a>V152 | Runs all tool calls without confirmation. | [VS Code Docs, permissions and approvals](https://code.visualstudio.com/docs/agents/run/approvals#:~:text=Runs%20all%20tool%20calls%20without%20confirmation.) | 2026-11-04 | released |
| <a id="ev-V153"></a>V153 | Uses an LLM judge to assess each tool call. | [VS Code Docs, permissions and approvals](https://code.visualstudio.com/docs/agents/run/approvals#:~:text=Uses%20an%20LLM%20judge%20to%20assess%20each%20tool%20call.) | 2026-11-04 | released |
| <a id="ev-V154"></a>V154 | Adds the tool result to the chat context without review. Use caution with external data that might contain prompt injection. | [VS Code Docs, permissions and approvals](https://code.visualstudio.com/docs/agents/run/approvals#:~:text=Adds%20the%20tool%20result%20to%20the,data%20that%20might%20contain%20prompt%20injection.) | 2026-11-04 | released |
| <a id="ev-V155"></a>V155 | Which tools require confirmation before or after they run | [VS Code Docs, permissions and approvals](https://code.visualstudio.com/docs/agents/run/approvals#:~:text=Which%20tools%20require%20confirmation%20before%20or%20after%20they%20run) | 2026-11-04 | released |
| <a id="ev-V156"></a>V156 | While this policy is set, tool confirmations offer only one-time approval, and tool approvals that developers saved earlier aren't applied. | [VS Code Docs, manage AI settings in the enterprise](https://code.visualstudio.com/docs/enterprise/manage-ai-settings#:~:text=While%20this%20policy%20is%20set%2C%20tool,applied.) | 2026-11-04 | released |
| <a id="ev-V157"></a>V157 | to disable Allow all in the permissions picker. | [VS Code Docs, manage AI settings in the enterprise](https://code.visualstudio.com/docs/enterprise/manage-ai-settings#:~:text=to%20disable%20Allow%20all%20in%20the%20permissions%20picker.) | 2026-11-04 | released |
| <a id="ev-V158"></a>V158 | Servers from other sources can require a separate MCP server trust decision and prompt again after configuration changes. | [VS Code Docs, trust and safety](https://code.visualstudio.com/docs/agents/concepts/trust-and-safety#:~:text=Servers%20from%20other%20sources%20can%20require,and%20prompt%20again%20after%20configuration%20changes.) | 2026-11-04 | released |
| <a id="ev-V159"></a>V159 | hook can inspect a supported tool's arguments and return a denial. A filter that misses a tool or argument shape does not validate that operation. | [VS Code Docs, security for agents](https://code.visualstudio.com/docs/agents/run/security#:~:text=hook%20can%20inspect%20a%20supported,shape%20does%20not%20validate%20that%20operation.) | 2026-11-04 | released |
| <a id="ev-V160"></a>V160 | Hooks are not a substitute for enforced permissions, sandboxing, or enterprise controls. | [VS Code Docs, security for agents](https://code.visualstudio.com/docs/agents/run/security#:~:text=Hooks%20are%20not%20a%20substitute%20for%20enforced%20permissions%2C%20sandboxing%2C%20or%20enterprise%20controls.) | 2026-11-04 | released |
| <a id="ev-V161"></a>V161 | At times, GitHub Copilot Chat may include a content filtering system that scans prompts and responses to detect and block harmful content. | [GitHub Docs, responsible use of GitHub Copilot Chat](https://docs.github.com/en/copilot/responsible-use/chat#:~:text=At%20times%2C%20GitHub%20Copilot%20Chat%20may,to%20detect%20and%20block%20harmful%20content.) | none shown | released |
| <a id="ev-V162"></a>V162 | Microsoft 365 Copilot supports federated Copilot connectors to enable organizations to connect their data to Copilot by using Model Context Protocol (MCP). | [Microsoft Learn, federated Microsoft 365 Copilot connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-overview#:~:text=Microsoft%20365%20Copilot%20supports%20federated%20Copilot,by%20using%20Model%20Context%20Protocol%20%28MCP%29.) | 2026-10-19 | released |
| <a id="ev-V163"></a>V163 | Admins control which federated connectors are available in their organization from Agents &gt; Settings &gt; Agent and plugin access in the Microsoft 365 admin center. | [Microsoft Learn, federated Microsoft 365 Copilot connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-overview#:~:text=Admins%20control%20which%20federated%20connectors%20are,in%20the%20Microsoft%20365%20admin%20center.) | 2026-10-19 | released |
| <a id="ev-V164"></a>V164 | Tools that create, update, or delete data require user approval. | [Microsoft Learn, federated Microsoft 365 Copilot connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-overview#:~:text=Tools%20that%20create%2C%20update%2C%20or%20delete%20data%20require%20user%20approval.) | 2026-10-19 | released |
| <a id="ev-V165"></a>V165 | Admins can audit activity in Microsoft Purview. | [Microsoft Learn, federated Microsoft 365 Copilot connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-overview#:~:text=Admins%20can%20audit%20activity%20in%20Microsoft%20Purview.) | 2026-10-19 | released |
| <a id="ev-V166"></a>V166 | A custom federated connector starts with a Model Context Protocol (MCP) server that exposes tools for Microsoft 365 Copilot to access data or take actions in your internal systems. | [Microsoft Learn, set up custom federated connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/set-up-custom-federated-connectors#:~:text=A%20custom%20federated%20connector%20starts%20with,take%20actions%20in%20your%20internal%20systems.) | 2026-10-19 | released |
| <a id="ev-V167"></a>V167 | Global Administrator or AI Administrator role in the Microsoft 365 admin center | [Microsoft Learn, set up custom federated connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/set-up-custom-federated-connectors#:~:text=Global%20Administrator%20or%20AI%20Administrator%20role%20in%20the%20Microsoft%20365%20admin%20center) | 2026-10-19 | released |
| <a id="ev-V168"></a>V168 | The Allow agents and plugins built by your organization setting in Agents &gt; Settings &gt; Agent and plugin access governs custom connectors. | [Microsoft Learn, set up custom federated connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/set-up-custom-federated-connectors#:~:text=The%20Allow%20agents%20and%20plugins%20built,and%20plugin%20access%20governs%20custom%20connectors.) | 2026-10-19 | released |
| <a id="ev-V169"></a>V169 | All of them must allow the user. | [Microsoft Learn, set up custom federated connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/set-up-custom-federated-connectors#:~:text=All%20of%20them%20must%20allow%20the%20user.) | 2026-10-19 | released |
| <a id="ev-V170"></a>V170 | If your MCP server restricts incoming traffic by source IP address, allow the static egress IP addresses used by Microsoft 365 Copilot | [Microsoft Learn, set up custom federated connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/set-up-custom-federated-connectors#:~:text=If%20your%20MCP%20server%20restricts%20incoming,addresses%20used%20by%20Microsoft%20365%20Copilot) | 2026-10-19 | released |
| <a id="ev-V171"></a>V171 | Is there a PowerShell or API option for Agent and plugin access? Not currently. Use the Microsoft 365 admin center. | [Microsoft Learn, manage federated Copilot connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/manage-federated-connectors#:~:text=Is%20there%20a%20PowerShell%20or%20API,Use%20the%20Microsoft%20365%20admin%20center.) | 2026-10-15 | released |
| <a id="ev-V172"></a>V172 | Tool-level and connector-level blocking. | [Microsoft Learn, manage federated Copilot connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/manage-federated-connectors#:~:text=Tool%2Dlevel%20and%20connector%2Dlevel%20blocking.) | 2026-10-15 | released |
| <a id="ev-V173"></a>V173 | Microsoft 365 Copilot Chat uses a fixed, known set of outbound (egress) IP addresses for Model Context Protocol (MCP) tool and API calls from declarative agents and federated connectors. | [Microsoft Learn, static IP addresses for MCP and federated connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-network-requirements#:~:text=Microsoft%20365%20Copilot%20Chat%20uses%20a,from%20declarative%20agents%20and%20federated%20connectors.) | 2026-10-23 | released |
| <a id="ev-V174"></a>V174 | IP allow listing doesn't replace authentication or authorization. | [Microsoft Learn, static IP addresses for MCP and federated connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-network-requirements#:~:text=IP%20allow%20listing,replace%20authentication%20or%20authorization.) | 2026-10-23 | released |
| <a id="ev-V175"></a>V175 | This IP address list can change with seven days' notice. | [Microsoft Learn, static IP addresses for MCP and federated connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-network-requirements#:~:text=This%20IP%20address%20list%20can%20change,notice.) | 2026-10-23 | released |
| <a id="ev-V176"></a>V176 | As of May 1, 2026, Microsoft Agent 365 is generally available for the Commercial segment on a per user basis. | [Microsoft Learn, Microsoft Agent 365 overview](https://learn.microsoft.com/en-us/microsoft-agent-365/overview#:~:text=As%20of%20May%201%2C%202026%2C%20Microsoft,segment%20on%20a%20per%20user%20basis.) | 2026-08-19 | released |
| <a id="ev-V177"></a>V177 | The Tools registry in the Microsoft 365 admin center is the source of truth for the MCP servers currently available in your tenant. | [Microsoft Learn, MCP server options in Agent 365](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview#:~:text=The%20Tools%20registry%20in%20the%20Microsoft,servers%20currently%20available%20in%20your%20tenant.) | 2026-10-08 | released |
| <a id="ev-V178"></a>V178 | Registration through the bring-your-own (BYO) process enables centralized review and governance. | [Microsoft Learn, MCP server options in Agent 365](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview#:~:text=Registration%20through%20the%20bring%2Dyour%2Down%20%28BYO%29%20process,process%20enables%20centralized%20review%20and%20governance.) | 2026-10-08 | released |
| <a id="ev-V179"></a>V179 | This feature is in preview. | [Microsoft Learn, Agent 365 bring-your-own MCP server](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-byo-mcp-server#:~:text=This%20feature%20is%20in%20preview.) | 2026-11-05 | released |
| <a id="ev-V180"></a>V180 | This feature is in preview. | [Microsoft Learn, Agent 365 tools gateway](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-tools-gateway#:~:text=This%20feature%20is%20in%20preview.) | 2026-11-06 | released |
| <a id="ev-V181"></a>V181 | and then select the Registry tab. | [Microsoft Learn, manage plugins, skills, and MCP servers](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-plugins-skills-mcp-servers#:~:text=and%20then%20select%20the%20Registry%20tab.) | 2026-11-11 | released |
| <a id="ev-V182"></a>V182 | and then select the Requests (preview) tab. | [Microsoft Learn, manage plugins, skills, and MCP servers](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-plugins-skills-mcp-servers#:~:text=and%20then%20select%20the%20Requests%20%28preview%29%20tab.) | 2026-11-11 | released |
| <a id="ev-V183"></a>V183 | The registry displays the following status indicators for MCP servers: Available : The tool is active and ready for use. Blocked : The tool is disabled, and agents can't access it. | [Microsoft Learn, manage plugins, skills, and MCP servers](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-plugins-skills-mcp-servers#:~:text=The%20registry%20displays%20the%20following%20status,access%20it.) | 2026-11-11 | released |
| <a id="ev-V184"></a>V184 | Select Approve to make the server available in the organizational registry, or Reject to deny the request. | [Microsoft Learn, manage plugins, skills, and MCP servers](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-plugins-skills-mcp-servers#:~:text=Select%20Approve%20to%20make%20the%20server,or%20Reject%20to%20deny%20the%20request.) | 2026-11-11 | released |
| <a id="ev-V185"></a>V185 | After approval, consent to the Microsoft Entra permissions required by the MCP server. The server becomes available to agent-building surfaces only after consent is granted. | [Microsoft Learn, manage plugins, skills, and MCP servers](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-plugins-skills-mcp-servers#:~:text=After%20approval%2C%20consent%20to%20the%20Microsoft,surfaces%20only%20after%20consent%20is%20granted.) | 2026-11-11 | released |
| <a id="ev-V186"></a>V186 | Two roles meet both requirements: AI Administrator | [Microsoft Learn, manage plugins, skills, and MCP servers](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-plugins-skills-mcp-servers#:~:text=Two%20roles%20meet%20both%20requirements%3A%20AI%20Administrator) | 2026-11-11 | released |
| <a id="ev-V187"></a>V187 | Global Administrator | [Microsoft Learn, manage plugins, skills, and MCP servers](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-plugins-skills-mcp-servers#:~:text=Global%20Administrator) | 2026-11-11 | released |
| <a id="ev-V188"></a>V188 | Tool-level granular control is rolling out to tenants and supports only specific types of MCP servers registered on Agent 365. | [Microsoft Learn, manage plugins, skills, and MCP servers](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-plugins-skills-mcp-servers#:~:text=Tool%2Dlevel%20granular%20control%20is%20rolling%20out,MCP%20servers%20registered%20on%20Agent%20365.) | 2026-11-11 | released |
| <a id="ev-V189"></a>V189 | The agent registry in Microsoft 365 admin center provides a centralized view of all agents available for your organization. | [Microsoft Learn, Agent Registry in Microsoft 365 admin center](https://learn.microsoft.com/en-us/entra/agent-id/agent-metadata-discoverability#:~:text=The%20agent%20registry%20in%20Microsoft%20365,all%20agents%20available%20for%20your%20organization.) | 2026-11-11 | released |
| <a id="ev-V190"></a>V190 | The Data &amp; tools tab is read-only and shows metadata reported by the agent platform. | [Microsoft Learn, understand agent details in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-details#:~:text=The%20Data%20%26%20tools%20tab%20is%20read%2Donly%20and%20shows%20metadata%20reported%20by%20the%20agent%20platform.) | 2026-11-11 | released |
| <a id="ev-V191"></a>V191 | Currently, Microsoft 365 admin center doesn't have data and tools information for all agents. | [Microsoft Learn, understand agent details in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-details#:~:text=Currently%2C%20Microsoft%20365%20admin%20center,and%20tools%20information%20for%20all%20agents.) | 2026-11-11 | released |
| <a id="ev-V192"></a>V192 | When a member of your organization publishes an agent to your tenant, the agent requires administrator approval before becoming available tenant-wide. | [Microsoft Learn, manage agent requests in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-requests#:~:text=When%20a%20member%20of%20your%20organization,administrator%20approval%20before%20becoming%20available%20tenant%2Dwide.) | 2026-11-11 | released |
| <a id="ev-V193"></a>V193 | Administrators can review the agent's details, such as the description, owner, data, and tools, and then publish or reject it. | [Microsoft Learn, manage agent requests in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-requests#:~:text=Administrators%20can%20review%20the,and%20then%20publish%20or%20reject%20it.) | 2026-11-11 | released |
| <a id="ev-V194"></a>V194 | Centralized MCP server inventory ✔️ ✔️ Block or unblock MCP servers ✔️ ✔️ Tool-level blocking ✔️ Tool activity observability ✔️ Tool threat protection ✔️ | [Microsoft Learn, API Management with Agent 365](https://learn.microsoft.com/en-us/azure/api-management/agent-365#:~:text=Centralized%20MCP%20server%20inventory%20%E2%9C%94%EF%B8%8F%20%E2%9C%94%EF%B8%8F,observability%20%E2%9C%94%EF%B8%8F%20Tool%20threat%20protection%20%E2%9C%94%EF%B8%8F) | 2026-10-06 | preview |
| <a id="ev-V195"></a>V195 | AI Gateway is a dedicated product for AI traffic. | [Microsoft Learn, What is AI Gateway?](https://learn.microsoft.com/en-us/azure/ai-gateway/overview#:~:text=AI%20Gateway%20is%20a%20dedicated%20product%20for%20AI%20traffic.) | 2026-10-28 | preview |
| <a id="ev-V196"></a>V196 | it's not a separate offering. | [Microsoft Learn, API Management AI gateway capabilities](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities#:~:text=,not%20a%20separate%20offering.) | 2026-05-29 | released |
| <a id="ev-V197"></a>V197 | AI Gateway uses Azure API Management behind the scenes to provide token limits, quotas, and governance for model deployments. | [Microsoft Learn, Configure AI Gateway in your Foundry resources](https://learn.microsoft.com/en-us/azure/foundry/configuration/enable-ai-api-management-gateway-portal#:~:text=AI%20Gateway%20uses%20Azure%20API%20Management,quotas%2C%20and%20governance%20for%20model%20deployments.) | 2026-08-03 | released |
| <a id="ev-V198"></a>V198 | Creates a Basic v2 SKU instance. | [Microsoft Learn, Configure AI Gateway in your Foundry resources](https://learn.microsoft.com/en-us/azure/foundry/configuration/enable-ai-api-management-gateway-portal#:~:text=Creates%20a%20Basic%20v2%20SKU%20instance.) | 2026-08-03 | released |
| <a id="ev-V199"></a>V199 | The API Management instance is created in one of the v2 tiers | [Microsoft Learn, Configure AI Gateway in your Foundry resources](https://learn.microsoft.com/en-us/azure/foundry/configuration/enable-ai-api-management-gateway-portal#:~:text=The%20API%20Management%20instance%20is%20created%20in%20one%20of%20the%20v2%20tiers) | 2026-08-03 | released |
| <a id="ev-V200"></a>V200 | The API Management instance is in the same Microsoft Entra tenant and the same subscription as the Foundry resource. | [Microsoft Learn, Configure AI Gateway in your Foundry resources](https://learn.microsoft.com/en-us/azure/foundry/configuration/enable-ai-api-management-gateway-portal#:~:text=The%20API%20Management%20instance%20is%20in,same%20subscription%20as%20the%20Foundry%20resource.) | 2026-08-03 | released |
| <a id="ev-V201"></a>V201 | For production workloads or higher throughput requirements, consider using an existing APIM instance with a Standard v2 or Premium v2 tier. | [Microsoft Learn, Configure AI Gateway in your Foundry resources](https://learn.microsoft.com/en-us/azure/foundry/configuration/enable-ai-api-management-gateway-portal#:~:text=For%20production%20workloads%20or%20higher%20throughput,Standard%20v2%20or%20Premium%20v2%20tier.) | 2026-08-03 | released |
| <a id="ev-V202"></a>V202 | AI gateways support only MCP tools. | [Microsoft Learn, Foundry tools governance](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/governance#:~:text=AI%20gateways%20support%20only%20MCP%20tools.) | 2026-08-19 | preview |
<!-- End source quotes -->

## Reviewed presentation text

The checker proves a verdict was recorded for the exact wording, not that the verdict is right. It reads each run of words in the ASCII figures as one text. Verdicts were set by hand: label, requirement or code token.

<!-- Begin reviewed presentation text -->
```text
label	MCP Governance in a Microsoft ecosystem
requirement	A proposed design to make a gateway the only way to reach a company MCP server and to limit managed clients to approved servers, across GitHub Copilot, VS Code, Foundry, Copilot Studio and Microsoft 365 Copilot. Nothing is tested in a tenant.
label	The design
label	recommendation
requirement	Design target: a Git repository holds the approved and denied MCP servers. A reviewed pull request changes it. After merge, a pipeline applies the list to three targets: Power Platform policy for Copilot Studio, GitHub Enterprise managed settings, and Foundry. A fourth target, the Microsoft 365 admin center, is set by hand. Each target names where it is administered and points to the clients it governs: Copilot Studio, VS Code with GitHub Copilot, Foundry agents and Microsoft 365 Copilot. The released-only design uses the Azure API Management service and its existing AI gateway capabilities; MCP server management is listed for supported classic and v2 tiers, with capability availability varying by tier. The separate AI Gateway product is not used in this design. The first three clients pass through client sign-in, Windows outbound firewall rules administered by Intune on managed Windows devices where applicable, API Management identity checks and authorization, and the company MCP server, which accepts calls only from the gateway. The remote MCP URL allowlist applies to managed VS Code and GitHub Copilot clients; it is separate from device egress rules. Microsoft 365 Copilot calls API Management from the Microsoft cloud, from fixed outbound addresses, and skips the client controls. A direct call from a client to the server is blocked. Agent 365 is not drawn: company servers join it through preview features.
label	SOURCE OF TRUTH
label	APPLY ON MERGE
label	GIT REPOSITORY
label	PIPELINE
label	Change by pull request
label	Runs after merge
label	TARGETS
label	POWER PLATFORM
label	GITHUB ENTERPRISE
label	FOUNDRY
label	MICROSOFT 365
label	Power Platform admin
label	Managed settings
label	Foundry portal
label	Microsoft 365 admin
label	center
label	repository
requirement	Approved list
requirement	Approved tools
requirement	Approved connectors
requirement	By pipeline
requirement	By hand
label	MCP CLIENTS
label	Copilot Studio
label	VS Code
label	Foundry agents
label	Microsoft 365 Copilot
label	GitHub Copilot
label	CLIENT CONTROLS
label	API MANAGEMENT
label	COMPANY MCP SERVER
label	URL allowlist: VS Code
requirement	MCP: supported tiers
requirement	Accepts calls from
label	and GitHub Copilot
requirement	Gateway only
requirement	Windows egress (Intune)
requirement	Check identity
requirement	Client signed in
requirement	Authorize requests
requirement	Log every call
requirement	Limit request rate
label	Microsoft cloud, fixed outbound addresses
requirement	Unlisted server denied
label	Agent 365 not drawn: company servers join it through preview features
label	Parts and control planes
label	unverified
label	inference
label	Controls
label	Controls by call layer
label	GUARDRAILS ALONG ONE MCP TOOL CALL (request goes down, response comes back)
label	FOUNDRY AGENT
label	COPILOT STUDIO
label	VS CODE, GITHUB COPILOT
label	(layer: AI estimate)
code token	allowed_tools list
label	Data policy: whole server
label	Allow and deny lists
code token	(empty = all tools)
label	(policy, managed settings)
label	Server trust prompt
code token	require_approval
label	Ask user before running
label	Confirmation dialog
label	(default: always)
label	Off by default
label	(default: Manual)
label	Can be set to never
label	(for MCP: unverified)
label	Allow all skips it
label	Policy can lock it
label	Preview only
label	preToolUse hook can deny
requirement	Every client, in the table below
requirement	Outbound rules, then API Management: check identity, authorize, limit rate, log
label	Foundry only: hosted agents run in a VM sandbox
label	Foundry only: Network control limits outbound traffic for hosted and Copilot-harness agents
requirement	Design target: only the gateway can call it. See the table below
label	response comes back
label	Result review before it
label	enters the chat context
label	Can be switched off
label	Rollout and tests
label	Order of work
label	Acceptance tests
label	Bad news first
label	preview
label	With preview preview
requirement	Design target: the figure shows the released-only design with the preview additions shaded. The preview design uses the separate AI Gateway product, which is in public preview, in place of the Azure API Management service gateway in the released-only design. A Git repository holds the approved and denied MCP servers. After a reviewed merge, a pipeline applies the list to Power Platform policy for Copilot Studio, GitHub Enterprise managed settings and Foundry. A fourth target, the Microsoft 365 admin center, is set by hand. Each target names where it is administered and points to the clients it governs: Copilot Studio, VS Code with GitHub Copilot, Foundry agents and Microsoft 365 Copilot. The first three pass through client sign-in, Windows outbound firewall rules administered by Intune on managed Windows devices where applicable, AI Gateway identity checks and authorization with tool threat protection. With the Agent 365 integration, server inventory and blocking are listed for API Management v2 and AI Gateway; tool blocking, activity observability and threat protection are listed only for AI Gateway. The remote MCP URL allowlist applies to managed VS Code and GitHub Copilot clients; it is separate from device egress rules. Microsoft 365 Copilot calls the gateway from the Microsoft cloud, from fixed outbound addresses, and skips the client controls. A direct call from a client to the server is blocked. Below the gateway, the Microsoft 365 admin view shows the all-agents registry, MCP server status, and the preview requests queue. Shaded in the client controls box: the Global Secure Access MCP firewall. Shaded in the gateway box: the separate product, its public preview status, the Agent 365 tool block and tool threat protection. A separate shaded BYO server route box shows the Agent 365 Tooling Gateway, which is not for Foundry agents. Foundry gateway routing and the Defender checks are in the tables below.
label	AI GATEWAY
requirement	Separate product
requirement	Public preview
requirement	Log usage
requirement	Agent 365 tool block
requirement	Tool threat protection
requirement	Connect gateway
label	AGENT 365 ADMIN VIEW
label	Agents > All agents
label	Tools: Available/Blocked
label	Requests (preview)
label	Gateway link (preview)
requirement	Shaded boxes and lines are what preview adds. Everything else is the released design. With preview, connect the gateway to Agent 365 and test tool threat protection in a sandbox. The view combines distinct admin pages: Agents > All agents > Registry, and Agents > Tools > Registry or Requests (preview). V182 V183 V189 The BYO server route is separate; its limits are in the controls below.
label	Added controls
label	Approval and denial workflow
requirement	A developer proposes a server in the reviewed Git inventory. A security reviewer approves or rejects the pull request. Rejection stops the request and is recorded as denied. After approval and merge, the developer registers the server through the Agent 365 preview flow. An administrator reviews the request in Microsoft 365 admin center Requests preview and approves or rejects it. Rejection leaves the server unavailable and the reason is recorded. Approval is followed by Microsoft Entra tenant consent; only then does the server become Available in the tools registry. The admin records the approved server and consent in the inventory, applies target-specific access controls, and monitors calls. A later deny blocks the server in the tools registry and updates the inventory and other policy targets.
label	COMPANY GOVERNANCE
label	AGENT 365, PREVIEW
label	Requester adds server, owner,
label	Developer registers server
label	auth, tools, and risk to Git
label	after the internal PR merges
label	SECURITY REVIEW
label	M365 ADMIN CENTER
label	Review server and each tool
label	Agents > Tools > Requests
label	(preview)
label	APPROVE
label	DENY
label	Review requester, URL,
label	auth, tools, permissions
label	Merge approved
label	Record denied
label	inventory
label	reason in Git
label	STOP
label	REJECT
label	Grant Entra consent
label	Keep unavailable;
label	record reason in Git
label	Registry: AVAILABLE
label	Apply target policies
label	and backend authorization
label	LATER DENY: BLOCK SERVER NOW,
label	MARK DENIED IN GIT, SYNC TARGETS,
label	TEST THAT CALLS FAIL
requirement	The Git pull request is the internal source-of-truth decision. The Microsoft 365 admin-center request is a separate product approval for the preview BYO route. Rejecting either stops rollout. The registry status is Available only after admin approval and required Microsoft Entra consent. V184 V185 V87
label	Guardrails added with preview
label	Tests added with preview
label	Preview pilot, after the baseline
label	Agent 365 Tooling Gateway
label	BYO SERVER ROUTE
label	Everything else is the released design
label	Foundry gateway routing and the Defender checks are in the tables below
label	Global Secure Access
label	MCP firewall
label	Not for Foundry agents
label	Separate from the gateway
label	Shaded = added by preview. AI Gateway takes the place of API Management
label	1 WHICH SERVER
label	2 PERSON APPROVES
label	3 CALL CONTENT
label	4 NETWORK AND GATEWAY
label	5 COMPANY MCP SERVER
label	6 TOOL RESPONSE
label	Guardrails by layer for one MCP tool call, in three columns: Foundry agent, Copilot Studio, and VS Code with GitHub Copilot. Layer 1 which server: Foundry allowed_tools, Copilot Studio data policy, VS Code and GitHub allow and deny lists plus a server trust prompt in VS Code. Layer 2 person approves: Foundry require_approval, default always, which can be set to never. Copilot Studio can ask the user before running a tool, off by default and unverified for MCP tools. VS Code shows a confirmation dialog by default, the Allow all level skips it, and a company policy can lock it. Layer 3 call content: preview only for Foundry and Copilot Studio. In VS Code a preToolUse hook can deny a call, unverified for MCP tools. Layer 4 network and gateway: the table lists what applies to every client, plus two lines that apply to Foundry only. Layer 5 company MCP server: the design target is that only the gateway can call it. Layer 6 tool response: preview only for Foundry. Copilot Studio has a built-in prompt attack block, whose layer is an AI estimate. VS Code can ask for a review of the result before it enters the chat context, and this can be switched off.
label	Prompt attack block (XPIA)
label	Gaps
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

## 2026-11-11, one table by call layer
- Moved text only. No claim added or removed. Merged rows kept every quote link; Microsoft 365 Copilot write approval (V164) and Purview audit (V165) now sit in table rows instead of a note.
- Quote check: 202 of 202 matched live. Label ledger: 199 texts, four ledger entries renamed to the new wording, no new verdicts needed.

## 2026-11-11: preview figure with shading

Figure text changed (shaded additions, BYO server route box, Global Secure Access MCP firewall line, legend). Label ledger updated. Checks run: label ledger, anchor check, quote check (202 quotes, 0 problems), dash scan, browser view at 1280 and 375 px (no sideways scroll, no console errors). Not checked: real phone, Safari, any tenant.

## 2026-11-11: obvious statements cut

No factual claim changed. One ledger line changed ("The effect on other traffic is in the gaps."). Checks run: label ledger, anchor check, quote check (202 quotes, 0 problems), dash scan, browser at 375 px (no sideways page scroll, no dead links, no console errors).

## 2026-11-11: design switch

No factual claim changed; the preview figure and its caption moved to The design. Checks run: label ledger, anchor check, quote check (202 quotes, 0 problems), dash scan, browser at 1280 and 375 px (switch works, shared link works, no sideways scroll, no dead links, no console errors). Not checked: real phone, Safari, light mode.

## 2026-11-11: simplified for a skilled audience

- No source was reread and no quote changed. The "Documentation checked" date did not move.
- Removed from the page: the Fact check section (now a link in the footer), Open questions for the preview, the Start by role links, Where each control applies, Where the preview controls apply, Approval boundaries and cross-cutting guardrails, Fallback, the MCP clients and Microsoft 365 agent registry rows of the parts table, the Result and Label columns, four pilot steps and the six approval steps (now three notes).
- Facts that moved instead of being cut: the cloud agent firewall limit (quote `gh-fw`) is now a gap. The re-review rule is in the Approved inventory row. The request queue quote (`a365-tools-overview`) is cited in the approval workflow note.
- Reviewed text ledger: 20 rows removed with their texts, one reworded (open question 2 now points to the controls table). Label check passes.
- 16 quotes in the table are not cited on the page. Whether they were cited before this pass was not compared. They stay in the table, because removing them would renumber V1 to V202.
- Not checked: the quote check against the live sources was not rerun in this pass. No wording of a sourced claim changed, apart from the moved facts above, which keep their quotes.

## 2026-11-11: content guardrails cut, layers renumbered

- No source was reread and no quote changed.
- Removed from the page: the old layer 1 (user input) and layer 8 (final answer) rows, and the Agent over model and Content moderation rows. These are content filters, not MCP controls. The page now says they are left out.
- Kept and moved: the Copilot Studio prompt attack block (`gr-cs-upia`, `gr-cs-block`) now sits at tool response. [inference] Interpretation by AI: the source does not say at which layer it acts. It is placed there because cross-domain attacks can arrive in tool results.
- Layers renumbered: old 2 to 7 are now 1 to 6. The preview guardrail table uses the new numbers. Defender real-time protection for Foundry reads "3 and 6, plus user input and final answer".
- Quotes no longer cited on the page after this cut: `gr-fy-agprev`, `gr-fy-override`, `gr-fy-inherit`, `gr-cs-mod`, `gr-fy-harm`, `gr-fy-del`, `gr-fy-in`, `gr-fy-block`, `gr-gh-filter`, `gr-fy-out`, `gr-fy-flag`. They stay in the table so V1 to V202 keep their numbers.
- Reviewed text ledger: 23 rows removed, 8 added (six renumbered box titles, one new box line, the figure description). Label check passes with 173 texts.
- Not checked: the quote check against the live sources was not rerun.

## 2026-11-11: open questions removed

- Removed the five main open questions and renamed the section Gaps. No source was reread and no quote changed. The ledger lost 13 texts and gained the heading "Gaps".
- The only sourced statement in them, that no source says whether the Copilot policy or Registry covers only the built-in GitHub server, stays in the gap for that server, which says the two switches are untested.
- Not checked: the quote check against the live sources was not rerun.
