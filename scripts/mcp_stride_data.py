"""Data for the STRIDE and DREAD threat model of mcp-governance-microsoft-interactive.html.

Every threat is interpretation by AI. Scores are AI estimates, and no attack was run in a tenant.
Some threats also match a public record (a CVE, a vendor advisory or a researcher demo). Those are listed in
OBSERVED with a link and an evidence level; the match is AI judgement, the record itself is not.
Page ids (ctrl-*, gap-*) must exist on the interactive page; build-mcp-stride.py checks that.
"""

STRIDE = {
    "S": "Spoofing",
    "T": "Tampering",
    "R": "Repudiation",
    "I": "Information disclosure",
    "D": "Denial of service",
    "E": "Elevation of privilege",
}

# kind: ext = external entity, proc = process, store = data store, flow = data flow, in element order
ELEMENTS = {
    "EE1": ("ext", "Developer using VS Code or GitHub Copilot"),
    "EE2": ("ext", "Microsoft 365 Copilot user"),
    "EE3": ("ext", "Requester and approver (Git pull request, admin center)"),
    "EE4": ("ext", "Unapproved or malicious MCP server"),
    "P1": ("proc", "Sync pipeline"),
    "P2": ("proc", "Managed client on Windows device"),
    "P3": ("proc", "Cloud agents (Microsoft 365 Copilot, Foundry, Copilot Studio)"),
    "P4": ("proc", "Gateway (API Management or AI Gateway)"),
    "P5": ("proc", "Company MCP server"),
    "P6": ("proc", "Runtime threat detection (Defender or external provider)"),
    "DS1": ("store", "Approved list in Git"),
    "DS2": ("store", "Policy targets (GitHub, Foundry, Power Platform, M365 admin center)"),
    "DS3": ("store", "Logs and Purview audit"),
    "F1": ("flow", "Policy sync: Git to pipeline to policy targets"),
    "F2": ("flow", "Tool call: client or agent to gateway"),
    "F3": ("flow", "Gateway to company MCP server"),
    "F4": ("flow", "Tool response back to the agent"),
    "F5": ("flow", "Bypass call: direct to backend or to an unapproved server"),
}

APPLIES = {
    "ext": "SR",
    "proc": "STRIDE",
    "store": "TRID",
    "flow": "TID",
}

# Short code -> SC-500 skill text, as published on the Microsoft Learn study guide (page last updated 2026-05-13, read 2026-11-12).
SC500 = {
    "CA": "1.1 Implement conditional access policies",
    "PIM": "1.1 Implement and configure Privileged Identity Management (PIM)",
    "MI": "1.1 Implement and configure managed identities for Azure resources",
    "APPID": "1.1 Implement and configure identity for applications, including enterprise applications and app registrations",
    "OAUTH": "1.1 Manage OAuth permission grants and consent settings",
    "KVACC": "1.2 Configure access to Key Vault",
    "KVSCAN": "1.2 Scan for secrets by using Defender Cloud Security Posture Management (Defender CSPM)",
    "IAC": "1.3 Implement and configure security controls by using infrastructure as code",
    "RBAC": "1.3 Evaluate and remediate overprivileged access assignments by using Azure role-based access control (RBAC)",
    "POLICY": "1.3 Implement and configure security controls by using Azure Policy",
    "PE": "2.3 Configure Azure private endpoints to secure access to Azure platform as a service (PaaS) resources",
    "FW": "2.3 Implement and configure Azure Firewall",
    "NSG": "2.3 Implement and manage network security groups (NSGs) and application security groups (ASGs)",
    "ENTRAPA": "2.3 Implement and configure Microsoft Entra Private Access",
    "AGENTCA": "3.1 Implement conditional access for Microsoft Entra Agent ID",
    "AGENTBLAST": "3.1 Analyze blast radius for security risks related to Entra Agent ID by using Defender XDR",
    "AGENTACC": "3.1 Manage Entra Agent ID access",
    "AIGW": "3.1 Configure and deploy AI Gateway in Azure API Management for Microsoft Foundry",
    "GUARD": "3.1 Configure guardrails for agent security in Foundry",
    "RTP": "3.1 Enable and configure real-time protection for Microsoft Copilot Studio agents",
    "DSPM": "3.1 Identify risks related to Microsoft Copilot and AI apps by using Microsoft Purview Data Security Posture Management (DSPM)",
    "AIDASH": "3.1 Monitor AI security by using the Data and AI security dashboard in Defender for Cloud",
    "M365AGENTS": "3.1 Manage agents in Microsoft 365 admin center",
    "SHAREPOINT": "3.1 Identify overexposure of data in SharePoint",
    "FUNC": "3.3 Implement and configure security controls for Azure Functions, including authentication and network access",
    "APIM": "3.3 Implement security policies for back-end API protection by using API Management",
    "WAF": "3.3 Implement and configure Azure Web Application Firewall",
    "SENCONN": "4.2 Configure and use Microsoft data connectors for Azure resources",
    "SENRET": "4.2 Implement data retention in Microsoft Sentinel data stores",
    "SENAUTO": "4.2 Implement automation rules and playbooks in Microsoft Sentinel",
    "PURVAUDIT": "4.2 Query Microsoft Purview Audit in Defender XDR",
    "CSPM": "4.1 Identify security risks by using Defender CSPM",
}

