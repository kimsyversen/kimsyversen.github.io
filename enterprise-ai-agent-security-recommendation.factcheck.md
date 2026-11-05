# Fact check ledger

**Belongs to:** [enterprise-ai-agent-security-recommendation.md](enterprise-ai-agent-security-recommendation.md)
**Checked on:** 2026-11-05
**Method:** each claim compared with the vendor page. Verdicts: **Correct**, **Corrected** (was wrong, now fixed), **Softened** (was too strong, now labelled), **Unverified** (no primary source read, now labelled).
**Not tested:** nothing was run in a real tenant. All verdicts come from documentation, not behavior.

## Corrected (was wrong)

| # | Old claim | Verdict | What the source says | Source |
|---|---|---|---|---|
| 1 | JSON example used `"serverCommand": "npx"` as a string and mixed `serverName` and `serverUrl` in one entry | Corrected | `serverCommand` is a list. It must match the command and every argument in order. No wildcards. Example now follows GitHub's shape and is tagged [pilot]. | GitHub enterprise MCP allowlist |
| 2 | Deny rule on `npx` alone would block risky servers | Corrected | Command matching is exact, so a broad `npx` deny does nothing. Deny list kept short, allowlist does the work. | GitHub enterprise MCP allowlist |
| 3 | "Prohibit personal Copilot accounts" as a GitHub setting | Corrected | No Copilot-specific setting found. EMU users cannot sign up for Copilot Pro or Free. Enterprise access restrictions need a break-and-inspect proxy that injects a header. Effect on Copilot Individual is not stated, so [pilot]. | GitHub managed user account limits; GitHub corporate proxy page |
| 4 | Azure API Center is "a list, not a gate" | Corrected | Page does not say it blocks. GitHub can use it as a registry policy, but that policy is public preview, "not the recommended method", and users can bypass it. | Azure API Center MCP servers; GitHub MCP registry restriction |
| 5 | Local `stdio` servers "only on managed devices" and "bypass any gateway" | Corrected | Microsoft describes registry and gateway for remote servers only. Not covered is an [inference]. GitHub `serverCommand` allowlist can govern local servers. | Agent 365 BYO MCP; GitHub allowlist |
| 6 | Dev Box and Cloud PC clipboard "off by default" | Corrected | Windows 365 Cloud PCs have clipboard, drive, USB and printer redirection off by default [verified]. The Dev Box pages read say clipboard redirection can be disabled with an Intune policy but give no default [not found]. An earlier ledger line said Dev Box has it on. That was wrong and is removed. The doc tells readers to set the policy explicitly. | Dev Box FAQ; Cloud PC RDP redirection |
| 7 | Access review "auto-removes if not answered" | Corrected | It is an option ("Remove access" for non-responders), not the default. | Access reviews for access packages |
| 8 | E7 price and GA date | Corrected | Not on the Microsoft pages read. Removed. Page states E7 includes E5, Copilot, Entra Suite and Agent 365. | Compare E3, E5, E7 |
| 9 | "Agent 365 covers Foundry and other platforms" | Softened | Microsoft says it manages agents "built across Microsoft Copilot Studio, Azure Foundry, and third-party runtimes". No per-platform list is given. | Agent 365 monitor agents |

## Third pass corrections (2026-11-05, after rereading primary pages)

