# Developer workstation risk map: content assessment

Belongs to [Developer-WS.html](Developer-WS.html). Written by AI on 10 November 2026.

Page version assessed: last commit `e728279` (9 November 2026) plus the uncommitted wording changes in the working tree. SHA-256 `0f4ede33364ead8432c8f278fa748d9308c21134b27101ff1da109be956cc23d`. The page was not changed during the assessment.

Update, 10 November 2026: after this assessment, observations 1 to 3 were applied to the page (npm 12.2.2, the Codex `[network_proxy]` name and the four source titles). The text below describes the page as it was assessed. The changes are recorded in the [fact check](Developer-WS.factcheck.md) under "Recheck, 10 November 2026".

## Verdict

No factual error was found. Every claim that was checked against its source held up.

Three things are out of date or drifting, all low. The page says npm 12.2.1 is current; the registry now serves 12.2.2. OpenAI has renamed the Codex network table. Four source titles have changed. None of these makes a statement on the page wrong for its "Current as of 1 November 2026" date.

Six items could not be checked today. They are listed under "Not checked" and are not counted as confirmed.

## What was checked, and how

Each source was fetched fresh on 10 November 2026 and searched for the page's claim. Pages that blocked a plain fetch were opened in a browser. This is a claim-by-claim check, not a full read of every source.

| Area | Method | Result |
|---|---|---|
| Claude Code settings and sandbox | Anthropic docs (sandboxing, settings, permissions, plugins, managed MCP) | All checked claims confirmed |
| VS Code policies, sandbox, tasks, tunnels, containers | Microsoft docs and the `mcpManagement.ts` source file | All checked claims confirmed; the docs and source still disagree on `chat.mcp.access`, as the page says |
| Codex requirements | OpenAI docs (approvals and security, managed configuration, auto-review) | Confirmed; one naming drift (observation 2) |
| npm 12 | npm registry API, npm v12 docs, GitHub changelog | Confirmed; one version drift (observation 1) |
| GitHub (package firewall, CODEOWNERS, Actions, Copilot managed settings) | GitHub docs and changelog | Confirmed |
| MCP specification and security guidance | modelcontextprotocol.io | Confirmed |
| Git, OpenSSH, Defender, incident response | git-scm.com, OpenBSD man page, Microsoft Learn | Confirmed |
| Incidents and research | The cited vendor or researcher write-up for each | Confirmed, except the items under "Not checked" |
| Page structure | Counts in the page data; `python3 -I scripts/section_anchors.py --check` | 10 top risks, 7 further risks, 62 sources; anchor check exit 0 |

Not done: no setting, command or hunting query was run on a managed machine. The Git behaviour tests recorded in the fact check were not re-run.

## Confirmed claims

### Claude Code

- The sandbox is off by default, covers macOS, Linux and WSL2, and does not cover native Windows.
- Sandbox limits cover shell commands only. Hooks, local MCP servers, plugin monitors, LSP servers, the status line and `apiKeyHelper` run with full access.
- Default sandbox reads include `~/.ssh` and `~/.aws/credentials` unless denied.
- These keys exist and behave as the page says: `failIfUnavailable`, `allowUnsandboxedCommands`, `allowManagedReadPathsOnly`, `allowManagedDomainsOnly`, `disableBypassPermissionsMode`, `disableAutoMode`, `requiredMinimumVersion`, `forceLoginMethod`, `forceLoginOrgUUID`, `cleanupPeriodDays`, `allowedMcpServers`, `allowManagedMcpServersOnly`, `strictKnownMarketplaces`, `strictPluginOnlyCustomization`, `autoMemoryEnabled`, `disableRemoteControl`, `allowManagedHooksOnly`.
- An invalid managed settings file makes Claude Code refuse to start. `/status` shows the settings source.
- "A list with only URL entries blocks local stdio servers." The docs say a server not matched by the allowlist is blocked, and a stdio server cannot match a `serverUrl` entry. Confirmed.
- Plugin auto-update is on by default for official marketplaces and off for others.
- `Bash(git push *)` does not match `git -C . push`.

