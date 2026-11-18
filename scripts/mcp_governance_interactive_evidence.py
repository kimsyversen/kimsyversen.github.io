"""Evidence for the interactive MCP design, including page-only review quotes.

python3 -I scripts/check-evidence-quotes.py <cache> mcp_governance_interactive_evidence mcp-governance-microsoft-interactive.html
"""
from mcp_governance_evidence import SOURCES as SHARED_SOURCES, QUOTES as SHARED_QUOTES, PREVIEW_ONLY as SHARED_PREVIEW

CHECKED = "2026-11-18"
UNAVAILABLE = {}
SOURCES = dict(SHARED_SOURCES)
QUOTES = list(SHARED_QUOTES)
# Source wording changed after the shared list was written; the page-only list follows the live text.
_LIVE = {
    "pv-byo-roll": "Individual tool blocking for BYO MCP servers is planned for a future release. Tool-level controls are rolling out for other supported MCP server types registered on Agent 365.",
    "pv-byo-tool-plan": "Individual tool blocking for BYO MCP servers is planned for a future release.",
    "pv-fy-prev": "Foundry no longer performs this registration or updates the endpoint automatically.",
    "pv-fy-new": "You configure or register the MCP route in your chosen gateway first. Then, you add or update the Foundry tool with the gateway-routed endpoint.",
    "pv-gr-fy-list": "Currently, the following tools support moderation: Foundry IQ (Azure AI Search), Azure Functions, OpenAPI, Sharepoint Grounding, Fabric Data Agent, Bing Grounding, Bing Custom Search, and Browser Automation.",
    "gr-fy-agprev": "Agent guardrails for content safety in Foundry Agent Service are in preview.",
    "gr-cs-ask": "Asks the user to confirm before the tool runs. Set to No by default.",
    "fy-aig-apim": "The hub publishes approved models through stable aliases and exposes gateway-routed tool endpoints to Foundry project spokes.",
    "fy-aig-new": "You can no longer create new API Management links from Foundry.",
    "fy-aig-v2": "API Management service tiers, including v1 and v2 tiers, can act as the hub.",
    "fy-aig-same": "Existing API Management configurations and traffic continue to work.",
    "fy-aig-prod": "Configure API Management in the Azure portal or through code, and use connected models for project consumption.",
    "pv-fy-aig-only-mcp": "When a project connection endpoint differs from server_url , Foundry uses the project connection endpoint.",
    "gh-fw": "In cloud sandboxes, it also applies to the built-in Playwright Model Context Protocol (MCP) server and its browser processes, so browser network requests are subject to the configured firewall rules. The firewall does not apply directly to other MCP servers, including repository-configured replacements for the built-in Playwright server, or to processes started in configured Copilot setup steps.",
    "a365-ga": "Microsoft Agent 365 is generally available for the Commercial segment on a per user basis.",
}
QUOTES = [(k, s, _LIVE.get(k, q)) for k, s, q in QUOTES]
IDS = {key: f"V{i}" for i, (key, _, _) in enumerate(QUOTES, 1)}
PREVIEW_ONLY = (SHARED_PREVIEW - {"pv-fy-prev", "pv-fy-new", "pv-fy-aig-only-mcp"}) | {"gr-fy-call", "gr-fy-resp"}
# Page-only quotes append to the shared list to preserve published V ids.
SOURCES.update({
    "purview-a365": ("Microsoft Learn, use Microsoft Purview for Microsoft Agent 365",
                     "https://learn.microsoft.com/en-us/purview/ai-agent-365", "2026-05-01"),
    "purview-dspm": ("Microsoft Learn, learn about Microsoft Purview Data Security Posture Management",
                     "https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about", "2026-05-26"),
    "purview-foundry": ("Microsoft Learn, use Microsoft Purview for Microsoft Foundry",
                        "https://learn.microsoft.com/en-us/purview/ai-azure-foundry", "2026-05-01"),
})
for _key, _skey, _q in [
    ("purview-audit-on", "purview-a365", "When you create an agent instance for Agent 365, it's automatically enabled for audit"),
    ("purview-audit-tools", "purview-a365", "Supported interactions: All agent-to-human, human-to-agent, agent-to-tools, and agent-to-agent interactions."),
    ("purview-audit-search", "purview-a365", "search the audit log for Agent 365 activities"),
    ("purview-dlp-scope", "purview-a365", "Block or audit agent-to-human and human-to-agent for Microsoft Teams, OneDrive or SharePoint, and emails."),
    ("purview-dspm-inventory", "purview-dspm", "An inventory of all AI apps and agents (including recently released Microsoft Agent 365) with activity in the last 30 days"),
    ("purview-foundry-audit", "purview-foundry", "prompts and responses are captured in the unified audit log"),
]:
    if _key in IDS:
        raise ValueError(f"duplicate quote key: {_key}")
    QUOTES.append((_key, _skey, _q))
    IDS[_key] = f"V{len(QUOTES)}"