| # | Old claim | Verdict | What the source says | Source |
|---|---|---|---|---|
| 41 | Custom agent profile exemption "reportedly" | Verified | Allow and deny keys "don't apply" to servers in repository custom agent profiles. GitHub advises keeping the start domains blocked in the custom firewall. | GitHub managed settings reference |
| 42 | One key per entry "partly read" | Verified | "Each entry must contain exactly one matcher property." serverName exact, no wildcards. serverUrl wildcards, remote only. serverCommand local only. | GitHub managed settings reference |
| 43 | File path "not found" | Verified | `.github-private` repo, `copilot/managed-settings.json`. Reaches users with an enterprise Copilot license on a supported client within about an hour. | GitHub get-started page |
| 44 | "Deny always wins" | Corrected | Built-in first-party servers are exempt from deny rules. Allowlists intersect across sources. Denylists union. | GitHub managed settings reference |
| 45 | Retained policy on fetch failure | Softened | Keeps the previous policy, only stricter. First fetch with no policy not stated. | GitHub allowlist page |
| 46 | MCP client support "not seen" | Partly read | Both keys read as supported in CLI, VS Code, Copilot app, cloud sandbox, JetBrains. Not in cloud on GitHub Actions. Read from icon labels. | GitHub managed settings reference |
| 47 | Guest add-on restricts "creating or changing" governance | Corrected | Add-on needed for Governance-exclusive features. P2 features (basic access packages and reviews) not billed and no link required. Enforced from January 2026. Admin needs one Governance or Suite license. | Guest licensing page |
| 48 | Employee license for access packages | Added | Needs Entra ID Governance or Suite. Both in E7. E5 gives P2 only. | Licensing fundamentals |
| 49 | Autonomous runs "always billed" | Corrected | Exemption for M365 Copilot users does not apply when an agent runs autonomously. Computer-using agents not included. Channels named: Copilot Chat, Teams, SharePoint. | Copilot Studio billing pages |
| 50 | Foundry bills tokens, tools, hosted compute | Corrected | Model deployments: Global Standard pay-per-token. Hosted agents: CPU and memory across active sessions. Agent overview lists possible extra charges (Application Insights, voice). No complete list found. | Foundry architecture; hosted agents; agent overview |
| 51 | DSPM weekly top 100 sites, preview, E5 | Corrected again | First pass cut it because the learn-about page lacks it. The data risk assessments page says the default assessment runs weekly for the top 100 SharePoint sites by usage and for the top 100 Fabric workspaces. Restored with that source. License level and preview status are not on the pages read. | Purview DSPM data risk assessments |
| 52 | Sentinel connectors | Partly read | Two connectors with tables, token scope and Enterprise Cloud limit. Page says connectors are in preview overall. Read through a summary. | Sentinel connectors reference |
| 53 | Quarterly reviews "Microsoft recommends" | Corrected | No source read. Now labelled [recommendation]. | None |
| 54 | Agent 365 GA, per user, E5 | Verified | Quote: "works best when using Microsoft E5 as a pre-requisite". Also stand-alone. No GCC date. | Agent 365 overview and service description |

## Fourth pass (2026-11-05, later in the day)

| # | Claim | Verdict | What the source says | Source |
|---|---|---|---|---|
| 58 | Guest limits for authentication strengths | Corrected | Strength pages describe external Microsoft Entra users. Email OTP is unsupported in the strength combinations. For Google, SAML and personal Microsoft account guests the resource tenant always handles MFA. Whether a strength policy works for them is not stated [not found]. Doc now says use the plain MFA grant [recommendation]. | Authentication strengths for external users; B2B Conditional Access |
| 59 | "Require approved client app" and "Require app protection policy" for guests | Verified | Not supported for guests. | B2B Conditional Access |
| 60 | Foundry managed network, model deployment policy GA, router policies preview, RBAC, agent identity | Verified | Rechecked on the primary pages. Managed network cannot be disabled once enabled. | Foundry pages in the sources table |
| 61 | Copilot Studio data policies, environment groups | Verified | Rechecked. Environment groups cover managed environments only. Rules are read-only in members. | Copilot Studio data policies; environment groups |
| 62 | DLP for Copilot cannot scan files uploaded straight into a prompt | Verified | Page is now titled "DLP for Microsoft 365 Copilot and Cowork". | DLP page |
| 63 | SharePoint Advanced Management with one Copilot license or E7 | Verified | Prerequisites page. Date in the doc corrected to 2026-08-18. | SAM prerequisites |
| 64 | Conditional Access for agents needs E7, or Agent 365 plus Entra P1 or M365 E3 | Verified | Doc date corrected to 2026-09-30. | Conditional Access for agents |
| 65 | Source table dates | Corrected | Updated for Conditional Access for agents, Copilot Studio data policies, Copilot security, SAM and DLP. Added rows for authentication strengths for external users, Foundry network isolation and the environment groups overview. | Sources table |

