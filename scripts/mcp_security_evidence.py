"""Evidence quotes for mcp-security.html.

  python3 -I scripts/check-evidence-quotes.py <cache-dir> mcp_security_evidence mcp-security.html
"""

CHECKED = "2026-11-26"

SOURCES = {
    "sec": ("MCP security policy",
            "https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/SECURITY.md", None),
    "bp": ("MCP security best practices",
           "https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices", None),
    "trans": ("MCP specification, transports",
              "https://modelcontextprotocol.io/specification/latest/basic/transports", None),
    "authz": ("MCP specification, authorization",
              "https://modelcontextprotocol.io/specification/latest/basic/authorization", None),
    "npx": ("npm Docs, npx", "https://docs.npmjs.com/cli/v11/commands/npx", None),
    "npm12": ("npm Docs, npm approve-scripts", "https://docs.npmjs.com/cli/v12/commands/npm-approve-scripts", None),
    "inv": ("Invariant Labs, tool poisoning attacks",
            "https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks", None),
    "vsc": ("VS Code Docs, manage MCP servers",
            "https://code.visualstudio.com/docs/agents/run/manage-mcp-servers", None),
    "cve": ("GitHub advisory GHSA-6xpm-ggf7-wc3p (CVE-2025-6514)",
            "https://github.com/advisories/GHSA-6xpm-ggf7-wc3p", None),
    "owasp": ("OWASP MCP Top 10", "https://owasp.org/www-project-mcp-top-10/", None),
}

QUOTES = [
    ("npx", "npx", "This command allows you to run an arbitrary command from an npm package"),
    ("trusted", "sec", "Local MCP servers are trusted like any other software you install."),
    ("access", "sec", "When you run a local MCP server, you are trusting it with the same level of access as any other application or package on your system."),
    ("binaries", "bp", "Local MCP servers are binaries that are downloaded and executed on the same machine as the MCP client."),
    ("anycmd", "bp", "Attackers can execute any command with MCP client privileges."),
    ("sandbox", "bp", "Execute MCP server commands in a sandboxed environment with minimal default privileges"),
    ("notsandbox", "sec", "stdio transport is not a sandbox."),
    ("scripts", "npm12", "Dependency install scripts are blocked by default."),
    ("vscsb", "vsc", "On macOS and Linux, per-server sandboxing restricts file system and network access for stdio MCP servers."),
    ("poison", "inv", "A Tool Poisoning Attack occurs when malicious instructions are embedded within MCP tool descriptions"),
    ("rugpull", "inv", "a malicious server can change the tool description after the client has already approved it."),
    ("shadow", "inv", "a malicious server can poison tool descriptions to exfiltrate data accessible through other trusted servers"),
    ("stdio", "trans", "newline-delimited messages over the standard streams of a client-launched subprocess."),
    ("http", "trans", "each message is an HTTP POST to a single MCP endpoint"),
    ("authopt", "authz", "Authorization is OPTIONAL for MCP implementations."),
    ("inject", "owasp", "Because models are designed to follow natural-language instructions, prompt injection attacks are both powerful and subtle."),
    ("bridge", "cve", "mcp-remote is exposed to OS command injection when connecting to untrusted MCP servers"),
]

IDS = {key: f"V{n}" for n, (key, _, _) in enumerate(QUOTES, 1)}