### VS Code

- All named policies exist: `AllowedExtensions` (from 1.96), `ExtensionsAutoUpdateDelay`, `ExtensionGalleryServiceUrl`, `ChatMCP`, `ChatAllowedMcpServers`, `McpGalleryServiceUrl`, `ChatAgentSandboxEnabled` (marked deprecated), `ChatAgentNetworkFilter`, `ChatToolsAutoApprove`, `ChatToolsEligibleForAutoApproval`, `ChatApprovedAccountOrganizations`, `CopilotSessionSync`, `BrowserChatTools`, `ChatStrictPluginOnlyCustomization`.
- `AllowedExtensions` does not verify where a VSIX came from.
- The agent sandbox does not block outbound network by default, is not a VM boundary, is experimental on Windows, and passes Git and `gh` credentials in by default. Managed enforcement is in preview.
- `task.allowAutomaticTasks` is off by default and never runs in an untrusted workspace.
- Dev Containers forward the SSH agent and reuse the Git credential helper.
- Dev Tunnels group policies apply to Windows only.

### Codex

- Default: no network, writes limited to the workspace.
- `[permissions.filesystem] deny_read` exists and users cannot weaken it. A read-only default does not hide files.
- `mcp_servers` allowlist with `identity = { command = ... }` or `{ url = ... }`. The string form of `identity.command` does not inspect arguments. An empty `mcp_servers` table disables all MCP servers.
- `allowed_permission_profiles` with a managed `default_permissions` needs 0.138.0 or later.
- `allowed_sandbox_modes`, `allowed_approval_policies`, `allowed_approvals_reviewers`, `[experimental_network] enabled = true`, limited Windows support.

### npm and GitHub

- npm 12.0.0 was published on 8 July 2026. Dependency install scripts are off by default.
- `npm install` runs a root `.npm-extension.mjs` or `.cjs`. `npm ci` "does not import or execute" it and only checks the recorded hash.
- `dangerously-allow-all-scripts` runs every dependency install script. npm calls it a "migration escape hatch only".
- Config precedence is cli, env, project, user, global, so a managed `min-release-age` is only a default.
- GitHub package firewall: public preview since 20 October 2026, Enterprise Cloud, npm only.
- CODEOWNERS needs "Require review from Code Owners" to be enforced.
- GitHub's managed `Read(...)` deny rules apply to Copilot Agent Host sessions in VS Code.

### MCP, Git, SSH, Defender

- MCP spec 2025-06-18: servers must validate `Origin`, should bind to localhost and should authenticate.
- MCP security guidance: servers must not accept tokens not issued for them.
- OWASP MCP Top 10 (beta): MCP01, MCP03, MCP07 and MCP08 carry the names the page uses.
- `git-credential-store` keeps credentials unencrypted in `~/.git-credentials`.
- `ssh-add -c` asks for confirmation on each use.
- Defender `DeviceProcessEvents` has the columns the hunting queries use.
- Microsoft incident response guidance says not to destroy forensic evidence.

### Incidents and research

