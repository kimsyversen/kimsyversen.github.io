# Fact check: MCP Risk Map

Belongs to [MCP-Risk-Map.html](MCP-Risk-Map.html). Other notes for the same page: [plan](MCP-Risk-Map.plan.md), [decisions](MCP-Risk-Map.decisions.md). Cut from [Developer-WS.html](Developer-WS.html).

Checked 2 November 2026. Sources were opened that day. Page checked: `MCP-Risk-Map.html`, MD5 `a35d1813dcbad214fb87ee1bf9c28e1e`.

## What was found

- Every factual claim on the page is listed below with its source and verdict.
- Spec rows were re-checked on 2 November 2026 against version 2026-07-28 (current). The earlier pages used 2025-06-18 and the draft.
- 4 claims in the first draft had no support in the sources read and were removed (see **Removed**).
- Only one MCP-specific attack (Mitiga) is cited. For the other seven risks no incident was verified, and the page says so.
- Not run: no setting, command or product behaviour on this page was tested on a real machine. Rendering was checked in a browser (no console errors, tabs, popovers, status tally, phone width).

Sources: **OWASP** = owasp.org/www-project-mcp-top-10. **SPEC-T** = MCP specification 2026-07-28 (current version per the versioning page), Streamable HTTP. **SPEC-D** = MCP security best practices, 2026-07-28. **MITIGA** = mitiga.io blog on Claude Code MCP token theft. **CC** = code.claude.com managed-mcp. **CODEX** = Codex managed configuration. **VSC** = VS Code enterprise policies.

| Verdict | Meaning |
| --- | --- |
| OK | Matches the source named. |
| JUDGEMENT | My own grouping, order or advice, tagged `[inference]` on the page. These are checklist questions and ratings, not factual claims. |
| CUT | Removed from the page because no source supports it. |
| CONTESTED | Sources or parties disagree; the page shows both. |

## Statements

| # | Statement (short) | Source | Verdict |
| --- | --- | --- | --- |
| 1 | OWASP MCP Top 10 is beta; IDs MCP01 to MCP10 and their names as mapped | OWASP | OK |
| 2 | Claude Code: by default anyone can connect any MCP server | CC | OK |
| 3 | Anthropic reviews connectors before listing them in its Directory, but does not security-audit or manage any MCP server | CC security page, MCP section (checked 2 Nov 2026, verbatim) | OK |
| 4 | `managed-mcp.json` gives a fixed set; empty `mcpServers` disables MCP | CC | OK |
| 5 | `allowedMcpServers` with `allowManagedMcpServersOnly`; denylist wins | CC | OK |
| 6 | Once any `serverUrl` entry exists every remote server must match a URL; same for `serverCommand` and stdio | CC | OK |
| 7 | `serverName` is not a security control | CC | OK |
| 8 | Codex `[mcp_servers.<name>]` allowlist in `requirements.toml` | CODEX | OK |
| 9 | VS Code `ChatAllowedMcpServers` exists as an allowlist (names only, no `chat.mcp.access` values) | VSC | OK |
| 10 | Local servers: allow by exact command; Claude does not compare `env` | CC | OK |
| 11 | Codex string `command` form does not check args, cwd, env; structured form is stricter | CODEX | OK |
| 12 | Spec: local server compromise risks are malicious startup command, arbitrary code execution, no visibility, data exfiltration | SPEC-D | OK |
| 13 | Client with one-click local setup must get consent and show the full command | SPEC-D | OK |
| 14 | Clients should sandbox local servers; server authors should use stdio or restrict HTTP | SPEC-D | OK |
| 15 | Removed from the page: "clients should support stdio" is in 2025-06-18 but not on the current stdio page | SPEC-T | CUT |
| 16 | Clients should run local servers sandboxed with minimal default privileges (the page no longer says anything about product support) | SPEC-D | OK |
| 17 | Tool poisoning, prompt injection, over-sharing and audit gaps are OWASP categories (MCP03, MCP06, MCP10, MCP08) | OWASP | OK |
| 18 | Tool poisoning and prompt injection are OWASP categories; the mechanism sentences were cut | OWASP | OK |
| 19 | Mitiga: npm postinstall hook edits `~/.claude.json` and points an MCP server URL at an attacker localhost proxy | MITIGA | OK |
| 20 | The proxy captured OAuth bearer and refresh tokens (Atlassian example) | MITIGA | OK |
| 21 | Needs code execution through the npm install | MITIGA | OK |
| 22 | The hook also pre-set trust-dialog flags and added a project SessionStart hook | MITIGA | OK |
| 23 | Mitiga published 5 May 2026, updated 30 October 2026 | MITIGA | OK |
| 24 | Mitiga recommends baselining endpoints, watching `~/.claude.json` and project MCP files, alerting on new local proxies, and says rotating tokens alone is not enough | MITIGA | OK |
| 25 | Anthropic called it out of scope and by design; Mitiga disagrees | MITIGA | CONTESTED |
| 26 | Stolen broad token has a larger blast radius; draft recommends progressive least-privilege scopes | SPEC-D | OK |
| 27 | Token passthrough is forbidden: a server must not accept tokens not issued for it | SPEC-D | OK |
| 28 | Confused deputy: per-client consent, exact `redirect_uri` match, single-use `state` | SPEC-D | OK |
| 29 | Local HTTP servers must validate `Origin`, should bind to 127.0.0.1 not 0.0.0.0, should authenticate | SPEC-T | OK |
| 30 | DNS rebinding can reach local servers from web pages | SPEC-T | OK |
| 31 | A malicious server can supply URLs pointing at internal addresses such as 169.254.169.254 | SPEC-D | OK |
| 32 | Clients should require HTTPS and block private and reserved ranges; operators should consider an egress proxy | SPEC-D | OK |
| 33 | Authorization URLs: allow only http and https, reject `javascript:`, never open with shell commands | SPEC-D | OK |
| 34 | Claude Code usage can be monitored with OpenTelemetry; `OTEL_LOG_TOOL_DETAILS=1` is the variable the docs name | CC | OK |
| 35 | `managedMcpServers` needs Claude Code 2.1.259 or later | CC | OK |
| 36 | Removed: supplier controls code, data may be retained, tool results reach the model provider (no source read) | none | CUT |
| 37 | The eight-risk grouping, order, map placement and friction ratings | none | JUDGEMENT (labelled on the page) |
| 38 | Every first-control row on Where to start | CC, CODEX, SPEC, MITIGA | OK for the setting; friction is JUDGEMENT |
| 39 | The page was checked against spec 2026-07-28, the current version on 2 November 2026: Origin MUST, localhost SHOULD, auth SHOULD, and the best-practices text all match | SPEC-T, SPEC-D | OK |

