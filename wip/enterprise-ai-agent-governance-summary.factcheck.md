**Belongs to:** [enterprise-ai-agent-governance-summary.html](enterprise-ai-agent-governance-summary.html)

# Fact check ledger: governance summary
**Checked on:** 2026-11-06
**Method:** every factual claim in the route table, automation table and gaps is tied to an exact quote (ids V1 to V57) or labelled `unverified`, `inference` or `recommendation`. Quotes live in `scripts/governance_evidence.py`.
**Not tested:** nothing was run in a real tenant, on a consultant device or on an agent runtime. All verdicts come from documentation.

## Mechanical quote check

`python3 -I scripts/check-evidence-quotes.py <cache-dir>` fetched each source URL and looked for each quote word for word (curly quotes, non-breaking spaces and whitespace normalised). It also checks that the page lists every quote under `id="ev-Vn"`. Result on 2026-11-06: 88 quotes, 0 problems. V52 to V57 were added for the Agents Toolkit row and V58 to V65 for Defender local discovery and V66 to V69 for the firewall prerequisites, the Copilot Studio integration and the Defender cloud limit, and V70 to V72 for the Defender supported OS and minimum versions, V73 for report-only mode, V74 for environment group rules V75 for per-server tool control in the firewall, V76 and V77 for Copilot Studio traffic forwarding to Global Secure Access, and V78 to V80 for how the firewall is enforced and which profile Copilot Studio agents use, and V81 to V88 for the Intune firewall allow list (default outbound block, Windows 1809 and later, dynamic keywords with Intune, domain rule limits, highly secure environments, Graph create policy). V37 to V46 were added in the verification pass and V47 to V51 for the Agent Builder row, both on 2026-11-06.

This proves the words are on the page the URL serves today. It does not prove that the claim built on the words is right. Re-run it before moving "Documentation checked".

## Verdicts