## Fifth pass (2026-11-05, after Stop hook)

| # | Claim | Verdict | What the source says | Source |
|---|---|---|---|---|
| 66 | Dev Box clipboard default | Still not found | Dev Box FAQ says clipboard redirection can be disabled and links to the Windows 365 page. That page says its defaults apply "for Cloud PCs". | Dev Box FAQ; Cloud PC RDP redirection |
| 67 | Source dates for Agent 365 overview and session policies | Corrected | Agent 365 overview updated 2026-10-23. Session policy page updated 2026-06-23. | Sources table |

## Correct (confirmed)

| # | Claim | Source |
|---|---|---|
| 10 | Agent 365 MCP registry is in preview and lives at Microsoft 365 admin center, Agents, Tools | Manage tools for agents |
| 11 | Supported clients: Copilot Studio, VS Code, Claude Code, GitHub Copilot CLI. Foundry and M365 declarative agents not supported | Agent 365 BYO MCP |
| 12 | Approval needs Entra consent. A whole server can be blocked. Tool-level blocking for BYO servers is planned | Agent 365 BYO MCP; plugins, skills, MCP page |
| 13 | Server needs a public endpoint. Auth types: NoAuth, API key, external OAuth, Entra OAuth | Agent 365 BYO MCP |
| 14 | GitHub decision order: defaults allowed, deny wins, allowlist blocks unlisted, unresolved variables blocked | GitHub allowlist |
| 15 | Malformed policy fails closed. GitHub fetch failure keeps last applied policy | GitHub allowlist |
| 16 | VS Code policy names (`ChatMCP`, `ChatAgentMode`, `ChatAllowedMcpServers`, `ChatDeniedMcpServers`, `ChatAllowManagedMcpServersOnly`, `ChatCopilotConnectors`, `AllowedExtensions`) | VS Code enterprise policies |
| 17 | Copilot managed settings win over device policy on the same control. Policy Diagnostics shows source | VS Code manage AI settings |
| 18 | Conditional Access for agents: three patterns, report-only advised, API keys not covered, needs E7 or Agent 365 plus Entra P1 or M365 E3 | Conditional Access for agents |
| 19 | Guest MFA, cross-tenant trust, authentication strength limits for non-Entra guests | B2B Conditional Access; authentication strengths |
| 20 | Access package expiry removes access. Guest blocked then removed after 30 days by default | Entitlement management external users |
| 21 | SharePoint limited web-only access blocks download, print, sync and desktop apps | Unmanaged devices in SharePoint |
| 22 | Defender session policies can block download, print, copy | Defender for Cloud Apps session policies |
| 23 | Copilot Studio data policies cover connectors, channels, authentication, knowledge, skills, Application Insights. Blocking connectors also blocks MCP tools that rely on them | Copilot Studio data policies; zoned governance |
| 24 | Environment groups: managed environments only, rules locked in members | Environment groups and rules |
| 25 | Foundry roles, agent identity (OBO is preview), network isolation, model Azure Policy (GA) | Foundry RBAC, agent identity, managed VNet, model deployment policy |
| 26 | Foundry AI gateway is preview, new MCP tools only, no OpenAPI, SharePoint, code-first or managed-OAuth tools, no tool traces | Foundry AI gateway page |
| 27 | Copilot works within user permissions. SharePoint Advanced Management included with a Copilot license | Copilot security; SAM prerequisites |
| 28 | DLP for Copilot cannot scan files uploaded straight into a prompt | DLP for Microsoft 365 Copilot |
| 29 | GitHub audit stream destinations list. Purview stream is preview, Copilot agent session events only | GitHub audit log streaming |
| 30 | Gateway calls queried with `ExecuteToolByGateway` in Defender advanced hunting | Agent 365 BYO MCP |

## Still not fully verified (state after the third pass)