## Removed

These are not on the page, because no source I read states them:

- That Anthropic reviews connectors in a Directory.
- That the SessionStart hook "reapplies" the config, and that the redirect "stays in place".
- A "consent cookie" detail in the confused-deputy line, and the three consequences of passthrough.
- "Check redirects" and "in OAuth metadata" in the SSRF lines.
- "Clients should support stdio" (not on the 2026-07-28 stdio page).
- Remote servers as suppliers who may retain data; the model cannot tell instructions from data; tool results reach the model provider; "product support differs, not tested".

## Left out on purpose

- The VS Code `chat.mcp.access` values: Microsoft's docs and source disagree.
- Plugin4Shell: it is about plugin pinning, not MCP.
- Any MCP incident besides Mitiga: none was verified.
- Codex plugin-bundled servers: not on the page.

## Limits

- The spec can change after 2 November 2026.
- No setting or command was run on a real machine; every product claim rests on its vendor docs.

## Learner additions (2 November 2026)
- "How MCP works" box: client, server, tools, stdio and HTTP. Matches the MCP specification transports page (2026-07-28). General description, no new claims.
- Glossary: DNS rebinding and the Origin check, confused deputy, token passthrough, SSRF and egress proxy use the wording of the specification security best practices page (2026-07-28). Token, scope, allowlist, sandbox and prompt injection are general definitions, not tied to one source.
- "In plain words" line per risk: restates the risk paragraph in simpler words. Judgement, no new facts.
- "How to set it": the vendor setting names and matching rules moved here unchanged from the check lists (M01, M02).

## VS Code tab (2 November 2026)
Source pages (code.visualstudio.com/docs): agent-customization/mcp-servers (A), agents/run/manage-mcp-servers (B), agents/reference/mcp-configuration (C), copilot/security (D), enterprise/policies (E), enterprise/telemetry (F). Text was read from the fetched pages. Nothing was run in VS Code.

| Row | Statement | Source | Verdict |
|---|---|---|---|
| V1 | Servers are added through gallery, MCP: Add Server, user mcp.json, .vscode/mcp.json, root .mcp.json, devcontainer.json, code --add-mcp | A, B, C | OK |
| V2 | Discovery: Copilot CLI on by default; Claude Desktop, Cursor, Windsurf off by default | C | OK |
| V3 | Workspace mcp files inherit Workspace Trust; restricted mode blocks start; trusted workspace starts without separate prompt, also after config changes | B | OK |
| V4 | chat.mcp.autostart experimental, default newAndOutdated, starts never-run or changed servers on chat message; never does not stop Copilot harness | B, C | OK |
| V5 | Trust plus autostart means a changed entry can start on the next chat message | V3 + V4 | JUDGEMENT, tagged [inference], not tested |
| V6 | Per-server sandbox, stdio only, macOS and Linux only, tool confirmations auto-approved | B, C, D | OK |
| V7 | MCP tool approval at session, workspace or user level; Allow all and Autopilot auto-approve; ChatToolsAutoApprove turns global auto-approval off | D | OK |
| V8 | Secure credentials store for sensitive inputs; OAuth per MCP authorization spec; do not commit secrets | D, B | OK |
| V9 | Settings Sync can sync user mcp.json, not workspace .mcp.json | B | OK. The "bad entry could spread" part is [inference], not observed |
| V10 | chat.mcp.serverSampling sets which models are exposed to servers | C | OK |
| V11 | Policies ChatMCP, ChatAllowedMcpServers, ChatAllowManagedMcpServersOnly, ChatDeniedMcpServers, McpGalleryServiceUrl; allowlist and deny precedence | E | OK. chat.mcp.access values left out on purpose |
| V12 | Claude and Codex harnesses cannot enforce Copilot enterprise-managed settings and are disabled when they apply | D | OK |
| V13 | MCP: Show Installed Servers; Copilot Chat OTel export covers tool execution | C, F | OK |
| V14 | Docs example runs npx -y @playwright/mcp@latest | B | OK. "Pinning avoids silent change" is [inference] |
