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
    "P6": ("proc", "Defender and threat detection checks (preview)"),
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
    ("EE1", "R", "A developer adds an unapproved server in a user file and later denies it; user settings leave no company record.",
     ["ctrl-logging", "ctrl-client"], ["PURVAUDIT", "SENCONN"], (4, 6, 4, 3, 5), "AI inference"),
    ("EE2", "S", "The gateway trusts Microsoft 365 Copilot's fixed outbound addresses without checking the caller, so a caller from another Copilot tenant on those addresses gets in.",
     ["ctrl-m365-network", "ctrl-identity"], ["CA", "APIM"], (6, 5, 4, 5, 5), "V170 V174; the claim that the addresses are shared across tenants is AI inference"),
    ("EE2", "R", "A user denies approving a write tool call; the write approval is stored only in the product.",
     ["ctrl-g-write-approval", "ctrl-purview-audit"], ["PURVAUDIT", "DSPM"], (3, 5, 3, 2, 4), "V164; where the approval is stored is AI inference"),
    ("EE3", "S", "An attacker with a stolen approver or admin account approves a server in Git or in the admin center.",
     ["ctrl-inventory", "ctrl-m365"], ["PIM", "CA"], (8, 3, 4, 7, 4), "AI inference"),
    ("EE3", "R", "An admin changes the Microsoft 365 admin center by hand and the change is not recorded in the repository.",
     ["ctrl-m365", "gap-m365-by-hand"], ["PURVAUDIT", "M365AGENTS"], (5, 7, 3, 4, 7), "V171, gap-m365-by-hand"),
    ("EE4", "S", "A server with a look-alike address matches an allowlist wildcard and is treated as approved.",
     ["ctrl-client", "ctrl-inventory"], [OUTSIDE], (7, 4, 5, 5, 4), "V17"),
    ("EE4", "R", "Nobody can show what an unapproved server received, because the server is outside the company logs.",
     ["ctrl-logging"], ["SENCONN", "FW"], (4, 8, 3, 3, 6), "AI inference"),

    # P1 Sync pipeline
    ("P1", "S", "An attacker uses a leaked pipeline credential to write a list to a policy target.",
     ["ctrl-pipeline"], ["MI", "KVACC"], (8, 4, 4, 7, 4), "AI inference"),
    ("P1", "T", "A pull request that edits the pipeline itself adds the attacker's server to every target.",
     ["ctrl-inventory", "ctrl-pipeline"], ["IAC"], (9, 4, 4, 8, 4), "AI inference"),
    ("P1", "R", "The pipeline writes to a target and keeps no run record that ties the change to a reviewed commit.",
     ["ctrl-pipeline"], ["IAC", "SENAUTO"], (4, 6, 3, 4, 5), "ctrl-pipeline"),
    ("P1", "I", "Pipeline run logs print target credentials or the full approved list.",
     ["ctrl-pipeline"], ["KVSCAN", "KVACC"], (6, 4, 4, 5, 4), "AI inference"),
    ("P1", "D", "The pipeline fails for one target and the list there goes stale; managed settings also refresh only about hourly.",
     ["ctrl-pipeline"], ["SENAUTO"], (5, 6, 3, 6, 5), "V90"),
    ("P1", "E", "One pipeline credential can write all targets, so a leak in one target reaches the others.",
     ["ctrl-pipeline"], ["RBAC", "MI"], (8, 4, 4, 7, 3), "ctrl-pipeline"),

    # P2 Managed client
    ("P2", "S", "A user-started local stdio server uses a command name that looks like an approved one.",
     ["ctrl-stdio"], [OUTSIDE], (6, 4, 4, 3, 4), "V18"),
    ("P2", "T", "The user reaches a server through a custom agent profile or the built-in GitHub server, which the lists do not cover.",
     ["gap-github-builtin", "ctrl-client"], [OUTSIDE], (6, 8, 7, 6, 7), "V20 V21"),
    ("P2", "T", "A local server package that was clean is updated with a backdoor, and the client installs the new version on its own.",
     ["ctrl-stdio"], [OUTSIDE], (7, 6, 5, 5, 4), "AI inference"),
    ("P2", "R", "A local MCP process on a device where Defender for Endpoint runtime protection is not active leaves no record, so a bypass cannot be traced to a person.",
     ["ctrl-logging", "ctrl-g-defender-for-endpoint-runtime-protection"], ["SENCONN", "CSPM"], (4, 6, 3, 4, 4), "V146 says local agents are covered through Defender for Endpoint; the unenrolled-device case is AI inference"),
    ("P2", "I", "With Allow all, a tool call sends files or secrets to an approved but over-permissioned server without a prompt.",
     ["ctrl-g-approval-lock", "ctrl-g-confirmation-dialog"], [OUTSIDE], (8, 6, 6, 4, 5), "V152 V157"),
    ("P2", "D", "A Windows rule that blocks all unmatched outbound traffic also blocks normal work and breaks the device.",
     ["ctrl-windows", "gap-windows-outbound"], ["FW", "NSG"], (5, 6, 2, 6, 6), "V32 V34"),
    ("P2", "E", "A local administrator turns off the managed policy or an unmanaged client runs the same server.",
     ["ctrl-stdio", "ctrl-client"], ["RBAC", "PIM"], (7, 5, 3, 3, 4), "AI inference"),
    ("P2", "E", "A local MCP tool or library runs input from an untrusted source as a command on the device: a crafted sign-in address from a server, or a request from a web page to an open local proxy.",
     ["ctrl-stdio", "ctrl-client"], [OUTSIDE], (9, 6, 5, 5, 5), "AI inference"),

    # P3 Cloud agents
    ("P3", "S", "An agent without a Microsoft Entra agent ID is outside Defender rule scope and is taken for a covered agent.",
     ["ctrl-g-defender-rules-and-scope"], ["AGENTCA", "AGENTACC"], (6, 6, 4, 4, 4), "V145"),
    ("P3", "T", "Hidden text in an external document steers the agent to call a tool the user did not intend.",
     ["ctrl-g-prompt-attack-block", "ctrl-g-untrusted-results"], ["GUARD", "RTP"], (8, 6, 6, 6, 8), "V107 V110"),
    ("P3", "R", "A Foundry tool call has no audit entry: Purview shows prompts and responses, not tool calls.",
     ["ctrl-purview-audit", "ctrl-logging"], ["PURVAUDIT", "DSPM"], (5, 7, 3, 5, 6), "V208 covers prompts and responses; that tool calls are not captured is AI inference, the Purview pages do not name MCP"),
    ("P3", "I", "A compromised agent sends secrets out through an MCP tool argument.",
     ["ctrl-g-defender-rules-and-scope", "ctrl-g-defender-real-time-protection"], ["RTP", "DSPM", "SHAREPOINT"], (8, 5, 5, 5, 5), "V125"),
    ("P3", "D", "An agent loop calls a tool without limit and uses up the gateway rate limit and the backend.",
     ["ctrl-gateway"], ["APIM"], (5, 6, 5, 6, 6), "V3"),
    ("P3", "E", "A Foundry MCP connection with an empty allowed tool list lets the agent call every tool, including write tools.",
     ["ctrl-foundry", "ctrl-g-approval"], ["GUARD", "AGENTACC"], (8, 7, 6, 5, 6), "V69"),

    # P4 Gateway
    ("P4", "S", "The gateway lets a caller pass on its source address alone, without a valid token.",
     ["ctrl-identity", "ctrl-m365-network"], ["CA", "APIM"], (8, 4, 5, 6, 5), "V174"),
    ("P4", "T", "Someone changes a gateway policy, or the Agent 365 consent lets a service write API-scoped policies.",
     ["ctrl-a365-consent", "ctrl-a365"], ["PIM", "OAUTH", "POLICY"], (8, 3, 4, 7, 3), "V39 V40"),
    ("P4", "R", "Gateway logs miss fields or expire early, so a tool call cannot be shown later.",
     ["ctrl-logging", "ctrl-gateway"], ["SENCONN", "SENRET"], (5, 5, 3, 5, 5), "V3"),
    ("P4", "I", "Gateway logs store tool arguments with personal data, or a shared backend connection exposes its permissions to every caller.",
     ["ctrl-ai-publish", "ctrl-logging"], ["KVACC", "MI", "DSPM"], (6, 5, 4, 5, 4), "V79"),
    ("P4", "D", "A flood against the single gateway stops every client; the AI Gateway preview also has one region pair and no private frontend.",
     ["ctrl-gateway", "ctrl-ai-limits"], ["APIM", "WAF"], (7, 5, 5, 8, 6), "V47 V52"),
    ("P4", "E", "A caller on a shared backend connection gets the connection's permissions, not its own.",
     ["ctrl-ai-publish"], ["MI", "RBAC"], (7, 5, 4, 5, 3), "V79"),

    # P5 Company MCP server
    ("P5", "S", "The backend accepts a token that has the wrong audience or comes from another identity than the gateway.",
     ["ctrl-identity", "ctrl-backend"], ["APPID", "FUNC", "MI"], (8, 4, 4, 5, 4), "AI inference"),
    ("P5", "T", "A tool argument carries a command or query that the server runs; no page control checks inputs at the server.",
     ["ctrl-g-tool-call-hook"], ["APIM", "WAF"], (9, 5, 5, 5, 5), "AI inference, not a page control"),
    ("P5", "R", "The server logs only the gateway identity, so it cannot tell which client or person asked.",
     ["ctrl-identity", "ctrl-logging"], ["SENCONN", "SENRET"], (4, 6, 3, 4, 4), "AI inference"),
    ("P5", "I", "The backend stays reachable on a public address and returns data to anyone with a token.",
     ["ctrl-backend"], ["PE", "FUNC", "ENTRAPA"], (9, 5, 5, 7, 4), "V9 V11"),
    ("P5", "I", "The server joins a caller-supplied path or address to its cloud API base address, so its own cloud token goes to a host the attacker picks.",
     ["ctrl-backend", "ctrl-identity"], ["FUNC", "RBAC"], (8, 5, 5, 6, 4), "AI inference"),
    ("P5", "D", "On a classic Consumption plan there are no private endpoints, so a direct flood reaches the server.",
     ["ctrl-backend"], ["PE", "FUNC", "FW"], (6, 5, 4, 6, 4), "V13"),
    ("P5", "E", "The gateway's identity or the server's own account has more rights than the approved tools need.",
     ["ctrl-identity", "ctrl-ai-publish"], ["RBAC", "MI"], (8, 4, 3, 5, 3), "AI inference"),

    # P6 Defender and threat detection (preview)
    ("P6", "S", "The external threat detection service for Copilot Studio is replaced by one that always answers allow.",
     ["ctrl-g-threat-detection"], ["RTP", "OAUTH"], (6, 3, 3, 4, 3), "V112 V113"),
    ("P6", "T", "An attacker hides intent so the check misses it; the unsafe email scenario is checked only at the tool request.",
     ["ctrl-g-defender-rules-and-scope"], ["RTP", "GUARD"], (6, 5, 5, 5, 5), "V144"),
    ("P6", "R", "The default Defender rule only audits, and nobody reads the audit.",
     ["ctrl-g-defender-rules-and-scope", "ctrl-logging"], ["AIDASH", "SENAUTO"], (4, 7, 2, 5, 6), "V123"),
    ("P6", "I", "Copilot Studio shares agent data with the threat detection provider.",
     ["ctrl-g-threat-detection"], ["DSPM"], (5, 8, 2, 4, 6), "V140"),
    ("P6", "D", "If the Copilot Studio provider is silent for one second, the call goes ahead by default, so an outage turns the check off.",
     ["ctrl-g-threat-detection"], ["RTP"], (7, 6, 4, 5, 5), "V114"),
    ("P6", "E", "Tool threat protection in Audit mode fails open, so a denied call still runs.",
     ["ctrl-ttp-modes", "ctrl-ttp-users"], ["AIGW", "GUARD"], (7, 6, 4, 4, 4), "V55 V59"),

    # D1 Approved list
    ("DS1", "T", "A direct push or an unreviewed merge changes the approved list.",
     ["ctrl-inventory"], ["IAC", "POLICY"], (9, 4, 4, 8, 4), "ctrl-inventory"),
    ("DS1", "R", "Squashed or unsigned commits hide who proposed a server.",
     ["ctrl-inventory"], ["IAC"], (3, 5, 3, 2, 5), "AI inference"),
    ("DS1", "I", "The list names internal server addresses, owners and risk classes to everyone who can read the repository.",
     ["ctrl-inventory"], ["KVSCAN"], (4, 7, 2, 4, 6), "AI inference"),
    ("DS1", "D", "The repository is deleted or unavailable, so no change can reach the targets.",
     ["ctrl-inventory", "ctrl-pipeline"], ["POLICY"], (4, 3, 3, 5, 3), "AI inference"),

    # D2 Policy targets
    ("DS2", "T", "A manual edit in a target (Foundry portal, admin center) drifts from the Git list.",
     ["ctrl-pipeline", "ctrl-m365", "gap-m365-by-hand"], ["M365AGENTS", "POLICY"], (6, 7, 4, 5, 6), "V171"),
    ("DS2", "R", "Target changes made by hand carry no link to a reviewed request.",
     ["ctrl-m365", "ctrl-logging"], ["PURVAUDIT"], (4, 7, 3, 4, 6), "gap-m365-by-hand"),
    ("DS2", "I", "A readable target shows the full set of approved servers.",
     ["ctrl-inventory"], [OUTSIDE], (3, 6, 3, 3, 5), "AI inference"),
    ("DS2", "D", "A wrong switch, such as turning off every MCP server in Copilot policy, stops all users at once.",
     ["gap-github-builtin"], [OUTSIDE], (6, 4, 3, 8, 4), "V93"),

    # D3 Logs and audit
    ("DS3", "T", "An attacker with log access deletes or edits gateway entries.",
     ["ctrl-logging"], ["SENRET", "RBAC"], (6, 3, 3, 5, 3), "AI inference"),
    ("DS3", "R", "Client side telemetry is missing for unmanaged devices and cloud agents outside the device rules.",
     ["ctrl-logging"], ["SENCONN", "PURVAUDIT"], (5, 6, 3, 5, 5), "AI inference"),
    ("DS3", "I", "Logs hold tool arguments and results with personal or secret data, readable by a wide group.",
     ["ctrl-logging"], ["SENRET", "DSPM", "RBAC"], (6, 6, 4, 5, 4), "AI inference"),
    ("DS3", "D", "Retention ends or ingestion stops, so the review of unapproved connections has nothing to read.",
     ["ctrl-logging"], ["SENRET", "SENCONN"], (5, 5, 2, 5, 5), "AI inference"),

    # F1 Policy sync
    ("F1", "T", "A policy file or API call is altered on its way to a target.",
     ["ctrl-pipeline"], ["IAC"], (7, 2, 2, 6, 2), "AI inference"),
    ("F1", "I", "Target credentials or the list leak in transit or in the run log.",
     ["ctrl-pipeline"], ["KVACC", "KVSCAN"], (6, 3, 3, 5, 3), "AI inference"),
    ("F1", "D", "An automated write to Power Platform policy may fail or do nothing for MCP settings, because the source does not show that they can be set through the API.",
     ["ctrl-power-platform"], [OUTSIDE], (4, 6, 2, 4, 6), "V66 describes the API in general; the MCP case is AI inference"),

    # F2 Tool call to gateway
    ("F2", "T", "A call in transit is changed to point at another tool or add arguments.",
     ["ctrl-gateway"], ["APIM", "WAF"], (6, 2, 2, 4, 2), "AI inference"),
    ("F2", "I", "A bearer token or tool argument leaks through a log, a proxy or a shared link.",
     ["ctrl-identity", "ctrl-logging"], ["CA", "KVSCAN"], (7, 4, 3, 4, 4), "V51"),
    ("F2", "D", "Microsoft changes the fixed outbound address list with seven days' notice, and calls from Microsoft 365 Copilot start to fail.",
     ["ctrl-m365-network"], ["APIM", "NSG"], (5, 4, 3, 6, 6), "V175"),

    # F3 Gateway to server
    ("F3", "T", "Traffic from the gateway to the server crosses a public path and is changed.",
     ["ctrl-backend"], ["PE", "NSG"], (7, 3, 3, 6, 3), "V9"),
    ("F3", "I", "Gateway to server traffic is read on a public path.",
     ["ctrl-backend"], ["PE", "ENTRAPA"], (7, 3, 3, 6, 3), "V9"),
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
    ("F5", "T", "A client calls the backend by IP address or from a cloud-hosted agent and skips every gateway rule.",
     ["ctrl-backend", "ctrl-windows"], ["PE", "NSG", "FW"], (9, 5, 5, 6, 5), "AI inference, acceptance test 12"),
    ("F5", "I", "A direct call skips gateway logging and sends company data out with no record.",
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
# Links were checked on 2026-11-12 (NVD API, CISA KEV file, vendor pages). The match to a threat is AI judgement.
NVD = "https://nvd.nist.gov/vuln/detail/"
LEVELS = ("exploited", "disclosed", "theoretical")
OBSERVED = {
    "S8": [("exploited", "CVE-2026-59822 LiteLLM MCP endpoint accepts any bearer token (CISA KEV, added 2026-09-02)", NVD + "CVE-2026-59822"),
              ("disclosed", "CVE-2026-33032 nginx-ui MCP message endpoint skips authentication when the IP allowlist is empty", NVD + "CVE-2026-33032")],
    "E5": [("exploited", "CVE-2026-42271 LiteLLM MCP test endpoints let an authenticated user run commands on the gateway (CISA KEV, added 2026-06-08)", NVD + "CVE-2026-42271"),
              ("disclosed", "CVE-2026-109492 Microsoft MCP Gateway authorization bypass through a user-controlled key raises privileges (published 2026-11-10)", NVD + "CVE-2026-109492")],
    "I14": [("disclosed", "Asana MCP server bug could have shown one customer's data to other MCP users (found 2025-06-04, vendor says no confirmed access)",
              "https://theregister.com/2025/06/18/asana_mcp_server_bug/"),
              ("disclosed", "CVE-2026-48529 GitHub MCP Server in HTTP lockdown mode runs later users' queries with the first user's credentials", NVD + "CVE-2026-48529"),
              ("disclosed", "CVE-2026-52869 MCP Python SDK serves a session to any caller that knows the session ID, whatever token it carries", NVD + "CVE-2026-52869"),
              ("disclosed", "CVE-2026-25536 MCP TypeScript SDK leaks response data across clients when one server and transport instance is reused", NVD + "CVE-2026-25536")],
    "I6": [("disclosed", "CVE-2026-58201 Lokka (Microsoft 365 MCP server) sends an Azure Resource Manager bearer token to an unintended host through a crafted path", NVD + "CVE-2026-58201"),
              ("disclosed", "CVE-2026-63127 rmcp (Rust MCP SDK) client sends a valid access token to a malicious MCP server that publishes another server's metadata", NVD + "CVE-2026-63127")],
    "I5": [("disclosed", "CVE-2026-114123 D365 Finance and Operations MCP Server: the documented Azure deploy leaves the API key empty and the server listens on all addresses", NVD + "CVE-2026-114123")],
    "S9": [("disclosed", "CVE-2026-32211 Azure MCP Server missing authentication", NVD + "CVE-2026-32211"),
              ("disclosed", "CVE-2026-116684 MCP Python SDK bearer check accepts a token issued for a different resource server", NVD + "CVE-2026-116684")],
    "T6": [("disclosed", "CVE-2025-68143 mcp-server-git accepted arbitrary filesystem paths", NVD + "CVE-2025-68143"),
              ("disclosed", "CVE-2026-33980 Azure Data Explorer MCP Server runs a query built from a tool argument (KQL injection)", NVD + "CVE-2026-33980"),
              ("disclosed", "CVE-2025-53355 mcp-server-kubernetes command injection", NVD + "CVE-2025-53355"),
              ("disclosed", "CVE-2025-53967 Framelink Figma MCP Server runs operating system commands from a crafted request", NVD + "CVE-2025-53967"),
              ("disclosed", "CVE-2025-68144 mcp-server-git passes user-controlled arguments to git without sanitizing", NVD + "CVE-2025-68144"),
              ("disclosed", "CVE-2025-66689 Zen MCP Server path traversal reads arbitrary files", NVD + "CVE-2025-66689"),
              ("disclosed", "CVE-2025-67366 filesystem-mcp path traversal", NVD + "CVE-2025-67366")],
    "E6": [("disclosed", "CVE-2026-26118 Azure MCP Server request forgery that raises privileges", NVD + "CVE-2026-26118"),
              ("disclosed", "CVE-2026-27826 mcp-atlassian lets an unauthenticated caller force outbound requests", NVD + "CVE-2026-27826"),
              ("disclosed", "CVE-2026-8355 IBM ContextForge MCP Gateway: a user-supplied token address makes the gateway send requests to internal hosts and cloud metadata", NVD + "CVE-2026-8355"),
              ("disclosed", "CVE-2025-65513 fetch-mcp SSRF bypasses the private IP check", NVD + "CVE-2025-65513")],
    "T4": [("disclosed", "CVE-2025-32711 EchoLeak, hidden prompt in Microsoft 365 Copilot", NVD + "CVE-2025-32711")],
    "I3": [("disclosed", "CVE-2025-32711 EchoLeak, data leaves through a crafted prompt", NVD + "CVE-2025-32711")],
    "T14": [("disclosed", "Invariant Labs demo: GitHub MCP issue text steers the agent to leak private repo data (2025-05-26)",
              "https://invariantlabs.ai/blog/mcp-github-vulnerability")],
    "E2": [("disclosed", "CVE-2025-53773 GitHub Copilot and Visual Studio command injection through prompt injection", NVD + "CVE-2025-53773"),
              ("disclosed", "CVE-2026-29783 GitHub Copilot CLI shell tool runs hidden commands after prompt injection", NVD + "CVE-2026-29783"),
              ("disclosed", "CVE-2026-30615 Windsurf prompt injection in HTML registers a malicious MCP STDIO server and runs commands", NVD + "CVE-2026-30615"),
              ("disclosed", "CVE-2026-30623 LiteLLM MCP server creation from a JSON config allows remote code execution", NVD + "CVE-2026-30623"),
              ("disclosed", "CVE-2026-40933 Flowise MCP adapter unsafe stdio command serialization", NVD + "CVE-2026-40933")],
    "E3": [("disclosed", "CVE-2025-6514 mcp-remote runs a command from a server's sign-in address", NVD + "CVE-2025-6514"),
              ("disclosed", "CVE-2025-49596 MCP Inspector runs code for unauthenticated requests", NVD + "CVE-2025-49596"),
              ("disclosed", "CVE-2025-9611 Microsoft Playwright MCP Server accepts web-page requests by DNS rebinding", NVD + "CVE-2025-9611"),
              ("disclosed", "CVE-2025-66416 MCP Python SDK leaves DNS rebinding protection off by default for local HTTP servers", NVD + "CVE-2025-66416"),
              ("disclosed", "CVE-2025-59163 vet local server lacks Host and Origin checks, DNS rebinding", NVD + "CVE-2025-59163"),
              ("disclosed", "CVE-2025-66414 MCP TypeScript SDK lacks DNS rebinding protection by default", NVD + "CVE-2025-66414")],
    "T2": [("disclosed", "CVE-2025-54136 Cursor runs a changed MCP config that was already trusted", NVD + "CVE-2025-54136")],
    "T3": [("exploited", "postmark-mcp npm package backdoored, confirmed by Postmark",
               "https://postmarkapp.com/blog/information-regarding-malicious-postmark-mcp-package"),
              ("disclosed", "GitHub malware advisory: npm mcp-server-github squats the official name (published 2026-08-20)", "https://github.com/advisories/GHSA-95pj-hrh5-27gq")],
}


def level_of(tid):
    refs = OBSERVED.get(tid, [])
    for lv in LEVELS:
        if any(r[0] == lv for r in refs):
            return lv
    return "theoretical"


def adjust(tid, dr):
    """Raise D-R-E-A-Di scores only where a public record exists. AI estimate rule, not a measurement."""
    d, r, e, a, di = dr
    lv = level_of(tid)
    if lv != "theoretical":
        di = max(di, 7)
    if lv == "exploited":
        r, e = max(r, 7), max(e, 7)
    return (d, r, e, a, di)