| # | Claim | Status | Label in doc |
|---|---|---|---|
| 31 | Repo custom agent profiles are exempt from allow and deny keys | Now verified, see row 41 | [verified] |
| 32 | Which GitHub clients honor the MCP keys | The client table cells were read. Both keys supported everywhere except Copilot in the cloud on GitHub Actions. | [verified] |
| 33 | Guest governance needs a linked Azure subscription add-on | Now verified with limits, see row 47 | [verified] |
| 34 | Sentinel GitHub connectors, their tables and tokens | Page read in full. Connector reference says connectors are in preview overall. | [verified] |
| 35 | Quarterly access reviews for guests | Relabelled, see row 53 | [recommendation] |
| 36 | DSPM weekly top 100 sites | Verified on the data risk assessments page, see row 51. License level not found. | [verified] |
| 37 | `managed-settings.json` on unmanaged laptops | The deploy page lists server-managed, MDM and file-based delivery. Server-managed reaches licensed users on supported clients without MDM. Not tested on a real unmanaged laptop. | [pilot] |
| 38 | Defender session policies and native or sync clients | Conditional Access app control page: session controls apply only to browser sessions. Admins should block native clients with an access policy (Client app filter Mobile and desktop). | [verified] |
| 39 | Exchange and Teams behavior under limited web-only access | Not read | Not claimed |
| 40 | `ExecuteToolByGateway` in the Defender table reference | Absent from the table page, present on the BYO page | Both stated |
| 55 | What Foundry Agent Service bills for | Hosted agents: CPU and memory in active sessions. No complete list. | [verified, partial] |
| 56 | First policy fetch with no earlier policy on GitHub | `forceRemoteSettingsRefresh: true` requires a fresh download at startup (CLI, VS Code, Copilot app) and blocks VS Code Copilot until it succeeds. With the setting off, other clients' first fetch is not stated. | [verified]; remainder [not found] |
| 57 | MDM paths per operating system | Read. Windows registry `HKLM\SOFTWARE\Policies\GitHubCopilot`, macOS `com.github.copilot`, strings, hourly, no Linux. | [verified] |

## Format checks (2026-11-05)

- Em dashes and en dashes: 0 in both files.
- Every paragraph, list item and bullet in the recommendation is 60 words or fewer. Table cells are also 60 words or fewer.
- All four Mermaid diagrams, extracted from the final file, parse with mermaid 10.9.1 (`mermaid.parse`). Not viewed in a rendered page.
- Source table dates rechecked against the pages read.

## Open questions

- Does your tenant have the Agent 365 registry, and are your client versions supported?
- Does a personal Copilot account work on your network when the proxy option is off?
- Does the GitHub file apply on an unmanaged laptop?
- What do GitHub clients other than Copilot CLI do on first start with no earlier policy when `forceRemoteSettingsRefresh` is off?
- What is the Dev Box clipboard default?
- What is the DSPM license level?
- When is Agent 365 available in GCC? (Answered in row 90.)

## Sixth pass (2026-11-05, after second Stop hook)

| # | Claim | Result | Label in doc |
|---|---|---|---|
| 68 | E7 GA 1 May 2026, $99 per user per month, with and without Teams; Agent 365 stand-alone $15 | Read on the Microsoft Tech Community GA post dated 2026-05-01 | [verified] |
| 69 | Authentication strength for non-Entra guests | Policy applies only to guests who authenticate with Entra ID. Others use the MFA grant control. Page `policy-guests-mfa-strength` last updated 2026-03-24 (read again 2026-11-05). The "resource tenant handles MFA" wording was NOT on that page or the external users page, so it was removed. | [verified] |
| 70 | Source URL for strength external users | Was wrong (404). Fixed to `concept-authentication-strength-external-users` (200). Page last updated 2025-10-25. | Source table |
| 71 | `forceRemoteSettingsRefresh` | Fresh download at startup in CLI, VS Code and Copilot app; skips one-hour cache; VS Code blocks Copilot until success; use MDM or file for first-startup enforcement | [verified] |
| 72 | Three long table cells trimmed to 60 words or fewer | Guests, guest limits, copy-out rows. Meaning unchanged. | Format |
| 73 | E7 price on microsoft.com | Page shows $99.00 per user per month, paid yearly, with E5, Copilot, Agent 365 and Entra Suite. Read 2026-11-05. | [verified] |
| 74 | `forceRemoteSettingsRefresh` scope | Cache skip and no fallback apply in the CLI and the Copilot app. VS Code blocks Copilot until the refresh succeeds. MDM or file needed for first startup. Policy helper scripts cannot set it. | [verified] |
| 75 | "Require approved client app" and "Require app protection policy" for guests | Re-read on the B2B Conditional Access page (updated 2026-03-27): not supported. | [verified] |
| 76 | DSPM license level | Purview service description (updated 2026-10-29) and the classic DSPM for AI page list no level for data risk assessments. | [not found] |
| 77 | What Foundry Agent Service bills for | Azure pricing page: no extra charge for Foundry-native agents with prompts and workflows; model tokens and tools or knowledge connections billed separately; hosted agents by container compute per hour. Earlier Learn page (2026-10-27): CPU and memory in active sessions. Both kept. | [verified] |
| 78 | Defender session policies and sync clients | Resolved earlier (row 38): session controls apply only to browser sessions. Removed from the not found list. | [verified] |

