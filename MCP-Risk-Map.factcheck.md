Belongs to [MCP-Risk-Map.html](MCP-Risk-Map.html).

# Statement review: 5 November 2026

This review supersedes the 2 November ledger retained below. All listed external primary sources were opened on 5 November 2026. The page was read in full, including static prose, glossary, VS Code rows, and JavaScript-generated popovers, first controls, evidence and source descriptions. Each inventory row below records one sentence or a short inseparable source-backed unit. Advice and questions are not empirical findings.

## Findings corrected

- The host is distinct from its MCP clients. Servers need not expose tools. Context inclusion is a host decision.
- Local process privileges depend on the execution account and isolation. Remote servers need not hold upstream tokens. MCP does not force all data off the machine.
- A token is authorization, not universally proof of a human login. Bearer use is limited by validity, permissions and service checks.
- Empty Claude Code managed MCP configuration is not a universal shutdown. SDK, built-in, managed and connector exceptions are documented. Deny precedence is scoped to servers that undergo those checks.
- A URL-only Claude allowlist does not permit arbitrary stdio commands: unmatched stdio entries are blocked. Command identity does not prove code integrity.
- Structured Codex command matching checks argument count and order, but not cwd or environment variables.
- Mitiga demonstrates bearer-token interception/reuse. Separate refresh-token capture is not demonstrated in the article. Its vendor-response account is attributed, not independently confirmed. The persistent hook must be removed during remediation.
- Authorization HTTP is limited to development loopback. SSRF checks cover OAuth discovery and redirects; server-side client egress guidance is scoped accordingly.
- VS Code editor per-server and Copilot harness sandboxes are separate. Windows support exists for the latter on supported systems. Saved approvals and auto-approval mean every tool call need not prompt.
- Secret inputs are configuration-format and harness dependent. Editor policies do not cover every independently discovered Copilot runtime server.
- Package version pinning reduces drift but is not a guarantee of immutable dependencies or safety.

## Evidence limits

No exploit, managed-client setting, OAuth flow, server installation or vendor enforcement was reproduced. Product statements report documentation, not measured behavior. Mitiga is research, not an independently confirmed victim incident. This audit does not claim that other incidents do not exist. Diagram topology, risk grouping, friction ratings, suggested controls and status definitions are editorial judgements. The diagram's named components and arrows are a reference scenario, not an inventory of a real organization.

Source keys below apply to the relevant named sections, not to unrelated statements on those pages. SELF denotes statements about this artifact, its behavior or this review. REVIEWED means checked against the named sources with the qualifiers present in the final page, not proof of universal implementation compliance.

## Primary sources

