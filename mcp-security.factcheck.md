# MCP security page: fact check

Page: `mcp-security.html`. Checked 26 November 2026.

## Quotes

Each quote was found word for word on its source page:

```
python3 -I scripts/check-evidence-quotes.py <cache-dir> mcp_security_evidence mcp-security.html
```

| ID | Quote | Source | Verdict |
|----|-------|--------|---------|
| V1 | This command allows you to run an arbitrary command from an npm package | [npm Docs, npx](https://docs.npmjs.com/cli/v11/commands/npx) | VERIFIED |
| V2 | Local MCP servers are trusted like any other software you install. | [MCP security policy](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/SECURITY.md) | VERIFIED |
| V3 | When you run a local MCP server, you are trusting it with the same level of access as any other application or package on your system. | [MCP security policy](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/SECURITY.md) | VERIFIED |
| V4 | Local MCP servers are binaries that are downloaded and executed on the same machine as the MCP client. | [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) | VERIFIED |
| V5 | Attackers can execute any command with MCP client privileges. | [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) | VERIFIED |
| V6 | Execute MCP server commands in a sandboxed environment with minimal default privileges | [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) | VERIFIED |
| V7 | stdio transport is not a sandbox. | [MCP security policy](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/SECURITY.md) | VERIFIED |
| V8 | Dependency install scripts are blocked by default. | [npm Docs, npm approve-scripts](https://docs.npmjs.com/cli/v12/commands/npm-approve-scripts) | VERIFIED |
| V9 | On macOS and Linux, per-server sandboxing restricts file system and network access for stdio MCP servers. | [VS Code Docs, manage MCP servers](https://code.visualstudio.com/docs/agents/run/manage-mcp-servers) | VERIFIED |
| V10 | A Tool Poisoning Attack occurs when malicious instructions are embedded within MCP tool descriptions | [Invariant Labs, tool poisoning attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) | VERIFIED |
| V11 | a malicious server can change the tool description after the client has already approved it. | [Invariant Labs, tool poisoning attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) | VERIFIED |
| V12 | a malicious server can poison tool descriptions to exfiltrate data accessible through other trusted servers | [Invariant Labs, tool poisoning attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) | VERIFIED |
| V13 | newline-delimited messages over the standard streams of a client-launched subprocess. | [MCP specification, transports](https://modelcontextprotocol.io/specification/latest/basic/transports) | VERIFIED |
| V14 | each message is an HTTP POST to a single MCP endpoint | [MCP specification, transports](https://modelcontextprotocol.io/specification/latest/basic/transports) | VERIFIED |
| V15 | Authorization is OPTIONAL for MCP implementations. | [MCP specification, authorization](https://modelcontextprotocol.io/specification/latest/basic/authorization) | VERIFIED |
| V16 | Because models are designed to follow natural-language instructions, prompt injection attacks are both powerful and subtle. | [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) | VERIFIED |
| V17 | mcp-remote is exposed to OS command injection when connecting to untrusted MCP servers | [GitHub advisory GHSA-6xpm-ggf7-wc3p (CVE-2025-6514)](https://github.com/advisories/GHSA-6xpm-ggf7-wc3p) | VERIFIED |

## Claims

| Page claim | Evidence | Verdict |
|------------|----------|---------|
| Installing a local server through npx is in practice the same as running any npm package | V1, V4, V7 | `[inference]` |
| MCP adds no installation mechanism, boundary or sandbox to the npx path | V7 covers the SDK stdio transport only | `[inference]`. The MCP project's registry and bundle format were not reviewed; the claim is limited to the npx path |
| What a malicious server can do (six items), without any tool call | V2, V3, V5 | `[inference]` from "same level of access". Not tested |
| Comparison table | V9 to V12 | `[inference]` |
| No sandbox by default from npm or MCP | V9 shows an opt-in client sandbox on macOS and Linux | `[inference]`. Other clients and Node's permission model were not reviewed |
| npm 12 blocks dependency install scripts by default | V8 | VERIFIED. How this applies to the package that npx itself runs was not checked; the page says only "dependency" |
| Local and remote transports | V13, V14 | VERIFIED |
| Remote server is closer to consuming an API; remaining risks | V10, V15, V16 | `[inference]` |
| A local bridge brings back local execution risk | V17, advisory range 0.0.5 up to but not including 0.1.16 | VERIFIED for mcp-remote; general statement is interpretation |
| Two governance layers, principles, controls | V6 for sandboxing | `[recommendation]`, supplied by the owner's brief; not source claims |

## Gaps

- Nothing was run or tested; the page rests on documentation and one advisory.
- The Invariant Labs post is dated 1 April 2025.
- The OWASP MCP Top 10 page described itself as in beta.
