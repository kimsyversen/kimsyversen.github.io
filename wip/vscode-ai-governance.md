# VS Code and AI governance on Windows and Azure

Checked against current Microsoft and GitHub documentation on **23 November 2026**. This area changes quickly. Re-check preview features and live policy references before deployment.

**Labels used in this document**

- **[Verified]**: confirmed in the linked primary documentation on 23 Nov 2026.
- **[Preview]**: real, but the vendor calls it preview or experimental. Use it, but do not base compliance claims on it alone.
- **[Unverified]**: not confirmed in the linked primary documentation. Verify before relying on it.

## Contents

1. [Short answer](#1-short-answer)
2. [How it works](#2-how-it-works)
3. [What to do, step by step](#3-what-to-do-step-by-step)
4. [VS Code policy reference](#4-vs-code-policy-reference)
5. [GitHub enterprise managed settings](#5-github-enterprise-managed-settings)
6. [What Sentinel can and cannot see](#6-what-sentinel-can-and-cannot-see)
7. [Hunting queries](#7-hunting-queries)
8. [Watch-outs](#8-watch-outs)
9. [Rollout checklist](#9-rollout-checklist)
10. [Verification notes](#10-verification-notes)
11. [Sources](#11-sources)

---

## 1. Short answer

You control VS Code in three places:

1. **The device.** VS Code reads policies from the Windows registry. You push them with Intune or Group Policy.
2. **The account and service.** GitHub organization and enterprise settings govern seats, available models, and service-side features; enterprise-managed settings govern supported clients.
3. **The network and endpoint.** Proxy, firewall, Defender for Endpoint, Defender for Cloud Apps and Purview.

Sentinel can receive endpoint, identity, GitHub audit, and configured agent telemetry. GitHub audit logs document policy and agent events but do not provide local IDE prompt text. To collect prompts and responses, configure supported Copilot OpenTelemetry content capture; verify the client and harness. This review did not confirm Purview coverage for GitHub Copilot IDE conversations.

Key gaps to manage:

- **Other editors and VS Code-derived products** need separate testing and governance; do not assume VS Code device policies apply to them.
- **Personal Copilot accounts** used on company code, unless you block them.
- **Attribution is limited.** Endpoint process events do not reliably identify which extension or agent caused an in-process action.

---

## 2. How it works

- **VS Code uses multiple processes**, including extension hosts and agent runtimes. Endpoint telemetry can show process and network activity, but usually does not reliably attribute an action to a particular extension or agent.
- **AI comes into VS Code four ways:**
  1. **GitHub Copilot, built in.** Chat, agent mode (edits files and runs terminal commands), MCP servers (add-on tools), hooks and plugins.
  2. **Other agent harnesses in VS Code.** Claude and Codex integrations may have separate availability and controls.
  3. **Other AI extensions**, such as Cline, Continue, Roo or Claude Code. These can send code to any server and bring their own model keys.
  4. **Other editors and VS Code-derived products.** Test their policy, extension, and update behavior separately.
- **Personal Copilot accounts are a separate governance path.** Copilot Free is available to individual developers in VS Code, but personal plan access is not governed by an organization's assigned Copilot seat or GitHub-side Copilot policies. Decide whether to block it on managed devices.
- **Two control systems overlap.** VS Code device policies and Copilot enterprise-managed settings can overlap. For the same control, enterprise-managed settings take precedence; values are not merged. Enforcement can vary by agent harness, so verify the behavior in the exact client and execution environment. **[Verified]**

---

## 3. What to do, step by step

### Step 1: See what you have (no impact on users)

- **Put developer machines on Defender for Endpoint Plan 2.** It can find local AI agents and their MCP servers. Portal: **Assets > AI agents > Local agents**. Hunt on it with the `AgentsInfo` table. **[Verified]**
  - Needs Defender Antivirus in active mode with real-time protection on.
  - Commercial cloud only. Some macOS VS Code extension inventory entries remain in preview. Confirm the current support matrix; MCP discovery has separate prerequisites.
  - Risk levels, indicators, and recommendations require Microsoft 365 E7, or Microsoft Agent 365 together with Defender for Endpoint Plan 2. The inventory and `AgentsInfo` queries require Plan 2.
- **Connect the GitHub Enterprise Audit Log connector** in Sentinel (Content Hub).
- **Look at Defender for Cloud Apps** Cloud Discovery, category Generative AI, to see which AI web services people use.
- **Run the queries in section 7** to see what normal looks like before you block anything.

### Step 2: Lock the basics with VS Code policies

**How to deploy** **[Verified]**

- Each VS Code release ships ADMX and ADML files in a `policies` folder (since version 1.69).
- Import them into your device-management solution or use Group Policy. The exact import workflow depends on the product; the VS Code documentation covers ADMX deployment.
- Policies work under both **Computer Configuration** and **User Configuration**. Computer-level values take precedence when both are configured.
- Registry path: `HKLM\Software\Policies\Microsoft\VSCode` (computer) or `HKCU\Software\Policies\Microsoft\VSCode` (user).
- Run **Developer: Policy Diagnostics** to inspect effective values, sources, and the account-policy gate. A reported value alone does not prove that every harness enforces it.
- A policy only works in VS Code versions that know it. Older versions ignore newer policies. Keep VS Code updated.

**Suggested baseline** (proposed values are recommendations; verify each control against the current policy reference and intended harness)

| Policy | Suggested value | Notes |
|---|---|---|---|
| `ChatApprovedAccountOrganizations` | `["your-github-org"]` | Fail-closed account gate for VS Code AI features; requires an eligible signed-in GitHub account. Check the effective gate in Policy Diagnostics. |
| `AllowedExtensions` | Explicit publisher/extension allowlist | Restricts installation and enablement, but does not verify VSIX provenance, protect modified extension files, or restrict extension runtime permissions. |
| `ExtensionGalleryServiceUrl` | Approved marketplace, if operated | Changes the marketplace service endpoint; validate availability and trust controls separately. |
| `ExtensionsAutoUpdate` + `ExtensionsAutoUpdateDelay` | Keep updates enabled; consider a short delay | Delay only applies when automatic extension updates are on. |
| `ChatToolsAutoApprove` | `false` | Disables global auto-approval. Keep it off unless the threat model explicitly permits it. |
| `ChatToolsTerminalEnableAutoApprove` | `false` | Controls rule-based terminal auto-approval for supported sessions; it does not disable every session-level or sandbox approval path. |
| `ChatToolsEligibleForAutoApproval` | Exclude sensitive tools | Enforcement differs by harness. In Copilot harness sessions, a `false` value removes Allow all for the session; it does not necessarily force a prompt for every invocation. |
| `ChatMCP` | `registry` or `none`, if suitable | VS Code device policy. For stronger cross-client controls, use supported Copilot enterprise-managed MCP settings and verify client coverage. |
| `ChatAllowedMcpServers` + `ChatDeniedMcpServers` | Explicit allowlist and denylist | Omitted allowlist can allow all servers. Deny rules take precedence. Prefer URL or exact command identity where supported. |
| `ChatAllowManagedMcpServersOnly` | `true`, if applicable | Verify exact version and session support in the live policy reference. |
| `ChatAllowManagedHooksOnly` + `ChatHooks` | Restrict sources and disable unsupported hooks | Hook controls differ by harness. Follow current enterprise AI settings guidance. |
| `ChatStrictMarketplaces` + `ChatStrictPluginOnlyCustomization` | Restrict to approved sources and customizations | Marketplace, plugin, and standalone customization controls are separate; configure both as required. |
| `ChatAgentNetworkFilter` + domain policies | Enable only with a tested allow/deny design | Applies differently by harness, tool, platform, and sandbox. Do not assume it filters every terminal process. |
| `ChatAgentSandboxEnabled` and related policies | Do not use as the sole Copilot harness control | These legacy device policies apply to Local harness sessions and are deprecated; Copilot harness sandbox restrictions use enterprise-managed `sandbox` settings and session controls. |
| `Codex3PIntegration` / `Claude3PIntegration` | Keep disabled unless explicitly approved | Device policy values do not by themselves override the default restriction imposed while Copilot enterprise-managed settings apply. Permitted third-party harnesses may not enforce Copilot managed controls. |
| `ChatAgentMode` | Decide by group and workflow | Disables the Agent option and Agents window, but is not a blanket restriction on Agent Host sessions. |
| `BrowserChatTools` + `ChatAgentExtensionTools` | Disable unless needed | Separate controls for browser tools and extension-contributed tools. Confirm harness behavior. |
| `CopilotOtel*` | Managed collector/export configuration | Current reference covers endpoint, protocol, content and identity capture, headers, and resource attributes. Protect captured content as sensitive data. |
| `CopilotSessionSync` | Set according to data policy | Check the current setting and account behavior before deployment. |
| `UpdateMode` | Keep security updates enabled | This controls the VS Code application updater, not package-manager or extension updates. |
| `TelemetryLevel`, `EnableFeedback` | Set per company policy | These concern VS Code telemetry and feedback, not your own agent monitoring. |

**Test with a pilot group first.** A wrong organization name or restrictive allowlist can block expected workflows. Confirm effective policy and behavior in each supported harness.

### Step 3: Control Copilot from GitHub

- **Use Copilot Business or Enterprise** for managed organizational access. Consider **Enterprise Managed Users (EMU)** when centrally managed GitHub identities are required.
- **Restrict Copilot plan endpoints on the network** with subscription-based routing. **[Verified]**
  - Allow the hostname for the assigned plan: `*.business.githubcopilot.com` for Business, or `*.enterprise.githubcopilot.com` for Enterprise or Copilot access billing. Block `*.individual.githubcopilot.com` to prevent Individual plan access on that network. Confirm the current hostname list and client versions before rollout.
- **Block personal GitHub accounts on github.com** with the proxy header (EMU only). **[Verified]**
  - Header: `sec-GitHub-allowed-enterprise: <ENTERPRISE-ID>`. Up to 20 IDs, comma-separated.
  - Inject it on `github.com/*`, `api.github.com/*` and `*.githubcopilot.com`.
  - Your proxy must do **TLS break-and-inspect** to add headers. Without that, this control is not available.
  - It does not cover SSH, Codespaces or GitHub Pages.
  - Not needed on GHE.com (data residency).
- **Set Copilot policies on GitHub:** allowed models, blocking of public-code matches, content exclusions, preview features and the cloud coding agent.
- **Control MCP servers with enterprise-managed settings** (section 5). Prefer URL or exact command matchers where supported. The separate MCP private-registry feature is public preview and can be bypassed by editing configuration files. **[Verified]**
- **Stream the GitHub audit log** to Sentinel. Filter on `actor:Copilot` to see agent actions. GitHub keeps 180 days, so stream it if you need more. The audit log does **not** include prompts that users send to Copilot locally. **[Verified]**

### Step 4: Harden Windows and the network

- **Manage VS Code installation and updates** through your approved software-management process. Keep security updates current.
- **Use application control or software inventory** to govern unapproved editors and agent CLIs. VS Code device policies do not establish control over other products.
- **Deploy the Dev Tunnels ADMX** (`TunnelsPolicies.admx`, from [aka.ms/devtunnels/policies/download](https://aka.ms/devtunnels/policies/download)). **[Verified]**
  - GPO path: Computer Configuration > Administrative Templates > Dev Tunnels.
  - Options: "Disable Dev Tunnels", "Disable anonymous tunnel access", "Allow only selected Microsoft Entra tenant IDs".
  - Covers VS Code port forwarding, the Remote - Tunnels extension, Visual Studio dev tunnels and the `devtunnel` CLI. Windows only.
  - Dev Tunnels can expose local services through remote tunnels. Restrict and monitor use according to your development workflows.
- **Mark unapproved AI services as Unsanctioned in Defender for Cloud Apps.** This label supports monitoring; blocking requires the Defender for Endpoint integration and endpoint Network Protection. **[Verified]**
  - Needs MDE cloud protection and network protection turned on.
  - Non-Microsoft browsers need the Defender Browser Protection add-on.
  - Microsoft documents propagation delays of up to about three hours in total, including cloud synchronization and endpoint policy distribution. Verify the current SLA and test enforcement.
  - Validate enforcement from VS Code, extensions, command-line clients, and browsers. Enforcement depends on endpoint configuration and domain coverage.
- **Configure Tenant Restrictions v2** with an explicit external-tenant policy and a supported enforcement path. It governs Microsoft Entra sign-ins and supported Microsoft resource scenarios, not every identity provider.

### Step 5: Get AI detail into Sentinel

- **Copilot OpenTelemetry (OTel).** **[Verified]**
  - Use current `CopilotOtel*` device policies or managed `telemetry` settings to configure export. VS Code documents collector-based OTLP export and managed Agent Host telemetry; validate the supported protocol and destination for each client. Application Insights can be a destination through an appropriate collector/exporter configuration.
  - Current VS Code documentation describes telemetry for Copilot Chat and Agent Host sessions, and managed export configuration. Coverage and restrictions differ for Claude, CLI, and other harnesses; do not infer that one configuration covers all of them.
  - **Without content capture**, prompts, responses, and tool arguments are not captured by default; metadata such as models, token counts, and durations is available.
  - **With content capture enabled**, telemetry can include prompt and response messages, system prompts, tool schemas and arguments, command text, and file paths. Verify exact fields for the deployed client and harness.
  - This data can contain source code, secrets, and personal information. Protect it as sensitive data and set appropriate access and retention controls.
  - Attribute names include standard `gen_ai.*` fields and VS Code/GitHub Copilot namespaces. Inspect representative telemetry before writing detections; current documentation identifies some older attributes as legacy.
- **Purview coverage for GitHub Copilot.** The sources reviewed for this update do not establish a generally available Purview audit or DLP path for local GitHub Copilot prompts and responses. Do not rely on Microsoft 365 Copilot audit documentation as evidence of GitHub Copilot coverage. Confirm product availability and scope in current Microsoft documentation and the tenant before relying on it.
- **Purview for local agents.** The sources reviewed do not confirm the claimed prompt, response, and action coverage for these named local agents. Treat this capability as unverified until Microsoft documents the supported products, licensing, and data scope.
- **Microsoft Copilot logs connector for Sentinel.** Microsoft documents ingestion of Microsoft 365 Copilot and Security Copilot activity into the `CopilotActivity` table. The current connector reference marks the table lake-only. This does not establish that the connector ingests GitHub Copilot IDE prompts or actions.

---

## 4. VS Code policy reference

The available VS Code enterprise policies change frequently. Do not rely on a static count or minimum-version list in this document. Use the live [enterprise policy reference](https://code.visualstudio.com/docs/enterprise/policies) and [enterprise AI settings guide](https://code.visualstudio.com/docs/enterprise/manage-ai-settings) for current names, supported versions, scope, and harness limitations. The current VS Code documentation distinguishes Local harness device policies from Copilot harness controls; some older sandbox policies apply only to Local sessions and are deprecated.

Notable limits documented at the time of this check:

- `ChatAgentMode` is not a universal restriction on Agent Host sessions.
- `AllowedExtensions` does not verify VSIX provenance or restrict runtime permissions.
- Network filtering, tool approval, hooks, sandboxing, and managed settings have harness-specific behavior.
- Workspace Trust, custom model endpoints, remote hosts, and third-party tools require separate controls and testing; do not infer coverage from a VS Code policy name alone.

## 5. GitHub enterprise managed settings

GitHub Copilot enterprise-managed settings use a common policy format with multiple delivery methods. Current delivery precedence is **MDM-managed**, then **server-managed**, then **file-based**, then user settings. Some keys combine in the restrictive direction. A device-managed deployment includes both native MDM policy and administrator-deployed managed-settings files. See GitHub's live [deployment guide](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/deploy-managed-settings) and [settings reference](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings).

When a managed setting and a VS Code device policy control the same behavior, the enterprise-managed setting takes precedence and the values are not merged. Enforcement is not uniform across harnesses: Claude and Codex integrations do not enforce Copilot-managed permissions, sandbox, MCP, or plugin controls. The current VS Code guide says applying managed settings can disable these harnesses by default; allowing them is an explicit exception and does not make them enforce Copilot controls.

Relevant managed-setting families include `allowedMcpServers` and `deniedMcpServers`, `permissions.*`, `sandbox`, `enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces`, and `telemetry`. Client support varies by key. Do not assume every key in GitHub's reference applies to VS Code, Copilot CLI, the Copilot app, or cloud agents equally.

**MCP allowlists**

- Use `serverUrl` for remote server identity and `serverCommand` for local server identity where supported. A command matcher must match the command array exactly. `serverName` is user-assigned and is not a strong identity control.
- Deny rules take precedence over allow rules. An omitted allowlist may leave servers permitted, depending on the applicable policy and client. An empty allowlist blocks unmatched servers, with documented first-party exceptions.
- Multiple managed sources can combine restrictions. A configuration that cannot be validated may fail closed; confirm the behavior for the supported client.
- The built-in GitHub MCP server has documented first-party exceptions in some managed settings, but Copilot account MCP policy can still disable it in supported clients. Avoid the blanket claim that it can never be denied.
- **[Preview]** GitHub's separate MCP private-registry enforcement feature is weaker: matching uses server name/ID, can be bypassed by editing configuration, and strict prevention of non-registry installation is not available. Prefer enterprise-managed server allowlists for enforcement.

## 6. What Sentinel can and cannot see

| Question | Data source | Table | How it gets to Sentinel | Status |
|---|---|---|---|---|
| Is VS Code or a fork running? | Defender for Endpoint | `DeviceProcessEvents` | Defender XDR connector | Verify executable inventory locally |
| What did VS Code start (terminal, scripts)? | Defender for Endpoint | `DeviceProcessEvents` | Defender XDR connector | Verified (test parent process, see 7.3) |
| Where does it connect? Which Copilot plan? | Defender for Endpoint | `DeviceNetworkEvents` | Defender XDR connector | Hostname visibility varies; supplement with proxy or firewall logs where needed |
| Extensions installed by command line or VSIX | Defender for Endpoint | `DeviceProcessEvents`, `DeviceFileEvents` | Defender XDR connector | Partial. Installs from the marketplace screen may not show |
| Dev tunnel use | Defender for Endpoint | `DeviceProcessEvents`, `DeviceNetworkEvents` | Defender XDR connector | Verified |
| Which AI agents are installed, their MCP servers, auto-approve | Defender local agent discovery | `AgentsInfo`, `ExposureGraphNodes`, `ExposureGraphEdges` | Defender advanced hunting and custom detections | Verified in Defender. **Unverified** whether it streams to Sentinel |
| Copilot policy and seat changes, agent actions on GitHub | GitHub audit log | `GitHubAuditLogsV2_CL` or `GitHubAuditLogsV3_CL`, depending on connector | GitHub Enterprise Audit Log connector | Verify connector generation and schema |
| Agent tool calls, models, tokens | Copilot OTel | Application Insights tables | Collector to workspace-based App Insights | Verified |
| Prompts, answers, commands the agent ran | Copilot OTel with content capture | Destination-specific OTel tables | Same | Verify client, harness, and emitted fields |
| GitHub Copilot prompts in Purview | No confirmed source in this review | Not established | Not established | Unverified |
| Microsoft 365 Copilot and Security Copilot activity | Microsoft Copilot logs connector | `CopilotActivity` | Microsoft Sentinel connector | Connector documentation lists this table as lake-only ingestion; this does not establish GitHub Copilot IDE coverage |
| Sign-ins from VS Code and Azure CLI, blocked cross-tenant sign-ins | Entra ID | `SigninLogs` and related | Entra ID connector | Verified |
| Which AI web services people use | Defender for Cloud Apps | Cloud Discovery | Defender XDR connector | Verified |
| Developer tools pointed at your Azure OpenAI or Foundry models | Diagnostic logs, Defender for AI | Diagnostics, alerts | Diagnostic settings, Defender for Cloud connector | Not re-checked in this pass |

**Blind spots**

- **Which extension did something.** Process telemetry does not reliably attribute in-process activity to a specific extension.
- **Local prompts and answers.** GitHub audit logs do not provide local IDE prompt text. OTel content capture is a documented option; Purview scope was not confirmed in this review.
- **Remote development.** Identify the host that runs the agent and commands in Remote-SSH, Dev Containers, WSL, and Codespaces. Apply monitoring and controls at that execution location; a local desktop sensor may not see the full activity.
- **Some HTTPS traffic** has no hostname in `DeviceNetworkEvents`.

**Retention and cost:** Defender XDR hunting retention, Sentinel analytics retention, and Sentinel data lake retention depend on product configuration and current licensing. Check current retention and pricing documentation before designing ingestion.

---

## 7. Hunting queries

Read this first:

- These are **starting points for hunting**, not finished alerts. Tune them on your own data first.
- **I have not run these against live data.** Test them in Defender advanced hunting before using them.
- They are written for Defender advanced hunting. In Sentinel Logs, use `TimeGenerated` if `Timestamp` is missing.

### 7.1 Personal Copilot on company devices

```kusto
DeviceNetworkEvents
| where Timestamp > ago(30d)
| where RemoteUrl has "individual.githubcopilot.com"
| summarize Connections = count(), LastSeen = max(Timestamp)
    by DeviceName, InitiatingProcessAccountName, InitiatingProcessFileName
```

### 7.2 Dev tunnels

VS Code port forwarding also uses dev tunnels, so some hits are normal.

```kusto
union
  (DeviceProcessEvents
   | where Timestamp > ago(30d)
   | where FileName in~ ("code.exe", "code-insiders.exe", "code-tunnel.exe", "devtunnel.exe")
   | where ProcessCommandLine has "tunnel"
   | project Timestamp, DeviceName, Account = AccountName, Evidence = ProcessCommandLine),
  (DeviceNetworkEvents
   | where Timestamp > ago(30d)
   | where RemoteUrl has_any ("devtunnels.ms", "tunnels.api.visualstudio.com")
   | project Timestamp, DeviceName, Account = InitiatingProcessAccountName,
             Evidence = strcat(InitiatingProcessFileName, " -> ", RemoteUrl))
| summarize FirstSeen = min(Timestamp), LastSeen = max(Timestamp), Evidence = make_set(Evidence, 10)
    by DeviceName, Account
```

### 7.3 VS Code (or a fork) starting risky tools

Catches the agent or an extension running attack-style commands.

```kusto
DeviceProcessEvents
| where Timestamp > ago(7d)
| where InitiatingProcessFileName in~ ("code.exe", "code-insiders.exe", "cursor.exe", "windsurf.exe")
| where FileName in~ ("certutil.exe", "bitsadmin.exe", "mshta.exe", "regsvr32.exe", "rundll32.exe", "wscript.exe", "cscript.exe")
    or (FileName in~ ("powershell.exe", "pwsh.exe")
        and ProcessCommandLine matches regex @"(?i)(\s-(e|ec|enc|encodedcommand)\s|frombase64string|downloadstring|\biex\b)")
| project Timestamp, DeviceName, AccountName, FileName, ProcessCommandLine, InitiatingProcessCommandLine
```

Validate process lineage on a pilot machine with a harmless command. Process trees vary by harness, platform, and release; check the actual chain in your environment and adjust the query.

### 7.4 Extensions installed from the command line or a VSIX file

Normal installs from the marketplace screen may not show up here. The allowlist is your real control for those.

```kusto
union
  (DeviceProcessEvents
   | where Timestamp > ago(30d)
   | where ProcessCommandLine has "--install-extension"
   | project Timestamp, DeviceName, Account = AccountName, Evidence = ProcessCommandLine),
  (DeviceFileEvents
   | where Timestamp > ago(30d)
   | where FileName endswith ".vsix"
   | project Timestamp, DeviceName, Account = InitiatingProcessAccountName,
             Evidence = strcat(FolderPath, " from ", FileOriginUrl))
```

### 7.5 Unapproved VS Code forks

Executable names are examples, not a complete or authoritative inventory. Compare them with your own software inventory and update the list.

```kusto
DeviceProcessEvents
| where Timestamp > ago(30d)
| where FileName in~ ("cursor.exe", "windsurf.exe", "kiro.exe", "trae.exe", "antigravity.exe", "vscodium.exe")
| summarize Devices = dcount(DeviceId), Users = make_set(AccountName, 50), LastSeen = max(Timestamp) by FileName
```

### 7.6 AI agents running in auto-approve

Adapted from Microsoft's local agent discovery docs. Validate metadata field names against the live schema and your tenant before relying on the result. Runs in Defender advanced hunting.

```kusto
AgentsInfo
| where Platform == "LocalAgents"
| summarize arg_max(Timestamp, Name, Version, LifecycleStatus, RawAgentInfo) by AgentId
| where LifecycleStatus !in~ ("Deleted", "Uninstalled")
| extend M = RawAgentInfo.localAgentMetadata
| where tostring(M.autoApprove) =~ "true"
| project Agent = Name, Vendor = tostring(M.vendor), Process = tostring(M.relatedProcess),
          Device = tostring(M.deviceName), Account = tostring(M.accountName)
```

---

## 8. Watch-outs

**Sandboxing is harness- and host-specific.** Current VS Code documentation describes sandboxing for Copilot Agent Host sessions. The legacy `ChatAgentSandbox*` device policies apply to Local harness sessions and are deprecated; do not use them as the Copilot harness enforcement mechanism. Configure the managed `sandbox` setting where supported, then inspect `/sandbox policy` in the session on the machine that executes commands. Windows support is still marked experimental and has specific Windows 11 update prerequisites. Check the live sandbox guide for current builds, network behavior, filesystem scope, and remote/container requirements. Sandboxing is not a VM or a replacement for endpoint security.

**Agent-mode policy is not a blanket agent kill switch.** `ChatAgentMode=false` hides the Agent option and Agents window but can leave Agent Host sessions available through other UI paths. Test all relevant harness/session entry points.

**Forks and other editors need separate governance.** VS Code device policies apply to supported VS Code installations. Do not assume they govern VS Code-derived products, other IDEs, standalone agent CLIs, or remote execution hosts. Use software inventory, application control, service-side controls, and separate policy tests.

**Account controls have different scopes.** `ChatApprovedAccountOrganizations` is a VS Code AI account gate. GitHub MCP governance applies only to subscriptions/accounts governed by the relevant organization or enterprise policies. Network routing can block Individual plan endpoints but should be tested with current client versions and all required plan endpoints.

**MCP servers and extensions execute code.** Local MCP servers and extensions can run with the user's permissions. Extension allowlists do not sandbox extensions. Review provenance, exact server identity, tokens, network access, and update processes.

**Unsanctioned app labels are not themselves a block.** Defender for Cloud Apps requires the Defender for Endpoint enforcement integration and correctly configured Network Protection. Check the app domain list, policy propagation, and actual endpoint behavior.

**Tenant Restrictions v2 scope is limited.** It governs Microsoft Entra tenant sign-ins and supported Microsoft resource scenarios. Pick and validate the enforcement path; do not describe it as blocking all external accounts or all identity providers.

**Telemetry content is sensitive.** Content capture can include source code, file paths, prompts, system prompts, tool definitions, command text, and results. Set access controls, retention, and legal/privacy review before enabling it. Collection details vary by client and harness.

**Remote development moves execution.** For SSH, WSL, containers, and cloud workspaces, determine where the agent host and commands run. Endpoint policy and telemetry on the local desktop may not cover that execution host.

**Preview and changing features:** Windows sandboxing remains experimental in the current VS Code guide. The VS Code policy catalog and GitHub managed-settings reference are living documents; re-check them before rollout. This review did not confirm Purview coverage for GitHub Copilot prompts or local-agent conversations.

## 9. Rollout checklist

1. [ ] Onboard developer machines to Defender for Endpoint Plan 2.
2. [ ] Connect Defender XDR and GitHub Enterprise Audit Log connectors to Sentinel.
3. [ ] Run the hunting queries for two weeks to learn what normal looks like.
4. [ ] Inventory forks, AI extensions and local agents.
5. [ ] Move everyone to Copilot Business or Enterprise. Consider EMU.
6. [ ] Pilot the VS Code policy baseline with a small group.
7. [ ] Set `ChatApprovedAccountOrganizations` and block `*.individual.githubcopilot.com` if personal Copilot plans are not allowed on managed networks.
8. [ ] Roll out `AllowedExtensions` and the update delay.
9. [ ] Set MCP allowlists (VS Code policy or GitHub managed settings, one owner).
10. [ ] Deploy the Dev Tunnels ADMX.
11. [ ] Block unapproved forks with App Control.
12. [ ] Mark unapproved AI services as Unsanctioned in Defender for Cloud Apps.
13. [ ] Decide on OTel content capture with privacy, legal and HR, then turn on OTel export.
14. [ ] Re-check current Microsoft Purview documentation for any newly supported GitHub Copilot coverage; do not assume support.
15. [ ] Turn the best hunting queries into analytics rules.
16. [ ] Re-check preview items and new policies every quarter.

---

## 10. Verification notes

This update checked official Microsoft and GitHub documentation on **23 November 2026**. It corrects several material issues from the prior version:

- Replaced the stale fixed count of VS Code policies and old minimum-version table with current live references.
- Corrected `ChatAgentMode`: it is not a blanket restriction on agent sessions.
- Corrected sandbox guidance: current Copilot harness sandbox controls use managed settings/session controls; older `ChatAgentSandbox*` device policies are Local-harness scoped and deprecated.
- Added harness-specific caveats for approvals, network filtering, hooks, telemetry, and third-party Claude/Codex sessions.
- Corrected Defender for Cloud Apps: marking an application Unsanctioned alone does not block it; endpoint enforcement must be configured.
- Removed unconfirmed claims that Purview captures GitHub Copilot/local-agent prompts and responses.
- Replaced old fixed MCP and telemetry assumptions with current managed-settings behavior and client-scope caveats.
- The hunting queries are examples only. They were not executed against a live Defender or Sentinel tenant, so validate table names, columns, data availability, process lineage, and results before operational use.

## 11. Sources

**VS Code**

- [Manage AI settings in enterprise environments](https://code.visualstudio.com/docs/enterprise/manage-ai-settings)
- [Enterprise policy reference](https://code.visualstudio.com/docs/enterprise/policies)
- [Agent sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing)
- [Monitor agent usage with OpenTelemetry](https://code.visualstudio.com/docs/agents/guides/monitoring-agents)
- [Manage extensions in enterprise environments](https://code.visualstudio.com/docs/enterprise/extensions)

**GitHub**

- [Deploy enterprise-managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/deploy-managed-settings)
- [Enterprise-managed settings reference](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings)
- [Copilot governance controls](https://docs.github.com/en/copilot/concepts/enterprise/governance-controls)
- [Getting started with a Copilot plan](https://docs.github.com/en/copilot/how-tos/manage-your-account/get-started-with-a-copilot-plan)
- [Copilot network access guidance](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-access/manage-network-access)
- [Copilot allowlist reference](https://docs.github.com/en/copilot/reference/copilot-allowlist-reference)
- [Restrict GitHub.com access with a corporate proxy](https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/hardening-security-for-your-enterprise/restricting-access-to-githubcom-using-a-corporate-proxy)
- [Review Copilot audit logs](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/review-audit-logs)
- [MCP private registry enforcement](https://docs.github.com/en/copilot/reference/enterprise-administrators/mcp-private-registry-enforcement)

**Microsoft security**

- [Discover local AI agents with Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/discover-local-ai-agents)
- [Govern discovered apps using Defender for Endpoint](https://learn.microsoft.com/en-us/defender-cloud-apps/mde-govern)
- [Investigate apps discovered by Defender for Endpoint](https://learn.microsoft.com/en-us/defender-cloud-apps/mde-investigation)
- [Microsoft Sentinel data connectors reference](https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference)
- [Microsoft Sentinel tables and connectors reference](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-tables-connectors-reference)
- [Configure Tenant Restrictions v2](https://learn.microsoft.com/en-us/entra/external-id/tenant-restrictions-v2)
- [Configure and deploy Dev Tunnels group policies](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)