# Additional review evidence; append so existing public V ids remain stable.
SOURCES["review-obo"] = ("Microsoft Learn, OAuth 2.0 on-behalf-of flow", "https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow", None)
for _key, _source, _quote in [
    ("review-account", "gh-deploy", "Server-managed settings are associated with the user's signed-in account."),
    ("review-local-policy", "gh-deploy", "remain active when users switch accounts"),
    ("review-obo", "review-obo", "the intent is to pass a user's identity and permissions through the request chain."),
    ("review-purview-setup", "purview-foundry", "Before Microsoft Purview can manage these AI interactions, ensure you perform either of the following configuration steps:"),
]:
    QUOTES.append((_key, _source, _quote))
    IDS[_key] = f"V{len(QUOTES)}"
PREVIEW_ONLY |= {"gr-fy-agprev"}

SOURCES["a365-agent-details"] = (SOURCES["a365-agent-details"][0], "https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-details", None)
# Source dates are displayed only when retrieved during the current review.
VERIFIED_SOURCE_DATES = {
    "azmcp-sec": "2026-07-31",
    "apim-sec": "2026-09-11",
    "apim-mi": "2026-10-22",
    "apim-a365": "2026-10-06",
    "func-net": "2026-09-16",
    "fy-tb": "2026-10-26",
    "studio": "2026-10-22",
    "gsa-fw": "2026-08-06",
    "intune-fw": "2026-04-15",
    "win-dk": "2025-04-07",
    "aig-ov": "2026-10-28",
    "aig-res": "2026-10-28",
    "aig-con": "2026-10-28",
    "aig-ttp": "2026-10-28",
    "a365-byo": "2026-11-16",
    "a365-gw": "2026-11-06",
    "fy-gov-tools": "2026-11-17",
    "pp-acp": "2026-09-09",
    "pp-acp-api": "2026-10-02",
    "fy-mcp": "2026-11-17",
    "apim-genai": "2026-05-29",
    "ai-gw-ov": "2026-10-28",
    "fy-aig-cfg": "2026-11-17",
    "apim-mcp": "2026-09-11",
    "fy-gr-ip": "2026-03-02",
    "fy-gr-how": "2026-10-15",
    "fy-hosted": "2026-11-11",
    "cs-ext": "2026-06-01",
    "cs-sec": "2026-11-05",
    "def-rt": "2026-10-15",
    "fy-gr-ov": "2026-11-17",
    "cs-tools": "2026-11-17",
    "mde-rt": "2026-11-17",
    "mde-matrix": "2026-11-12",
    "m365-fed": "2026-11-16",
    "m365-manage": "2026-10-16",
    "m365-custom": "2026-10-19",
    "m365-net": "2026-10-28",
    "a365-ov": "2026-11-12",
    "a365-tools": "2026-10-13",
    "a365-admin-tools": "2026-11-16",
    "a365-agent-registry": "2026-11-06",
    "a365-agent-details": "2026-10-23",
    "a365-agent-requests": "2026-10-23",
    "purview-a365": "2026-05-01",
    "purview-dspm": "2026-05-26",
    "purview-foundry": "2026-05-01",
    "review-obo": "2025-01-04",
}
SOURCES = {key: (title, url, VERIFIED_SOURCE_DATES.get(key)) for key, (title, url, _date) in SOURCES.items()}

for _key, _source, _quote in [
    ("review-ttp-discovery", "aig-ttp", "Tool discovery and session-management operations don't invoke tools and aren't evaluated."),
    ("review-acp-mixed", "pp-acp", "ACP runs alongside classic data policies, and the most restrictive settings from both are enforced."),
    ("review-ttp-retry", "aig-ttp", "Don't automatically retry a tool call when the response says that the tool ran but its result was withheld."),
]:
    QUOTES.append((_key, _source, _quote))
    IDS[_key] = f"V{len(QUOTES)}"
