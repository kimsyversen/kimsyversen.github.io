"""Evidence quotes for Developer-WS2.html (Intune and MCP servers).

Shared by build-developer-ws2.py (writes the table) and check-developer-ws2.py
(confirms each quote appears in its source). Quotes already checked for the
enterprise agent governance pages are reused word for word from governance_evidence.py.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import governance_evidence as ge  # noqa: E402

CHECKED = ge.CHECKED  # 2026-11-06

_MS = "https://learn.microsoft.com/en-us/intune"

NEW_SOURCES = {
    "vs-pol": ("VS Code docs, enterprise policies",
               "https://code.visualstudio.com/docs/enterprise/policies", "none shown"),
    "in-admx": ("Microsoft Learn, import custom ADMX and ADML templates into Intune",
                f"{_MS}/device-configuration/settings-catalog/import-custom-admx-templates", "2026-07-01"),
    "in-mac": ("Microsoft Learn, custom settings for Apple devices in Intune",
               f"{_MS}/device-configuration/templates/configure-custom-settings-apple", "2026-07-01"),
    "in-rem": ("Microsoft Learn, remediations in Intune",
               f"{_MS}/device-management/tools/deploy-remediations", "2026-09-01"),
    "in-comp": ("Microsoft Learn, custom compliance settings in Intune",
                f"{_MS}/device-security/compliance/custom-settings", "2026-09-17"),
    "ac-intune": ("Microsoft Learn, App Control for Business policy and managed installers in Intune",
                  f"{_MS}/intune-service/protect/endpoint-security-app-control-policy", "2026-07-01"),
    "ac-win": ("Microsoft Learn, Application Control for Windows",
               "https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol", "2026-10-08"),
    "ac-script": ("Microsoft Learn, App Control script enforcement",
                  "https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/design/script-enforcement", "2026-11-02"),
    "ind-file": ("Microsoft Learn, file indicators in Defender for Endpoint",
                 "https://learn.microsoft.com/en-us/defender-endpoint/indicator-file", "2026-07-03"),
}

# Reused from the governance pages: (quote key, source key) pairs are taken from ge.QUOTES.
REUSE = [
    "gh-hour", "gh-builtin",
    "def-disc", "def-av", "def-cmd", "def-incomplete", "def-lic", "def-noproof",
    "fw-preview", "fw-remote", "fw-license", "fw-client", "fw-tls",
    "ifw-block", "ifw-ver", "dk-csp", "dk-dns", "dk-limits",
    "graph-cp",
]

NEW_QUOTES = [
    # Claude Code
    # VS Code
    ("vs-intune", "vs-pol", "use your MDM solution (for example, Microsoft Intune) to configure the imported VS Code administrative template policies."),
    ("vs-over", "vs-pol", "When a policy value is set, the value overrides the VS Code setting value configured at any level (default, user, and workspace)."),
    ("vs-allow", "vs-pol", "ChatAllowedMcpServers Allowlist of Model Context Protocol servers. When set, only servers matching an entry may be installed or run; omit entirely to allow all servers (subject to the deny list)."),
    ("vs-deny", "vs-pol", "ChatDeniedMcpServers Denylist of Model Context Protocol servers. Servers matching any entry are blocked from being installed or run, even if they also match the allow list; deny rules always take precedence."),
    ("vs-only", "vs-pol", "ChatAllowManagedMcpServersOnly Use only the enterprise-managed MCP allowlist when deciding which servers may run."),
    ("vs-admx", "vs-pol", "Starting from VS Code version 1.69, each release ships with a policies directory containing ADMX template files that define the available policies."),
    ("vs-pc", "vs-pol", "Computer-level policies take precedence over user-level policies when both are configured."),
    # GitHub Copilot managed settings
    ("gh-mdm", "gh-deploy", "Native MDM delivery is available on Windows and macOS"),
    ("gh-str", "gh-deploy", "All native MDM values must be strings."),
    ("gh-inter", "gh-ref", "the effective allowlist is the intersection of all sources. A server must be permitted by every source to run."),
    # Codex
    # Claude Desktop
    # Cursor
    # Intune delivery
    ("in-admx", "in-admx", "You can import custom and third-party/partner ADMX and ADML templates into the Intune admin center."),
    ("in-admx-prev", "in-admx", "Import custom ADMX and ADML administrative templates into Microsoft Intune (public preview)"),
    ("in-mac", "in-mac", "For macOS devices, the settings must be in an .xml or .mobileconfig file."),
    ("in-chan", "in-mac", "After you select a channel and save the profile, you can't change the channel."),
    ("in-rem-join", "in-rem", "Devices must be Microsoft Entra joined or Microsoft Entra hybrid joined"),
    ("in-rem-lic", "in-rem", "Windows Enterprise E3 or E5 (included in Microsoft 365 F3, E3, or E5)"),
    ("in-rem-miss", "in-rem", "If a scheduled run is missed, the remediation runs when the device is online, and as soon as possible."),
    ("in-comp-8h", "in-comp", "Checks for new or updated PowerShell scripts every eight hours. Runs discovery scripts every eight hours."),
    ("in-comp-os", "in-comp", "Windows devices use a PowerShell script. Linux and macOS devices use a POSIX-compliant shell script."),
]

# Added last so the ids of the quotes above keep their numbers.
LATE_QUOTES = [
    ("ac-intune", "ac-intune", "To help prevent undesired apps from running on your managed Windows devices, you can use Microsoft Intune App Control for Business policies"),
    ("ac-apps", "ac-win", "restricting the apps that users can run"),
    ("ac-code", "ac-win", "code runs only if your policy says so"),
    ("ind-mac", "ind-file", "Custom file indicators with the Allow, Block and Remediate actions are now also available in the enhanced anti-malware engine capabilities for macOS and Linux"),
    ("ind-block", "ind-file", "Blocking the file prevents it from being read, written, or executed on devices in your organization."),
    ("ind-types", "ind-file", "On macOS, file indicators support three types of files: Mach-O executables, POSIX shell scripts (e.g., those run by sh or bash), and AppleScript files (.scpt)."),
    ("ac-unenl", "ac-script", "App Control doesn't control scripts run through an unenlightened script host, such as many 3rd-party Java or Python engines."),
    ("ac-implicit", "ac-script", "If your App Control policy allows an unenlightened script host to run, then you implicitly allow all scripts run through that host."),
    ("vs-mac", "vs-pol", "Starting from VS Code version 1.99, each release ships with a sample .mobileconfig file."),
    ("vs-mac-intune", "vs-pol", "For enterprise deployments across multiple devices, use Mobile Device Management (MDM) solutions such as: Microsoft Intune"),
    ("vs-syntax", "vs-pol", "If there's a syntax error in the policy value, the setting will not be applied."),
]

SOURCES = dict(NEW_SOURCES)
_ge_q = {k: (s, q) for k, s, q in ge.QUOTES}
for _k in REUSE:
    _s, _q = _ge_q[_k]
    SOURCES.setdefault(_s, ge.SOURCES[_s])

QUOTES = list(NEW_QUOTES) + [(k, _ge_q[k][0], _ge_q[k][1]) for k in REUSE] + LATE_QUOTES
IDS = {key: f"V{i}" for i, (key, _, _) in enumerate(QUOTES, 1)}

# A text fragment cannot cross an HTML block (table cell, code line). For quotes that
# do, the link targets the longest piece that sits inside one block. The checker
# confirms each piece is inside one block of the source.
BLOCK_FRAGS = {
    "vs-allow": "Allowlist of Model Context Protocol servers. When set, only servers matching an entry may be installed or run; omit entirely to allow all servers (subject to the deny list).",
    "vs-deny": "Denylist of Model Context Protocol servers. Servers matching any entry are blocked from being installed or run, even if they also match the allow list; deny rules always take precedence.",
    "vs-only": "Use only the enterprise-managed MCP allowlist when deciding which servers may run.",
    "in-comp-8h": "Checks for new or updated PowerShell scripts every eight hours.",
    "fw-remote": "Only remote MCP servers are inspected. Local MCP servers that run on a device aren't visible to Global Secure Access.",
    "dk-csp": "which can be used with a Mobile Device Management (MDM) solution like Microsoft Intune",
    "vs-mac-intune": "For enterprise deployments across multiple devices, use Mobile Device Management (MDM) solutions such as:",
    "vs-syntax": "syntax error in the policy value, the setting will not be applied.",
    "ac-unenl": "scripts run through an unenlightened script host, such as many 3rd-party Java or Python engines.",
}
