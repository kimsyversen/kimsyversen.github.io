# 10 November 2026: risk-by-zone table scope and controls

This review supersedes the 9 November check for the risk-by-zone table. The page now shows each mapped component with its related finding, requirement, or control, exposes an exact quote and source link where the claim has a registered quote, and links each risk to its full checklist. “No mapped component” means this reference scenario assigns no component to that zone. It does not claim that no control exists.

New Microsoft policy claims were checked against primary documentation retrieved on 10 November 2026. The General-view sandbox and approval recommendations reuse MCP specification and CoSAI evidence reviewed on 9 November 2026:

- **M03 / Device policy, General view:** the page recommends requiring local servers to run sandboxed with minimal default privileges, tagged `[inference]`. It also says covered Copilot allowlists can match specific commands but do not verify code or provide runtime isolation, tagged `[inference]`. Evidence: `localsandbox`, `gh1`, `gh2`, `gh4`.
- **M03 / Device policy, Microsoft view:** the same Copilot command allowlist is shown with its scope and limitations. Windows On-device Agent Registry can control server access per agent, but it is prerelease and specific to that registry. Evidence: `gh1`, `gh2`, `gh4`, `odr2`, `odr4`.
- **M09 / Device policy, General view:** requiring human approval for high-impact tools and keeping prompts reviewable is a recommendation, tagged `[inference]`, based on the specification and CoSAI's human-in-the-loop and approval-fatigue risks. Evidence: `spt1`, `cs9`, `cs13`.
- **M09 / Device policy, Microsoft view:** VS Code's enterprise policy can make selected tools ineligible for auto-approval; the documentation says those tools always request confirmation. Evidence: `vp2`.
- **VS Code tool-approval row:** the new `ChatToolsEligibleForAutoApproval` control and its confirmation behavior were checked against the policy reference. The distinction from global auto-approval remains explicit.

The table still does not assert every control available for every product. Detailed risk checks remain in the risk cards. Browser status is self-reported, and no client policy or command was run. The quote checker verifies source wording and source links, not enforcement behavior.

# Final statement and MECE audit: 9 November 2026

This audit supersedes earlier completion claims and stale wording in the historical inventories below. The authoritative content is the current HTML and its generated data. The earlier claim that quote matching established correct attribution was false: four Copilot Studio quote identifiers had been overwritten by CoSAI quotes. Valid quotation text alone does not establish support for the attached claim.

## Scope, method and verdict

Reviewed the static prose, all 14 cards, the framework mapping, general placements, Microsoft cards and placements, product rows, first actions, labels and evidence declarations. Retrieved the external source set again into a fresh cache on 9 November 2026. Reviewed documentation as documentation; vendor claims are not measurements of enforcement. Research is attributed to its authors; CVE records are advisories, not independently verified victim incidents.

MECE applies to individual control failures within the 10 OWASP and 34 CoSAI entries, not to entire attacks or to the overlapping source taxonomies. The classification-boundaries section defines a single home and explicit exclusions for each failure. Attack chains can contain different failures. Broad entries #24 and #27 have related-control references instead of implying their entire scope is exclusive to their assigned home. Outside-scope findings remain unclassified. These classification decisions are interpretation by AI [inference], not a claim made by either framework.

## Final corrections and evidence

| Content reviewed | Verdict on 9 November 2026 | Evidence / reason |
| --- | --- | --- |
| Card labels and 44 framework entry homes | Corrected and checked | OWASP project page and CoSAI numbered threat list; M01 home is #6, M02 homes are #5, #25, #32. M13 owns tool definition poisoning. Exact ID coverage and distinct OWASP homes checked. |
| Boundaries for all 14 cards | Interpretation by AI [inference] | Distinguishes provenance, execution, model instructions, tool definitions, credentials, privileges, access checks, oversight, network reach, transport integrity, data isolation, resource limits, admission and visibility. Each definition names adjacent exclusions. |
| Claims that OWASP does not cover oversight, costs or transport | Removed | An absent category name does not establish absent coverage. The page now states its own classification choice. |
| Copilot Studio authentication, query keys, SSE and DLP | Citation attribution corrected; verified against source | Restored four quotations from the Copilot Studio add-server and DLP pages, now studio1 to studio4. cs1 to cs34 belong only to CoSAI. |
| Microsoft permission breadth | Supported documentation summary | Azure MCP Server security asks users to review their signed-in identity's access. M06 now holds this fact. |
| Microsoft approval controls | Supported documentation summary | Visual Studio tool confirmation and auto-confirm documentation now have their home in M09. Removed the false claim that no Microsoft source had been reviewed for M09. |
| Windows isolation | Supported documentation summary | Windows on-device registry prerelease documentation. Moved to M03, with preview qualification retained. |
| VS Code tool approval and server sampling risk links | Corrected interpretation by AI [inference] | Approval links to M09; model exposure and background requests link to M06/M11, not audit visibility. |
| VS Code discovery and configuration destinations | Updated from current documentation | Add MCP servers now documents Customizations / Marketplace as the default browse route, Copilot Global configuration, experimental guided workspace-root setup, and compatibility destinations labelled deprecated in that flow. Removed obsolete general gallery-preview wording. Routes explicitly non-exhaustive. |
| Remaining VS Code rows | Supported with harness and platform limits | Manage MCP servers, MCP configuration, AI security, enterprise policies, managed AI settings, telemetry and sandboxing pages freshly retrieved. No assumption that editor policies cover independently discovered runtime servers. |
| General client restrictions, command identity and token guidance | Supported with stated exceptions | Claude managed MCP, Codex managed configuration, MCP security best practices, transports and tools. Command matching does not validate executable contents. Narrow scopes are separate from token lifecycle. |
| Bearer-token explanation | Qualified | RFC 6750: validity, scope, expiry and revocation constrain reuse. |
| Mitiga and Invariant research, two Azure CVEs | Attributed source reports | Existing prerequisite, client scope, persistence and incident qualifications retained. No exploit reproduced. |
| M10 to M12 Microsoft coverage | Explicitly unassessed | General framework guidance remains visible; no new product capability is inferred from it. |
| First actions, findings, diagram placements and friction | Interpretation by AI [inference] | Recommendations and representative scenarios, not measured prevalence, guarantees or vendor endorsements. Footer defines every [inference] marker as interpretation by AI. |
| Status controls and section roles | Artifact definitions | Browser status is self-reported; OK requires the reader's own evidence. No evidence is stored in the tracker. Map, matrix and mapping are related views, not additional risks. |

Primary source URLs and exact quotations remain in the page data and source register below. The online checker compared all 135 quotations with freshly retrieved source text, including their CoSAI PDF pages. It validates the exact 10/34 ID sets, distinct OWASP homes, static card labels, quote namespaces and 98 distinct Microsoft-view presentation strings against the recorded verdicts. Two quotations, `cxcmd` and `studio3`, matched after whitespace normalization. A passing check is evidence consistency, not proof of product enforcement.

## Evidence moved from the reader-facing tab

The separate Evidence and Sources tabs have been removed, and the Risks tab is hidden from navigation at the owner's request. Risk details remain available from map markers and direct links. This file is the authoritative home for evidence, source register, statement inventory, verdicts and review limits. The former `#evidence-status` and `#sources-2` fragments are retained as aliases into Risks.

## Validation and limits

- Earlier browser checks covered 1440px and 375px, light and dark, both scopes, and five tabs. They predate removal of the Evidence and Sources tabs and hiding Risks from navigation. The current page has three tab panels and two visible navigation tabs. A fresh browser check could not be completed because the browser would not open the local workspace page.
- Framework mapping: All = 14 risks / 44 entries, OWASP = 10 / 10, CoSAI = 14 / 34 in both scopes. The static link-routing code opens Risks for its deep links and reveals a filtered-out risk; these behaviors were not rechecked in a browser after the navigation change.
- Section anchor and quote/label checks pass. Index entry and footer already carry 9 November 2026; the description remains aligned with the 10/14 risk views.
- No managed-product configuration, exploit reproduction, end-to-end OAuth test or per-marker manual mouse audit. No claim of exhaustive coverage outside the cited frameworks.
- Reviewed HTML SHA-256: `4aaa95e601679274c7c170e43a42911cbdc1f54ae55237b81631aac2950d8c95`.

## Historical audits below (superseded where wording differs)

Belongs to [MCP-Risk-Map.html](MCP-Risk-Map.html).

# Framework selector and CoSAI review: 9 November 2026

Scope: the new Risk list buttons (All, OWASP MCP Top 10, CoSAI), the four new risks M09 to M12, every placement the CoSAI paper touches, and the placements found wrong in the earlier review. Method: read the CoSAI PDF (27 pages, 34 threats in twelve categories), compared each threat with the twelve risks, tied every added sentence to a quote, and ran `scripts/check-mcp-risk-map.py`. The check script matched 127 quotes, including every CoSAI quote on the PDF page it cites, and matched all 10 OWASP names and all 34 CoSAI names to their sources.

## Placement corrections

- **M05, token reuse:** Mitiga's reuse of the captured Atlassian token sat on the local HTTP server box. It is a call to the remote Atlassian MCP server, so it moved to Remote MCP servers. A separate M05 row now covers the localhost proxy (quote `mitlocal`).
- **M06, confused deputy:** the OAuth proxy rule sat on SaaS and Azure APIs. The rule is about an MCP proxy server, so it was merged into the Remote MCP servers row, next to the token-audience rule.
- **M07, self-reference:** the AI host row repeated a sentence about itself. It now says only what the quote says.
- **Header counts:** "top 10" wording was removed. The page no longer claims the ten OWASP names are the whole list.

## Mapping (updated 9 November 2026, MECE pass)

Each OWASP entry and each CoSAI threat has one home risk, and each OWASP entry has a different home, so the OWASP view shows exactly ten risks. The assignment is interpretation by AI `[inference]`. The page has the full table under Risks.

- OWASP: MCP01 M05, MCP02 M06, MCP03 M13, MCP04 M02, MCP05 M03, MCP06 M04, MCP07 M14, MCP08 M08, MCP09 M01, MCP10 M10.
- CoSAI adds four risks of its own: M07 (network reach), M09 (approval and over-trust), M11 (cost), M12 (transport). CoSAI #10 (multitenancy) is not a separate risk: it is the same subject as OWASP MCP10 and sits under M10.
- Partial fits, labelled on the page: OWASP MCP03 also names tool outputs, which the page keeps under M04; OWASP MCP05 also touches M04; CoSAI #28 is about stdio streams (home M12, also M03).
- Before this pass, M02 held MCP03 and MCP04, M06 held MCP02 and MCP07, and M08 held MCP08 and MCP10. They were split (new M13 and M14) so no risk merges two OWASP entries.

## Text added or changed in the MECE pass (9 November 2026)

| Where | Statement | Source | Verdict |
|---|---|---|---|
| M02 | A tampered package, a bad update or a look-alike name brings malicious code in. | OWASP MCP04 name; CoSAI #5, #25, #32 (quotes on the card) | SUPPORTED, wording is interpretation by AI |
| M03 | OWASP command injection definition (quote `owcmd`) | OWASP MCP05 page | VERIFIED by the checker |
| M13 | OWASP tool poisoning definition (`ow2d`), CoSAI #2 and #3, specification: clients MUST consider tool annotations untrusted (`spt3`) | OWASP, CoSAI PDF, MCP Tools page | VERIFIED by the checker |
| M13 | The line between M13 (description and schema) and M04 (outputs) | none | `[inference]`, interpretation by AI |
| M14 | OWASP MCP07 name (`ow7`), CoSAI #1, #8, #18, specification token passthrough and confused deputy (moved from M06) | OWASP, CoSAI PDF, MCP security best practices | VERIFIED by the checker |
| M06, M08, M10 | Retitled to one subject each; check lists reworded. New checks without a source are labelled `[inference]`. | as before | SUPPORTED |
| Microsoft view | M13 takes the tool-change quote and check from M02; M14 takes the API Management and OAuth items from M06; M06 says not assessed | Microsoft Learn quotes unchanged | VERIFIED by the checker |

Not tested: no product setting or exploit was run. Saved statuses for M02, M06, M08 and M10 may now describe a narrower card than the reader had in mind; no migration was done.

## What was verified and what was not

- Each added CoSAI and specification sentence is tied to an exact quote with a link (PDF page or text fragment). The spec quotes sit in the Tools page's "Security Considerations" lists (Servers MUST: rate limit tool invocations; human in the loop SHOULD be present).
- The Microsoft view has no source for M06 and M09 to M12 and says so.
- CoSAI status: the paper says "Status: Draft" (PDF page 2) and also says the CoSAI Project Governing Board approved it on 8 January 2026 (page 4). The page reports both.
- CoSAI numbering quirks, not resolved by the paper: threat #4 cites "Prompt Injection (#12)" while the list numbers it #11; the category table (pages 8 and 9) names #8 "Confused Deputy (OAuth Proxy)" under one category and "Privilege Escalation" under another, while the list names #8 "Privilege Escalation via Authentication and Authorization Bypass". The page follows the list.
- Not tested: no CoSAI threat was reproduced. Quote matching shows the text is in the PDF, not that the paper's claims are right.

# Complete statement review: 9 November 2026

This review supersedes the 5 and 8 November reviews below. Both views, all five tabs, the shared glossary and VS Code table, all risk cards, both sets of diagram popovers, start recommendations, evidence descriptions, source descriptions and status/export wording were reviewed. Documentation claims describe the documented behavior; they are not product enforcement tests.

## Corrections and verdicts

- **GitHub lists:** corrected missing built-in-default-server exemption. Repository custom agent profiles remain excluded. Deny precedence is limited to servers subject to evaluation.
- **Visual Studio trust:** corrected unconditional prompting. The source documents an initial automatic baseline, built-in, RegistryOnly and Always Trust exceptions, and a switch to disable change prompts. Tool-list resets require a server notification, not detection of arbitrary changes to executable code.
- **VS Code:** separated editor per-server sandboxing from Copilot harness sandboxing; labelled Windows 11 harness support Experimental. Added the independent CLI-configuration discovery path, scoped editor policy claims, and included Assisted permissions in the auto-approval policy description.
- **Windows registry:** restricted the isolation claim to ODR-managed servers, not all programs on Windows. Prerelease labels retained.
- **Research evidence:** Invariant's demonstrated client was Claude Desktop with GitHub MCP. Removed the implication of a Microsoft Copilot client test and the broad claim that no Microsoft demonstration was found. Mitiga is evidence for the cited Claude Code chain only. CVEs are vendor records, not evidence here of observed victims.
- **Definitions:** clarified the OAuth confused-deputy scenario, the MCP client's role in SSRF, and that prompt injections can be visible.
- **Diagram evidence:** added quotations and passage links for all 28 general-view markers. Simplified marker wording to what its evidence supports. The detailed controls retain their authoritative home in the risk cards.
- **Review dates:** all current review dates now read 9 November 2026. Publication dates and historical reviews are retained. Index entry 03 and footer updated in the same change.
- **Evidence checker:** now checks general-view diagram quotations as well as Microsoft quotations. Earlier source mappings such as SELF for token scopes or CC for VS Code telemetry are superseded by this review.

## Evidence and review limits

All external sources in the page were retrieved on 9 November 2026. Source quotation matching alone is not semantic verification: the surrounding sections were also reviewed for scope, exceptions and prerequisites. All retained empirical claims are supported by the listed primary documentation or attributed research. Advice, risk grouping, placement, friction ratings, recommended controls and status meanings are editorial choices, not experimentally verified facts. Labels and interface instructions were checked against the page.

No exploit, OAuth flow, installed client, managed policy, server isolation or CVE remediation was exercised. This review verifies published documentation and research claims, not universal implementation behavior or absence of other incidents. Preview and experimental features remain explicitly identified. Sources can change after this review.

## Section responsibilities

The map explains the reference scenario and gives source-backed placement summaries. Risks own detailed controls and prerequisites; markers cross-reference them. The VS Code table owns harness-specific differences. The other Microsoft table summarizes the named products only. Evidence describes verification limits; Sources identifies primary documents. The eight editorial risk groups overlap in attack chains and are not asserted to exhaust every MCP threat.

## Source register

Keys ARCH, TOOLS, STDIO, HTTP, SEC, VER, OWASP, CC, CODEX, MITIGA, VADD, VMAN, VCONF, VSEC, VPOL, VMGMT, VOTEL, OAUTH and BEARER refer to the primary-source URLs in the historical register below, freshly retrieved for this review. SELF means the page's code, interface, declared scenario or editorial choice. VSANDBOX is [VS Code Copilot agent sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing), including Experimental Windows support. Lowercase keys below identify the quotation sources in the page.

