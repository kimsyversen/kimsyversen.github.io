"""Evidence for the interactive MCP design, including page-only review quotes.

python3 -I scripts/check-evidence-quotes.py <cache> mcp_governance_interactive_evidence mcp-governance-microsoft-interactive.html
"""
from mcp_governance_evidence import SOURCES as SHARED_SOURCES, QUOTES as SHARED_QUOTES, PREVIEW_ONLY as SHARED_PREVIEW

CHECKED = "2026-11-12"
UNAVAILABLE = {"pv-aig-separate": "Overview URL could not be retrieved on 2026-11-12; retained for anchor history, not used by active claims."}
SOURCES = dict(SHARED_SOURCES)
QUOTES = list(SHARED_QUOTES)
IDS = {key: f"V{i}" for i, (key, _, _) in enumerate(QUOTES, 1)}
PREVIEW_ONLY = set(SHARED_PREVIEW) | {"gr-fy-call", "gr-fy-resp"}
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
    "a365-byo": "2026-11-05",
    "a365-gw": "2026-11-06",
    "fy-gov-tools": "2026-08-19",
    "fy-aig-cfg": "2026-08-06",
    "apim-mcp": "2026-09-11",
    "fy-gr-ip": "2026-03-02",
    "fy-hosted": "2026-11-11",
    "cs-ext": "2026-06-01",
    "def-rt": "2026-10-15",
    "fy-gr-ov": "2026-10-20",
    "cs-tools": "2026-10-01",
    "m365-manage": "2026-10-16",
    "m365-custom": "2026-10-19",
    "m365-net": "2026-10-28",
    "a365-ov": "2026-08-20",
    "a365-tools": "2026-10-13",
    "a365-admin-tools": "2026-10-23",
    "a365-agent-registry": "2026-10-23",
    "a365-agent-requests": "2026-10-23",
    "purview-a365": "2026-05-01",
    "purview-dspm": "2026-05-26",
    "purview-foundry": "2026-05-01"
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

