# MCP governance STRIDE and DREAD model: fact check

Checked 2026-11-12. This review supersedes the earlier same-day verification narrative.

## Verdict and scope

The original model was a useful scenario inventory, but was not correct enough to call a verified deployment threat model. This review checked all 74 scenarios against STRIDE definitions, their stated preconditions, the quoted architecture sources and the public records. It corrected 54 scenario/basis entries while preserving every threat and element ID.

All scenarios remain `[inference]`: interpretation by AI, not findings reproduced against a tenant. The 20 unchanged scenarios were retained as plausible conditional scenarios, not confirmed vulnerabilities. Related rows can represent different attack stages or STRIDE consequences; counts and scores must not be added as independent risks.

| Check | Result | Limit |
|---|---|---|
| Architecture source quotes | 208/208 present in freshly fetched sources, including V203-V208 | Quote presence is not proof that an inference follows; surrounding passages relevant to the corrections were also inspected |
| Source fetching | All 62 distinct source URLs fetched successfully on 2026-11-12 | Redirects are followed; no assertion about an undocumented deployment or release schedule |
| CVE records | All 36 originally cited distinct CVE Program CNA records fetched and descriptions read | Product/version applicability to this design is not established |
| Incident/research records | Original incident, researcher and malware-advisory records read; follow-up search assessed WhatsApp, Supabase, Smithery, GlassWorm, npm malware and MCP reconnaissance | Asana is secondary reporting; researcher demonstrations and published malware are not proof of victim compromise or attacks against this deployment |
| Exploitation | Official CISA KEV data, catalog released 2026-11-10, confirms CVE-2026-59822 and CVE-2026-42271; Postmark confirms the malicious package incident | Only the first CVE matches a retained row. KEV absence is not evidence of no exploitation |
| STRIDE coverage | 71 selected cells: 4 external entities x 2 + 6 processes x 6 + 3 stores x 4 + 5 flows x 3; 74 scenario rows | A populated matrix does not establish completeness. Store repudiation is relevant to retained approval/change/audit history, not every store universally |
| DREAD | 8 High, 60 Medium, 6 Low; arithmetic checked, automatic evidence lifts removed | Factor values are carried-forward, uncalibrated AI estimates; no per-factor measurement or deployment-specific residual-risk calculation |
| Retained evidence | 14 threat IDs: 2 exploited-class, 12 disclosed-class; 60 rows have no attached matching public record | 38 record-to-row associations, 37 distinct records (29 CVEs and 8 non-CVE incident, research, news or malware records) |
| SC-500 map | All 32 skill strings found in the freshly fetched official study guide | An exam skill link is not a sufficient mitigation or implementation test |

## Primary sources and interpretation