- **ARCH**: [MCP architecture](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture), opened 5 November 2026.
- **TOOLS**: [MCP tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools), opened 5 November 2026.
- **STDIO**: [MCP stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio), opened 5 November 2026.
- **HTTP**: [MCP Streamable HTTP, Security & Endpoint](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http#security-endpoint), opened 5 November 2026.
- **SEC**: [MCP Security Best Practices, relevant named subsection](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices), opened 5 November 2026.
- **VER**: [MCP versioning](https://modelcontextprotocol.io/specification/versioning), opened 5 November 2026.
- **OWASP**: [OWASP MCP Top 10, phase 3 and entries MCP01 to MCP10](https://owasp.org/www-project-mcp-top-10/), opened 5 November 2026.
- **CC**: [Claude Code managed MCP, matching / exceptions / monitoring](https://code.claude.com/docs/en/managed-mcp), opened 5 November 2026.
- **CODEX**: [OpenAI managed configuration, Enforce command rules from requirements](https://learn.chatgpt.com/docs/enterprise/managed-configuration), opened 5 November 2026.
- **MITIGA**: [Mitiga research, five-step chain / disclosure / FAQ](https://www.mitiga.io/blog/claude-code-mcp-token-theft-mitm), opened 5 November 2026.
- **VADD**: [VS Code add MCP servers](https://code.visualstudio.com/docs/agent-customization/mcp-servers), opened 5 November 2026.
- **VMAN**: [VS Code manage MCP servers](https://code.visualstudio.com/docs/agents/run/manage-mcp-servers), opened 5 November 2026.
- **VCONF**: [VS Code MCP configuration reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration), opened 5 November 2026.
- **VSEC**: [VS Code AI security, approvals / sandboxing / policy gaps](https://code.visualstudio.com/docs/agents/run/security), opened 5 November 2026.
- **VPOL**: [VS Code device policy reference](https://code.visualstudio.com/docs/enterprise/policies), opened 5 November 2026.
- **VMGMT**: [VS Code manage AI settings, harness availability and coverage](https://code.visualstudio.com/docs/enterprise/manage-ai-settings), opened 5 November 2026.
- **VOTEL**: [VS Code enterprise telemetry, OpenTelemetry support](https://code.visualstudio.com/docs/enterprise/telemetry), opened 5 November 2026.
- **OAUTH**: [RFC 6749, sections 1.4, 3.3, 4.4](https://www.rfc-editor.org/rfc/rfc6749.html), opened 5 November 2026.
- **BEARER**: [RFC 6750, bearer token usage](https://www.rfc-editor.org/rfc/rfc6750), opened 5 November 2026.
- **SELF**: [Page source and review scope](MCP-Risk-Map.html), opened 5 November 2026.

## Complete statement inventory

| # | Location | Final statement | Evidence | Verdict |
| --- | --- | --- | --- | --- |
| 1 | intro , line 271 | Risk map · MCP servers and AI agents | ARCH, SEC | REVIEWED |
| 2 | intro , line 273 | Where the main risks sit when developers connect AI agents to MCP servers, what to check for each, and where to start. | ARCH, SEC | REVIEWED |
| 3 | intro , line 273 | The detail is kept low on purpose. | SELF | REVIEWED |
| 4 | intro , line 273 | Exceptions exist. | SELF | REVIEWED |
| 5 | p-map , line 295 | The host is the AI application. | ARCH, SEC | REVIEWED |
| 6 | p-map , line 295 | Its MCP clients connect to servers. | ARCH, SEC | REVIEWED |
| 7 | p-map , line 295 | Servers can offer tools for the agent to call; a server need not offer tools. | ARCH, SEC | REVIEWED |
| 8 | p-map , line 296 | A local server is a program on your computer. | ARCH, SEC | REVIEWED |
| 9 | p-map , line 296 | With the stdio transport the client starts it and talks to it over its standard streams. | ARCH, SEC, STDIO | REVIEWED |
| 10 | p-map , line 296 | A server can also run behind an HTTP address, on your computer or elsewhere. | ARCH, SEC | REVIEWED |
| 11 | p-map , line 297 | The client sends tool arguments to a server and receives results. | ARCH, SEC | REVIEWED |
| 12 | p-map , line 297 | The host decides how to use those results, including whether to include them in the model's context. | ARCH, SEC | REVIEWED |
| 13 | p-map , line 303 | An MCP server can offer tools. | ARCH, SEC | REVIEWED |
| 14 | p-map , line 303 | An unrestricted local server can act with the launching account's privileges. | ARCH, SEC | REVIEWED |
| 15 | p-map , line 303 | A remote server receives the data sent to it; authentication and token storage depend on the deployment. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 16 | p-map , line 304 | The main questions are: which servers are allowed, what can each one reach, and who would notice if one changed? [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 17 | p-map , line 305 | Only one MCP-specific research demonstration is cited here (Mitiga, May 2026). | MITIGA | REVIEWED |
| 18 | p-map , line 305 | The other risks come from OWASP categories or specification warnings, and no incident is cited for them. | OWASP | REVIEWED |
| 19 | p-map , line 311 | An access token authorizes access to a service. | BEARER, OAUTH, SEC | REVIEWED |
| 20 | p-map , line 311 | A valid bearer token can be used by whoever holds it, within its permissions and other service checks. | BEARER, OAUTH, SEC | REVIEWED |
| 21 | p-map , line 311 | Tokens do not always represent a human user. | BEARER, OAUTH, SEC | REVIEWED |
| 22 | p-map , line 312 | A named permission requested or granted during authorization. | SELF | REVIEWED |
| 23 | p-map , line 312 | The service must still enforce access checks. | SELF | REVIEWED |
| 24 | p-map , line 313 | A list of permitted servers, enforced within the control's scope and documented exceptions. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 25 | p-map , line 314 | An isolation mechanism that restricts access to resources such as files and networks. | SELF | REVIEWED |
| 26 | p-map , line 314 | Its protection depends on its rules and implementation. | SELF | REVIEWED |
| 27 | p-map , line 315 | Malicious instructions in content the agent reads that may steer its behavior. | OWASP, VSEC | REVIEWED |
| 28 | p-map , line 315 | They can be visible or hidden. | SELF | REVIEWED |
| 29 | p-map , line 316 | An attacker changes where a domain resolves, potentially letting a web page reach a local server. | ARCH, SEC | REVIEWED |
| 30 | p-map , line 316 | Streamable HTTP servers must validate Origin; an invalid supplied origin requires HTTP 403. | ARCH, HTTP, SEC | REVIEWED |
| 31 | p-map , line 316 | Local binding and authentication provide additional protection. | SELF | REVIEWED |
| 32 | p-map , line 317 | A proxy server that connects clients to another service can be tricked into giving an attacker a login code without the user agreeing. | ARCH, SEC | REVIEWED |
| 33 | p-map , line 318 | A server accepts a token that was not made for it and passes it on. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 34 | p-map , line 318 | The specification forbids this. | SELF | REVIEWED |
| 35 | p-map , line 319 | Tricking a client into requesting addresses it should not, such as internal systems or a cloud metadata address. | ARCH, SEC | REVIEWED |
| 36 | p-map , line 320 | A gate that outbound traffic must pass. | SELF | REVIEWED |
| 37 | p-map , line 320 | It can block internal destinations. | SELF | REVIEWED |
| 38 | p-map , line 326 | From where servers and content come from, through the agent and its servers, to what goes out. | ARCH, SEC | REVIEWED |
| 39 | p-map , line 326 | Each marker shows where a risk enters or must be controlled. | SELF | REVIEWED |
| 40 | p-map , line 326 | M01 to M08 are coloured by the status you set under Risks. | SELF | REVIEWED |
| 41 | p-map , line 337 | Servers, packages, config and content (1) reach the workstation (2), where this example places the agent, local servers and client credentials. | ARCH, SEC | REVIEWED |
| 42 | p-map , line 337 | Traffic leaves through the egress boundary (3), a control point only where traffic is forced through a proxy or gateway. | SELF | REVIEWED |
| 43 | p-map , line 337 | Governance and monitoring (4) covers every layer. | SELF | REVIEWED |
| 44 | p-map , line 338 | Arrows show selected paths, not every data flow. | SELF | REVIEWED |
| 45 | p-map , line 338 | Select a marker or a box to see its risks. | SELF | REVIEWED |
| 46 | p-map , line 348 | The diagram is wide. | SELF | REVIEWED |
| 47 | p-map , line 348 | Drag sideways in it, or use the table below. | SELF | REVIEWED |
| 48 | p-map , line 352 | The same placement as the diagram. | SELF | REVIEWED |
| 49 | p-map , line 352 | Select a risk to show it in the diagram. | SELF | REVIEWED |
| 50 | p-map , line 356 | Risk1 · Sources2 · Workstation3 · Outbound4 · Governance | SELF | REVIEWED |
| 51 | p-map , line 364 | This is a reference layout, not your organisation's setup. | SELF | REVIEWED |
| 52 | p-map , line 364 | Common differences: only remote servers, only local servers, servers inside dev containers, or an internal gateway in front of all servers. | ARCH, SEC | REVIEWED |
| 53 | p-map , line 364 | Draw your own variant and move the markers. | SELF | REVIEWED |
| 54 | p-map , line 365 | The placement of risks is my judgement based on the sources. [inference] | SELF | JUDGEMENT / CHECK QUESTION |
| 55 | p-risks , line 373 | Grouped from the OWASP MCP Top 10 and the specification's security guidance. | OWASP | JUDGEMENT / CHECK QUESTION |
| 56 | p-risks , line 373 | The order and the grouping are my judgement. [inference] OWASP's list is in beta and may change. | OWASP | JUDGEMENT / CHECK QUESTION |
| 57 | p-risks , line 379 | OWASP MCP Top 10: in beta (phase 3). | OWASP | REVIEWED |
| 58 | p-risks , line 379 | IDs and names can change. | SELF | REVIEWED |
| 59 | p-risks , line 380 | Specification versions: the Origin, localhost and security rules were checked against version 2026-07-28, the current one on 5 November 2026. | ARCH, HTTP, SEC, VER | REVIEWED |
| 60 | p-risks , line 380 | They can change. | SELF | REVIEWED |
| 61 | p-risks , line 381 | Claude Code: the managedMcpServers setting needs version 2.1.259 or later. | ARCH, CC, SEC | REVIEWED |
| 62 | p-risks , line 382 | Mitiga: Mitiga reports that Anthropic told it the behaviour is out of scope and by design. | BEARER, CC, MITIGA, OAUTH, SEC | REVIEWED |
| 63 | p-risks , line 382 | Mitiga disagrees. | MITIGA | REVIEWED |
| 64 | p-risks , line 382 | This page does not take a side. | SELF | REVIEWED |
| 65 | p-risks , line 388 | One suggested first control per risk. | SELF | JUDGEMENT / CHECK QUESTION |
| 66 | p-risks , line 388 | These are recommendations, and the friction is my estimate. [inference] | SELF | JUDGEMENT / CHECK QUESTION |
| 67 | p-risks , line 392 | RiskFirst controlFriction | SELF | REVIEWED |
| 68 | p-risks , line 400 | OK: in place and tested on a named product and operating system, with evidence and a date recorded elsewhere; the tracker stores status values in this browser, with no evidence attachments. | SELF | JUDGEMENT / CHECK QUESTION |
| 69 | p-risks , line 400 | Partial: covers some products, platforms or users. | SELF | JUDGEMENT / CHECK QUESTION |
| 70 | p-risks , line 400 | Missing: not in place. | SELF | JUDGEMENT / CHECK QUESTION |
| 71 | p-risks , line 400 | Unknown: looked at but not confirmed. | SELF | JUDGEMENT / CHECK QUESTION |
| 72 | p-risks , line 400 | Not assessed: nobody has looked yet. | SELF | JUDGEMENT / CHECK QUESTION |
| 73 | p-risks , line 400 | These definitions are mine. [inference] | SELF | JUDGEMENT / CHECK QUESTION |
| 74 | p-risks M01, line 424 | OWASP MCP09 Shadow MCP Servers | ARCH, OWASP, SEC | REVIEWED |
| 75 | p-risks M01, line 425 | In plain words: Without enforced restrictions, users can configure unapproved servers. | ARCH, SEC | REVIEWED |
| 76 | p-risks M01, line 425 | An allowlist limits which servers can load within its documented scope. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 77 | p-risks M01, line 426 | By default in Claude Code anyone can connect any MCP server. | ARCH, CC, SEC | REVIEWED |
| 78 | p-risks M01, line 426 | Anthropic reviews connectors before listing them in its Directory, but does not security-audit or manage any MCP server. | ARCH, CC, SEC | REVIEWED |
| 79 | p-risks M01, line 426 | So each developer decides what the agent can reach, unless policy limits it. | SELF | REVIEWED |
| 80 | p-risks M01, line 429 | Is there an approved list of servers, and is it enforced? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 81 | p-risks M01, line 430 | Does the list cover both remote servers and local ones? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 82 | p-risks M01, line 431 | Is a server's name used as the control? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 83 | p-risks M01, line 431 | Anthropic says the name is not a security control. | CC | REVIEWED |
| 84 | p-risks M01, line 434 | Claude Code: use managed allowedMcpServers with allowManagedMcpServersOnly: true. | ARCH, CC, SEC | REVIEWED |
| 85 | p-risks M01, line 434 | For servers subject to the allowlist, URL entries require remote URL matches, and command entries require stdio command matches. | ARCH, SEC, STDIO | REVIEWED |
| 86 | p-risks M01, line 434 | Matching deny rules take precedence. | SELF | REVIEWED |
| 87 | p-risks M01, line 435 | managed-mcp.json restricts user-added servers, but an empty mcpServers does not disable every server: managed-settings servers, in-process SDK servers and explicitly permitted connectors or built-ins can still load. | ARCH, CC, SEC | REVIEWED |
| 88 | p-risks M01, line 435 | SDK servers skip these checks; some managed and built-in servers skip the allowlist. | ARCH, SEC | REVIEWED |
| 89 | p-risks M01, line 435 | Review the vendor's exceptions for your session type. | SELF | REVIEWED |
| 90 | p-risks M01, line 436 | Codex: configure server identities under [mcp_servers.<name>] in managed requirements.toml. | ARCH, CODEX, SEC | REVIEWED |
| 91 | p-risks M01, line 436 | VS Code: use ChatAllowedMcpServers; review the selected harness and policy coverage. | ARCH, SEC, VCONF | REVIEWED |
| 92 | p-risks M01, line 438 | Typical findingsUnrestricted server configuration, required servers missing from the allowlist, user-assigned names used as identity checks. [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 93 | p-risks M02, line 443 | OWASP MCP04 Software Supply Chain Attacks and Dependency Tampering · MCP03 Tool Poisoning | OWASP, SEC | REVIEWED |
| 94 | p-risks M02, line 444 | In plain words: A local server is a program someone wrote. | ARCH, SEC | REVIEWED |
| 95 | p-risks M02, line 444 | If it is malicious, it can act with the launching account's privileges unless isolation restricts it. | SEC | REVIEWED |
| 96 | p-risks M02, line 445 | A local server may be installed from a package or repository, or written locally. | ARCH, SEC | REVIEWED |
| 97 | p-risks M02, line 445 | Without adequate isolation, malicious server code can execute with the MCP client's privileges. | ARCH, SEC | REVIEWED |
| 98 | p-risks M02, line 445 | No MCP-specific incident for this risk is cited here. | SEC | REVIEWED |
| 99 | p-risks M02, line 448 | Are local servers allowed by exact command rather than by name? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 100 | p-risks M02, line 449 | Who wrote each approved server, and how does it update? [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 101 | p-risks M02, line 451 | Claude Code matches serverCommand exactly but does not compare the env block. | ARCH, CC, SEC | JUDGEMENT / CHECK QUESTION |
| 102 | p-risks M02, line 451 | Matching a command does not verify the contents of its package or executable. [inference] | SEC | JUDGEMENT / CHECK QUESTION |
| 103 | p-risks M02, line 451 | Codex: the string form of command does not check args, cwd or env; the structured form checks the executable, argument count, order and matching rules. | CODEX, SEC | REVIEWED |
| 104 | p-risks M02, line 451 | It still ignores cwd, env and env_vars. | SEC | REVIEWED |
| 105 | p-risks M02, line 452 | Typical findingsServers installed from any package, no review of updates. [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 106 | p-risks M03, line 457 | OWASP MCP05 Command Injection and Execution | OWASP, SEC | REVIEWED |
| 107 | p-risks M03, line 458 | In plain words: A local server is started by a command. | ARCH, SEC | REVIEWED |
| 108 | p-risks M03, line 458 | If the client executes a malicious command, attacker code runs within the configured execution environment. | ARCH, SEC | REVIEWED |
| 109 | p-risks M03, line 459 | The MCP specification lists local server compromise as a risk: a malicious startup command in the client config, or a malicious payload in the server. | ARCH, SEC | REVIEWED |
| 110 | p-risks M03, line 459 | The results it names are arbitrary code execution, no visibility and data exfiltration. | SEC | REVIEWED |
| 111 | p-risks M03, line 462 | Does your client ask before it runs a server's command, and show the whole command? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 112 | p-risks M03, line 462 | The specification (2026-07-28) says a client with one-click local setup must. | ARCH, SEC, VER | REVIEWED |
| 113 | p-risks M03, line 463 | Does your client sandbox local servers? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 114 | p-risks M03, line 463 | The specification says clients should run them with minimal default privileges. | ARCH, SEC | REVIEWED |
| 115 | p-risks M03, line 464 | Is stdio used where possible? | SEC, STDIO | JUDGEMENT / CHECK QUESTION |
| 116 | p-risks M03, line 464 | The specification says server authors should use stdio, or restrict HTTP with an auth token or unix sockets. | ARCH, BEARER, OAUTH, SEC, STDIO | REVIEWED |
| 117 | p-risks M03, line 467 | Typical findingsOne-click setup that hides the command, servers started with no sandbox. [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 118 | p-risks M04, line 472 | OWASP MCP06 Prompt Injection via Contextual Payloads | OWASP, VSEC | REVIEWED |
| 119 | p-risks M04, line 473 | In plain words: The agent reads text that tools bring back. | SELF | REVIEWED |
| 120 | p-risks M04, line 473 | If that text hides instructions, the agent may follow them. | OWASP, VSEC | REVIEWED |
| 121 | p-risks M04, line 474 | A tool can read pages, tickets or files that someone else wrote. | SELF | REVIEWED |
| 122 | p-risks M04, line 474 | Hidden instructions in that text can steer the agent. | OWASP, VSEC | REVIEWED |
| 123 | p-risks M04, line 474 | OWASP lists this as a category; no MCP-specific incident is cited here. | OWASP | REVIEWED |
| 124 | p-risks M04, line 477 | Which servers read content you do not control (web, tickets, mail, shared files)? [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 125 | p-risks M04, line 478 | Are untrusted reading tasks separated into sessions without tools that can write, send or run things? [inference] | SELF | JUDGEMENT / CHECK QUESTION |
| 126 | p-risks M04, line 479 | Does a person approve tool calls that change something? [inference] | SELF | JUDGEMENT / CHECK QUESTION |
| 127 | p-risks M04, line 482 | Typical findingsOne agent holding both a reader of outside text and a server that can send or change things. [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 128 | p-risks M05, line 487 | OWASP MCP01 Token Mismanagement and Secret Exposure | BEARER, OAUTH, OWASP, SEC | REVIEWED |
| 129 | p-risks M05, line 488 | In plain words: A bearer token grants access to a service. | BEARER, OAUTH, SEC | REVIEWED |
| 130 | p-risks M05, line 488 | An attacker who can intercept it may be able to reuse it. | SELF | REVIEWED |
| 131 | p-risks M05, line 489 | Mitiga (May 2026) showed an npm postinstall hook that edits ~/.claude.json and points an MCP server URL at an attacker's localhost proxy. | ARCH, MITIGA, SEC | REVIEWED |
| 132 | p-risks M05, line 489 | Mitiga shows interception and reuse of an OAuth bearer token with Atlassian. | BEARER, MITIGA, OAUTH, SEC | REVIEWED |
| 133 | p-risks M05, line 489 | Its article discusses refresh-token persistence but does not separately demonstrate capture of a refresh token. | BEARER, OAUTH, SEC | REVIEWED |
| 134 | p-risks M05, line 489 | The chain requires local code execution through the npm installation. | SELF | REVIEWED |
| 135 | p-risks M05, line 489 | Mitiga describes a project SessionStart hook that restores the malicious endpoint; remediation must remove that persistence as well as repair the configuration and rotate credentials. | MITIGA | REVIEWED |
| 136 | p-risks M05, line 492 | Do you watch ~/.claude.json and project MCP files for changed server URLs? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 137 | p-risks M05, line 492 | Mitiga recommends this. | MITIGA | REVIEWED |
| 138 | p-risks M05, line 493 | Is there a baseline of approved MCP endpoints, with an alert on new local proxies? | SELF | JUDGEMENT / CHECK QUESTION |
| 139 | p-risks M05, line 493 | Mitiga recommends this too. | MITIGA | REVIEWED |
| 140 | p-risks M05, line 494 | After a suspected case, is the config fixed as well as the tokens rotated? | BEARER, OAUTH, SEC | JUDGEMENT / CHECK QUESTION |
| 141 | p-risks M05, line 494 | Mitiga says rotating tokens alone is not enough. | BEARER, MITIGA, OAUTH, SEC | REVIEWED |
| 142 | p-risks M05, line 497 | Typical findingsNo watch on MCP config files, overly long-lived credentials. [inference] | SELF | JUDGEMENT / CHECK QUESTION |
| 143 | p-risks M06, line 502 | OWASP MCP02 Privilege Escalation via Scope Creep · MCP07 Insufficient Authentication and Authorization | BEARER, OAUTH, OWASP, SEC | REVIEWED |
| 144 | p-risks M06, line 503 | In plain words: A key that opens many doors does more harm when stolen. | SEC | REVIEWED |
| 145 | p-risks M06, line 503 | An MCP server must reject client tokens intended for a different service. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 146 | p-risks M06, line 504 | A stolen token with wide scope reaches further than a narrow one. | BEARER, OAUTH, SEC | REVIEWED |
| 147 | p-risks M06, line 504 | The specification forbids token passthrough: an MCP server must not accept tokens that were not issued for it. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 148 | p-risks M06, line 504 | It also warns that a proxy server with a static client ID can be abused (confused deputy). | ARCH, SEC | REVIEWED |
| 149 | p-risks M06, line 507 | Are tokens short-lived and narrow? | BEARER, OAUTH, SEC | JUDGEMENT / CHECK QUESTION |
| 150 | p-risks M06, line 507 | The specification recommends a progressive, least-privilege scope model. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 151 | p-risks M06, line 508 | Do servers you or a supplier run refuse tokens not issued for them? | ARCH, BEARER, OAUTH, SEC | JUDGEMENT / CHECK QUESTION |
| 152 | p-risks M06, line 509 | Proxy servers with a static client ID: per-client consent, exact redirect_uri match and single-use OAuth state. | ARCH, SEC | REVIEWED |
| 153 | p-risks M06, line 512 | Typical findingsBroad personal tokens in MCP config, servers that forward whatever token they receive. [inference] | ARCH, BEARER, OAUTH, SEC | JUDGEMENT / CHECK QUESTION |
| 154 | p-risks M07, line 517 | MCP specification: transports and security best practices | SEC | REVIEWED |
| 155 | p-risks M07, line 518 | In plain words: A server on your own computer can be reached by other programs, and sometimes by web pages. | ARCH, SEC | REVIEWED |
| 156 | p-risks M07, line 518 | A server can also send your client to addresses it should not visit. | ARCH, SEC | REVIEWED |
| 157 | p-risks M07, line 519 | An MCP server that listens on local HTTP can be reached by other local programs and, through DNS rebinding, by web pages. | ARCH, HTTP, SEC | REVIEWED |
| 158 | p-risks M07, line 519 | The specification also warns that a malicious server can supply URLs that point at internal addresses, such as 169.254.169.254. | ARCH, SEC | REVIEWED |
| 159 | p-risks M07, line 522 | Local HTTP servers: do they check the Origin header (must), bind to 127.0.0.1 rather than 0.0.0.0 (should) and require authentication (should)? | ARCH, HTTP, SEC | JUDGEMENT / CHECK QUESTION |
| 160 | p-risks M07, line 522 | Source: specification 2026-07-28. | SEC, VER | REVIEWED |
| 161 | p-risks M07, line 523 | For OAuth metadata discovery, does the client require HTTPS, restrict private and reserved destinations, and recheck redirect targets? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 162 | p-risks M07, line 523 | The guidance recommends these checks for production, with explicit loopback exceptions for development. | SEC | REVIEWED |
| 163 | p-risks M07, line 523 | For server-side client deployments, operators should consider an egress proxy. | ARCH, SEC | REVIEWED |
| 164 | p-risks M07, line 524 | Does the client require HTTPS authorization URLs, allow HTTP only for loopback during local development, reject dangerous schemes such as javascript:, and avoid shell execution when opening URLs? | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 165 | p-risks M07, line 524 | The guidance requires these protections. | SEC | REVIEWED |
| 166 | p-risks M07, line 527 | Typical findingsA server left running on localhost with no token, bound to all interfaces. [inference] | ARCH, BEARER, OAUTH, SEC | JUDGEMENT / CHECK QUESTION |
| 167 | p-risks M08, line 532 | OWASP MCP10 Context Injection and Over-Sharing · MCP08 Lack of Audit and Telemetry | OWASP | REVIEWED |
| 168 | p-risks M08, line 533 | In plain words: Without server inventories and suitable logs, it is harder to establish what was shared. [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 169 | p-risks M08, line 534 | MCP calls send data to the selected server. | ARCH, SEC | REVIEWED |
| 170 | p-risks M08, line 534 | Local calls can stay on the machine; external disclosure depends on the server, host and model deployment. | ARCH, SEC | REVIEWED |
| 171 | p-risks M08, line 534 | OWASP separately lists context over-sharing and missing audit telemetry as risks. | OWASP | REVIEWED |
| 172 | p-risks M08, line 534 | No MCP-specific incident for these risks is cited here. | SELF | REVIEWED |
| 173 | p-risks M08, line 537 | Is there a list of servers in use, who runs them and what data each receives? [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 174 | p-risks M08, line 538 | Can you see MCP use? | SELF | JUDGEMENT / CHECK QUESTION |
| 175 | p-risks M08, line 538 | Claude Code usage can be monitored with OpenTelemetry; OTEL_LOG_TOOL_DETAILS=1 is the variable the docs name for tool details. | CC | REVIEWED |
| 176 | p-risks M08, line 539 | Has someone decided what may be sent to remote servers? [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 177 | p-risks M08, line 542 | Typical findingsNo inventory, no usage logs, remote servers receiving whole files. [inference] | ARCH, SEC | JUDGEMENT / CHECK QUESTION |
| 178 | p-vscode , line 565 | What the VS Code documentation says about MCP, and which risk each point touches. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 179 | p-vscode , line 565 | The general risks still apply. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 180 | p-vscode , line 565 | Rows summarize the VS Code docs on 5 November 2026 unless it is tagged [inference]. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 181 | p-vscode , line 565 | Nothing here was tested. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEW SCOPE |
| 182 | p-vscode , line 569 | TopicWhat VS Code doesRisk | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 183 | p-vscode , line 571 | Ways a server gets addedFrom the MCP server gallery (Preview), MCP: Add Server, your user mcp.json, a repo's .vscode/mcp.json or root .mcp.json, a Dev Container's devcontainer.json, or code --add-mcp.M01 | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 184 | p-vscode , line 572 | Servers found in other appschat.mcp.discovery.enabled picks the sources. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 185 | p-vscode , line 572 | GitHub Copilot CLI discovery is on by default. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 186 | p-vscode , line 572 | Claude Desktop, Cursor and Windsurf are off by default.M01 | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 187 | p-vscode , line 573 | Workspace TrustServers in .vscode/mcp.json and .mcp.json follow Workspace Trust. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 188 | p-vscode , line 573 | Restricted mode stops them from starting. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 189 | p-vscode , line 573 | In a trusted workspace they can start with no separate MCP prompt, also after the config changes.M03 | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 190 | p-vscode , line 574 | Autostartchat.mcp.autostart (experimental) defaults to newAndOutdated. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 191 | p-vscode , line 574 | When you send a chat message, VS Code starts servers that never ran or whose config changed. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 192 | p-vscode , line 574 | Setting it to never does not stop Copilot harness sessions from starting their own servers. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 193 | p-vscode , line 574 | Disable the server to stop it.M03 | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 194 | p-vscode , line 575 | Trust and autostart togetherIn a trusted repo, a new or changed server entry can start on your next chat message. [inference] Built from the two rows above. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 195 | p-vscode , line 575 | Not tested.M03 | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 196 | p-vscode , line 576 | Sandbox for local serversThe editor per-server sandbox uses sandboxEnabled and access rules for stdio servers on macOS and Linux; its tool calls are auto-approved. | ARCH, SEC, STDIO, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 197 | p-vscode , line 576 | The Copilot harness has a separate sandbox, including supported Windows systems, controlled by chat.agent.sandbox.mcpServers. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 198 | p-vscode , line 576 | The scopes and approval behavior differ.M03, M04 | BEARER, OAUTH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 199 | p-vscode , line 577 | Tool approvalMCP invocations use approval controls; saved grants and sandbox auto-approval can avoid repeated prompts. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 200 | p-vscode , line 577 | Allow all permissions and Autopilot mode bypass manual tool approval. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 201 | p-vscode , line 577 | Setting ChatToolsAutoApprove to false disables global auto-approval and hides those modes, but does not establish that every invocation prompts in every harness.M04 | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 202 | p-vscode , line 578 | Logins and secretsVS Code-format input variables can prompt for secrets and store them securely. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 203 | p-vscode , line 578 | Servers requiring these inputs are not forwarded to Copilot harness sessions. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 204 | p-vscode , line 578 | OAuth is supported for compatible servers. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 205 | p-vscode , line 578 | Do not commit tokens, passwords or populated authentication headers.M05, M06 | BEARER, OAUTH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 206 | p-vscode , line 579 | Settings SyncIf you select MCP Servers in Settings Sync, your user-profile mcp.json syncs to your other devices. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 207 | p-vscode , line 579 | Workspace .mcp.json files do not. [inference] A bad entry on one device could reach the others. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 208 | p-vscode , line 579 | Not observed.M05 | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 209 | p-vscode , line 580 | What servers can ask of the modelchat.mcp.serverSampling sets which models are exposed to servers for background requests.M08 | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 210 | p-vscode , line 581 | Organisation policyChatMCP (chat.mcp.access), ChatAllowedMcpServers, ChatAllowManagedMcpServersOnly, ChatDeniedMcpServers and McpGalleryServiceUrl. | ARCH, CC, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 211 | p-vscode , line 581 | When an allowlist is set, only matching servers may be installed or run. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 212 | p-vscode , line 581 | A deny rule always wins. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 213 | p-vscode , line 581 | These editor policies do not establish coverage of independently discovered Copilot runtime servers; check the harness-specific management guidance.M01 | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 214 | p-vscode , line 582 | Other agents inside VS CodeClaude and Codex harness integrations are disabled while Copilot enterprise-managed settings apply, because those harnesses cannot enforce them. | CODEX, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 215 | p-vscode , line 582 | This includes server-, MDM- and file-delivered settings. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 216 | p-vscode , line 582 | It is a restriction on harness availability, not on selecting Claude or OpenAI models within Copilot.M01 | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 217 | p-vscode , line 583 | VisibilityMCP: Show Installed Servers lists the servers. | ARCH, SEC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 218 | p-vscode , line 583 | Copilot Chat can export traces, metrics and events through OpenTelemetry, which covers tool execution.M08 | CC, VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 219 | p-vscode , line 584 | Example commandsThe docs' own example runs npx -y @playwright/mcp@latest, an unpinned package. [inference] Pinning a package version reduces changes from resolving @latest; it does not guarantee immutable dependencies or safe code.M02 | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | JUDGEMENT / CHECK QUESTION |
| 220 | p-vscode , line 591 | VS Code has more than one kind of agent session (local and Copilot harness), and the settings do not always reach both. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 221 | p-vscode , line 591 | The rows say where the docs name a difference. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 222 | p-vscode , line 591 | Settings and policy names come from the docs; none was run on a managed machine. | VADD, VCONF, VMAN, VMGMT, VOTEL, VPOL, VSEC | REVIEWED |
| 223 | p-evidence , line 599 | What was checked, what is my judgement, and what is still open. | SELF | REVIEWED |
| 224 | p-sources , line 608 | All opened on 5 November 2026, except the Developer-WS page, which is on this site. | SELF | REVIEW SCOPE |
| 225 | p-sources , line 614 | Marked [inference] is my judgement, not taken directly from a source. | SELF | JUDGEMENT / CHECK QUESTION |
| 226 | p-sources , line 614 | The documented product settings and attack paths were not tested on a real system. | SELF | REVIEW SCOPE |
| 227 | p-sources , line 615 | No setting or command on this page was run on a managed machine. | SELF | REVIEW SCOPE |
| 228 | p-sources , line 616 | Versions and dates change quickly in this area. | SELF | REVIEWED |
| 229 | p-sources , line 616 | Check the "Current" box against the sources before you use it in a report. | SELF | REVIEWED |
| 230 | p-sources , line 617 | Made with AIThis page was written with the help of AI. | SELF | REVIEW SCOPE |
| 231 | p-sources , line 617 | Its content has not necessarily been fully quality checked by a human. | SELF | REVIEWED |
| 232 | PLACE / M01 / src | Servers come from many places. Anthropic says it does not security-audit or manage any MCP server. | ARCH, CC, SEC | REVIEWED |
| 233 | PLACE / M01 / cfgin | A project can carry a file such as .mcp.json that names servers to start. | ARCH, SEC | REVIEWED |
| 234 | PLACE / M01 / agent | By default in Claude Code anyone can connect any MCP server, so each developer decides what the agent can reach. | ARCH, CC, SEC | REVIEWED |
| 235 | PLACE / M01 / policy | Claude Code, Codex and VS Code each have an MCP allowlist. In Claude Code, deny rules win within their scope; in-process SDK servers bypass these checks. A user-assigned name does not identify the underlying server. | ARCH, BEARER, CC, CODEX, OAUTH, SEC, VCONF | REVIEWED |
| 236 | PLACE / M02 / pkg | A server installed from a package runs that package's code. OWASP lists dependency tampering as MCP04. | ARCH, OWASP, SEC | REVIEWED |
| 237 | PLACE / M02 / local | Without isolation, local server code can run with the MCP client's privileges. The specification names arbitrary code execution, no visibility and data exfiltration for a compromised one. | ARCH, SEC | REVIEWED |
| 238 | PLACE / M02 / agent | OWASP lists Tool Poisoning as MCP03. The model reads tool descriptions, so a changed description can change what the agent does. [inference] | ARCH, OWASP, SEC | JUDGEMENT |
| 239 | PLACE / M02 / policy | Allow local servers by exact command. Claude Code does not compare the env block; the Codex string form does not check args, cwd or env. | ARCH, CC, CODEX, SEC | REVIEWED |
| 240 | PLACE / M03 / cfgin | A client with one-click local setup must get consent before running a command, and show the exact command in full (specification 2026-07-28). | ARCH, SEC, VER | REVIEWED |
| 241 | PLACE / M03 / cfgf | A malicious startup command in the client config is one of the compromise paths the specification names. | ARCH, SEC | REVIEWED |
| 242 | PLACE / M03 / local | Without isolation, a local server can act with the MCP client's privileges. The specification names arbitrary code execution, no visibility and data exfiltration. | ARCH, SEC | REVIEWED |
| 243 | PLACE / M03 / files | Data exfiltration is one of the consequences the specification names for a compromised local server. | ARCH, SEC | REVIEWED |
| 244 | PLACE / M03 / agent | The specification says clients should run local servers sandboxed with minimal default privileges. | ARCH, SEC | REVIEWED |
| 245 | PLACE / M04 / content | Pages, tickets and files that a tool reads can carry hidden instructions. OWASP lists this as MCP06. | OWASP, VSEC | REVIEWED |
| 246 | PLACE / M05 / pkg | In Mitiga's research an npm postinstall hook edited ~/.claude.json. It needs code execution through the install. | MITIGA | REVIEWED |
| 247 | PLACE / M05 / cfgf | Mitiga reports that the hook rewrote an MCP server URL to an attacker's localhost proxy, pre-set trust-dialog flags and added a project SessionStart hook. | ARCH, MITIGA, SEC | REVIEWED |
| 248 | PLACE / M05 / lhttp | Mitiga demonstrates interception and reuse of an Atlassian OAuth bearer token; separate refresh-token capture is not demonstrated in the article. | BEARER, MITIGA, OAUTH, SEC | REVIEWED |
| 249 | PLACE / M05 / tok | Mitiga says rotating tokens alone is not enough. | BEARER, MITIGA, OAUTH, SEC | REVIEWED |
| 250 | PLACE / M05 / edr | Mitiga recommends baselining approved MCP endpoints, watching ~/.claude.json and project MCP files, and alerting on new local proxies. | MITIGA | REVIEWED |
| 251 | PLACE / M06 / tok | A stolen token with broad scope has a larger blast radius. The specification recommends progressive, least-privilege scopes. | BEARER, OAUTH, SEC | REVIEWED |
| 252 | PLACE / M06 / mcpr | An MCP server must not accept tokens that were not issued for it. The authorization specification forbids token passthrough. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 253 | PLACE / M06 / saas | A proxy server with a static client ID can be abused (confused deputy). Protections include per-client consent, exact redirect_uri match, single-use state. | ARCH, SEC | REVIEWED |
| 254 | PLACE / M07 / lhttp | Servers must validate the Origin header to stop DNS rebinding, should bind to 127.0.0.1 rather than 0.0.0.0, and should authenticate (specification 2026-07-28). | ARCH, HTTP, SEC, VER | REVIEWED |
| 255 | PLACE / M07 / egress | A malicious server can supply URLs that point at internal addresses such as 169.254.169.254. For production OAuth discovery, restrict private destinations and redirects. Server-side client operators should consider an egress proxy; development loopback needs explicit exceptions. | ARCH, SEC | REVIEWED |
| 256 | PLACE / M07 / agent | Clients must require HTTPS authorization URLs, allowing HTTP only for development loopback, reject dangerous schemes, and avoid shell execution when opening URLs (security guidance, 2026-07-28). | ARCH, SEC, VER | REVIEWED |
| 257 | PLACE / M08 / agent | OWASP lists Context Injection and Over-Sharing as MCP10: more context goes to a server than it needs. | ARCH, OWASP, SEC | REVIEWED |
| 258 | PLACE / M08 / policy | An inventory and usage logs help establish which servers are used. [inference] OWASP MCP08 concerns missing audit and telemetry. | ARCH, OWASP, SEC | JUDGEMENT |
| 259 | PLACE / M08 / tele | Claude Code usage can be monitored with OpenTelemetry; OTEL_LOG_TOOL_DETAILS=1 is the variable the docs name for tool details. | CC | REVIEWED |
| 260 | START / M01 | Claude Code allowManagedMcpServersOnly with an allowlist of both URLs and commands; the Codex and VS Code allowlists, with session-specific exceptions reviewed; friction: Moderate | ARCH, CC, CODEX, SEC, VCONF | JUDGEMENT |
| 261 | START / M02 | Allow local servers by exact command, not by name; friction: Low | ARCH, SEC | JUDGEMENT |
| 262 | START / M03 | Check that each client shows the full command and asks before running it; friction: Low | ARCH, SEC | JUDGEMENT |
| 263 | START / M04 | Use separate sessions for untrusted reading, without tools that can write or send; friction: Moderate | SELF | JUDGEMENT |
| 264 | START / M05 | Alert on changes to ~/.claude.json and project MCP files; friction: Low | SELF | JUDGEMENT |
| 265 | START / M06 | Short-lived, narrowly scoped tokens per server; friction: Moderate | ARCH, BEARER, OAUTH, SEC | JUDGEMENT |
| 266 | START / M07 | Bind local HTTP servers to 127.0.0.1, check Origin and require a token; friction: Low | ARCH, BEARER, HTTP, OAUTH, SEC | JUDGEMENT |
| 267 | START / M08 | A list of approved servers, and Claude Code usage export through OpenTelemetry; friction: Low | ARCH, CC, SEC | JUDGEMENT |
| 268 | EVIDENCE / Checked against sources | OWASP MCP Top 10 names and IDs (MCP01 to MCP10), read 5 November 2026. The project is in beta (phase 3). | OWASP | REVIEWED |
| 269 | EVIDENCE / Checked against sources | MCP specification 2026-07-28 (the current version), Streamable HTTP: Origin validation, localhost binding, authentication. | ARCH, HTTP, SEC, VER | REVIEWED |
| 270 | EVIDENCE / Checked against sources | MCP security best practices (2026-07-28): confused deputy, token passthrough, SSRF, local server compromise, authorization URL validation, scope minimisation. | ARCH, BEARER, OAUTH, SEC, VER | REVIEWED |
| 271 | EVIDENCE / Checked against sources | Mitiga research, published 5 May 2026, updated 30 October 2026: endpoint rewriting, bearer-token interception and reuse, prerequisite local code execution, and the vendor response as reported by Mitiga. | BEARER, MITIGA, OAUTH, SEC | REVIEWED |
| 272 | EVIDENCE / Checked against sources | Claude Code managed MCP page: managed-mcp.json, allowedMcpServers and deniedMcpServers, allowManagedMcpServersOnly, URL and command matching, OpenTelemetry. | ARCH, CC, SEC | REVIEWED |
| 273 | EVIDENCE / Checked against sources | Codex managed configuration: mcp_servers allowlist and string versus structured command matching; neither form verifies cwd or environment variables. | ARCH, CODEX, SEC | REVIEWED |
| 274 | EVIDENCE / Checked against sources | VS Code docs (agent customization, manage MCP servers, MCP configuration reference, AI security, policies, telemetry): the rows on the VS Code tab. | ARCH, SEC, VCONF | REVIEWED |
| 275 | EVIDENCE / My judgement | The choice of eight risks, their order and the OWASP mapping. | OWASP | JUDGEMENT |
| 276 | EVIDENCE / My judgement | Where each risk sits on the map. | SELF | JUDGEMENT |
| 277 | EVIDENCE / My judgement | Statements tagged [inference] (advice questions, not facts), and the friction estimates. | SELF | JUDGEMENT |
| 278 | EVIDENCE / My judgement | Which VS Code facts are shown, and the risk each is tied to. | VCONF | JUDGEMENT |
| 279 | EVIDENCE / Still open | The specification can change. This page was checked against version 2026-07-28, the current one on 5 November 2026. | VER | REVIEWED |
| 280 | EVIDENCE / Still open | Only one MCP-specific research demonstration (Mitiga) is cited. For the other risks no incident was verified. That does not mean none exists. | MITIGA | REVIEWED |
| 281 | EVIDENCE / Still open | Mitiga reports that Anthropic told it the issue was out of scope and by design. Mitiga disagrees. This page does not take a side. | BEARER, CC, MITIGA, OAUTH, SEC | REVIEWED |
| 282 | EVIDENCE / Still open | Product policy coverage depends on the harness and configuration source. Editor controls do not necessarily cover independently discovered Copilot servers. | ARCH, SEC | REVIEWED |
| 283 | EVIDENCE / Still open | No setting or command on this page was run on a managed machine. | SELF | REVIEWED |
| 284 | EVIDENCE / Still open | VS Code has local and Copilot harness sessions. Settings do not always reach both. | VCONF | REVIEWED |
| 285 | EVIDENCE / Still open | Documentation was reviewed, but no exploit or managed-product behavior was reproduced. Mitiga is a research demonstration, not evidence here of an observed victim incident. | MITIGA | REVIEWED |
| 286 | SOURCES / OWASP MCP Top 10 | OWASP. Beta (phase 3). MCP01 to MCP10. | OWASP | REVIEWED |
| 287 | SOURCES / MCP specification: transports (Streamable HTTP) | Model Context Protocol, version 2026-07-28 (current). Origin validation, localhost binding, authentication. | ARCH, HTTP, SEC, VER | REVIEWED |
| 288 | SOURCES / MCP security best practices (2026-07-28) | Model Context Protocol. Confused deputy, token passthrough, SSRF, local server compromise, authorization URL validation, scope minimisation. | ARCH, BEARER, OAUTH, SEC | REVIEWED |
| 289 | SOURCES / Stealing MCP tokens in Claude Code via ~/.claude.json | Mitiga (5.5.2026, updated 30.10.2026). Attack steps, vendor response and recommendations. | MITIGA | REVIEWED |
| 290 | SOURCES / Claude Code: managed MCP | Anthropic. managed-mcp.json, allowlist and denylist matching, allowManagedMcpServersOnly, OpenTelemetry monitoring. | ARCH, CC, SEC | REVIEWED |
| 291 | SOURCES / Codex managed configuration | OpenAI. requirements.toml mcp_servers allowlist and identity forms. | ARCH, SEC | REVIEWED |
| 292 | SOURCES / VS Code: Add MCP servers | Microsoft. Gallery, adding servers, trust warning. | ARCH, SEC | REVIEWED |
| 293 | SOURCES / VS Code: Manage MCP servers | Microsoft. Workspace Trust, autostart, sandbox, Settings Sync, Dev Containers. | ARCH, SEC | REVIEWED |
| 294 | SOURCES / VS Code: MCP configuration reference | Microsoft. Settings, discovery sources, sandbox schema. | ARCH, SEC | REVIEWED |
| 295 | SOURCES / VS Code: AI security | Microsoft. Tool approval, permission levels, secure credentials store, MCP sandboxing. | ARCH, SEC | REVIEWED |
| 296 | SOURCES / Centrally manage VS Code settings with policies | Microsoft. ChatMCP, ChatAllowedMcpServers, ChatDeniedMcpServers, McpGalleryServiceUrl, ChatToolsAutoApprove. | ARCH, SEC | REVIEWED |
| 297 | SOURCES / VS Code: enterprise telemetry | Microsoft. OpenTelemetry export from Copilot Chat. | CC | REVIEWED |
| 298 | SOURCES / Developer workstation risk map | This site. The wider page this one was cut from; it covers MCP together with VS Code, git and agents. | VCONF | REVIEWED |
| 299 | SOURCES / MCP specification: stdio | Subprocess launch and standard-stream transport. | SELF | REVIEWED |
| 300 | SOURCES / MCP specification: tools | Tool capabilities, invocation and host interaction choices. | ARCH, SEC | REVIEWED |
| 301 | SOURCES / MCP versioning | Current protocol revision and compatibility rules. | SELF | REVIEWED |
| 302 | SOURCES / OAuth bearer token usage (RFC 6750) | Bearer possession and authorized resource access. | SELF | REVIEWED |
| 303 | SOURCES / VS Code: manage AI settings | Management layers, precedence and harness coverage. | SELF | REVIEWED |
| 304 | SOURCES / MCP architecture overview | Hosts, clients, servers and application control of model context. | ARCH, SEC | REVIEWED |
| 305 | SOURCES / OAuth 2.0 (RFC 6749) | Access tokens, service credentials and authorization scopes. | BEARER, OAUTH, SEC | REVIEWED |

## Rendering and interaction validation

Passed all five tabs at 1440px and 375px in light and dark modes (20 combinations). No page-wide horizontal overflow and no JavaScript exceptions or console error events. Visually inspected desktop and phone screenshots in both themes, including the diagram in both themes. Confirmed status persistence/tally and a diagram marker popover. Browser checks used an isolated temporary profile.

Inline JavaScript syntax and embedded data parsed successfully. No duplicate HTML ids, no changed public ids, no em or en dashes, and no HTML paragraph over 60 words. The site has no build step. Product settings and attack paths remain untested.

Reviewed page SHA-256: `379181795945cbb1ff004d75dbb5dc9f30d39d533bb1860b1fdb903b082a4177`.

## Historical ledger, 2 November 2026 (superseded)

The following records the earlier review, including incorrect OK verdicts. It is retained for history and is not current evidence.

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
