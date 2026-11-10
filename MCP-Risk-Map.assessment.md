# MCP-Risk-Map.html: content assessment

Belongs to [MCP-Risk-Map.html](MCP-Risk-Map.html). Written by AI on 9 November 2026.

Page version assessed: commit `a867618`, file SHA-256 `4aaa95e6...0d8c95` (same hash the fact check records as reviewed). The page was not changed.

## Verdict

No factual error was found. Every claim that was checked matches its source as the source reads today.

Three small things are worth knowing. None of them makes the page wrong. They are listed under "Observations".

This is a check of the page against documents. It is not a test of any product. See "Not checked".

## What was checked, and how

All sources were fetched fresh on 9 November 2026.

| Area | Method | Result |
|---|---|---|
| All 135 quotes | Ran `scripts/check-mcp-risk-map.py` against freshly fetched sources | "135 quotes, 98 reviewed texts, 0 problems". Two quotes (`cxcmd`, `studio3`) match only when whitespace is ignored. |
| General view, unquoted claims | Searched the fetched source text for each claim | All found. Details below. |
| VS Code table, 14 rows | Fetched 8 VS Code docs pages and searched for each setting, default and behaviour | All found. Details below. |
| Microsoft view, 14 cards, 10 rows, 6 notes | Read every summary sentence beside its quotes, and looked up the parts a quote did not cover | All supported. Details below. |
| Framework mapping | Counted entries in the page data | 10 OWASP entries, CoSAI numbers 1 to 34 with no gaps or repeats, 14 risk cards. |
| Section links | `python3 -I scripts/section_anchors.py --check` | Exit code 0. |

### General view: claims confirmed

- **Claude Code** (code.claude.com/docs/en/managed-mcp). `managedMcpServers` "Requires Claude Code v2.1.259 or later". Denylist entries always apply. Server name is "not a security control". The `env` block is not compared. In-process SDK servers skip the checks. Some managed and built-in servers skip the allowlist. An empty server map blocks every server "except the ones that load under exclusive control". OpenTelemetry export and `OTEL_LOG_TOOL_DETAILS=1` are documented under "Monitor MCP usage".
- **Codex** (managed configuration page). The string form of `identity.command` "doesn't inspect args, cwd, env, or env_vars". The structured form checks executable, argument count and argument order, and still does not inspect `cwd`, `env` or `env_vars`.
- **MCP specification 2026-07-28.** The versioning page says "The current protocol version is 2026-07-28". The page's "must" and "should" words match the specification in every case checked:
  - One-click local setup: client MUST show the full command and ask. Sandbox with minimal privileges: SHOULD. stdio or restricted HTTP for local servers: SHOULD.
  - Origin header: MUST. Bind to 127.0.0.1: SHOULD. Authentication: SHOULD.
  - Authorization URLs: MUST allow only HTTPS (HTTP for loopback in development), MUST reject `javascript:` and similar, MUST NOT open URLs through a shell.
  - OAuth discovery checks (HTTPS, private ranges, redirects): SHOULD. Egress proxy: "SHOULD consider".
  - Tools: "Servers MUST ... Rate limit tool invocations". Human in the loop: SHOULD.
  - Tokens: "MCP servers MUST NOT accept any tokens that were not explicitly issued for the MCP server".
  - Proxy servers: per-client consent, exact redirect URI match and single-use state are all under MUST.
- **Mitiga.** Published 5 May 2026. npm postinstall hook, edit of `~/.claude.json`, localhost proxy, Atlassian token, SessionStart hook that restores the endpoint, and Anthropic's "out-of-scope" and "by design" reply are all in the article. The three recommendations (baseline endpoints, watch the config files, alert on new local proxies) are there too.
- **OWASP MCP Top 10.** "Phase 3, Beta Release and Pilot Testing, We are here right now". The ten names match.
- **CoSAI paper.** "Status: Draft" and "Approved by the CoSAI Project Governing Board on 8 January 2026" are both in the PDF.