# Used by threats whose control is a GitHub, VS Code, Intune or Power Platform setting that SC-500 does not list.
OUTSIDE = "outside"

# (element, category, threat, page control ids, SC-500 codes, (D, R, E, A, Di), basis)
# basis: V-number of a quoted claim in the page's fact check, "gap-..." id, or "AI inference"
THREATS = [
    # External entities
    ("EE1", "S", "A stolen developer sign-in token is used to call the gateway as that developer.",
     ["ctrl-identity", "ctrl-gateway"], ["CA", "AGENTACC"], (7, 5, 5, 4, 5), "AI inference"),
    ("EE1", "R", "A developer denies adding an unapproved server; neither managed configuration history nor endpoint telemetry records who changed the user file.",
     ["ctrl-logging", "ctrl-client"], [OUTSIDE, "SENCONN"], (4, 6, 4, 3, 5), "AI inference"),
    ("EE2", "S", "An attacker able to send through an allowed source impersonates a Copilot user when the gateway checks only the source IP and does not authenticate the user or tenant.",
     ["ctrl-m365-network", "ctrl-identity"], ["CA", "APIM"], (6, 5, 4, 5, 5), "V170 V174; attacker access to an allowed source is a precondition, not a documented cross-tenant bypass"),
    ("EE2", "R", "A user denies approving a write tool call, and retained records do not bind that approval to the user, tool arguments and resulting action.",
     ["ctrl-g-write-approval", "ctrl-purview-audit"], ["PURVAUDIT", "DSPM"], (3, 5, 3, 2, 4), "V164 requires approval; insufficient approval correlation is AI inference, not a claim about product storage"),
    ("EE3", "S", "An attacker with a stolen approver or admin account approves a server in Git or in the admin center.",
     ["ctrl-inventory", "ctrl-m365"], ["PIM", "CA"], (8, 3, 4, 7, 4), "AI inference"),
    ("EE3", "R", "An admin denies a manual connector-access change, and no retained admin audit record or change request can attribute it to the admin.",
     ["ctrl-m365", "gap-m365-by-hand"], ["PURVAUDIT", "M365AGENTS"], (5, 7, 3, 4, 7), "V171 requires manual administration; missing attribution is AI inference, not implied by absence from Git"),
    ("EE4", "S", "An attacker controls a subdomain or path actually covered by a broad allowlist wildcard and presents its server as approved.",
     ["ctrl-client", "ctrl-inventory"], [OUTSIDE], (7, 4, 5, 5, 4), "V17 supports wildcards; attacker control of a matching endpoint is AI inference. A look-alike domain alone need not match"),
    ("EE4", "R", "An unapproved server operator denies receiving company data, and no company-side request record or independently retained receipt can establish the transfer.",
     ["ctrl-logging"], ["SENCONN", "FW"], (4, 8, 3, 3, 6), "AI inference"),

    # P1 Sync pipeline
    ("P1", "S", "An attacker uses a leaked pipeline credential to write a list to a policy target.",
     ["ctrl-pipeline"], ["MI", "KVACC"], (8, 4, 4, 7, 4), "AI inference"),
    ("P1", "T", "An attacker gets unreviewed pipeline code merged or executed with deployment credentials and changes the approved-server policy at every target that identity can write.",
     ["ctrl-inventory", "ctrl-pipeline"], ["IAC"], (9, 4, 4, 8, 4), "AI inference"),
    ("P1", "R", "The pipeline writes to a target and keeps no run record that ties the change to a reviewed commit.",
     ["ctrl-pipeline"], ["IAC", "SENAUTO"], (4, 6, 3, 4, 5), "ctrl-pipeline"),
    ("P1", "I", "Pipeline run logs print target credentials that are then read by someone without permission to use those credentials.",
     ["ctrl-pipeline"], ["KVSCAN", "KVACC"], (6, 4, 4, 5, 4), "AI inference"),
    ("P1", "D", "An attacker disables the sync runner or its credentials, preventing legitimate policy updates and onboarding until service is restored.",
     ["ctrl-pipeline"], ["SENAUTO"], (5, 6, 3, 6, 5), "AI inference; V90 describes a propagation delay, not denial of service"),
    ("P1", "E", "An attacker compromises a runner intended for one target and uses a shared deployment credential to administer other targets beyond that runner's intended scope.",
     ["ctrl-pipeline"], ["RBAC", "MI"], (8, 4, 4, 7, 3), "ctrl-pipeline"),

    # P2 Managed client
    ("P2", "S", "An attacker who can replace an executable or alter command resolution supplies a malicious binary under the exact command and arguments allowed for a local stdio server.",
     ["ctrl-stdio"], [OUTSIDE], (6, 4, 4, 3, 4), "V18 matches command and arguments, not binary integrity; writable executable or search path is AI inference"),
    ("P2", "T", "An attacker with repository write access alters a trusted MCP configuration or custom agent profile to select a malicious server, and the client does not require a fresh review.",
     ["gap-github-builtin", "ctrl-client"], [OUTSIDE], (6, 8, 7, 6, 7), "V20 excludes custom agent profiles from these lists; trusted-config replacement is illustrated by Cursor, not proven for GitHub or VS Code. V21 is a separate policy exemption, not tampering"),
    ("P2", "T", "A package publisher adds a backdoor to a previously trusted local MCP package, and a user or an unpinned launcher installs the malicious version.",
     ["ctrl-stdio"], [OUTSIDE], (7, 6, 5, 5, 4), "AI inference"),
    ("P2", "R", "A user denies launching a local MCP process, and retained endpoint, process and configuration records cannot attribute the launch to that user.",
     ["ctrl-logging", "ctrl-g-defender-for-endpoint-runtime-protection"], [OUTSIDE, "SENCONN"], (4, 6, 3, 4, 4), "V146 describes endpoint runtime protection; absence of that feature does not prove absence of other logs. Insufficient attribution is AI inference"),
    ("P2", "I", "With Allow all, a tool call sends files or secrets to an approved but over-permissioned server without a prompt.",
     ["ctrl-g-approval-lock", "ctrl-g-confirmation-dialog"], [OUTSIDE], (8, 6, 6, 4, 5), "V152 V157"),
    ("P2", "D", "An attacker or mistaken administrator deploys an outbound block policy without required allow rules, denying legitimate network-dependent work on managed devices.",
     ["ctrl-windows", "gap-windows-outbound"], [OUTSIDE], (5, 6, 2, 6, 6), "V32 V34"),
    ("P2", "E", "Attacker-controlled repository content or MCP output bypasses the client's command approval checks, causing code to run with the user's privileges without the required approval.",
     ["ctrl-stdio", "ctrl-client"], [OUTSIDE], (7, 5, 3, 3, 4), "AI inference"),
    ("P2", "E", "An untrusted server exploits a local MCP library's command parsing, or a malicious website reaches an unauthenticated local HTTP MCP endpoint through DNS rebinding, gaining tool access or code execution with the local process's privileges.",
     ["ctrl-stdio", "ctrl-client"], [OUTSIDE], (9, 6, 5, 5, 5), "AI inference"),

    # P3 Cloud agents
    ("P3", "S", "An attacker presents another cloud agent's identity to a tool that trusts a supplied agent name or identifier without validating its authenticated identity and tenant.",
     ["ctrl-identity", "ctrl-g-defender-rules-and-scope"], ["AGENTCA", "AGENTACC"], (6, 6, 4, 4, 4), "AI inference; V145 describes agents selectable in rule scope, not agent impersonation or a universal coverage rule"),
    ("P3", "T", "Hidden text in an external document steers the agent to call a tool the user did not intend.",
     ["ctrl-g-prompt-attack-block", "ctrl-g-untrusted-results"], ["GUARD", "RTP"], (8, 6, 6, 6, 8), "V107 V110"),
    ("P3", "R", "An agent owner denies a tool action, and the deployment has not retained correlated agent, gateway and backend events that identify the initiating user and tool arguments.",
     ["ctrl-purview-audit", "ctrl-logging"], ["PURVAUDIT", "DSPM"], (5, 7, 3, 5, 6), "V208 covers prompts and responses; omission of MCP tool calls from that page does not establish absence of tool audit. Missing correlation is AI inference"),
    ("P3", "I", "A compromised agent sends secrets out through an MCP tool argument.",
     ["ctrl-g-defender-rules-and-scope", "ctrl-g-defender-real-time-protection"], ["RTP", "DSPM", "SHAREPOINT"], (8, 5, 5, 5, 5), "V125"),
    ("P3", "D", "An agent loop calls a tool without limit and uses up the gateway rate limit and the backend.",
     ["ctrl-gateway"], ["APIM"], (5, 6, 5, 6, 6), "V3"),
    ("P3", "E", "A read-only agent is configured with an empty allowed_tools list by mistake; an attacker then induces a write call that the server permits under the connection's credentials.",
     ["ctrl-foundry", "ctrl-g-approval"], ["GUARD", "AGENTACC"], (8, 7, 6, 5, 6), "V69"),

    # P4 Gateway
    ("P4", "S", "A gateway with missing or defective authentication accepts an unauthenticated caller as trusted, for example by relying only on source IP or accepting a fabricated bearer token.",
     ["ctrl-identity", "ctrl-m365-network"], ["CA", "APIM"], (8, 4, 5, 6, 5), "V174"),
    ("P4", "T", "An attacker with gateway policy write access, including a compromised service granted the Agent 365 policy role, removes authentication or tool restrictions from an API policy.",
     ["ctrl-a365-consent", "ctrl-a365"], ["PIM", "OAUTH", "POLICY"], (8, 3, 4, 7, 3), "V39 V40"),
    ("P4", "R", "Gateway logs miss fields or expire early, so a tool call cannot be shown later.",
     ["ctrl-logging", "ctrl-gateway"], ["SENCONN", "SENRET"], (5, 5, 3, 5, 5), "V3"),
    ("P4", "I", "A gateway caches a sensitive tool result without binding the cache key to the authorized caller and tenant, and returns it to another caller.",
     ["ctrl-identity", "ctrl-gateway"], ["APIM", "DSPM"], (6, 5, 4, 5, 4), "AI inference; requires a configured result cache. Log disclosure is covered by I10; shared-identity authorization by E5"),
    ("P4", "D", "An attacker exhausts gateway capacity or request quotas, denying legitimate calls when clients depend on that deployment and no adequate isolation or failover is configured.",
     ["ctrl-gateway", "ctrl-ai-limits"], ["APIM", "WAF"], (7, 5, 5, 8, 6), "AI inference; V47 V52 document private-endpoint and regional limits for AI Gateway preview, not an Azure region pair or an APIM-wide limitation"),
    ("P4", "E", "A gateway fails to enforce caller-specific tool authorization, allowing a low-privilege caller to invoke privileged operations through a more powerful shared backend connection.",
     ["ctrl-ai-publish", "ctrl-identity"], ["MI", "RBAC"], (7, 5, 4, 5, 3), "V79 supports shared connection permissions; missing caller-specific authorization is AI inference. A shared connection alone is not a vulnerability"),

    # P5 Company MCP server
    ("P5", "S", "A backend with missing authentication or incomplete token validation accepts an unauthenticated request or a token issued for another resource as an approved caller.",
     ["ctrl-identity", "ctrl-backend"], ["APPID", "FUNC", "MI"], (8, 4, 4, 5, 4), "AI inference"),
    ("P5", "T", "An attacker supplies a tool argument that escapes the intended command, query or filesystem scope and causes an unauthorized data or file modification under the server's privileges.",
     ["ctrl-g-tool-call-hook"], ["APIM", "WAF"], (9, 5, 5, 5, 5), "AI inference, not a page control"),
    ("P5", "R", "A caller denies a backend action; the server logs only a shared gateway identity and retains no correlation identifier that joins it to an authenticated upstream caller record.",
     ["ctrl-identity", "ctrl-logging"], ["SENCONN", "SENRET"], (4, 6, 3, 4, 4), "AI inference"),
    ("P5", "I", "An attacker reads backend data because authentication is disabled or a read tool fails to enforce object, path, query or tenant authorization; public reachability makes the vulnerable endpoint accessible but does not itself grant access.",
     ["ctrl-backend", "ctrl-identity"], ["PE", "FUNC", "ENTRAPA"], (9, 5, 5, 7, 4), "V9 V11 support network restrictions; missing authentication or read authorization is AI inference and illustrated by the attached records"),
    ("P5", "I", "The server joins a caller-supplied path or address to its cloud API base address, so its own cloud token goes to a host the attacker picks.",
     ["ctrl-backend", "ctrl-identity"], ["FUNC", "RBAC"], (8, 5, 5, 6, 4), "AI inference"),
    ("P5", "D", "An attacker floods a publicly reachable backend that lacks effective inbound restrictions and resource limits, denying legitimate tool calls.",
     ["ctrl-backend"], ["PE", "FUNC", "FW"], (6, 5, 4, 6, 4), "V11 V13: classic Consumption lacks private endpoints but supports inbound restrictions; absence of a private endpoint alone does not establish exposure"),
    ("P5", "E", "An attacker exploits an unchecked outbound URL or another server-side authorization flaw to reach internal services or cloud credentials with the server's privileges beyond the caller's permitted tool scope.",
     ["ctrl-identity", "ctrl-ai-publish"], ["RBAC", "MI"], (8, 4, 3, 5, 3), "AI inference"),

    # P6 Defender and threat detection (preview)
    ("P6", "S", "The external threat detection service for Copilot Studio is replaced by one that always answers allow.",
     ["ctrl-g-threat-detection"], ["RTP", "OAUTH"], (6, 3, 3, 4, 3), "V112 V113"),
    ("P6", "T", "An attacker rewrites or splits the content that a detection check inspects so an unsafe action receives an allow verdict; the unsafe email scenario is checked only at the tool request.",
     ["ctrl-g-defender-rules-and-scope"], ["RTP", "GUARD"], (6, 5, 5, 5, 5), "V144"),
    ("P6", "R", "An operator denies disabling a blocking rule, and retained administration records cannot establish who changed the protection configuration.",
     ["ctrl-g-defender-rules-and-scope", "ctrl-logging"], ["AIDASH", "SENAUTO"], (4, 7, 2, 5, 6), "AI inference; V123 says default rules record activity. Unread audit events do not by themselves enable repudiation"),
    ("P6", "I", "A compromised or excessively privileged external threat detection provider exposes sensitive agent data received for inspection to an unauthorized party.",
     ["ctrl-g-threat-detection"], ["DSPM"], (5, 8, 2, 4, 6), "V140 supports data sharing; provider compromise or unauthorized onward disclosure is AI inference. Intended inspection is not itself a disclosure vulnerability"),
    ("P6", "D", "An attacker overloads the Copilot Studio detection provider so it cannot return verdicts in time; under the documented default, a response taking more than one second permits the tool to run.",
     ["ctrl-g-threat-detection"], ["RTP"], (7, 6, 4, 5, 5), "V114"),
    ("P6", "E", "An attacker induces a privileged tool action while the deployment mistakenly relies on Audit mode or only a post-invocation check to prevent it; required authorization or pre-invocation enforcement is missing.",
     ["ctrl-ttp-modes", "ctrl-ttp-users"], ["AIGW", "GUARD"], (7, 6, 4, 4, 4), "V55 V59: Audit mode does not block; a post-invocation denial cannot undo completed actions. Block mode is documented as fail-closed. Privilege gain requires the stated authorization gap"),

    # DS1 Approved list
    ("DS1", "T", "An attacker with repository write access bypasses required review through a direct push or unreviewed merge and changes the approved list.",
     ["ctrl-inventory"], ["IAC", "POLICY"], (9, 4, 4, 8, 4), "ctrl-inventory"),
    ("DS1", "R", "An attacker rewrites approval history and denies proposing a server; no independent pull-request review or authenticated approval record survives to attribute the proposal.",
     ["ctrl-inventory"], ["IAC"], (3, 5, 3, 2, 5), "AI inference"),
    ("DS1", "I", "A repository containing sensitive internal server addresses or owner details is readable by people without a business need for that inventory.",
     ["ctrl-inventory"], ["KVSCAN"], (4, 7, 2, 4, 6), "AI inference"),
    ("DS1", "D", "The repository is deleted or unavailable, so no change can reach the targets.",
     ["ctrl-inventory", "ctrl-pipeline"], ["POLICY"], (4, 3, 3, 5, 3), "AI inference"),

    # DS2 Policy targets
    ("DS2", "T", "An attacker or administrator bypasses required review with a manual policy-target edit, allowing servers that the approved Git list excludes.",
     ["ctrl-pipeline", "ctrl-m365", "gap-m365-by-hand"], ["M365AGENTS", "POLICY"], (6, 7, 4, 5, 6), "V171"),
    ("DS2", "R", "An operator denies a manual target-policy change, and retained target history cannot link the write to an authenticated operator or a reviewed change request.",
     ["ctrl-m365", "ctrl-logging"], ["PURVAUDIT"], (4, 7, 3, 4, 6), "gap-m365-by-hand"),
    ("DS2", "I", "A policy target grants configuration read access to an unauthorized principal, exposing sensitive server inventory or connection details.",
     ["ctrl-inventory"], [OUTSIDE], (3, 6, 3, 3, 5), "AI inference"),
    ("DS2", "D", "A wrong switch, such as turning off every MCP server in Copilot policy, stops all users at once.",
     ["gap-github-builtin"], [OUTSIDE], (6, 4, 3, 8, 4), "V93"),

    # DS3 Logs and audit
    ("DS3", "T", "An attacker with log deletion, purge or ingestion-control privileges removes audit evidence or injects forged entries; ordinary log read access is insufficient.",
     ["ctrl-logging"], ["SENRET", "RBAC"], (6, 3, 3, 5, 3), "AI inference"),
    ("DS3", "R", "A caller denies a tool action and the audit store lacks authenticated caller, tenant or correlation fields needed to join the agent, gateway and backend records.",
     ["ctrl-logging"], ["SENCONN", "PURVAUDIT"], (5, 6, 3, 5, 5), "AI inference"),
    ("DS3", "I", "Logs hold tool arguments and results with personal or secret data, readable by a wide group.",
     ["ctrl-logging"], ["SENRET", "DSPM", "RBAC"], (6, 6, 4, 5, 4), "AI inference"),
    ("DS3", "D", "An attacker disables ingestion or reduces retention below the required investigation period, making audit records unavailable when investigators need them.",
     ["ctrl-logging"], ["SENRET", "SENCONN"], (5, 5, 2, 5, 5), "AI inference"),

    # F1 Policy sync
    ("F1", "T", "An attacker changes a policy payload at a compromised intermediary or across a connection without effective transport integrity, and the target applies the altered policy.",
     ["ctrl-pipeline"], ["IAC"], (7, 2, 2, 6, 2), "AI inference"),
    ("F1", "I", "An attacker reads deployment credentials or sensitive policy data in transit because TLS is absent, certificate validation is disabled or a trusted TLS intermediary is compromised.",
     ["ctrl-pipeline"], ["KVACC", "KVSCAN"], (6, 3, 3, 5, 3), "AI inference"),
    ("F1", "D", "Policy delivery is interrupted or an API request is rejected, preventing an approved update from reaching a target while no working retry or manual recovery path exists.",
     ["ctrl-power-platform", "ctrl-pipeline"], [OUTSIDE], (4, 6, 2, 4, 6), "AI inference; V66 describes policy APIs generally. MCP-specific automation support remains unverified, not a documented API failure"),

    # F2 Tool call to gateway
    ("F2", "T", "An attacker at a compromised intermediary or a connection without effective TLS integrity changes the requested tool or arguments before the gateway authenticates and authorizes the request.",
     ["ctrl-gateway"], ["APIM", "WAF"], (6, 2, 2, 4, 2), "AI inference"),
    ("F2", "I", "A bearer token or sensitive tool argument is exposed to an untrusted proxy, a plaintext connection or a shared URL carrying credentials, allowing an attacker to read or reuse it.",
     ["ctrl-identity", "ctrl-logging"], ["CA", "KVSCAN"], (7, 4, 3, 4, 4), "V51 specifies the Authorization header; credential disclosure requires the stated transport or URL-handling failure, not ordinary bearer authentication"),
    ("F2", "D", "Microsoft 365 Copilot egress addresses change and the operator misses the announced update, so a stale inbound allowlist rejects legitimate calls.",
     ["ctrl-m365-network"], ["APIM", "NSG"], (5, 4, 3, 6, 6), "V175"),

    # F3 Gateway to server
    ("F3", "T", "An attacker modifies backend requests across a link with missing TLS integrity, disabled certificate validation or a compromised TLS terminator, causing unauthorized changes.",
     ["ctrl-backend", "ctrl-identity"], ["PE", "NSG"], (7, 3, 3, 6, 3), "AI inference; V9 supports restricting direct access, not the claim that public-network traffic defeats correctly validated TLS"),
    ("F3", "I", "An attacker reads backend request data on an unencrypted link or at a compromised TLS terminator; use of a public route alone does not reveal TLS-protected payloads.",
     ["ctrl-backend", "ctrl-identity"], ["PE", "ENTRAPA"], (7, 3, 3, 6, 3), "AI inference; V9 supports network restrictions, not passive decryption of HTTPS"),
    ("F3", "D", "The private path to the backend fails, and every approved call fails with it.",
     ["ctrl-backend"], ["PE", "NSG"], (6, 4, 2, 8, 5), "AI inference"),

    # F4 Tool response
    ("F4", "T", "A tool result carries instructions that the agent follows (indirect prompt injection).",
     ["ctrl-g-untrusted-results", "ctrl-g-tool-call-and-tool-response-guardrails", "ctrl-g-result-review"], ["GUARD", "RTP"], (9, 7, 6, 6, 8), "V107 V133 V154"),
    ("F4", "I", "A response with data for one user is returned to another user's agent session.",
     ["ctrl-identity", "ctrl-ttp-users"], ["APPID", "DSPM"], (7, 3, 3, 4, 3), "AI inference"),
    ("F4", "D", "A very large or endless response fills the agent's context or the gateway buffer.",
     ["ctrl-gateway"], ["APIM"], (4, 5, 4, 5, 5), "AI inference"),

    # F5 Bypass
    ("F5", "T", "A client directly reaches a backend that lacks equivalent action authorization and performs an unauthorized write that gateway policy would have blocked.",
     ["ctrl-backend", "ctrl-windows"], ["PE", "NSG", "FW"], (9, 5, 5, 6, 5), "AI inference, acceptance test 12"),
    ("F5", "I", "A compromised client sends company data directly to an unapproved MCP server over an allowed egress path, bypassing gateway inspection and its audit trail.",
     ["ctrl-backend", "ctrl-logging"], ["PE", "SENCONN"], (8, 5, 5, 5, 5), "AI inference"),
    ("F5", "D", "A direct flood skips gateway rate limits.",
     ["ctrl-backend", "ctrl-gateway"], ["PE", "WAF", "FW"], (6, 5, 4, 6, 4), "AI inference"),
]

