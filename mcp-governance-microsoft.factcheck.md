Belongs to: [MCP Governance in a Microsoft ecosystem](mcp-governance-microsoft.html)

# Fact check: MCP Governance in a Microsoft ecosystem

Documentation checked: 2026-11-11.

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

## 2026-11-11, control planes pass (latest)

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
label	SOURCE OF TRUTH
label	APPLY ON MERGE
label	GIT REPOSITORY
label	PIPELINE
label	Change by pull request
label	Runs after merge
label	COPILOT STUDIO
label	FOUNDRY
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
label	AI GATEWAY, PREVIEW
requirement	Publish MCP endpoints
requirement	Tool threat protection
requirement	Connect gateway
label	AGENT 365, PREVIEW
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
requirement	Who approves and reviews the Agent 365 consent?
requirement	The consent lets the service write API policies. Name an approver and a reviewer. See the controls.
requirement	What ends the pilot?
requirement	Set the exit evidence now: terms accepted, features released, clients covered. Without it the pilot has no end. See the fallback.
requirement	Does a gateway with no private endpoints fit the network rules?
requirement	The new resource has no private endpoints. Check the rules before building. See the gaps.
requirement	Is the built-in GitHub MCP server acceptable on managed clients?
requirement	The allow and deny lists cannot block it. Choices: accept it, turn off the MCP servers in Copilot policy (stops all servers), or limit it through GitHub account permissions. inference No source checked says whether that policy or Registry only covers the built-in server. Test both in a pilot.
label	inference
requirement	Which Agent 365 route will the pilot use?
requirement	Choose the API Management gateway integration or the separate BYO server registration route. See the controls.
label	Fact check
label	Parts of the design
requirement	Choices: never, in a sandbox only, or later. Require released features for production. The proposed pipeline and cross-client enforcement still need validation.
label	Controls
requirement	Are preview features allowed at all?
label	Environments
label	Fallback
requirement	Released only is the baseline. Compare it with the preview design, then read the open questions.
label	(Preview)
label	(default: always)
label	1 USER INPUT
label	2 WHICH SERVER
label	3 PERSON APPROVES
label	4 CALL CONTENT
label	6 COMPANY MCP SERVER
label	7 TOOL RESPONSE
label	8 FINAL ANSWER
label	Allow and deny lists
label	Built-in prompt attack
label	Confirmation dialog
requirement	Design target: only the gateway can call it. See the design above
label	FOUNDRY AGENT
label	Guardrails by layer
label	None found
label	Not stated
label	Preview only
label	Threat detection (Preview)
label	Tool call guardrail
label	Tool response guardrail
label	VS CODE, GITHUB COPILOT
label	What each guardrail does
code token	allowed_tools list
label	block (UPIA, XPIA)
code token	require_approval
label	unverified
code token	(empty = all tools)
label	(interpretation by AI)
label	(see below)
label	ANY LAYER: Copilot Studio content moderation. The sources checked do not say at which layer
label	Data policy: whole server
label	Defender rule (Preview)
label	GUARDRAILS ALONG ONE MCP TOOL CALL (request goes down, response comes back)
label	Harm levels
label	MCP is not on its list
label	No reply in 1 s: allowed
requirement	Outbound rules, then API Management: check identity, authorize, limit rate, log
label	Preview: tool threat protection
label	Prompt attack check
label	Protected material (flag)
label	response comes back
label	(by default)
label	(layer: AI estimate)
label	5 NETWORK AND GATEWAY
label	Agent 365 path only: Defender rule checks tool calls to MCP tools onboarded there
requirement	Every client, from the design above
label	Foundry only: Network control limits outbound traffic for hosted and Copilot-harness agents
label	Foundry only: hosted agents run in a VM sandbox
label	(policy, managed settings)
label	(default: Manual)
label	(for MCP: unverified)
label	(source says 'may')
label	Allow all skips it
label	Ask user before running
label	Can be set to never
label	Can be switched off
label	FOUNDRY: agent guardrails (Preview). With none set, the agent uses its model's guardrail
label	GitHub content filter
label	Guardrails by layer for one MCP tool call, in three columns: Foundry agent, Copilot Studio, and VS Code with GitHub Copilot. Layer 1 user input: Foundry has harm levels and a prompt attack check, Copilot Studio has a built-in prompt attack block, whose layer is an AI estimate, and GitHub says its content filter may scan prompts. Layer 2 which server: Foundry allowed_tools, Copilot Studio data policy, VS Code and GitHub allow and deny lists plus a server trust prompt in VS Code. Layer 3 person approves: Foundry require_approval, default always, which can be set to never. Copilot Studio can ask the user before running a tool, off by default and unverified for MCP tools. VS Code shows a confirmation dialog by default, the Allow all level skips it, and a company policy can lock it. Layer 4 call content: Foundry has a tool call guardrail in preview that does not list MCP, Copilot Studio has threat detection in preview that by default allows the call after one second without a reply. In VS Code a preToolUse hook can deny a call, unverified for MCP tools. Layer 5 network and gateway: the design above applies to every client, with tool threat protection in preview, plus a Defender rule for tool calls to MCP tools onboarded to Agent 365 and two lines that apply to Foundry only. Layer 6 company MCP server: the design target is that only the gateway can call it. Layer 7 tool response: Foundry has a tool response guardrail in preview that does not list MCP, none found for Copilot Studio. VS Code can ask for a review of the result before it enters the chat context, and this can be switched off. Layer 8 final answer: Foundry has harm levels and a protected material flag, Copilot Studio is not stated, and GitHub says its content filter may scan answers. Below the figure: Copilot Studio content moderation has no stated layer. Foundry agent guardrails have preview status, and with none set the agent uses the guardrail of its model. In preview, a Microsoft Defender real-time protection rule also applies for Foundry at layers 1, 4, 7 and 8 and for Copilot Studio at layer 4. Defender for Endpoint runtime protection, in preview on Windows, lists the VS Code GitHub Copilot extension, with no layer stated.
label	Guardrails by layer for one MCP tool call, in three columns: Foundry agent, Copilot Studio, and VS Code with GitHub Copilot. Layer 1 user input: Foundry has harm levels and a prompt attack check, Copilot Studio has a built-in prompt attack block, whose layer is an AI estimate, and GitHub says its content filter may scan prompts. Layer 2 which server: Foundry allowed_tools, Copilot Studio data policy, VS Code and GitHub allow and deny lists plus a server trust prompt in VS Code. Layer 3 person approves: Foundry require_approval, default always, which can be set to never. Copilot Studio can ask the user before running a tool, off by default and unverified for MCP tools. VS Code shows a confirmation dialog by default, the Allow all level skips it, and a company policy can lock it. Layer 4 call content: preview only for Foundry and Copilot Studio. In VS Code a preToolUse hook can deny a call, unverified for MCP tools. Layer 5 network and gateway: the design above applies to every client, plus two lines that apply to Foundry only. Layer 6 company MCP server: the design target is that only the gateway can call it. Layer 7 tool response: preview only for Foundry, none found for Copilot Studio. VS Code can ask for a review of the result before it enters the chat context, and this can be switched off. Layer 8 final answer: Foundry has harm levels and a protected material flag, Copilot Studio is not stated, and GitHub says its content filter may scan answers. Below the figure: Copilot Studio content moderation has no stated layer. Foundry agent guardrails have preview status, and with none set the agent uses the guardrail of its model.
label	Off by default
label	Policy can lock it
label	Result review before it
label	Server trust prompt
label	VS CODE: Defender for Endpoint runtime protection (Preview, Windows). Layer not stated
label	enters the chat context
label	may scan answers
label	may scan prompts
label	preToolUse hook can deny
requirement	A proposed design for governing MCP servers across GitHub Copilot, VS Code, Foundry, Copilot Studio and Microsoft 365 Copilot.
label	Agent 365 not drawn: company servers join it through preview features
requirement	Approved connectors
requirement	By hand
requirement	By pipeline
label	Control planes
requirement	Design target: a Git repository holds the approved and denied MCP servers. A reviewed pull request changes it. After merge, a pipeline applies the list to three targets: Power Platform policy for Copilot Studio, GitHub Enterprise managed settings, and Foundry. A fourth target, the Microsoft 365 admin center, is set by hand. Each target names where it is administered and points to the clients it governs: Copilot Studio, VS Code with GitHub Copilot, Foundry agents and Microsoft 365 Copilot. The first three pass through client controls, Windows outbound firewall rules where applicable, API Management and the company MCP server, which only the gateway can reach. Microsoft 365 Copilot calls API Management from the Microsoft cloud, from fixed outbound addresses, and skips the client controls. A direct call from a client to the server is blocked. Agent 365 is not drawn: company servers join it through preview features.
label	Approval boundaries and cross-cutting guardrails
label	Foundry portal
label	GITHUB ENTERPRISE
label	MICROSOFT 365
label	Managed settings
label	Microsoft 365 Copilot
label	Microsoft 365 admin
label	Microsoft cloud, fixed outbound addresses
requirement	Name the reviewers of the repository, the pipeline owner and the person called when a target fails to update. Name who applies the list by hand in the Microsoft 365 admin center.
label	POWER PLATFORM
label	Power Platform admin
label	TARGETS
label	center
label	repository
label	Approval and denial workflow
label	AGENT 365 ADMIN VIEW
label	Agents > All agents
label	Tools: Available/Blocked
label	Requests (preview)
label	(preview)
label	COMPANY GOVERNANCE
label	M365 ADMIN CENTER
label	SECURITY REVIEW
label	APPROVE
label	DENY
label	STOP
label	REJECT
label	Registry: AVAILABLE
label	LATER DENY: BLOCK SERVER NOW,
label	MARK DENIED IN GIT, SYNC TARGETS,
label	TEST THAT CALLS FAIL
label	Requester adds server, owner,
label	auth, tools, and risk to Git
label	Developer registers server
label	after the internal PR merges
label	Review server and each tool
label	Agents > Tools > Requests
label	Review requester, URL,
label	auth, tools, permissions
label	Merge approved
label	inventory
label	Record denied
label	reason in Git
label	Grant Entra consent
label	Keep unavailable;
label	record reason in Git
label	Apply target policies
label	and backend authorization
requirement	Design target: the released-only design with preview additions. A Git repository holds the approved and denied MCP servers. After a reviewed merge, a pipeline applies the list to Power Platform policy for Copilot Studio, GitHub Enterprise managed settings and Foundry. A fourth target, the Microsoft 365 admin center, is set by hand. Each target names where it is administered and points to the clients it governs: Copilot Studio, VS Code with GitHub Copilot, Foundry agents and Microsoft 365 Copilot. The first three pass through client controls, Windows outbound firewall rules where applicable, Azure AI Gateway with tool threat protection, and a company MCP server that only the gateway can reach. Microsoft 365 Copilot calls the gateway from the Microsoft cloud, from fixed outbound addresses, and skips the client controls. A direct call from a client to the server is blocked. Below the gateway, the Microsoft 365 admin view shows the all-agents registry, MCP server status, and the preview requests queue.
requirement	A developer proposes a server in the reviewed Git inventory. A security reviewer approves or rejects the pull request. Rejection stops the request and is recorded as denied. After approval and merge, the developer registers the server through the Agent 365 preview flow. An administrator reviews the request in Microsoft 365 admin center Requests preview and approves or rejects it. Rejection leaves the server unavailable and the reason is recorded. Approval is followed by Microsoft Entra tenant consent; only then does the server become Available in the tools registry. The admin records the approved server and consent in the inventory, applies target-specific access controls, and monitors calls. A later deny blocks the server in the tools registry and updates the inventory and other policy targets.
requirement	The Git pull request is the internal source-of-truth decision. The Microsoft 365 admin-center request is a separate product approval for the preview BYO route. Rejecting either stops rollout. The registry status is Available only after admin approval and required Microsoft Entra consent. V184 V185 V87
requirement	With preview, connect the API Management gateway to Agent 365 and test tool threat protection in a sandbox. The view combines distinct admin pages: Agents > All agents > Registry, and Agents > Tools > Registry or Requests (preview). V182 V183 V189 The BYO server route is separate; its limits are listed below.
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