### VS Code table: claims confirmed

Add routes (`MCP: Add Server`, `code --add-mcp`, Dev Containers, Find MCP Servers in Customizations, legacy gallery). Copilot Global path `$COPILOT_HOME/mcp-config.json` with `~/.copilot/mcp-config.json` as fallback. Experimental `chat.mcp.workspaceRootConfig.enabled`. Older destinations "labeled deprecated in the guided flow". Discovery defaults (Copilot CLI on, all others off). Workspace Trust and Restricted mode. `chat.mcp.autostart` is experimental, default `newAndOutdated`, and does not stop Copilot harness sessions. Per-server sandbox on macOS and Linux only, with tool confirmations auto-approved. `chat.agent.sandbox.mcpServers`, and "Windows support is Experimental" on Windows 11. `ChatToolsAutoApprove`. Input variables not forwarded to Copilot harness sessions. Settings Sync covers the user-profile `mcp.json` only. `chat.mcp.serverSampling`. The five policy names, with "deny rules always take precedence". Claude and Codex harnesses disabled under enterprise-managed settings. `MCP: Show Installed Servers`. OpenTelemetry export covering tool execution. The `npx -y @playwright/mcp@latest` example.

### Microsoft view: claims confirmed

Every summary sentence is supported by its quotes. Parts not covered by a quote were looked up and found:

- GitHub lists live in `managed-settings.json`. A malformed list is treated "as an empty allowedMcpServers list".
- Visual Studio prompts on changes to configuration or capabilities. Trust prompts can be turned off in Tools > Options.
- Both CVE records are published and assigned by Microsoft, so "vendor advisory" is right. Scores 8.8 and 9.1 match.
- M10, M11 and M12 say no Microsoft source was reviewed and carry `[unverified]`. That is an honest label, not a gap in accuracy.

## Observations

None of these is a factual error. All are rated low.

1. **Microsoft map shows General notes for M09.** Low. Read from the script, not checked in a browser.
   The script has `NEWR = ["M09","M10","M11","M12"]` (line 1040) and adds the General map notes for those four risks to the Microsoft map (line 1052). M10 to M12 have no Microsoft notes, so that is needed. M09 now has two Microsoft notes of its own (Visual Studio tool confirmation), so on the Microsoft map it gets four notes: two Microsoft, two product neutral (CoSAI and the specification). The notes are true and cited. The mix may or may not be intended.
   Related: `MCP-Risk-Map.decisions.md` line 101 still says the Microsoft view shows "not assessed" on M09 to M12. For M09 that is out of date.

2. **Mitiga article was updated after the cited date.** Low.
   The article shows "May 5, 2026" and "Updated On October 30, 2026". The page says "Mitiga (May 2026)". The claims on the page match the updated text, so nothing is wrong today.

3. **One clause is shortened.** Low.
   The Claude Code docs say Anthropic reviews connectors "against its listing criteria" before adding them to its directory. The page says it reviews them before listing them. The meaning that matters (no security audit) is kept and quoted.

Also noted, no action needed: the section id `the-eight-risks` sits under the heading "The fourteen risks". AGENTS.md says existing ids must not change, so this is correct as it is.

## Not checked

- No product setting, policy or command was run. The page says the same about itself.
- No attack was reproduced.
- The page was not opened in a browser for this assessment. The fact check also says its last browser check after the tab change was not completed.
- The General view's quoted claims were covered by the automated quote check and by topic searches. They were not each read one by one beside their quote, as the Microsoft view was.
- Whether each of the 34 CoSAI threats and 10 OWASP entries has the best home risk is a judgement (interpretation by AI on the page). Names and numbers were checked. The choice of home was not audited.
- Statements tagged `[inference]` are interpretation by AI and have no source to check against.
- Sources change. This holds for 9 November 2026 only.