# STRIDE-per-element cells with no threat. Empty on purpose: every applicable cell has a threat above.
NOT_APPLICABLE = {}


def dread_score(dr):
    return round(sum(dr) / 5, 1)


def rating(score):
    if score >= 6:
        return "High"
    if score >= 4:
        return "Medium"
    return "Low"


# Evidence levels, strongest first. exploited = used in attacks (CISA KEV entry or vendor-confirmed incident);
# disclosed = public CVE, vendor advisory or researcher demo, fixed or demonstrated, no confirmed attacks found;
# theoretical = interpretation by AI only. Threat id -> references. A reference is (level, title, url).
# Records rechecked on 2026-11-12 using the CVE Program CNA records, official CISA KEV data,
# Postmark's incident notice and the researcher's original demo. Matches are failure-class
# analogies, not findings against the proposed deployment. See the fact check for exclusions.
NVD = "https://nvd.nist.gov/vuln/detail/"
LEVELS = ("exploited", "disclosed", "theoretical")
OBSERVED = {
    "S8": [("exploited", "CVE-2026-59822 LiteLLM MCP endpoint accepts any bearer token (CISA KEV, added 2026-09-02)", NVD + "CVE-2026-59822"),
              ("disclosed", "CVE-2026-33032 nginx-ui MCP message endpoint has no authentication, and its empty default IP allowlist allows every caller", NVD + "CVE-2026-33032")],
    "I14": [("disclosed", "CVE-2026-48529 GitHub MCP Server in HTTP lockdown mode runs later users' queries with the first user's credentials", NVD + "CVE-2026-48529"),
              ("disclosed", "CVE-2026-25536 MCP TypeScript SDK leaks response data across clients when one server and transport instance is reused", NVD + "CVE-2026-25536"),
              ("disclosed", "Asana MCP server cross-organization data exposure reported by BleepingComputer, citing Asana notifications and spokesperson; no external hack reported", "https://www.bleepingcomputer.com/news/security/asana-warns-mcp-ai-feature-exposed-customer-data-to-other-orgs/")],
    "I6": [("disclosed", "CVE-2026-58201 Lokka (Microsoft 365 MCP server) sends an Azure Resource Manager bearer token to an unintended host through a crafted path", NVD + "CVE-2026-58201")],
    "I5": [("disclosed", "CVE-2026-114123 D365 Finance and Operations MCP Server: an empty API key permits anonymous read tools if no separate access controls protect the deployment", NVD + "CVE-2026-114123"),
              ("disclosed", "CVE-2026-33980 Azure Data Explorer MCP Server interpolates table_name into KQL without validation, allowing queries beyond the intended tool input", NVD + "CVE-2026-33980"),
              ("disclosed", "CVE-2025-66689 Zen MCP Server path traversal reads arbitrary files", NVD + "CVE-2025-66689"),
              ("disclosed", "CVE-2025-67366 filesystem-mcp symlink handling allows reads outside the permitted directory", NVD + "CVE-2025-67366"),
              ("disclosed", "IONIX researcher report: an exposed unauthenticated MCP server allowed tool invocation and demonstrated host file reads during low-impact testing", "https://www.ionix.io/blog/exposed-ai-agents-in-the-wild-public-mcp-server-security-exposed/")],
    "S9": [("disclosed", "CVE-2026-32211 Azure MCP Server missing authentication", NVD + "CVE-2026-32211"),
              ("disclosed", "CVE-2026-116684 MCP Python SDK bearer check accepts a token issued for a different resource server", NVD + "CVE-2026-116684")],
    "T6": [("disclosed", "CVE-2025-68143 mcp-server-git accepted arbitrary filesystem paths", NVD + "CVE-2025-68143"),
              ("disclosed", "CVE-2025-53355 mcp-server-kubernetes command injection", NVD + "CVE-2025-53355"),
              ("disclosed", "CVE-2025-53967 Framelink Figma MCP Server runs operating system commands from a crafted request", NVD + "CVE-2025-53967"),
              ("disclosed", "CVE-2025-68144 mcp-server-git passes user-controlled arguments to git without sanitizing, enabling arbitrary file overwrites", NVD + "CVE-2025-68144")],
    "E6": [("disclosed", "CVE-2026-26118 Azure MCP Server request forgery that raises privileges", NVD + "CVE-2026-26118"),
              ("disclosed", "CVE-2026-27826 mcp-atlassian lets an unauthenticated caller force outbound requests", NVD + "CVE-2026-27826"),
              ("disclosed", "CVE-2026-8355 IBM ContextForge MCP Gateway: a user-supplied token address makes the gateway send requests to internal hosts and cloud metadata", NVD + "CVE-2026-8355"),
              ("disclosed", "CVE-2025-65513 fetch-mcp SSRF bypasses the private IP check", NVD + "CVE-2025-65513")],
    "T4": [("disclosed", "CVE-2025-32711 Microsoft 365 Copilot AI command injection causing information disclosure; the CNA summary does not specify MCP", NVD + "CVE-2025-32711")],
    "I3": [("disclosed", "CVE-2025-32711 Microsoft 365 Copilot AI command injection causing information disclosure; the CNA summary does not specify an MCP tool argument", NVD + "CVE-2025-32711"),
              ("disclosed", "Invariant WhatsApp research demo (2025-04-07): malicious metadata redirects send_message and includes chat history; a separate injected-message test leaks contacts", "https://invariantlabs.ai/blog/whatsapp-mcp-exploited")],
    "T14": [("disclosed", "Invariant Labs demo: GitHub MCP issue text steers the agent to leak private repo data (2025-05-26)",
              "https://invariantlabs.ai/blog/mcp-github-vulnerability"),
              ("disclosed", "Pillar Security observed a live server returning credential-seeking tool metadata after three calls; the reviewed delivery pull requests were unmerged", "https://www.pillar.security/blog/deadbugz-currently-active-mcp-supply-chain-campaign"),
              ("disclosed", "General Analysis Supabase/Cursor research demo (2025-07-08): a support ticket causes privileged SQL reads and copies dummy tokens into an attacker-visible reply; not a customer breach", "https://generalanalysis.com/blog/supabase-mcp-blog")],
    "E2": [("disclosed", "CVE-2026-29783 GitHub Copilot CLI shell tool runs hidden commands after prompt injection", NVD + "CVE-2026-29783"),
              ("disclosed", "CVE-2026-30615 Windsurf prompt injection in HTML registers a malicious MCP STDIO server and runs commands", NVD + "CVE-2026-30615")],
    "E3": [("disclosed", "CVE-2025-6514 mcp-remote runs a command from a server's sign-in address", NVD + "CVE-2025-6514"),
              ("disclosed", "CVE-2025-49596 MCP Inspector runs code for unauthenticated requests", NVD + "CVE-2025-49596"),
              ("disclosed", "CVE-2025-9611 Microsoft Playwright MCP Server accepts web-page requests by DNS rebinding", NVD + "CVE-2025-9611"),
              ("disclosed", "CVE-2025-66416 MCP Python SDK leaves DNS rebinding protection off by default for local HTTP servers", NVD + "CVE-2025-66416"),
              ("disclosed", "CVE-2025-59163 vet in MCP SSE mode exposes scan data through DNS rebinding", NVD + "CVE-2025-59163"),
              ("disclosed", "CVE-2025-66414 MCP TypeScript SDK lacks DNS rebinding protection by default", NVD + "CVE-2025-66414")],
    "T2": [("disclosed", "CVE-2025-54136 Cursor runs a changed MCP config that was already trusted", NVD + "CVE-2025-54136")],
    "T3": [("exploited", "Postmark confirms an unofficial impersonating package added an email-stealing backdoor in version 1.0.16 after building trust over 15 versions",
               "https://postmarkapp.com/blog/information-regarding-malicious-postmark-mcp-package"),
              ("disclosed", "GHSA-p6wc-j7x7-ff3v: @antv/mcp-server-antv 0.2.8 and 0.3.8 contain a malicious preinstall hook after a publishing-account compromise; advisory does not quantify victims", "https://github.com/advisories/GHSA-p6wc-j7x7-ff3v")],
}


def level_of(tid):
    refs = OBSERVED.get(tid, [])
    for lv in LEVELS:
        if any(r[0] == lv for r in refs):
            return lv
    return "theoretical"


def adjust(tid, dr):
    """Keep scenario estimates separate from public-record evidence (legacy call signature)."""
    return tuple(dr)