| Block | Verdict |
|---|---|
| VS Code and GitHub row | Confirmed by V1 to V3 (publish, hourly apply), V4 (custom agent profiles exempt), V5 (built-in server exempt), V8 (coverage varies). "A person approves the pull request" is the recommended process, not a vendor fact. |
| Tools Gateway row | Confirmed by V9 to V13, V26 and V37 to V39. V37 shows blocking a tool in the admin center. V38 shows tool-level blocking needs the AI Gateway tier. V39 shows v1 tiers are unsupported. Allow or block by pipeline: unverified (the page documents the admin center only). Whether a new server starts allowed or blocked: unverified (searched the gateway and API Management pages, not stated). |
| BYO row | Confirmed by V14 to V20 and V42. V42 shows registration through the `a365` command line, so registration can be scripted. Approval is a person in the admin center. Approval from a pipeline: unverified. |
| Copilot Studio row | V21 confirms connector blocking also blocks MCP tools. V43 shows the `New-DlpPolicy` PowerShell command creates a data policy, so a pipeline could call it. Mapping the Git list to connector entries is our own build, labelled recommendation and untested. Moved from inference. |
| Foundry row | V22 to V24 confirm the approved-tools policy, Deny and the non-compliant marking of existing resources. V25 covers the Azure CLI route. Runtime blocking: inference (not shown). The pipeline is our own build and untested. |
| Agents Toolkit row | V52 says the Agents Toolkit adds an MCP server to a declarative agent as a plugin. V53 says a developer needs custom app upload enabled to sideload, so the admin setting matters. V54 says an admin can install, uninstall or block a plugin and set user availability. V55 says admins review plugin access requests and standalone MCP server registration requests. V56 says plugin availability grants no access to external services or data. V57 says a remote MCP server can have separate controls. Verdict: documented. Whether the Git list, the Agent 365 gateway or the network firewall applies to these plugins is not stated: unverified. |
| Agent Builder row | V47 confirms Agent 365 inventories Agent Builder agents. V48 says draft agents from Agent Builder are not shown. V49 says Agent Builder has no external-service actions. V51 says connectors and workflows need a copy to Copilot Studio. V50 says admins can switch Agent Builder on or off. MCP servers are not mentioned on the Agent Builder page: unverified (not observed). Per-server allow or block: not shown. The route is not in the 2.4 figure. |
| Local stdio row | V6 and V7 confirm the exact-command rule and the wildcard limit. V31 and V33 confirm Global Secure Access does not see local servers. V58 and V61 confirm Defender for Endpoint discovers supported local servers on devices, and is not a complete inventory. No source says Defender blocks a server (unverified). |
| Defender local discovery (path 4, local row, gap) | Checked 2026-11-06 against three Microsoft Learn pages, each last updated 2026-11-03. V58 discovers agents and their MCP servers. V59 needs antivirus active mode and real-time protection. V60 lists the details Defender can report. V61 not a complete inventory. V62 Plan 2 is the minimum license. V63 generally available on supported Windows and macOS, except preview scenarios. V64 the VS Code GitHub Copilot extension row has both ticks. V65 discovery does not prove use. Blocking: no source read shows it, labelled unverified. Corrects an earlier version of this page that said only the GitHub list reaches local servers. |
| Global Secure Access client and Copilot Studio (paths 2 and 6, firewall row) | The firewall page lists the client on an Entra joined or hybrid joined device (V66) and TLS inspection (V67) as prerequisites. The logging page lists two configurations: the client on the device, or the Copilot Studio integration that routes agent traffic through Global Secure Access (V68). The old text said cloud agent traffic never passes Global Secure Access; that was wrong for Copilot Studio and is corrected. The Power Platform page (read 2026-11-06, updated 2026-04-04) says forwarding covers custom MCP servers (V76) and that web content filtering, threat intelligence filtering and network file filtering apply (V77). It never mentions the MCP firewall policy. The firewall page says enforcement uses a Conditional Access policy (V78). The Entra page for Copilot Studio agents says profiles linked to Conditional Access are not currently supported for them (V79) and policies go in the baseline profile (V80). So the firewall most likely does not apply to Copilot Studio traffic. This is our reading, labelled inference, not tested in a tenant. |
| Network firewall row | V29 to V34 and V36 confirm preview, URL lists, remote-only scope, license and client prerequisites. Git feeding the URL lists: unverified. |
| Intune firewall allow list (matrix row, automation row, gap) | Checked 2026-11-06 against three Microsoft Learn pages. V81 all outbound connections without a matching rule are blocked. V82 Windows 1809 and later. V83 Firewall CSP usable with Intune. V84 block all outbound and allow specific outbound traffic. V85 domain rules need a DNS lookup. V86 limits: proxy, secure DNS, some VPN tunnels, cached addresses. V87 the block default is for certain highly secure environments. V88 Graph creates a configuration policy. Not shown by any source: Git feeding Intune, the Graph API writing dynamic keywords, macOS support. Those are recommendation or unverified. Nothing tested in a tenant. |
| Direct API row | V40 shows Agent 365 does not route agents through a customer-hosted gateway by itself. V41 says to restrict connectivity so the gateway is the only permitted caller. The old claim that no one tool blocks every path could not be shown either way, so it was replaced by the claim the quotes support. Enforcing at the API or data source is a recommendation. |
| API Center row | V27 and V28 confirm inventory and continuous sync. V44 confirms registered servers can be integrated with the Foundry tool catalogs. Blocking is not described: inference. Whether the catalog stops agents from using other tools: not shown, unverified. |
| Tool-to-job table | V35 says E7 includes the Entra Suite. V45 confirms Conditional Access in E7. Prices are not on this page (the price page returned HTTP 403 to the checker on 2026-11-06). V46 says most organizations get Intune in bundles such as E3, E5 or E7. The Intune price page returned HTTP 403, so Intune is stated only as "bundles such as", not as a line item. Other rows point to the row they summarise. |
| Traffic figure and path table (below the 2.4 figure) | Seven paths, each with a quote. 1: V1, V2, V3, V5, V8. 2: V34, V32, V36. 3: V29 to V31 and V33. 4: V31, V2, V8. 5: V10, V13, V14, V15, V20. 6: V40, V41. 7: V21 to V24. Quotes show the device-side parts: V31 (local servers run on a device) and V34 (the client is installed on the device). That the cloud boxes sit outside the client, and that a cloud agent's traffic does not pass the device client, is inference and is labelled. Figure text holds labels only. Verdicts for each text are in the reviewed list, which proves a verdict was recorded for that wording, not that it is right. |
| Reused blocks (2.4 figure, five-points figure, tiers, action policy, checklist, runbook, nine rules) | Copied from the long page. Their wording is covered by the long page's own fact check. The sentence "Microsoft recommends this for agent policies." was dropped from the nine-rules table because no source was found for it on this review. |

## Not checked