## Seventh pass (2026-11-05, after third Stop hook)

| # | Claim | Result | Label in doc |
|---|---|---|---|
| 79 | "No built-in Azure Policy for Foundry tools" | Wrong. Policy index lists two preview built-ins: "Microsoft Foundry agents and toolboxes should only use approved tools" and "...should not use denied tools" (Audit, Deny, Disabled, version 1.0.0-preview). Index updated 2026-07-13. Doc corrected. | Verified |
| 80 | "No how-to for disabling Foundry key authentication" | Wrong. Learn page "Disable local authentication in Foundry Tools" (updated 2026-06-02) gives the built-in policy, `disableLocalAuth` and PowerShell. Propagation can take hours. Doc corrected. | Verified |
| 81 | "Agent 365 gives no per-platform list" | Wrong. Admin overview (updated 2026-10-23) names Copilot Studio, SharePoint, Agent Builder, AI Foundry, Agents Toolkit. Connected platforms page (updated 2026-10-15) lists Bedrock, Vertex AI, Agentforce, Databricks Genie, Claude, Oracle, Snowflake, with manual sync. Doc corrected. | Verified |
| 82 | "Access review results cannot be applied automatically" (listed as not found) | Resolved. Create-access-review page (updated 2026-03-12): "Auto apply results to resource" removes denied users after the review. Warning if reviewers do not respond. Doc line added. | Verified |
| 83 | Agent 365 GCC availability | Not stated on the Agent 365 pages read. Only the CLI page covers GCC endpoints. Kept as not found. | Not found |
| 84 | Format checks after seventh pass | No U+2014 or U+2013. No paragraph, list item or table cell over 60 words. Mermaid diagrams unchanged since the last parse. | Checked |
| 85 | Not-found items, searched exhaustively | Agent 365 GCC: all 151 TOC pages searched, only CLI covers GCC. DSPM license: all 1,352 Purview TOC pages searched, none states a level for data risk assessments. Dev Box clipboard default: 66 Dev Box and 197 Windows 365 enterprise pages, none states it. GitHub first start with key off: managed settings reference, get-started and MCP management pages, none states it. Doc now says "not stated on the pages searched" with counts. | Not found |
| 86 | Foundry guardrails row and Studio/Foundry table row | Reconciled with the tool policy finding. Tool policy marked preview. | Verified |
| 87 | Mermaid after seventh and eighth edits | Extracted from the final file and parsed with mermaid 10.9.1: 4 of 4 ok. No dashes. No cell, paragraph or list item over 60 words. | Checked |
| 88 | Full re-read of the final document, ninth pass | Header said "third pass": fixed to eighth. Tag table lacked [not found]: added. GCC sentence in E7 section aligned with the search count. No other statement changed. Dash and 60-word checks pass. Diagrams unchanged since the last parse (4 of 4 ok). | Checked |
| 89 | VS Code first-fetch behavior | VS Code page (checked 2026-11-05): from 1.145 a failed refresh keeps a cached registry policy. With no cache and a failed first fetch, registry policy alone does not restrict MCP; the ChatMCP device policy does. Document now states this for the registry policy. The server-managed key-off first start for other clients stays [not found]. | Verified, gap narrowed |
| 90 | Agent 365 GCC date. Earlier claim "no GCC date on any Agent 365 page" was wrong | Microsoft Cloud blog, 2026-09-15: Agent 365 and Microsoft 365 G7 on sale for GCC from 1 October 2026, more options from 1 November, features in phases as GCC authorization milestones clear. No GCC High or DoD date found. | Corrected, verified |
| 91 | Dev Box clipboard default. Earlier "not found" was wrong | AVD clipboard redirection page (page date 2024-04-29) states: Dev Box clipboard redirection is enabled, both directions. Windows 365 Cloud PCs: disabled for new and reprovisioned. Fetched with curl 2026-11-05 after the browser got 429. | Corrected, verified |
| 92 | DSPM license | DSPM get-started page (page date 2025-12-15): DSPM needs Microsoft 365 E5 or Purview Suite. No separate level is named for data risk assessments, so that part is inference. | Verified for DSPM, inference for risk assessments |
| 93 | Remaining [not found] | One: first start with no earlier policy and forceRemoteSettingsRefresh off, for server-managed settings in clients other than the CLI. VS Code states the case for its registry policy only. | Open |
| 94 | "No Copilot-specific setting blocks personal Copilot accounts" | Incomplete. GitHub docs (fetched 2026-11-05): subscription-based network routing lets owners allow their plan endpoint and block the personal-plan endpoint at the firewall. Covers VS Code, Visual Studio, JetBrains, Copilot Chat on GitHub, GitHub Mobile, CLI. Not supported on GHE.com. Wording changed from "Copilot-specific setting" to "GitHub admin setting" and the firewall control added. Effect on a real network is untested. | Corrected, verified; test is [pilot] |
| 95 | Mermaid, tenth pass | Extracted from the final file, parsed with mermaid 10.9.1 in the browser: 4 of 4 ok. | Checked |
| 96 | Sweep of absence claims ("no", "not supported", "does not") after four earlier ones proved wrong | Copilot Studio MCP data policy: Microsoft Learn data policy page (search result 2026-11-05) says blocking a connector also blocks MCP tools that use it. Matches the document. Other absence claims already carry source and date. | No change needed |
| 97 | Last retry of the one [not found] fact | GitHub changelog 2026-10-13 and the deploy page (fetched 2026-11-05) repeat what the document already says: a server-managed value forces refresh only from the second startup, and without the key clients use the normal cache. Neither states first start with no cache and no key for clients other than the CLI. | Still [not found], document unchanged |
| 98 | Eleventh pass: retire [pilot] and [not found] tags | Each open item is now written as a statement that is true as written: either "the pages do not state X" (verified by search on 2026-11-05) or "we did not test X, test it before you rely on it" (a recommendation). No claim about untested behavior remains. Tag table updated. | Checked |
| 99 | Mermaid, eleventh pass, and the E7 page | Diagrams extracted from the current file and parsed with mermaid 10.9.1 in the browser: 4 of 4 ok. The E7 page on microsoft.com loads in the browser (curl got HTTP 403, the browser did not): $99.00 per user per month, includes E5, Microsoft 365 Copilot, Agent 365 and Entra Suite. Matches the document. | Checked 2026-11-05 |
| 100 | Re-read of 2.3 (lines 196 to 270) after the eleventh pass, and one more search for the first-start case | Every statement matches its source row in this ledger. No contradiction between 2.3 and Part 5 items 5, 7 and 10. The search (docs.github.com, github.blog, code.visualstudio.com, 2026-11-05) returned the same pages as before and no new statement on first start for clients other than the CLI. | Checked 2026-11-05 |
| 101 | Link check of every URL in the document (74 unique) | curl with a browser user agent, 2026-11-05: 71 return HTTP 200. One is the placeholder `mcp.example.corp` in the example file, which is meant not to exist. Two microsoft.com pages return 403 to curl: the E7 page and the G7 blog post. Both load in the browser. The G7 post text matches the document: GCC purchase from 1 October 2026, more options 1 November, capabilities in phases as GCC authorization milestones are met. | Checked 2026-11-05 |