PREVIEW_ONLY |= {"review-ttp-discovery", "review-ttp-retry"}

QUOTES.append(("review-acp-rollout", "pp-acp", "Each maker portal's release of design-time enforcement for ACP marks the general availability of ACP for that workload."))
IDS["review-acp-rollout"] = f"V{len(QUOTES)}"

QUOTES.append(("review-def-local-sep", "def-rt", "Local agents are onboarded separately from cloud agents."))
IDS["review-def-local-sep"] = f"V{len(QUOTES)}"

QUOTES.append(("review-obo-token", "review-obo", "For the middle-tier service to make authenticated requests to the downstream service, it needs to secure an access token from the Microsoft identity platform."))
IDS["review-obo-token"] = f"V{len(QUOTES)}"

for _key, _skey, _q in [
    ("review-ttp-example", "aig-ttp", "For example, MCP initialize , tools/list , and notifications don't trigger an evaluation."),
    ("review-req-fields", "a365-admin-tools", "Review the server name, publisher, requester, and request date."),
    ("review-req-info", "a365-admin-tools", "Review the server information and declared tools for accuracy and compliance."),
]:
    QUOTES.append((_key, _skey, _q))
    IDS[_key] = f"V{len(QUOTES)}"
PREVIEW_ONLY |= {"review-ttp-example"}

QUOTES.append(("review-gh-private", "gh-deploy", "Server-managed (.github-private repository)"))
IDS["review-gh-private"] = f"V{len(QUOTES)}"
QUOTES.append(("review-req-queue", "a365-admin-tools", "To review and approve MCP server registration requests, follow these steps:"))
IDS["review-req-queue"] = f"V{len(QUOTES)}"
QUOTES.append(("review-custom-classic", "pp-acp", "For governing custom connectors and HTTP connectors today, continue using classic data policies"))
IDS["review-custom-classic"] = f"V{len(QUOTES)}"

# Use canonical pages: the older firewall URL can serve an inconsistent snapshot.
SOURCES["gh-fw"] = (SOURCES["gh-fw"][0], "https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-the-firewall", None)
SOURCES["a365-agent-registry"] = (SOURCES["a365-agent-registry"][0], "https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry-overview", VERIFIED_SOURCE_DATES["a365-agent-registry"])
SOURCES.update({
    "m365-release": ("Microsoft Learn, Microsoft 365 Copilot release notes", "https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes", "2026-11-18"),
    "studio-kusto": ("Microsoft Learn, configure a FinOps hub agent in Copilot Studio", "https://learn.microsoft.com/en-us/cloud-computing/finops/toolkit/hubs/configure-ai-copilot-studio", "2026-05-18"),
})
for _key, _source, _quote in [
    ("review-gateway-admin", "a365-gw", "You must have the Global Administrator role to connect Azure AI Gateway. The AI Administrator role doesn't support this operation."),
    ("review-connector-override", "m365-manage", "A setting you make on an individual connector takes precedence over the bulk Agent and plugin access setting. User access always applies."),
    ("review-write-approval-scope", "m365-fed", "Always allow and Allow for conversation apply to the individual tool, not to the whole connector."),
    ("review-defender-scope", "def-rt", "Scope: Choose whether the rule applies to All agents or to specific agents."),
    ("fy-egress-ga", "fy-gr-ov", "Network egress controls are generally available, except for Transform rules, which remain in preview."),
    ("fy-egress-harness", "fy-gr-ov", "Prompt agents that use the Microsoft Copilot harness (preview) also support network egress controls."),
    ("fy-egress-exceptions", "fy-gr-ov", "Secret-backed header values and Azure Policy governance for hosted-agent egress guardrails remain in preview."),
    ("m365-researcher", "m365-fed", "The Researcher agent doesn't support write, update, or delete actions."),
    ("apim-mcp-scope", "apim-mcp", "API Management currently supports MCP server tools, but doesn't support MCP resources or prompts."),
    ("gh-cloud-settings", "gh-ref", "Cloud sessions can run in sandboxes or on GitHub Actions. Coverage of policies and enterprise managed settings currently varies between environments."),
    ("m365-fed-ga", "m365-release", "Microsoft is announcing the General Availability (GA) of federated Copilot connectors for Microsoft 365 Copilot."),
    ("studio-kusto-confirm", "studio-kusto", "Add Kusto Query MCP Server (by Azure Data Explorer) with these settings: Ask the end user before running: No"),
]:
    QUOTES.append((_key, _source, _quote))
    IDS[_key] = f"V{len(QUOTES)}"
