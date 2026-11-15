# VS Code agent guardrails: fact check

Checked on 15 November 2026. Sources are the VS Code docs, each marked `DateApproved: 11/11/2026`. The raw markdown was read from the `microsoft/vscode-docs` repository on GitHub, which the public pages under `https://code.visualstudio.com/docs/` are built from.

## How the quotes were checked

A script took every quote from the `Q` table in `vscode-guardrails.html` and looked for it in the saved source text, after removing markdown bold, code marks, link syntax and the docs' product-name placeholders. Result on 15 November 2026: 44 of 44 found (the 36 below, the six baseline step names and the two questions in the first section). A pass shows the words are in the source. It does not show the claim built on the quote is right.

## Source quotes

| Id | Quote | Source | Verdict |
|----|-------|--------|---------|
| restricted | Opening a workspace in restricted mode disables agents in that workspace. | [editing/workspaces/workspace-trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust) | Word for word |
| trustcert | Trust permits access or execution; it doesn't certify that every result or action is safe. | [agents/concepts/trust-and-safety](https://code.visualstudio.com/docs/agents/concepts/trust-and-safety) | Word for word |
| manual | Uses your tool, URL, and terminal approval settings. Actions that are not auto-approved require your confirmation. | [agents/run/approvals](https://code.visualstudio.com/docs/agents/run/approvals) | Word for word |
| assisted | Uses an LLM judge to assess each tool call. Calls that the judge does not approve require your confirmation. | [agents/run/approvals](https://code.visualstudio.com/docs/agents/run/approvals) | Word for word |
| assistedrisk | This permission level reduces approval interruptions but is not a security boundary. | [agents/run/security](https://code.visualstudio.com/docs/agents/run/security) | Word for word |
| all | Runs all tool calls without confirmation. | [agents/run/approvals](https://code.visualstudio.com/docs/agents/run/approvals) | Word for word |
| termdefault | By default, common read-only commands run automatically, while risky commands such as rm and del require approval. | [agents/run/approvals](https://code.visualstudio.com/docs/agents/run/approvals) | Word for word |
| runtime | In Copilot harness sessions, the runtime can approve read-only commands or sandboxed commands before terminal approval rules are evaluated. | [agents/run/approvals](https://code.visualstudio.com/docs/agents/run/approvals) | Word for word |
| besteffort | Terminal auto-approval is a best-effort convenience, not a security boundary. | [agents/run/approvals](https://code.visualstudio.com/docs/agents/run/approvals) | Word for word |
| urlreq | Prevents data from being sent to an untrusted site. | [agents/run/approvals](https://code.visualstudio.com/docs/agents/run/approvals) | Word for word |
| urlres | Helps prevent prompt injection from untrusted content. | [agents/run/approvals](https://code.visualstudio.com/docs/agents/run/approvals) | Word for word |
| sensitive | Sensitive-file approval happens before the agent saves an edit, rather than during review. | [agents/run/review-code-edits](https://code.visualstudio.com/docs/agents/run/review-code-edits) | Word for word |
| editauto | File edits might be auto-approved. | [agents/concepts/trust-and-safety](https://code.visualstudio.com/docs/agents/concepts/trust-and-safety) | Word for word |
| builtin | Built-in agent tools can only read and write files within the current workspace folder. | [agents/run/security](https://code.visualstudio.com/docs/agents/run/security) | Word for word |
| privs | The agent can execute terminal commands and shell scripts with your user privileges | [agents/run/security](https://code.visualstudio.com/docs/agents/run/security) | Word for word |
| cwd | The sandbox automatically grants read and write access to the current working directory. | [agents/run/agent-sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) | Word for word |
| ssh | It protects sensitive locations, such as SSH keys and shell configuration, and applies to child processes such as package managers and build scripts. | [agents/concepts/trust-and-safety](https://code.visualstudio.com/docs/agents/concepts/trust-and-safety) | Word for word |
| netopen | Turning on sandboxing does not block outbound network access by default. | [agents/run/agent-sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) | Word for word |
| netblock | Set it to false to block outbound access, including for the integrated browser. | [agents/run/agent-sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) | Word for word |
| escask | The agent requests approval when a sandboxed command fails or sandbox restrictions would block it. | [agents/run/agent-sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) | Word for word |
| escno | Rejecting the confirmation prevents the command from running outside the sandbox. | [agents/run/agent-sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) | Word for word |
| escoff | Allow Outside Sandbox is not offered, and requests to run outside the sandbox fail instead of prompting for approval. | [agents/run/agent-sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) | Word for word |
| escyes | Approval to run outside the sandbox removes file system and network restrictions for that operation. | [agents/run/agent-sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) | Word for word |
| notcovered | The agent's read, edit, and write tools use VS Code's permission system directly. | [agents/concepts/trust-and-safety](https://code.visualstudio.com/docs/agents/concepts/trust-and-safety) | Word for word |
| fetchsep | Network controls for fetch and browser tools are separate from sandbox network controls for terminal commands. | [agents/concepts/trust-and-safety](https://code.visualstudio.com/docs/agents/concepts/trust-and-safety) | Word for word |
| indep | For example, the sandbox continues to restrict processes when you select Allow all. | [agents/run/agent-sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) | Word for word |
| keep | Pending edits are already saved to disk, so running your application or tests uses the changed files. | [agents/run/review-code-edits](https://code.visualstudio.com/docs/agents/run/review-code-edits) | Word for word |
| noundo | Stopping a request or restoring workspace files doesn't reverse completed terminal commands, network requests, deployments, or changes to external services. | [agents/concepts/trust-and-safety](https://code.visualstudio.com/docs/agents/concepts/trust-and-safety) | Word for word |
| notvm | Sandboxing is not a virtual machine or user-account boundary, and it does not replace endpoint security. | [agents/run/agent-sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) | Word for word |
| devtool | It grants read access to tool directories on PATH, toolchain directories, developer-tool configuration and caches, including registry tokens, and read and write access to shared build caches. | [agents/run/agent-sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) | Word for word |
| nosilent | If an operating system dependency is unavailable, the command does not silently run without the sandbox. | [agents/run/agent-sandboxing](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) | Word for word |
| worktree | It doesn't restrict commands, network access, or access to other files. | [agents/concepts/trust-and-safety](https://code.visualstudio.com/docs/agents/concepts/trust-and-safety) | Word for word |
| ext | Workspace Trust can't prevent a malicious extension from executing code and ignoring Restricted Mode. | [editing/workspaces/workspace-trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust) | Word for word |
| mcp | In a trusted workspace, they can start without a separate MCP trust prompt, including after configuration changes. | [agents/run/manage-mcp-servers](https://code.visualstudio.com/docs/agents/run/manage-mcp-servers) | Word for word |
| status | Agent sandboxing is in Preview on macOS, Linux, and WSL2, and Experimental on Windows. | [agents/run/approvals](https://code.visualstudio.com/docs/agents/run/approvals) | Word for word |
| fatigue | Repeatedly approving commands can cause you to pay less attention to what you're approving, especially during long agent sessions. | [agents/concepts/trust-and-safety](https://code.visualstudio.com/docs/agents/concepts/trust-and-safety) | Word for word |

## Claims that are not quotes

| Claim on the page | Verdict | Basis |
|-------------------|---------|-------|
| Sandbox is off by default | Confirmed | Agent sandboxing: "It accepts `off` or `on` and defaults to `off`." |
| macOS needs 15 or later | Confirmed | Agent sandboxing, platform table |
| Linux and WSL2 need glibc, `bubblewrap` 0.5.0 or later, `slirp4netns` | Confirmed, shortened | Same table also lists util-linux 2.35 or later and `iptables` tools |
| Windows 11 25H2 build 26200.9550 or later | Confirmed, shortened | Same page also lists 26H1 build 28000.3086 or later |
| Alpine (musl) and WSL1 not supported | Confirmed | Agent sandboxing |
| Manual permissions asks for `cat ~/.ssh/...` and `curl ...` when the sandbox is off | `[unverified]` | The docs say actions that are not auto-approved need confirmation. The built-in terminal rule list was not read, so it is not known whether these two commands are auto-approved. |
| The "run outside the sandbox" prompt still appears under Allow all | `[unverified]` | Not stated in the pages read. |
| With no `.env` rule, the edit is saved without a question | `[inference]` | Interpretation by AI from "File edits might be auto-approved." |
| With the sandbox on, terminal commands skip the approval question at every permission level | Confirmed for Copilot harness | Approvals: the runtime "can approve read-only commands or sandboxed commands before terminal approval rules are evaluated. These calls do not prompt". The docs say "can", so a prompt may still appear in some cases. |
| The sandbox blocks reading an SSH key | Confirmed in general terms | Trust and safety: file system isolation "protects sensitive locations, such as SSH keys and shell configuration". The default read rules outside the working directory are not listed in the pages read. |
| A sandboxed command can read registry tokens unless developer-tool access is off | Confirmed | Agent sandboxing, `allowDevToolAccess` defaults to `true` |
| Terminal rules can be fooled | Confirmed | Approvals lists parser limits; AI security: "quote concatenation or shell aliases might bypass the rules" |

## Gaps

- Only the Copilot harness is covered. Local, Claude and Codex harness behavior was read but is not on the page.
- Enterprise policies were read but are not on the page.
- Nothing was run in VS Code. All outcomes come from the docs.