- [Microsoft SDL secure design guidance](https://www.microsoft.com/en-us/securityengineering/sdl/practices/secure-by-design): used for STRIDE meanings, actor/precondition/action/consequence structure, trust boundaries, assumptions and mitigation validation. Filling cells is not a replacement for attacker-oriented analysis.
- [Microsoft STRIDE-per-element example](https://learn.microsoft.com/en-us/archive/msdn-magazine/2006/november/uncover-security-design-flaws-using-the-stride-approach): external entities S/R, processes all six, flows T/I/D; store repudiation requires an evidentiary purpose. DS1 approval history, DS2 policy-change history and DS3 audit evidence justify the selected R cells as interpretation by AI.
- [MCP security guidance, revision 2026-07-28](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices): identifies authorization, confused-deputy, token, SSRF, local execution and state-handle concerns. This is a comparison checklist, not proof those attacks are present in the design. Legacy session handling requires a protocol-version-specific review.
- [AI Gateway tool threat protection](https://learn.microsoft.com/en-us/azure/ai-gateway/policy-tool-threat): Audit is nonblocking and may fail open; Block is documented as fail-closed. Post-invocation denial cannot reverse completed tool side effects. This is the AI Gateway preview feature, not an assertion about every APIM gateway.
- [Defender runtime protection](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-real-time-protection): default rules record events, including identity/tool context. The Entra agent-ID statement applies to the agent-selection list; it does not establish that every agent without an ID can impersonate a protected agent or is universally unmonitored.
- [Copilot Studio external provider](https://learn.microsoft.com/en-us/microsoft-copilot-studio/external-security-provider): data sharing and the default one-second allow-on-timeout behavior support I7/D6 conditions. Legitimate inspection itself is not an unauthorized disclosure.
- [Functions networking](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options): lack of private endpoints on classic Consumption does not remove inbound restrictions. Public reachability does not itself bypass authentication or correctly validated HTTPS.
- [Foundry MCP configuration](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol): an empty `allowed_tools` list allows all exposed tools. E4 also requires server-side permission to perform the unintended operation.
- [Foundry Purview auditing](https://learn.microsoft.com/en-us/purview/ai-azure-foundry): describes prompt/response auditing. Silence about MCP tool calls cannot establish that none are audited. R7 is now a conditional correlation gap.
- [Enterprise managed settings](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings): wildcard and exact command matching, profile exclusions and first-party exceptions are distinct controls/limits. An exempt server is not itself a tampering exploit.
- [SC-500 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-500): wording of the exported skills checked, not effectiveness as controls.

## Additional non-CVE reporting checked (2026-11-12)

- [BleepingComputer on Asana's MCP data exposure](https://www.bleepingcomputer.com/news/security/asana-warns-mcp-ai-feature-exposed-customer-data-to-other-orgs/): reports Asana's user notices and a company spokesperson's estimate of about 1,000 affected customers; describes a cross-organization logic flaw, not an external hack. This supports I14 at disclosed/report level. It is secondary reporting; no Asana postmortem was obtained in this review. The report does not establish this architecture is affected.
- [IONIX's exposed MCP server investigation](https://www.ionix.io/blog/exposed-ai-agents-in-the-wild-public-mcp-server-security-exposed/): the researchers describe several publicly exposed servers and low-impact testing of one unauthenticated endpoint that allowed tool calls and reads of non-sensitive host files. This supports I5's unauthenticated read-exposure class as researcher-reported evidence. It is a different, anonymized server; this is not proof of attacks in the proposed deployment.
- [Pillar Security's Deadbugz report](https://www.pillar.security/blog/deadbugz-currently-active-mcp-supply-chain-campaign): researchers report observing a live server return credential-seeking metadata after three tool calls and matching it to public source. They reviewed 23 campaign pull requests and say none was merged at review time. This supports T14 as a researcher-observed malicious metadata/prompt-injection campaign, but does not establish an affected victim or successful credential theft.
- [Microsoft Incident Response's tool-poisoning analysis](https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/): says techniques first disclosed in 2025 were observed against enterprise agents in 2026, then presents an invoice-workflow attack chain. Microsoft does not identify an affected organization or say the displayed workflow is a specific case. Used as threat-intelligence context for T14, not counted as an additional independently verified incident.
- [NSA's MCP security design guidance](https://media.defense.gov/2026/Jun/02/2003943289/-1/-1/0/CSI_MCP_SECURITY.pdf): official advisory covering authentication, authorization, serialization, trust boundaries and agent misuse. Guidance establishes an authoritative threat taxonomy, not that a particular exploit or incident occurred.

These examples show why evidence should retain its source type: confirmed incident, public exploit/CVE, researcher reproduction, observed campaign, news reporting and official threat guidance do not establish the same thing. The model labels these cross-product matches `disclosed`; it does not claim the proposed design has been attacked.

### Follow-up search (2026-11-12)

The row mappings below are interpretation by AI. Each record has one authoritative scenario home; related attack stages are described here without counting the same record repeatedly.

| Record and date | Verified evidence and limit | Register treatment |
|---|---|---|
| [Invariant WhatsApp experiments, 2025-04-07](https://invariantlabs.ai/blog/whatsapp-mcp-exploited) | Researchers demonstrated a sleeper server's metadata steering a trusted WhatsApp tool to send chat history to another recipient. A second experiment injected a WhatsApp message and leaked contacts without a malicious server. Controlled demonstrations, not reported victim incidents; the confirmation UI still required user approval and obscured payload details. | Added to I3: exfiltration in an MCP tool argument. |
| [General Analysis Supabase/Cursor demonstration, 2025-07-08](https://generalanalysis.com/blog/supabase-mcp-blog) | A support ticket caused privileged MCP SQL calls to read dummy integration tokens and write them into an attacker-visible reply. Historical test used `service_role`; the researchers explicitly have not rerun it against the current server. [Supabase's response, 2025-09-16](https://supabase.com/blog/defense-in-depth-mcp), acknowledges the pattern and says no customer had reported a leak via MCP at that date. RLS was not bypassed by an exploit: the configured role already bypassed it. | Added to T14: untrusted tool results become instructions. |
| [Malware advisory GHSA-p6wc-j7x7-ff3v, 2026-07-27](https://github.com/advisories/GHSA-p6wc-j7x7-ff3v) | Lists malicious `@antv/mcp-server-antv` versions 0.2.8 and 0.3.8 with a credential-stealing preinstall hook following publishing-account compromise. Checked the linked OpenSSF record and original SafeDep/Socket research. Evidence of published malicious releases, not a quantified count of victims; advisory remains active. | Added to T3 at disclosed level; its strongest level remains exploited because of the existing Postmark record. |
| [GitGuardian Smithery hosting research, 2025-10-22](https://blog.gitguardian.com/breaking-mcp-server-hosting/) | Build-context path traversal exposed a Fly.io credential. Researchers demonstrated privileged container command execution and capture of an API key in inbound server traffic. They report a patch after disclosure and no evidence of malicious exploitation. Potential access to thousands of hosted apps is a blast-radius claim, not a victim count. | Context only. The shared hosting/build control plane is outside the current aggregated DFD. I1 is specifically pipeline-log exposure; I5 is backend read authorization; neither describes this chain accurately. |
| [Koi/Palo Alto Networks GlassWorm report, 2026-03-16](https://www.paloaltonetworks.com/blog/security-operations/glassworm-wave-5-malicious-mcp-servers/) | Researchers analyzed a trojanized `@iflow-mcp/watercrawl-watercrawl-mcp` package containing an invisible-Unicode payload. The report says all five releases were malicious from their first release. It does not establish this MCP package's victim count; victims elsewhere in the wider campaign must not be attributed to it. | Context only. Initial installation of a lookalike package differs from T3's malicious update to a previously trusted package. This is an additional onboarding scenario to model if the DFD is expanded. |
| [Pillar Bizarre Bazaar / separate MCP reconnaissance report, 2026-01-28](https://www.pillar.security/blog/operation-bizarre-bazaar-first-attributed-llmjacking-campaign-with-commercial-marketplace-monetization) | Honeypot observations show active targeting of AI infrastructure. The MCP-focused traffic is explicitly a separate reconnaissance campaign; LLM resale findings do not establish successful MCP compromise or lateral movement. | Context only; not evidence that S8, E6 or a denial-of-service scenario succeeded. |
| [GHSA-3x3c-57v3-ghqc](https://github.com/advisories/GHSA-3x3c-57v3-ghqc) | Advisory for `mcp-server-iehub-proxy` is marked withdrawn on 2026-08-04. No withdrawal rationale was obtained. | Excluded. The original allegation is not retained as confirmed malware evidence. |

No matching incident evidence for the remaining repudiation or denial-of-service scenarios was established by this search. This is a search limit, not evidence those scenarios cannot occur.

The original shared quote checker reads 202 module quotes and reports the interactive page's six additions as extras. That is a checker coverage mismatch, not six failed live quotes. `scripts/check-mcp-stride.py --quotes <fresh-cache>` checks all 208 source-table quotes without omitting those six.

## Row-by-row review (2026-11-12)

This table is the wording ledger. Each verdict concerns the exact scenario text and its primary STRIDE consequence. All scenarios and causal mappings are interpretation by AI. “Retained” means plausible subject to the listed conditions; “Corrected” identifies the change from the original model. Controls are related design links, not proven fixes.

| ID | Element | Reviewed scenario | Verdict and rationale |
|---|---|---|---|
| S1 | EE1 | A stolen developer sign-in token is used to call the gateway as that developer. | Retained. Stolen valid credential enables identity impersonation; token theft is assumed, not demonstrated. |
| R1 | EE1 | A developer denies adding an unapproved server; neither managed configuration history nor endpoint telemetry records who changed the user file. | Corrected. Insufficient attribution is conditional; local configuration does not prove no company telemetry exists. |
| S2 | EE2 | An attacker able to send through an allowed source impersonates a Copilot user when the gateway checks only the source IP and does not authenticate the user or tenant. | Corrected. Allowed-source access is an explicit precondition; no unsupported claim about shared tenant egress. |
| R2 | EE2 | A user denies authorizing a write action, and retained records cannot link the action to that user's one-time or saved tool approval. | Corrected 2026-11-13. V164 and V227 distinguish initial approval from conversation or persistent tool approval; correlation must retain approval scope. |
| S3 | EE3 | An attacker with a stolen approver or admin account approves a server in Git or in the admin center. | Retained. Stolen approval/admin identity enables fraudulent approval; identity compromise is assumed. |
| R3 | EE3 | An admin denies a manual connector-access change, and no retained admin audit record or change request can attribute it to the admin. | Corrected. No Git commit does not prove no admin audit; missing attribution must be demonstrated. |
| S4 | EE4 | An attacker controls a subdomain or path actually covered by a broad allowlist wildcard and presents its server as approved. | Corrected. A wildcard must actually match an endpoint the attacker controls; visual similarity is insufficient. |
| R4 | EE4 | An unapproved server operator denies receiving company data, and no company-side request record or independently retained receipt can establish the transfer. | Corrected. External ownership alone does not remove company-side logs; retained transfer evidence is the issue. |
| S5 | P1 | An attacker uses a leaked pipeline credential to write a list to a policy target. | Retained. Leaked deployment credential enables pipeline impersonation; target permissions remain a precondition. |
| T1 | P1 | An attacker gets unreviewed pipeline code merged or executed with deployment credentials and changes the approved-server policy at every target that identity can write. | Corrected. Unreviewed code must obtain deployment execution and credentials; merely proposing a PR is insufficient. |
| R5 | P1 | The pipeline writes to a target and keeps no run record that ties the change to a reviewed commit. | Retained. Missing commit-to-deployment traceability permits denial of a change; conditional scenario, not a platform logging claim. |
| I1 | P1 | Pipeline run logs print target credentials that are then read by someone without permission to use those credentials. | Corrected. Sensitive credential access, not disclosure of a potentially nonsecret list, is the pipeline-log scenario. |
| D1 | P1 | An attacker disables the sync runner or its credentials, preventing legitimate policy updates and onboarding until service is restored. | Corrected. Stale policy is not by itself DoS; disabling sync denies the policy-update service. |
| E1 | P1 | An attacker compromises a runner intended for one target and uses a shared deployment credential to administer other targets beyond that runner's intended scope. | Corrected. Compromise of a limited runner reaches broader deployment authority; credential reuse alone is only blast radius. |
| S6 | P2 | An attacker who can replace an executable or alter command resolution supplies a malicious binary under the exact command and arguments allowed for a local stdio server. | Corrected. Exact command/argument matching does not authenticate executable bytes; writable resolution is required. |
| T2 | P2 | An attacker with repository write access alters a trusted MCP configuration or custom agent profile to select a malicious server, and the client does not require a fresh review. | Corrected. Configuration modification is tampering; an exempt built-in server is not itself a tampering attack. |
| T3 | P2 | A package publisher adds a backdoor to a previously trusted local MCP package, and a user or an unpinned launcher installs the malicious version. | Corrected. Trusted third-party publisher adds a backdoor; neither automatic updating nor compromise of official Postmark is asserted. |
| R6 | P2 | A user denies launching a local MCP process, and retained endpoint, process and configuration records cannot attribute the launch to that user. | Corrected. Missing Defender runtime protection does not prove missing operating-system or other endpoint records. |
| I2 | P2 | With Allow all, a tool call sends files or secrets to an approved but over-permissioned server without a prompt. | Retained. Auto-approved sensitive tool calls require a malicious or misused server and available data permissions. |
| D2 | P2 | An attacker or mistaken administrator deploys an outbound block policy without required allow rules, denying legitimate network-dependent work on managed devices. | Corrected. Availability loss is legitimate traffic blocked by missing allow rules, not a claim that the device is physically broken. |
| E2 | P2 | Attacker-controlled repository content or MCP output bypasses the client's command approval checks, causing code to run with the user's privileges without the required approval. | Corrected. Code execution bypasses intended approval from untrusted content. Existing local administrator rights are not new privilege. |
| E3 | P2 | An untrusted server exploits a local MCP library's command parsing, or a malicious website reaches an unauthenticated local HTTP MCP endpoint through DNS rebinding, gaining tool access or code execution with the local process's privileges. | Corrected. Distinguishes command parsing from local HTTP/DNS-rebinding tool access; not every record proves operating-system RCE. |
| S7 | P3 | An attacker presents another cloud agent's identity to a tool that trusts a supplied agent name or identifier without validating its authenticated identity and tenant. | Corrected. Replaced a detection-scope gap with an actual false-identity scenario. V145 only describes the rule picker. |
| T4 | P3 | Hidden text in an external document steers the agent to call a tool the user did not intend. | Retained. Untrusted document instructions can alter agent intent; the Copilot CNA record supports AI injection generally, not an MCP-specific path. |
| R7 | P3 | An agent owner denies a tool action, and the deployment has not retained correlated agent, gateway and backend events that identify the initiating user and tool arguments. | Corrected. Source silence about tool audit is not proof of absence. Checks must join agent, gateway and backend events. |
| I3 | P3 | A compromised agent sends secrets out through an MCP tool argument. | Retained; 2026-11-13: basis now V142 (secret exfiltration blocked) with V125, since V125 alone covers only the unsafe-domain email case. Secret exfiltration is a plausible agent misuse; EchoLeak supports the broader injection/exposure class, not tool-argument routing. |
| D3 | P3 | An agent loop calls a tool without limit and uses up the gateway rate limit and the backend. | Retained. Repeated tool invocations can exhaust shared limits; the loop, quotas and isolation are deployment conditions. |
| E4 | P3 | A read-only agent is configured with an empty allowed_tools list by mistake; an attacker then induces a write call that the server permits under the connection's credentials. | Corrected. Empty allowed_tools is documented to allow all; unauthorized write also requires usable server permissions and a read-only intent. |
| S8 | P4 | A gateway with missing or defective authentication accepts an unauthenticated caller as trusted, for example by relying only on source IP or accepting a fabricated bearer token. | Corrected. Missing or defective authentication now covers the attached auth-bypass records; source IP alone was too narrow. |
| T5 | P4 | An attacker with gateway policy write access, including a compromised service granted the Agent 365 policy role, removes authentication or tool restrictions from an API policy. | Corrected. Compromised write authority performs an unauthorized change; the legitimate consent grant is not itself an attack. |
| R8 | P4 | Gateway logs miss fields or expire early, so a tool call cannot be shown later. | Retained. Insufficient fields/retention undermine attribution; implementation-specific retention must be checked. |
| I4 | P4 | A gateway caches a sensitive tool result without binding the cache key to the authorized caller and tenant, and returns it to another caller. | Corrected. Cache isolation failure is conditional on a configured cache. I10 owns log disclosure and E5 owns shared-identity authorization. |
| D4 | P4 | An attacker exhausts gateway capacity or request quotas, denying legitimate calls when clients depend on that deployment and no adequate isolation or failover is configured. | Corrected. Capacity, quota isolation and failover are the availability scenario; East US 2 and Sweden Central are not asserted to be an Azure region pair. |
| E5 | P4 | A gateway fails to enforce caller-specific tool authorization, allowing a low-privilege caller to invoke privileged operations through a more powerful shared backend connection. | Corrected. Shared backend identity is legitimate behavior; missing caller-specific authorization creates the privilege gain. |
| S9 | P5 | A backend with missing authentication or incomplete token validation accepts an unauthenticated request or a token issued for another resource as an approved caller. | Corrected. Missing authentication and wrong-audience validation are distinguished; both require server defects. |
| T6 | P5 | An attacker supplies a tool argument that escapes the intended command, query or filesystem scope and causes an unauthorized data or file modification under the server's privileges. | Corrected. Defines the unauthorized integrity effect and server input-validation gap. Read-only records moved to I5. |
| R9 | P5 | A caller denies a backend action; the server logs only a shared gateway identity and retains no correlation identifier that joins it to an authenticated upstream caller record. | Corrected. A shared backend identity only prevents attribution when upstream correlation is also unavailable. |
| I5 | P5 | An attacker reads backend data because authentication is disabled or a read tool fails to enforce object, path, query or tenant authorization; public reachability makes the vulnerable endpoint accessible but does not itself grant access. | Corrected. Public reachability alone does not grant access. Authentication and object/path/query/tenant authorization failures are explicit. |
| I6 | P5 | The server joins a caller-supplied path or address to its cloud API base address, so its own cloud token goes to a host the attacker picks. | Retained. Lokka explicitly confirms URL-authority confusion leaking a server token. Client metadata confusion was removed. |
| D5 | P5 | An attacker floods a publicly reachable backend that lacks effective inbound restrictions and resource limits, denying legitimate tool calls. | Corrected. Classic Consumption lacks private endpoints but supports inbound restrictions; a public unprotected backend is an explicit condition. |
| E6 | P5 | An attacker exploits an unchecked outbound URL or another server-side authorization flaw to reach internal services or cloud credentials with the server's privileges beyond the caller's permitted tool scope. | Corrected. Added the actual SSRF/authorization attack needed to use server privileges; overprivilege alone is a precondition. |
| S10 | P6 | The external threat detection service for Copilot Studio is replaced by one that always answers allow. | Retained. Provider impersonation requires control of endpoint configuration or failure of provider identity validation. |
| T7 | P6 | An attacker rewrites or splits the content that a detection check inspects so an unsafe action receives an allow verdict; the unsafe email scenario is checked only at the tool request. | Reworded 2026-11-12. The old text ("hides intent so the check misses it") described evasion without naming what is altered. The row now states the Tampering consequence: manipulated input produces a wrong verdict. Still hypothetical; V144 establishes only the unsafe-email intervention point. |
| R10 | P6 | An operator denies disabling a blocking rule, and retained administration records cannot establish who changed the protection configuration. | Corrected. Unread recorded events do not remove evidence; replaced with untraceable protection-rule administration. |
| I7 | P6 | A compromised or excessively privileged external threat detection provider exposes sensitive agent data received for inspection to an unauthorized party. | Corrected. Intended provider inspection is not a vulnerability; compromise or unauthorized onward disclosure is required. |
| D6 | P6 | An attacker overloads the Copilot Studio detection provider so it cannot return verdicts in time; under the documented default, a response taking more than one second permits the tool to run. | Corrected. DoS is against the detection service; default timeout permitting execution is its secondary security consequence. |
| E7 | P6 | An attacker induces a privileged tool action while the deployment mistakenly relies on Audit mode or only a post-invocation check to prevent it; required authorization or pre-invocation enforcement is missing. | Corrected. Audit is nonblocking, Block is fail-closed, and post-invocation denial cannot reverse side effects; privilege gain needs missing enforcement. |
| T8 | DS1 | An attacker with repository write access bypasses required review through a direct push or unreviewed merge and changes the approved list. | Corrected. Repository write access and bypass of required review are explicit. |
| R11 | DS1 | An attacker rewrites approval history and denies proposing a server; no independent pull-request review or authenticated approval record survives to attribute the proposal. | Corrected. Squash merging and unsigned commits do not inherently erase identity; surviving review/audit records matter. |
| I8 | DS1 | A repository containing sensitive internal server addresses or owner details is readable by people without a business need for that inventory. | Corrected. Inventory must contain sensitive information and be exposed beyond its intended audience. |
| D7 | DS1 | The inventory repository is deleted or unavailable, delaying reviewed policy updates and automated synchronization; emergency manual blocks remain possible. | Corrected 2026-11-13. Repository availability does not prevent emergency manual enforcement. |
| T9 | DS2 | An attacker or administrator bypasses required review with a manual policy-target edit, allowing servers that the approved Git list excludes. | Corrected. Unreviewed target modification changes permitted servers; manual administration is not automatically malicious. |
| R12 | DS2 | An operator denies a manual target-policy change, and retained target history cannot link the write to an authenticated operator or a reviewed change request. | Corrected. A manual change must lack attributable target history, not merely a Git reference. |
| I9 | DS2 | A policy target grants configuration read access to an unauthorized principal, exposing sensitive server inventory or connection details. | Corrected. Configuration read access must be unauthorized and expose sensitive information. |
| D8 | DS2 | A wrong switch, such as turning off every MCP server in Copilot policy, stops all users at once. | Retained. A mistaken or malicious global disable can deny legitimate tool access; actual policy scope needs testing. |
| T10 | DS3 | An attacker with log deletion, purge or ingestion-control privileges removes audit evidence or injects forged entries; ordinary log read access is insufficient. | Corrected. Read access is insufficient for purge, deletion or forged ingestion; necessary permissions are explicit. |
| R13 | DS3 | A caller denies a tool action and the audit store lacks authenticated caller, tenant or correlation fields needed to join the agent, gateway and backend records. | Corrected. Logs must retain authenticated identity and correlation; cloud agents do not use endpoint rules. |
| I10 | DS3 | Logs hold tool arguments and results with personal or secret data, readable by a wide group. | Retained. Log access by a group not entitled to sensitive payloads is disclosure; actual collection and permissions need review. |
| D9 | DS3 | An attacker disables ingestion or reduces retention below the required investigation period, making audit records unavailable when investigators need them. | Corrected. Retention must fall below the required investigation period or ingestion be disabled; routine expiry alone is not an attack. |
| T11 | F1 | An attacker changes a policy payload at a compromised intermediary or across a connection without effective transport integrity, and the target applies the altered policy. | Corrected. Requires compromised intermediary or ineffective transport integrity; not an assumed TLS break. |
| I11 | F1 | An attacker reads deployment credentials or sensitive policy data in transit because TLS is absent, certificate validation is disabled or a trusted TLS intermediary is compromised. | Corrected. Transit disclosure is separate from I1 run-log disclosure; ineffective TLS or compromised TLS termination is required. |
| D10 | F1 | Policy delivery is interrupted or an API request is rejected, preventing an approved update from reaching a target while no working retry or manual recovery path exists. | Corrected. Unsupported automation is an unresolved implementation question, not proof an API fails. Interrupted/rejected delivery denies updates. |
| T12 | F2 | An attacker at a compromised intermediary or a connection without effective TLS integrity changes the requested tool or arguments before the gateway authenticates and authorizes the request. | Corrected. Requires compromised intermediary or ineffective transport integrity; authentication alone does not validate intent. |
| I12 | F2 | A bearer token or sensitive tool argument is exposed to an untrusted proxy, a plaintext connection or a shared URL carrying credentials, allowing an attacker to read or reuse it. | Corrected. Ordinary bearer authentication does not imply disclosure; an untrusted proxy, plaintext or credential-bearing URL is required. |
| D11 | F2 | Microsoft 365 Copilot egress addresses change and the operator misses the announced update, so a stale inbound allowlist rejects legitimate calls. | Corrected. Missing an announced egress-list change is the condition; a change does not necessarily cause an outage. |
| T13 | F3 | An attacker modifies backend requests across a link with missing TLS integrity, disabled certificate validation or a compromised TLS terminator, causing unauthorized changes. | Corrected. Public routing does not defeat TLS; ineffective TLS or a compromised terminator is required. |
| I13 | F3 | An attacker reads backend request data on an unencrypted link or at a compromised TLS terminator; use of a public route alone does not reveal TLS-protected payloads. | Corrected. Public routing alone does not expose TLS-protected payloads. |
| D12 | F3 | The private path to the backend fails, and every approved call fails with it. | Retained. Loss of a required backend network path denies calls; redundancy is unspecified. |
| T14 | F4 | A tool result carries instructions that the agent follows (indirect prompt injection). | Retained. Researcher demonstration directly supports indirect injection through GitHub MCP results; deployment applicability remains untested. |
| I14 | F4 | A response with data for one user is returned to another user's agent session. | Retained. Cross-user credential/cache or transport isolation failures are supported; session message injection is a different mechanism. |
| D13 | F4 | A very large or endless response fills the agent's context or the gateway buffer. | Retained. Unbounded response consumption is a plausible resource-exhaustion scenario; no product limit was measured. |
| T15 | F5 | A client directly reaches a backend that lacks equivalent action authorization and performs an unauthorized write that gateway policy would have blocked. | Corrected. Direct reachability is not tampering; an unauthorized backend write and missing equivalent authorization are required. |
| I15 | F5 | A compromised client or cloud agent sends company data directly to an unapproved MCP server over an allowed or unrestricted egress path, bypassing gateway inspection and its audit trail. | Corrected. Unapproved-server egress bypasses gateway inspection; absence of all possible logs is not asserted. 2026-11-12: widened to cloud agents. V101 says the Foundry Network control does not affect prompt agents outside the Copilot harness, so their egress can be unrestricted. Controls now point at device and Foundry egress and the new gap instead of backend isolation, which does not stop traffic to another server. |
| D14 | F5 | A direct flood skips gateway rate limits. | Retained. Direct rate-limit bypass requires reachable backend and ineffective equivalent backend limits. |

## Retained public-record matches

All links below were checked through the CVE Program CNA record, incident/research notice, news article or malware advisory on 2026-11-12. A match is interpretation by AI at failure-class level. It does not assert an affected current Microsoft product or a reproduced exploit in this design. CNA records that state only generic AI injection or missing authentication support only that broad class.

| Record | Row(s) | Checked failure class |
|---|---|---|
| [Invariant original demo](https://invariantlabs.ai/blog/mcp-github-vulnerability) | T14 | Invariant Labs demo: GitHub MCP issue text steers the agent to leak private repo data (2025-05-26) |
| [Asana incident news report](https://www.bleepingcomputer.com/news/security/asana-warns-mcp-ai-feature-exposed-customer-data-to-other-orgs/) | I14 | Report of Asana notices and spokesperson confirmation of cross-organization exposure; secondary source |
| [IONIX exposed-server research](https://www.ionix.io/blog/exposed-ai-agents-in-the-wild-public-mcp-server-security-exposed/) | I5 | Researcher-reported unauthenticated exposed server, tool invocation and limited host file reads |
| [Pillar Security Deadbugz research](https://www.pillar.security/blog/deadbugz-currently-active-mcp-supply-chain-campaign) | T14 | Live server returned delayed hostile tool metadata; campaign pull requests were unmerged at review |
| [Invariant WhatsApp experiments](https://invariantlabs.ai/blog/whatsapp-mcp-exploited) | I3 | Research demonstrations exfiltrated chat history/contacts through a trusted messaging tool; no victim incident asserted |
| [General Analysis Supabase demonstration](https://generalanalysis.com/blog/supabase-mcp-blog) | T14 | Retrieved support-ticket instructions triggered privileged SQL reads and publication of dummy tokens; historical test |
| [GHSA-p6wc-j7x7-ff3v](https://github.com/advisories/GHSA-p6wc-j7x7-ff3v) | T3 | Publishing-account compromise introduced credential-stealing install hooks into an existing MCP package |
| [CVE-2025-32711](https://cveawg.mitre.org/api/cve/CVE-2025-32711) | T4, I3 | CVE-2025-32711 Microsoft 365 Copilot AI command injection causing information disclosure; the CNA summary does not specify MCP |
| [CVE-2025-49596](https://cveawg.mitre.org/api/cve/CVE-2025-49596) | E3 | CVE-2025-49596 MCP Inspector runs code for unauthenticated requests |
| [CVE-2025-53355](https://cveawg.mitre.org/api/cve/CVE-2025-53355) | T6 | CVE-2025-53355 mcp-server-kubernetes command injection |
| [CVE-2025-53967](https://cveawg.mitre.org/api/cve/CVE-2025-53967) | T6 | CVE-2025-53967 Framelink Figma MCP Server runs operating system commands from a crafted request |
| [CVE-2025-54136](https://cveawg.mitre.org/api/cve/CVE-2025-54136) | T2 | CVE-2025-54136 Cursor runs a changed MCP config that was already trusted |
| [CVE-2025-59163](https://cveawg.mitre.org/api/cve/CVE-2025-59163) | E3 | CVE-2025-59163 vet in MCP SSE mode exposes scan data through DNS rebinding |
| [CVE-2025-6514](https://cveawg.mitre.org/api/cve/CVE-2025-6514) | E3 | CVE-2025-6514 mcp-remote runs a command from a server's sign-in address |
| [CVE-2025-65513](https://cveawg.mitre.org/api/cve/CVE-2025-65513) | E6 | CVE-2025-65513 fetch-mcp SSRF bypasses the private IP check |
| [CVE-2025-66414](https://cveawg.mitre.org/api/cve/CVE-2025-66414) | E3 | CVE-2025-66414 MCP TypeScript SDK lacks DNS rebinding protection by default |
| [CVE-2025-66416](https://cveawg.mitre.org/api/cve/CVE-2025-66416) | E3 | CVE-2025-66416 MCP Python SDK leaves DNS rebinding protection off by default for local HTTP servers |
| [CVE-2025-66689](https://cveawg.mitre.org/api/cve/CVE-2025-66689) | I5 | CVE-2025-66689 Zen MCP Server path traversal reads arbitrary files |
| [CVE-2025-67366](https://cveawg.mitre.org/api/cve/CVE-2025-67366) | I5 | CVE-2025-67366 filesystem-mcp symlink handling allows reads outside the permitted directory |
| [CVE-2025-68143](https://cveawg.mitre.org/api/cve/CVE-2025-68143) | T6 | CVE-2025-68143 mcp-server-git accepted arbitrary filesystem paths |
| [CVE-2025-68144](https://cveawg.mitre.org/api/cve/CVE-2025-68144) | T6 | CVE-2025-68144 mcp-server-git passes user-controlled arguments to git without sanitizing, enabling arbitrary file overwrites |
| [CVE-2025-9611](https://cveawg.mitre.org/api/cve/CVE-2025-9611) | E3 | CVE-2025-9611 Microsoft Playwright MCP Server accepts web-page requests by DNS rebinding |
| [CVE-2026-114123](https://cveawg.mitre.org/api/cve/CVE-2026-114123) | I5 | CVE-2026-114123 D365 Finance and Operations MCP Server: an empty API key permits anonymous read tools if no separate access controls protect the deployment |
| [CVE-2026-116684](https://cveawg.mitre.org/api/cve/CVE-2026-116684) | S9 | CVE-2026-116684 MCP Python SDK bearer check accepts a token issued for a different resource server |
| [CVE-2026-25536](https://cveawg.mitre.org/api/cve/CVE-2026-25536) | I14 | CVE-2026-25536 MCP TypeScript SDK leaks response data across clients when one server and transport instance is reused |
| [CVE-2026-26118](https://cveawg.mitre.org/api/cve/CVE-2026-26118) | E6 | CVE-2026-26118 Azure MCP Server request forgery that raises privileges |
| [CVE-2026-27826](https://cveawg.mitre.org/api/cve/CVE-2026-27826) | E6 | CVE-2026-27826 mcp-atlassian lets an unauthenticated caller force outbound requests |
| [CVE-2026-29783](https://cveawg.mitre.org/api/cve/CVE-2026-29783) | E2 | CVE-2026-29783 GitHub Copilot CLI shell tool runs hidden commands after prompt injection |
| [CVE-2026-30615](https://cveawg.mitre.org/api/cve/CVE-2026-30615) | E2 | CVE-2026-30615 Windsurf prompt injection in HTML registers a malicious MCP STDIO server and runs commands |
| [CVE-2026-32211](https://cveawg.mitre.org/api/cve/CVE-2026-32211) | S9 | CVE-2026-32211 Azure MCP Server missing authentication |
| [CVE-2026-33032](https://cveawg.mitre.org/api/cve/CVE-2026-33032) | S8 | CVE-2026-33032 nginx-ui MCP message endpoint has no authentication, and its empty default IP allowlist allows every caller |
| [CVE-2026-33980](https://cveawg.mitre.org/api/cve/CVE-2026-33980) | I5 | CVE-2026-33980 Azure Data Explorer MCP Server interpolates table_name into KQL without validation, allowing queries beyond the intended tool input |
| [CVE-2026-48529](https://cveawg.mitre.org/api/cve/CVE-2026-48529) | I14 | CVE-2026-48529 GitHub MCP Server in HTTP lockdown mode runs later users' queries with the first user's credentials |
| [CVE-2026-58201](https://cveawg.mitre.org/api/cve/CVE-2026-58201) | I6 | CVE-2026-58201 Lokka (Microsoft 365 MCP server) sends an Azure Resource Manager bearer token to an unintended host through a crafted path |
| [CVE-2026-59822](https://cveawg.mitre.org/api/cve/CVE-2026-59822) | S8 | CVE-2026-59822 LiteLLM MCP endpoint accepts any bearer token (CISA KEV, added 2026-09-02) |
| [CVE-2026-8355](https://cveawg.mitre.org/api/cve/CVE-2026-8355) | E6 | CVE-2026-8355 IBM ContextForge MCP Gateway: a user-supplied token address makes the gateway send requests to internal hosts and cloud metadata |
| [Postmark incident](https://postmarkapp.com/blog/information-regarding-malicious-postmark-mcp-package) | T3 | Postmark confirms an unofficial impersonating package added an email-stealing backdoor in version 1.0.16 after building trust over 15 versions |

Official exploitation source: [CISA KEV data maintained by CISA](https://github.com/cisagov/kev-data/blob/main/known_exploited_vulnerabilities.json). CVE-2026-59822 was added 2026-09-02; CVE-2026-42271 was added 2026-06-08. Postmark's own notice confirms the unofficial package built trust over 15 versions before adding the email-stealing backdoor in 1.0.16. It does not establish automatic updating in this architecture.

## Removed or reassigned evidence

| Original association | Disposition and reason |
|---|---|
| [CVE-2026-42271](https://cveawg.mitre.org/api/cve/CVE-2026-42271) -> E5 | Removed. Real exploited LiteLLM stdio test-endpoint command execution, not evidence of shared backend connection authorization in APIM/AI Gateway. Do not transfer its exploitation status or scores to E5 |
| [CVE-2026-109492](https://cveawg.mitre.org/api/cve/CVE-2026-109492) -> E5 | Removed. Microsoft CNA says authorization bypass through a user-controlled key in `mcp-gateway`. It does not establish shared-connection behavior or identify this as APIM/AI Gateway |
| [CVE-2026-52869](https://cveawg.mitre.org/api/cve/CVE-2026-52869) -> I14 | Removed. CNA describes a bearer-authenticated client injecting JSON-RPC into a known existing session without principal binding. That is not the same as a demonstrated response leak to another agent session |
| [CVE-2026-63127](https://cveawg.mitre.org/api/cve/CVE-2026-63127) -> I6 | Removed. Client OAuth metadata/resource confusion sends a token to a malicious server; I6 describes a server leaking its own token through URL concatenation |
| [CVE-2025-53773](https://cveawg.mitre.org/api/cve/CVE-2025-53773) -> E2 | Removed. The checked Microsoft CNA summary establishes local code execution, not the command-approval bypass mechanism. Other checked records support E2 directly |
| [CVE-2026-30623](https://cveawg.mitre.org/api/cve/CVE-2026-30623), [CVE-2026-40933](https://cveawg.mitre.org/api/cve/CVE-2026-40933) -> E2 | Removed. LiteLLM/Flowise stdio configuration execution on the host is not the specific client approval-bypass scenario |
| [The Register Asana report](https://theregister.com/2025/06/18/asana_mcp_server_bug/) -> I14 | Original link removed; BleepingComputer's stronger report now documents Asana user notices and a spokesperson's affected-customer estimate. The evidence remains secondary reporting; no Asana postmortem was obtained |
| [GHSA-95pj-hrh5-27gq](https://api.github.com/advisories/GHSA-95pj-hrh5-27gq) -> T3 | Removed. Confirms malware in an npm package, but not introduction of a backdoor after earlier trusted versions, nor the old title's name-squatting claim |
| CVE-2026-33980, CVE-2025-66689, CVE-2025-67366 -> T6 | Moved to I5. Checked descriptions establish unrestricted KQL queries or unauthorized file reads, not the data/file modification consequence selected for T6 |

These are exclusions of particular evidence-to-scenario mappings, not declarations that the vulnerabilities are irrelevant to a fuller MCP threat model. A separate OAuth/client/session or hosted-stdio model should retain those concerns.

## Diagram, assumptions and open validation

The DFD is a logical design view. Its eight zones are not eight demonstrated trust boundaries in a deployment. In particular P6 aggregates in-platform Defender and an external provider, whose separate data/identity boundary is not drawn. Product variants (APIM, AI Gateway preview, Foundry, Copilot Studio and Microsoft 365) must be decomposed before claiming complete boundary coverage.

- F1 is policy delivery for targets that actually support automation. Microsoft 365 connector-access administration remains manual per V171; the grouped policy store must not imply a working Microsoft 365 policy API.
- F4 draws P5 -> P4 only. P4 -> P2/P3 responses, P3 bypass routes, identity/consent exchanges, downstream APIs/data stores, package distribution and non-gateway audit feeds are not drawn. Absence of a drawn route is not proof it cannot occur.
- OAuth consent/redirect checks, confused deputy, token passthrough and resource binding, client metadata discovery, state-handle/session ownership and replay need deployment/version-specific review. The diagram/register is not exhaustive for these.
- Local `stdio` runs between local processes; an HTTP gateway cannot inspect that traffic. Exact command allowlisting does not prove executable/package integrity. Validate package version/content, command resolution, endpoint controls and sandboxing separately.
- Backend input validation, per-tool/per-object/per-tenant authorization and TLS are required independent of a gateway or preview detector. A VS Code hook, WAF, allowlist or exam-skill link is not proof that those controls are implemented.
- No actor counts, data sensitivity distribution, tenant scale, per-factor DREAD rubric, mitigation owner/status, control effectiveness or residual-risk acceptance has been validated. Scores remain uncalibrated scenario estimates. There is no empirical justification for raising a factor to 7 because a different product was exploited; that old rule is superseded.

Public threat URLs remain `mcp-governance-stride.html#t-<ID>`. Public element URLs remain:
- `mcp-governance-stride.html#el-EE1`
- `mcp-governance-stride.html#el-EE2`
- `mcp-governance-stride.html#el-EE3`
- `mcp-governance-stride.html#el-EE4`
- `mcp-governance-stride.html#el-P1`
- `mcp-governance-stride.html#el-P2`
- `mcp-governance-stride.html#el-P3`
- `mcp-governance-stride.html#el-P4`
- `mcp-governance-stride.html#el-P5`
- `mcp-governance-stride.html#el-P6`
- `mcp-governance-stride.html#el-DS1`
- `mcp-governance-stride.html#el-DS2`
- `mcp-governance-stride.html#el-DS3`
- `mcp-governance-stride.html#el-F1`
- `mcp-governance-stride.html#el-F2`
- `mcp-governance-stride.html#el-F3`
- `mcp-governance-stride.html#el-F4`
- `mcp-governance-stride.html#el-F5`

## Reproduction and checks

Rebuild both artifact sets after changing source data:

```sh
python3 -I scripts/build-mcp-stride.py
python3 -I scripts/build-mcp-stride-page.py
python3 -I scripts/check-mcp-stride.py
python3 -I scripts/check-mcp-stride.py --quotes /tmp/mcp-stride-audit
python3 -I scripts/section_anchors.py --check
```

The optional source cache must be freshly populated from the source-table URLs before interpreting quote matches as a live check. Its filename convention is documented in `scripts/check-evidence-quotes.py`. `check-mcp-stride.py` verifies every reviewed scenario's exact wording, TSV/page scores and evidence, all public threat IDs, element IDs, duplicate HTML IDs, removal of the obsolete evidence rule and all 208 quotes when a cache is supplied. It does not prove semantic correctness or mitigations work.

UI and export verification results are recorded below after execution. No security attack or mitigation efficacy test was performed.

## Diagram wording ledger

Labels name logical elements or modeled operations; boundaries, policy delivery, calls and logging are design requirements, not evidence of enforcement. Threat chips are reviewed in the row ledger above. No diagram label asserts a product guarantee or a tested bypass block.

<!-- Begin reviewed diagram labels -->
label	DS1 Approved list in Git
label	DS2 Policy targets (GitHub, Foundry, Power Platform, M365 admin center)
label	DS3 Logs and Purview audit
label	EE1 Developer
label	EE2 M365 Copilot user
label	EE3 Requester and approver
label	EE4 Unapproved or malicious MCP server
requirement	F1 policy update
requirement	F2
requirement	F2 tool call
requirement	F3 calls
requirement	F4 response
requirement	F5 direct bypass attempt
requirement	F5 unapproved server
label	P1 Sync pipeline
label	P2 Managed client (VS Code, Windows device)
label	P3 Cloud agents
label	P4 Gateway (API Management or AI Gateway)
label	P5 Company MCP server
label	P6 Runtime detection
requirement	TB0 Internet: not company controlled
requirement	TB1 Company governance
requirement	TB2 Policy targets (Microsoft and GitHub clouds)
requirement	TB3 Managed Windows device
requirement	TB4 Microsoft cloud agents
requirement	TB5 Company Azure: gateway
requirement	TB6 Private backend network
requirement	TB7 Monitoring
requirement	applied
requirement	log
requirement	on merge
requirement	pull request
requirement	uses
<!-- End reviewed diagram labels -->

## Final validation (2026-11-12)

- Both builders completed: 74 threats, 8 High / 60 Medium / 6 Low; 2 exploited-class / 12 disclosed-class / 60 without attached matching public record.
- Follow-up non-CVE additions rebuilt successfully. The register retains 14 evidenced threat IDs, now with 38 associations and 37 distinct records. Scenario/evidence consistency, stable anchors, section anchors and `git diff --check` passed. No browser layout or security attack test was performed for these evidence-text additions.
- `check-mcp-stride.py --quotes /tmp/mcp-stride-audit` passed: exact review verdicts for 74 scenarios, 33 diagram labels/design requirements, page/TSV scores and evidence, public threat and element identifiers, and all 208 live-source quotes across 62 URLs. Legend examples now use real threats with matching rating and evidence state; the old E5 solid example no longer falsely implies it has public evidence.
- `section_anchors.py --check` and `git diff --check` passed. Local links in the index and threat-model page resolve. Both XML exports parse and every edge endpoint resolves. Inline JavaScript passes `node --check`; embedded JSON parses. Existing HTML IDs are preserved, including the now-unused hidden score-lift marker.
- Not completed: desktop/narrow viewport rendering, browser console and interactive controls, or a new draw.io visual render. The environment blocked browser access to the local preview; no workaround was attempted. XML/syntax checks do not replace visual or browser-runtime checks.
- Independent recheck on 2026-11-12: all 29 cited CVE records were read from the CVE.org record API (all published; titles and row mappings match), and the CISA KEV catalog (version 2026.11.10) lists CVE-2026-59822. One title was corrected: CVE-2026-33032 now says the nginx-ui MCP message endpoint has no authentication and its empty default IP allowlist allows every caller; the old wording said authentication was skipped only when the allowlist was empty. The Asana report and the IONIX post were reread in a browser and match the I14 and I5 wording. The SC-500 study guide still shows "Last updated on 2026-05-13" and all 32 mapped skill names.
- Browser pass on 2026-11-12, replacing the "Not completed" item above for the page itself: the page loads with no console messages at desktop width and at 375 px, with no sideways page scroll at 375 px. 74 chips and 74 register rows render. `#t-S8` opens the threat panel and `#el-P5` opens the element view with 7 threats. Filters return 14 rows (public record only), 8 (High) and 13 (Repudiation), and clearing returns 74. A draw.io visual render was not checked: no draw.io application is installed on this machine.
- Corrections on 2026-11-12: T7 was reworded so its Tampering consequence is explicit; id, element, scores and basis are unchanged. Register sorting was then tested in a browser: all eight column buttons sort all 74 rows in both directions. One defect was seen and fixed: the first click on Evidence put the 60 rows without a public record first; it now puts exploited and disclosed rows first. Both builders and all checks were rerun and pass.
- No attack, mitigation efficacy, SDK-version applicability or tenant configuration test was performed. The open-work plan records those limits.

The SC-500 export is labeled as related study topics, not proven mitigations. R1 local configuration history and R6 endpoint runtime attribution are marked outside the outline (with Sentinel ingestion retained as a related topic); D2 Windows outbound policy and E2 local approval bypass are no longer presented as Azure Firewall/NSG or Azure RBAC/PIM implementation controls.

## Governance alignment review (2026-11-12)

Reconciled the model with the interactive design's holistic review. This supplements the earlier row-by-row review; it does not reverify the model's CVEs or incident records.

- E5: related controls now include baseline gateway authorization. The shared managed-identity baseline can need caller-specific authorization just as a preview shared connection does; V79 illustrates the latter only.
- I15: added client policy and `ctrl-foundry-egress`; its basis identifies Network guardrails as preview (V101/V134) and distinguishes released toolbox egress from inbound private access. The scenario text and scores stay unchanged.
- T9: basis now states the manual Microsoft 365 and unverified Power Platform MCP automation paths. F1's name describes validated adapters and manual target changes.
- DFD text and Method now explicitly exclude direct BYO access to the private company backend and record gateway-fronted BYO composition as untested. The diagram remains aggregated; it does not claim a validated deployment or draw that excluded composition.
- Rebuilt HTML, TSV and draw.io exports from their sources. All 74 threat IDs, 18 element IDs and DREAD scores are preserved. The source checker follows the expanded 215-row governance evidence inventory and explicitly reports the unavailable historical V195 quote.

The governance quote verification covers 214 available source quotes with one explicitly unverified historical quote. It does not establish tenant protection or revalidate the threat model's external vulnerability records. Browser and build results for this revision are recorded in the associated design fact check.

### Completion alignment (2026-11-12)

T9 now links Power Platform policy configuration and records that mixed mode is required where classic policies protect custom/HTTP connectors (V214). T14 links the preview tool-evaluation control and states that discovery/session operations are outside its evaluation scope (V213); the scenario remains tool-result injection. Hostile discovery metadata requires its own review. No scenario, score, public identifier or incident association changed. The DFD text export carries these deployment constraints.

The complete governance quote inventory now has 215 rows: 214 matching the same-day source snapshots and one explicitly unavailable historical quote (V195), unused by active claims. New passages were read live through the web connector. Browser QA was attempted but blocked by unavailable headless Chrome and a locked Mac; tenant and attack validation remain outside this design-stage review.

### Final governance alignment (2026-11-12)

T9 now also records the workload-specific ACP availability qualification from V216. The final governance inventory has 216 rows: 215 match the existing same-day source snapshots and V195 remains explicitly unverified and unused. All 74 threat scenarios, scores, IDs and incident associations remain unchanged. Both exports and the HTML were regenerated; quote, register, label, anchor, local-link, syntax and deterministic-build checks pass. Browser QA for this revision remains blocked by unavailable headless Chrome and a failed in-app browser session; no tenant or attack test was run.


### Design context alignment (2026-11-13)

- R2 now distinguishes one-time approval from saved per-tool approval (V164, V227); missing approval attribution remains interpretation by AI.
- T9's basis records individual connector overrides and the User access ceiling (V226), consistent with the tightened default-deny design.
- T6 now points to gateway/server authorization and server-side argument validation requirements, rather than only a client hook whose MCP coverage is unverified. Its study mapping uses API Management and Functions instead of treating WAF as the validation boundary.
- D7 no longer claims repository loss prevents every target change: emergency manual blocks remain possible. Scores and public IDs are unchanged.
- Re-read all 74 scenario/control pairs for consistency with the revised design. Regenerated the page, TSV and draw.io exports; quote, diagram-label, score/export and anchor checks passed. The historical public-record evidence was not independently re-fetched in this design-alignment pass, so the page's broader Current as of date was not advanced.