- **odr**: [MCP on Windows: Windows On-device Agent Registry](https://learn.microsoft.com/en-us/windows/ai/mcp/overview), retrieved 10 November 2026.
- **vs**: [Visual Studio: use MCP servers](https://learn.microsoft.com/en-us/visualstudio/ide/mcp-servers), retrieved 9 November 2026.
- **ghal**: [GitHub: configure an enterprise MCP allowlist](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-enterprise-allowlist), retrieved 10 November 2026.
- **ghreg**: [GitHub: configure an MCP registry](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-mcp-registry), retrieved 9 November 2026.
- **ghenf**: [GitHub: MCP private registry enforcement](https://docs.github.com/en/copilot/reference/enterprise-administrators/mcp-private-registry-enforcement), retrieved 9 November 2026.
- **csadd**: [Copilot Studio: add an existing MCP server](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent), retrieved 9 November 2026.
- **csdlp**: [Copilot Studio: data loss prevention](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention), retrieved 9 November 2026.
- **gsa**: [Entra Global Secure Access: MCP firewall](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-mcp-firewall), retrieved 9 November 2026.
- **gsalog**: [Entra Global Secure Access: MCP logging](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-view-model-context-protocol-logging), retrieved 9 November 2026.
- **apim**: [Azure API Management: secure MCP servers](https://learn.microsoft.com/en-us/azure/api-management/secure-mcp-servers), retrieved 9 November 2026.
- **a365gw**: [Agent 365: tools gateway](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-tools-gateway), retrieved 9 November 2026.
- **a365byo**: [Agent 365: bring your own MCP server](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-byo-mcp-server), retrieved 9 November 2026.
- **azmcp**: [Azure MCP Server: security](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security), retrieved 9 November 2026.
- **cve26118**: [CVE-2026-26118 (Azure MCP Server)](https://www.cve.org/CVERecord?id=CVE-2026-26118), retrieved 9 November 2026.
- **cve32211**: [CVE-2026-32211 (Azure MCP Server)](https://www.cve.org/CVERecord?id=CVE-2026-32211), retrieved 9 November 2026.
- **inv**: [Invariant Labs: GitHub MCP exploited](https://invariantlabs.ai/blog/mcp-github-vulnerability), retrieved 9 November 2026.
- **vscm**: [VS Code: manage MCP servers](https://code.visualstudio.com/docs/agents/run/manage-mcp-servers), retrieved 9 November 2026.
- **vspol**: [Centrally manage VS Code settings with policies](https://code.visualstudio.com/docs/enterprise/policies), retrieved 10 November 2026.
- **vstel**: [VS Code: enterprise telemetry](https://code.visualstudio.com/docs/enterprise/telemetry), retrieved 9 November 2026.
- **sphttp**: [MCP specification: transports (Streamable HTTP)](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http), retrieved 9 November 2026.
- **spsec**: [MCP security best practices (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices), retrieved 9 November 2026.
- **spver**: [MCP versioning](https://modelcontextprotocol.io/specification/versioning), retrieved 9 November 2026.
- **owasp**: [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/), retrieved 9 November 2026.
- **cosai**: [CoSAI: Model Context Protocol (MCP) Security](https://www.coalitionforsecureai.org/wp-content/uploads/2026/03/model-context-protocol-security-1.pdf), Workstream 4, 27 pages, retrieved 9 November 2026. Quotes are matched on the PDF page they cite.
- **sptools**: [MCP specification: tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools), retrieved 9 November 2026.
- **mit**: [Mitiga: MCP token theft in Claude Code](https://www.mitiga.io/blog/claude-code-mcp-token-theft-mitm), retrieved 9 November 2026.
- **cc**: [Claude Code: managed MCP](https://code.claude.com/docs/en/managed-mcp), retrieved 9 November 2026.
- **codex**: [Codex managed configuration](https://learn.chatgpt.com/docs/enterprise/managed-configuration), retrieved 9 November 2026.
- **vconf**: [VS Code: MCP configuration reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration), retrieved 9 November 2026.

## Historical statement inventory (see final audit above)

Each row preserves a complete prose unit so its qualifications remain attached. Source text itself is checked through the quotation inventory; labels, recommendations and review declarations are not recast as empirical claims.

| Location | Current text | Evidence | Verdict |
| --- | --- | --- | --- |
| intro  | Risk map · MCP servers and AI agents | SELF | LABEL / REVIEW SCOPE |
| intro  | Risk map · MCP servers and AI agents · Microsoft ecosystem | SELF | LABEL / REVIEW SCOPE |
| intro  | Where the main risks sit when developers connect AI agents to MCP servers, what to check for each, and where to start. The detail is kept low on purpose. Exceptions exist. | SELF | LABEL / REVIEW SCOPE |
| intro  | Where the main risks sit when developers connect AI agents to MCP servers through Microsoft products: VS Code, Visual Studio, GitHub Copilot, Copilot Studio, Windows, Azure and Microsoft Entra. Third-party servers used inside these clients still apply. The detail is kept low on purpose. Exceptions exist. | SELF | LABEL / REVIEW SCOPE |
| p-map  | (Removed 9 Nov 2026 at the owner's request.) The sections "How MCP works", "In short" and "Words used on this page" (host/client/server basics, the In short list, and the ten word definitions from Token to Egress proxy). | n/a | REMOVED |
| p-map  | (Removed 9 Nov 2026 at the owner's request.) Was: "From where servers and content come from ... Risk list buttons above show the OWASP MCP Top 10 risks, the CoSAI risks or all of them." | n/a | REMOVED |
| p-map  | (Removed 9 Nov 2026 at the owner's request.) Was: "The diagram is wide. Drag sideways in it, or use the table below." | n/a | REMOVED |
| p-map  | The same placement as the diagram. (The sentence "Select a risk to show it in the diagram." was removed 9 Nov 2026.) | SELF | REVIEWED |
| p-map  | Risk1 · Sources2 · Workstation3 · Outbound4 · Governance | ARCH, TOOLS, STDIO, HTTP, SEC, OAUTH, BEARER; SELF for map instructions | REVIEWED / labelled judgement |
| p-map  | (Removed 9 Nov 2026 at the owner's request, with its heading "Before you use the map".) Was: "This is a reference layout, not your organisation's setup ... Draw your own variant and move the markers." | n/a | REMOVED |
| p-map  | (Removed 9 Nov 2026 at the owner's request.) Was: "The placement of risks is interpretation by AI based on the sources. [inference]" The same judgement is still stated for the mapping table and the risk grouping. | n/a | REMOVED |
| p-risks  | Grouped from the OWASP MCP Top 10 and the specification's security guidance. The order and the grouping are interpretation by AI. [inference] OWASP's list is in beta and may change. | OWASP, VER, CC, MITIGA; SELF for status definitions | REVIEWED / recommendation or label |
| p-risks  | OWASP MCP Top 10: in beta (phase 3). IDs and names can change. | OWASP, VER, CC, MITIGA; SELF for status definitions | REVIEWED / recommendation or label |
| p-risks  | Specification versions: the Origin, localhost and security rules were checked against version 2026-07-28, the current one on 9 November 2026. They can change. | OWASP, VER, CC, MITIGA; SELF for status definitions | REVIEWED / recommendation or label |
| p-risks  | Claude Code: the managedMcpServers setting needs version 2.1.259 or later. | OWASP, VER, CC, MITIGA; SELF for status definitions | REVIEWED / recommendation or label |
| p-risks  | Mitiga: Mitiga reports that Anthropic told it the behaviour is out of scope and by design. Mitiga disagrees. This page does not take a side. | OWASP, VER, CC, MITIGA; SELF for status definitions | REVIEWED / recommendation or label |
| p-risks  | One suggested first control per risk. These are recommendations, and the friction is an AI estimate. [inference] None of them needs a preview feature. | OWASP, VER, CC, MITIGA; SELF for status definitions | REVIEWED / recommendation or label |
| p-risks  | RiskFirst controlFriction | OWASP, VER, CC, MITIGA; SELF for status definitions | REVIEWED / recommendation or label |
| p-risks  | OK: in place and tested on a named product and operating system, with evidence and a date recorded elsewhere; the tracker stores status values in this browser, with no evidence attachments. Partial: covers some products, platforms or users. Missing: not in place. Unknown: looked at but not confirmed. Not assessed: nobody has looked yet. Definitions are interpretation by AI. [inference] | OWASP, VER, CC, MITIGA; SELF for status definitions | REVIEWED / recommendation or label |
| p-risks M01 | OWASP MCP09 Shadow MCP Servers | CC, CODEX, VPOL, VMGMT | REVIEWED / recommendation or label |
| p-risks M01 | In plain words: Without enforced restrictions, users can configure unapproved servers. An allowlist limits which servers can load within its documented scope. | CC, CODEX, VPOL, VMGMT | REVIEWED / recommendation or label |
| p-risks M01 | By default in Claude Code anyone can connect any MCP server. Anthropic reviews connectors before listing them in its Directory, but does not security-audit or manage any MCP server. So each developer decides what the agent can reach, unless policy limits it. | CC, CODEX, VPOL, VMGMT | REVIEWED / recommendation or label |
| p-risks M01 | Is there an approved list of servers, and is it enforced? | CC, CODEX, VPOL, VMGMT | REVIEWED / recommendation or label |
| p-risks M01 | Does the list cover both remote servers and local ones? | CC, CODEX, VPOL, VMGMT | REVIEWED / recommendation or label |
| p-risks M01 | Is a server's name used as the control? Anthropic says the name is not a security control. | CC, CODEX, VPOL, VMGMT | REVIEWED / recommendation or label |
| p-risks M01 | Claude Code: use managed allowedMcpServers with allowManagedMcpServersOnly: true. For servers subject to the allowlist, URL entries require remote URL matches, and command entries require stdio command matches. Matching deny rules take precedence. | CC, CODEX, VPOL, VMGMT | REVIEWED / recommendation or label |
| p-risks M01 | managed-mcp.json restricts user-added servers, but an empty mcpServers does not disable every server: managed-settings servers, in-process SDK servers and explicitly permitted connectors or built-ins can still load. SDK servers skip these checks; some managed and built-in servers skip the allowlist. Review the vendor's exceptions for your session type. | CC, CODEX, VPOL, VMGMT | REVIEWED / recommendation or label |
| p-risks M01 | Codex: configure server identities under [mcp_servers.<name>] in managed requirements.toml. VS Code: use ChatAllowedMcpServers; review the selected harness and policy coverage. | CC, CODEX, VPOL, VMGMT | REVIEWED / recommendation or label |
| p-risks M01 | Typical findingsUnrestricted server configuration, required servers missing from the allowlist, user-assigned names used as identity checks. [inference] | CC, CODEX, VPOL, VMGMT | REVIEWED / recommendation or label |
| p-risks M02 | OWASP MCP04 Software Supply Chain Attacks and Dependency Tampering · MCP03 Tool Poisoning | SEC, OWASP, CC, CODEX | REVIEWED / recommendation or label |
| p-risks M02 | In plain words: A local server is a program someone wrote. If it is malicious, it can act with the launching account's privileges unless isolation restricts it. | SEC, OWASP, CC, CODEX | REVIEWED / recommendation or label |
| p-risks M02 | A local server may be installed from a package or repository, or written locally. Without adequate isolation, malicious server code can execute with the MCP client's privileges. No MCP-specific incident for this risk is cited here. | SEC, OWASP, CC, CODEX | REVIEWED / recommendation or label |
| p-risks M02 | Are local servers allowed by exact command rather than by name? | SEC, OWASP, CC, CODEX | REVIEWED / recommendation or label |
| p-risks M02 | Who wrote each approved server, and how does it update? [inference] | SEC, OWASP, CC, CODEX | REVIEWED / recommendation or label |
| p-risks M02 | Claude Code matches serverCommand exactly but does not compare the env block. Matching a command does not verify the contents of its package or executable. [inference] | SEC, OWASP, CC, CODEX | REVIEWED / recommendation or label |
| p-risks M02 | Codex: the string form of command does not check args, cwd or env; the structured form checks the executable, argument count, order and matching rules. It still ignores cwd, env and env_vars. | SEC, OWASP, CC, CODEX | REVIEWED / recommendation or label |
| p-risks M02 | Typical findingsServers installed from any package, no review of updates. [inference] | SEC, OWASP, CC, CODEX | REVIEWED / recommendation or label |
| p-risks M03 | OWASP MCP05 Command Injection and Execution | SEC, OWASP | REVIEWED / recommendation or label |
| p-risks M03 | In plain words: A local server is started by a command. If the client executes a malicious command, attacker code runs within the configured execution environment. | SEC, OWASP | REVIEWED / recommendation or label |
| p-risks M03 | The MCP specification lists local server compromise as a risk: a malicious startup command in the client config, or a malicious payload in the server. The results it names are arbitrary code execution, no visibility and data exfiltration. | SEC, OWASP | REVIEWED / recommendation or label |
| p-risks M03 | Does your client ask before it runs a server's command, and show the whole command? The specification (2026-07-28) says a client with one-click local setup must. | SEC, OWASP | REVIEWED / recommendation or label |
| p-risks M03 | Does your client sandbox local servers? The specification says clients should run them with minimal default privileges. | SEC, OWASP | REVIEWED / recommendation or label |
| p-risks M03 | Is stdio used where possible? The specification says server authors should use stdio, or restrict HTTP with an auth token or unix sockets. | SEC, OWASP | REVIEWED / recommendation or label |
| p-risks M03 | Typical findingsOne-click setup that hides the command, servers started with no sandbox. [inference] | SEC, OWASP | REVIEWED / recommendation or label |
| p-risks M04 | OWASP MCP06 Prompt Injection via Contextual Payloads | OWASP, inv | REVIEWED / recommendation or label |
| p-risks M04 | In plain words: The agent reads text that tools bring back. If that text contains malicious instructions, the agent may follow them. | OWASP, inv | REVIEWED / recommendation or label |
| p-risks M04 | A tool can read pages, tickets or files that someone else wrote. Malicious instructions, visible or hidden, can steer the agent. OWASP lists this category. The Microsoft view cites an Invariant Labs research demonstration; no victim incident is verified here. | OWASP, inv | REVIEWED / recommendation or label |
| p-risks M04 | Which servers read content you do not control (web, tickets, mail, shared files)? [inference] | OWASP, inv | REVIEWED / recommendation or label |
| p-risks M04 | Are untrusted reading tasks separated into sessions without tools that can write, send or run things? [inference] | OWASP, inv | REVIEWED / recommendation or label |
| p-risks M04 | Does a person approve tool calls that change something? [inference] | OWASP, inv | REVIEWED / recommendation or label |
| p-risks M04 | Typical findingsOne agent holding both a reader of outside text and a server that can send or change things. [inference] | OWASP, inv | REVIEWED / recommendation or label |
| p-risks M05 | OWASP MCP01 Token Mismanagement and Secret Exposure | MITIGA, OAUTH, BEARER | REVIEWED / recommendation or label |
| p-risks M05 | In plain words: A bearer token grants access to a service. An attacker who can intercept it may be able to reuse it. | MITIGA, OAUTH, BEARER | REVIEWED / recommendation or label |
| p-risks M05 | Mitiga (May 2026) showed an npm postinstall hook that edits ~/.claude.json and points an MCP server URL at an attacker's localhost proxy. Mitiga shows interception and reuse of an OAuth bearer token with Atlassian. Its article discusses refresh-token persistence but does not separately demonstrate capture of a refresh token. | MITIGA, OAUTH, BEARER | REVIEWED / recommendation or label |
| p-risks M05 | The chain requires local code execution through the npm installation. Mitiga describes a project SessionStart hook that restores the malicious endpoint; remediation must remove that persistence as well as repair the configuration and rotate credentials. | MITIGA, OAUTH, BEARER | REVIEWED / recommendation or label |
| p-risks M05 | Do you watch ~/.claude.json and project MCP files for changed server URLs? Mitiga recommends this. | MITIGA, OAUTH, BEARER | REVIEWED / recommendation or label |
| p-risks M05 | Is there a baseline of approved MCP endpoints, with an alert on new local proxies? Mitiga recommends this too. | MITIGA, OAUTH, BEARER | REVIEWED / recommendation or label |
| p-risks M05 | After a suspected case, is the config fixed as well as the tokens rotated? Mitiga says rotating tokens alone is not enough. | MITIGA, OAUTH, BEARER | REVIEWED / recommendation or label |
| p-risks M05 | Typical findingsNo watch on MCP config files, overly long-lived credentials. [inference] | MITIGA, OAUTH, BEARER | REVIEWED / recommendation or label |
| p-risks M06 | OWASP MCP02 Privilege Escalation via Scope Creep · MCP07 Insufficient Authentication and Authorization | SEC, OAUTH, BEARER, OWASP | REVIEWED / recommendation or label |
| p-risks M06 | In plain words: A key that opens many doors does more harm when stolen. An MCP server must reject client tokens intended for a different service. | SEC, OAUTH, BEARER, OWASP | REVIEWED / recommendation or label |
| p-risks M06 | A stolen token with wide scope reaches further than a narrow one. The specification forbids token passthrough: an MCP server must not accept tokens that were not issued for it. It also warns that a proxy server with a static client ID can be abused (confused deputy). | SEC, OAUTH, BEARER, OWASP | REVIEWED / recommendation or label |
| p-risks M06 | Are tokens short-lived and narrow? The specification recommends a progressive, least-privilege scope model. | SEC, OAUTH, BEARER, OWASP | REVIEWED / recommendation or label |
| p-risks M06 | Do servers you or a supplier run refuse tokens not issued for them? | SEC, OAUTH, BEARER, OWASP | REVIEWED / recommendation or label |
| p-risks M06 | Proxy servers with a static client ID: per-client consent, exact redirect_uri match and single-use OAuth state. | SEC, OAUTH, BEARER, OWASP | REVIEWED / recommendation or label |
| p-risks M06 | Typical findingsBroad personal tokens in MCP config, servers that forward whatever token they receive. [inference] | SEC, OAUTH, BEARER, OWASP | REVIEWED / recommendation or label |
| p-risks M07 | MCP specification: transports and security best practices | SEC, HTTP | REVIEWED / recommendation or label |
| p-risks M07 | In plain words: A server on your own computer can be reached by other programs, and sometimes by web pages. A server can also send your client to addresses it should not visit. | SEC, HTTP | REVIEWED / recommendation or label |
| p-risks M07 | An MCP server that listens on local HTTP can be reached by other local programs and, through DNS rebinding, by web pages. The specification also warns that a malicious server can supply URLs that point at internal addresses, such as 169.254.169.254. | SEC, HTTP | REVIEWED / recommendation or label |
| p-risks M07 | Local HTTP servers: do they check the Origin header (must), bind to 127.0.0.1 rather than 0.0.0.0 (should) and require authentication (should)? Source: specification 2026-07-28. | SEC, HTTP | REVIEWED / recommendation or label |
| p-risks M07 | For OAuth metadata discovery, does the client require HTTPS, restrict private and reserved destinations, and recheck redirect targets? The guidance recommends these checks for production, with explicit loopback exceptions for development. For server-side client deployments, operators should consider an egress proxy. | SEC, HTTP | REVIEWED / recommendation or label |
| p-risks M07 | Does the client require HTTPS authorization URLs, allow HTTP only for loopback during local development, reject dangerous schemes such as javascript:, and avoid shell execution when opening URLs? The guidance requires these protections. | SEC, HTTP | REVIEWED / recommendation or label |
| p-risks M07 | Typical findingsA server left running on localhost with no token, bound to all interfaces. [inference] | SEC, HTTP | REVIEWED / recommendation or label |
| p-risks M08 | OWASP MCP10 Context Injection and Over-Sharing · MCP08 Lack of Audit and Telemetry | ARCH, OWASP, CC | REVIEWED / recommendation or label |
| p-risks M08 | In plain words: Without server inventories and suitable logs, it is harder to establish what was shared. [inference] | ARCH, OWASP, CC | REVIEWED / recommendation or label |
| p-risks M08 | MCP calls send data to the selected server. Local calls can stay on the machine; external disclosure depends on the server, host and model deployment. OWASP separately lists context over-sharing and missing audit telemetry as risks. No MCP-specific incident for these risks is cited here. | ARCH, OWASP, CC | REVIEWED / recommendation or label |
| p-risks M08 | Is there a list of servers in use, who runs them and what data each receives? [inference] | ARCH, OWASP, CC | REVIEWED / recommendation or label |
| p-risks M08 | Can you see MCP use? Claude Code usage can be monitored with OpenTelemetry; OTEL_LOG_TOOL_DETAILS=1 is the variable the docs name for tool details. | ARCH, OWASP, CC | REVIEWED / recommendation or label |
| p-risks M08 | Has someone decided what may be sent to remote servers? [inference] | ARCH, OWASP, CC | REVIEWED / recommendation or label |
| p-risks M08 | Typical findingsNo inventory, no usage logs, remote servers receiving whole files. [inference] | ARCH, OWASP, CC | REVIEWED / recommendation or label |
| p-vscode  | What the VS Code documentation says about MCP, and which risk each point touches. The general risks still apply. Rows summarize the VS Code docs checked on 9 November 2026, except for the enterprise tool-approval policy checked on 10 November. Nothing here was tested. | SELF | REVIEWED / documentation scope |
| p-vscode  | TopicWhat VS Code doesRisk | SELF | REVIEWED / documentation scope |
| p-vscode  | Ways a server gets addedFrom the MCP server gallery (Preview), MCP: Add Server, your user mcp.json, a repo's .vscode/mcp.json or root .mcp.json, a Dev Container's devcontainer.json, or code --add-mcp.M01 | VADD, VCONF | REVIEWED / documentation scope |
| p-vscode  | Servers found in other appschat.mcp.discovery.enabled picks the sources. GitHub Copilot CLI discovery is on by default. Claude Desktop, Cursor and Windsurf are off by default. Copilot harness sessions independently read CLI configuration; this discovery setting does not control that path.M01 | VCONF | REVIEWED / documentation scope |
| p-vscode  | Workspace TrustServers in .vscode/mcp.json and .mcp.json follow Workspace Trust. Restricted mode stops them from starting. In a trusted workspace they can start with no separate MCP prompt, also after the config changes.M03 | VMAN | REVIEWED / documentation scope |
| p-vscode  | Autostartchat.mcp.autostart (experimental) defaults to newAndOutdated. When you send a chat message, VS Code starts servers that never ran or whose config changed. Setting it to never does not stop Copilot harness sessions from starting their own servers. Disable the server to stop it.M03 | VMAN, VCONF | REVIEWED / documentation scope |
| p-vscode  | Trust and autostart togetherIn a trusted repo, a new or changed server entry can start on your next chat message. [inference] Built from the two rows above. Not tested.M03 | VMAN (inference) | REVIEWED / documentation scope |
| p-vscode  | Sandbox for local serversThe editor per-server sandbox uses sandboxEnabled and access rules for stdio servers on macOS and Linux; its tool calls are auto-approved. The Copilot harness has a separate sandbox, including supported Windows 11 systems (Experimental), controlled by chat.agent.sandbox.mcpServers. The scopes and approval behavior differ.M03, M04 | VMAN, VCONF, VSANDBOX | REVIEWED / documentation scope |
| p-vscode  | Tool approvalMCP invocations use approval controls; saved grants and sandbox auto-approval can avoid repeated prompts. Allow all permissions and Autopilot mode bypass manual tool approval. Setting ChatToolsAutoApprove to false disables global auto-approval and hides Assisted permissions, Allow all permissions and Autopilot, but does not establish that every invocation prompts in every harness.M04 | VSEC, VPOL, VMGMT | REVIEWED / documentation scope |
| p-vscode  | Logins and secretsVS Code-format input variables can prompt for secrets and store them securely. Servers requiring these inputs are not forwarded to Copilot harness sessions. OAuth is supported for compatible servers. Do not commit tokens, passwords or populated authentication headers.M05, M06 | VCONF, VADD | REVIEWED / documentation scope |
| p-vscode  | Settings SyncIf you select MCP Servers in Settings Sync, your user-profile mcp.json syncs to your other devices. Workspace .mcp.json files do not. [inference] A bad entry on one device could reach the others. Not observed.M05 | VMAN (plus labelled inference) | REVIEWED / documentation scope |
| p-vscode  | What servers can ask of the modelchat.mcp.serverSampling sets which models are exposed to servers for background requests.M08 | VCONF | REVIEWED / documentation scope |
| p-vscode  | Organisation policyChatMCP (chat.mcp.access), ChatAllowedMcpServers, ChatAllowManagedMcpServersOnly, ChatDeniedMcpServers and McpGalleryServiceUrl. For editor-managed servers subject to these policies, an allowlist requires a match and deny rules take precedence. These editor policies do not establish coverage of independently discovered Copilot runtime servers; check the harness-specific management guidance.M01 | VPOL, VMGMT | REVIEWED / documentation scope |
| p-vscode  | Other agents inside VS CodeClaude and Codex harness integrations are disabled while Copilot enterprise-managed settings apply, because those harnesses cannot enforce them. This includes server-, MDM- and file-delivered settings. It is a restriction on harness availability, not on selecting Claude or OpenAI models within Copilot.M01 | VMGMT | REVIEWED / documentation scope |
| p-vscode  | VisibilityMCP: Show Installed Servers lists the servers. Copilot Chat can export traces, metrics and events through OpenTelemetry, which covers tool execution.M08 | VMAN, VOTEL | REVIEWED / documentation scope |
| p-vscode  | Example commandsThe docs' own example runs npx -y @playwright/mcp@latest, an unpinned package. [inference] Pinning a package version reduces changes from resolving @latest; it does not guarantee immutable dependencies or safe code.M02 | VCONF (plus labelled inference) | REVIEWED / documentation scope |
| p-vscode  | What Microsoft and GitHub documentation or CVE records say about MCP outside VS Code, and which risk each row touches. Each row has the exact quote and a link to the source. Checked on 9 November 2026. Nothing here was tested. | SELF | REVIEWED / documentation scope |
| p-vscode  | TopicWhat the source saysRisk | SELF | REVIEWED / documentation scope |
| p-vscode  | VS Code has more than one kind of agent session (local and Copilot harness), and the settings do not always reach both. The rows say where the docs name a difference. Settings and policy names come from the docs; none was run on a managed machine. | SELF | REVIEWED / documentation scope |
| p-evidence  | What was checked, what is interpretation by AI, and what is still open. | SELF | LABEL / REVIEW SCOPE |
| p-sources  | All opened on 9 November 2026, except the Developer-WS page, which is on this site. | SELF | LABEL / REVIEW SCOPE |
| p-sources  | All external sources opened on 9 November 2026. The Developer-WS page sits on this site. | SELF | LABEL / REVIEW SCOPE |
| p-sources  | Marked [inference] is interpretation by AI, not stated in a source. The documented product settings and attack paths were not tested on a real system. | SELF | LABEL / REVIEW SCOPE |
| p-sources  | No setting or command on this page was run on a managed machine. | SELF | LABEL / REVIEW SCOPE |
| p-sources  | Versions and dates change quickly in this area. Check the "Current" box against the sources before you use it in a report. | SELF | LABEL / REVIEW SCOPE |
| p-sources  | Made with AIThis page was written with the help of AI. Its content has not necessarily been fully quality checked by a human. | SELF | LABEL / REVIEW SCOPE |
| START M01 | Claude Code allowManagedMcpServersOnly with an allowlist of both URLs and commands; the Codex and VS Code allowlists, with session-specific exceptions reviewed; friction: Moderate | SELF | RECOMMENDATION / ESTIMATE |
| START M02 | Allow local servers by exact command, not by name; friction: Low | SELF | RECOMMENDATION / ESTIMATE |
| START M03 | Check that each client shows the full command and asks before running it; friction: Low | SELF | RECOMMENDATION / ESTIMATE |
| START M04 | Use separate sessions for untrusted reading, without tools that can write or send; friction: Moderate | SELF | RECOMMENDATION / ESTIMATE |
| START M05 | Alert on changes to ~/.claude.json and project MCP files; friction: Low | SELF | RECOMMENDATION / ESTIMATE |
| START M06 | Short-lived, narrowly scoped tokens per server; friction: Moderate | SELF | RECOMMENDATION / ESTIMATE |
| START M07 | Bind local HTTP servers to 127.0.0.1, check Origin and require a token; friction: Low | SELF | RECOMMENDATION / ESTIMATE |
| START M08 | A list of approved servers, and Claude Code usage export through OpenTelemetry; friction: Low | SELF | RECOMMENDATION / ESTIMATE |
| EVIDENCE Checked against sources | OWASP MCP Top 10 names and IDs (MCP01 to MCP10), read 9 November 2026. The project is in beta (phase 3). | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Checked against sources | MCP specification 2026-07-28 (the current version), Streamable HTTP: Origin validation, localhost binding, authentication. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Checked against sources | MCP security best practices (2026-07-28): confused deputy, token passthrough, SSRF, local server compromise, authorization URL validation, scope minimisation. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Checked against sources | Mitiga research, published 5 May 2026, updated 30 October 2026: endpoint rewriting, bearer-token interception and reuse, prerequisite local code execution, and the vendor response as reported by Mitiga. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Checked against sources | Claude Code managed MCP page: managed-mcp.json, allowedMcpServers and deniedMcpServers, allowManagedMcpServersOnly, URL and command matching, OpenTelemetry. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Checked against sources | Codex managed configuration: mcp_servers allowlist and string versus structured command matching; neither form verifies cwd or environment variables. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Checked against sources | VS Code docs (agent customization, manage MCP servers, MCP configuration reference, AI security, policies, telemetry): the rows on the VS Code tab. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Interpretation by AI | The choice of eight risks, their order and the OWASP mapping. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Interpretation by AI | Where each risk sits on the map. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Interpretation by AI | Statements tagged [inference] (advice questions, not facts), and the friction estimates. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Interpretation by AI | Which VS Code facts are shown, and the risk each is tied to. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Still open | The specification can change. This page was checked against version 2026-07-28, the current one on 9 November 2026. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Still open | The general view cites Mitiga; the Microsoft view adds Invariant Labs and two vendor CVE records. No victim incident was independently verified. That does not mean none exists. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Still open | Mitiga reports that Anthropic told it the issue was out of scope and by design. Mitiga disagrees. This page does not take a side. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Still open | Product policy coverage depends on the harness and configuration source. Editor controls do not necessarily cover independently discovered Copilot servers. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Still open | No setting or command on this page was run on a managed machine. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Still open | VS Code has local and Copilot harness sessions. Settings do not always reach both. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| EVIDENCE Still open | Documentation was reviewed, but no exploit or managed-product behavior was reproduced. Mitiga is a research demonstration, not evidence here of an observed victim incident. | Primary sources below; SELF for audit scope | REVIEWED / scope or judgement |
| SOURCES | OWASP MCP Top 10: OWASP. Beta (phase 3). MCP01 to MCP10. | https://owasp.org/www-project-mcp-top-10/ | SOURCE DESCRIPTION |
| SOURCES | MCP specification: transports (Streamable HTTP): Model Context Protocol, version 2026-07-28 (current). Origin validation, localhost binding, authentication. | https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http#security-endpoint | SOURCE DESCRIPTION |
| SOURCES | MCP security best practices (2026-07-28): Model Context Protocol. Confused deputy, token passthrough, SSRF, local server compromise, authorization URL validation, scope minimisation. | https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices | SOURCE DESCRIPTION |
| SOURCES | Stealing MCP tokens in Claude Code via ~/.claude.json: Mitiga (5.5.2026, updated 30.10.2026). Attack steps, vendor response and recommendations. | https://www.mitiga.io/blog/claude-code-mcp-token-theft-mitm | SOURCE DESCRIPTION |
| SOURCES | Claude Code: managed MCP: Anthropic. managed-mcp.json, allowlist and denylist matching, allowManagedMcpServersOnly, OpenTelemetry monitoring. | https://code.claude.com/docs/en/managed-mcp | SOURCE DESCRIPTION |
| SOURCES | Codex managed configuration: OpenAI. requirements.toml mcp_servers allowlist and identity forms. | https://learn.chatgpt.com/docs/enterprise/managed-configuration | SOURCE DESCRIPTION |
| SOURCES | VS Code: Add MCP servers: Microsoft. Gallery, adding servers, trust warning. | https://code.visualstudio.com/docs/agent-customization/mcp-servers | SOURCE DESCRIPTION |
| SOURCES | VS Code: Manage MCP servers: Microsoft. Workspace Trust, autostart, sandbox, Settings Sync, Dev Containers. | https://code.visualstudio.com/docs/agents/run/manage-mcp-servers | SOURCE DESCRIPTION |
| SOURCES | VS Code: MCP configuration reference: Microsoft. Settings, discovery sources, sandbox schema. | https://code.visualstudio.com/docs/agents/reference/mcp-configuration | SOURCE DESCRIPTION |
| SOURCES | VS Code: AI security: Microsoft. Tool approval, permission levels, secure credentials store, MCP sandboxing. | https://code.visualstudio.com/docs/copilot/security | SOURCE DESCRIPTION |
| SOURCES | Centrally manage VS Code settings with policies: Microsoft. ChatMCP, ChatAllowedMcpServers, ChatDeniedMcpServers, McpGalleryServiceUrl, ChatToolsAutoApprove. | https://code.visualstudio.com/docs/enterprise/policies | SOURCE DESCRIPTION |
| SOURCES | VS Code: enterprise telemetry: Microsoft. OpenTelemetry export from Copilot Chat. | https://code.visualstudio.com/docs/enterprise/telemetry | SOURCE DESCRIPTION |
| SOURCES | Developer workstation risk map: This site. The wider page this one was cut from; it covers MCP together with VS Code, git and agents. | Developer-WS.html | SOURCE DESCRIPTION |
| SOURCES | MCP specification: stdio: Subprocess launch and standard-stream transport. | https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio | SOURCE DESCRIPTION |
| SOURCES | MCP specification: tools: Tool capabilities, invocation and host interaction choices. | https://modelcontextprotocol.io/specification/2026-07-28/server/tools | SOURCE DESCRIPTION |
| SOURCES | MCP versioning: Current protocol revision and compatibility rules. | https://modelcontextprotocol.io/specification/versioning | SOURCE DESCRIPTION |
| SOURCES | OAuth bearer token usage (RFC 6750): Bearer possession and authorized resource access. | https://www.rfc-editor.org/rfc/rfc6750 | SOURCE DESCRIPTION |
| SOURCES | VS Code: manage AI settings: Management layers, precedence and harness coverage. | https://code.visualstudio.com/docs/enterprise/manage-ai-settings | SOURCE DESCRIPTION |
| SOURCES | MCP architecture overview: Hosts, clients, servers and application control of model context. | https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture | SOURCE DESCRIPTION |
| SOURCES | OAuth 2.0 (RFC 6749): Access tokens, service credentials and authorization scopes. | https://www.rfc-editor.org/rfc/rfc6749.html#section-3.3 | SOURCE DESCRIPTION |
| SOURCES | VS Code: Copilot agent sandboxing: Separate Copilot harness sandbox; Windows support is Experimental. | https://code.visualstudio.com/docs/agents/run/agent-sandboxing | SOURCE DESCRIPTION |
| general place[0] M01/src | Anthropic says it does not security-audit or manage MCP servers. | cc | REVIEWED; inference where labelled |
| general place[1] M01/cfgin | VS Code documents sharing server definitions in a workspace-root .mcp.json. | vscm | REVIEWED; inference where labelled |
| general place[2] M01/agent | Without administrator restrictions, Claude Code lets users connect their choice of MCP server. | cc | REVIEWED; inference where labelled |
| general place[3] M01/policy | A user-assigned server name does not identify the underlying code or endpoint. Claude Code explicitly says name matching is not a security control. | cc | REVIEWED; inference where labelled |
| general place[4] M02/pkg | OWASP lists software supply chain attacks and dependency tampering as MCP04. | owasp | REVIEWED; inference where labelled |
| general place[5] M02/local | Local servers execute on the same machine as their client. Review and isolate their code. [inference] | spsec | REVIEWED; inference where labelled |
| general place[6] M02/agent | OWASP lists tool poisoning as MCP03. A changed description can change agent behavior. [inference] | owasp | REVIEWED; inference where labelled |
| general place[7] M02/policy | Command matching is only one check: Claude Code ignores env; Codex string-form identity matches only the command. Review executable contents and environment separately. [inference] | cc, codex | REVIEWED; inference where labelled |
| general place[8] M03/cfgin | For one-click local setup, MCP guidance requires showing the full command and explicit approval. | spsec | REVIEWED; inference where labelled |
| general place[9] M03/cfgf | Review startup commands in client configuration as executable code. [inference] | spsec | REVIEWED; inference where labelled |
| general place[10] M03/local | MCP security guidance recommends sandboxing local server commands with minimal default privileges. | spsec | REVIEWED; inference where labelled |
| general place[11] M03/files | Limit local server access to sensitive files and credentials. [inference] | spsec | REVIEWED; inference where labelled |
| general place[12] M03/agent | MCP security guidance recommends sandboxing local server commands with minimal default privileges. | spsec | REVIEWED; inference where labelled |
| general place[13] M04/content | Untrusted tool content can carry malicious instructions, visible or hidden. OWASP calls this contextual prompt injection. [inference] | owasp | REVIEWED; inference where labelled |
| general place[14] M05/pkg | Mitiga describes a post-install hook rewriting MCP endpoints to route traffic through attacker infrastructure. | mit | REVIEWED; inference where labelled |
| general place[15] M05/cfgf | Mitiga describes configuration rewriting as the entry point for its token interception chain. | mit | REVIEWED; inference where labelled |
| general place[16] M05/lhttp | Mitiga demonstrates reuse of a captured Atlassian MCP token to access account information and Jira issues. | mit | REVIEWED; inference where labelled |
| general place[17] M05/tok | Mitiga says rotation helps only after the hook and configuration rewrite are removed. | mit | REVIEWED; inference where labelled |
| general place[18] M05/edr | Mitiga recommends endpoint baselines, configuration monitoring and alerts for local proxies or unexpected URL changes. | mit | REVIEWED; inference where labelled |
| general place[19] M06/tok | MCP guidance recommends progressive, least-privilege scopes to reduce token compromise impact. | spsec | REVIEWED; inference where labelled |
| general place[20] M06/mcpr | MCP servers must reject tokens not explicitly issued for them. | spsec | REVIEWED; inference where labelled |
| general place[21] M06/saas | MCP OAuth proxies must implement per-client consent and other protections against confused-deputy attacks. | spsec | REVIEWED; inference where labelled |
| general place[22] M07/lhttp | Streamable HTTP servers must validate Origin and should bind to localhost when running locally. | sphttp | REVIEWED; inference where labelled |
| general place[23] M07/egress | MCP guidance identifies cloud metadata URLs as an SSRF target. Production OAuth discovery needs destination and redirect checks. | spsec | REVIEWED; inference where labelled |
| general place[24] M07/agent | MCP clients must avoid shell execution when opening authorization URLs. See M07 for the scheme restrictions. | spsec | REVIEWED; inference where labelled |
| general place[25] M08/agent | OWASP lists context injection and over-sharing as MCP10. | owasp | REVIEWED; inference where labelled |
| general place[26] M08/policy | Maintain an inventory and usable audit logs. [inference] OWASP MCP08 concerns missing audit and telemetry. | owasp | REVIEWED; inference where labelled |
| general place[27] M08/tele | Claude Code documents OTEL_LOG_TOOL_DETAILS=1 for MCP server and tool names in telemetry. | cc | REVIEWED; inference where labelled |
| M01.body[0] | GitHub enterprise allowlists and denylists govern covered Copilot servers. Repository custom agent profiles are excluded, and built-in default servers are always allowed. | ghal | REVIEWED; inference where labelled |
| M01.body[1] | GitHub's registry enforcement is in public preview, and GitHub says it is not the recommended method. It matches on server name or ID, which can be bypassed by editing configuration files. | ghreg, ghenf | REVIEWED; inference where labelled |
| M01.checks[0] | Is there an enterprise allowlist or denylist, and do repository custom agent profiles add servers outside it? | ghal | REVIEWED; inference where labelled |
| M01.checks[1] | Does Visual Studio follow the same list? Its docs say it respects allow list policies set through GitHub. | vs | REVIEWED; inference where labelled |
| M01.checks[2] | Do not rely on a gateway for this. The Agent 365 tools gateway can block or allow a server, but it is in preview. | a365gw | REVIEWED; inference where labelled |
| M01.how[0] | GitHub: define allowedMcpServers and deniedMcpServers in managed-settings.json. Match by name, URL or command. Built-in default servers bypass these lists; for other covered servers, deny rules take precedence. | ghal | REVIEWED; inference where labelled |
| M01.how[1] | A malformed list is treated as an empty allowlist, which blocks all servers except built-in default servers. | ghal | REVIEWED; inference where labelled |
| M01.how[2] | VS Code: use the policies ChatAllowedMcpServers and ChatDeniedMcpServers. A deny rule wins over an allow rule. | vspol | REVIEWED; inference where labelled |
| M02.body[0] | The Azure MCP Server security page says to prefer the official Microsoft-maintained Azure MCP Server, and not to use a local one with production data or production credentials. | azmcp | REVIEWED; inference where labelled |
| M02.body[1] | A tool definition can change after approval. Visual Studio resets earlier tool acceptances when a server reports that its tool list changed. The Azure page asks for review, pinning and re-approval of tool definitions. | vs, azmcp | REVIEWED; inference where labelled |
| M02.checks[0] | Is each server package pinned to a version in its command? Visual Studio runs the command you specify. | vs | REVIEWED; inference where labelled |
| M02.checks[1] | Are tool changes reviewed before a server is approved again? | azmcp | REVIEWED; inference where labelled |
| M02.how[0] | Visual Studio respects whatever command you specify, so you can pin versions or pass flags as needed. Matching a command does not verify the contents of its package. [inference] | vs | REVIEWED; inference where labelled |
| M03.body[0] | Visual Studio 18.7+ can prompt for changed server configuration or capabilities. Prompts can be disabled and are skipped on first use, for built-in servers, under RegistryOnly policy, or after Always Trust. | vs | REVIEWED; inference where labelled |
| M03.body[1] | The VS Code editor per-server sandbox supports stdio servers on macOS and Linux, not Windows. The separate Copilot harness sandbox has different platform support; see the VS Code table. Microsoft says Azure MCP Server can act with your Azure identity. | vscm, azmcp | REVIEWED; inference where labelled |
| M03.checks[0] | In VS Code, are unfamiliar repositories opened in Restricted mode, which prevents these servers from starting? | vscm | REVIEWED; inference where labelled |
| M03.checks[1] | In Visual Studio, is server trust in use? It needs version 18.7 or later. | vs | REVIEWED; inference where labelled |
| M03.checks[2] | Does a person confirm tool calls, and who may turn on auto-confirm for a session, a solution or all future calls? | vs | REVIEWED; inference where labelled |
| M04.body[0] | Invariant Labs demonstrated prompt injection through a malicious GitHub issue using Claude Desktop and the GitHub MCP server, leaking private repository data. This is third-party research, not a demonstration against Microsoft Copilot clients. | inv | REVIEWED; inference where labelled |
| M04.body[1] | Windows says its on-device agent registry (prerelease) keeps MCP servers in a separate environment by default, with access to approved resources only. | odr | REVIEWED; inference where labelled |
| M04.checks[0] | Does an agent that reads GitHub issues also hold a token for private repositories? [inference] | inv | REVIEWED; inference where labelled |
| M04.checks[1] | Is auto-confirm in Visual Studio allowed for tools that write or send? [inference] | vs | REVIEWED; inference where labelled |
| M05.body[0] | The Mitiga research targets Claude Code, so it is outside this view. This article does not demonstrate the same chain against a Microsoft product. | mit | REVIEWED; inference where labelled |
| M05.body[1] | Visual Studio change prompts have exceptions; see M03. In a trusted VS Code workspace, changed MCP configuration can start without a separate prompt. Autostart defaults to newAndOutdated. | vs, vscm | REVIEWED; inference where labelled |
| M05.body[2] | In Copilot Studio an MCP server can use an API key, and the key can be sent as a query parameter in the URL. A key in a URL can leak through logs and history. [inference] | csadd | REVIEWED; inference where labelled |
| M05.checks[0] | Are changes to mcp.json and .mcp.json reviewed like code changes? [inference] | vscm | REVIEWED; inference where labelled |
| M05.checks[1] | Where the server allows it, does Copilot Studio use OAuth 2.0 instead of an API key in the query string? [inference] | csadd | REVIEWED; inference where labelled |
| M05.checks[2] | Is there a baseline of approved MCP endpoints, with an alert when a URL changes? [inference] | SELF | REVIEWED; inference where labelled |
| M06.body[0] | Azure API Management can secure inbound access (client to API Management) and outbound access (API Management to the MCP server). Inbound can use Microsoft Entra ID tokens validated by the validate-azure-ad-token policy. | apim | REVIEWED; inference where labelled |
| M06.body[1] | Its credential manager can inject OAuth 2.0 tokens for backend requests. Request headers are forwarded to tool calls with certain exclusions, so check which headers reach the backend. [inference] | apim | REVIEWED; inference where labelled |
| M06.body[2] | CVE-2026-32211 is a missing-authentication flaw in Azure MCP Server (CVSS 9.1). The record lists Azure Web Apps with the tag exclusively-hosted-service. It is a vendor advisory, not evidence here of a victim incident. | cve32211 | REVIEWED; inference where labelled |
| M06.checks[0] | If remote servers sit behind API Management, does inbound access validate Microsoft Entra ID tokens, not only a subscription key? [inference] | apim | REVIEWED; inference where labelled |
| M06.checks[1] | Which request headers reach the backend tool calls? [inference] | apim | REVIEWED; inference where labelled |
| M06.checks[2] | In Copilot Studio, which of the three authentication options does each server use? | csadd | REVIEWED; inference where labelled |
| M07.body[0] | Entra Global Secure Access has an MCP firewall in preview. It inspects MCP traffic to remote servers and can allow or block by server URL pattern. It needs TLS inspection to enforce MCP policy. | gsa | REVIEWED; inference where labelled |
| M07.body[1] | CVE-2026-26118 is a server-side request forgery flaw in Azure MCP Server (CVSS 8.8). It is a vendor advisory, not evidence here of a victim incident. | cve26118 | REVIEWED; inference where labelled |
| M07.checks[0] | Are local HTTP servers bound to 127.0.0.1, and do they validate the Origin header? | sphttp | REVIEWED; inference where labelled |
| M07.checks[1] | Is the Azure MCP Server updated in line with the vendor advisory for CVE-2026-26118? | cve26118 | REVIEWED; inference where labelled |
| M08.body[0] | VS Code can export traces, metrics and events through OpenTelemetry, covering tool execution. Defender advanced hunting shows activity for servers registered through Agent 365 BYO (preview). | vstel, a365byo | REVIEWED; inference where labelled |
| M08.body[1] | Entra MCP logging (preview) can help discover shadow MCP servers, but it captures remote traffic only. Local servers are not visible to it. | gsalog | REVIEWED; inference where labelled |
| M08.body[2] | Windows says users and administrators can log and audit client and server interactions in its on-device agent registry (prerelease). | odr | REVIEWED; inference where labelled |
| M08.checks[0] | Is OpenTelemetry export on in VS Code, and does it reach your SIEM? | vstel | REVIEWED; inference where labelled |
| M08.checks[1] | Are local servers, which Entra logging cannot see, covered by endpoint tooling? [inference] | gsalog | REVIEWED; inference where labelled |
| row[0] Visual Studio trust and tool reset | Visual Studio 18.7+ can prompt on server changes, with the exceptions listed in M03. On a reported tool-list change, it resets earlier tool acceptances. Trust prompts can be disabled. | vs | REVIEWED; inference where labelled |
| row[1] Visual Studio tool confirmation | Copilot asks for confirmation before it runs a tool. A tool can be auto-confirmed for the session, the solution or all future calls. | vs | REVIEWED; inference where labelled |
| row[2] Visual Studio configuration discovery | Visual Studio also reads MCP configurations that other development environments set up. | vs | REVIEWED; inference where labelled |
| row[3] GitHub allowlist and registry (preview) | Enterprise lists exclude repository custom agent profiles and always allow built-in default servers. Registry enforcement is in public preview, matches on name or ID, and can be bypassed by editing configuration files. | ghal, ghreg, ghenf | REVIEWED; inference where labelled |
| row[4] Copilot Studio authentication, SSE and DLP | Servers can use none, an API key or OAuth 2.0. An API key can be sent in the URL query. SSE is no longer supported for MCP after August 2025. Blocking Power Platform connectors also blocks tools in connected MCP servers. | csadd, csdlp | REVIEWED; inference where labelled |
| row[5] Windows on-device agent registry (prerelease) | Servers run in a separate environment by default. Users and IT admins can control access per agent with Windows Settings and tools such as Intune, and interactions can be logged. | odr | REVIEWED; inference where labelled |
| row[6] Entra MCP firewall and logging (preview) | The firewall can allow or block remote MCP servers by URL pattern and needs TLS inspection. Logging can help discover shadow servers, but it sees remote traffic only. | gsa, gsalog | REVIEWED; inference where labelled |
| row[7] Azure API Management | Inbound and outbound access to an MCP server can be secured. Inbound can use Microsoft Entra ID tokens. The credential manager can inject OAuth 2.0 tokens for backend requests. Headers are forwarded with certain exclusions. | apim | REVIEWED; inference where labelled |
| row[8] Agent 365 gateway and BYO (preview) | A gateway can be connected to discover and govern MCP servers, and a server can be blocked or allowed. BYO servers can be monitored through Defender advanced hunting. | a365gw, a365byo | REVIEWED; inference where labelled |
| row[9] Azure MCP Server security and CVEs | Microsoft says to prefer the official Azure MCP Server and not to use a local one with production data or credentials. Two CVE records name Azure MCP Server: a server-side request forgery flaw and a missing-authentication flaw. Both are vendor advisories, not evidence here of victim incidents. | azmcp, cve26118, cve32211 | REVIEWED; inference where labelled |
| place[0] M01/src | GitHub's registry feature is in public preview, and GitHub says it is not the recommended way to restrict servers. | ghreg | REVIEWED; inference where labelled |
| place[1] M01/cfgin | Visual Studio also checks for MCP configurations that other development environments set up. | vs | REVIEWED; inference where labelled |
| place[2] M01/agent | In VS Code, servers in .vscode/mcp.json and .mcp.json can start in a trusted workspace without a separate MCP trust prompt. | vscm | REVIEWED; inference where labelled |
| place[3] M01/policy | GitHub enterprise lists exclude repository custom agent profiles and always allow built-in default servers. Visual Studio documents GitHub allow list policy support; verify coverage in the deployed client. | ghal, vs | REVIEWED; inference where labelled |
| place[4] M01/gw | The Agent 365 tools gateway can block or allow an MCP server (preview). | a365gw | REVIEWED; inference where labelled |
| place[5] M02/pkg | OWASP lists software supply chain attacks and dependency tampering as MCP04. | owasp | REVIEWED; inference where labelled |
| place[6] M02/local | Microsoft says not to use a local Azure MCP Server for production data or production credentials. | azmcp | REVIEWED; inference where labelled |
| place[7] M02/agent | OWASP lists tool poisoning as MCP03. Visual Studio resets earlier tool acceptances when a server reports a tool-list change. | owasp, vs | REVIEWED; inference where labelled |
| place[8] M02/policy | Visual Studio runs the command you specify, so you can pin versions. The Azure page says to prefer the official Microsoft-maintained Azure MCP Server. | vs, azmcp | REVIEWED; inference where labelled |
| place[9] M03/cfgin | Visual Studio 18.7+ can prompt for changed server configuration or capabilities. Prompts can be disabled and are skipped on first use, for built-in servers, under RegistryOnly policy, or after Always Trust. | vs | REVIEWED; inference where labelled |
| place[10] M03/cfgf | In VS Code, a trusted workspace can start servers from .vscode/mcp.json and .mcp.json without a separate prompt, also after configuration changes. | vscm | REVIEWED; inference where labelled |
| place[11] M03/local | The VS Code editor per-server sandbox supports stdio servers on macOS and Linux, not Windows. The Copilot harness sandbox is separate; see the VS Code table. | vscm | REVIEWED; inference where labelled |
| place[12] M03/files | Microsoft says the Azure MCP Server can act with your Azure identity, and asks you to review what your signed-in account can access. | azmcp | REVIEWED; inference where labelled |
| place[13] M03/agent | Visual Studio asks for confirmation before Copilot runs a tool. You can auto-confirm a tool for the session, the solution or all future calls. | vs | REVIEWED; inference where labelled |
| place[14] M04/content | Invariant Labs demonstrated a malicious GitHub issue causing private repository leakage through GitHub MCP in Claude Desktop. Microsoft Copilot clients were not the demonstrated client. | inv | REVIEWED; inference where labelled |
| place[15] M04/agent | Auto-confirm in Visual Studio removes the prompt for that tool. [inference] | vs | REVIEWED; inference where labelled |
| place[16] M04/local | Microsoft describes default isolation for servers in the Windows on-device agent registry (prerelease). This is a claim about that registry, not all MCP servers running on Windows. | odr | REVIEWED; inference where labelled |
| place[17] M05/cfgf | Visual Studio 18.7+ can prompt for changed server configuration or capabilities. Prompts can be disabled and are skipped on first use, for built-in servers, under RegistryOnly policy, or after Always Trust. | vs | REVIEWED; inference where labelled |
| place[18] M05/agent | VS Code autostart defaults to newAndOutdated: it starts servers that have never run or whose configuration has changed. | vscm | REVIEWED; inference where labelled |
| place[19] M05/tok | Copilot Studio can send an API key as a query parameter in the URL. A key in a URL can leak through logs and history. [inference] | csadd | REVIEWED; inference where labelled |
| place[20] M06/tok | API Management can inject OAuth 2.0 tokens for backend requests. Headers are forwarded with certain exclusions, so check which ones reach the backend. [inference] | apim | REVIEWED; inference where labelled |
| place[21] M06/mcpr | CVE-2026-32211: missing authentication in Azure MCP Server (CVSS 9.1). The record lists Azure Web Apps and the tag exclusively-hosted-service. A vendor advisory, not evidence here of a victim incident. | cve32211 | REVIEWED; inference where labelled |
| place[22] M06/saas | Copilot Studio offers three authentication options for an MCP server: none, API key and OAuth 2.0. | csadd | REVIEWED; inference where labelled |
| place[23] M06/gw | API Management can secure inbound and outbound access. Inbound can use Microsoft Entra ID tokens through the validate-azure-ad-token policy. | apim | REVIEWED; inference where labelled |
| place[24] M07/lhttp | The MCP specification says servers must validate the Origin header, and should bind to localhost (127.0.0.1) when running locally. | sphttp | REVIEWED; inference where labelled |
| place[25] M07/egress | The MCP specification names URLs that target 169.254.169.254, the cloud metadata address, as a way to exfiltrate cloud credentials. | spsec | REVIEWED; inference where labelled |
| place[26] M07/agent | The MCP specification warns that authorization URLs from malicious servers can lead to cross-site scripting and remote code execution in the client. | spsec | REVIEWED; inference where labelled |
| place[27] M07/mcpr | CVE-2026-26118: server-side request forgery in Azure MCP Server (CVSS 8.8). A vendor advisory, not evidence here of a victim incident. | cve26118 | REVIEWED; inference where labelled |
| place[28] M07/gw | The Entra MCP firewall (preview) can allow or block remote MCP servers by URL pattern. It needs TLS inspection to enforce MCP policy. | gsa | REVIEWED; inference where labelled |
| place[29] M08/agent | OWASP lists context injection and over-sharing as MCP10. | owasp | REVIEWED; inference where labelled |
| place[30] M08/policy | The Windows on-device agent registry (prerelease) says users and administrators can log and audit client and server interactions. | odr | REVIEWED; inference where labelled |
| place[31] M08/tele | VS Code can export traces, metrics and events through OpenTelemetry, covering tool execution. Defender advanced hunting shows activity for Agent 365 BYO servers (preview). | vstel, a365byo | REVIEWED; inference where labelled |
| place[32] M08/gw | Entra MCP logging (preview) can help discover shadow MCP servers. It captures remote traffic only. | gsalog | REVIEWED; inference where labelled |
| callout[0] | OWASP MCP Top 10: in beta (phase 3). IDs and names can change. | owasp | REVIEWED; inference where labelled |
| callout[1] | Specification versions: the Origin, localhost and security rules were checked against version 2026-07-28, the current one on 9 November 2026. They can change. | spver | REVIEWED; inference where labelled |
| callout[2] | Preview: Microsoft or GitHub describe these as preview or prerelease: the Windows on-device agent registry, the Entra MCP firewall and logging, the Agent 365 tools gateway and BYO servers, and GitHub registry enforcement. They can change. | odr, gsa, gsalog, a365gw, a365byo, ghreg | REVIEWED; inference where labelled |
| callout[3] | Visual Studio: MCP server trust needs version 18.7 or later. | vs | REVIEWED; inference where labelled |
| callout[4] | Mitiga: the research targets Claude Code, which is outside this view. This article does not demonstrate the same chain against a Microsoft product. | mit | REVIEWED; inference where labelled |

## Validation

- Retrieved 36 distinct external primary-source URLs on 9 November 2026; no retrieval failures. This includes the separately added Copilot sandbox documentation.
- Quote and label check: 92 quotes, 108 reviewed presentation texts, zero problems. Whitespace normalization was needed for cs3 and cxcmd.
- Reviewed 288 current prose units in the inventory above, plus quoted evidence, interface labels, diagram labels and generated status/export text.
- Browser: both views, all five tabs, 1440px and 375px, light and dark themes (40 combinations). No page-wide horizontal overflow, JavaScript exceptions or console errors. Desktop and narrow screenshots visually inspected.
- All 61 risk markers opened with quotations and source links. CVE links intentionally point to records without text fragments. Shared scope links and independent saved statuses survived reload in both views.
- Inline JavaScript syntax passed. HTML ids are unique and unchanged; local links resolve. The Made with AI wording remains unchanged. No build system exists for this standalone HTML page.
- Product controls and attack reproduction remain untested, as stated above.

Reviewed page SHA-256: `42f4956428b12fbed1fae2f0f2bf70d052c96b709414af9f3417e9d4f5331b7b`.

## Superseded reviews and maintained label-check inventory

The following dated reviews are historical. Their statement wording and source mappings must not override the current inventory above. The final reviewed-presentation-text block is maintained for the current automated label check.

# Statement review: 5 November 2026

This review supersedes the 2 November ledger retained below. All listed external primary sources were opened on 5 November 2026. The page was read in full, including static prose, glossary, VS Code rows, and JavaScript-generated popovers, first controls, evidence and source descriptions. Each inventory row below records one sentence or a short inseparable source-backed unit. Advice and questions are not empirical findings.

## Findings corrected

- The host is distinct from its MCP clients. Servers need not expose tools. Context inclusion is a host decision.
- Local process privileges depend on the execution account and isolation. Remote servers need not hold upstream tokens. MCP does not force all data off the machine.
- A token is authorization, not universally proof of a human login. Bearer use is limited by validity, permissions and service checks.
- Empty Claude Code managed MCP configuration is not a universal shutdown. SDK, built-in, managed and connector exceptions are documented. Deny precedence is scoped to servers that undergo those checks.
- A URL-only Claude allowlist does not permit arbitrary stdio commands: unmatched stdio entries are blocked. Command identity does not prove code integrity.
- Structured Codex command matching checks argument count and order, but not cwd or environment variables.
- Mitiga demonstrates bearer-token interception/reuse. Separate refresh-token capture is not demonstrated in the article. Its vendor-response account is attributed, not independently confirmed. The persistent hook must be removed during remediation.
- Authorization HTTP is limited to development loopback. SSRF checks cover OAuth discovery and redirects; server-side client egress guidance is scoped accordingly.
- VS Code editor per-server and Copilot harness sandboxes are separate. Windows support exists for the latter on supported systems. Saved approvals and auto-approval mean every tool call need not prompt.
- Secret inputs are configuration-format and harness dependent. Editor policies do not cover every independently discovered Copilot runtime server.
- Package version pinning reduces drift but is not a guarantee of immutable dependencies or safety.

## Evidence limits

No exploit, managed-client setting, OAuth flow, server installation or vendor enforcement was reproduced. Product statements report documentation, not measured behavior. Mitiga is research, not an independently confirmed victim incident. This audit does not claim that other incidents do not exist. Diagram topology, risk grouping, friction ratings, suggested controls and status definitions are editorial judgements. The diagram's named components and arrows are a reference scenario, not an inventory of a real organization.

Source keys below apply to the relevant named sections, not to unrelated statements on those pages. SELF denotes statements about this artifact, its behavior or this review. REVIEWED means checked against the named sources with the qualifiers present in the final page, not proof of universal implementation compliance.

## Primary sources

- **ARCH**: [MCP architecture](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture), opened 9 November 2026.
- **TOOLS**: [MCP tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools), opened 9 November 2026.
- **STDIO**: [MCP stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio), opened 9 November 2026.
- **HTTP**: [MCP Streamable HTTP, Security & Endpoint](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http#security-endpoint), opened 9 November 2026.
- **SEC**: [MCP Security Best Practices, relevant named subsection](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices), opened 9 November 2026.
- **VER**: [MCP versioning](https://modelcontextprotocol.io/specification/versioning), opened 9 November 2026.
- **OWASP**: [OWASP MCP Top 10, phase 3 and entries MCP01 to MCP10](https://owasp.org/www-project-mcp-top-10/), opened 9 November 2026.
- **CC**: [Claude Code managed MCP, matching / exceptions / monitoring](https://code.claude.com/docs/en/managed-mcp), opened 9 November 2026.
- **CODEX**: [OpenAI managed configuration, Enforce command rules from requirements](https://learn.chatgpt.com/docs/enterprise/managed-configuration), opened 9 November 2026.
- **MITIGA**: [Mitiga research, five-step chain / disclosure / FAQ](https://www.mitiga.io/blog/claude-code-mcp-token-theft-mitm), opened 9 November 2026.
- **VADD**: [VS Code add MCP servers](https://code.visualstudio.com/docs/agent-customization/mcp-servers), opened 9 November 2026.
- **VMAN**: [VS Code manage MCP servers](https://code.visualstudio.com/docs/agents/run/manage-mcp-servers), opened 9 November 2026.
- **VCONF**: [VS Code MCP configuration reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration), opened 9 November 2026.
- **VSEC**: [VS Code AI security, approvals / sandboxing / policy gaps](https://code.visualstudio.com/docs/agents/run/security), opened 9 November 2026.
- **VPOL**: [VS Code device policy reference](https://code.visualstudio.com/docs/enterprise/policies), opened 9 November 2026.
- **VMGMT**: [VS Code manage AI settings, harness availability and coverage](https://code.visualstudio.com/docs/enterprise/manage-ai-settings), opened 9 November 2026.
- **VOTEL**: [VS Code enterprise telemetry, OpenTelemetry support](https://code.visualstudio.com/docs/enterprise/telemetry), opened 9 November 2026.
- **OAUTH**: [RFC 6749, sections 1.4, 3.3, 4.4](https://www.rfc-editor.org/rfc/rfc6749.html), opened 9 November 2026.
- **BEARER**: [RFC 6750, bearer token usage](https://www.rfc-editor.org/rfc/rfc6750), opened 9 November 2026.
- **SELF**: [Page source and review scope](MCP-Risk-Map.html), opened 9 November 2026.

## Complete statement inventory

| # | Location | Final statement | Evidence | Verdict |
| --- | --- | --- | --- | --- |
| 1 | intro , line 271 | Risk map · MCP servers and AI agents | ARCH, SEC | REVIEWED |
| 2 | intro , line 273 | Where the main risks sit when developers connect AI agents to MCP servers, what to check for each, and where to start. | ARCH, SEC | REVIEWED |
| 3 | intro , line 273 | The detail is kept low on purpose. | SELF | REVIEWED |
| 4 | intro , line 273 | Exceptions exist. | SELF | REVIEWED |
| 5 | p-map , line 295 | The host is the AI application. | ARCH, SEC | REMOVED 9 Nov 2026 |
| 6 | p-map , line 295 | Its MCP clients connect to servers. | ARCH, SEC | REMOVED 9 Nov 2026 |
| 7 | p-map , line 295 | Servers can offer tools for the agent to call; a server need not offer tools. | ARCH, SEC | REMOVED 9 Nov 2026 |
| 8 | p-map , line 296 | A local server is a program on your computer. | ARCH, SEC | REMOVED 9 Nov 2026 |
| 9 | p-map , line 296 | With the stdio transport the client starts it and talks to it over its standard streams. | ARCH, SEC, STDIO | REMOVED 9 Nov 2026 |
| 10 | p-map , line 296 | A server can also run behind an HTTP address, on your computer or elsewhere. | ARCH, SEC | REMOVED 9 Nov 2026 |
| 11 | p-map , line 297 | The client sends tool arguments to a server and receives results. | ARCH, SEC | REMOVED 9 Nov 2026 |
| 12 | p-map , line 297 | The host decides how to use those results, including whether to include them in the model's context. | ARCH, SEC | REMOVED 9 Nov 2026 |
| 13 | p-map , line 303 | An MCP server can offer tools. | ARCH, SEC | REMOVED 9 Nov 2026 |
| 14 | p-map , line 303 | An unrestricted local server can act with the launching account's privileges. | ARCH, SEC | REMOVED 9 Nov 2026 |
| 15 | p-map , line 303 | A remote server receives the data sent to it; authentication and token storage depend on the deployment. | ARCH, BEARER, OAUTH, SEC | REMOVED 9 Nov 2026 |
| 16 | p-map , line 304 | The main questions are: which servers are allowed, what can each one reach, and who would notice if one changed? [inference] | ARCH, SEC | REMOVED 9 Nov 2026 |
| 17 | p-map , line 305 | Only one MCP-specific research demonstration is cited here (Mitiga, May 2026). | MITIGA | REMOVED 9 Nov 2026 |
| 18 | p-map , line 305 | The other risks come from OWASP categories or specification warnings, and no incident is cited for them. | OWASP | REMOVED 9 Nov 2026 |
| 19 | p-map , line 311 | An access token authorizes access to a service. | BEARER, OAUTH, SEC | REMOVED 9 Nov 2026 |
| 20 | p-map , line 311 | A valid bearer token can be used by whoever holds it, within its permissions and other service checks. | BEARER, OAUTH, SEC | REMOVED 9 Nov 2026 |
| 21 | p-map , line 311 | Tokens do not always represent a human user. | BEARER, OAUTH, SEC | REMOVED 9 Nov 2026 |
| 22 | p-map , line 312 | A named permission requested or granted during authorization. | SELF | REMOVED 9 Nov 2026 |
| 23 | p-map , line 312 | The service must still enforce access checks. | SELF | REMOVED 9 Nov 2026 |
| 24 | p-map , line 313 | A list of permitted servers, enforced within the control's scope and documented exceptions. | ARCH, BEARER, OAUTH, SEC | REMOVED 9 Nov 2026 |
| 25 | p-map , line 314 | An isolation mechanism that restricts access to resources such as files and networks. | SELF | REMOVED 9 Nov 2026 |
| 26 | p-map , line 314 | Its protection depends on its rules and implementation. | SELF | REMOVED 9 Nov 2026 |
| 27 | p-map , line 315 | Malicious instructions in content the agent reads that may steer its behavior. | OWASP, VSEC | REMOVED 9 Nov 2026 |
| 28 | p-map , line 315 | They can be visible or hidden. | SELF | REMOVED 9 Nov 2026 |
| 29 | p-map , line 316 | An attacker changes where a domain resolves, potentially letting a web page reach a local server. | ARCH, SEC | REMOVED 9 Nov 2026 |
| 30 | p-map , line 316 | Streamable HTTP servers must validate Origin; an invalid supplied origin requires HTTP 403. | ARCH, HTTP, SEC | REMOVED 9 Nov 2026 |
| 31 | p-map , line 316 | Local binding and authentication provide additional protection. | SELF | REMOVED 9 Nov 2026 |
| 32 | p-map , line 317 | A proxy server that connects clients to another service can be tricked into giving an attacker a login code without the user agreeing. | ARCH, SEC | REMOVED 9 Nov 2026 |
| 33 | p-map , line 318 | A server accepts a token that was not made for it and passes it on. | ARCH, BEARER, OAUTH, SEC | REMOVED 9 Nov 2026 |
| 34 | p-map , line 318 | The specification forbids this. | SELF | REMOVED 9 Nov 2026 |
| 35 | p-map , line 319 | Tricking a client into requesting addresses it should not, such as internal systems or a cloud metadata address. | ARCH, SEC | REMOVED 9 Nov 2026 |
| 36 | p-map , line 320 | A gate that outbound traffic must pass. | SELF | REMOVED 9 Nov 2026 |
| 37 | p-map , line 320 | It can block internal destinations. | SELF | REMOVED 9 Nov 2026 |
| 38 | p-map , line 326 | From where servers and content come from, through the agent and its servers, to what goes out. | ARCH, SEC | REMOVED 9 Nov 2026 |
| 39 | p-map , line 326 | Each marker shows where a risk enters or must be controlled. | SELF | REMOVED 9 Nov 2026 |
| 40 | p-map , line 326 | M01 to M08 are coloured by the status you set under Risks. | SELF | REMOVED 9 Nov 2026 |
| 41 | p-map , line 337 | Servers, packages, config and content (1) reach the workstation (2), where this example places the agent, local servers and client credentials. | ARCH, SEC | REMOVED 9 Nov 2026 (the Microsoft version too) |
| 42 | p-map , line 337 | Traffic leaves through the egress boundary (3), a control point only where traffic is forced through a proxy or gateway. | SELF | REVIEWED |
| 43 | p-map , line 337 | Governance and monitoring (4) covers every layer. | SELF | REVIEWED |
| 44 | p-map , line 338 | Arrows show selected paths, not every data flow. | SELF | REVIEWED |
| 45 | p-map , line 338 | Select a marker or a box to see its risks. | SELF | REMOVED 9 Nov 2026 |
| 46 | p-map , line 348 | The diagram is wide. | SELF | REVIEWED |
| 47 | p-map , line 348 | Drag sideways in it, or use the table below. | SELF | REMOVED 9 Nov 2026 |
| 48 | p-map , line 352 | The same placement as the diagram. | SELF | REVIEWED |
| 49 | p-map , line 352 | Select a risk to show it in the diagram. | SELF | REMOVED 9 Nov 2026 |
| 50 | p-map , line 356 | Risk1 · Sources2 · Workstation3 · Outbound4 · Governance | SELF | REVIEWED |
| 51 | p-map , line 364 | This is a reference layout, not your organisation's setup. | SELF | REMOVED 9 Nov 2026 |
| 52 | p-map , line 364 | Common differences: only remote servers, only local servers, servers inside dev containers, or an internal gateway in front of all servers. | ARCH, SEC | REMOVED 9 Nov 2026 |
| 53 | p-map , line 364 | Draw your own variant and move the markers. | SELF | REMOVED 9 Nov 2026 |
| 54 | p-map , line 365 | The placement of risks is interpretation by AI based on the sources. [inference] | SELF | REMOVED 9 Nov 2026 |
| 55 | p-risks , line 373 | Grouped from the OWASP MCP Top 10 and the specification's security guidance. | OWASP | JUDGEMENT / CHECK QUESTION |
| 56 | p-risks , line 373 | The order and the grouping are interpretation by AI. [inference] OWASP's list is in beta and may change. | OWASP | JUDGEMENT / CHECK QUESTION |
| 57 | p-risks , line 379 | OWASP MCP Top 10: in beta (phase 3). | OWASP | REVIEWED |
| 58 | p-risks , line 379 | IDs and names can change. | SELF | REVIEWED |
| 59 | p-risks , line 380 | Specification versions: the Origin, localhost and security rules were checked against version 2026-07-28, the current one on 5 November 2026. | ARCH, HTTP, SEC, VER | REVIEWED |
| 60 | p-risks , line 380 | They can change. | SELF | REVIEWED |
| 61 | p-risks , line 381 | Claude Code: the managedMcpServers setting needs version 2.1.259 or later. | ARCH, CC, SEC | REVIEWED |
| 62 | p-risks , line 382 | Mitiga: Mitiga reports that Anthropic told it the behaviour is out of scope and by design. | BEARER, CC, MITIGA, OAUTH, SEC | REVIEWED |
| 63 | p-risks , line 382 | Mitiga disagrees. | MITIGA | REVIEWED |
| 64 | p-risks , line 382 | This page does not take a side. | SELF | REVIEWED |
| 65 | p-risks , line 388 | One suggested first control per risk. | SELF | JUDGEMENT / CHECK QUESTION |
| 66 | p-risks , line 388 | These are recommendations, and the friction is an AI estimate. [inference] | SELF | JUDGEMENT / CHECK QUESTION |
| 67 | p-risks , line 392 | RiskFirst controlFriction | SELF | REVIEWED |
| 68 | p-risks , line 400 | OK: in place and tested on a named product and operating system, with evidence and a date recorded elsewhere; the tracker stores status values in this browser, with no evidence attachments. | SELF | JUDGEMENT / CHECK QUESTION |
| 69 | p-risks , line 400 | Partial: covers some products, platforms or users. | SELF | JUDGEMENT / CHECK QUESTION |
| 70 | p-risks , line 400 | Missing: not in place. | SELF | JUDGEMENT / CHECK QUESTION |
| 71 | p-risks , line 400 | Unknown: looked at but not confirmed. | SELF | JUDGEMENT / CHECK QUESTION |
| 72 | p-risks , line 400 | Not assessed: nobody has looked yet. | SELF | JUDGEMENT / CHECK QUESTION |
| 73 | p-risks , line 400 | Definitions are interpretation by AI. [inference] | SELF | JUDGEMENT / CHECK QUESTION |
| 74 | p-risks M01, line 424 | OWASP MCP09 Shadow MCP Servers | ARCH, OWASP, SEC | REVIEWED |
| 75 | p-risks M01, line 425 | In plain words: Without enforced restrictions, users can configure unapproved servers. | ARCH, SEC | REVIEWED |
| 76 | p-risks M01, line 425 | An allowlist limits which servers can load within its documented scope. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 77 | p-risks M01, line 426 | By default in Claude Code anyone can connect any MCP server. | ARCH, CC, SEC | REVIEWED |
| 78 | p-risks M01, line 426 | Anthropic reviews connectors before listing them in its Directory, but does not security-audit or manage any MCP server. | ARCH, CC, SEC | REVIEWED |
| 79 | p-risks M01, line 426 | So each developer decides what the agent can reach, unless policy limits it. | SELF | REVIEWED |
| 80 | p-risks M01, line 429 | Is there an approved list of servers, and is it enforced? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 81 | p-risks M01, line 430 | Does the list cover both remote servers and local ones? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 82 | p-risks M01, line 431 | Is a server's name used as the control? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 83 | p-risks M01, line 431 | Anthropic says the name is not a security control. | CC | REVIEWED |
| 84 | p-risks M01, line 434 | Claude Code: use managed allowedMcpServers with allowManagedMcpServersOnly: true. | ARCH, CC, SEC | REVIEWED |
| 85 | p-risks M01, line 434 | For servers subject to the allowlist, URL entries require remote URL matches, and command entries require stdio command matches. | ARCH, SEC, STDIO | REVIEWED |
| 86 | p-risks M01, line 434 | Matching deny rules take precedence. | SELF | REVIEWED |
| 87 | p-risks M01, line 435 | managed-mcp.json restricts user-added servers, but an empty mcpServers does not disable every server: managed-settings servers, in-process SDK servers and explicitly permitted connectors or built-ins can still load. | ARCH, CC, SEC | REVIEWED |
| 88 | p-risks M01, line 435 | SDK servers skip these checks; some managed and built-in servers skip the allowlist. | ARCH, SEC | REVIEWED |
| 89 | p-risks M01, line 435 | Review the vendor's exceptions for your session type. | SELF | REVIEWED |
| 90 | p-risks M01, line 436 | Codex: configure server identities under [mcp_servers.<name>] in managed requirements.toml. | ARCH, CODEX, SEC | REVIEWED |
| 91 | p-risks M01, line 436 | VS Code: use ChatAllowedMcpServers; review the selected harness and policy coverage. | ARCH, SEC, VCONF | REVIEWED |
| 92 | p-risks M01, line 438 | Typical findingsUnrestricted server configuration, required servers missing from the allowlist, user-assigned names used as identity checks. [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 93 | p-risks M02, line 443 | OWASP MCP04 Software Supply Chain Attacks and Dependency Tampering · MCP03 Tool Poisoning | OWASP, SEC | REVIEWED |
| 94 | p-risks M02, line 444 | In plain words: A local server is a program someone wrote. | ARCH, SEC | REVIEWED |
| 95 | p-risks M02, line 444 | If it is malicious, it can act with the launching account's privileges unless isolation restricts it. | SEC | REVIEWED |
| 96 | p-risks M02, line 445 | A local server may be installed from a package or repository, or written locally. | ARCH, SEC | REVIEWED |
| 97 | p-risks M02, line 445 | Without adequate isolation, malicious server code can execute with the MCP client's privileges. | ARCH, SEC | REVIEWED |
| 98 | p-risks M02, line 445 | No MCP-specific incident for this risk is cited here. | SEC | REVIEWED |
| 99 | p-risks M02, line 448 | Are local servers allowed by exact command rather than by name? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 100 | p-risks M02, line 449 | Who wrote each approved server, and how does it update? [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 101 | p-risks M02, line 451 | Claude Code matches serverCommand exactly but does not compare the env block. | ARCH, CC, SEC | JUDGEMENT / CHECK QUESTION |
| 102 | p-risks M02, line 451 | Matching a command does not verify the contents of its package or executable. [inference] | SEC | JUDGEMENT / CHECK QUESTION |
| 103 | p-risks M02, line 451 | Codex: the string form of command does not check args, cwd or env; the structured form checks the executable, argument count, order and matching rules. | CODEX, SEC | REVIEWED |
| 104 | p-risks M02, line 451 | It still ignores cwd, env and env_vars. | SEC | REVIEWED |
| 105 | p-risks M02, line 452 | Typical findingsServers installed from any package, no review of updates. [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 106 | p-risks M03, line 457 | OWASP MCP05 Command Injection and Execution | OWASP, SEC | REVIEWED |
| 107 | p-risks M03, line 458 | In plain words: A local server is started by a command. | ARCH, SEC | REVIEWED |
| 108 | p-risks M03, line 458 | If the client executes a malicious command, attacker code runs within the configured execution environment. | ARCH, SEC | REVIEWED |
| 109 | p-risks M03, line 459 | The MCP specification lists local server compromise as a risk: a malicious startup command in the client config, or a malicious payload in the server. | ARCH, SEC | REVIEWED |
| 110 | p-risks M03, line 459 | The results it names are arbitrary code execution, no visibility and data exfiltration. | SEC | REVIEWED |
| 111 | p-risks M03, line 462 | Does your client ask before it runs a server's command, and show the whole command? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 112 | p-risks M03, line 462 | The specification (2026-07-28) says a client with one-click local setup must. | ARCH, SEC, VER | REVIEWED |
| 113 | p-risks M03, line 463 | Does your client sandbox local servers? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 114 | p-risks M03, line 463 | The specification says clients should run them with minimal default privileges. | ARCH, SEC | REVIEWED |
| 115 | p-risks M03, line 464 | Is stdio used where possible? | SEC, STDIO | JUDGEMENT / CHECK QUESTION |
| 116 | p-risks M03, line 464 | The specification says server authors should use stdio, or restrict HTTP with an auth token or unix sockets. | ARCH, BEARER, OAUTH, SEC, STDIO | REVIEWED |
| 117 | p-risks M03, line 467 | Typical findingsOne-click setup that hides the command, servers started with no sandbox. [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 118 | p-risks M04, line 472 | OWASP MCP06 Prompt Injection via Contextual Payloads | OWASP, VSEC | REVIEWED |
| 119 | p-risks M04, line 473 | In plain words: The agent reads text that tools bring back. | SELF | REVIEWED |
| 120 | p-risks M04, line 473 | If that text hides instructions, the agent may follow them. | OWASP, VSEC | REVIEWED |
| 121 | p-risks M04, line 474 | A tool can read pages, tickets or files that someone else wrote. | SELF | REVIEWED |
| 122 | p-risks M04, line 474 | Hidden instructions in that text can steer the agent. | OWASP, VSEC | REVIEWED |
| 123 | p-risks M04, line 474 | OWASP lists this as a category; no MCP-specific incident is cited here. | OWASP | REVIEWED |
| 124 | p-risks M04, line 477 | Which servers read content you do not control (web, tickets, mail, shared files)? [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 125 | p-risks M04, line 478 | Are untrusted reading tasks separated into sessions without tools that can write, send or run things? [inference] | SELF | JUDGEMENT / CHECK QUESTION |
| 126 | p-risks M04, line 479 | Does a person approve tool calls that change something? [inference] | SELF | JUDGEMENT / CHECK QUESTION |
| 127 | p-risks M04, line 482 | Typical findingsOne agent holding both a reader of outside text and a server that can send or change things. [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 128 | p-risks M05, line 487 | OWASP MCP01 Token Mismanagement and Secret Exposure | BEARER, OAUTH, OWASP, SEC | REVIEWED |
| 129 | p-risks M05, line 488 | In plain words: A bearer token grants access to a service. | BEARER, OAUTH, SEC | REVIEWED |
| 130 | p-risks M05, line 488 | An attacker who can intercept it may be able to reuse it. | SELF | REVIEWED |
| 131 | p-risks M05, line 489 | Mitiga (May 2026) showed an npm postinstall hook that edits ~/.claude.json and points an MCP server URL at an attacker's localhost proxy. | ARCH, MITIGA, SEC | REVIEWED |
| 132 | p-risks M05, line 489 | Mitiga shows interception and reuse of an OAuth bearer token with Atlassian. | BEARER, MITIGA, OAUTH, SEC | REVIEWED |
| 133 | p-risks M05, line 489 | Its article discusses refresh-token persistence but does not separately demonstrate capture of a refresh token. | BEARER, OAUTH, SEC | REVIEWED |
| 134 | p-risks M05, line 489 | The chain requires local code execution through the npm installation. | SELF | REVIEWED |
| 135 | p-risks M05, line 489 | Mitiga describes a project SessionStart hook that restores the malicious endpoint; remediation must remove that persistence as well as repair the configuration and rotate credentials. | MITIGA | REVIEWED |
| 136 | p-risks M05, line 492 | Do you watch ~/.claude.json and project MCP files for changed server URLs? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 137 | p-risks M05, line 492 | Mitiga recommends this. | MITIGA | REVIEWED |
| 138 | p-risks M05, line 493 | Is there a baseline of approved MCP endpoints, with an alert on new local proxies? | SELF | JUDGEMENT / CHECK QUESTION |
| 139 | p-risks M05, line 493 | Mitiga recommends this too. | MITIGA | REVIEWED |
| 140 | p-risks M05, line 494 | After a suspected case, is the config fixed as well as the tokens rotated? | BEARER, OAUTH, SEC | JUDGEMENT / CHECK QUESTION |
| 141 | p-risks M05, line 494 | Mitiga says rotating tokens alone is not enough. | BEARER, MITIGA, OAUTH, SEC | REVIEWED |
| 142 | p-risks M05, line 497 | Typical findingsNo watch on MCP config files, overly long-lived credentials. [inference] | SELF | JUDGEMENT / CHECK QUESTION |
| 143 | p-risks M06, line 502 | OWASP MCP02 Privilege Escalation via Scope Creep · MCP07 Insufficient Authentication and Authorization | BEARER, OAUTH, OWASP, SEC | REVIEWED |
| 144 | p-risks M06, line 503 | In plain words: A key that opens many doors does more harm when stolen. | SEC | REVIEWED |
| 145 | p-risks M06, line 503 | An MCP server must reject client tokens intended for a different service. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 146 | p-risks M06, line 504 | A stolen token with wide scope reaches further than a narrow one. | BEARER, OAUTH, SEC | REVIEWED |
| 147 | p-risks M06, line 504 | The specification forbids token passthrough: an MCP server must not accept tokens that were not issued for it. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 148 | p-risks M06, line 504 | It also warns that a proxy server with a static client ID can be abused (confused deputy). | ARCH, SEC | REVIEWED |
| 149 | p-risks M06, line 507 | Are tokens short-lived and narrow? | BEARER, OAUTH, SEC | JUDGEMENT / CHECK QUESTION |
| 150 | p-risks M06, line 507 | The specification recommends a progressive, least-privilege scope model. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 151 | p-risks M06, line 508 | Do servers you or a supplier run refuse tokens not issued for them? | ARCH, BEARER, OAUTH, SEC | JUDGEMENT / CHECK QUESTION |
| 152 | p-risks M06, line 509 | Proxy servers with a static client ID: per-client consent, exact redirect_uri match and single-use OAuth state. | ARCH, SEC | REVIEWED |
| 153 | p-risks M06, line 512 | Typical findingsBroad personal tokens in MCP config, servers that forward whatever token they receive. [inference] | ARCH, BEARER, OAUTH, SEC | JUDGEMENT / CHECK QUESTION |
| 154 | p-risks M07, line 517 | MCP specification: transports and security best practices | SEC | REVIEWED |
| 155 | p-risks M07, line 518 | In plain words: A server on your own computer can be reached by other programs, and sometimes by web pages. | ARCH, SEC | REVIEWED |
| 156 | p-risks M07, line 518 | A server can also send your client to addresses it should not visit. | ARCH, SEC | REVIEWED |
| 157 | p-risks M07, line 519 | An MCP server that listens on local HTTP can be reached by other local programs and, through DNS rebinding, by web pages. | ARCH, HTTP, SEC | REVIEWED |
| 158 | p-risks M07, line 519 | The specification also warns that a malicious server can supply URLs that point at internal addresses, such as 169.254.169.254. | ARCH, SEC | REVIEWED |
| 159 | p-risks M07, line 522 | Local HTTP servers: do they check the Origin header (must), bind to 127.0.0.1 rather than 0.0.0.0 (should) and require authentication (should)? | ARCH, HTTP, SEC | JUDGEMENT / CHECK QUESTION |
| 160 | p-risks M07, line 522 | Source: specification 2026-07-28. | SEC, VER | REVIEWED |
| 161 | p-risks M07, line 523 | For OAuth metadata discovery, does the client require HTTPS, restrict private and reserved destinations, and recheck redirect targets? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 162 | p-risks M07, line 523 | The guidance recommends these checks for production, with explicit loopback exceptions for development. | SEC | REVIEWED |
| 163 | p-risks M07, line 523 | For server-side client deployments, operators should consider an egress proxy. | ARCH, SEC | REVIEWED |
| 164 | p-risks M07, line 524 | Does the client require HTTPS authorization URLs, allow HTTP only for loopback during local development, reject dangerous schemes such as javascript:, and avoid shell execution when opening URLs? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 165 | p-risks M07, line 524 | The guidance requires these protections. | SEC | REVIEWED |
| 166 | p-risks M07, line 527 | Typical findingsA server left running on localhost with no token, bound to all interfaces. [inference] | ARCH, BEARER, OAUTH, SEC | JUDGEMENT / CHECK QUESTION |
| 167 | p-risks M08, line 532 | OWASP MCP10 Context Injection and Over-Sharing · MCP08 Lack of Audit and Telemetry | OWASP | REVIEWED |
| 168 | p-risks M08, line 533 | In plain words: Without server inventories and suitable logs, it is harder to establish what was shared. [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 169 | p-risks M08, line 534 | MCP calls send data to the selected server. | ARCH, SEC | REVIEWED |
| 170 | p-risks M08, line 534 | Local calls can stay on the machine; external disclosure depends on the server, host and model deployment. | ARCH, SEC | REVIEWED |
| 171 | p-risks M08, line 534 | OWASP separately lists context over-sharing and missing audit telemetry as risks. | OWASP | REVIEWED |
| 172 | p-risks M08, line 534 | No MCP-specific incident for these risks is cited here. | SELF | REVIEWED |
| 173 | p-risks M08, line 537 | Is there a list of servers in use, who runs them and what data each receives? [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 174 | p-risks M08, line 538 | Can you see MCP use? | SELF | JUDGEMENT / CHECK QUESTION |
| 175 | p-risks M08, line 538 | Claude Code usage can be monitored with OpenTelemetry; OTEL_LOG_TOOL_DETAILS=1 is the variable the docs name for tool details. | CC | REVIEWED |
| 176 | p-risks M08, line 539 | Has someone decided what may be sent to remote servers? [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 177 | p-risks M08, line 542 | Typical findingsNo inventory, no usage logs, remote servers receiving whole files. [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 178 | p-vscode , line 565 | What the VS Code documentation says about MCP, and which risk each point touches. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 179 | p-vscode , line 565 | The general risks still apply. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 180 | p-vscode , line 565 | Rows summarize the VS Code docs on 5 November 2026 unless it is tagged [inference]. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 181 | p-vscode , line 565 | Nothing here was tested. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEW SCOPE |
| 182 | p-vscode , line 569 | TopicWhat VS Code doesRisk | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 183 | p-vscode , line 571 | Ways a server gets addedFrom the MCP server gallery (Preview), MCP: Add Server, your user mcp.json, a repo's .vscode/mcp.json or root .mcp.json, a Dev Container's devcontainer.json, or code --add-mcp.M01 | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 184 | p-vscode , line 572 | Servers found in other appschat.mcp.discovery.enabled picks the sources. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 185 | p-vscode , line 572 | GitHub Copilot CLI discovery is on by default. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 186 | p-vscode , line 572 | Claude Desktop, Cursor and Windsurf are off by default.M01 | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 187 | p-vscode , line 573 | Workspace TrustServers in .vscode/mcp.json and .mcp.json follow Workspace Trust. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 188 | p-vscode , line 573 | Restricted mode stops them from starting. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 189 | p-vscode , line 573 | In a trusted workspace they can start with no separate MCP prompt, also after the config changes.M03 | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 190 | p-vscode , line 574 | Autostartchat.mcp.autostart (experimental) defaults to newAndOutdated. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 191 | p-vscode , line 574 | When you send a chat message, VS Code starts servers that never ran or whose config changed. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 192 | p-vscode , line 574 | Setting it to never does not stop Copilot harness sessions from starting their own servers. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 193 | p-vscode , line 574 | Disable the server to stop it.M03 | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 194 | p-vscode , line 575 | Trust and autostart togetherIn a trusted repo, a new or changed server entry can start on your next chat message. [inference] Built from the two rows above. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 195 | p-vscode , line 575 | Not tested.M03 | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 196 | p-vscode , line 576 | Sandbox for local serversThe editor per-server sandbox uses sandboxEnabled and access rules for stdio servers on macOS and Linux; its tool calls are auto-approved. | ARCH, SEC, STDIO, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 197 | p-vscode , line 576 | The Copilot harness has a separate sandbox, including supported Windows systems, controlled by chat.agent.sandbox.mcpServers. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 198 | p-vscode , line 576 | The scopes and approval behavior differ.M03, M04 | BEARER, OAUTH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 199 | p-vscode , line 577 | Tool approvalMCP invocations use approval controls; saved grants and sandbox auto-approval can avoid repeated prompts. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 200 | p-vscode , line 577 | Allow all permissions and Autopilot mode bypass manual tool approval. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 201 | p-vscode , line 577 | Setting ChatToolsAutoApprove to false disables global auto-approval and hides those modes, but does not establish that every invocation prompts in every harness.M04 | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 202 | p-vscode , line 578 | Logins and secretsVS Code-format input variables can prompt for secrets and store them securely. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 203 | p-vscode , line 578 | Servers requiring these inputs are not forwarded to Copilot harness sessions. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 204 | p-vscode , line 578 | OAuth is supported for compatible servers. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 205 | p-vscode , line 578 | Do not commit tokens, passwords or populated authentication headers.M05, M06 | BEARER, OAUTH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 206 | p-vscode , line 579 | Settings SyncIf you select MCP Servers in Settings Sync, your user-profile mcp.json syncs to your other devices. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 207 | p-vscode , line 579 | Workspace .mcp.json files do not. [inference] A bad entry on one device could reach the others. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 208 | p-vscode , line 579 | Not observed.M05 | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 209 | p-vscode , line 580 | What servers can ask of the modelchat.mcp.serverSampling sets which models are exposed to servers for background requests.M08 | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 210 | p-vscode , line 581 | Organisation policyChatMCP (chat.mcp.access), ChatAllowedMcpServers, ChatAllowManagedMcpServersOnly, ChatDeniedMcpServers and McpGalleryServiceUrl. | ARCH, CC, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 211 | p-vscode , line 581 | When an allowlist is set, only matching servers may be installed or run. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 212 | p-vscode , line 581 | A deny rule always wins. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 213 | p-vscode , line 581 | These editor policies do not establish coverage of independently discovered Copilot runtime servers; check the harness-specific management guidance.M01 | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 214 | p-vscode , line 582 | Other agents inside VS CodeClaude and Codex harness integrations are disabled while Copilot enterprise-managed settings apply, because those harnesses cannot enforce them. | CODEX, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 215 | p-vscode , line 582 | This includes server-, MDM- and file-delivered settings. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 216 | p-vscode , line 582 | It is a restriction on harness availability, not on selecting Claude or OpenAI models within Copilot.M01 | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 217 | p-vscode , line 583 | VisibilityMCP: Show Installed Servers lists the servers. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 218 | p-vscode , line 583 | Copilot Chat can export traces, metrics and events through OpenTelemetry, which covers tool execution.M08 | CC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 219 | p-vscode , line 584 | Example commandsThe docs' own example runs npx -y @playwright/mcp@latest, an unpinned package. [inference] Pinning a package version reduces changes from resolving @latest; it does not guarantee immutable dependencies or safe code.M02 | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 220 | p-vscode , line 591 | VS Code has more than one kind of agent session (local and Copilot harness), and the settings do not always reach both. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 221 | p-vscode , line 591 | The rows say where the docs name a difference. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 222 | p-vscode , line 591 | Settings and policy names come from the docs; none was run on a managed machine. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 223 | p-evidence , line 599 | What was checked, what is interpretation by AI, and what is still open. | SELF | REVIEWED |
| 224 | p-sources , line 608 | All opened on 5 November 2026, except the Developer-WS page, which is on this site. | SELF | REVIEW SCOPE |
| 225 | p-sources , line 614 | Marked [inference] is interpretation by AI, not stated in a source. | SELF | JUDGEMENT / CHECK QUESTION |
| 226 | p-sources , line 614 | The documented product settings and attack paths were not tested on a real system. | SELF | REVIEW SCOPE |
| 227 | p-sources , line 615 | No setting or command on this page was run on a managed machine. | SELF | REVIEW SCOPE |
| 228 | p-sources , line 616 | Versions and dates change quickly in this area. | SELF | REVIEWED |
| 229 | p-sources , line 616 | Check the "Current" box against the sources before you use it in a report. | SELF | REVIEWED |
| 230 | p-sources , line 617 | Made with AIThis page was written with the help of AI. | SELF | REVIEW SCOPE |
| 231 | p-sources , line 617 | Its content has not necessarily been fully quality checked by a human. | SELF | REVIEWED |
| 232 | PLACE / M01 / src | Servers come from many places. Anthropic says it does not security-audit or manage any MCP server. | ARCH, CC, SEC | REVIEWED |
| 233 | PLACE / M01 / cfgin | A project can carry a file such as .mcp.json that names servers to start. | ARCH, SEC | REVIEWED |
| 234 | PLACE / M01 / agent | By default in Claude Code anyone can connect any MCP server, so each developer decides what the agent can reach. | ARCH, CC, SEC | REVIEWED |
| 235 | PLACE / M01 / policy | Claude Code, Codex and VS Code each have an MCP allowlist. In Claude Code, deny rules win within their scope; in-process SDK servers bypass these checks. A user-assigned name does not identify the underlying server. | ARCH, BEARER, CC, CODEX, OAUTH, SEC, VCONF | REVIEWED |
| 236 | PLACE / M02 / pkg | A server installed from a package runs that package's code. OWASP lists dependency tampering as MCP04. | ARCH, OWASP, SEC | REVIEWED |
| 237 | PLACE / M02 / local | Without isolation, local server code can run with the MCP client's privileges. The specification names arbitrary code execution, no visibility and data exfiltration for a compromised one. | ARCH, SEC | REVIEWED |
| 238 | PLACE / M02 / agent | OWASP lists Tool Poisoning as MCP03. The model reads tool descriptions, so a changed description can change what the agent does. [inference] | ARCH, OWASP, SEC | JUDGEMENT |
| 239 | PLACE / M02 / policy | Allow local servers by exact command. Claude Code does not compare the env block; the Codex string form does not check args, cwd or env. | ARCH, CC, CODEX, SEC | REVIEWED |
| 240 | PLACE / M03 / cfgin | A client with one-click local setup must get consent before running a command, and show the exact command in full (specification 2026-07-28). | ARCH, SEC, VER | REVIEWED |
| 241 | PLACE / M03 / cfgf | A malicious startup command in the client config is one of the compromise paths the specification names. | ARCH, SEC | REVIEWED |
| 242 | PLACE / M03 / local | Without isolation, a local server can act with the MCP client's privileges. The specification names arbitrary code execution, no visibility and data exfiltration. | ARCH, SEC | REVIEWED |
| 243 | PLACE / M03 / files | Data exfiltration is one of the consequences the specification names for a compromised local server. | ARCH, SEC | REVIEWED |
| 244 | PLACE / M03 / agent | The specification says clients should run local servers sandboxed with minimal default privileges. | ARCH, SEC | REVIEWED |
| 245 | PLACE / M04 / content | Pages, tickets and files that a tool reads can carry hidden instructions. OWASP lists this as MCP06. | OWASP, VSEC | REVIEWED |
| 246 | PLACE / M05 / pkg | In Mitiga's research an npm postinstall hook edited ~/.claude.json. It needs code execution through the install. | MITIGA | REVIEWED |
| 247 | PLACE / M05 / cfgf | Mitiga reports that the hook rewrote an MCP server URL to an attacker's localhost proxy, pre-set trust-dialog flags and added a project SessionStart hook. | ARCH, MITIGA, SEC | REVIEWED |
| 248 | PLACE / M05 / lhttp | Mitiga demonstrates interception and reuse of an Atlassian OAuth bearer token; separate refresh-token capture is not demonstrated in the article. | BEARER, MITIGA, OAUTH, SEC | REVIEWED |
| 249 | PLACE / M05 / tok | Mitiga says rotating tokens alone is not enough. | BEARER, MITIGA, OAUTH, SEC | REVIEWED |
| 250 | PLACE / M05 / edr | Mitiga recommends baselining approved MCP endpoints, watching ~/.claude.json and project MCP files, and alerting on new local proxies. | MITIGA | REVIEWED |
| 251 | PLACE / M06 / tok | A stolen token with broad scope has a larger blast radius. The specification recommends progressive, least-privilege scopes. | BEARER, OAUTH, SEC | REVIEWED |
| 252 | PLACE / M06 / mcpr | An MCP server must not accept tokens that were not issued for it. The authorization specification forbids token passthrough. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 253 | PLACE / M06 / saas | A proxy server with a static client ID can be abused (confused deputy). Protections include per-client consent, exact redirect_uri match, single-use state. | ARCH, SEC | REVIEWED |
| 254 | PLACE / M07 / lhttp | Servers must validate the Origin header to stop DNS rebinding, should bind to 127.0.0.1 rather than 0.0.0.0, and should authenticate (specification 2026-07-28). | ARCH, HTTP, SEC, VER | REVIEWED |
| 255 | PLACE / M07 / egress | A malicious server can supply URLs that point at internal addresses such as 169.254.169.254. For production OAuth discovery, restrict private destinations and redirects. Server-side client operators should consider an egress proxy; development loopback needs explicit exceptions. | ARCH, SEC | REVIEWED |
| 256 | PLACE / M07 / agent | Clients must require HTTPS authorization URLs, allowing HTTP only for development loopback, reject dangerous schemes, and avoid shell execution when opening URLs (security guidance, 2026-07-28). | ARCH, SEC, VER | REVIEWED |
| 257 | PLACE / M08 / agent | OWASP lists Context Injection and Over-Sharing as MCP10: more context goes to a server than it needs. | ARCH, OWASP, SEC | REVIEWED |
| 258 | PLACE / M08 / policy | An inventory and usage logs help establish which servers are used. [inference] OWASP MCP08 concerns missing audit and telemetry. | ARCH, OWASP, SEC | JUDGEMENT |
| 259 | PLACE / M08 / tele | Claude Code usage can be monitored with OpenTelemetry; OTEL_LOG_TOOL_DETAILS=1 is the variable the docs name for tool details. | CC | REVIEWED |
| 260 | START / M01 | Claude Code allowManagedMcpServersOnly with an allowlist of both URLs and commands; the Codex and VS Code allowlists, with session-specific exceptions reviewed; friction: Moderate | ARCH, CC, CODEX, SEC, VCONF | JUDGEMENT |
| 261 | START / M02 | Allow local servers by exact command, not by name; friction: Low | ARCH, SEC | JUDGEMENT |
| 262 | START / M03 | Check that each client shows the full command and asks before running it; friction: Low | ARCH, SEC | JUDGEMENT |
| 263 | START / M04 | Use separate sessions for untrusted reading, without tools that can write or send; friction: Moderate | SELF | JUDGEMENT |
| 264 | START / M05 | Alert on changes to ~/.claude.json and project MCP files; friction: Low | SELF | JUDGEMENT |
| 265 | START / M06 | Short-lived, narrowly scoped tokens per server; friction: Moderate | ARCH, BEARER, OAUTH, SEC | JUDGEMENT |
| 266 | START / M07 | Bind local HTTP servers to 127.0.0.1, check Origin and require a token; friction: Low | ARCH, BEARER, HTTP, OAUTH, SEC | JUDGEMENT |
| 267 | START / M08 | A list of approved servers, and Claude Code usage export through OpenTelemetry; friction: Low | ARCH, CC, SEC | JUDGEMENT |
| 268 | EVIDENCE / Checked against sources | OWASP MCP Top 10 names and IDs (MCP01 to MCP10), read 5 November 2026. The project is in beta (phase 3). | OWASP | REVIEWED |
| 269 | EVIDENCE / Checked against sources | MCP specification 2026-07-28 (the current version), Streamable HTTP: Origin validation, localhost binding, authentication. | ARCH, HTTP, SEC, VER | REVIEWED |
| 270 | EVIDENCE / Checked against sources | MCP security best practices (2026-07-28): confused deputy, token passthrough, SSRF, local server compromise, authorization URL validation, scope minimisation. | ARCH, BEARER, OAUTH, SEC, VER | REVIEWED |
| 271 | EVIDENCE / Checked against sources | Mitiga research, published 5 May 2026, updated 30 October 2026: endpoint rewriting, bearer-token interception and reuse, prerequisite local code execution, and the vendor response as reported by Mitiga. | BEARER, MITIGA, OAUTH, SEC | REVIEWED |
| 272 | EVIDENCE / Checked against sources | Claude Code managed MCP page: managed-mcp.json, allowedMcpServers and deniedMcpServers, allowManagedMcpServersOnly, URL and command matching, OpenTelemetry. | ARCH, CC, SEC | REVIEWED |
| 273 | EVIDENCE / Checked against sources | Codex managed configuration: mcp_servers allowlist and string versus structured command matching; neither form verifies cwd or environment variables. | ARCH, CODEX, SEC | REVIEWED |
| 274 | EVIDENCE / Checked against sources | VS Code docs (agent customization, manage MCP servers, MCP configuration reference, AI security, policies, telemetry): the rows on the VS Code tab. | ARCH, SEC, VCONF | REVIEWED |
| 275 | EVIDENCE / Interpretation by AI | The choice of eight risks, their order and the OWASP mapping. | OWASP | JUDGEMENT |
| 276 | EVIDENCE / Interpretation by AI | Where each risk sits on the map. | SELF | JUDGEMENT |
| 277 | EVIDENCE / Interpretation by AI | Statements tagged [inference] (advice questions, not facts), and the friction estimates. | SELF | JUDGEMENT |
| 278 | EVIDENCE / Interpretation by AI | Which VS Code facts are shown, and the risk each is tied to. | VCONF | JUDGEMENT |
| 279 | EVIDENCE / Still open | The specification can change. This page was checked against version 2026-07-28, the current one on 5 November 2026. | VER | REVIEWED |
| 280 | EVIDENCE / Still open | Only one MCP-specific research demonstration (Mitiga) is cited. For the other risks no incident was verified. That does not mean none exists. | MITIGA | REVIEWED |
| 281 | EVIDENCE / Still open | Mitiga reports that Anthropic told it the issue was out of scope and by design. Mitiga disagrees. This page does not take a side. | BEARER, CC, MITIGA, OAUTH, SEC | REVIEWED |
| 282 | EVIDENCE / Still open | Product policy coverage depends on the harness and configuration source. Editor controls do not necessarily cover independently discovered Copilot servers. | ARCH, SEC | REVIEWED |
| 283 | EVIDENCE / Still open | No setting or command on this page was run on a managed machine. | SELF | REVIEWED |
| 284 | EVIDENCE / Still open | VS Code has local and Copilot harness sessions. Settings do not always reach both. | VCONF | REVIEWED |
| 285 | EVIDENCE / Still open | Documentation was reviewed, but no exploit or managed-product behavior was reproduced. Mitiga is a research demonstration, not evidence here of an observed victim incident. | MITIGA | REVIEWED |
| 286 | SOURCES / OWASP MCP Top 10 | OWASP. Beta (phase 3). MCP01 to MCP10. | OWASP | REVIEWED |
| 287 | SOURCES / MCP specification: transports (Streamable HTTP) | Model Context Protocol, version 2026-07-28 (current). Origin validation, localhost binding, authentication. | ARCH, HTTP, SEC, VER | REVIEWED |
| 288 | SOURCES / MCP security best practices (2026-07-28) | Model Context Protocol. Confused deputy, token passthrough, SSRF, local server compromise, authorization URL validation, scope minimisation. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 289 | SOURCES / Stealing MCP tokens in Claude Code via ~/.claude.json | Mitiga (5.5.2026, updated 30.10.2026). Attack steps, vendor response and recommendations. | MITIGA | REVIEWED |
| 290 | SOURCES / Claude Code: managed MCP | Anthropic. managed-mcp.json, allowlist and denylist matching, allowManagedMcpServersOnly, OpenTelemetry monitoring. | ARCH, CC, SEC | REVIEWED |
| 291 | SOURCES / Codex managed configuration | OpenAI. requirements.toml mcp_servers allowlist and identity forms. | ARCH, SEC | REVIEWED |
| 292 | SOURCES / VS Code: Add MCP servers | Microsoft. Gallery, adding servers, trust warning. | ARCH, SEC | REVIEWED |
| 293 | SOURCES / VS Code: Manage MCP servers | Microsoft. Workspace Trust, autostart, sandbox, Settings Sync, Dev Containers. | ARCH, SEC | REVIEWED |
| 294 | SOURCES / VS Code: MCP configuration reference | Microsoft. Settings, discovery sources, sandbox schema. | ARCH, SEC | REVIEWED |
| 295 | SOURCES / VS Code: AI security | Microsoft. Tool approval, permission levels, secure credentials store, MCP sandboxing. | ARCH, SEC | REVIEWED |
| 296 | SOURCES / Centrally manage VS Code settings with policies | Microsoft. ChatMCP, ChatAllowedMcpServers, ChatDeniedMcpServers, McpGalleryServiceUrl, ChatToolsAutoApprove. | ARCH, SEC | REVIEWED |
| 297 | SOURCES / VS Code: enterprise telemetry | Microsoft. OpenTelemetry export from Copilot Chat. | CC | REVIEWED |
| 298 | SOURCES / Developer workstation risk map | This site. The wider page this one was cut from; it covers MCP together with VS Code, git and agents. | VCONF | REVIEWED |
| 299 | SOURCES / MCP specification: stdio | Subprocess launch and standard-stream transport. | SELF | REVIEWED |
| 300 | SOURCES / MCP specification: tools | Tool capabilities, invocation and host interaction choices. | ARCH, SEC | REVIEWED |
| 301 | SOURCES / MCP versioning | Current protocol revision and compatibility rules. | SELF | REVIEWED |
| 302 | SOURCES / OAuth bearer token usage (RFC 6750) | Bearer possession and authorized resource access. | SELF | REVIEWED |
| 303 | SOURCES / VS Code: manage AI settings | Management layers, precedence and harness coverage. | SELF | REVIEWED |
| 304 | SOURCES / MCP architecture overview | Hosts, clients, servers and application control of model context. | ARCH, SEC | REVIEWED |
| 305 | SOURCES / OAuth 2.0 (RFC 6749) | Access tokens, service credentials and authorization scopes. | BEARER, OAUTH, SEC | REVIEWED |

## Rendering and interaction validation

Passed all five tabs at 1440px and 375px in light and dark modes (20 combinations). No page-wide horizontal overflow and no JavaScript exceptions or console error events. Visually inspected desktop and phone screenshots in both themes, including the diagram in both themes. Confirmed status persistence/tally and a diagram marker popover. Browser checks used an isolated temporary profile.

Inline JavaScript syntax and embedded data parsed successfully. No duplicate HTML ids, no changed public ids, no em or en dashes, and no HTML paragraph over 60 words. The site has no build step. Product settings and attack paths remain untested.

Reviewed page SHA-256: `379181795945cbb1ff004d75dbb5dc9f30d39d533bb1860b1fdb903b082a4177`.

## Historical ledger, 2 November 2026 (superseded)

The following records the earlier review, including incorrect OK verdicts. It is retained for history and is not current evidence.

# Fact check: MCP Risk Map

Belongs to [MCP-Risk-Map.html](MCP-Risk-Map.html). Other notes for the same page: [plan](MCP-Risk-Map.plan.md), [decisions](MCP-Risk-Map.decisions.md). Cut from [Developer-WS.html](Developer-WS.html).

Checked 2 November 2026. Sources were opened that day. Page checked: `MCP-Risk-Map.html`, MD5 `a35d1813dcbad214fb87ee1bf9c28e1e`.

## What was found

- Every factual claim on the page is listed below with its source and verdict.
- Spec rows were re-checked on 2 November 2026 against version 2026-07-28 (current). The earlier pages used 2025-06-18 and the draft.
- 4 claims in the first draft had no support in the sources read and were removed (see **Removed**).
- Only one MCP-specific attack (Mitiga) is cited. For the other seven risks no incident was verified, and the page says so.
- Not run: no setting, command or product behaviour on this page was tested on a real machine. Rendering was checked in a browser (no console errors, tabs, popovers, status tally, phone width).

Sources: **OWASP** = owasp.org/www-project-mcp-top-10. **SPEC-T** = MCP specification 2026-07-28 (current version per the versioning page), Streamable HTTP. **SPEC-D** = MCP security best practices, 2026-07-28. **MITIGA** = mitiga.io blog on Claude Code MCP token theft. **CC** = code.claude.com managed-mcp. **CODEX** = Codex managed configuration. **VSC** = VS Code enterprise policies.

| Verdict | Meaning |
| --- | --- |
| OK | Matches the source named. |
| JUDGEMENT | My own grouping, order or advice, tagged `[inference]` on the page. These are checklist questions and ratings, not factual claims. |
| CUT | Removed from the page because no source supports it. |
| CONTESTED | Sources or parties disagree; the page shows both. |

## Statements

| # | Statement (short) | Source | Verdict |
| --- | --- | --- | --- |
| 1 | OWASP MCP Top 10 is beta; IDs MCP01 to MCP10 and their names as mapped | OWASP | OK |
| 2 | Claude Code: by default anyone can connect any MCP server | CC | OK |
| 3 | Anthropic reviews connectors before listing them in its Directory, but does not security-audit or manage any MCP server | CC security page, MCP section (checked 2 Nov 2026, verbatim) | OK |
| 4 | `managed-mcp.json` gives a fixed set; empty `mcpServers` disables MCP | CC | OK |
| 5 | `allowedMcpServers` with `allowManagedMcpServersOnly`; denylist wins | CC | OK |
| 6 | Once any `serverUrl` entry exists every remote server must match a URL; same for `serverCommand` and stdio | CC | OK |
| 7 | `serverName` is not a security control | CC | OK |
| 8 | Codex `[mcp_servers.<name>]` allowlist in `requirements.toml` | CODEX | OK |
| 9 | VS Code `ChatAllowedMcpServers` exists as an allowlist (names only, no `chat.mcp.access` values) | VSC | OK |
| 10 | Local servers: allow by exact command; Claude does not compare `env` | CC | OK |
| 11 | Codex string `command` form does not check args, cwd, env; structured form is stricter | CODEX | OK |
| 12 | Spec: local server compromise risks are malicious startup command, arbitrary code execution, no visibility, data exfiltration | SPEC-D | OK |
| 13 | Client with one-click local setup must get consent and show the full command | SPEC-D | OK |
| 14 | Clients should sandbox local servers; server authors should use stdio or restrict HTTP | SPEC-D | OK |
| 15 | Removed from the page: "clients should support stdio" is in 2025-06-18 but not on the current stdio page | SPEC-T | CUT |
| 16 | Clients should run local servers sandboxed with minimal default privileges (the page no longer says anything about product support) | SPEC-D | OK |
| 17 | Tool poisoning, prompt injection, over-sharing and audit gaps are OWASP categories (MCP03, MCP06, MCP10, MCP08) | OWASP | OK |
| 18 | Tool poisoning and prompt injection are OWASP categories; the mechanism sentences were cut | OWASP | OK |
| 19 | Mitiga: npm postinstall hook edits `~/.claude.json` and points an MCP server URL at an attacker localhost proxy | MITIGA | OK |
| 20 | The proxy captured OAuth bearer and refresh tokens (Atlassian example) | MITIGA | OK |
| 21 | Needs code execution through the npm install | MITIGA | OK |
| 22 | The hook also pre-set trust-dialog flags and added a project SessionStart hook | MITIGA | OK |
| 23 | Mitiga published 5 May 2026, updated 30 October 2026 | MITIGA | OK |
| 24 | Mitiga recommends baselining endpoints, watching `~/.claude.json` and project MCP files, alerting on new local proxies, and says rotating tokens alone is not enough | MITIGA | OK |
| 25 | Anthropic called it out of scope and by design; Mitiga disagrees | MITIGA | CONTESTED |
| 26 | Stolen broad token has a larger blast radius; draft recommends progressive least-privilege scopes | SPEC-D | OK |
| 27 | Token passthrough is forbidden: a server must not accept tokens not issued for it | SPEC-D | OK |
| 28 | Confused deputy: per-client consent, exact `redirect_uri` match, single-use `state` | SPEC-D | OK |
| 29 | Local HTTP servers must validate `Origin`, should bind to 127.0.0.1 not 0.0.0.0, should authenticate | SPEC-T | OK |
| 30 | DNS rebinding can reach local servers from web pages | SPEC-T | OK |
| 31 | A malicious server can supply URLs pointing at internal addresses such as 169.254.169.254 | SPEC-D | OK |
| 32 | Clients should require HTTPS and block private and reserved ranges; operators should consider an egress proxy | SPEC-D | OK |
| 33 | Authorization URLs: allow only http and https, reject `javascript:`, never open with shell commands | SPEC-D | OK |
| 34 | Claude Code usage can be monitored with OpenTelemetry; `OTEL_LOG_TOOL_DETAILS=1` is the variable the docs name | CC | OK |
| 35 | `managedMcpServers` needs Claude Code 2.1.259 or later | CC | OK |
| 36 | Removed: supplier controls code, data may be retained, tool results reach the model provider (no source read) | none | CUT |
| 37 | The eight-risk grouping, order, map placement and friction ratings | none | JUDGEMENT (labelled on the page) |
| 38 | Every first-control row on Where to start | CC, CODEX, SPEC, MITIGA | OK for the setting; friction is JUDGEMENT |
| 39 | The page was checked against spec 2026-07-28, the current version on 2 November 2026: Origin MUST, localhost SHOULD, auth SHOULD, and the best-practices text all match | SPEC-T, SPEC-D | OK |

## Removed

These are not on the page, because no source I read states them:

- That Anthropic reviews connectors in a Directory.
- That the SessionStart hook "reapplies" the config, and that the redirect "stays in place".
- A "consent cookie" detail in the confused-deputy line, and the three consequences of passthrough.
- "Check redirects" and "in OAuth metadata" in the SSRF lines.
- "Clients should support stdio" (not on the 2026-07-28 stdio page).
- Remote servers as suppliers who may retain data; the model cannot tell instructions from data; tool results reach the model provider; "product support differs, not tested".

## Left out on purpose

- The VS Code `chat.mcp.access` values: Microsoft's docs and source disagree.
- Plugin4Shell: it is about plugin pinning, not MCP.
- Any MCP incident besides Mitiga: none was verified.
- Codex plugin-bundled servers: not on the page.

## Limits

- The spec can change after 2 November 2026.
- No setting or command was run on a real machine; every product claim rests on its vendor docs.

## Learner additions (2 November 2026)
- "How MCP works" box: client, server, tools, stdio and HTTP. Matches the MCP specification transports page (2026-07-28). General description, no new claims.
- Glossary: DNS rebinding and the Origin check, confused deputy, token passthrough, SSRF and egress proxy use the wording of the specification security best practices page (2026-07-28). Token, scope, allowlist, sandbox and prompt injection are general definitions, not tied to one source.
- "In plain words" line per risk: restates the risk paragraph in simpler words. Judgement, no new facts.
- "How to set it": the vendor setting names and matching rules moved here unchanged from the check lists (M01, M02).

## VS Code tab (2 November 2026)
Source pages (code.visualstudio.com/docs): agent-customization/mcp-servers (A), agents/run/manage-mcp-servers (B), agents/reference/mcp-configuration (C), copilot/security (D), enterprise/policies (E), enterprise/telemetry (F). Text was read from the fetched pages. Nothing was run in VS Code.

| Row | Statement | Source | Verdict |
|---|---|---|---|
| V1 | Servers are added through gallery, MCP: Add Server, user mcp.json, .vscode/mcp.json, root .mcp.json, devcontainer.json, code --add-mcp | A, B, C | OK |
| V2 | Discovery: Copilot CLI on by default; Claude Desktop, Cursor, Windsurf off by default | C | OK |
| V3 | Workspace mcp files inherit Workspace Trust; restricted mode blocks start; trusted workspace starts without separate prompt, also after config changes | B | OK |
| V4 | chat.mcp.autostart experimental, default newAndOutdated, starts never-run or changed servers on chat message; never does not stop Copilot harness | B, C | OK |
| V5 | Trust plus autostart means a changed entry can start on the next chat message | V3 + V4 | JUDGEMENT, tagged [inference], not tested |
| V6 | Per-server sandbox, stdio only, macOS and Linux only, tool confirmations auto-approved | B, C, D | OK |
| V7 | MCP tool approval at session, workspace or user level; Allow all and Autopilot auto-approve; ChatToolsAutoApprove turns global auto-approval off | D | OK |
| V8 | Secure credentials store for sensitive inputs; OAuth per MCP authorization spec; do not commit secrets | D, B | OK |
| V9 | Settings Sync can sync user mcp.json, not workspace .mcp.json | B | OK. The "bad entry could spread" part is [inference], not observed |
| V10 | chat.mcp.serverSampling sets which models are exposed to servers | C | OK |
| V11 | Policies ChatMCP, ChatAllowedMcpServers, ChatAllowManagedMcpServersOnly, ChatDeniedMcpServers, McpGalleryServiceUrl; allowlist and deny precedence | E | OK. chat.mcp.access values left out on purpose |
| V12 | Claude and Codex harnesses cannot enforce Copilot enterprise-managed settings and are disabled when they apply | D | OK |
| V13 | MCP: Show Installed Servers; Copilot Chat OTel export covers tool execution | C, F | OK |
| V14 | Docs example runs npx -y @playwright/mcp@latest | B | OK. "Pinning avoids silent change" is [inference] |

## 8 November 2026, Microsoft ecosystem view

Belongs to the Microsoft ecosystem scope of [MCP-Risk-Map.html](MCP-Risk-Map.html). Scope: MCP as used through VS Code, Visual Studio, GitHub Copilot, Copilot Studio, Windows, Azure and Microsoft Entra.

Method: every source page was fetched on 8 November 2026 and each quote was checked word for word against the page text with `python3 -I scripts/check-mcp-risk-map.py <cache-dir>`. The VS Code tab rows keep their 5 November 2026 check and are shared by both views.

Limits: nothing was tested on a real system. No setting or command was run on a managed machine. Preview features may change. Quote `cs3` matches only when whitespace is ignored, because the source lists a bold label and a colon as separate elements. The script is a mechanical check: a pass proves the quotes are on the pages the sources serve today and that a verdict was recorded for the exact wording. It does not prove a verdict or a claim is right.

### Sources

| Key | Source | URL | Note |
|---|---|---|---|
| odr | MCP on Windows: Windows On-device Agent Registry | https://learn.microsoft.com/en-us/windows/ai/mcp/overview | Microsoft Learn. Prerelease. Separate environment, Intune control, logging. |
| vs | Visual Studio: use MCP servers | https://learn.microsoft.com/en-us/visualstudio/ide/mcp-servers | Microsoft Learn. Server trust (18.7 or later), tool confirmation, tool-list reset, allow list policies. |
| ghal | GitHub: configure an enterprise MCP allowlist | https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-enterprise-allowlist | GitHub Docs. managed-settings.json, allowedMcpServers, deniedMcpServers. |
| ghreg | GitHub: configure an MCP registry | https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-mcp-registry | GitHub Docs. Public preview; not the recommended method. |
| ghenf | GitHub: MCP private registry enforcement | https://docs.github.com/en/copilot/reference/enterprise-administrators/mcp-private-registry-enforcement | GitHub Docs. Name and ID matching; bypass by editing configuration files. |
| csadd | Copilot Studio: add an existing MCP server | https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent | Microsoft Learn. Authentication options, API key in header or query, SSE. |
| csdlp | Copilot Studio: data loss prevention | https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention | Microsoft Learn. Connector blocking and MCP tools. |
| gsa | Entra Global Secure Access: MCP firewall | https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-mcp-firewall | Microsoft Learn. Preview. Server URL patterns, TLS inspection. |
| gsalog | Entra Global Secure Access: MCP logging | https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-view-model-context-protocol-logging | Microsoft Learn. Preview. Shadow MCP discovery; remote servers only. |
| apim | Azure API Management: secure MCP servers | https://learn.microsoft.com/en-us/azure/api-management/secure-mcp-servers | Microsoft Learn. Inbound and outbound access, credential manager, header forwarding. |
| a365gw | Agent 365: tools gateway | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-tools-gateway | Microsoft Learn. Preview. Block or allow a server, LiteLLM gateway. |
| a365byo | Agent 365: bring your own MCP server | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-byo-mcp-server | Microsoft Learn. Preview. Defender advanced hunting; supported client surfaces. |
| azmcp | Azure MCP Server: security | https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security | Microsoft Learn. Production data, Azure identity, change control, official server. |
| cve26118 | CVE-2026-26118 (Azure MCP Server) | https://cveawg.mitre.org/api/cve/CVE-2026-26118 | CVE record published by Microsoft. A vendor advisory, not an observed incident. |
| cve32211 | CVE-2026-32211 (Azure MCP Server) | https://cveawg.mitre.org/api/cve/CVE-2026-32211 | CVE record published by Microsoft. A vendor advisory, not an observed incident. |
| inv | Invariant Labs: GitHub MCP exploited | https://invariantlabs.ai/blog/mcp-github-vulnerability | Invariant Labs. Third-party research, not a Microsoft or GitHub advisory. |
| vscm | VS Code: manage MCP servers | https://code.visualstudio.com/docs/agents/run/manage-mcp-servers | Microsoft. Workspace Trust, autostart, sandbox. |
| vspol | Centrally manage VS Code settings with policies | https://code.visualstudio.com/docs/enterprise/policies | Microsoft. ChatAllowedMcpServers, ChatDeniedMcpServers. |
| vstel | VS Code: enterprise telemetry | https://code.visualstudio.com/docs/enterprise/telemetry | Microsoft. OpenTelemetry export from Copilot Chat. |
| sphttp | MCP specification: transports (Streamable HTTP) | https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http | Model Context Protocol, version 2026-07-28. Origin validation, localhost binding. |
| spsec | MCP security best practices (2026-07-28) | https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices | Model Context Protocol. SSRF, authorization URL validation. |
| spver | MCP versioning | https://modelcontextprotocol.io/specification/versioning | Model Context Protocol. Current protocol version. |
| owasp | OWASP MCP Top 10 | https://owasp.org/www-project-mcp-top-10/ | OWASP. Beta (phase 3). MCP01 to MCP10. |
| mit | Mitiga: MCP token theft in Claude Code | https://www.mitiga.io/blog/claude-code-mcp-token-theft-mitm | Mitiga. Third-party research on Claude Code, not on a Microsoft product. |

### Quotes

Verdict VERIFIED 8 Nov 2026 means the quote was found in the source. Each quote is shown on the page in the place named in the last column.

| Id | Source | Quote | Used in | Verdict |
|---|---|---|---|---|
| odr2 | odr | Some information relates to prereleased product that might change substantially before it's commercially released. | M04.body[1]; M08.body[2]; row[5] Windows on-device agent registry (prerelease); place[13] M03/policy; place[16] M04/local; place[30] M08/policy; callout[2] | VERIFIED 10 Nov 2026 |
| odr3 | odr | MCP servers are contained in a separate environment by default and can only access approved resources, limiting vulnerability to threats like cross-prompt injection attacks | M04.body[1]; row[5] Windows on-device agent registry (prerelease); place[16] M04/local | VERIFIED 8 Nov 2026 |
| odr4 | odr | users and IT admins can control access to MCP servers for each agent by using Windows Settings and management tools like Microsoft Intune | row[5] Windows on-device agent registry (prerelease); place[13] M03/policy | VERIFIED 10 Nov 2026 |
| odr5 | odr | users and administrators can log and audit interactions between MCP clients and servers | M08.body[2]; row[5] Windows on-device agent registry (prerelease); place[30] M08/policy | VERIFIED 8 Nov 2026 |
| vs1 | vs | MCP server trust is available in Visual Studio 2026 version 18.7 and later. | M03.checks[1]; row[0] Visual Studio trust and tool reset; place[9] M03/cfgin; callout[3] | VERIFIED 8 Nov 2026 |
| vs2 | vs | Visual Studio asks you to trust an MCP server again when the server changes since the last time you used it. | M03.body[0]; M05.body[1]; row[0] Visual Studio trust and tool reset; place[9] M03/cfgin | VERIFIED 8 Nov 2026 |
| vs3 | vs | Server configuration details, such as transport type, URL, command, or arguments. | M03.body[0]; M05.body[1]; place[9] M03/cfgin; place[17] M05/cfgf | VERIFIED 8 Nov 2026 |
| vs6 | vs | Visual Studio resets any prior acceptances or permissions on tools (to prevent rug-pull attacks), refetches the tool list, and updates the count and UI live. | M02.body[1]; row[0] Visual Studio trust and tool reset; place[7] M02/agent | VERIFIED 8 Nov 2026 |
| vs7 | vs | When you invoke a tool, Copilot requests confirmation to run the tool. | M03.checks[2]; row[1] Visual Studio tool confirmation; place[13] M03/agent | VERIFIED 8 Nov 2026 |
| vs8 | vs | You can automatically confirm the specific tool for the current session, the current solution, or all future invocations. | M03.checks[2]; M04.checks[1]; row[1] Visual Studio tool confirmation; place[13] M03/agent; place[15] M04/agent | VERIFIED 8 Nov 2026 |
| vs9 | vs | Visual Studio also checks for MCP configurations that other development environments set up. | row[2] Visual Studio configuration discovery; place[1] M01/cfgin | VERIFIED 8 Nov 2026 |
| vs10 | vs | MCP server usage in Visual Studio respects allow list policies set by organization administrators through GitHub. | M01.checks[1]; place[3] M01/policy | VERIFIED 8 Nov 2026 |
| vs11 | vs | Visual Studio respects whatever command you specify, so you can pin versions or pass flags as needed. | M02.checks[0]; M02.how[0]; place[8] M02/policy | VERIFIED 8 Nov 2026 |
| gh1 | ghal | You can define an allowlist and denylist to control which MCP servers users in your enterprise can run in Copilot clients and cloud sandboxes. | M01.body[0]; place[12] M03/policy | VERIFIED 10 Nov 2026 |
| gh2 | ghal | don't apply to MCP servers defined in repository custom agent profiles. | M01.body[0]; M01.checks[0]; row[3] GitHub allowlist and registry (preview); place[3] M01/policy; place[12] M03/policy | VERIFIED 10 Nov 2026 |
| gh3 | ghal | Because deny rules take precedence | M01.how[0] | VERIFIED 8 Nov 2026 |
| gh4 | ghal | You can match by name, server URL, or specific commands. | M01.how[0]; place[12] M03/policy | VERIFIED 10 Nov 2026 |
| gh5 | ghal | This blocks all servers except built-in default servers. | M01.how[1] | VERIFIED 8 Nov 2026 |
| gh6 | ghreg | This feature is in public preview and is not the recommended method for restricting access to MCP servers. | M01.body[1]; row[3] GitHub allowlist and registry (preview); place[0] M01/src; callout[2] | VERIFIED 8 Nov 2026 |
| gh7 | ghenf | Enforcement is based only on server name/ID matching, which can be bypassed by editing configuration files. | M01.body[1]; row[3] GitHub allowlist and registry (preview) | VERIFIED 8 Nov 2026 |
| cs1 | csadd | Copilot Studio no longer supports SSE for MCP after August 2025. | row[4] Copilot Studio authentication, SSE and DLP | VERIFIED 8 Nov 2026 |
| cs2 | csadd | Select this option if your MCP server requires the API key to be sent as a query parameter in the URL. | M05.body[2]; M05.checks[1]; row[4] Copilot Studio authentication, SSE and DLP; place[19] M05/tok | VERIFIED 8 Nov 2026 |
| cs3 | csadd | You have three options: None API key: Configure API key authentication OAuth 2.0: Configure OAuth 2.0 authentication | M06.checks[2]; row[4] Copilot Studio authentication, SSE and DLP; place[22] M06/saas | VERIFIED 8 Nov 2026 |
| cs4 | csdlp | Blocking Power Platform connectors also blocks access to tools in connected MCP servers, which rely on Power Platform connectors for connectivity. | row[4] Copilot Studio authentication, SSE and DLP | VERIFIED 8 Nov 2026 |
| gsa1 | gsa | The MCP firewall is currently in preview. | M07.body[0]; row[6] Entra MCP firewall and logging (preview); place[28] M07/gw; callout[2] | VERIFIED 8 Nov 2026 |
| gsa2 | gsa | network-based, identity-centric security control that provides centralized visibility, policy enforcement, and runtime protection for MCP traffic between AI agents and remote MCP servers. | M07.body[0] | VERIFIED 8 Nov 2026 |
| gsa3 | gsa | Create allow-lists or deny-lists of MCP servers based on server URL patterns. | M07.body[0]; row[6] Entra MCP firewall and logging (preview); place[28] M07/gw | VERIFIED 8 Nov 2026 |
| gsa5 | gsa | Without TLS inspection, Global Secure Access can't parse or enforce MCP policy. | M07.body[0]; row[6] Entra MCP firewall and logging (preview); place[28] M07/gw | VERIFIED 8 Nov 2026 |
| gl1 | gsalog | MCP logging is currently in preview. | M08.body[1]; row[6] Entra MCP firewall and logging (preview); place[32] M08/gw; callout[2] | VERIFIED 8 Nov 2026 |
| gl2 | gsalog | MCP Logging helps you discover shadow MCP servers in your organization | M08.body[1]; row[6] Entra MCP firewall and logging (preview); place[32] M08/gw | VERIFIED 8 Nov 2026 |
| gl3 | gsalog | MCP Logging only captures traffic to remote MCP servers. Local MCP servers running on a device are not visible because their traffic doesn't have a network footprint that Global Secure Access can inspect. | M08.body[1]; M08.checks[1]; row[6] Entra MCP firewall and logging (preview); place[32] M08/gw | VERIFIED 8 Nov 2026 |
| ap1 | apim | You can secure either or both inbound access to the MCP server (from an MCP client to API Management) and outbound access (from API Management to the MCP server). | M06.body[0]; row[7] Azure API Management; place[23] M06/gw | VERIFIED 8 Nov 2026 |
| ap2 | apim | Use API Management's credential manager to securely inject OAuth 2.0 tokens for backend API requests that MCP server tools make. | M06.body[1]; row[7] Azure API Management; place[20] M06/tok | VERIFIED 8 Nov 2026 |
| ap3 | apim | Request headers are automatically forwarded (with certain exclusions) to MCP tool invocations. | M06.body[1]; M06.checks[1]; row[7] Azure API Management; place[20] M06/tok | VERIFIED 8 Nov 2026 |
| ap4 | apim | use the validate-azure-ad-token policy to validate Microsoft Entra ID tokens | M06.body[0]; M06.checks[0]; row[7] Azure API Management; place[23] M06/gw | VERIFIED 8 Nov 2026 |
| gw1 | a365gw | Connect Azure AI Gateway or a LiteLLM gateway to Microsoft Agent 365 to discover and govern the Model Context Protocol (MCP) servers registered with the gateway. | row[8] Agent 365 gateway and BYO (preview) | VERIFIED 8 Nov 2026 |
| gw2 | a365gw | You can block or allow an MCP server to manage its availability. | M01.checks[2]; row[8] Agent 365 gateway and BYO (preview); place[4] M01/gw | VERIFIED 8 Nov 2026 |
| gw3 | a365gw | Important This feature is in preview. | M01.checks[2]; row[8] Agent 365 gateway and BYO (preview); place[4] M01/gw; callout[2] | VERIFIED 8 Nov 2026 |
| by1 | a365byo | Important This feature is in preview. | M08.body[0]; place[31] M08/tele; callout[2] | VERIFIED 8 Nov 2026 |
| by2 | a365byo | The security team monitors activity and tool invocations through Microsoft Defender advanced hunting | M08.body[0]; row[8] Agent 365 gateway and BYO (preview); place[31] M08/tele | VERIFIED 8 Nov 2026 |
| by3 | a365byo | Supported client surfaces during preview are Copilot Studio, Visual Studio Code, Claude Code, and GitHub Copilot CLI. | row[8] Agent 365 gateway and BYO (preview) | VERIFIED 8 Nov 2026 |
| az1 | azmcp | Don't use a local Azure MCP Server to handle production data or production credentials. | M02.body[0]; row[9] Azure MCP Server security and CVEs; place[6] M02/local | VERIFIED 8 Nov 2026 |
| az2 | azmcp | Because it can act with your Azure identity, review what your signed-in account can access before you connect an agent to Azure resources | M03.body[1]; place[12] M03/files | VERIFIED 8 Nov 2026 |
| az3 | azmcp | Review and pin known-good tool schemas and descriptions, and require re-approval before updated tool metadata takes effect | M02.body[1]; M02.checks[1] | VERIFIED 8 Nov 2026 |
| az4 | azmcp | Prefer the official Microsoft-maintained Azure MCP Server. | M02.body[0]; row[9] Azure MCP Server security and CVEs; place[8] M02/policy | VERIFIED 8 Nov 2026 |
| c1a | cve26118 | Server-side request forgery (ssrf) in Azure MCP Server allows an authorized attacker to elevate privileges over a network. | M07.body[1]; M07.checks[1]; row[9] Azure MCP Server security and CVEs; place[27] M07/mcpr | VERIFIED 8 Nov 2026 |
| c1b | cve26118 | "baseScore":8.8 | M07.body[1]; place[27] M07/mcpr | VERIFIED 8 Nov 2026 |
| c2a | cve32211 | Missing authentication for critical function in Azure MCP Server allows an unauthorized attacker to disclose information over a network. | M06.body[2]; row[9] Azure MCP Server security and CVEs; place[21] M06/mcpr | VERIFIED 8 Nov 2026 |
| c2b | cve32211 | "baseScore":9.1 | M06.body[2]; place[21] M06/mcpr | VERIFIED 8 Nov 2026 |
| c2c | cve32211 | "product":"Azure Web Apps" | M06.body[2]; place[21] M06/mcpr | VERIFIED 8 Nov 2026 |
| c2d | cve32211 | "tags":["exclusively-hosted-service"] | M06.body[2]; place[21] M06/mcpr | VERIFIED 8 Nov 2026 |
| inv1 | inv | The vulnerability allows an attacker to hijack a user's agent via a malicious GitHub Issue, and coerce it into leaking data from private repositories. | M04.body[0]; M04.checks[0]; place[14] M04/content | VERIFIED 8 Nov 2026 |
| vc1 | vscm | Restricted mode prevents these servers from starting. | M03.checks[0] | VERIFIED 8 Nov 2026 |
| vc2 | vscm | In a trusted workspace, they can start without a separate MCP trust prompt, including after configuration changes. | M03.body[0]; M05.body[1]; M05.checks[0]; place[2] M01/agent; place[10] M03/cfgf; place[17] M05/cfgf | VERIFIED 8 Nov 2026 |
| vc3 | vscm | newAndOutdated (default): Start servers that have never run or whose configuration has changed. | M05.body[1]; place[18] M05/agent | VERIFIED 8 Nov 2026 |
| vc4 | vscm | On macOS and Linux, per-server sandboxing restricts file system and network access for stdio MCP servers. | M03.body[1]; place[11] M03/local | VERIFIED 8 Nov 2026 |
| vc5 | vscm | This mechanism isn't available on Windows. | M03.body[1]; place[11] M03/local | VERIFIED 8 Nov 2026 |
| vp1 | vspol | Servers matching any entry are blocked from being installed or run, even if they also match the allow list; deny rules always take precedence. | M01.how[2] | VERIFIED 8 Nov 2026 |
| vp2 | vspol | Tools set to 'false' will always present a confirmation and will never offer the option to auto-approve. | place[29] M09/policy | VERIFIED 10 Nov 2026 |
| vt1 | vstel | Copilot Chat in VS Code can export traces, metrics, and events via OpenTelemetry (OTel) to give you real-time visibility into agent interactions, LLM calls, tool execution, and token usage. | M08.body[0]; M08.checks[0]; place[31] M08/tele | VERIFIED 8 Nov 2026 |
| sp1 | sphttp | Servers MUST validate the Origin header on all incoming connections to prevent DNS rebinding attacks. | M07.checks[0]; place[24] M07/lhttp | VERIFIED 8 Nov 2026 |
| sp2 | sphttp | servers SHOULD bind only to localhost (127.0.0.1) rather than all network interfaces (0.0.0.0). | M07.checks[0]; place[24] M07/lhttp | VERIFIED 8 Nov 2026 |
| sp3 | spsec | URLs targeting http://169.254.169.254/ (AWS/GCP/Azure metadata service) can exfiltrate cloud credentials and instance information | place[25] M07/egress | VERIFIED 8 Nov 2026 |
| sp4 | spsec | OAuth authorization URLs provided by malicious MCP servers can exploit client-side URL handling vulnerabilities, leading to Cross-Site Scripting (XSS) attacks and Remote Code Execution (RCE). | place[26] M07/agent | VERIFIED 8 Nov 2026 |
| localsandbox | spsec | Execute MCP server commands in a sandboxed environment with minimal default privileges | place[12] M03/policy | VERIFIED 9 Nov 2026 |
| sp5 | spver | The current protocol version is 2026-07-28 | callout[1] | VERIFIED 8 Nov 2026 |
| ow1 | owasp | MCP04:2025 - Software Supply Chain Attacks & Dependency Tampering | place[5] M02/pkg | VERIFIED 8 Nov 2026 |
| ow2 | owasp | MCP03:2025 - Tool Poisoning | place[7] M02/agent | VERIFIED 8 Nov 2026 |
| ow3 | owasp | MCP10:2025 - Context Injection & Over-Sharing | place[29] M08/agent | VERIFIED 8 Nov 2026 |
| ow5 | owasp | We are here right now - release a "beta" version of MCP Top 10. | callout[0] | VERIFIED 8 Nov 2026 |
| mi1 | mit | MCP Token Theft in Claude Code: A Man-in-the-Middle Attack Chain | M05.body[0]; callout[4] | VERIFIED 8 Nov 2026 |

### Statements tagged as inference

Statements without a quote carry an [inference] or [unverified] tag on the page. The check script fails if an untagged sentence has no quote id. No such statement is a source claim.

### Reviewed presentation text (Microsoft view)

Text with no evidence list holds requirements, labels and code tokens only. Each row is `verdict`, a tab, then the exact text. The script fails when a text is missing from this list, when a text here no longer appears on the page, or when fact-style wording appears. A pass proves a verdict was recorded for the exact wording, not that the verdict is right.

<!-- Begin reviewed presentation text (Microsoft view) -->
```text
label	MCP Risk Map
label	Risk map · MCP servers and AI agents · Microsoft ecosystem
requirement	Where the main risks sit when developers connect AI agents to MCP servers through Microsoft products: VS Code, Visual Studio, GitHub Copilot, Copilot Studio, Windows, Azure and Microsoft Entra. Third-party servers used inside these clients still apply. The detail is kept low on purpose. Exceptions exist.
label	Vendor sources Microsoft Learn, VS Code, GitHub Docs, MCP specification, CVE records, Invariant Labs
label	Facts checked 9 Nov 2026
label	View
label	General
label	Microsoft ecosystem
label	Current as of 9 November 2026
requirement	None of them needs a preview feature.
label	Other Microsoft surfaces
label	What Microsoft and GitHub documentation or CVE records say about MCP outside VS Code, and which risk each row touches. Each row has the exact quote and a link to the source. Earlier rows were checked on 9 November 2026; new governance claims were checked on 10 November. Nothing here was tested.
label	Gallery, GitHub, registries
label	VS Code, Visual Studio, Copilot
code token	mcp.json, .mcp.json
label	Code, .env, Azure login
label	SaaS and Azure APIs
label	Device and org policy
label	Intune, GitHub managed settings
label	OpenTelemetry, Defender, SIEM
label	MCP gateway or firewall
label	APIM, Agent 365, Entra GSA
label	MCP gateway
requirement	Set an enterprise allowlist and denylist in GitHub managed-settings.json, and review which repository custom agent profiles exist
label	Moderate
requirement	Pin package versions in each server command
label	Low
requirement	Review tool changes before approving them again
requirement	Open unfamiliar repositories in Restricted mode and keep Workspace Trust on
requirement	Use separate sessions for untrusted reading, without tools that can write or send
requirement	Review changes to mcp.json and .mcp.json like code changes
requirement	Validate caller identity and enforce authorization for each server operation
requirement	Review the Azure identity and reduce unnecessary access
requirement	Review Visual Studio auto-confirm grants for tools that write or send
requirement	Bind local HTTP servers to 127.0.0.1 and check the Origin header. Allow remote servers only from the approved list in M01
requirement	Export OpenTelemetry from VS Code to your existing log system, and keep a list of approved servers
label	MCP on Windows: Windows On-device Agent Registry
label	Microsoft Learn. Prerelease. Separate environment, Intune control, logging.
label	Visual Studio: use MCP servers
label	Microsoft Learn. Server trust (18.7 or later), tool confirmation, tool-list reset, allow list policies.
label	GitHub: configure an enterprise MCP allowlist
label	GitHub Docs. managed-settings.json, allowedMcpServers, deniedMcpServers.
label	GitHub: configure an MCP registry
label	GitHub Docs. Public preview; not the recommended method.
label	GitHub: MCP private registry enforcement
label	GitHub Docs. Name and ID matching; bypass by editing configuration files.
label	Copilot Studio: add an existing MCP server
label	Microsoft Learn. Authentication options, API key in header or query, SSE.
label	Copilot Studio: data loss prevention
label	Microsoft Learn. Connector blocking and MCP tools.
label	Entra Global Secure Access: MCP firewall
label	Microsoft Learn. Preview. Server URL patterns, TLS inspection.
label	Entra Global Secure Access: MCP logging
label	Microsoft Learn. Preview. Shadow MCP discovery; remote servers only.
label	Azure API Management: secure MCP servers
label	Microsoft Learn. Inbound and outbound access, credential manager, header forwarding.
label	Agent 365: tools gateway
label	Microsoft Learn. Preview. Block or allow a server, LiteLLM gateway.
label	Agent 365: bring your own MCP server
label	Microsoft Learn. Preview. Defender advanced hunting; supported client surfaces.
label	Azure MCP Server: security
label	Microsoft Learn. Production data, Azure identity, change control, official server.
label	CVE-2026-26118 (Azure MCP Server)
label	CVE record published by Microsoft. A vendor advisory, not evidence here of a victim incident.
label	CVE-2026-32211 (Azure MCP Server)
label	Invariant Labs: GitHub MCP exploited
label	Invariant Labs. Third-party research, not a Microsoft or GitHub advisory.
label	VS Code: manage MCP servers
label	Microsoft. Workspace Trust, autostart, sandbox.
label	Centrally manage VS Code settings with policies
label	Microsoft. ChatAllowedMcpServers, ChatDeniedMcpServers.
label	VS Code: enterprise telemetry
label	Microsoft. OpenTelemetry export from Copilot Chat.
label	MCP specification: transports (Streamable HTTP)
label	Model Context Protocol, version 2026-07-28. Origin validation, localhost binding.
label	MCP security best practices (2026-07-28)
label	Model Context Protocol. SSRF, authorization URL validation.
label	MCP versioning
label	Model Context Protocol. Current protocol version.
label	OWASP MCP Top 10
label	OWASP. Beta (phase 3). MCP01 to MCP10.
label	Mitiga: MCP token theft in Claude Code
label	Mitiga. Third-party research on Claude Code, not on a Microsoft product.
label	Claude Code: managed MCP
label	Primary documentation, checked 9 November 2026.
label	Codex managed configuration
label	VS Code: MCP configuration reference
label	Also check
label	Check
label	CoSAI
label	Risk list
label	Not assessed
label	Not assessed for the Microsoft ecosystem
label	CoSAI: Model Context Protocol (MCP) Security
label	Coalition for Secure AI, Workstream 4. Marked Draft. Threat names, numbers and quoted sentences.
label	MCP specification: tools
label	Model Context Protocol, version 2026-07-28. Human in the loop and rate limiting.
label	All
```
<!-- End reviewed presentation text (Microsoft view) -->