PREVIEW_ONLY.add("review-gateway-admin")

# Keep the earlier migration guidance addressable for readers following published V links.
HISTORICAL = {"pv-pe", "pv-vnet", "pv-cs", "pv-domain", "pv-regions", "pv-gr-mde-pre", "pv-gr-mde-win"}
SOURCES.update({
    "ignite-gateway": ("Microsoft Azure, Azure AI Gateway general availability", "https://techcommunity.microsoft.com/blog/IntegrationsonAzureBlog/azure-ai-gateway-is-now-generally-available-ship-faster-stay-in-control/4572644", "2026-11-17"),
    "ignite-apim": ("Microsoft Azure, API Management at Ignite", "https://techcommunity.microsoft.com/blog/integrationsonazureblog/whats-new-in-azure-api-management-at-microsoft-ignite-2026/4574194", "2026-11-17"),
    "ignite-a365": ("Microsoft Agent 365, Ignite announcements", "https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-microsoft-agent-365-ignite-2026/4571753", "2026-11-17"),
    "apim-vnet-out": ("Microsoft Learn, outbound virtual network integration", "https://learn.microsoft.com/en-us/azure/api-management/integrate-vnet-outbound", None),
    "vs-hooks": ("Visual Studio Code, configure agent hooks", "https://code.visualstudio.com/docs/agent-customization/hooks", None),
    "studio-ga": ("Microsoft Copilot Studio, MCP general availability", "https://www.microsoft.com/en-us/copilot/blog/copilot-studio/model-context-protocol-mcp-is-now-generally-available-in-microsoft-copilot-studio/", "2025-05-29"),
    "studio-standard": ("Microsoft Learn, extend your agent with MCP", "https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp", None),
    "studio-copilot": ("Microsoft Learn, add an MCP server with the Microsoft Copilot harness", "https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/tools-add-mcp-server", None),
})
for _key, _source, _quote in [
    ("gateway-ga", "ignite-gateway", "general availability of Azure AI Gateway"),
    ("gateway-regions", "ignite-gateway", "available today in 17 Azure regions"),
    ("gateway-network", "ignite-gateway", "Private Link (preview) for inbound calls, VNet integration (preview) for private backends"),
    ("gateway-content", "ignite-gateway", "Screen prompts and responses with Azure AI Content Safety."),
    ("gateway-threat", "ignite-gateway", "Protection from poisoned tools (preview)"),
    ("apim-integration-ga", "ignite-apim", "The Microsoft Agent 365 integration with Azure API Management and Azure AI Gateway is now generally available"),
    ("a365-gateway-preview", "ignite-a365", "Azure AI Gateway and LiteLLM gateway support is in preview"),
    ("defender-windows-ga", "ignite-a365", "Now generally available on Windows, Defender inspects critical points in the agent loop"),
    ("apim-private", "apim-vnet-out", "The API Management instance can reach both public and network-isolated backend services."),
    ("apim-private-tiers", "apim-vnet-out", "APPLIES TO: Standard v2 | Premium v2"),
    ("vs-hook-preview", "vs-hooks", "Agent hooks is in preview"),
    ("studio-mcp-ga", "studio-ga", "general availability of MCP integration in Copilot Studio"),
    ("studio-standard", "studio-standard", "This article describes features used in agents or agent flows powered by the standard harness"),
    ("studio-copilot-preview", "studio-copilot", "Add a Model Context Protocol (MCP) server to your agent as a tool (Microsoft Copilot) (preview)"),
]:
    QUOTES.append((_key, _source, _quote))
    IDS[_key] = f"V{len(QUOTES)}"
PREVIEW_ONLY.difference_update(HISTORICAL | {"pv-aig-separate", "pv-res-change", "pv-res-date", "pv-res-removed", "pv-bearer",
                                            "pv-shared-cred", "pv-aig-comb", "pv-gr-mde-how", "pv-gr-mde-vs", "pv-gr-def-local", "review-def-local-sep"})
PREVIEW_ONLY.update({"gr-vs-hook", "gr-vs-hook-not", "vs-hook-preview", "gateway-network", "gateway-threat", "a365-gateway-preview", "studio-copilot-preview"})