- ChainDrop: Microsoft, 4 August 2026, more than 400 npm packages.
- s1ngularity: August 2025, ran `claude`, `gemini` and `q` with permission checks off.
- Amazon Q extension 1.84.0: mis-scoped GitHub token, code failed to run because of a syntax error (AWS bulletin).
- GlassWorm 2026 variants install into VS Code, Cursor and Windsurf (Socket).
- CVE-2025-48384: macOS and Linux affected, Windows not (Datadog).
- CVE-2025-53773: prompt injection writes `"chat.tools.autoApprove": true` (Embrace The Red).
- Check Point: CVE-2025-59536 and CVE-2026-21852; the hooks finding had no CVE named.
- GhostApproval: Wiz, 8 July 2026, six agents, symlink to files such as `~/.ssh/authorized_keys`.
- Plugin4Shell: disclosed 18 September 2026; fixed in Claude Code 2.1.179 and Codex 0.146.0; no Copilot fix; Gemini CLI not being fixed; CSA says auto-update is on by default in Claude Code and Codex.
- GitSpawn: Manifold, 1 September 2026, eight findings across seven agents, four unpatched, second Claude Code path open on 2.1.252, a plain clone does nothing. The Hacker News report (2 September) agrees.
- Gen Digital, 8 September 2026: infostealers collect tokens, MCP configuration and prompt histories; figures are detections among protected users.
- Forever Security via Help Net Security: planted AGENTS.md in Downloads, Codex changed its own settings first, about a quarter of sessions open a browser.
- Mitiga, 5 May 2026: a hook rewrites MCP addresses in `~/.claude.json`.
- OWASP AST01: skills write into the agent's identity file and survive uninstall.
- Contagious Interview: `tasks.json` with `runOn: folderOpen` (The Hacker News, 20 January 2026).
- Grok Build 0.2.93 uploaded whole Git repositories to xAI storage (The Hacker News, 14 July 2026).
- VS Code tunnels used by attackers: Unit 42 describes `code.exe tunnel` with GitHub sign-in. Security Affairs reports Operation Digital Eye relying on VS Code Remote Tunnels.

## Observations

1. **npm 12.2.1 is no longer current. Low, drift.** The page says "12.2.1 is current on the npm registry". The registry's `latest` tag was 12.2.2 on 10 November 2026, published 4 November 2026. 12.2.1 was published 15 October 2026, so the sentence was true on the page's date. How known: npm registry API queried today.

2. **Codex network table has a new name. Low, drift.** The page names `[experimental_network]`. OpenAI's managed configuration page now says that in Codex 0.166.0 `[network_proxy]` is the canonical table and the older name is still accepted. It also advises keeping `[experimental_network]` until every client supports the new name, so the page's advice still works. It was not checked whether this text was on the OpenAI page on 1 November. How known: OpenAI docs fetched today.

3. **Four source titles have changed. Low, cosmetic.** The links still work. How known: live page titles today.
   - "Claude Code: discover and install plugins" is now "Install and manage plugins".
   - "Claude Code: sandboxing" is now "Configure the sandboxed Bash tool".
   - "Responsible use of GitHub Copilot cloud agent" is now "Application card: GitHub Copilot Agents".
   - "Stealing MCP tokens in Claude Code via ~/.claude.json" is now "MCP Token Theft in Claude Code: A Man-in-the-Middle Attack Chain".

4. **Sandbox and `WebFetch` rules are linked. Low, nuance, not an error.** The page treats the sandbox's domain list and permission rules as separate. Anthropic's docs say `WebFetch(domain:...)` allow rules also feed the sandbox's allowed domains. No statement on the page is wrong because of this.

## Not checked

- **ClawHavoc count of at least 1,184 skills (Antiy CERT).** The site refused the connection. The Snyk source that was read does not contain the figure.
- **The Register on Plugin4Shell.** Blocked by a bot check. The Plugin4Shell claims were confirmed from the CSA research note instead.
- **"GlassWorm has hit Open VSX in waves since October 2025."** The cited Socket article confirms the 2026 waves but does not give the October 2025 start. The earlier-wave article was not fetched.
- **OWASP Agentic Top 10 names (ASI01 to ASI10).** The OWASP page is a download page for a PDF, which was not opened. The names on the page match the list as known to AI, which is not a check against the source.
- **CISA KEV date for CVE-2025-48384 (25 August 2025).** SecurityWeek confirms the flaw was exploited and that CISA warned about it. The date itself was not checked against the KEV catalogue.
- **Forever Security's own report.** Its claims were checked against the Help Net Security article the page cites, not against Forever Security's original write-up.
- **Interpretation by AI on the page**: the priority order, the OWASP mapping, the placement of risks on the map and the friction estimates. These are judgements, so there is no source to check them against.
- **Behaviour on real machines.** No policy, setting, command or hunting query was run.