- Own-process wording: pull request approval, merge as the publish trigger and the pipeline steps are our design, now labelled recommendation. No source describes them.
- Agent platforms not on this page: V47 names SharePoint, Researcher and non-Microsoft platforms, and the Defender matrix lists many more local agents. Not added.
- Defender: prerequisites re-read on the Learn page on 2026-11-06 and quoted (V59, V62, V69 to V72): cloud, Plan 2, active mode, supported OS, minimum versions. Which local servers Defender really finds on our devices: nothing tested. Whether Defender can block a local server: not shown in the pages read. Defender AI agent runtime protection (public preview, page updated 2026-10-09) is a separate feature: it blocks agent actions on prompt injection, not unapproved MCP servers. Not covered on the page.
- Reused blocks (risk tiers, action policy, checklist, runbook, target-state figure, seven of the nine rules) are design choices. They are labelled recommendation and no source can confirm them. The two rules that rest on a product fact are quoted (V73, V74).
- The GitHub Actions claim from the long page has no text quote, so it is not asserted here.
- Foundry runtime blocking: searched the Azure Policy, deny and API Center pages on 2026-11-06, nothing shown. Kept as inference.
- Whether the firewall URL lists can be fed from Git. A Microsoft Graph mention was seen for retrieval only. Kept as unverified.
- Whether a new gateway server starts allowed or blocked. Kept as unverified.
- Whether MCP servers added through Agents Toolkit show in the Agent 365 Tools page or pass the gateway. The two Learn pages read do not say. Kept as unverified.
- Traffic figure: where Copilot Studio, Agent Builder and Foundry run, and whether their MCP calls ever pass a device client. No quote says. Kept as inference.
- Traffic figure: whether the firewall also inspects traffic from agents in the cloud. The firewall page read describes the device client only.
- Any behavior in a real tenant. Each "we cannot" and "we can" is documentation only.

## Reviewed presentation text

Text outside the evidence table (titles, headings, chips, lead, questions, answers, flow steps) holds design requirements and labels only. `python3 -I scripts/check-enterprise-agent-labels.py enterprise-ai-agent-governance-summary.html` fails when a text is missing from this list, changed since review, or uses fact-style wording. The script proves a verdict was recorded for the exact wording, not that the verdict is right.

<!-- Begin reviewed presentation text -->
```text
label	Governing MCP servers summary
label	Governing MCP servers and AI agents
requirement	How we govern MCP servers and what to do with them. The page shows what we can do, what we cannot do and which tool does the job, then the target state. Open questions are at the end.
label	Decision makers
label	Platform and security owners
requirement	See how the approved list is governed and what each route can do.
label	Architects
requirement	See the target state and which tool does which job.
label	Open questions
label	recommendation
requirement	Is Git the one source of the approved MCP list?
requirement	Every route then takes its entries from one reviewed file. Without it, each platform keeps its own list and the lists drift. See how the list is governed.
requirement	Who owns the list, and who approves tiers 2 and 3?
requirement	Name an owner for the list and for each server. Security and the data owner approve tiers 2 and 3. See the risk tiers.
label	How we govern MCP servers
label	Answer recommendation
requirement	Keep one approved MCP list in Git, and publish it by pull request into each technology's own control: the GitHub settings file for VS Code and Copilot, the Agent 365 registry or gateway for agents, data policies for Copilot Studio, Azure Policy for Foundry, and the network firewall for remote servers.
requirement	No single control covers every agent, so combine these, restrict direct API access with permissions at the source, and accept that most of these are previews that are untested in our tenant (see the route table).
label	MCP server approval and enforcement
requirement	Proposed workflow from left to right. A rejected request is closed with a reason. An approved request goes into Git for automatic distribution to four destinations. The catalog is a separate discovery branch. Before enabling a route, verify enforcement and keep failed routes disabled. Monitor enabled routes and revoke access on incident.
label	1. REQUEST
label	2. REVIEW
label	3. APPROVE
label	4. AUTO-PUBLISH ON MERGE
label	5. VERIFY
label	6. USE
label	GitHub request
label	pull request
label	owner, data, risk tier
label	Security review
label	server checklist
label	rejected
requirement	Close request
requirement	record the reason
label	Approved list
label	reviewed pull request
label	merged into Git
label	VS Code and GitHub Copilot
code token	managed-settings.json
requirement	Check client coverage
label	Agent 365 registry
label	API Management registration
requirement	Check server allow or block
label	Foundry
label	Azure Policy assignment
requirement	Check configuration scope
label	Azure API Center
label	Catalog and discovery
requirement	Check catalog publication
requirement	Verify enforcement
label	configuration and calls
label	pass
requirement	Enable use
label	tested routes
label	fail
requirement	Keep disabled
requirement	resolve the gap
label	Monitor
label	calls and decisions
label	incident or failed review
requirement	Block and revoke access
requirement	block gateway and client routes
requirement	revoke backend permissions and verify the stop
label	Proposed workflow step
label	Catalog route
requirement	Keep disabled or revoke
label	Request and review
requirement	Submit a pull request with the owner, data, tools and risk tier. Record the approval or rejection.
label	Publish the approved list
requirement	Trigger distribution on merge. Record the policy version and result for each destination.
requirement	Check the outcome
requirement	Record discovery, applied configuration and verified enforcement separately. Complete any required administrator step.
label	Enable and monitor
requirement	Enable only tested routes. On incident, block access and verify revocation.
label	Risk tiers recommendation
label	Read-only, internal, no sensitive data
label	Internal case search
requirement	Automate checklist checks. Record approval in the pull request.
label	Read-only, sensitive data
label	HR or finance reads
label	Security and data owner
label	Can change data or call out
label	Create tickets, send mail, deploy
requirement	Security and data owner approve publication. Apply the action policy at run time.
label	Third-party operated or untrusted code
label	Community MCP servers
requirement	Default deny. A recorded exception must still meet the action policy.
label	Approval for tools and actions recommendation
label	Before publication
requirement	Review the endpoint, tool version, schema, data and permissions in the pull request. Security and the data owner approve tier 2 and tier 3 tools. Tier 4 also needs an exception.
label	For each call
requirement	Check that the caller may use this server, tool and resource. Apply access checks independently of the model.
label	For a write or outbound action
requirement	Require an authorized request or approved trigger. Require human approval for high-impact actions and actions outside an approved rule. A rules service may approve only explicitly approved low-risk actions, bounded by tool, permitted inputs, target and data. Deny if the required approval is absent.
label	For execution
requirement	Use a separate, narrowly scoped identity to execute an approved action. Record the approval and outcome.
label	Server checklist recommendation
label	Named owner
label	Purpose
label	Publisher and source
label	Authentication type
label	Data it can read
label	Actions it can take
label	Logging available
label	How to disable it
label	Review date
label	What we can and cannot do, route by route
label	VS Code and GitHub Copilot GitHub managed-settings.json
label	preview
label	Agent 365 Tools Gateway preview Agent 365 with Azure API Management
label	unverified
label	Agent 365 bring-your-own registry preview Agent 365 BYO MCP
label	Copilot Studio Power Platform data policies
label	Agent Builder Microsoft 365 Copilot, users build their own agents
label	Agents Toolkit Microsoft 365 Agents Toolkit, developers build declarative agents with MCP plugins
label	inference
label	Foundry agent tools preview Azure Policy approved tools
label	Local MCP via stdio GitHub serverCommand list
label	Network MCP firewall preview Global Secure Access, Entra Internet Access
label	Intune firewall allow list Intune, Windows Firewall
label	Direct API or data access Permissions at the API or data source
label	Azure API Center catalog API Center
label	The target state, as part of the governance
requirement	The target state is the same approved list, enforced in layers. Git holds the policy. Each platform enforces it with its own control. Consultants work from a managed desktop. Agents get their own identity, start read-only and need approval for high-impact actions. Logs and revocation close the loop.
requirement	Apply one policy through each platform's own controls
requirement	Verify where each control applies before enabling a route. Compare the routes.
requirement	Allow only approved MCP servers and tools
requirement	Start from default deny where supported. Test the exceptions and block or restrict alternate paths. Review and publish the approved list.
requirement	Keep code and sensitive data on managed devices
requirement	Give consultants on personal laptops a managed cloud desktop for work. Set up identity and device access.
requirement	Give agents their own identity and least privilege
requirement	Start with read-only access. Require human approval for high-impact actions. Use rules only for explicitly approved, bounded low-risk actions. Read the action policy.
label	Manage policy changes in Git
requirement	Require an approved pull request, publish the list automatically and verify the deployed policy. Follow the publication workflow.
label	The five points on the target state
requirement	Proposed design. A policy repository in Git feeds changes through an approved pull request and automatic publication into each platform. Consultants work through a managed cloud desktop. Each agent has its own identity, starts read-only and needs human approval for high-impact actions. Tool access allows only approved MCP servers and tools. Data protection and audit sit below. The deployed policy is checked against Git.
label	5
label	POLICY CHANGES IN GIT
label	Policy repository in Git
requirement	approved list, rules, settings
label	Approved pull request
requirement	review before merge
label	Automatic publication
requirement	on merge, no manual edit
requirement	publishes to each platform
label	PEOPLE AND DEVICES
label	Staff
label	managed device
label	Consultants
label	personal laptop
label	Managed cloud dev desktop
label	Dev Box, Windows 365 or Azure Virtual Desktop
label	3
label	Microsoft Entra ID
label	MFA, Conditional Access, B2B guests, access reviews, agent identities
requirement	each agent has its own identity
label	4
label	DEVELOPMENT
label	VS Code + Copilot
label	GitHub Enterprise
label	policies, PR review, scans
label	CI/CD
label	checks, release approval
label	release
label	1
label	AGENT PLATFORMS
requirement	one policy, each platform's own controls
label	Copilot Studio
requirement	native policy controls
label	Microsoft 365 Copilot
label	AGENT ACTIONS
label	Read-only start
requirement	no write access at first
label	Human approval
requirement	for high-impact actions
label	Rules
requirement	only bounded, low-risk actions
label	2
label	TOOL ACCESS
label	Agent 365 MCP registry
requirement	approval and revocation
label	Agent 365 route
label	Azure API Management
label	Foundry tool gateway
label	limits in 2.6
requirement	catalog and discovery
label	catalog route
label	Approved MCP servers
label	backend authorization
label	Approved list only
requirement	servers and tools, nothing else
label	Default deny
requirement	where the platform supports it
label	Other routes
requirement	blocked or restricted, then tested
label	DATA
label	Purview labels and DLP
label	data protection design in 2.7
label	SharePoint, repos, APIs
label	permissions enforced at the source
label	AUDIT AND MONITORING
label	Audit and monitoring
label	Entra, GitHub, Purview, Defender, Sentinel, Agent 365 inventory
label	VERIFY
label	Verify deployed policy
requirement	compare with Git
label	Proposed design
label	n
label	nNumber of the point above
requirement	Proposed design. Policy flows from Git down into each layer. Work access flows from the managed desktop. Compare with the full target state.
label	Which tool does which job
label	Automation and admin work
label	Monitor and stop an agent
label	Find the affected calls
requirement	Use the tool-call record to identify the caller, route, tool, resource and decision.
label	Contain the route
requirement	Disable the agent and block the affected client or gateway route. Use the route matrix to locate other paths.
label	Revoke at the source
requirement	Remove tool or backend permissions and update the approved list in Git. Record each change.
label	Verify the stop
requirement	Retry from an existing agent and any permitted alternate path. Confirm denial and correlate the events before restoring access.
label	Known gaps and what has not been tested
label	Bad news first
label	Preview watchlist
label	The gaps
label	Quotes behind the route table
label	Check product scope and coverage
requirement	Do we accept preview controls?
requirement	Enable only the routes that fit our needs. Keep the rest disabled. The route table shows what each route can and cannot do.
requirement	Go to the open questions.
requirement	Proposed workflow. Record delivery, configuration and enforcement separately. Check GitHub and VS Code, Agent 365, Foundry and API Center in the route matrix. Follow the revocation procedure.
requirement	Run the checks
requirement	The watchlist names every control that its vendor labels preview. Decide whether we use them, and who re-checks them each month. See the preview watchlist.
requirement	Which routes do we enable?
label	6
label	7
label	Agent 365 gateway
label	Agents in the cloud
label	Copilot Studio, Foundry
label	Data policy, Azure Policy
label	END USER DEVICE (THE CLIENT)
label	GitHub settings file
label	Global Secure Access
label	Local MCP server
label	MCP firewall
requirement	MCP traffic paths and the end user client
label	NOT THE USER'S CLIENT: CLOUD AND NETWORK
requirement	Proposed view of where MCP traffic flows. The left zone is the end user's device and holds VS Code with GitHub Copilot, a local MCP server and the Global Secure Access client. The right zone is not the user's client and holds the GitHub settings file, the MCP firewall, agents in the cloud, the Agent 365 gateway and remote MCP servers. Seven numbered paths are explained in the table below.
requirement	Proposed view. Numbers match the paths in the table below. The placement of the cloud services is interpretation by AI.
requirement	Red dashed box: preview
requirement	Red dashed line: path with a gap
label	Remote MCP servers
requirement	Solid line: policy or traffic
requirement	Where MCP traffic flows, and what is the end user's client recommendation
label	approved or not
label	client on the device
label	end user client
label	or registry
label	stdio, on the device
```
<!-- End reviewed presentation text -->
