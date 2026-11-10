# Fact check: Developer Workstation Risk Map

Belongs to [Developer-WS.html](Developer-WS.html), named `Developer Workstation Risk Map.html` when this work was done. Other notes for the same page: [plan](Developer-WS.plan.md), [decisions](Developer-WS.decisions.md).

Checked 30 October to 1 November 2026. Every statement on the page, one row each, compared with its source. Three drift items were updated on 10 November 2026; see **Recheck, 10 November 2026**.

Page checked: `Developer-WS.html` (then named `Developer Workstation Risk Map.html`), MD5 `c20d450b532e5615bef1db0dcf6e9a7c`.

## What was found

- 965 statements: 403 OK, 35 FIXED, 18 CUT, 147 JUDGEMENT, 104 RECORD, 53 QUESTION, 205 UI.
- 35 statements were wrong or not backed by their source. They are listed under **Corrections** with what changed and why.
- Long statements were shortened in passes 3 to 6, 8 and 9. The **Change log** at the end shows every changed sentence, before and after.
- Paragraph length after pass 9: 240 text blocks (paragraphs, list items, table cells, caption rows and labels); the longest is 60 words, median 24, none over 60. Code samples are not counted. The longest text field in the page's data (More risks, map notes, Evidence, Review, Sources) is 58 words.
- Every statement was checked. The Hacker News blocks scripted fetches, so its three articles were read in a browser on 1 November.

## Recheck, 10 November 2026

A claim-by-claim recheck of the page against fresh copies of its sources, written up in [Developer-WS.assessment.md](Developer-WS.assessment.md). It found no factual error and three drift items. The page was updated for those three only.

| Rows | What changed | How known |
| --- | --- | --- |
| 69, 629, npm source note | "12.2.1 is current" is now "12.2.2 was current ... on 10 November 2026". | npm registry API on 10 Nov 2026: `latest` is 12.2.2, published 4 Nov 2026. 12.2.1 was published 15 Oct 2026, so the old sentence was true on 1 November. |
| 287, 702 | Added that the Codex network table is `[network_proxy]` from 0.166.0. `[experimental_network]` stays as the name the page uses. | OpenAI managed configuration page on 10 Nov 2026: "In Codex 0.166.0, [network\_proxy] is the canonical table"; "Keep [experimental\_network] in published policies until every client and policy validator supports [network\_proxy]." Not checked: whether this text was already there on 1 November. |
| 683, 686, 710, 717 | Source titles changed to match the live pages. Links are unchanged. | Live page titles on 10 Nov 2026. |

Limits of this recheck:

- The "Current as of 1 November 2026" heading was not moved. This was not a full row-by-row check, and six items could not be checked on 10 November. They are listed under "Not checked" in the assessment.
- Rows 505 and 650 still name `[experimental_network]` only. They are still correct, because the older name is accepted.
- The **Where** line numbers in the tables are from 1 November and were not renumbered.
- The verdict counts under **What was found** are unchanged. No verdict changed.
- The quotes for rows 69 to 717 were checked by text search in the fetched pages. No setting was run on a machine.

## How to read the tables

Each row is one sentence or one data item from the page. **Where** is the page line (`L123`) or the data array and item (`PLACE[9]`). **Evidence** names a key from the source list below. **Pass** says which pass of this check changed the text, if any.

| Verdict | Meaning |
| --- | --- |
| OK | Matches the source named in the Evidence column. |
| FIXED | Was wrong or not backed by its source. Corrected in this check. |
| CUT | Shortened in this check; what is left matches the source. |
| JUDGEMENT | The author's own judgement, advice, or a line tagged [inference]. No source can confirm it. |
| RECORD | Part of the review history on the Review tab. It records what an earlier round found or changed. |
| QUESTION | A checklist question. It asks; it does not claim. |
| UI | A label, title or diagram text with no factual claim. |
| NOT CHECKABLE | The source could not be read. The reason is in the note. |

A row that shares a verdict with the rows around it says "same as #N". The note on row N covers them all.

## Corrections

| # | Where | Statement now | What was wrong and how it was fixed |
| --- | --- | --- | --- |
| 5 | L274 | Facts checked 29 Oct 2026; corrections 30 Oct and 1 Nov 2026 | Date line. Now names the 30 Oct and 1 Nov correction rounds. |
| 68 | L371 | Current as of 1 November 2026 | Was 30 October. Now 1 November 2026, the date of this check. |
| 170 | L474 | GlassWorm has hit Open VSX in waves since October 2025, and its 2026 variants also install into VS Code, Cursor and Windsurf. | Was "every editor". Socket names VS Code, Cursor and Windsurf, and waves since Oct 2025. |
| 206 | L501 | Read(./.env) matches only the start folder; Read(.env) matches any depth. | Was "project root". Docs: Read(./.env) matches .env in the current directory, where Claude started. Read(.env) matches at any level. |
| 221 | L516 | In October 2026 Forever Security reported a planted AGENTS.md in a customer's Downloads folder that tried to make Codex install a malicious npm package. | Was "found ... in October 2026". Help Net (26 Oct 2026) reports the find but gives no find date, so now "reported". |
| 239 | L535 | ClawHavoc put more than 1,000 malicious skills on ClawHub in early 2026. | Source added. Antiy CERT (6 Feb 2026): "at least 1,184 malicious Skills ... on ClawHub". Snyk's 76 does not back it. |
| 271 | L557 | Codex sandboxes commands by default (network off, writes limited to the workspace) but by default leaves reads open. | Added "by default". Codex docs: network off, writes limited to the workspace; no read limit stated, and deny\_read exists in requirements.toml. |
| 304 | L577 | GhostApproval (Wiz, July 2026) used repo symlinks to make six agents write outside the project, such as to ~/.ssh/authorized\_keys; in some, the prompt named a harmless file or came after the write. | Was "several of the six". Wiz (8 Jul 2026, via CSA note): symlinks, writes outside the project such as ~/.ssh/authorized\_keys; some prompts showed a harmless file, some came after the write. |
| 339 | L601 | A Claude Code managed settings file, plist or HKLM value that is not valid JSON stops Claude Code from starting, and a developer with local admin rights can edit the managed policy itself. | Was "a file-based policy". Claude docs: invalid managed JSON stops startup; plist and HKLM forms are also editable by a local admin. |
| 364 | L620 | In July 2026 Grok Build CLI was found uploading whole Git repositories to xAI's storage. | Was unnamed. Hacker News, July 2026: Grok Build CLI uploaded whole Git repos to xAI storage. Pass 9: "a researcher found" became "was found"; the researcher is named in Sources. |
| 379 | L637 | In Forever Security's case Codex first changed its own settings, which then applied to every later Codex session in any project. | Was a config.toml detail Help Net does not name. Help Net: Codex "first changed its own settings", then every later session in any project ran the attacker's command. |
| 469 | L738 | The unverified Codex side was removed on 1 November. | Put in the past tense on 1 Nov; the Codex sentence was cut. |
| 494 | L762 | That split is now in the D06 map notes. | Put in the past tense: the split now lives in the D06 map notes. |
| 504 | L773 | It was marked contested; D06 now attributes the default to CSA. | Put in the past tense. |
| 541 | L826 | The git commands were re-run on 29 October 2026 on Git 2.43.0 and on 1 November 2026 on Git 2.54.0 in throwaway repos, including a normal clone and a copied folder. | Added the 1 Nov re-run on Git 2.54.0. |
| 624 | PERSONAS[2].f[3] | Narrowed several claims: CVE-2025-59536 covers code run through project config before trust, and the hooks finding had no CVE; 1,184 ClawHavoc skills is a minimum count; not all six GhostApproval agents showed a misleading dialog; Gen Digital's figures count protected users with detections, not confirmed infections. | Gen Digital part reworded to "protected users with detections, not confirmed infections". CVE-2025-59536, 1,184 minimum and GhostApproval parts match their sources. |
| 665 | SOURCES[6] | OWASP MCP Top 10 \| https://owasp.org/www-project-mcp-top-10/ \| OWASP. Beta (phase 3). MCP01 to MCP10. | Was a narrower ID range. The list runs MCP01 to MCP10, beta. |
| 668 | SOURCES[9] | Researcher uncovers 30+ flaws in AI coding tools (IDEsaster) \| https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html \| The Hacker News (December 2025). | Was "Researchers uncover". Read in a browser on 1 Nov: the headline is "Researcher Uncovers 30+ Flaws in AI Coding Tools", one researcher (Ari Marzouk), dated 6 Dec 2025. |
| 671 | SOURCES[12] | Malicious .git configs can make Claude, Codex, Cursor and other AI agents run attacker code \| https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html \| The Hacker News (2.9.2026). GitSpawn by Manifold Security, versions and mitigations. | Note now says GitSpawn by Manifold. The day is right: read in a browser on 1 Nov, the article is dated Sep 02, 2026 and names Manifold Security. |
| 680 | SOURCES[21] | AI coding agents' 0-click RCE flaw (Plugin4Shell) \| https://www.theregister.com/a/5297335 \| The Register (September 2026), on research by Air Security. | Research credited to Air Security, as The Register says. |
| 683 | SOURCES[24] | MCP Token Theft in Claude Code: A Man-in-the-Middle Attack Chain \| https://www.mitiga.io/blog/claude-code-mcp-token-theft-mitm \| Mitiga (5.5.2026). | Date corrected to 5.5.2026. |
| 719 | SOURCES[60] | Grok Build uploaded entire Git repositories to xAI storage, not just files it read \| https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html \| The Hacker News (July 2026). Researcher cereblab, Grok Build CLI 0.2.93. | Added: Hacker News, July 2026, cereblab, CLI 0.2.93. Read in a browser on 1 Nov: dated 14 Jul 2026, researcher cereblab, version 0.2.93. |
| 720 | SOURCES[61] | ClawHavoc: analysis of large-scale poisoning campaign targeting the OpenClaw skill market for AI agents \| https://www.antiy.net/p/clawhavoc-analysis-of-large-scale-poisoning-campaign-targeting-the-openclaw-skill-market-for-ai-agents/ \| Antiy CERT (6.2.2026). At least 1,184 malicious skills on ClawHub; Koi Security named the campaign. | Added: Antiy CERT, 6.2.2026, at least 1,184 skills; Koi named the campaign. |
| 745-746 | PLACE[9] D02/agent | GitSpawn: background Git calls in several agents ran a command from the repo's Git config, sometimes before the trust prompt. Separately, Check Point found Claude Code running project config before trust (CVE-2025-59536). | Pass 4. Before: one sentence put GitSpawn and the Check Point findings together as background Git calls. Check Point's finding (CVE-2025-59536) was project config, not Git. Now two sentences. |
| 752 | PLACE[12] D03/exth | GlassWorm's 2026 variants also install into other editors, such as VS Code, Cursor and Windsurf. | Pass 1. Before: "install into every editor on the machine". Socket names VS Code, Cursor and Windsurf. |
| 759 | PLACE[15] D04/files | Read(./.env) matches only the start folder; Read(.env) matches any depth. | Pass 1. Before: "Read(./.env) covers the project root only". Anthropic anchors ./ to the start folder; Read(.env) matches at any depth. |
| 767 | PLACE[21] D05/repo | Forever Security reported a planted AGENTS.md in a customer's Downloads folder in October 2026. | Pass 2. Before: "found in October 2026". Help Net gives no find date, only the October report. |
| 775-776 | PLACE[27] D06/mcp | Local MCP servers run as the user. Their tool descriptions enter the model context, where poisoned text acts as instructions. | Pass 4. Before also said a local HTTP server "must also validate Origin, bind to localhost and authenticate". The spec says must for Origin but should for localhost and auth. Sentence cut; row 787 states it correctly. |
| 781-783 | PLACE[30] D06/mcpr | Remote MCP servers, whoever runs them, hold their own tokens, receive what the agent sends and return results into the model context. Allowlist them by URL. The MCP spec says they must accept only tokens issued for them and must not pass a client's token on. | Pass 4. Before: servers "should accept only tokens issued for them". The spec says MUST and MUST NOT pass through. Pass 6 shortened it. |
| 784-785 | PLACE[31] D06/policy | VS Code, Claude Code and Codex each support an MCP allowlist. Claude Code and Codex can also restrict plugin marketplace sources; VS Code can set which plugins are enabled. | Pass 4. Before: "VS Code and Claude Code both support an MCP allowlist and a fixed plugin marketplace". VS Code has no marketplace lock (it has ChatEnabledPlugins); Codex added. |

## Sources used as evidence

All read between 30 October and 1 November 2026. The npm registry, the OpenAI managed configuration page and the four retitled sources were read again on 10 November 2026.

| Key | Source |
| --- | --- |
| npm-reg | https://registry.npmjs.org/npm (latest version) |
| npm-ext | https://docs.npmjs.com/cli/v12/configuring-npm/npm-extension/ |
| npm12-cfg | https://docs.npmjs.com/cli/v12/using-npm/config |
| npm11-cfg | https://docs.npmjs.com/cli/v11/using-npm/config |
| npm12-blog | https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/ |
| manifold | https://manifold.security/blog/ai-coding-agents-git-hijack |
| thn-gitspawn | https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html (blocks scripted fetches; read in a browser) |
| csa-p4s | https://labs.cloudsecurityalliance.org/research/csa-research-note-plugin4shell-ai-coding-agent-supply-chain/ |
| register-p4s | https://www.theregister.com/a/5297335 |
| gh-fw | https://github.blog/changelog/2026-10-20-github-package-firewall-in-public-preview/ |
| grok | https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html (read in a browser) |
| chaindrop | https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/ |
| cc-sbx | https://code.claude.com/docs/en/sandboxing |
| cc-plug | https://code.claude.com/docs/en/plugins/install |
| aws-q | https://aws.amazon.com/security/security-bulletins/AWS-2025-015/ |
| socket-gw | https://socket.dev/blog/73-open-vsx-sleeper-extensions-glassworm |
| s1ng | https://www.stepsecurity.io/blog/supply-chain-security-alert-popular-nx-build-system-package-compromised-with-data-stealing-malware |
| thn-nk | https://thehackernews.com/2026/01/north-korea-linked-hackers-target.html |
| helpnet | https://www.helpnetsecurity.com/2026/10/26/ai-coding-agents-malware-openai-codex/ |
| gen | https://www.gendigital.com/blog/insights/research/infostealers-your-ai-agent |
| mitiga | https://www.mitiga.io/blog/claude-code-mcp-token-theft-mitm |
| csa-ghost | https://labs.cloudsecurityalliance.org/research/csa-research-note-ghostapproval-ai-coding-agents-20260715-cs/ |
| itpro | https://www.itpro.com/software/development/claude-code-flaws-left-ai-tool-wide-open-to-hackers-heres-what-developers-need-to-know |
| cve | NVD pages for CVE-2025-59536, CVE-2026-21852, CVE-2026-19592, CVE-2025-48384 and CVE-2025-53773; cveawg.mitre.org; the CISA KEV JSON feed |
| vsc-pol | https://code.visualstudio.com/docs/enterprise/policies |
| vsc-sbx | https://code.visualstudio.com/docs/agents/run/agent-sandboxing |
| vsc-sec | https://code.visualstudio.com/docs/agents/run/security |
| vsc-appr | https://code.visualstudio.com/docs/agents/run/approvals |
| vsc-ext | https://code.visualstudio.com/docs/enterprise/extensions |
| vsc-ers | https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security |
| vsc-tasks | https://code.visualstudio.com/docs/debugtest/tasks |
| vsc-tun | https://code.visualstudio.com/docs/remote/tunnels |
| vsc-src | https://github.com/microsoft/vscode/blob/main/src/vs/platform/mcp/common/mcpManagement.ts |
| gh-cms | https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/enterprise-administrators/enterprise-managed-settings |
| cx-appr | https://developers.openai.com/codex/agent-approvals-security |
| cx-mc | https://learn.chatgpt.com/docs/enterprise/managed-configuration |
| cx-ar | https://learn.chatgpt.com/codex/sandboxing/auto-review |
| cx-sbx | https://learn.chatgpt.com/codex/sandboxing and https://learn.chatgpt.com/codex/permissions |
| search-cx | Web search on how Codex limits reads |
| cc-setref | https://code.claude.com/docs/en/settings-reference |
| cc-mset | https://code.claude.com/docs/en/managed-settings |
| cc-mcp | https://code.claude.com/docs/en/mcp |
| cc-perm | https://code.claude.com/docs/en/permissions |
| cc-pmodes | https://code.claude.com/docs/en/permission-modes |
| cc-settings | https://code.claude.com/docs/en/settings |
| cc-mmcp | https://code.claude.com/docs/en/managed-mcp |
| cc-sex | https://code.claude.com/docs/en/settings-example |
| mde | https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table |
| mcp-tr | https://modelcontextprotocol.io/specification/2025-06-18/basic/transports |
| mcp-bp | https://modelcontextprotocol.io/specification/draft/basic/security_best_practices |
| mcp-auth | https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization |
| mcp-arch | https://modelcontextprotocol.io/docs/learn/architecture |
| owasp-mcp | https://owasp.org/www-project-mcp-top-10/ |
| owasp-asi | https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ |
| ast01 | https://owasp.org/www-project-agentic-skills-top-10/ast01.html |
| devtun | https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies |
| unit42 | https://unit42.paloaltonetworks.com/stately-taurus-abuses-vscode-southeast-asian-espionage/ |
| ms-ir | https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents |
| snyk | https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/ |
| antiy | https://www.antiy.net/p/clawhavoc-analysis-of-large-scale-poisoning-campaign-targeting-the-openclaw-skill-market-for-ai-agents/ |
| gh-mcp | https://raw.githubusercontent.com/github/github-mcp-server/main/README.md |
| git-test | Local Git tests: Git 2.43.0 on 29 Oct 2026, Git 2.54.0 (Apple Git-157) on 1 Nov 2026 |
| dc-ref | https://containers.dev/implementors/json_reference/ |
| dc-cred | https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials |
| dc-docs | https://code.visualstudio.com/docs/devcontainers/containers |
| codeowners | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners |
| git-cred | https://git-scm.com/docs/git-credential-store |
| ssh-add | https://man.openbsd.org/ssh-add.1 |
| gh-secure | https://docs.github.com/en/actions/reference/security/secure-use |
| gh-resp | https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent |
| secaffairs | https://securityaffairs.com/171879/uncategorized/operation-digital-china-apt-targets-europe.html |
| thn-ides | https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html (read in a browser) |
| secweek | https://www.securityweek.com/organizations-warned-of-exploited-git-vulnerability/ |
| embrace | https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/ |
| datadog | https://securitylabs.datadoghq.com/articles/git-arbitrary-file-write/ |
| dgl | https://dgl.cx/2025/07/git-clone-submodule-cve-2025-48384 |
| ubuntu | https://ubuntu.com/security/CVE-2025-48384 |
| cursor-ext | https://cursor.com/docs/configuration/extensions |
| vscodium | https://github.com/VSCodium/vscodium (docs) |
| search-ovsx | Web search on Windsurf and Open VSX |

## Statement by statement

### Header

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | L268 | Risk map · VS Code, git CLI and local AI agents | - | UI | - | Page title. |
| 1 | L269 | Developer workstation risk map | - | UI | - | same as #0 |
| 2 | L270 | Where the ten most important risks sit when developers run VS Code, the git CLI and AI coding agents on their own machine, what to check for each, and seven further risks to keep in view. | - | OK | - | Matches the page: D01 to D10, then D11 to D17. |
| 3 | L272 | Frameworks OWASP Agentic Top 10 (2026), MCP Top 10 (beta) | owasp-asi, owasp-mcp | OK | - | OWASP titles its list "Top 10 for Agentic Applications for 2026"; the MCP Top 10 page says beta. |
| 4 | L273 | Vendor sources VS Code, Claude Code, OpenAI Codex, GitHub, Microsoft Defender, npm, Git | - | OK | - | Each vendor named has its own docs in Sources. |
| 5 | L274 | Facts checked 29 Oct 2026; corrections 30 Oct and 1 Nov 2026 | - | FIXED | 1 | Date line. Now names the 30 Oct and 1 Nov correction rounds. |
| 6 | L275 | Review persona-based passes and two audit rounds, records not attached | - | RECORD | - | Describes the Review tab. The persona and audit records are not attached, as it says. |
| 7 | L280 | 1 · Risk map | - | UI | - | Tab labels and heading. |
| 8 | L281 | 2 · Top 10 | - | UI | - | same as #7 |
| 9 | L282 | 3 · Review | - | UI | - | same as #7 |
| 10 | L283 | Sources | - | UI | - | same as #7 |

### In short

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 11 | L289 | In short | - | UI | - | same as #7 |
| 12 | L291 | Everything on the laptop starts with the developer's rights: VS Code, extensions, agents, MCP servers and install scripts. | cc-sbx, vsc-sbx, vsc-sec | OK | 3 | Vendor docs: tools, extensions, hooks and MCP servers run with the user's rights unless sandboxed. |
| 13 | L291 | A sandbox or per-tool permission narrows that only where it is on and covers the tool. | cc-sbx, vsc-sbx | OK | 3 | Both sandboxes wrap only what they list. Claude's page names what runs outside it. |
| 14 | L291 | Everything else can read what the developer can. | cc-sbx | OK | 3 | Claude's page: hooks, local MCP servers and helpers outside the sandbox "run with your full access". |
| 15 | L292 | The main question is: what can untrusted content, a bad add-on or a stolen token make the machine do, and what stops it? | - | JUDGEMENT | - | The framing question. Tagged [inference]. |
| 16 | L292 | [inference] | - | JUDGEMENT | - | same as #15 |
| 17 | L293 | Several documented 2025 and 2026 incidents entered through things developers fetch: repos, extensions, packages and agent add-ons. | chaindrop, socket-gw, aws-q, manifold, csa-p4s, antiy | OK | - | Each cited incident came in through a repo, an extension, a package or an agent add-on. |
| 18 | L293 | The incidents cited here are a sample, not a defined dataset, so no share is claimed. | - | JUDGEMENT | - | Method note. The page claims no share anywhere. |

### Risk map of the workstation

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 19 | L298 | Risk map of the workstation | - | UI | - | Diagram heading and legend text. |
| 20 | L299 | A typical enterprise developer machine, from what comes in to what goes out. | - | UI | - | same as #19 |
| 21 | L299 | Each marker shows where a risk enters or must be controlled. | - | UI | - | same as #19 |
| 22 | L299 | D01 to D10 are the top 10, coloured by the status you set under Top 10. | - | UI | 3 | same as #19 |
| 23 | L299 | D11 to D17, with dashed markers, are the further risks listed below the map. | - | UI | - | same as #19 |
| 24 | L301 | More risks | - | UI | - | same as #19 |
| 25 | L311 | Untrusted inputs (1) reach the workstation (2), where VS Code, extensions and the agent act with the developer's rights. | cc-sbx, vsc-sec | OK | - | Same basis as row 12. |
| 26 | L311 | Traffic leaves through the egress boundary (3), a control point only where traffic is forced through a proxy or gateway. | - | JUDGEMENT | 4 | How the diagram zones are meant. A design statement, not a fact claim. |
| 27 | L311 | Governance and monitoring (4) covers every layer. | - | JUDGEMENT | - | same as #26 |
| 28 | L312 | The dashed two-way line starts outbound but carries commands back in. | unit42, devtun | OK | 4 | A tunnel connects outbound, then lets a remote party send commands in (Unit 42 on code tunnel). |
| 29 | L312 | Arrows show selected paths, not every data flow. | - | UI | 3 | Diagram help and legend labels. |
| 30 | L312 | Select a marker or a box to see its risks. | - | UI | 3 | same as #29 |
| 31 | L314 | D01 Not assessed | - | UI | - | same as #29 |
| 32 | L315 | D01 OK (tested, with evidence; see Top 10) | - | UI | - | same as #29 |
| 33 | L316 | D01 Partial | - | UI | - | same as #29 |
| 34 | L317 | D01 Missing | - | UI | - | same as #29 |
| 35 | L318 | D01 Unknown | - | UI | - | same as #29 |
| 36 | L319 | D11 More risks, not in the top 10 (no status) | - | UI | - | same as #29 |
| 37 | L320 | Agent sandbox, if enabled (covers agent commands; MCP coverage depends on the agent) | cc-sbx, vsc-sbx | OK | - | VS Code: chat.agent.sandbox.mcpServers defaults to true and sandboxes local MCP servers. Claude: local MCP servers run outside the sandbox. |
| 38 | L324 | The diagram is wide. | - | UI | - | Headings, table labels and help text. |
| 39 | L324 | Drag sideways in it, or use the table below. | - | UI | - | same as #38 |

### Risk by zone

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 40 | L327 | Risk by zone | - | UI | - | same as #38 |
| 41 | L328 | The same placement as the diagram, for the top 10 risks. | - | UI | - | same as #38 |
| 42 | L328 | D11 to D17 are in the same layout under More risks. | - | UI | - | same as #38 |
| 43 | L328 | Select a risk to show it in the diagram. | - | UI | - | same as #38 |
| 44 | L332 | Risk 1 · Inputs 2 · Workstation 3 · Outbound 4 · Governance | - | UI | - | same as #38 |

### More risks

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 45 | L339 | More risks | - | UI | - | same as #38 |
| 46 | L340 | Seven risks outside the top 10 that belong in a full assessment, placed the same way as the diagram. | - | UI | - | same as #38 |
| 47 | L340 | They have dashed markers in the diagram. | - | UI | - | same as #38 |
| 48 | L340 | Select a risk to show it in the diagram. | - | UI | - | same as #38 |
| 49 | L344 | Risk 1 · Inputs 2 · Workstation 3 · Outbound 4 · Governance | - | UI | - | same as #38 |

### Relevance and first control

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 50 | L351 | Relevance and first control | - | UI | - | same as #38 |
| 51 | L352 | All 17 risks in the order of the two tables above. | - | UI | - | same as #38 |
| 52 | L352 | Open a risk for its description and first control. | - | UI | 3 | same as #38 |
| 53 | L352 | For D01 to D10 the first control and its friction come from Where to start under Top 10. | - | UI | 3 | same as #38 |
| 54 | L352 | For D11 to D17 relevance is interpretation by AI for an enterprise developer fleet. | - | JUDGEMENT | - | Relevance of D11 to D17 is the author's call. Tagged. |
| 55 | L352 | [inference] | - | JUDGEMENT | - | same as #54 |
| 56 | L357 | Before you use the map | - | UI | - | Heading. |
| 57 | L358 | This is a reference layout, not your organisation's setup. | - | JUDGEMENT | 3 | Reference layout and placement are the author's call. Tagged. |
| 58 | L358 | Common differences: agents used only in the terminal, all agent work in dev containers or cloud sessions, an internal package proxy, and VS Code forks such as Cursor or Windsurf. | - | JUDGEMENT | 3 | same as #57 |
| 59 | L358 | Draw your own variant and move the markers. | - | JUDGEMENT | 3 | same as #57 |
| 60 | L359 | The placement of risks and the owner per zone are interpretation by AI based on the sources. | - | JUDGEMENT | - | same as #57 |
| 61 | L359 | [inference] | - | JUDGEMENT | - | same as #57 |

### The ten risks

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 62 | L366 | The ten risks | - | UI | - | Heading. |
| 63 | L367 | Proposed, not measured: the order weighs how often each risk appears in the cited reporting against how far the damage reaches. | - | JUDGEMENT | 9 | Priority method and classification. The page calls it proposed, not measured. Pass 9: joined two sentences (was "A proposed priority order, not a measured ranking. It weighs how often ..."). |
| 64 | L367 | D09 and D10 are a control gap and a data governance risk, not attack paths. | - | JUDGEMENT | - | Priority method and classification. The page calls it proposed, not measured. |
| 65 | L367 | VS Code tunnels (D13), used in real attacks, are the strongest candidate to move up. | unit42, secaffairs | CUT | 9 | Unit 42 (Sep 2024) and SentinelLabs via Security Affairs (Dec 2024) report attackers using VS Code tunnels. "Strongest candidate to move up" is judgement. Pass 9: "have been used in real attacks and are" became "used in real attacks, are". Same claim. |
| 66 | L367 | The order and OWASP mapping are interpretation by AI. | - | JUDGEMENT | 9 | Tagged [inference]. Pass 9: dropped "the". |
| 67 | L367 | [inference] | - | JUDGEMENT | - | Tagged [inference]. |
| 68 | L371 | Current as of 1 November 2026 | - | FIXED | 1 | Was 30 October. Now 1 November 2026, the date of this check. |
| 69 | L373 | npm: npm 12 has been out since July 2026 (12.2.2 was current on the npm registry on 10 November 2026). | npm-reg | OK | - | Registry on 1 Nov 2026: latest 12.2.1; 12.0.0 published 8 Jul 2026. Rechecked 10 Nov 2026: latest 12.2.2, published 4 Nov 2026; statement updated. |
| 70 | L373 | It no longer runs dependency install scripts unless they are approved. | npm12-blog, npm12-cfg | OK | - | npm 12 runs dependency install scripts only when allowed by allow-scripts. |
| 71 | L373 | It still runs the project's own.npm-extension.mjs or.npm-extension.cjs on npm install (not on npm ci), and dangerously-allow-all-scripts switches script approval off. | npm-ext, npm12-cfg | OK | - | npm install runs the root .npm-extension file, npm ci does not. dangerously-allow-all-scripts turns approval off. |
| 72 | L374 | GitSpawn: at publication on 1 September 2026, four of eight findings across seven agents were unpatched, including a second Claude Code path still open on 2.1.252. | manifold | OK | 3 | Manifold, 1 Sep 2026: 8 findings across 7 agents, 4 unpatched; a second Claude Code path still open on 2.1.252. |
| 73 | L374 | It needs a repo that arrives as files with its.git folder; a normal clone does not carry it. | manifold, git-test | OK | 3 | Manifold: a normal clone does not trigger it. Local test: git clone does not copy the remote's .git/config. |
| 74 | L374 | A global core.fsmonitor of false does not help, because the repo's own config wins. | git-test | OK | 3 | Tested on Git 2.54.0, 1 Nov 2026: repo core.fsmonitor ran despite a global false. |
| 75 | L375 | Plugin4Shell: fixed in Claude Code 2.1.179 and Codex 0.146.0. | csa-p4s | OK | - | CSA: fixed in Claude Code 2.1.179 and Codex 0.146.0. |
| 76 | L375 | At disclosure on 18 September Copilot had no client fix and Gemini CLI was not being fixed. | csa-p4s, register-p4s | OK | - | CSA: disclosed 18 Sep 2026; Copilot had no client fix; Gemini CLI would not be fixed. |
| 77 | L376 | GitHub package firewall: public preview since 20 October 2026 for GitHub Enterprise Cloud, npm only. | gh-fw | OK | - | GitHub changelog 20 Oct 2026: public preview, Enterprise Cloud, npm only. |
| 78 | L377 | Sandboxes on Windows: Claude Code does not sandbox on native Windows (WSL2 only). | cc-sbx | OK | - | Claude sandbox: macOS, Linux and WSL2. Native Windows is not supported. |
| 79 | L377 | VS Code's Windows sandbox is experimental and needs a recent Windows 11 build. | vsc-sbx | OK | - | VS Code: the Windows sandbox is experimental and needs a recent Windows 11 build. |
| 80 | L382 | Where to start | - | UI | - | Heading. |
| 81 | L383 | One first control per risk that gives visible value at fleet scale. | - | JUDGEMENT | - | Choice of first control and friction. Tagged. |
| 82 | L383 | Suggested by the endpoint reviewer; the friction is their estimate. | - | JUDGEMENT | - | same as #81 |
| 83 | L383 | [inference] | - | JUDGEMENT | - | same as #81 |
| 84 | L387 | Risk First control Friction | - | UI | - | Table header and heading. |
| 85 | L394 | What a status means | - | UI | - | same as #84 |
| 86 | L395 | OK: in place and tested on a named product and operating system, with evidence and a date recorded elsewhere; this page stores only the status, in this browser. | - | CUT | 9 | Status definition (the author's) merged with two old statements: "Record those details elsewhere; this page stores only the status" and "Status is stored only in this browser". Pass 9: re-checked the page code on 1 Nov 2026: status is saved with localStorage only, and the page makes no network requests. |
| 87 | L395 | Partial: covers some products, platforms or users. | - | JUDGEMENT | 9 | Status definitions. The page says they are the author's. Pass 9: "some products, platforms or users are covered" became "covers some products, platforms or users". |
| 88 | L395 | Missing: not in place. | - | JUDGEMENT | - | Status definitions. The page says they are the author's. |
| 89 | L395 | Unknown: looked at but not confirmed. | - | JUDGEMENT | 3 | same as #88 |
| 90 | L395 | Not assessed: nobody has looked yet. | - | JUDGEMENT | 3 | same as #88 |
| 91 | L395 | These definitions are interpretation by AI. | - | JUDGEMENT | 3 | same as #88 |
| 92 | L395 | [inference] | - | JUDGEMENT | - | same as #88 |
| 93 | L400 | OK 0 | - | UI | - | Counters, buttons and filter labels. |
| 94 | L401 | Partial 0 | - | UI | - | same as #93 |
| 95 | L402 | Missing 0 | - | UI | - | same as #93 |
| 96 | L403 | Unknown 0 | - | UI | - | same as #93 |
| 97 | L404 | Not assessed 10 | - | UI | - | same as #93 |
| 98 | L408 | Copy status as text | - | UI | - | same as #93 |
| 99 | L409 | Reset | - | UI | - | same as #93 |
| 100 | L410 | Yes, reset all Cancel | - | UI | - | same as #93 |
| 101 | L417 | Filter by attack path | - | UI | - | same as #93 |
| 102 | L419 | All | - | UI | - | same as #93 |
| 103 | L420 | Poisoned content | - | UI | - | same as #93 |
| 104 | L421 | Booby-trapped project | - | UI | - | same as #93 |
| 105 | L422 | Supply chain | - | UI | - | same as #93 |
| 106 | L423 | Stolen tokens | - | UI | - | same as #93 |
| 107 | L425 | Shows all ten. | - | UI | - | same as #93 |
| 108 | L425 | The link between attack path and risk is interpretation by AI. | - | JUDGEMENT | - | Path-to-risk link. Tagged. |
| 109 | L425 | [inference] | - | JUDGEMENT | - | same as #108 |

### D01

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 110 | L431 | D01 Malicious packages and install scripts OWASP ASI04 Agentic Supply Chain Vulnerabilities | owasp-asi | OK | - | ASI04 is "Agentic Supply Chain Vulnerabilities". The mapping itself is judgement (row 66). |
| 111 | L432 | A package install can run code before anyone reads it. | chaindrop | OK | - | A preinstall script runs during install. |
| 112 | L432 | ChainDrop (Microsoft, 4 August 2026) used a preinstall script in more than 400 npm packages to steal credentials and republish packages. | chaindrop | OK | 5 | Microsoft, 4 Aug 2026: preinstall script, more than 400 npm packages, stole credentials and republished packages. |
| 113 | L432 | Some copies had valid provenance from a real CI workflow, so provenance alone does not prove safety. | chaindrop | OK | 3 | Microsoft: some malicious versions carried valid provenance from a real CI workflow. |
| 114 | L433 | In August 2025 the s1ngularity malware ran installed AI CLIs with their permission checks off to search the disk for secrets. | s1ng | OK | 3 | StepSecurity, Aug 2025: the Nx malware ran installed AI CLIs with permission-skipping flags to look for secrets. |
| 115 | L434 | Check | - | UI | - | Label. |
| 116 | L436 | Is npm 12 (released July 2026) or later in use? | npm-reg | OK | - | 12.0.0 published 8 Jul 2026. |
| 117 | L436 | It runs dependency install scripts only when approved. | npm12-blog, npm12-cfg | OK | - | Same as row 70. |
| 118 | L436 | It needs Node.js 22.22.2, 24.15.0 or 26 and later, so plan it as a fleet change. | npm-reg | OK | - | npm 12.0.0 engines: node ^22.22.2, ^24.15.0 or &gt;=26.0.0. |
| 119 | L437 | [command] npm --version | npm12-cfg | OK | - | Commands. All five config keys exist in the npm v12 config docs. |
| 120 | L438 | npm config get ignore-scripts min-release-age dangerously-allow-all-scripts ignore-extension extension-file Copy | npm12-cfg | OK | - | same as #119 |
| 121 | L439 | Do any projects bypass or widen script approval? dangerously-allow-all-scripts runs every dependency install script; npm calls it a migration escape hatch only. | npm12-cfg | OK | 3 | npm docs: dangerously-allow-all-scripts runs every install script and is meant as a migration escape hatch. |
| 122 | L439 | Review allowScripts grants in package.json and.npmrc, since a repo can carry its own [inference]. | npm12-cfg | OK | 3 | allowScripts can live in package.json and .npmrc. The repo point is tagged [inference]. |
| 123 | L439 | [not run here] | - | UI | - | Tag. |
| 124 | L440 | Is project code that runs outside script approval reviewed? npm install runs a root.npm-extension.mjs or.npm-extension.cjs before dependencies resolve; npm ci only checks its recorded hash. ignore-extension or ignore-scripts skips it. | npm-ext | OK | 3 | npm docs: npm install runs it before resolving dependencies; npm ci only checks its recorded hash; ignore-extension and ignore-scripts skip it. |
| 125 | L440 | The docs do not say whether script approval covers it, so treat it as uncovered [inference]. | npm-ext | JUDGEMENT | 3 | The docs are silent on this. Tagged [inference]. |
| 126 | L440 | Put these files under code-owner review (D02). | - | JUDGEMENT | - | Advice. |
| 127 | L441 | Is there a cooldown before new versions install? min-release-age in a managed npmrc is only a default: a command-line flag, an environment variable or a project.npmrc overrides it. | npm11-cfg, npm12-cfg | OK | 3 | npm precedence: command line, environment, project, user, global. So the managed file loses. |
| 128 | L441 | To enforce it, use the registry or a package firewall (GitHub's is in public preview, npm only). | gh-fw | OK | 3 | Same as row 77. |
| 129 | L442 | Is there a route for urgent security fixes? | - | QUESTION | - | Check question. |
| 130 | L442 | If a cooldown blocks the fix npm audit fix would install, npm keeps the vulnerable version and warns. min-release-age-exclude exempts named packages. | npm12-cfg | OK | 3 | npm docs: if the cooldown blocks an audit fix, npm keeps the vulnerable version and warns. min-release-age-exclude exists. |
| 131 | L442 | Agree who grants exceptions and for how long. | - | JUDGEMENT | 3 | Process advice. Tagged. |
| 132 | L442 | [inference] for the process. | - | JUDGEMENT | - | same as #131 |
| 133 | L443 | Do installs go through an internal registry or proxy rather than straight to public registries? | - | QUESTION | - | Check questions. Tagged where needed. |
| 134 | L444 | Are pnpm, Yarn, pip and other package managers covered too? | - | QUESTION | - | same as #133 |
| 135 | L444 | [inference] | - | QUESTION | - | same as #133 |
| 136 | L446 | Typical findings npm 10 or 11 with scripts on, no cooldown or one that a flag or project file can undo, provenance treated as proof of safety, script approval switched off or widened, root extension files nobody reviews. | - | JUDGEMENT | - | Typical findings, from the reviewers. |
| 137 | L447 | Supply chain Stolen tokens | - | UI | - | Attack path tags. |

### D02

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 138 | L452 | D02 Code runs when a project is opened OWASP ASI05 Unexpected Code Execution | owasp-asi | OK | - | ASI05 is "Unexpected Code Execution". |
| 139 | L453 | Project files that survive a clone can name a program to run:.vscode/tasks.json, workspace settings,.devcontainer/devcontainer.json (its initializeCommand runs on the host),.claude/settings.json,.mcp.json and npm's root.npm-extension files. | vsc-tasks, dc-ref, cc-setref, cc-mcp, npm-ext | OK | 5 | Each file can name a program: tasks, initializeCommand (runs on the host), hooks in settings, stdio servers in .mcp.json, the npm root extension. |
| 140 | L453 | North Korea's Contagious Interview campaign sends fake coding tests whose tasks.json runs on folder open. | thn-nk | OK | 3, 4, 5, 9 | THN Jan 2026: fake coding tests with tasks.json runOn folderOpen. Pass 9: this was joined to the next sentence in the extracted text; it is now its own row. |
| 141 | L454 | .git/config and hooks arrive only when a project is shared as files, such as a zip. | git-test | OK | 5, 9 | Local test: clone does not bring .git/config or hooks. Pass 9: starts a new paragraph. |
| 142 | L454 | In GitSpawn (September 2026), background Git calls in seven agents ran a command from that config, sometimes before the trust prompt. | manifold | OK | 4 | Manifold: background Git calls in seven agents ran it, some before the trust prompt. |
| 143 | L455 | Check | - | UI | - | Label. |
| 144 | L457 | Is Workspace Trust left on, and do developers choose restricted mode for unreviewed code? | - | QUESTION | - | Check question. |
| 145 | L457 | CLI agents have their own trust prompts, and GitSpawn showed that some run code before them. | manifold | OK | - | Same as row 142. |
| 146 | L458 | Are automatic tasks kept off? task.allowAutomaticTasks is off by default, but VS Code asks once per workspace whether to allow them, and on runs them in every trusted workspace without asking. | vsc-tasks | OK | - | VS Code tasks docs: default off; VS Code asks per workspace; on runs them without asking in trusted workspaces. |
| 147 | L458 | Automatic tasks never run in an untrusted workspace. | vsc-tasks | OK | - | Docs: automatic tasks do not run in untrusted workspaces. |
| 148 | L458 | Decide whether developers may answer Allow, and check that no settings file sets on. | - | JUDGEMENT | - | Advice. |
| 149 | L459 | Are agents on current versions? | - | QUESTION | - | Check question and pointer. |
| 150 | L459 | See the Current box above. | - | QUESTION | - | same as #149 |
| 151 | L460 | Did the repo arrive as files rather than as a clone? | - | QUESTION | - | Check question. |
| 152 | L460 | Then read its Git config before an agent opens the folder, and look in.git/hooks too. | - | JUDGEMENT | - | Advice. |
| 153 | L460 | Look for fsmonitor, hookspath, sshcommand, pager, editor, filter, textconv and include. | manifold | OK | - | Manifold names fsmonitor. The others are Git keys that name a program to run, or (include) pull in another config file. |
| 154 | L461 | [command] git config --file &lt;repo&gt;/.git/config --list --show-origin Copy | git-test | OK | - | Command ran on Git 2.54.0. |
| 155 | L462 | Do not rely on git config --global core.fsmonitor false. | git-test | OK | - | Tested 29 Oct (Git 2.43.0) and 1 Nov 2026 (Git 2.54.0). |
| 156 | L462 | A repo's own config overrides it; this was tested here. | git-test | OK | - | same as #155 |
| 157 | L462 | An environment override ( GIT\_CONFIG\_COUNT) does block it, but it also breaks legitimate fsmonitor use, and it does not cover the other command-bearing settings. | git-test | OK | - | Tested: GIT\_CONFIG\_COUNT blocks it. It sets one key, so other keys stay open. |
| 158 | L463 | Do changes to.vscode/,.claude/,.devcontainer/, AGENTS.md,.npm-extension.\* and.npmrc need code-owner approval? | - | QUESTION | - | Check question. |
| 159 | L463 | A CODEOWNERS file on its own only requests review. | codeowners | OK | - | GitHub: CODEOWNERS only requests review; required approval needs the branch rule. GitHub advises owning CODEOWNERS itself. |
| 160 | L463 | Turn on Require review from Code Owners in branch protection or a ruleset, give CODEOWNERS itself an owner, and review who can bypass the rule. | codeowners | OK | - | same as #159 |
| 161 | L463 | [inference] for the bypass point. | - | JUDGEMENT | - | Tagged [inference]. |
| 162 | L464 | Is Git patched for CVE-2025-48384 on macOS and Linux? | - | QUESTION | - | Check question. |
| 163 | L464 | Windows is not affected. | datadog, dgl | OK | - | Datadog and the finder (dgl.cx): Windows is not affected. |
| 164 | L464 | Distributions backport fixes without changing the version string, so use vulnerability-management inventory rather than git --version. | ubuntu | OK | - | Ubuntu lists the fix as 1:2.43.0-1ubuntu7.3 while git --version still says 2.43.0. |
| 165 | L466 | Typical findings Trust granted to every folder, repos from shared drives opened straight in an agent, no review on config folders. | - | JUDGEMENT | - | Typical findings. |
| 166 | L467 | Booby-trapped project | - | UI | - | Tag. |

### D03

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 167 | L472 | D03 Malicious or hijacked extensions OWASP ASI04 Agentic Supply Chain Vulnerabilities | owasp-asi | OK | - | ASI04 name matches. |
| 168 | L473 | An extension runs with the developer's rights. | vsc-ext, vsc-sec | OK | 3 | VS Code docs: extensions run with the user's rights. |
| 169 | L473 | In July 2025 the official Amazon Q Developer extension 1.84.0 shipped with malicious code added through a mis-scoped GitHub token; AWS says it failed to run because of a syntax error. | aws-q | OK | - | AWS-2025-015: 1.84.0 had malicious code via a mis-scoped token; it did not run because of a syntax error. |
| 170 | L474 | GlassWorm has hit Open VSX in waves since October 2025, and its 2026 variants also install into VS Code, Cursor and Windsurf. | socket-gw | FIXED | 3 | Was "every editor". Socket names VS Code, Cursor and Windsurf, and waves since Oct 2025. |
| 171 | L474 | Cursor, Windsurf and VSCodium use Open VSX by default. | cursor-ext, vscodium, search-ovsx | OK | 3 | Cursor and VSCodium docs name Open VSX; Windsurf by search. |
| 172 | L475 | Check | - | UI | - | Label. |
| 173 | L477 | Is the AllowedExtensions policy deployed (VS Code 1.96 or later), seeded from the current inventory? | vsc-ext, vsc-pol | OK | - | AllowedExtensions policy, VS Code 1.96 or later. |
| 174 | L477 | It overrides the user setting. | vsc-pol | OK | 3 | Policies override user settings. |
| 175 | L477 | It is not an integrity control: for a local VSIX, Microsoft says it does not verify origin, stop changes to installed files, or limit runtime permissions. | vsc-ext | OK | 3 | VS Code docs say this for a local VSIX. |
| 176 | L477 | Add a private marketplace and file-integrity monitoring of extension folders [inference]. | - | JUDGEMENT | 3 | Tagged [inference]. |
| 177 | L478 | Is ExtensionsAutoUpdateDelay set, so a new extension version waits some hours before it installs? | vsc-pol | OK | - | ExtensionsAutoUpdateDelay: hours to wait after an update is published. |
| 178 | L479 | Do you need a private marketplace ( ExtensionGalleryServiceUrl, or GitHub's private marketplace for Enterprise customers)? | vsc-ext | OK | - | ExtensionGalleryServiceUrl and GitHub's private marketplace for Enterprise. |
| 179 | L480 | Which editors are approved? | - | QUESTION | - | Check question. |
| 180 | L480 | Forks are not governed by VS Code policies, so block unapproved editors with application control. | - | JUDGEMENT | - | Tagged [inference]. |
| 181 | L480 | [inference] | - | JUDGEMENT | - | same as #180 |
| 182 | L481 | Which extensions are installed? | - | QUESTION | - | Check question. Tag. |
| 183 | L481 | [not run here] | - | QUESTION | - | same as #182 |
| 184 | L482 | [command] code --list-extensions --show-versions Copy | - | OK | - | Real VS Code CLI command. |
| 185 | L484 | Typical findings No allowlist, extensions from unknown publishers, forks outside policy. | - | JUDGEMENT | - | Typical findings. |
| 186 | L485 | Supply chain | - | UI | - | Tag. |

### D04

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 187 | L490 | D04 Secrets and long-lived tokens on the machine OWASP ASI03 Identity and Privilege Abuse · MCP01 Token Mismanagement | owasp-asi, owasp-mcp | OK | - | ASI03 "Identity and Privilege Abuse"; MCP01 "Token Mismanagement" (OWASP MCP Top 10 beta list). |
| 188 | L491 | A developer laptop holds SSH keys, Git, cloud and npm tokens,.env files, and now agent tokens and transcripts. | cc-setref, gen | OK | 3 | Agent tokens and transcripts are stored locally (cleanupPeriodDays keeps transcripts); Gen Digital lists them as infostealer targets. |
| 189 | L491 | Any process running as the user can read unprotected credential files and use credentials exposed through a helper or agent. | cc-sbx | OK | 3 | Claude's page: processes outside the sandbox run with full access; files readable by the user are readable by them. |
| 190 | L491 | Infostealers now collect AI agent tokens too (Gen Digital, September 2026). | gen | OK | 5, 9 | Gen Digital, 8 Sep 2026: infostealers collect AI agent access tokens and MCP configs. Pass 9: moved into the first paragraph of the card. |
| 191 | L492 | Sandboxes do not change that by default: Claude Code's sandbox reads ~/.ssh and ~/.aws unless denied, VS Code passes Git and GitHub CLI credentials in, and Dev Containers forward the SSH agent and reuse local Git credentials. | cc-sbx, vsc-sbx, dc-cred | OK | 4 | Claude: default reads cover "~/.ssh and ~/.aws/credentials". VS Code: credential settings default to true and pass Git and GitHub CLI auth. Dev Containers: SSH agent forwarded, local Git credentials reused. |
| 192 | L493 | Check | - | UI | - | Label. |
| 193 | L495 | Is a Git credential helper set to store ? | - | QUESTION | - | Check question. |
| 194 | L495 | It saves credentials unencrypted in ~/.git-credentials. | git-cred | OK | 3 | Git docs: the store helper keeps credentials unencrypted in ~/.git-credentials. |
| 195 | L495 | The command shows every scope, including system. | git-test | OK | 3 | --show-origin with --get-all lists every scope, system included. |
| 196 | L496 | [command] git config --show-origin --get-all credential.helper Copy | git-test | OK | - | same as #195 |
| 197 | L497 | Are SSH keys protected by more than file permissions? | - | QUESTION | - | Check question. |
| 198 | L497 | A key in an SSH agent can be used without its file, so control who can reach the agent socket [inference]. | - | JUDGEMENT | 5 | Tagged [inference]. |
| 199 | L497 | Load keys with ssh-add -t (lifetime), -c (confirm each use) and -h (limit destinations; OpenSSH 8.9 or later). | ssh-add | OK | 5 | ssh-add(1): -t lifetime, -c confirm each use, -h destination constraints (OpenSSH 8.9). |
| 200 | L497 | [not run here] | - | UI | - | Tag. |
| 201 | L498 | Are secret files kept out of agent reads, not only edits? | - | QUESTION | - | Check question. |
| 202 | L498 | Treat four controls separately: read restriction, edit approval, command isolation, and whether the secret is on the machine at all. | - | JUDGEMENT | - | Framing advice. |
| 203 | L500 | VS Code: chat.tools.edits.autoApprove with "\*\*/.env": false only gates edits. | vsc-appr, vsc-sec | OK | 5 | chat.tools.edits.autoApprove decides which edits need approval. It does not restrict reads. |
| 204 | L500 | GitHub's managed permissions.deny with Read(...) rules blocks reads, but only in Copilot Agent Host sessions. sandbox.userPolicy.filesystem.deniedPaths covers processes the agent starts. | gh-cms | OK | 5 | GitHub: permission rules "apply to Copilot sessions that use Agent Host"; a managed deniedPaths adds to the user's. |
| 205 | L501 | Claude Code: Read(...) deny rules in permissions.deny block the Read tool and are merged into the sandbox. sandbox.filesystem.denyRead or sandbox.credentials alone covers shell commands only. | cc-perm, cc-sbx | OK | 3 | Claude: Read deny rules stop the Read tool and are merged into the sandbox config; denyRead and credentials entries constrain sandboxed commands only. |
| 206 | L501 | Read(./.env) matches only the start folder; Read(.env) matches any depth. | cc-perm | FIXED | 2, 3 | Was "project root". Docs: Read(./.env) matches .env in the current directory, where Claude started. Read(.env) matches at any level. |
| 207 | L501 | Add rules for ~/.ssh and cloud credential folders. | - | JUDGEMENT | 3 | Advice. |
| 208 | L502 | Codex: [permissions.filesystem] deny\_read in requirements.toml, which users cannot weaken. | cx-mc | OK | - | Codex: admins deny reads with [permissions.filesystem]; requirements.toml cannot be weakened by users. |
| 209 | L502 | On native Windows it applies to direct file tools, not to shell subprocess reads. | cx-mc | OK | - | Codex: "On native Windows, managed deny\_read applies to direct file tools; shell subprocess reads don't use this sandbox rule." |
| 210 | L504 | Do GitHub and npm tokens expire, and are they narrowly scoped? | - | QUESTION | - | Check questions. |
| 211 | L504 | Can a developer laptop reach production with its own credentials? | - | QUESTION | - | same as #210 |
| 212 | L505 | Are agent config files with tokens watched for change? | - | QUESTION | - | same as #210 |
| 213 | L505 | Research by Mitiga showed an install script planting a hook that rewrote MCP server addresses in ~/.claude.json to capture OAuth tokens. | mitiga | OK | - | Mitiga, 5 May 2026: an install-time hook rewrote MCP server entries in ~/.claude.json to a local proxy and captured the OAuth token. |
| 214 | L506 | How long do agents keep transcripts? | - | QUESTION | - | Check question. |
| 215 | L506 | Claude Code: cleanupPeriodDays. | cc-setref | OK | - | cleanupPeriodDays: "how many days Claude Code keeps transcripts". |
| 216 | L508 | Typical findings Broad tokens that never expire, the store helper in use, production keys in.env files. | - | JUDGEMENT | - | Typical findings. |
| 217 | L509 | Stolen tokens Supply chain Booby-trapped project | - | UI | - | Tags. |

### D05

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 218 | L514 | D05 Prompt injection and poisoned instruction files OWASP ASI01 Agent Goal Hijack | owasp-asi | OK | - | ASI01 is "Agent Goal Hijack". |
| 219 | L515 | Text the agent reads can redirect it: a web page, issue, README, code comment, file name or MCP tool output. | mcp-bp, vsc-sec | OK | 3 | Sources list web content, issues, files and tool output as injection carriers. |
| 220 | L515 | Agents load instruction files such as AGENTS.md and CLAUDE.md as instructions, so these carry more weight. | vsc-sec, cc-setref | OK | 5 | AGENTS.md and CLAUDE.md are loaded as instructions by design. |
| 221 | L516 | In October 2026 Forever Security reported a planted AGENTS.md in a customer's Downloads folder that tried to make Codex install a malicious npm package. | helpnet | FIXED | 2 | Was "found ... in October 2026". Help Net (26 Oct 2026) reports the find but gives no find date, so now "reported". |
| 222 | L516 | In testing, Codex followed it in more than 90% of attempts. | helpnet | OK | 5 | "In our testing, Codex ran the malware in more than 90% of attempts." |
| 223 | L517 | Check | - | UI | - | Label. |
| 224 | L519 | Do developers start agents only inside a project folder, never in the home folder or Downloads? | - | QUESTION | - | Check questions. |
| 225 | L520 | Are AGENTS.md, CLAUDE.md and other rule files reviewed like code, for example through CODEOWNERS? | - | QUESTION | - | same as #224 |
| 226 | L521 | Are unreviewed repos opened in VS Code restricted mode? | - | QUESTION | - | same as #224 |
| 227 | L521 | It disables agents in VS Code only; CLI agents rely on their own trust prompts. | vsc-sec | OK | - | VS Code restricted mode disables agents in VS Code. CLI agents have their own trust prompts (Manifold, row 142). |
| 228 | L522 | Are there instruction files you did not write? | - | QUESTION | - | Check question and help. |
| 229 | L522 | Each command lists files to review. | - | QUESTION | - | same as #228 |
| 230 | L523 | [command] # macOS and Linux | - | OK | - | Find commands. Syntax checked; the macOS one ran here. |
| 231 | L524 | find ~/Downloads ~ -maxdepth 4 \\( -name AGENTS.md -o -name CLAUDE.md \\) -not -path '\*/node\_modules/\*' 2&gt;/dev/null \| sort -u | - | OK | - | same as #230 |
| 232 | L525 | # Windows PowerShell | - | OK | - | same as #230 |
| 233 | L526 | Get-ChildItem -Path $HOME -Recurse -Depth 4 -Include AGENTS.md,CLAUDE.md -ErrorAction SilentlyContinue \| Select-Object FullName Copy | - | OK | - | same as #230 |
| 234 | L528 | Typical findings Agents started from the home folder or Downloads, instruction files changed without review, fetch allowed for any domain. | - | JUDGEMENT | - | Typical findings. |
| 235 | L529 | Poisoned content Booby-trapped project | - | UI | - | Tags. |

### D06

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 236 | L534 | D06 Untrusted MCP servers, plugins and skills OWASP ASI04 · MCP03 Tool Poisoning · MCP07 Insufficient Authentication and Authorization · AST01 Malicious Skills | owasp-asi, owasp-mcp, ast01 | OK | - | MCP03 Tool Poisoning, MCP07 Insufficient Authentication and Authorization, AST01 Malicious Skills match OWASP titles. |
| 237 | L535 | A local MCP server runs as the developer, and its tool descriptions go straight into the model's context. | mcp-arch, mcp-bp | OK | 3 | A local stdio server is a process the client starts; tool descriptions go to the model. |
| 238 | L535 | A remote one holds its own tokens, sees what the agent sends and can return prompt injection. | mcp-bp, mcp-auth | OK | 5 | Remote servers hold their own tokens and return content the client passes to the model. |
| 239 | L535 | ClawHavoc put more than 1,000 malicious skills on ClawHub in early 2026. | antiy, ast01 | FIXED | 4 | Source added. Antiy CERT (6 Feb 2026): "at least 1,184 malicious Skills ... on ClawHub". Snyk's 76 does not back it. |
| 240 | L535 | In Plugin4Shell (September 2026), Claude Code, Codex and Copilot ran git checkout &lt;SHA&gt; for a pinned plugin without checking the result, so a branch named after the hash could win. | csa-p4s, register-p4s, cc-plug | CUT | 3, 4, 5 | Shortened 188 -&gt; 83 words. CSA: git checkout of a pinned SHA without checking; a branch named after the hash wins; auto-update made it zero-click. Claude docs: auto-update off for third-party marketplaces. |
| 241 | L535 | It needs control of the plugin's repo, an update that re-pins it, and a Git host that allows hash-named branches. | csa-p4s, register-p4s, cc-plug | CUT | 3, 4, 5 | same as #240 |
| 242 | L536 | CSA says automatic updates, then on by default, made it zero-click; Claude Code's docs now leave them off for third-party marketplaces. | csa-p4s, register-p4s, cc-plug | CUT | 3, 4, 5 | same as #240 |
| 243 | L537 | Check | - | UI | - | Label. |
| 244 | L539 | VS Code: is ChatMCP ( chat.mcp.access) limited to the registry, with ChatAllowedMcpServers or a private registry ( McpGalleryServiceUrl)? | vsc-pol, vsc-src | OK | - | ChatMCP (chat.mcp.access), ChatAllowedMcpServers and McpGalleryServiceUrl are VS Code policies. |
| 245 | L539 | Microsoft's docs and source code disagree on its values [contested], so confirm with Policy Diagnostics. | vsc-pol, vsc-src | OK | 5 | Docs list registryOnly and off; source code has none, registry, all. Tagged [contested]. |
| 246 | L539 | It does not cover MCP servers the Copilot runtime finds on its own. | vsc-sec | OK | 3 | "ChatMCP doesn't apply to MCP servers that the Copilot runtime discovers on its own." |
| 247 | L540 | Claude Code: allowedMcpServers with allowManagedMcpServersOnly, and strictKnownMarketplaces for plugins. | cc-mmcp, cc-setref | OK | - | allowedMcpServers, allowManagedMcpServersOnly and strictKnownMarketplaces are Claude managed settings. |
| 248 | L540 | A list with only URL entries blocks local stdio servers, so list the ones you allow too. | cc-mmcp | OK | 3 | A stdio server is allowed only by a serverCommand entry (or a serverName entry when no serverCommand exists). Only URL entries leaves it blocked. |
| 249 | L541 | Codex: an [mcp\_servers.&lt;name&gt;] allowlist in requirements.toml, matched on identity.command (stdio) or identity.url (remote); use the structured command form to pin arguments. | cx-mc | OK | 5 | Codex: identity.command for stdio, identity.url for remote; structured form must match executable, count and order of arguments. |
| 250 | L541 | An empty mcp\_servers table disables all servers. | cx-mc | OK | 3 | "If mcp\_servers is present but empty, the local client disables all MCP servers." |
| 251 | L541 | Plugin-bundled servers need plugins.&lt;plugin&gt;.mcp\_servers.&lt;server&gt; entries. | cx-mc | OK | 3 | "Plugin-bundled MCP servers use the same identity shapes under plugins.&lt;plugin&gt;.mcp\_servers.&lt;server&gt;." |
| 252 | L541 | For plugin sources, set [marketplaces] restrict\_to\_allowed\_sources = true with marketplaces.allowed\_sources; bundled and remotely installed workspace plugins have separate controls. | cx-mc | OK | 5 | Codex: restrict\_to\_allowed\_sources = true under [marketplaces] limits local and Git sources; bundled and workspace plugins are controlled separately. |
| 253 | L542 | Which remote MCP servers are in use, who runs them, and what data and tokens do they receive? | - | JUDGEMENT | - | Check question and supplier advice. Tagged. |
| 254 | L542 | Treat each as a supplier. | - | JUDGEMENT | - | same as #253 |
| 255 | L542 | [inference] | - | JUDGEMENT | - | same as #253 |
| 256 | L543 | Do MCP servers use short-lived, narrowly scoped tokens? | - | QUESTION | - | Check questions. |
| 257 | L544 | Do MCP servers you or a supplier run refuse tokens not issued for them? | - | QUESTION | 5 | same as #256 |
| 258 | L544 | The MCP security guidance forbids token passthrough: forwarding a client's token unchanged to a downstream API. | mcp-bp | OK | 5 | Best practices: token passthrough is an anti-pattern and forbidden. |
| 259 | L544 | A proxy server with a static client ID for a third-party OAuth service should get consent per client. | mcp-bp | OK | 5 | Best practices: proxy servers with a static client ID must get per-client consent (confused deputy). |
| 260 | L544 | Source: the draft specification [may be outdated]. | mcp-bp | OK | 3 | The page is the draft spec, as the tag says. |
| 261 | L545 | Do local MCP servers that use HTTP check the Origin header, bind to localhost and require authentication? | - | QUESTION | 3 | Check question. |
| 262 | L545 | The MCP specification (2025-06-18) says servers must validate Origin and should bind to localhost and authenticate, to stop DNS rebinding [may be outdated]. | mcp-tr | OK | 3 | 2025-06-18 transports: servers MUST validate Origin, SHOULD bind to localhost, SHOULD authenticate; DNS rebinding is the named risk. |
| 263 | L546 | Are automatic plugin updates set on purpose for each marketplace? | - | QUESTION | - | Check question. |
| 264 | L546 | Claude Code's defaults differ by marketplace type, so decide whether a new plugin version may install without review. | cc-plug | OK | - | Claude plugin docs: auto-update depends on the marketplace and its type. |
| 265 | L547 | Are agents patched for Plugin4Shell (Claude Code 2.1.179, Codex 0.146.0 or later)? | csa-p4s | OK | - | Same versions as row 75. |
| 266 | L549 | Typical findings MCP servers started from any source, broad personal tokens in MCP config, plugins from personal GitHub repos. | - | JUDGEMENT | - | Typical findings. |
| 267 | L550 | Supply chain Poisoned content Stolen tokens | - | UI | - | Tags. |

### D07

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 268 | L555 | D07 No sandbox and open network OWASP ASI05 · makes exfiltration in ASI01 and ASI03 possible | owasp-asi | JUDGEMENT | - | ASI codes valid. The exfiltration link is the author's mapping. |
| 269 | L556 | Claude Code's sandbox is off by default and does not run on native Windows. | cc-sbx | OK | 5 | "The sandbox is off by default." Not on native Windows. |
| 270 | L556 | It covers shell commands only; hooks, local MCP servers and apiKeyHelper run outside it, and the Read, Edit and WebFetch tools follow permission rules instead. | cc-sbx | OK | 5 | Claude's page lists hooks, local MCP servers and apiKeyHelper outside the sandbox; Read, Edit, WebFetch follow permission rules. |
| 271 | L557 | Codex sandboxes commands by default (network off, writes limited to the workspace) but by default leaves reads open. | cx-appr, cx-sbx, search-cx | FIXED | 5 | Added "by default". Codex docs: network off, writes limited to the workspace; no read limit stated, and deny\_read exists in requirements.toml. |
| 272 | L557 | VS Code's agent sandbox leaves network on by default, is experimental on Windows, and is not a virtual machine or user-account boundary. | vsc-sbx | OK | 4 | VS Code: network on unless restricted; Windows support experimental; "not a virtual machine or user-account boundary". |
| 273 | L557 | A dev container gets Git credentials and the SSH agent by default. | dc-cred | OK | 5 | Dev Containers docs: Git credentials reused and SSH agent forwarded automatically. |
| 274 | L558 | Check | - | UI | - | Label. |
| 275 | L560 | Is sandboxing required centrally? | - | QUESTION | - | Check question. |
| 276 | L560 | VS Code: ChatAgentSandboxEnabled is deprecated; Microsoft points to the Copilot managed setting sandbox.enabled and calls managed enforcement a preview. | vsc-pol, vsc-sbx, gh-cms | OK | 5 | ChatAgentSandboxEnabled is marked Deprecated; managed sandbox.enabled is in preview. |
| 277 | L560 | Claude Code: sandbox.enabled, failIfUnavailable (refuse to start where the sandbox cannot run, such as native Windows) and allowUnsandboxedCommands: false. | cc-sbx | OK | 5 | failIfUnavailable makes Claude exit at startup when the sandbox cannot start; allowUnsandboxedCommands false stops the unsandboxed retry. |
| 278 | L561 | What is the effective policy? | - | QUESTION | 3 | Check question. |
| 279 | L561 | When the sandbox is admin-required, Claude Code ignores loosening settings from a repository but still honours user settings and --settings, which can add excludedCommands, write paths and socket access [inference]. | cc-sbx | OK | 5 | Claude: when admin-required, loosening settings come only from managed settings, --settings and ~/.claude/settings.json; repo files are ignored. Tagged [inference] for the risk. |
| 280 | L561 | Lock with allowManagedReadPathsOnly and allowManagedDomainsOnly, and pin enableWeakerNestedSandbox, enableWeakerNetworkIsolation, network.allowAllUnixSockets and network.allowLocalBinding to false [inference]. | cc-setref | JUDGEMENT | 5 | All six keys exist in the settings reference. The advice is tagged [inference]. |
| 281 | L562 | Codex: is danger-full-access blocked in requirements.toml ? | - | QUESTION | - | Check question. |
| 282 | L562 | From Codex 0.138.0 use allowed\_permission\_profiles with a managed default\_permissions; older deployments use allowed\_sandbox\_modes = ["read-only", "workspace-write"]. | cx-mc | OK | - | "Permission-profile allowlists require Codex 0.138.0 or later." allowed\_sandbox\_modes is for legacy sandbox\_mode deployments. |
| 283 | L562 | Settings in config.toml and managed\_config.toml are defaults users can change, not requirements. | cx-mc | OK | - | config.toml settings "users can override"; managed\_config.toml likewise. |
| 284 | L563 | Is outbound access allowlisted? | - | QUESTION | 9 | Check question. Pass 9: "limited to an allowlist" became "allowlisted". |
| 285 | L563 | Claude Code: sandbox.network.allowedDomains with allowManagedDomainsOnly covers shell commands; WebFetch(domain:...) allow rules only pre-approve fetches and are not an allowlist. | cc-sbx, cc-perm | OK | 5 | allowedDomains limits sandboxed commands. A WebFetch allow rule means "fetches without prompting"; other domains still prompt. |
| 286 | L563 | VS Code: sandbox.userPolicy.network.allowOutbound for commands, ChatAgentNetworkFilter for the fetch tool and integrated browser. | gh-cms, vsc-pol | OK | 5 | sandbox.userPolicy.network.allowOutbound for commands; ChatAgentNetworkFilter covers "agent tools (fetch tool, integrated browser)". |
| 287 | L563 | Codex: [experimental\_network] ([network\_proxy] from 0.166.0) in requirements.toml for commands, with enabled = true; limited Windows support. | cx-mc | OK | 5 | "Set experimental\_network.enabled = true to activate the managed proxy"; Windows support "still limited". Rechecked 10 Nov 2026: "In Codex 0.166.0, [network\_proxy] is the canonical table"; "Codex also accepts the older [experimental\_network] name"; OpenAI says to keep the older name until every client supports the new one. |
| 288 | L563 | Web search, MCP and apps have separate controls. | cx-mc | OK | 3 | Web search, MCP and apps have their own requirements keys. |
| 289 | L564 | Is an allowed domain still a way out? | - | QUESTION | - | Check question. |
| 290 | L564 | An allowed service such as github.com can receive data into an attacker's account. | - | JUDGEMENT | 3 | Known exfiltration pattern; no single source needed. |
| 291 | L564 | Anthropic warns that broad domains create exfiltration paths and that hostname-only filtering without TLS inspection can be bypassed, for example by domain fronting. | cc-sbx | OK | 3 | Claude: broad domains "can create paths for data exfiltration"; without TLS inspection code may "use domain fronting". |
| 292 | L564 | Keep the list short, and restrict by account, tenant or operation where the service allows it. | - | JUDGEMENT | 3 | Advice. |
| 293 | L565 | Which local services can a command reach? | - | QUESTION | - | Check question. |
| 294 | L565 | Docker and other Unix sockets and unauthenticated localhost services can give a command more power than file and domain rules suggest; Anthropic names these sockets as ways around its sandbox. | cc-sbx | CUT | 9 | Claude: allowing /var/run/docker.sock "effectively grants access to the host system". Pass 9: "names the Docker socket and Unix sockets" became "names these sockets", which points back to Docker and other Unix sockets. |
| 295 | L565 | Keep the Docker socket out of agent sessions, leave sandbox.network.allowAllUnixSockets and allowLocalBinding (macOS) off, and require authentication on local services. | cc-setref | JUDGEMENT | 3 | Settings exist; the advice is the author's. |
| 296 | L566 | On Windows: is there a plan for WSL2 or dev containers? | - | QUESTION | - | Check question. |
| 297 | L566 | VS Code's Windows sandbox needs Windows 11 25H2 build 26200.9550 or 26H1 build 28000.3086 or later. | vsc-sbx | OK | - | VS Code: 25H2 build 26200.9550, 26H1 build 28000.3086 or later. |
| 298 | L567 | Is high-risk work, such as unknown repos and autonomous runs, done in a dev container or cloud session with credential forwarding turned off where it is not needed? | - | QUESTION | - | Check question. |
| 299 | L569 | Typical findings Sandbox off, network open, a Windows fleet assumed to be sandboxed, autonomous runs on the main laptop. | - | JUDGEMENT | - | Typical findings. |
| 300 | L570 | Poisoned content Supply chain Stolen tokens | - | UI | - | Tags. |

### D08

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 301 | L575 | D08 Approval bypass OWASP ASI02 Tool Misuse · ASI09 Human-Agent Trust Exploitation | owasp-asi | OK | - | ASI02 "Tool Misuse and Exploitation", ASI09 "Human-Agent Trust Exploitation". |
| 302 | L576 | Approval prompts fail when they are switched off (Allow all, Autopilot, bypass modes, or a project file), or when the prompt shows something other than what happens. | vsc-appr, vsc-sec, cc-pmodes | OK | 5 | Allow all, Autopilot and bypass modes skip prompts by design; rows 303 and 304 show the second case. |
| 303 | L576 | CVE-2025-53773 let a prompt injection make Copilot write "chat.tools.autoApprove": true into workspace settings. | cve, embrace | OK | 3 | NVD CVE-2025-53773 (Copilot and VS Code). Embrace the Red: the injection writes "chat.tools.autoApprove": true to .vscode/settings.json. |
| 304 | L577 | GhostApproval (Wiz, July 2026) used repo symlinks to make six agents write outside the project, such as to ~/.ssh/authorized\_keys; in some, the prompt named a harmless file or came after the write. | csa-ghost | FIXED | 3 | Was "several of the six". Wiz (8 Jul 2026, via CSA note): symlinks, writes outside the project such as ~/.ssh/authorized\_keys; some prompts showed a harmless file, some came after the write. |
| 305 | L577 | Anthropic disputed that it is a vulnerability. | csa-ghost | OK | - | CSA: Anthropic "disputed that the behavior was a vulnerability", calling it "outside our threat model". |
| 306 | L578 | Check | - | UI | - | Label. |
| 307 | L580 | Is the VS Code policy ChatToolsAutoApprove set to block global auto-approve? | vsc-pol | QUESTION | - | ChatToolsAutoApprove maps to chat.tools.global.autoApprove. |
| 308 | L580 | It also takes Assisted permissions, Allow all and Autopilot out of use. | vsc-sec | OK | - | VS Code: admins can block "Assisted permissions and Allow all permission levels, and the Autopilot agent mode, with the ChatToolsAutoApprove policy". |
| 309 | L581 | Do high-risk tools always ask? | - | QUESTION | - | Check question. |
| 310 | L581 | ChatToolsEligibleForAutoApproval can require approval for named tools, but it does not stop Assisted permissions or approvals saved earlier in a Copilot harness session. | vsc-sec | OK | 3 | ChatToolsEligibleForAutoApproval requires approval for named tools; VS Code says Copilot harness sessions don't fully enforce some of these policies. |
| 311 | L582 | Claude Code: are permissions.disableBypassPermissionsMode and, where needed, permissions.disableAutoMode set to "disable" in managed settings? | cc-setref, cc-pmodes | QUESTION | - | Both keys exist and take "disable". |
| 312 | L582 | Anthropic's settings reference also accepts disableAutoMode at top level. | cc-pmodes | OK | 3 | Permission modes page: "Any settings file sets disableAutoMode to \\"disable\\"" (top level) as well as permissions.disableAutoMode. An earlier "fix" here was wrong and was rolled back. |
| 313 | L582 | Check enforcement on the deployed version. | - | JUDGEMENT | 3 | Advice. |
| 314 | L583 | Codex: does requirements.toml set allowed\_approval\_policies = ["on-request"], so --ask-for-approval never is refused? | cx-mc | QUESTION | - | allowed\_approval\_policies exists in requirements.toml. |
| 315 | L583 | Combine it with the sandbox limit under D07 to block --yolo. | - | JUDGEMENT | - | Cross-reference to D07. |
| 316 | L583 | Optional command rules in [rules] can force a prompt or forbid matching commands. | cx-mc | OK | - | Codex [rules] prefix rules with prompt or forbidden decisions. |
| 317 | L584 | Codex: on-request does not mean a person decides: with approvals\_reviewer = "auto\_review" an automatic reviewer can answer. | cx-ar | OK | 3 | Codex auto-review: approvals\_reviewer = "auto\_review" lets a reviewer agent answer on-request prompts. |
| 318 | L584 | To require a human, set allowed\_approvals\_reviewers = ["user"] in requirements.toml. | cx-mc | OK | 3 | allowed\_approvals\_reviewers in requirements.toml. |
| 319 | L584 | This sets who reviews requests, not which actions need approval. | cx-ar | OK | 3 | Auto-review changes who answers, not when a prompt is raised. |
| 320 | L584 | [not run here] | - | UI | - | Tag. |
| 321 | L585 | Copilot: do managed permissions.ask rules cover the actions that must never be approved silently? | - | QUESTION | - | Check question. |
| 322 | L585 | GitHub says a managed ask rule always needs a fresh approval, which bypass modes, auto-approval, hooks and saved grants cannot satisfy. | gh-cms | OK | - | GitHub: a managed ask rule needs a fresh approval that bypass modes, auto-approval, hooks and saved grants cannot satisfy. |
| 323 | L585 | It applies to Agent Host sessions only. | gh-cms | OK | - | "apply to Copilot sessions that use Agent Host". |
| 324 | L586 | Are approvals granted for the session rather than for the workspace or user? | - | QUESTION | - | Check question. |
| 325 | L588 | Typical findings Allow all used daily to save time, bypass flags in shell aliases, no central policy. | - | JUDGEMENT | - | Typical findings. |
| 326 | L589 | Poisoned content Booby-trapped project | - | UI | - | Tags. |

### D09

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 327 | L594 | D09 No inventory, version floor or agent telemetry OWASP MCP08 Lack of Audit and Telemetry · ASI10 Rogue Agents (secondary, detection side) | owasp-mcp, owasp-asi | OK | - | MCP08 "Lack of Audit and Telemetry"; ASI10 "Rogue Agents". "Secondary" is the author's mapping. |
| 328 | L595 | You cannot act on the next GitSpawn without knowing which agents and versions run where. | - | JUDGEMENT | - | Framing. |
| 329 | L595 | A Defender process event records the command lines of the new process and its parent, but only the grandparent's name and ID. | mde | OK | 5 | DeviceProcessEvents has ProcessCommandLine and InitiatingProcessCommandLine, but only InitiatingProcessParentFileName and InitiatingProcessParentId for the grandparent. |
| 330 | L595 | It does not record the task, prompt, approval or agent session. | mde | OK | 4 | No task, prompt, approval or session column in the schema. |
| 331 | L596 | Forever Security caught the planted AGENTS.md by watching the agent, not only the user. | helpnet | OK | 4 | Help Net: Forever caught it by monitoring the agent's behaviour. |
| 332 | L596 | VS Code ignores a policy value with a syntax error, so policies can fail quietly. | vsc-pol | OK | 5 | VS Code policies page: a policy value with a syntax error is ignored. |
| 333 | L597 | Check | - | UI | - | Label. |
| 334 | L599 | Is there an inventory of agents, versions, extensions and MCP servers per machine, for example from Defender for Endpoint and Intune? | - | QUESTION | - | Check questions. |
| 335 | L600 | Is a minimum version enforced? | - | QUESTION | - | same as #334 |
| 336 | L600 | Claude Code: requiredMinimumVersion, set to a current build rather than the first fixed one. | cc-setref | OK | - | requiredMinimumVersion exists in managed settings. "Current build" is advice. |
| 337 | L600 | Codex permission-profile requirements need 0.138.0 or later, so set the version floor before relying on them. | cx-mc | OK | - | "Permission-profile allowlists require Codex 0.138.0 or later." |
| 338 | L601 | Is managed-settings JSON validated before rollout? | - | QUESTION | - | Check question. |
| 339 | L601 | A Claude Code managed settings file, plist or HKLM value that is not valid JSON stops Claude Code from starting, and a developer with local admin rights can edit the managed policy itself. | cc-mset | FIXED | 1 | Was "a file-based policy". Claude docs: invalid managed JSON stops startup; plist and HKLM forms are also editable by a local admin. |
| 340 | L602 | Can you see which commands agents started? | - | QUESTION | - | Check question. |
| 341 | L602 | A first Defender advanced hunting query [not run here]. | - | UI | 3 | Tag [not run here]. |
| 342 | L602 | It matches only events where the initiating process or its parent looks like an agent, so deeper processes and renamed agents are missed. | mde | OK | 3 | Read from the query itself: it filters on the initiating process and its parent only. |
| 343 | L602 | Join on process IDs and creation times to rebuild the chain: | mde | OK | 3 | InitiatingProcessId and InitiatingProcessCreationTime columns exist for the join. |
| 344 | L603 | [command] DeviceProcessEvents | mde | OK | - | Every column name exists in the DeviceProcessEvents schema. Query not run here, as tagged. |
| 345 | L604 | \| where InitiatingProcessCommandLine has\_any ("claude", "codex", "copilot") | mde | OK | - | same as #344 |
| 346 | L605 | or InitiatingProcessParentFileName has\_any ("claude", "codex", "copilot") | mde | OK | - | same as #344 |
| 347 | L606 | \| project Timestamp, DeviceName, InitiatingProcessParentFileName, | mde | OK | - | same as #344 |
| 348 | L607 | InitiatingProcessParentId, InitiatingProcessId, | mde | OK | - | same as #344 |
| 349 | L608 | InitiatingProcessFileName, InitiatingProcessCommandLine, FileName, ProcessCommandLine Copy | mde | OK | - | same as #344 |
| 350 | L609 | Does agent telemetry reach the SIEM? | - | QUESTION | - | Check question. |
| 351 | L609 | VS Code: CopilotOtelEnabled and CopilotOtelEndpoint. | vsc-pol | OK | - | CopilotOtelEnabled, CopilotOtelEndpoint, CopilotOtelCaptureContent are listed policies. |
| 352 | L609 | Decide whether to capture prompt content ( CopilotOtelCaptureContent). | vsc-pol | OK | - | same as #351 |
| 353 | L609 | VS Code says hooks are not a complete audit trail. | vsc-sec | OK | - | "Verify event coverage and failure behavior before treating the log as a complete audit trail." |
| 354 | L610 | Are policies actually applied? | - | QUESTION | - | Check question. |
| 355 | L610 | In VS Code run Developer: Policy Diagnostics; in Claude Code run /status and look for Enterprise managed settings on the Setting sources line. | vsc-pol, cc-settings | OK | - | VS Code: "Developer: Policy Diagnostics". Claude: run /status, "the Setting sources line names the managed source". |
| 356 | L611 | Does each policy reach every harness? | - | QUESTION | - | Check question. |
| 357 | L611 | Some do not: ChatMCP misses MCP servers the Copilot runtime finds itself, and ChatToolsEligibleForAutoApproval does not stop Assisted permissions or saved approvals. | vsc-sec | OK | - | Same two gaps as rows 246 and 310. |
| 358 | L611 | Test each one with a real session. | - | JUDGEMENT | - | Advice. |
| 359 | L613 | Typical findings No agent inventory, updates left to each user, telemetry off, hooks treated as a full audit log. | - | JUDGEMENT | - | Typical findings. |
| 360 | L614 | Poisoned content Booby-trapped project Supply chain Stolen tokens | - | UI | - | Tags. |

### D10

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 361 | L619 | D10 Code and context sent to unapproved AI services Data governance, not an OWASP attack class | - | JUDGEMENT | - | Heading; "not an OWASP attack class" is the author's framing. |
| 362 | L620 | Model requests can include code, files the agent read, terminal output, tool results and sometimes secrets. | vsc-sec | CUT | 9 | Context sent to the model includes files, terminal output and tool results. Pass 9: "Requests to the model can include selected code" became "Model requests can include code". |
| 363 | L620 | The risk is where they go: a personal account, a provider without a company agreement, or an own-key model, where VS Code says content filtering is not guaranteed. | vsc-sec | OK | 3 | VS Code: with bring-your-own-key models "there is no guarantee that responsible AI filtering is applied". |
| 364 | L620 | In July 2026 Grok Build CLI was found uploading whole Git repositories to xAI's storage. | grok | FIXED | 9 | Was unnamed. Hacker News, July 2026: Grok Build CLI uploaded whole Git repos to xAI storage. Pass 9: "a researcher found" became "was found"; the researcher is named in Sources. |
| 365 | L621 | Check | - | UI | - | Label. |
| 366 | L623 | Is ChatApprovedAccountOrganizations set to your approved GitHub organisations? | vsc-pol | QUESTION | 3 | ChatApprovedAccountOrganizations exists. |
| 367 | L623 | It checks the signed-in account's organisation membership, so a personal account that is a member can qualify; it does not require a company-managed identity. \* accepts any signed-in GitHub or GHE account, so do not use it to restrict membership. | vsc-pol | OK | 3 | The policy checks organisation membership of the signed-in account; \* accepts any signed-in account. |
| 368 | L624 | Claude Code: forceLoginMethod and forceLoginOrgUUID in managed settings. | cc-setref | OK | - | forceLoginMethod and forceLoginOrgUUID are managed settings. |
| 369 | L625 | Which agents and providers are approved, and is the list enforced on the machine, not only written in a policy? | - | QUESTION | - | Check question. |
| 370 | L625 | In VS Code the Claude and Codex harnesses are turned off when Copilot enterprise-managed settings apply. | vsc-appr | OK | - | "Claude and Codex harnesses are disabled when Copilot enterprise-managed settings apply." |
| 371 | L626 | Does session sync to GitHub ( CopilotSessionSync) fit your data rules? | vsc-pol | OK | - | CopilotSessionSync is a listed policy. |
| 372 | L627 | Does the agreement with each approved provider settle retention, use for training, data residency, subprocessors and deletion? | - | QUESTION | - | Check question. |
| 373 | L627 | Pinning the account is not enough without these terms. | - | JUDGEMENT | - | Tagged [inference]. |
| 374 | L627 | [inference] | - | JUDGEMENT | - | same as #373 |
| 375 | L629 | Typical findings Personal subscriptions on work laptops, no list of approved providers, own-key models in use. | - | JUDGEMENT | - | Typical findings. |
| 376 | L630 | Governance | - | UI | - | Tag. |

### If something got in

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 377 | L636 | If something got in | - | UI | - | Heading. |
| 378 | L637 | Removing a planted instruction file or updating the agent does not undo what already ran. | - | JUDGEMENT | - | General incident-response point. |
| 379 | L637 | In Forever Security's case Codex first changed its own settings, which then applied to every later Codex session in any project. | helpnet | FIXED | 2 | Was a config.toml detail Help Net does not name. Help Net: Codex "first changed its own settings", then every later session in any project ran the attacker's command. |
| 380 | L637 | The order below is interpretation by AI. | - | JUDGEMENT | - | Order is the author's; tagged [inference]. |
| 381 | L637 | [inference] | - | JUDGEMENT | - | same as #380 |
| 382 | L639 | Isolate the device through your endpoint tool before cleaning it, so stolen sessions and any open tunnel stop working from that machine. | ms-ir | JUDGEMENT | - | Isolate first, keep powered on. Consistent with Microsoft IR guidance; order is judgement. |
| 383 | L639 | Keep it powered on and do not wipe it yet. | ms-ir | JUDGEMENT | - | same as #382 |
| 384 | L640 | Preserve evidence before any cleanup or rebuild. | ms-ir | OK | - | Microsoft: preserve evidence before remediation. |
| 385 | L640 | Microsoft's incident-response guidance says not to destroy forensic evidence. | ms-ir | OK | 3 | Microsoft IR guidance: do not destroy forensic evidence. |
| 386 | L640 | Copy to storage the user cannot change: agent transcripts (they age out; see Claude Code's cleanupPeriodDays), agent and MCP config, shell history, planted files, package artifacts, and endpoint, code host, cloud and identity logs. | cc-setref | CUT | 9 | cleanupPeriodDays ages out transcripts. The item list is tagged [inference]. Pass 9: cut "and session logs", "as found" and "for the window". |
| 387 | L640 | [inference] | - | JUDGEMENT | - | Tagged [inference]. Pass 9: the tag now sits right after the list of items it covers (was "[inference] for the list of items"). |
| 388 | L640 | Collect quickly, so revoking access is not delayed. | - | JUDGEMENT | 3, 9 | Tagged [inference]. |
| 389 | L641 | Revoke tokens and sessions, not only passwords: GitHub, npm, cloud, SSH keys, MCP OAuth tokens and the agents' own sign-in tokens. | - | JUDGEMENT | - | Token list is advice. |
| 390 | L641 | Forever Security advises assuming the agent login token leaked, since a stolen token works as a live session. | helpnet | OK | - | Forever advises treating the agent token as leaked. |
| 391 | L642 | Look for persistence outside the repo: user-level agent config such as ~/.codex/config.toml, ~/.claude/settings.json and MCP addresses in ~/.claude.json, VS Code user settings, user tasks and extensions, global Git config and hooks, shell startup files, and services or scheduled jobs, including a code tunnel service. | helpnet, mitiga, vsc-tun | JUDGEMENT | - | Paths are real config locations; the list is the author's. |
| 392 | L643 | Follow the identity downstream: pushes, pull requests, workflow runs, package publishes, and cloud and SaaS sign-ins or changes made with the developer's credentials during the window. | - | JUDGEMENT | - | Advice. |
| 393 | L644 | Recover from a known-good state once the evidence is preserved and the scope is clear: rebuild or restore the machine, reissue credentials after the rebuild, and check repos and packages the identity could change. | - | JUDGEMENT | - | same as #392 |

### How the analysis was checked

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 394 | L652 | How the analysis was checked | - | UI | - | Heading. |
| 395 | L653 | The earlier drafts were checked in persona-based review passes. | - | RECORD | 9 | Describes the earlier review passes. Pass 9: cut "each taking a different role". |
| 396 | L653 | Their notes and test records are not attached to this page, so treat them as structured self-checks rather than independent reviews. | - | RECORD | - | Describes the earlier review passes. |
| 397 | L653 | Their findings and the changes they caused are listed below. | - | RECORD | - | same as #396 |
| 398 | L653 | The Git behaviour they flagged was re-run on 29 October and 1 November 2026; see Evidence status. | git-test | OK | 1 | Git tests re-run on 29 Oct (2.43.0) and 1 Nov 2026 (2.54.0). |

### Merge check, 29 October 2026

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 399 | L657 | Merge check, 29 October 2026 | - | RECORD | - | Merge check of 29 Oct 2026. A record of what was done; checked for agreement with the current page (D11 to D17 exist, seven further risks). |
| 400 | L658 | The separate More risks tab was merged into the Risk map. | - | RECORD | - | same as #399 |
| 401 | L658 | Three more persona-based passes checked the merge before it was published. | - | RECORD | - | same as #399 |
| 402 | L658 | Afterwards the further risks were renamed from E01 to E07 to D11 to D17 and given their own markers in the diagram. | - | RECORD | - | same as #399 |
| 403 | L660 | Content-integrity auditor Did anything get lost or changed by accident? | - | RECORD | - | same as #399 |
| 404 | L662 | Compared old and new versions field by field. | - | RECORD | - | same as #399 |
| 405 | L662 | Every further risk kept its ID, title, description, relevance and control, and the top 10, sources and review data were unchanged. | - | RECORD | - | same as #399 |
| 406 | L663 | Found that old links to the More risks section no longer reached it. | - | RECORD | - | same as #399 |
| 407 | L663 | Fixed. | - | RECORD | - | same as #399 |
| 408 | L665 | Security architect Are the further risks placed and scoped correctly? | - | RECORD | - | same as #399 |
| 409 | L667 | Policy gaps between agent harnesses repeated points already in the top 10, so it was folded into D09 as a check. | - | RECORD | - | same as #399 |
| 410 | L667 | There are now seven further risks instead of eight. | - | RECORD | - | same as #399 |
| 411 | L668 | Widened where several risks sit in the map, and rewrote VS Code tunnels and remote sessions as inbound remote access, with Microsoft's Dev Tunnels policies and Claude Code's remote-control switch as controls. | - | RECORD | - | same as #399 |
| 412 | L669 | Noted that VS Code tunnels have real-world use while D09 and D10 do not. | - | RECORD | - | same as #399 |
| 413 | L669 | The top 10 now says so. | - | RECORD | - | same as #399 |
| 414 | L671 | QA and accessibility engineer Does the merged map work by mouse, keyboard and screen reader? | - | RECORD | - | same as #399 |
| 415 | L673 | Confirmed every chip, table button and popover link outlines the right boxes, with no script errors and no sideways page scroll in light or dark at phone and desktop width. | - | RECORD | - | same as #399 |
| 416 | L674 | Fixed: keyboard focus hidden on outlined boxes, focus lost after popover links, a table wider than its column, an over-tall popover, and table rows that read the full description as a header. | - | RECORD | - | same as #399 |

### Review round, 29 October 2026

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 417 | L680 | Review round, 29 October 2026 | - | UI | - | Heading. |
| 418 | L681 | Five reviewer lenses raised 22 findings. | - | RECORD | - | Counts of a past review. The notes are not attached (row 396), so the count is not checkable. |
| 419 | L681 | Each was checked against the source named below before the page changed; all were taken over, some in narrower form. | - | RECORD | - | same as #418 |
| 420 | L683 | Security architect Is the map drawn correctly? | - | UI | - | Lens label. |
| 421 | L685 | Rewrote the opening line: the same user account does not mean the same effective access once sandboxes and tool permissions apply. | - | RECORD | - | Matches the current header and D07 rows 269 to 273. |
| 422 | L686 | D07 now describes defaults per product. | - | RECORD | - | same as #421 |
| 423 | L686 | Codex sandboxes commands with network off by default (OpenAI docs). | cx-sbx | OK | - | Codex sandbox: network off by default. |
| 424 | L687 | Added direct network paths from the terminal and from extensions, a two-way tunnel path, and a box for remote MCP servers. | - | RECORD | - | Matches ARROWS and COMP (tunnel, remote MCP, conceptual egress label). |
| 425 | L687 | The egress point is now labelled as a conceptual boundary. | - | RECORD | - | same as #424 |
| 426 | L689 | Offensive security researcher Are attack prerequisites stated correctly? | - | UI | - | Lens label. |
| 427 | L691 | D02 separates clones from repos received as files. | - | RECORD | - | Matches D02. |
| 428 | L691 | Manifold's write-up says a clone does nothing; re-run here, a clone carried no config or hooks but did carry tracked.vscode/. | manifold, git-test | OK | - | Manifold: clone alone does nothing. Re-run: clone carried tracked .vscode/ but no config or hooks. |
| 429 | L692 | GitSpawn is described as unsafe background Git calls, not seven fsmonitor runs: ultrareview used another key and Codex differed in mechanism (Manifold). | manifold | OK | - | Manifold: Claude ultrareview used another key; Codex differed in mechanism. |
| 430 | L693 | Added task.allowAutomaticTasks (VS Code tasks docs) and the Plugin4Shell prerequisites (CSA research note). | vsc-tasks, csa-p4s | OK | - | task.allowAutomaticTasks exists; Plugin4Shell prerequisites from CSA. |
| 431 | L695 | Developer-platform engineer Do the controls do what the page says? | - | UI | - | Lens label. |
| 432 | L697 | D04 separates read restriction from edit approval. chat.tools.edits.autoApprove only gates edits (VS Code security docs). | vsc-appr | OK | - | Same as row 203. |
| 433 | L698 | Claude Code sandbox limits do not cover the Read or WebFetch tools (Anthropic sandboxing docs). | cc-sbx | OK | - | Same as row 270. |
| 434 | L698 | Checks added to D04 and D07. | - | RECORD | - | Matches D04, D06 to D09 (requirements.toml checks present). |
| 435 | L699 | Resolved the VSIX question, made CODEOWNERS enforcement explicit, qualified the worktree advice, and added Codex requirements.toml controls to D04, D06, D07, D08 and D09. | - | RECORD | - | same as #434 |
| 436 | L701 | Incident responder and data governance Can a team detect, respond and govern? | - | UI | - | Lens label. |
| 437 | L703 | D09 credits Defender with process command lines and names what it lacks (DeviceProcessEvents schema). | mde | OK | - | Same as row 329. |
| 438 | L703 | The audit round below narrowed this: the schema has the initiating process's command line but not its parent's. | mde | OK | - | same as #437 |
| 439 | L704 | D10 no longer says every prompt carries code, and asks for retention, training, residency, subprocessor and deletion terms. | - | RECORD | - | Matches D10 rows 362 and 372, the response section and D16. |
| 440 | L705 | Added an incident-response section and widened D16 to signed-in browser sessions. | - | RECORD | - | same as #439 |
| 441 | L707 | Assurance and QA Are claims and the page itself sound? | - | UI | - | Lens label. |
| 442 | L709 | The ranking is now a proposed priority order, and review claims without records were reworded. | - | RECORD | - | Page behaviour; the render check covers focus and tallies. |
| 443 | L710 | Fixed the tally, which counted Unknown as Not assessed. | - | RECORD | - | same as #442 |
| 444 | L710 | Unknown now has its own count. | - | RECORD | - | same as #442 |
| 445 | L711 | Opening a checklist from the map now moves keyboard focus to the card, and the page declares its language. | - | RECORD | - | same as #442 |

### Audit round, 29 October 2026

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 446 | L717 | Audit round, 29 October 2026 | - | UI | - | Heading. |
| 447 | L718 | An outside audit raised findings on controls, the diagram, the response sequence and some wording. | - | RECORD | - | Describes a past audit. |
| 448 | L718 | Each was checked against the primary source before the page changed. | - | RECORD | - | same as #447 |
| 449 | L718 | All held; some were adopted in narrower form, as noted. | - | RECORD | - | same as #447 |
| 450 | L718 | Where a source could not settle a point, the page says so. | - | RECORD | - | same as #447 |
| 451 | L720 | Controls and checks D01, D04, D06, D07, D08, D11 | - | UI | - | Group label. |
| 452 | L722 | D01: a managed npmrc is a default, not enforcement. npm applies command line, environment, project, user, then global (npm docs). | npm12-cfg | OK | - | npm config docs: command line, environment, project, user, global, built-in. |
| 453 | L722 | Added a route for urgent fixes, since a cooldown can block npm audit fix. | - | RECORD | - | Matches D01. |
| 454 | L723 | D04 and D08: added GitHub's managed permissions.deny with Read(...), its Agent Host limit, sandbox.userPolicy.filesystem.deniedPaths, and managed permissions.ask. | gh-cms | OK | - | Same keys as rows 204 and 322. |
| 455 | L724 | D06 and D07: added local services and sockets, local HTTP MCP checks (Origin, localhost, authentication) and the allowed-domain exfiltration route, with Anthropic's own warning on hostname filtering. | mcp-tr, cc-sbx | OK | - | Same as rows 262 and 291. |
| 456 | L725 | D08: in Codex, on-request can still be answered by automatic review. | cx-ar | OK | - | Same as row 317. |
| 457 | L725 | Added allowed\_approvals\_reviewers with ["user"], which OpenAI documents for manual approval (confirmed 30 October). | cx-mc | OK | 6 | Same as row 318. |
| 458 | L726 | D11: branch protection does not cover CI that runs before merge. | gh-secure | JUDGEMENT | - | Pre-merge point is tagged [inference], as row 547. |
| 459 | L726 | Added a CI boundary (GitHub secure use reference). | gh-secure | JUDGEMENT | - | same as #458 |
| 460 | L726 | The pre-merge trigger point is marked as inference. | gh-secure | JUDGEMENT | - | same as #458 |
| 461 | L728 | Diagram Are the paths drawn that the text describes? | - | UI | - | Group label. |
| 462 | L730 | Added direct Read and Edit arrows from the agent to workspace files and agent local data, outside the shell sandbox. | - | RECORD | - | Matches ARROWS (Read/Edit arrows, Local services box, remote MCP to SaaS). |
| 463 | L731 | Added a Local services box (Docker and other sockets, localhost ports) and an arrow from the agent. | - | RECORD | - | same as #462 |
| 464 | L732 | Added the return of remote MCP results to the agent and remote MCP access to downstream SaaS. | - | RECORD | - | same as #462 |
| 465 | L733 | The remote MCP box no longer implies a supplier runs it: ownership is separate from location (MCP architecture overview). | mcp-arch | OK | - | MCP architecture: servers can be local or remote; who runs them is separate. |
| 466 | L734 | Package fetches now enter the terminal rather than the workspace files box, and the credentials and workspace files boxes swapped places to keep the new arrows clear. | - | RECORD | - | Matches ARROWS. |
| 467 | L736 | Wording and assurance D06, D09, D16, response section, statuses | - | UI | - | Group label. |
| 468 | L738 | D06: plugin updates are automatic only where the marketplace has them on, and Claude Code defaults differ by marketplace type. | cc-plug | OK | 6 | Same as row 264. |
| 469 | L738 | The unverified Codex side was removed on 1 November. | - | FIXED | 6 | Put in the past tense on 1 Nov; the Codex sentence was cut. |
| 470 | L739 | D09: the Defender schema has the initiating process's command line but not its parent's. | mde | OK | - | Same as row 329. |
| 471 | L739 | The query now includes copilot and is labelled an initial query with incomplete coverage. | - | RECORD | 6 | Matches the query (row 345 includes copilot; row 341 tag). |
| 472 | L740 | "Most 2025 and 2026 incidents" became "Several documented" incidents. | - | RECORD | 6 | Wording history. |
| 473 | L740 | D16's quarter of sessions is attributed to Forever Security's customer telemetry. | helpnet | OK | - | Help Net: "about a quarter" of sessions (Forever telemetry). |
| 474 | L741 | Response section: evidence is preserved before cleanup or rebuild, and the Codex persistence is described as the user's sessions, not the whole computer. | - | RECORD | - | Matches the response section and status definitions. |
| 475 | L742 | Added a definition of OK: a named product and operating system, with evidence and date. | - | RECORD | - | same as #474 |

### Verification round, 29 October 2026

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 476 | L748 | Verification round, 29 October 2026 | - | UI | - | Heading. |
| 477 | L749 | A further audit raised ten findings. | - | RECORD | - | Describes a past audit. |
| 478 | L749 | Each was checked against its source before the page changed; all ten changed the content, some in narrower form. | - | RECORD | 9 | Describes a past audit. Pass 9: shortened (was "... against the page named in Sources ..., in full or in narrower form"). |
| 479 | L749 | A suggested field for product, operating system, version, assessor, evidence and date was not built: the page stores status only, a documented limit. | - | RECORD | 9 | Describes a past audit. Pass 9: shortened (was "One extra suggestion, ... the page already says it stores status only, so that stays a documented limit"). |
| 480 | L749 | Unconfirmed points are marked in the text. | - | RECORD | 9 | Describes a past audit. Pass 9: "Points that could not be confirmed" became "Unconfirmed points". |
| 481 | L751 | Controls and checks Findings 1 to 5 | - | UI | - | Group label. |
| 482 | L753 | npm: npm install runs a root.npm-extension.mjs or.cjs; npm ci does not (npm v12 docs). | npm-ext | OK | 6 | npm v12 docs: npm install runs a root .npm-extension.mjs or .cjs; npm ci does not. |
| 483 | L753 | Added to D01, D02 and the Current box, with dangerously-allow-all-scripts and a review of allowScripts grants. | - | RECORD | - | Matches D01 and D02; inference tag present. |
| 484 | L753 | Whether script approval covers the file is marked inference. | - | RECORD | 6 | same as #483 |
| 485 | L754 | Codex: an empty mcp\_servers table disables all servers, and plugin-bundled servers use plugins.&lt;plugin&gt;.mcp\_servers (OpenAI managed configuration). | cx-mc | OK | - | Same as rows 250 and 251. |
| 486 | L754 | The 30 October check confirmed that OpenAI documents separate rules for Git marketplace sources, bundled plugins and workspace plugins. | cx-mc | OK | 4 | Same as row 252. |
| 487 | L755 | D06 now covers token audience, token passthrough and per-client consent for proxy servers (MCP security best practices, draft). | mcp-bp | OK | - | Same as rows 258 and 259. |
| 488 | L756 | D07 now asks for the effective sandbox policy and lists the helper processes outside it (Anthropic sandbox docs). | cc-sbx | OK | - | Same as row 270. |
| 489 | L757 | D04 separates reading credential files from using exposed helpers or agents, and adds ssh-add -t, -c and -h (OpenBSD man page). | ssh-add | OK | - | Same as row 199. |
| 490 | L759 | Diagram Findings 6 and 7 | - | UI | - | Group label. |
| 491 | L761 | Added a browser profile box outside the shell sandbox, and arrows from the terminal to local services, from local MCP servers to the agent and from model providers back. | - | RECORD | 6 | Matches COMP and ARROWS. |
| 492 | L761 | The top row was narrowed to fit. | - | RECORD | 6 | same as #491 |
| 493 | L762 | The caption said arrows show selected paths, not every data flow, and split access to a remote MCP server from its access to downstream SaaS. | - | RECORD | 6 | same as #491 |
| 494 | L762 | That split is now in the D06 map notes. | - | FIXED | 6 | Put in the past tense: the split now lives in the D06 map notes. |
| 495 | L764 | Mapping, output quality and accessibility Findings 8 to 10 | - | UI | - | Group label. |
| 496 | L766 | D09 now maps first to OWASP MCP08 Lack of Audit and Telemetry, with ASI10 as a secondary relationship (OWASP MCP Top 10, beta). | owasp-mcp | OK | - | Same as row 327. |
| 497 | L767 | D11 now covers plausible but wrong or insecure agent code, gated by human review and security testing. | gh-resp | OK | 6 | GitHub: generated code can look valid while being wrong. |
| 498 | L767 | GitHub's guidance does not address agent-written tests, so that check is marked inference. | - | JUDGEMENT | 6 | Tagged inference. |
| 499 | L768 | Every marker, risk chip and map table button now carries its status in its accessible name and refreshes when the status changes. | - | RECORD | - | Accessible names; seen in the render check. |
| 500 | L770 | Found while checking Not in the audit | - | UI | - | Group label. |
| 501 | L772 | Claude Code approval keys: the location of disableAutoMode was initially marked contested. | cc-pmodes, cc-setref | OK | - | Both disableAutoMode forms documented (row 312). |
| 502 | L772 | Resolved on 30 October: the current settings reference explicitly accepts both the top-level and nested forms. | cc-pmodes, cc-setref | OK | - | same as #501 |
| 503 | L773 | Plugin4Shell: CSA reports automatic plugin updates on by default in Claude Code and Codex; Claude Code's docs differ by marketplace type. | csa-p4s, cc-plug | OK | 6 | CSA reports updates on by default; Claude docs differ by marketplace type. |
| 504 | L773 | It was marked contested; D06 now attributes the default to CSA. | - | FIXED | 5, 6 | Put in the past tense. |
| 505 | L774 | Codex [experimental\_network] needs enabled = true; domain rules alone do not turn the proxy on. | cx-mc | OK | - | Same as row 287. |

### Source corrections, 30 October 2026

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 506 | L780 | Source corrections, 30 October 2026 | - | UI | - | Heading. |
| 507 | L781 | Six findings were corrected against current official documentation: | vsc-pol, cc-perm, cx-mc, cc-pmodes, cc-setref | CUT | 8 | Pass 8 split one 63-word sentence into an intro and six list items, same words. Each of the six points matches rows 367, 285, 312, 252, 318 and the D14 card. |
| 508 | L782 | D14: plugin-only settings still permit plugin customisations. | vsc-pol, cc-perm, cx-mc, cc-pmodes, cc-setref | CUT | 8 | same as #507 |
| 509 | L783 | D10: the VS Code account gate checks organisation membership, not company ownership. | vsc-pol, cc-perm, cx-mc, cc-pmodes, cc-setref | CUT | 8 | same as #507 |
| 510 | L784 | D07: WebFetch approval rules are not a destination allowlist. | vsc-pol, cc-perm, cx-mc, cc-pmodes, cc-setref | CUT | 8 | same as #507 |
| 511 | L785 | D08: both disableAutoMode locations are documented. | vsc-pol, cc-perm, cx-mc, cc-pmodes, cc-setref | CUT | 8 | same as #507 |
| 512 | L786 | D06: Codex marketplace source restrictions have an official reference with stated scope limits. | vsc-pol, cc-perm, cx-mc, cc-pmodes, cc-setref | CUT | 8 | same as #507 |
| 513 | L787 | D08: the user approval-reviewer value is documented. | vsc-pol, cc-perm, cx-mc, cc-pmodes, cc-setref | CUT | 8 | same as #507 |
| 514 | L788 | This was a document and source review. | - | RECORD | - | Scope of a past check. |
| 515 | L788 | It did not rerun product enforcement tests or independently verify the earlier review and test records. | - | RECORD | - | same as #514 |
| 516 | L788 | Unrelated unresolved findings remain open. | - | RECORD | - | same as #514 |

### Fact check, 1 November 2026

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 517 | L792 | Fact check, 1 November 2026 | - | UI | 1, 2 | Heading. |
| 518 | L793 | Statements were checked against their sources, and long ones were shortened. | - | RECORD | 3 | This check. |
| 519 | L793 | Changed: | - | RECORD | - | same as #518 |
| 520 | L794 | D03: GlassWorm reaches other editors, not every editor. | socket-gw | OK | 4 | Restates FIXED row 170. |
| 521 | L795 | D04: Read(./.env) matches only the start folder; Dev Containers reuse local Git credentials and forward the SSH agent, as Microsoft words it. | cc-perm, dc-cred | OK | 4 | Restates FIXED row 206 and row 191. |
| 522 | L796 | D05: the planted AGENTS.md was reported in October; no find date is given. | helpnet | OK | 4 | Restates FIXED row 221. |
| 523 | L797 | D07: Codex leaves reads open by default; VS Code calls managed sandbox enforcement a preview. | cx-appr, vsc-sbx | OK | 4 | Restates FIXED row 271 and row 276. |
| 524 | L798 | D08: GhostApproval's misleading prompts hit some agents, not all. | csa-ghost | OK | 4 | Restates FIXED row 304. |
| 525 | L799 | D09: a local admin can edit any managed policy. | cc-mset | OK | 4 | Restates FIXED row 339. |
| 526 | L800 | D10: the repo upload was Grok Build. | grok | OK | 4 | Restates FIXED row 364. |
| 527 | L801 | Map notes: background Git calls are GitSpawn, not Check Point; servers must check Origin and should bind to localhost and authenticate (MCP spec); VS Code has an MCP allowlist but no plugin marketplace lock. | manifold, mcp-tr, vsc-pol | OK | 6 | Restates the map notes fixed in pass 4 (rows 745-746, 775-776, 784-785); row 787 already said must/should correctly. |
| 528 | L802 | Review and sources: Gen Digital counts protected users with detections; ClawHavoc's ClawHub count cites Antiy CERT. | gen, antiy | OK | 4 | Restates FIXED rows 624 and 239. |
| 529 | L803 | Removed, since no source states them: that ChatAgentNetworkFilter skips terminal commands, two example tool names (D08) and a Codex update default (D06). | - | RECORD | 4 | Lists the cuts made in this check. |
| 530 | L804 | Long paragraphs were shortened, and past review notes that no longer match the page were put in the past tense. | - | RECORD | 5 | same as #529 |
| 531 | L806 | The Git tests were re-run on Git 2.54.0 with the same results. | git-test | OK | 1 | Git 2.54.0 run on 1 Nov matched the 29 Oct results. |
| 532 | L806 | No product enforcement tests were run. | - | RECORD | 1 | No enforcement tests were run. |

### Evidence status

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 533 | L810 | Evidence status | - | UI | - | Headings. |

### Sources

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 534 | L818 | Sources | - | UI | - | same as #533 |
| 535 | L819 | The original review records these sources as opened on 29 October 2026. | - | RECORD | - | Source history. Row 537 names the sources added on 1 Nov (rows 719 and 720). |
| 536 | L819 | The six corrections dated 30 October used Microsoft's policy reference, Anthropic's settings and permissions references, and OpenAI's managed-configuration documentation. | - | RECORD | - | same as #535 |
| 537 | L819 | The 1 November fact check rechecked statements against them and added Grok Build and Antiy CERT. | - | RECORD | 9 | Source history. Row 537 names the sources added on 1 Nov (rows 719 and 720). Pass 9: "rechecked statements against these sources and added the Grok Build and Antiy CERT sources" became "... against them and added Grok Build and Antiy CERT". |
| 538 | L819 | Dates in brackets are the page's own publication or update date. | - | RECORD | - | Source history. Row 537 names the sources added on 1 Nov (rows 719 and 720). |

### Footer

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 539 | L825 | Marked [inference] is interpretation by AI, not stated in a source. | - | UI | - | Tag definitions. |
| 540 | L825 | Marked [unverified] or [not run here] was not checked against a source or a real system here. | - | UI | - | same as #539 |
| 541 | L826 | The git commands were re-run on 29 October 2026 on Git 2.43.0 and on 1 November 2026 on Git 2.54.0 in throwaway repos, including a normal clone and a copied folder. | git-test | FIXED | 1 | Added the 1 Nov re-run on Git 2.54.0. |
| 542 | L826 | The npm, VS Code, PowerShell and Defender hunting commands were not run here. | - | RECORD | - | True: those commands were not run. |
| 543 | L827 | Versions and dates change quickly in this area. | - | JUDGEMENT | - | Advice. |
| 544 | L827 | Check the "Current" box against the sources before you use it in a report. | - | JUDGEMENT | - | same as #543 |

### MORE

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 545 | MORE[0].t D11 | Agent changes reach shared repos and pipelines unchecked | - | UI | - | Title. |
| 546 | MORE[0].d D11 | The agent pushes, opens pull requests or starts workflows with the developer's identity. | - | JUDGEMENT | 6 | Describes agent capability. |
| 547 | MORE[0].d D11 | Branch protection governs what merges, not what runs: workflows can run before anything merges. | gh-secure | JUDGEMENT | 4 | Tagged [inference]. |
| 548 | MORE[0].d D11 | [inference] | gh-secure | JUDGEMENT | - | same as #547 |
| 549 | MORE[0].d D11 | GitHub's secure use reference treats repository write access as access to its secrets. | gh-secure | OK | - | GitHub secure use: write access to a repo gives access to its secrets through workflows. |
| 550 | MORE[0].d D11 | GitHub also says generated code can look valid while being wrong. | gh-resp | CUT | 9 | GitHub: generated code can look valid while being wrong. Pass 9: dropped "The agent can also write plausible code that is wrong or unsafe;". GitHub's sentence carries the point. |
| 551 | MORE[0].c D11 | For what merges: required review and narrowly scoped tokens. | gh-secure, codeowners | OK | 6 | Least-privilege GITHUB\_TOKEN, environments with required reviewers, CODEOWNERS, ephemeral runners are in GitHub's guidance. Pass 9: dropped "protected" before environments; required reviewers is the protection rule that matters here. |
| 552 | MORE[0].c D11 | For what runs: least-privilege GITHUB\_TOKEN permissions, environments with required reviewers, CODEOWNERS on workflow files and ephemeral runners. | gh-secure, codeowners | OK | 9 | same as #551 |
| 553 | MORE[0].c D11 | Claude Code ask rules are not a boundary: git -C. push does not match Bash(git push \*). | cc-perm | CUT | 9 | Claude permissions page: Bash rules match the command string, so git -C . push does not match Bash(git push \*). Pass 9: reworded to "Claude Code ask rules are not a boundary: git -C . push does not match Bash(git push \*)". Same fact. |
| 554 | MORE[0].c D11 | Add security scans, and check changed tests still fail when behaviour breaks. | - | JUDGEMENT | 9 | Tagged [inference]. Pass 9: dropped "Gate merges on review"; required review is already in the sentence before. Also cut "that" and "the" so the rendered item, with its "Control in full:" label, is 60 words. |
| 555 | MORE[0].c D11 | [inference] | - | JUDGEMENT | - | Tagged [inference]. |
| 556 | MORE[1].t D12 | Destructive actions with no attacker involved | - | UI | - | Title. |
| 557 | MORE[1].d D12 | VS Code warns that even without malicious intent an agent may provision cloud resources, change infrastructure, push code or trigger a deployment, all with the developer's credentials. | vsc-sec | OK | - | VS Code warns an agent may provision cloud resources, change infrastructure, push code or trigger a deployment. |
| 558 | MORE[1].c D12 | Keep production credentials off developer machines. | - | JUDGEMENT | - | Tagged [inference]. Worktrees share .git metadata (Git design). |
| 559 | MORE[1].c D12 | A separate Git worktree keeps agent edits apart from yours, but it does not limit credentials, network access, other folders or the shared.git metadata, so pair it with a sandbox or container and backups you can restore. | - | JUDGEMENT | - | same as #558 |
| 560 | MORE[1].c D12 | [inference] | - | JUDGEMENT | - | same as #558 |
| 561 | MORE[2].t D13 | VS Code tunnels used as a backdoor | - | UI | - | Title. |
| 562 | MORE[2].d D13 | Attackers with a foothold start a VS Code tunnel with code tunnel, from VS Code or the standalone CLI, and can install it as a service. | vsc-tun, unit42 | OK | - | code tunnel from VS Code or the CLI; can be installed as a service (code tunnel service install). Unit 42: attacker use. |
| 563 | MORE[2].d D13 | They then control the machine through Microsoft infrastructure. | vsc-tun | OK | - | Tunnels relay through Microsoft's dev tunnels service. |
| 564 | MORE[2].d D13 | Unit 42 reported this from Stately Taurus in 2024, and SentinelLabs in Operation Digital Eye. | unit42, secaffairs | OK | 6 | Unit 42 (Sep 2024): Stately Taurus used code tunnel. Security Affairs (11 Dec 2024): SentinelLabs, Operation Digital Eye. |
| 565 | MORE[2].c D13 | On Windows, use the Dev Tunnels policies (Disable Dev Tunnels, or allow only your Entra tenant). | devtun | OK | - | Dev Tunnels policies: disable Dev Tunnels, or allow only listed Entra tenants; Windows Group Policy. |
| 566 | MORE[2].c D13 | Alert on code tunnel processes, since Microsoft does not say whether the policies cover the code CLI. | devtun | OK | - | The policies page names Dev Tunnels and the Remote - Tunnels extension and is silent on the code CLI. Absence observed on the page. |
| 567 | MORE[3].t D14 | Poisoned agent memory | - | UI | - | Title. |
| 568 | MORE[3].d D14 | Agent memory can keep an attacker's instructions alive after the first session (OWASP ASI06). | owasp-asi | OK | - | ASI06 "Memory and Context Poisoning". |
| 569 | MORE[3].d D14 | AST01 describes skills that write into an agent's identity file. | ast01 | OK | - | AST01 describes skills writing persistent instructions into agent identity and memory files. |
| 570 | MORE[3].c D14 | Turn off agent memory where it is not needed (Claude Code autoMemoryEnabled). | cc-setref | OK | 4 | autoMemoryEnabled exists. |
| 571 | MORE[3].c D14 | Block standalone customisations with ChatStrictPluginOnlyCustomization (VS Code) or strictPluginOnlyCustomization (Claude Code). | vsc-pol, cc-setref | OK | 4 | ChatStrictPluginOnlyCustomization and strictPluginOnlyCustomization exist. |
| 572 | MORE[3].c D14 | Customisations from plugins are still allowed, so also restrict plugins and marketplaces; Anthropic recommends pairing its setting with strictKnownMarketplaces. | cc-setref | OK | 4 | Plugin customisations still load; Anthropic pairs the setting with strictKnownMarketplaces. |
| 573 | MORE[4].t D15 | Remote sessions and remote control reach the laptop | - | UI | - | Title. |
| 574 | MORE[4].d D15 | Session sync to GitHub, sharing the machine as a GitHub environment through Mission Control, and Claude Code Remote Control widen who and what can reach agent sessions on the machine. | vsc-pol, cc-setref | OK | - | VS Code: ChatAgentHostGitHubEnvironments "shared as a GitHub environment ... through Mission Control"; CopilotSessionSync; Claude Remote Control. |
| 575 | MORE[4].c D15 | Decide ChatAgentHostGitHubEnvironments and CopilotSessionSync by policy, and set Claude Code disableRemoteControl where remote control is not needed. | vsc-pol, cc-setref | OK | - | All three setting names exist. |
| 576 | MORE[5].t D16 | Agent-driven browsing | - | UI | - | Title. |
| 577 | MORE[5].d D16 | Browser tools let the agent open pages that can drop files or carry instructions. | vsc-sec | JUDGEMENT | - | General browser risk. |
| 578 | MORE[5].d D16 | In Forever Security's customer telemetry, about a quarter of agent sessions open a browser. | helpnet | OK | 4 | "About a quarter" of agent sessions, from Forever telemetry. |
| 579 | MORE[5].d D16 | A browser that is already signed in also lets the agent act in those web apps as the user. | - | JUDGEMENT | 4 | Tagged [inference]. |
| 580 | MORE[5].d D16 | [inference] | - | JUDGEMENT | - | same as #579 |
| 581 | MORE[5].c D16 | Limit browser tools (BrowserChatTools) and apply the domain allowlist (ChatAgentNetworkFilter). | vsc-pol | OK | - | BrowserChatTools (workbench.browser.enableChatTools) and ChatAgentNetworkFilter exist. |
| 582 | MORE[5].c D16 | In Codex, set browser origin rules under [browser\_use] and decide on computer\_use, which can drive a browser as a native app. | cx-mc | OK | - | Codex requirements: [browser\_use] origin rules and [computer\_use] sections. |
| 583 | MORE[5].c D16 | Give agents a browser profile without the user's sign-ins. | - | JUDGEMENT | - | Tagged [inference]. |
| 584 | MORE[5].c D16 | [inference] for the profile. | - | JUDGEMENT | - | same as #583 |
| 585 | MORE[6].t D17 | Telemetry becomes a sensitive data store | - | UI | - | Title. |
| 586 | MORE[6].d D17 | Capturing prompt, response and tool content (CopilotOtelCaptureContent) copies code, and any secrets in it, into the logging pipeline. | vsc-pol | OK | - | CopilotOtelCaptureContent captures prompt and response content. |
| 587 | MORE[6].c D17 | Capture metadata by default, and content only where the SIEM is approved for it. | - | JUDGEMENT | - | Advice. |

### PERSONAS

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 588 | PERSONAS[0].n | Offensive security lead | - | RECORD | - | Persona label. |
| 589 | PERSONAS[0].r | Red team: are these the right risks, in the right order, in the right place? | - | RECORD | - | same as #588 |
| 590 | PERSONAS[0].f[0] | The ranking broke its own rule. | - | RECORD | - | Past finding; the priority list is marked as a proposed order. |
| 591 | PERSONAS[0].f[0] | It claimed to rank by observed exploitation, yet put prompt injection and approval bypass first, while packages, booby-trapped repos and extensions drove the 2025 and 2026 incidents. | - | RECORD | - | same as #590 |
| 592 | PERSONAS[0].f[0] | The list was reordered. | - | RECORD | - | same as #590 |
| 593 | PERSONAS[0].f[1] | The advice to set core.fsmonitor to false globally gave false assurance, because a repo's own config wins. | git-test | OK | - | Re-run: a repo's own core.fsmonitor overrides the global value. |
| 594 | PERSONAS[0].f[1] | Reproduced in a throwaway repo and replaced with patched agents, a config check before opening, and review on config folders. | git-test | OK | - | same as #593 |
| 595 | PERSONAS[0].f[2] | The sandbox boundary was drawn too wide. | - | RECORD | - | Past finding. |
| 596 | PERSONAS[0].f[2] | Claude Code runs MCP servers and hooks outside its sandbox, and dev containers forward credentials and run initializeCommand on the host. | cc-sbx, dc-ref, dc-cred | OK | - | Claude: MCP servers and hooks run outside the sandbox. Dev Containers: credentials forwarded; initializeCommand runs on the host. |
| 597 | PERSONAS[0].f[2] | MCP servers now sit outside the boundary and.devcontainer is part of D02. | - | RECORD | - | Matches ZONES and D02. |
| 598 | PERSONAS[0].f[3] | s1ngularity was filed under approval bypass, but the malware already ran code through an install script. | s1ng | OK | - | StepSecurity: s1ngularity ran through a postinstall script, then drove local AI CLIs. |
| 599 | PERSONAS[0].f[3] | It moved to D01, and each incident now has one home. | s1ng | OK | - | same as #598 |
| 600 | PERSONAS[0].f[4] | Added: the compromised official Amazon Q extension, the worm-to-repo loop on the code host, VS Code tunnels as a backdoor (now D13), and the point that provenance is not proof of safety. | aws-q | OK | - | AWS-2025-015: Amazon Q Developer extension 1.84.0. The rest matches D11, D13 and D03. |
| 601 | PERSONAS[1].n | Endpoint and developer-platform engineer | - | RECORD | - | Persona label. |
| 602 | PERSONAS[1].r | Fleet view: do the settings, commands and versions exist, and do they work at scale? | - | RECORD | - | same as #601 |
| 603 | PERSONAS[1].f[0] | Most names matched current docs, including AllowedExtensions, ChatToolsAutoApprove, chat.tools.edits.autoApprove, ChatApprovedAccountOrganizations, the Copilot OpenTelemetry policies and the Claude managed keys. | vsc-pol, vsc-ext, cc-setref | OK | - | All named settings exist in current docs. |
| 604 | PERSONAS[1].f[1] | Windows sandboxing was overstated. | cc-sbx, vsc-sbx | OK | - | Claude: no native Windows sandbox. VS Code: Windows experimental, Windows 11 builds listed (row 297). |
| 605 | PERSONAS[1].f[1] | Claude Code does not sandbox on native Windows, and VS Code's Windows sandbox is experimental and needs recent Windows 11 builds. | cc-sbx, vsc-sbx | OK | - | same as #604 |
| 606 | PERSONAS[1].f[1] | The VS Code sandbox device policies do not enforce anything for Copilot harness sessions. | vsc-sbx | OK | - | VS Code: "Sandbox device policies don't enforce these controls for Copilot harness sessions." |
| 607 | PERSONAS[1].f[2] | The chat.mcp.access values were wrong as written. | vsc-sec, vsc-src | OK | - | Docs say registryOnly and off; source says none, registry, all. Still marked contested. |
| 608 | PERSONAS[1].f[2] | The security page says registryOnly and off, the source code says none, registry and all. | vsc-sec, vsc-src | OK | - | same as #607 |
| 609 | PERSONAS[1].f[2] | Now marked contested. | vsc-sec, vsc-src | OK | - | same as #607 |
| 610 | PERSONAS[1].f[3] | ChatAgentNetworkFilter covers the fetch tool and the integrated browser. | vsc-pol | OK | 4 | ChatAgentNetworkFilter covers "fetch tool, integrated browser". |
| 611 | PERSONAS[1].f[3] | Corrected. | vsc-pol | OK | - | same as #610 |
| 612 | PERSONAS[1].f[4] | A deployment hazard was missing: a Claude managed settings file that is not valid JSON stops Claude Code from starting. | cc-mset | OK | - | Invalid managed JSON stops Claude Code from starting. |
| 613 | PERSONAS[1].f[4] | Added to D09. | cc-mset | OK | - | same as #612 |
| 614 | PERSONAS[1].f[5] | Several quick checks were fixed: credential.helper across all scopes, a config check that reads a received repo without entering it, a PowerShell variant, and npm checks that return a useful answer. | - | RECORD | - | Past fixes to the quick checks. |
| 615 | PERSONAS[1].f[5] | CVE-2025-48384 does not affect Windows. | datadog, ubuntu | OK | - | Datadog: Windows not affected by CVE-2025-48384. An earlier "fix" here was wrong and rolled back. |
| 616 | PERSONAS[2].n | Auditor and fact-checker | - | RECORD | - | Persona label. |
| 617 | PERSONAS[2].r | Assurance: is every date, number, CVE and attribution right? | - | RECORD | - | same as #616 |
| 618 | PERSONAS[2].f[0] | Most claims held up against primary sources. | - | RECORD | - | Past pass; no count kept, as it says. |
| 619 | PERSONAS[2].f[0] | The rest needed attribution or scope fixes, and one was a real technical error. | - | RECORD | - | same as #618 |
| 620 | PERSONAS[2].f[0] | The pass kept no count, so no figure is given. | - | RECORD | - | same as #618 |
| 621 | PERSONAS[2].f[1] | Confirmed dates and IDs for the OWASP lists, CVE-2025-53773, CVE-2025-48384 (in CISA KEV from 25 August 2025), CVE-2026-21852, CVE-2026-19592, GitSpawn, Plugin4Shell, ChainDrop, npm 12 and the package firewall. | cve | OK | - | CISA KEV added CVE-2025-48384 on 25 Aug 2025. NVD has CVE-2025-53773, CVE-2026-21852 and CVE-2026-19592. |
| 622 | PERSONAS[2].f[2] | Flagged the same core.fsmonitor error as the other two passes. | git-test | OK | - | Same Git result; re-run date correct. |
| 623 | PERSONAS[2].f[2] | The behaviour was re-run in a throwaway repo on 29 October 2026. | git-test | OK | - | same as #622 |
| 624 | PERSONAS[2].f[3] | Narrowed several claims: CVE-2025-59536 covers code run through project config before trust, and the hooks finding had no CVE; 1,184 ClawHavoc skills is a minimum count; not all six GhostApproval agents showed a misleading dialog; Gen Digital's figures count protected users with detections, not confirmed infections. | cve, antiy, csa-ghost, gen | FIXED | 1 | Gen Digital part reworded to "protected users with detections, not confirmed infections". CVE-2025-59536, 1,184 minimum and GhostApproval parts match their sources. |
| 625 | PERSONAS[2].f[4] | Softened wording: Microsoft calls a dev container an additional boundary rather than a stronger one, and one VS Code page says restricted permission levels stay visible but disabled. | dc-docs, vsc-appr | OK | - | Microsoft calls a dev container an additional boundary; the approvals page says blocked levels "remain visible but disabled". |

### EVIDENCE

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 626 | EVIDENCE[0].h | Verified here | - | UI | - | Heading. |
| 627 | EVIDENCE[0].i[0] | Setting and policy names against the VS Code and Claude Code docs, both updated in October 2026. | - | RECORD | - | Scope of a past check. |
| 628 | EVIDENCE[0].i[1] | Git behaviour in throwaway repos, run 29 October 2026 on Git 2.43.0 and re-run 1 November 2026 on Git 2.54.0: a repo's own core.fsmonitor overrides the global value; the environment override and git -c both block it; a normal clone carries no config or hooks but keeps tracked.vscode files; a copied folder with.git runs the command. | git-test | OK | - | Each Git result reproduced on 1 Nov 2026. |
| 629 | EVIDENCE[0].i[2] | npm 12.0.0 was released on 8 July 2026, 12.2.2 was current on 10 November 2026, and npm 12 needs Node.js 22.22.2, 24.15.0 or 26 (npm registry). | npm-reg | OK | - | Registry: 12.0.0 published 8 Jul 2026, latest 12.2.1, engines node ^22.22.2, ^24.15.0 or &gt;=26. Rechecked 10 Nov 2026: latest 12.2.2, published 4 Nov 2026; statement updated. |
| 630 | EVIDENCE[0].i[3] | Incidents and CVEs against the vendor advisory or the original research where one was available. | - | RECORD | - | Scope of past checks. |
| 631 | EVIDENCE[0].i[4] | Against vendor docs on 29 October 2026: Codex sandbox defaults and requirements.toml keys, VS Code automatic tasks and VSIX allowlists, GitHub code-owner rules, Claude Code sandbox scope and Defender process columns. | - | RECORD | 4 | same as #630 |
| 632 | EVIDENCE[0].i[5] | In the audit round: Copilot managed permissions, Actions secure use, npm config precedence, MCP transport security (2025-06-18), Claude Code plugin update defaults, Codex automatic review and Microsoft incident-response guidance. | - | RECORD | 4 | same as #630 |
| 633 | EVIDENCE[0].i[6] | Second pass, 29 October 2026: npm 12 script approval, Claude Code sandbox helpers, Codex mcp\_servers tables and approval reviewers, MCP security best practices (draft), ssh-add options, OWASP MCP Top 10 names, GitHub generated-code guidance, VS Code, Claude Code and Codex setting names, and the Plugin4Shell, GitSpawn and ChainDrop figures. | - | RECORD | 4 | same as #630 |
| 634 | EVIDENCE[0].i[7] | Source corrections, 30 October 2026: six findings checked against current Microsoft policy, Anthropic settings and permissions, and OpenAI managed-configuration documentation. | - | RECORD | - | same as #630 |
| 635 | EVIDENCE[0].i[7] | Updated D06, D07, D08, D10 and D14, the map summaries and source notes. | - | RECORD | - | same as #630 |
| 636 | EVIDENCE[0].i[7] | No product enforcement tests were run in this correction pass. | - | RECORD | 1 | same as #630 |
| 637 | EVIDENCE[0].i[8] | Fact check, 1 November 2026: every statement rechecked against its source, then corrected, shortened or cut. | - | RECORD | 6 | This check; matches rows 719, 720 and 639 (gh-cms keys confirmed). |
| 638 | EVIDENCE[0].i[8] | Git re-run on 2.54.0. | - | RECORD | - | same as #637 |
| 639 | EVIDENCE[0].i[8] | GitHub's sandbox.userPolicy keys confirmed. | - | RECORD | 2 | same as #637 |
| 640 | EVIDENCE[0].i[8] | Grok Build and Antiy CERT sources added. | - | RECORD | 2 | same as #637 |
| 641 | EVIDENCE[1].h | Interpretation by AI | - | UI | - | Heading. |
| 642 | EVIDENCE[1].i[0] | The priority order, which is not scored, and the mapping to OWASP IDs. | - | JUDGEMENT | - | Listed as judgement. |
| 643 | EVIDENCE[1].i[1] | Where each risk sits on the map, and the owner per zone. | - | JUDGEMENT | - | same as #642 |
| 644 | EVIDENCE[1].i[2] | Relevance of the further risks, and the friction estimates for first controls. | - | JUDGEMENT | - | same as #642 |
| 645 | EVIDENCE[2].h | Still open | - | UI | - | Heading. |
| 646 | EVIDENCE[2].i[0] | The valid chat.mcp.access values, since Microsoft's docs and source disagree. | vsc-sec, vsc-src | OK | - | Open: docs and source disagree (row 245). |
| 647 | EVIDENCE[2].i[1] | Whether ChatToolsAutoApprove hides the permission levels or leaves them visible but disabled, since two VS Code pages say different things. | vsc-sec, vsc-appr | OK | - | Open: the security page says the policy will "hide" the levels; the approvals page says they "remain visible but disabled". |
| 648 | EVIDENCE[2].i[2] | Whether VS Code blocks reads of secret files outside Agent Host sessions. | gh-cms | OK | - | Open: managed Read(...) rules are documented for Agent Host only. |
| 649 | EVIDENCE[2].i[2] | GitHub documents managed Read(...) deny rules for Copilot Agent Host sessions only; none was found for other harnesses, which does not mean none exists. | gh-cms | OK | - | same as #648 |
| 650 | EVIDENCE[2].i[3] | How Codex [experimental\_network] behaves on Windows; OpenAI says support is limited. | cx-mc | OK | - | Open: OpenAI says Windows support is "still limited". |
| 651 | EVIDENCE[2].i[4] | Whether Claude Code releases after 2.1.252 closed the second GitSpawn path. | manifold | RECORD | - | Open item. No source answers it. |
| 652 | EVIDENCE[2].i[4] | No source says. | manifold | RECORD | - | same as #651 |
| 653 | EVIDENCE[2].i[5] | Copilot's Plugin4Shell status after September 2026. | csa-p4s | RECORD | - | Open item. |
| 654 | EVIDENCE[2].i[6] | The npm, VS Code, PowerShell and Defender hunting commands were not run on a managed machine. | - | RECORD | - | True: those commands were not run here. |
| 655 | EVIDENCE[2].i[7] | How an empty Codex mcp\_servers table treats plugin-bundled servers was not tested. | cx-mc | OK | 4 | Open item; separate controls for bundled, workspace and Git sources are documented. |
| 656 | EVIDENCE[2].i[7] | OpenAI documents separate controls for bundled, workspace and Git-sourced plugins; check each route in use. | cx-mc | OK | 4 | same as #655 |
| 657 | EVIDENCE[2].i[8] | Whether npm script approval covers the root.npm-extension file. | npm-ext, npm12-cfg | OK | - | Open: neither npm page says whether allow-scripts covers .npm-extension. |
| 658 | EVIDENCE[2].i[8] | The npm page is silent. | npm-ext, npm12-cfg | OK | - | same as #657 |

### SOURCES

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 659 | SOURCES[0] | Secure AI-assisted development in VS Code \| https://code.visualstudio.com/docs/agents/run/security \| Microsoft (October 2026). Trust boundaries, approvals, sandbox, risk categories, policy gaps per harness. | vsc-sec | OK | - | Title and URL match. |
| 660 | SOURCES[1] | Centrally manage VS Code settings with policies \| https://code.visualstudio.com/docs/enterprise/policies \| Microsoft (28.10.2026). Policy names and behaviour, including the approved-organisation membership gate and plugin-only customisation scope. Rechecked for the six corrections on 30.10.2026. | vsc-pol | OK | - | Title, URL, 28.10.2026 match. |
| 661 | SOURCES[2] | Manage approvals and permissions \| https://code.visualstudio.com/docs/agents/run/approvals \| Microsoft. Permission levels and terminal auto-approval. | vsc-appr | OK | - | Title and URL match. |
| 662 | SOURCES[3] | Manage extensions in enterprise environments \| https://code.visualstudio.com/docs/enterprise/extensions \| Microsoft. AllowedExtensions and the private marketplace. | vsc-ext | OK | - | Title and URL match. |
| 663 | SOURCES[4] | Claude Code: example settings files \| https://code.claude.com/docs/en/settings-example \| Anthropic. Managed settings keys for permissions, MCP, plugins, sandbox and versions. | cc-sex | OK | - | Page exists, titled "Example settings files". Its managed-settings.json example sets permissions.deny, allowedMcpServers, allowManagedMcpServersOnly, strictKnownMarketplaces, sandbox and requiredMinimumVersion. |
| 664 | SOURCES[5] | OWASP Top 10 for Agentic Applications for 2026 \| https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ \| OWASP GenAI Security Project (9.12.2025). ASI names cross-checked against secondary summaries. | owasp-asi | OK | - | Title, URL, 9.12.2025 match. |
| 665 | SOURCES[6] | OWASP MCP Top 10 \| https://owasp.org/www-project-mcp-top-10/ \| OWASP. Beta (phase 3). MCP01 to MCP10. | owasp-mcp | FIXED | 7 | Was a narrower ID range. The list runs MCP01 to MCP10, beta. |
| 666 | SOURCES[7] | OWASP Agentic Skills Top 10: AST01 Malicious Skills \| https://owasp.org/www-project-agentic-skills-top-10/ast01.html \| OWASP. ClawHavoc and skill persistence. | ast01 | OK | - | Title and URL match. |
| 667 | SOURCES[8] | GitHub Copilot: Remote Code Execution via Prompt Injection (CVE-2025-53773) \| https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection \| Embrace The Red, original research. | embrace | OK | - | Title and URL match. |
| 668 | SOURCES[9] | Researcher uncovers 30+ flaws in AI coding tools (IDEsaster) \| https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html \| The Hacker News (December 2025). | thn-ides | FIXED | 9 | Was "Researchers uncover". Read in a browser on 1 Nov: the headline is "Researcher Uncovers 30+ Flaws in AI Coding Tools", one researcher (Ari Marzouk), dated 6 Dec 2025. |
| 669 | SOURCES[10] | North Korea-linked hackers target developers with VS Code projects \| https://thehackernews.com/2026/01/north-korea-linked-hackers-target.html \| The Hacker News (January 2026). tasks.json with runOn: folderOpen. | thn-nk | OK | - | Title, URL, January 2026, runOn: folderOpen match. |
| 670 | SOURCES[11] | Organizations warned of exploited Git vulnerability \| https://www.securityweek.com/organizations-warned-of-exploited-git-vulnerability/ \| SecurityWeek. CVE-2025-48384 in CISA KEV. Fixed versions from Computing. | secweek | OK | - | Title and URL match; CVE-2025-48384 in KEV. |
| 671 | SOURCES[12] | Malicious .git configs can make Claude, Codex, Cursor and other AI agents run attacker code \| https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html \| The Hacker News (2.9.2026). GitSpawn by Manifold Security, versions and mitigations. | thn-gitspawn, manifold | FIXED | 1 | Note now says GitSpawn by Manifold. The day is right: read in a browser on 1 Nov, the article is dated Sep 02, 2026 and names Manifold Security. |
| 672 | SOURCES[13] | Claude Code flaws left AI tool wide open to hackers \| https://www.itpro.com/software/development/claude-code-flaws-left-ai-tool-wide-open-to-hackers-heres-what-developers-need-to-know \| ITPro (27.2.2026). Check Point findings, CVE-2025-59536 and CVE-2026-21852. | itpro | OK | - | 27.2.2026, Check Point, both CVEs. |
| 673 | SOURCES[14] | GhostApproval: a trust boundary gap in six AI coding agents \| https://labs.cloudsecurityalliance.org/research/csa-research-note-ghostapproval-ai-coding-agents-20260715-cs/ \| Cloud Security Alliance (15.7.2026), on Wiz research of 8.7.2026. | csa-ghost | OK | - | 15.7.2026 note on Wiz research of 8.7.2026. |
| 674 | SOURCES[15] | 73 Open VSX sleeper extensions linked to GlassWorm \| https://socket.dev/blog/73-open-vsx-sleeper-extensions-glassworm \| Socket (25.4.2026). Earlier wave: socket.dev/blog/open-vsx-transitive-glassworm-campaign. | socket-gw | OK | - | 25.4.2026. |
| 675 | SOURCES[16] | s1ngularity: Nx build system package compromised \| https://stepsecurity.io/blog/supply-chain-security-alert-popular-nx-build-system-package-compromised-with-data-stealing-malware \| StepSecurity (August 2025). Malware abusing local AI CLIs. | s1ng | OK | - | August 2025. |
| 676 | SOURCES[17] | ChainDrop supply chain compromise: anatomy of a self-propagating worm \| https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/ \| Microsoft Threat Intelligence (4.8.2026). Mitigations and Defender detections. | chaindrop | OK | - | 4.8.2026. |
| 677 | SOURCES[18] | Upcoming breaking changes for npm v12 \| https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/ \| GitHub (9.6.2026). Current npm release checked on the npm registry, 10.11.2026. | npm12-blog, npm-reg | OK | - | 9.6.2026. Rechecked 10 Nov 2026: check date in the note updated. |
| 678 | SOURCES[19] | GitHub package firewall in public preview \| https://github.blog/changelog/2026-10-20-github-package-firewall-in-public-preview/ \| GitHub (20.10.2026). | gh-fw | OK | - | 20.10.2026, public preview. |
| 679 | SOURCES[20] | ToxicSkills: malicious AI agent skills on ClawHub \| https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/ \| Snyk (5.2.2026). | snyk | OK | - | 5.2.2026. |
| 680 | SOURCES[21] | AI coding agents' 0-click RCE flaw (Plugin4Shell) \| https://www.theregister.com/a/5297335 \| The Register (September 2026), on research by Air Security. | register-p4s | FIXED | 7 | Research credited to Air Security, as The Register says. |
| 681 | SOURCES[22] | Infostealers have found a new target: your AI agent \| https://www.gendigital.com/blog/insights/research/infostealers-your-ai-agent \| Gen Digital (8.9.2026). | gen | OK | - | 8.9.2026. |
| 682 | SOURCES[23] | AI coding agents fall for malicious instructions planted in the Downloads folder \| https://www.helpnetsecurity.com/2026/10/26/ai-coding-agents-malware-openai-codex/ \| Help Net Security (26.10.2026), on Forever Security research. | helpnet | OK | - | 26.10.2026, Forever Security. |
| 683 | SOURCES[24] | MCP Token Theft in Claude Code: A Man-in-the-Middle Attack Chain \| https://www.mitiga.io/blog/claude-code-mcp-token-theft-mitm \| Mitiga (5.5.2026). | mitiga | FIXED | 7 | Date corrected to 5.5.2026. Rechecked 10 Nov 2026: title updated to the live page title. |
| 684 | SOURCES[25] | git-credential-store \| https://git-scm.com/docs/git-credential-store \| Git documentation. The store helper keeps credentials in plaintext. | git-cred | OK | - | Plaintext storage. |
| 685 | SOURCES[26] | Operation Digital Eye: China APT targets Europe via VS Code tunnels \| https://securityaffairs.com/171879/uncategorized/operation-digital-china-apt-targets-europe.html \| Security Affairs (11.12.2024), on SentinelLabs and Tinexta Cyber research. | secaffairs | OK | - | 11.12.2024. |
| 686 | SOURCES[27] | Claude Code: configure the sandboxed Bash tool \| https://code.claude.com/docs/en/sandboxing \| Anthropic. Platforms (no native Windows), what runs outside the sandbox, default read scope, limits of hostname filtering, Unix and Docker sockets. | cc-sbx | OK | - | Each listed topic is on the page. Rechecked 10 Nov 2026: title updated to the live page title. |
| 687 | SOURCES[28] | Claude Code: deploy managed settings \| https://code.claude.com/docs/en/managed-settings \| Anthropic. Delivery per OS, malformed files stop Claude Code, local admin caveat. | cc-mset | OK | - | Each listed topic is on the page. |
| 688 | SOURCES[29] | VS Code: agent sandboxing \| https://code.visualstudio.com/docs/agents/run/agent-sandboxing \| Microsoft. Windows 11 requirements, default network, credential pass-through, managed enforcement in preview. | vsc-sbx | OK | 4 | Each listed topic is on the page. |
| 689 | SOURCES[30] | Sharing Git credentials with your container \| https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials \| Microsoft. Dev Containers copy .gitconfig, reuse local Git credentials and forward the SSH agent. | dc-cred | OK | 4 | Copies .gitconfig, reuses credentials, forwards the SSH agent. |
| 690 | SOURCES[31] | Dev Container metadata reference \| https://containers.dev/implementors/json\_reference/ \| Dev Containers spec. initializeCommand runs on the host. | dc-ref | OK | - | initializeCommand runs on the host. |
| 691 | SOURCES[32] | AWS security bulletin AWS-2025-015 \| https://aws.amazon.com/security/security-bulletins/AWS-2025-015/ \| AWS (23.7.2025). Amazon Q Developer extension 1.84.0. | aws-q | OK | - | 23.7.2025, version 1.84.0. |
| 692 | SOURCES[33] | Git arbitrary file write (CVE-2025-48384) \| https://securitylabs.datadoghq.com/articles/git-arbitrary-file-write/ \| Datadog Security Labs. Windows not affected. | datadog | OK | - | Windows not affected. |
| 693 | SOURCES[34] | VS Code source: McpAccessValue \| https://github.com/microsoft/vscode/blob/main/src/vs/platform/mcp/common/mcpManagement.ts \| Microsoft. chat.mcp.access values none, registry, all. | vsc-src | OK | - | McpAccessValue: none, registry, all. |
| 694 | SOURCES[35] | Plugin4Shell research note \| https://labs.cloudsecurityalliance.org/research/csa-research-note-plugin4shell-ai-coding-agent-supply-chain/ \| Cloud Security Alliance (September 2026). Patched versions and Copilot status. Opened by the fact-checker. | csa-p4s | OK | - | September 2026; patched versions and Copilot status. |
| 695 | SOURCES[36] | Stately Taurus abuses VS Code in Southeast Asian espionage \| https://unit42.paloaltonetworks.com/stately-taurus-abuses-vscode-southeast-asian-espionage \| Unit 42 (September 2024). First reported real-world use of code tunnel. | unit42 | OK | - | September 2024. |
| 696 | SOURCES[37] | Dev Tunnels policies \| https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies \| Microsoft. Windows-only Group Policy for Dev Tunnels and the Remote - Tunnels extension. | devtun | OK | - | Windows Group Policy for Dev Tunnels and Remote - Tunnels. |
| 697 | SOURCES[38] | Claude Code settings reference \| https://code.claude.com/docs/en/settings-reference \| Anthropic. Plugin-only customisation scope, strictKnownMarketplaces, autoMemoryEnabled, disableRemoteControl and allowManagedHooksOnly. Explicitly accepts disableAutoMode at top level and under permissions. Rechecked for the six corrections on 30.10.2026. | cc-setref | OK | - | Each named key is on the page, including both disableAutoMode forms. |
| 698 | SOURCES[39] | VS Code Remote Tunnels \| https://code.visualstudio.com/docs/remote/tunnels \| Microsoft. code tunnel from VS Code or the standalone CLI, and code tunnel service install. | vsc-tun | OK | - | code tunnel and code tunnel service install. |
| 699 | SOURCES[40] | GitSpawn: a single flaw lets untrusted repos run code \| https://www.manifold.security/blog/ai-coding-agents-git-hijack \| Manifold Security (1.9.2026). Original research: clone does nothing, ultrareview uses another key, Codex mechanism differs. | manifold | OK | - | 1.9.2026. |
| 700 | SOURCES[41] | Integrate with external tools via tasks \| https://code.visualstudio.com/docs/debugtest/tasks \| Microsoft (28.10.2026). task.allowAutomaticTasks and runOn: folderOpen. | vsc-tasks | OK | - | 28.10.2026; task.allowAutomaticTasks and runOn: folderOpen. |
| 701 | SOURCES[42] | Codex: agent approvals and security \| https://developers.openai.com/codex/agent-approvals-security \| OpenAI. Default sandbox with command network off. | cx-appr | OK | - | Network off by default. |
| 702 | SOURCES[43] | Codex managed configuration \| https://learn.chatgpt.com/docs/enterprise/managed-configuration \| OpenAI. requirements.toml: approval policies and the user reviewer, permission profiles, deny\_read, MCP identities, network, browser, remote control and marketplace source restrictions, including their scope limits. Rechecked for the six corrections on 30.10.2026. From Codex 0.166.0 the network table is [network\_proxy]; [experimental\_network] is still accepted (checked 10.11.2026). | cx-mc | OK | - | Each listed topic is on the page. Rechecked 10 Nov 2026: table name note added, same as row 287. |
| 703 | SOURCES[44] | About code owners \| https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners \| GitHub. Review requests versus required code-owner approval, and owning CODEOWNERS itself. | codeowners | OK | - | Review requests vs required code-owner approval. |
| 704 | SOURCES[45] | DeviceProcessEvents table \| https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table \| Microsoft (7.8.2026). Command lines of the created and initiating process; parent file name, ID and creation time, but no parent command line. | mde | OK | - | 7.8.2026; columns as described. |
| 705 | SOURCES[46] | Secure use reference (GitHub Actions) \| https://docs.github.com/en/actions/reference/security/secure-use \| GitHub. Least-privilege GITHUB\_TOKEN, environments with required reviewers, ephemeral runners, CODEOWNERS on workflows, repository write access and secrets. | gh-secure | OK | - | Each listed topic is on the page. |
| 706 | SOURCES[47] | Enterprise managed settings for GitHub Copilot \| https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/enterprise-administrators/enterprise-managed-settings \| GitHub. Managed permissions (deny, ask, allow), Read(...) rules, Agent Host scope, sandbox deniedPaths. | gh-cms | OK | - | Each listed topic is on the page. |
| 707 | SOURCES[48] | MCP specification: transports (Streamable HTTP) \| https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#security-warning \| Model Context Protocol, version 2025-06-18. Origin validation, localhost binding, authentication. Newer versions were not compared. | mcp-tr | OK | - | Origin, localhost, authentication under 2025-06-18. |
| 708 | SOURCES[49] | MCP architecture overview \| https://modelcontextprotocol.io/docs/learn/architecture \| Model Context Protocol. A server is the program that serves context, regardless of where it runs; local and remote servers use different transports. | mcp-arch | OK | - | Local and remote servers, different transports. |
| 709 | SOURCES[50] | npm config \| https://docs.npmjs.com/cli/v11/using-npm/config \| npm. Precedence cli, env, project, user, global; min-release-age and min-release-age-exclude. | npm11-cfg | OK | - | Precedence and min-release-age on the v11 page. |
| 710 | SOURCES[51] | Claude Code: install and manage plugins \| https://code.claude.com/docs/en/plugins/install \| Anthropic. Auto-update defaults per marketplace type. | cc-plug | OK | - | Auto-update by marketplace type. Rechecked 10 Nov 2026: title updated to the live page title. |
| 711 | SOURCES[52] | Codex: automatic review \| https://learn.chatgpt.com/codex/sandboxing/auto-review \| OpenAI. Automatic review of escalation requests under the on-request policy. | cx-ar | OK | - | Auto-review under on-request. |
| 712 | SOURCES[53] | Plan incident response \| https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents \| Microsoft Learn. Balance urgency with precision; do no harm; do not destroy forensic evidence. | ms-ir | OK | - | Do not destroy forensic evidence. |
| 713 | SOURCES[54] | npm: .npm-extension \| https://docs.npmjs.com/cli/v12/configuring-npm/npm-extension/ \| npm. Root extension file run by npm install, not npm ci; transformManifest limits; ignore-extension; extension-file. | npm-ext | OK | - | npm install, not npm ci; options as listed. |
| 714 | SOURCES[55] | npm config (v12) \| https://docs.npmjs.com/cli/v12/using-npm/config \| npm. allow-scripts, dangerously-allow-all-scripts, ignore-scripts, ignore-extension, extension-file, min-release-age. | npm12-cfg | OK | - | Each listed option is on the page. |
| 715 | SOURCES[56] | MCP security best practices (draft specification) \| https://modelcontextprotocol.io/specification/draft/basic/security\_best\_practices \| Model Context Protocol. Confused deputy and per-client consent, token passthrough and audience validation, local server compromise. | mcp-bp | OK | - | Each listed topic is on the page. |
| 716 | SOURCES[57] | ssh-add(1) \| https://man.openbsd.org/ssh-add.1 \| OpenBSD. -t maximum lifetime, -c confirmation on each use, -h destination constraints (OpenSSH 8.9 or later). | ssh-add | OK | - | -t, -c, -h (OpenSSH 8.9). |
| 717 | SOURCES[58] | Application card: GitHub Copilot Agents \| https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent \| GitHub. Generated code can look valid while being wrong; automated checks supplement human review. | gh-resp | OK | - | Generated code can look valid while wrong. Rechecked 10 Nov 2026: title updated to the live page title. |
| 718 | SOURCES[59] | Claude Code: permissions \| https://code.claude.com/docs/en/permissions \| Anthropic. Permission rules and modes, WebFetch domain approvals, and disabling bypass and auto mode. Rechecked for the six corrections on 30.10.2026. | cc-perm | OK | - | Each listed topic is on the page. |
| 719 | SOURCES[60] | Grok Build uploaded entire Git repositories to xAI storage, not just files it read \| https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html \| The Hacker News (July 2026). Researcher cereblab, Grok Build CLI 0.2.93. | grok | FIXED | 1, 2 | Added: Hacker News, July 2026, cereblab, CLI 0.2.93. Read in a browser on 1 Nov: dated 14 Jul 2026, researcher cereblab, version 0.2.93. |
| 720 | SOURCES[61] | ClawHavoc: analysis of large-scale poisoning campaign targeting the OpenClaw skill market for AI agents \| https://www.antiy.net/p/clawhavoc-analysis-of-large-scale-poisoning-campaign-targeting-the-openclaw-skill-market-for-ai-agents/ \| Antiy CERT (6.2.2026). At least 1,184 malicious skills on ClawHub; Koi Security named the campaign. | antiy | FIXED | 2 | Added: Antiy CERT, 6.2.2026, at least 1,184 skills; Koi named the campaign. |

### START

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 721 | START[0] | D01 \| A release cooldown (min-release-age) as a managed npmrc default, enforced at the registry or firewall where it must hold; npm 12 per team later \| Low | npm11-cfg, cc-setref, vsc-ext, codeowners, vsc-pol, cc-sbx, mde | JUDGEMENT | - | Each named setting exists in its vendor docs. The choice of first control and the friction level are judgement. |
| 722 | START[1] | D02 \| Minimum agent versions, plus Git patching from vulnerability management \| Low | npm11-cfg, cc-setref, vsc-ext, codeowners, vsc-pol, cc-sbx, mde | JUDGEMENT | - | same as #721 |
| 723 | START[2] | D03 \| AllowedExtensions at publisher level, seeded from the current inventory \| Moderate | npm11-cfg, cc-setref, vsc-ext, codeowners, vsc-pol, cc-sbx, mde | JUDGEMENT | - | same as #721 |
| 724 | START[3] | D04 \| Expiry policy for GitHub and npm tokens \| None on the laptop | npm11-cfg, cc-setref, vsc-ext, codeowners, vsc-pol, cc-sbx, mde | JUDGEMENT | - | same as #721 |
| 725 | START[4] | D05 \| CODEOWNERS review on AGENTS.md, CLAUDE.md, .vscode/, .claude/, .devcontainer/ and .npm-extension.\* \| None on the laptop | npm11-cfg, cc-setref, vsc-ext, codeowners, vsc-pol, cc-sbx, mde | JUDGEMENT | - | same as #721 |
| 726 | START[5] | D06 \| VS Code MCP registry mode plus Claude Code strictKnownMarketplaces \| Moderate | npm11-cfg, cc-setref, vsc-ext, codeowners, vsc-pol, cc-sbx, mde | JUDGEMENT | - | same as #721 |
| 727 | START[6] | D07 \| Claude Code sandbox on macOS and WSL2 first, with failIfUnavailable \| Low on macOS | npm11-cfg, cc-setref, vsc-ext, codeowners, vsc-pol, cc-sbx, mde | JUDGEMENT | - | same as #721 |
| 728 | START[7] | D08 \| Block global auto-approve and bypass mode by policy \| Low | npm11-cfg, cc-setref, vsc-ext, codeowners, vsc-pol, cc-sbx, mde | JUDGEMENT | - | same as #721 |
| 729 | START[8] | D09 \| Agent and Git version inventory from Defender for Endpoint and Intune \| Low | npm11-cfg, cc-setref, vsc-ext, codeowners, vsc-pol, cc-sbx, mde | JUDGEMENT | - | same as #721 |
| 730 | START[9] | D10 \| Restrict AI sign-in to approved organisations; verify company-managed identity separately \| Low | npm11-cfg, cc-setref, vsc-ext, codeowners, vsc-pol, cc-sbx, mde | JUDGEMENT | - | same as #721 |

### PLACE

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 731 | PLACE[0] D01/pkg | ChainDrop in August 2026 put a credential-stealing worm into more than 400 npm packages through a preinstall script. | chaindrop | OK | - | Microsoft (4 Aug 2026): worm in more than 400 npm packages via a preinstall script. |
| 732 | PLACE[1] D01/term | Before npm 12, npm install ran dependency install scripts by default. s1ngularity used that foothold to drive local AI CLIs. | npm12-blog, s1ng | OK | - | npm 12 changelog: install scripts now need approval; before that they ran by default. StepSecurity: s1ngularity used a postinstall script to drive local AI CLIs. |
| 733 | PLACE[2] D01/files | Install scripts run inside the workspace and can change any file in it. | - | JUDGEMENT | - | Follows from install scripts running as the user inside the project; no single source sentence. |
| 734 | PLACE[3] D01/agent | Agents install dependencies with no human looking at each package. | - | JUDGEMENT | - | Describes how agents work. |
| 735 | PLACE[3] D01/agent | GitHub names agents and CI as especially exposed. | gh-fw | OK | - | GitHub: install-time malware "affects coding agents and CI runners in particular". |
| 736 | PLACE[4] D01/code | Stolen npm and GitHub tokens let the worm republish packages. | chaindrop | OK | - | Microsoft: stolen npm and GitHub tokens used to republish; some copies carried valid provenance from a real CI workflow. |
| 737 | PLACE[4] D01/code | Some copies carried valid provenance from a real CI workflow. | chaindrop | OK | - | same as #736 |
| 738 | PLACE[5] D02/repo | Fake job tests, shared archives and synced folders deliver projects built to run code when opened. | thn-nk | OK | - | North Korean fake job tests deliver repos built to run code on open. |
| 739 | PLACE[5] D02/repo | They keep.git/config and hooks; a normal clone drops those but keeps tracked.vscode and.claude files. | git-test | OK | 4 | Re-run on Git 2.54.0: a zip keeps .git/config and hooks; a clone drops them but keeps tracked .vscode and .claude files. Shortened in pass 4. |
| 740 | PLACE[6] D02/vscode | In a trusted workspace, a folderOpen task runs once automatic tasks are allowed (task.allowAutomaticTasks, off by default with a one-time prompt). | vsc-tasks | OK | - | runOn folderOpen needs task.allowAutomaticTasks; off by default with a one-time prompt. |
| 741 | PLACE[6] D02/vscode | Restricted mode blocks tasks and agents in VS Code until the code is reviewed. | vsc-sec | OK | - | Restricted mode blocks tasks and agents until the workspace is trusted. |
| 742 | PLACE[7] D02/files | .vscode/tasks.json,.git/config,.devcontainer/devcontainer.json,.claude/settings.json and.mcp.json can all name a command to run. | vsc-tasks, dc-ref, cc-settings, cc-mcp | OK | - | Each file has a field that names a command (task command, postCreateCommand, hooks, MCP command). |
| 743 | PLACE[8] D02/term | Git runs a core.fsmonitor helper on git status, and hooks on checkout, when the repo arrived with its own.git folder. | git-test | OK | - | Re-run on Git 2.43.0 and 2.54.0: repo core.fsmonitor runs on git status and overrides the global value; hooks run on checkout. |
| 744 | PLACE[8] D02/term | A global setting does not override the repo's own config. | git-test | OK | - | same as #743 |
| 745 | PLACE[9] D02/agent | GitSpawn: background Git calls in several agents ran a command from the repo's Git config, sometimes before the trust prompt. | manifold, itpro, cve | FIXED | 4 | Pass 4. Before: one sentence put GitSpawn and the Check Point findings together as background Git calls. Check Point's finding (CVE-2025-59536) was project config, not Git. Now two sentences. |
| 746 | PLACE[9] D02/agent | Separately, Check Point found Claude Code running project config before trust (CVE-2025-59536). | manifold, itpro, cve | FIXED | 4 | same as #745 |
| 747 | PLACE[10] D02/code | Worms with stolen GitHub tokens push these config files into other repos, so the next clone carries the trap. | chaindrop | OK | - | Microsoft: malware can "inject Claude and Visual Studio Code configuration files into repositories". |
| 748 | PLACE[10] D02/code | Require review on config folders. | - | JUDGEMENT | - | Advice. |
| 749 | PLACE[11] D03/ext | The official Amazon Q extension 1.84.0 shipped with injected code in 2025. | aws-q | OK | - | AWS-2025-015: Amazon Q extension 1.84.0 shipped with injected code. |
| 750 | PLACE[11] D03/ext | GlassWorm has hit Open VSX repeatedly since October 2025. | socket-gw | OK | - | Socket: GlassWorm waves on Open VSX since October 2025. |
| 751 | PLACE[12] D03/exth | Extensions run with the user's rights and can read any file the user can. | vsc-ers | OK | - | VS Code: "The extension host has the same permissions as VS Code itself"; an extension "can read and write files". |
| 752 | PLACE[12] D03/exth | GlassWorm's 2026 variants also install into other editors, such as VS Code, Cursor and Windsurf. | socket-gw | FIXED | 1 | Pass 1. Before: "install into every editor on the machine". Socket names VS Code, Cursor and Windsurf. |
| 753 | PLACE[13] D03/policy | AllowedExtensions and an auto-update delay are the central controls in VS Code. | vsc-pol | OK | - | AllowedExtensions and ExtensionsAutoUpdateDelay (extensions.autoUpdateDelay) are VS Code policies. |
| 754 | PLACE[13] D03/policy | They match declared identifiers and do not verify a VSIX package's origin. | vsc-ext | OK | - | The allowlist matches publisher and extension IDs; it does not check where a VSIX came from. |
| 755 | PLACE[13] D03/policy | Forks need their own controls. | cursor-ext, vscodium | OK | - | Cursor and VSCodium use their own marketplaces and settings. |
| 756 | PLACE[14] D04/creds | SSH keys, gh, az and npm tokens, and ~/.git-credentials (plaintext with the store helper) sit in predictable places. | git-cred | OK | - | Git docs: the store helper writes credentials unencrypted to ~/.git-credentials. |
| 757 | PLACE[15] D04/files | .env files and local config end up in agent context unless reads are blocked. | - | JUDGEMENT | - | Describes agent context. |
| 758 | PLACE[15] D04/files | Edit approval does not block reads. | vsc-appr | OK | - | Edit approval and read access are separate settings. |
| 759 | PLACE[15] D04/files | Read(./.env) matches only the start folder; Read(.env) matches any depth. | cc-perm | FIXED | 2, 3 | Pass 1. Before: "Read(./.env) covers the project root only". Anthropic anchors ./ to the start folder; Read(.env) matches at any depth. |
| 760 | PLACE[16] D04/adata | Infostealers now collect agent tokens, MCP configuration and prompt histories (Gen Digital, September 2026). | gen | OK | 4 | Gen Digital (8 Sep 2026): stealers collect "access tokens, MCP configurations, prompt histories". Pass 4 swapped "transcripts" for Gen's own words. |
| 761 | PLACE[17] D04/term | Sandboxed commands can still read credentials by default: Claude Code's sandbox reads ~/.ssh unless denied, and VS Code passes Git and gh credentials in. | cc-sbx, vsc-sbx | OK | - | Claude Code sandbox allows reads outside denied paths by default; VS Code passes Git and gh credentials into the sandbox. |
| 762 | PLACE[18] D04/cloud | Long-lived, broad tokens turn one compromised laptop into cloud and SaaS access. | - | JUDGEMENT | - | Risk statement. |
| 763 | PLACE[19] D04/agent | The agent's own Read and Edit tools open workspace files and agent config directly, outside the shell sandbox. | cc-sbx | OK | - | Claude Code: Read and Edit tools are governed by permission rules, not the sandbox. |
| 764 | PLACE[19] D04/agent | Read deny rules, not only sandbox rules, decide whether.env files and ~/.ssh reach the model. | cc-perm | OK | - | Read deny rules stop the Read tool; sandbox rules cover shell commands. |
| 765 | PLACE[20] D05/web | Pages, issues, pull requests and READMEs can carry hidden instructions that the agent reads as commands. | mcp-bp, vsc-sec | OK | - | Both describe hidden instructions in content the agent reads. |
| 766 | PLACE[21] D05/repo | A repo or a download can bring its own instruction files. | - | JUDGEMENT | - | Describes how agents load files. |
| 767 | PLACE[21] D05/repo | Forever Security reported a planted AGENTS.md in a customer's Downloads folder in October 2026. | helpnet | FIXED | 2 | Pass 2. Before: "found in October 2026". Help Net gives no find date, only the October report. |
| 768 | PLACE[22] D05/instr | Agents are built to obey AGENTS.md, CLAUDE.md and rule files. | vsc-sec | OK | - | Agents load AGENTS.md, CLAUDE.md and rule files as instructions. |
| 769 | PLACE[22] D05/instr | VS Code notes that instructions guide the model and are not an enforcement boundary. | vsc-sec | OK | - | VS Code security page: "Instructions guide the model and are not an enforcement boundary." |
| 770 | PLACE[23] D05/agent | The model cannot reliably tell instructions from data. | - | JUDGEMENT | - | General model behaviour. |
| 771 | PLACE[23] D05/agent | An agent started in the home folder or Downloads also reads far more than the project. | - | JUDGEMENT | - | same as #770 |
| 772 | PLACE[24] D05/mcp | MCP tool output goes straight into the model context, so a tool that reads attacker text passes it on. | mcp-arch | OK | - | MCP: tool results return into the model context. |
| 773 | PLACE[25] D05/mcpr | Results from a remote MCP server return into the agent's context, so a server that relays attacker-controlled text passes prompt injection on. | mcp-arch | OK | - | same as #772 |
| 774 | PLACE[26] D06/addon | Malicious skills (ClawHavoc on ClawHub) and swapped plugins (Plugin4Shell, research) arrive through add-on marketplaces. | antiy, csa-p4s | CUT | 2 | Pass 2 dropped the [unverified] Codex clause (27 -&gt; 17 words). ClawHavoc on ClawHub: Antiy. Plugin4Shell: CSA research note. |
| 775 | PLACE[27] D06/mcp | Local MCP servers run as the user. | mcp-arch, mcp-bp | FIXED | 4 | Pass 4. Before also said a local HTTP server "must also validate Origin, bind to localhost and authenticate". The spec says must for Origin but should for localhost and auth. Sentence cut; row 787 states it correctly. |
| 776 | PLACE[27] D06/mcp | Their tool descriptions enter the model context, where poisoned text acts as instructions. | mcp-arch, mcp-bp | FIXED | 4 | same as #775 |
| 777 | PLACE[28] D06/agent | Plugin4Shell needed no click where automatic plugin updates were on. | csa-p4s | OK | 2 | CSA: no click needed where automatic plugin updates were on. |
| 778 | PLACE[28] D06/agent | Current defaults differ by product and marketplace. | cc-plug | OK | 2 | Claude Code plugin auto-update defaults differ by marketplace. |
| 779 | PLACE[29] D06/cloud | MCP servers hold tokens for SaaS and cloud, so a bad server reaches well beyond the laptop. | mcp-bp | OK | 4 | MCP best practices: token audience checks, no token passthrough. Shortened in pass 4. |
| 780 | PLACE[29] D06/cloud | Access to the server and the server's access downstream are separate checks (token audience, no token passthrough). | mcp-bp | OK | 4 | same as #779 |
| 781 | PLACE[30] D06/mcpr | Remote MCP servers, whoever runs them, hold their own tokens, receive what the agent sends and return results into the model context. | mcp-auth, mcp-bp | FIXED | 6 | Pass 4. Before: servers "should accept only tokens issued for them". The spec says MUST and MUST NOT pass through. Pass 6 shortened it. |
| 782 | PLACE[30] D06/mcpr | Allowlist them by URL. | mcp-auth, mcp-bp | FIXED | 6 | same as #781 |
| 783 | PLACE[30] D06/mcpr | The MCP spec says they must accept only tokens issued for them and must not pass a client's token on. | mcp-auth, mcp-bp | FIXED | 6 | same as #781 |
| 784 | PLACE[31] D06/policy | VS Code, Claude Code and Codex each support an MCP allowlist. | vsc-pol, cc-mmcp, cc-setref, cx-mc | FIXED | 4 | Pass 4. Before: "VS Code and Claude Code both support an MCP allowlist and a fixed plugin marketplace". VS Code has no marketplace lock (it has ChatEnabledPlugins); Codex added. |
| 785 | PLACE[31] D06/policy | Claude Code and Codex can also restrict plugin marketplace sources; VS Code can set which plugins are enabled. | vsc-pol, cc-mmcp, cc-setref, cx-mc | FIXED | 4 | same as #784 |
| 786 | PLACE[32] D06/svc | A local MCP server that uses HTTP rather than stdio can be reached by other local processes and, through DNS rebinding, by web pages. | mcp-tr | OK | - | MCP transports: servers MUST validate Origin, SHOULD bind to localhost, SHOULD authenticate; DNS rebinding named. |
| 787 | PLACE[32] D06/svc | The MCP specification says it must validate Origin and should bind to localhost and authenticate. | mcp-tr | OK | - | same as #786 |
| 788 | PLACE[33] D07/agent | Claude Code's sandbox covers shell commands only. | cc-sbx, cc-perm | OK | 4 | Claude Code sandbox covers Bash only; WebFetch allow rules pre-approve. Shortened in pass 4. |
| 789 | PLACE[33] D07/agent | Read, Edit and WebFetch follow permission rules instead. | cc-sbx, cc-perm | OK | 4 | same as #788 |
| 790 | PLACE[33] D07/agent | A WebFetch allow rule pre-approves matching requests; others fall to the permission mode, not an automatic block. | cc-sbx, cc-perm | OK | 4 | same as #788 |
| 791 | PLACE[34] D07/term | Without a sandbox, commands run with the user's full file access. | - | JUDGEMENT | - | Plain consequence of no sandbox. |
| 792 | PLACE[34] D07/term | Codex sandboxes commands by default; Claude Code's sandbox is off by default and has no native Windows support. | cx-appr, cc-sbx | OK | - | Codex sandbox on by default; Claude Code sandbox opt-in, macOS, Linux and WSL2 only. |
| 793 | PLACE[34] D07/term | Commands can also open their own network connections. | - | JUDGEMENT | - | Plain consequence. |
| 794 | PLACE[35] D07/mcp | Claude Code runs local MCP servers, hooks, plugin monitors, LSP servers, the status line command and apiKeyHelper outside its sandbox with full access. | cc-sbx | OK | - | Anthropic lists these as running outside the sandbox. |
| 795 | PLACE[35] D07/mcp | VS Code can sandbox stdio servers on macOS and Linux. | vsc-sec | OK | - | VS Code: "On macOS and Linux, you can enable sandboxing for locally-running MCP servers that use the stdio transport." |
| 796 | PLACE[36] D07/svc | Docker sockets, other Unix sockets and unauthenticated localhost services can give a command more reach than file and domain rules suggest. | cc-sbx | OK | 4 | Anthropic names the Docker socket and Unix sockets as sandbox escapes. Shortened in pass 4. |
| 797 | PLACE[36] D07/svc | Anthropic names the Docker socket and Unix sockets as ways around the sandbox. | cc-sbx | OK | 4 | same as #796 |
| 798 | PLACE[37] D07/egress | VS Code's agent sandbox leaves outbound network on by default; Codex keeps command network off by default. | vsc-sbx, cx-appr | OK | - | VS Code sandbox network open unless restricted; Codex network off by default. |
| 799 | PLACE[37] D07/egress | Without a domain allowlist, exfiltration is one request away. | - | JUDGEMENT | - | Risk statement and design advice. |
| 800 | PLACE[37] D07/egress | This is only a control point if traffic is forced through a proxy. | - | JUDGEMENT | - | same as #799 |
| 801 | PLACE[38] D07/inet | Any domain works for exfiltration and command and control when egress is open. | - | JUDGEMENT | - | same as #799 |
| 802 | PLACE[38] D07/inet | An allowed service such as GitHub can also receive data into an attacker-controlled account. | cc-sbx | OK | - | Anthropic warns allowed domains such as github.com can carry data out. |
| 803 | PLACE[39] D08/agent | Allow all, Autopilot and bypass modes remove the approval prompt. | vsc-appr, cc-pmodes | OK | - | Allow all, Autopilot and bypassPermissions skip prompts. |
| 804 | PLACE[39] D08/agent | Assisted permissions use a model judge, which VS Code says is not a security boundary. | vsc-sec | OK | - | VS Code: Assisted permissions "reduces approval interruptions but is not a security boundary". |
| 805 | PLACE[40] D08/vscode | A workspace settings file can switch on auto-approve. | embrace, cve | OK | - | CVE-2025-53773: the agent wrote chat.tools.autoApprove into .vscode/settings.json. |
| 806 | PLACE[40] D08/vscode | CVE-2025-53773 had the agent write that setting itself. | embrace, cve | OK | - | same as #805 |
| 807 | PLACE[41] D08/term | Terminal auto-approve rules use best-effort command parsing. | vsc-sec | OK | - | VS Code: "best-effort command parsing and have known limitations with shell aliases, quote concatenation". |
| 808 | PLACE[41] D08/term | VS Code warns that aliases and quote tricks can slip past them. | vsc-sec | OK | - | same as #807 |
| 809 | PLACE[42] D08/policy | ChatToolsAutoApprove in VS Code and disableBypassPermissionsMode in Claude Code lock this centrally. | vsc-pol, cc-perm | OK | - | Both settings exist. |
| 810 | PLACE[43] D09/policy | Without an inventory of agents, versions, extensions and MCP servers you cannot tell who is exposed when the next flaw lands. | - | JUDGEMENT | - | Advice. |
| 811 | PLACE[44] D09/edr | Defender records the command lines of a new process and of its parent. | mde | OK | 4 | DeviceProcessEvents has ProcessCommandLine and InitiatingProcessCommandLine. Shortened in pass 4. |
| 812 | PLACE[44] D09/edr | That shows an agent started a command, but not the prompt, task or approval behind it. | mde | OK | 4 | same as #811 |
| 813 | PLACE[45] D09/tele | Agent telemetry (OpenTelemetry export in Copilot) shows tool calls. | vsc-pol, vsc-sec | OK | - | Copilot OTel export exists; VS Code says to verify coverage before treating logs as a complete audit trail. |
| 814 | PLACE[45] D09/tele | VS Code says hooks are not a complete audit trail. | vsc-pol, vsc-sec | OK | - | same as #813 |
| 815 | PLACE[46] D09/agent | Many 2026 fixes need a minimum agent version. | - | JUDGEMENT | - | Advice. |
| 816 | PLACE[46] D09/agent | Pin a current one centrally where the tool supports it. | - | JUDGEMENT | - | same as #815 |
| 817 | PLACE[47] D10/llm | Requests can carry selected code, file contents, terminal output and tool results to the model provider. | vsc-sec | OK | - | VS Code lists what context is sent. |
| 818 | PLACE[48] D10/mcpr | A remote MCP server is another recipient of code and context, with its own retention and location. | - | JUDGEMENT | - | Risk statement. |
| 819 | PLACE[49] D10/agent | Personal accounts, own-key models and third-party harnesses may fall outside company terms and policy. | - | JUDGEMENT | - | same as #818 |
| 820 | PLACE[50] D10/policy | Restrict sign-in to approved organisations: ChatApprovedAccountOrganizations in VS Code and forceLoginOrgUUID in Claude Code. | vsc-pol, cc-setref | OK | - | ChatApprovedAccountOrganizations and forceLoginOrgUUID exist; \* accepts any signed-in account. |
| 821 | PLACE[50] D10/policy | The VS Code gate checks membership, not company ownership of the GitHub account; its \* value accepts any signed-in GitHub or GHE account. | vsc-pol, cc-setref | OK | - | same as #820 |
| 822 | PLACE[51] D11/agent | The agent decides to push, open pull requests or start workflows, using the developer's identity. | - | JUDGEMENT | - | Describes agent capability; [inference] tag. |
| 823 | PLACE[51] D11/agent | It can also write plausible code that adds vulnerabilities or changes tests to hide defects [inference]. | - | JUDGEMENT | - | same as #822 |
| 824 | PLACE[52] D11/term | git push runs from the terminal. | - | JUDGEMENT | - | same as #822 |
| 825 | PLACE[52] D11/term | Ask rules such as Bash(git push \*) are easy to slip past, for example with git -C. push. | cc-perm | OK | - | Anthropic: git -C . push does not match Bash(git push \*). |
| 826 | PLACE[53] D11/mcp | A GitHub MCP server can open pull requests and start workflows without any git command. | gh-mcp | OK | - | GitHub MCP server tools include create\_pull\_request and run\_workflow. |
| 827 | PLACE[54] D11/code | Branch protection and required review control what merges, not what runs. | - | JUDGEMENT | - | Restates D11. |
| 828 | PLACE[54] D11/code | Workflows can run before merge, so add a CI boundary: restricted workflow permissions, protected environments with required reviewers and isolated, ephemeral runners. | gh-secure | OK | - | GitHub secure use guidance. |
| 829 | PLACE[55] D12/agent | VS Code warns that an agent may provision cloud resources, change infrastructure or trigger a deployment even without malicious intent. | vsc-sec | OK | - | VS Code: agents may provision cloud resources; "File modifications are written directly to disk". |
| 830 | PLACE[56] D12/files | VS Code notes that the agent can create, modify and delete files in the workspace, and that edits go straight to disk. | vsc-sec | OK | - | same as #829 |
| 831 | PLACE[57] D12/creds | The agent can do whatever the developer's credentials allow. | - | JUDGEMENT | - | Risk statements. |
| 832 | PLACE[57] D12/creds | Production credentials on the laptop raise the stakes. | - | JUDGEMENT | - | same as #831 |
| 833 | PLACE[58] D12/cloud | Changes to cloud and SaaS made with the developer's credentials are where accidental damage lands. | - | JUDGEMENT | - | same as #831 |
| 834 | PLACE[59] D13/vscode | code tunnel, from VS Code or the standalone CLI, gives remote control of the machine. | vsc-tun | OK | - | code tunnel and code tunnel service install. |
| 835 | PLACE[59] D13/vscode | It can also be installed as a service. | vsc-tun | OK | - | same as #834 |
| 836 | PLACE[60] D13/egress | The tunnel connection starts outbound through Microsoft infrastructure but carries commands back in, and blends in with normal traffic. | - | JUDGEMENT | - | Network behaviour and advice. |
| 837 | PLACE[60] D13/egress | Decide at the proxy whether the tunnel service is allowed. | - | JUDGEMENT | - | same as #836 |
| 838 | PLACE[61] D13/edr | Alert on code tunnel processes and on tunnels installed as a service. | - | JUDGEMENT | - | same as #836 |
| 839 | PLACE[62] D13/policy | On Windows, the Dev Tunnels policies can turn tunnels off or limit them to your Entra tenant. | devtun | OK | - | Dev Tunnels policies on Windows. |
| 840 | PLACE[63] D14/adata | Agent memory persists between sessions, so an injected instruction can come back in every new session. | owasp-asi | OK | - | ASI06 memory poisoning. |
| 841 | PLACE[64] D14/addon | OWASP AST01 describes malicious skills that write into the agent's identity file and survive uninstall. | ast01 | OK | - | AST01: "Malicious skills write backdoor instructions into the agent's identity file, surviving skill uninstall." |
| 842 | PLACE[65] D14/policy | Turn memory off where it is not needed (Claude Code autoMemoryEnabled). | cc-setref, vsc-pol | OK | - | autoMemoryEnabled, strict plugin-only settings and Remote Control setting exist. |
| 843 | PLACE[65] D14/policy | Block standalone customisations and separately restrict permitted plugins and marketplaces; plugin-only settings still permit eligible plugin customisations. | cc-setref, vsc-pol | OK | - | same as #842 |
| 844 | PLACE[66] D15/agent | Sharing the machine as a GitHub environment (Mission Control) or turning on Claude Code Remote Control lets agent sessions here be reached from other devices. | cc-setref, vsc-pol | OK | - | same as #842 |
| 845 | PLACE[67] D15/code | Session sync sends Copilot session history to GitHub.com (CopilotSessionSync). | vsc-pol | OK | - | CopilotSessionSync and ChatAgentHostGitHubEnvironments exist. |
| 846 | PLACE[68] D15/policy | ChatAgentHostGitHubEnvironments, CopilotSessionSync and Claude Code disableRemoteControl decide this centrally. | vsc-pol | OK | - | same as #845 |
| 847 | PLACE[69] D15/egress | These features keep connections open to outside services, which the egress point can see and limit. | - | JUDGEMENT | - | Tagged [inference]. |
| 848 | PLACE[69] D15/egress | [inference] | - | JUDGEMENT | - | same as #847 |
| 849 | PLACE[70] D16/agent | Browser tools let the agent open pages on its own. | - | JUDGEMENT | - | Describes the feature. |
| 850 | PLACE[70] D16/agent | In Forever Security's customer telemetry about a quarter of agent sessions open a browser. | helpnet | OK | - | Help Net: "about a quarter" of sessions. |
| 851 | PLACE[71] D16/web | A page the agent visits can drop files into Downloads or carry instructions for the agent. | - | JUDGEMENT | - | General browser risk. |
| 852 | PLACE[72] D16/egress | ChatAgentNetworkFilter limits which domains the fetch tool and the integrated browser can reach. | vsc-pol | OK | - | ChatAgentNetworkFilter covers fetch and the integrated browser. |
| 853 | PLACE[73] D16/cloud | A signed-in browser lets the agent act in web apps as the user. | - | JUDGEMENT | - | Tagged [inference]. |
| 854 | PLACE[73] D16/cloud | [inference] | - | JUDGEMENT | - | same as #853 |
| 855 | PLACE[74] D17/tele | Capturing prompt, response and tool content copies code, and any secrets in it, into the logging pipeline. | vsc-pol | OK | - | CopilotOtelCaptureContent captures content. |
| 856 | PLACE[75] D17/policy | CopilotOtelCaptureContent decides centrally whether content is captured. | vsc-pol | OK | - | same as #855 |
| 857 | PLACE[76] D16/browser | Browser tools let the agent drive a browser. | - | JUDGEMENT | - | Tagged [inference]. Shortened in pass 4. |
| 858 | PLACE[76] D16/browser | A signed-in profile carries the user's web sessions, which the agent reaches through tools outside the shell sandbox. | - | JUDGEMENT | 4 | same as #857 |
| 859 | PLACE[76] D16/browser | [inference] | - | JUDGEMENT | - | same as #857 |

### DESC

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 860 | DESC.all | Shows all ten. The link between attack path and risk is interpretation by AI. | - | JUDGEMENT | - | States itself as judgement. |
| 861 | DESC.content | Poisoned content: a web page, issue, README or tool output carries instructions, and the agent acts on them with the developer’s rights. | - | UI | - | Definitions of the four attack paths. |
| 862 | DESC.repo | Booby-trapped project: a repo, archive or shared folder is built so that opening it, or letting an agent look at it, runs code. | - | UI | - | same as #861 |
| 863 | DESC.supply | Supply chain: an extension, package, MCP server, plugin or skill is malicious from the start or turns malicious in an update. | - | UI | - | same as #861 |
| 864 | DESC.creds | Stolen tokens: malware or a hijacked agent collects keys and tokens from the machine and uses them elsewhere. | - | UI | - | same as #861 |

### ZONES

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 865 | ZONES[1].t | Untrusted inputs | - | UI | - | Zone names and owners. Owners are judgement. |
| 866 | ZONES[1].o | INTERNET AND SUPPLIERS | - | UI | - | same as #865 |
| 867 | ZONES[2].t | Developer workstation | - | UI | - | same as #865 |
| 868 | ZONES[2].o | DEVELOPER, WITH THE ENDPOINT TEAM | - | UI | - | same as #865 |
| 869 | ZONES[3].t | Outbound services | - | UI | - | same as #865 |
| 870 | ZONES[3].o | SUPPLIERS AND YOUR TENANTS | - | UI | - | same as #865 |
| 871 | ZONES[4].t | Governance and monitoring | - | UI | - | same as #865 |
| 872 | ZONES[4].o | IT, SECURITY AND SOC | - | UI | - | same as #865 |
| 873 | ZONES[4].note | Sets policy for, and collects events from, every layer | - | UI | - | same as #865 |

### COMP

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 874 | COMP.repo.t | Repos and shared files | - | UI | - | Diagram labels: names of sources and products. |
| 875 | COMP.repo.s | Clone, zip, drive, Downloads | - | UI | - | same as #874 |
| 876 | COMP.repo.short | Repos | - | UI | - | same as #874 |
| 877 | COMP.ext.t | Extension marketplaces | - | UI | - | same as #874 |
| 878 | COMP.ext.s | VS Code Marketplace, Open VSX | - | UI | - | same as #874 |
| 879 | COMP.ext.short | Extension marketplaces | - | UI | - | same as #874 |
| 880 | COMP.web.t | Web, issues and docs | - | UI | - | same as #874 |
| 881 | COMP.web.s | Pages, PRs, tickets, READMEs | - | UI | - | same as #874 |
| 882 | COMP.web.short | Web and issues | - | UI | - | same as #874 |
| 883 | COMP.addon.t | Agent add-ons | - | UI | - | same as #874 |
| 884 | COMP.addon.s | MCP registries, plugins, skills | - | UI | - | same as #874 |
| 885 | COMP.pkg.t | Package registries | - | UI | - | same as #874 |
| 886 | COMP.pkg.s | npm, PyPI and others | - | UI | - | same as #874 |
| 887 | COMP.vscode.t | VS Code | - | UI | - | same as #874 |
| 888 | COMP.vscode.s | Trust, settings, tasks | - | UI | - | same as #874 |
| 889 | COMP.exth.t | Extensions | - | UI | - | same as #874 |
| 890 | COMP.exth.s | Host runs as the user | vsc-ers | OK | - | Extension host has the same permissions as VS Code. |
| 891 | COMP.instr.t | Instruction files | - | UI | - | Diagram labels. |
| 892 | COMP.instr.s | AGENTS.md, CLAUDE.md | - | UI | - | same as #891 |
| 893 | COMP.browser.t | Browser profile | - | UI | - | same as #891 |
| 894 | COMP.browser.s | Signed-in sessions | - | UI | - | same as #891 |
| 895 | COMP.agent.t | Agent harness | - | UI | - | same as #891 |
| 896 | COMP.agent.s | Copilot, Claude Code, Codex and others | - | UI | - | same as #891 |
| 897 | COMP.agent.s2 | Model loop, tool calls, approvals, permission modes | - | UI | - | same as #891 |
| 898 | COMP.term.t | Terminal and git CLI | - | UI | - | same as #891 |
| 899 | COMP.term.s | Shell, git, npm, pip: run as the user | vsc-sec | OK | - | VS Code: development tasks "operate with the same permissions as the user". |
| 900 | COMP.term.short | Terminal and git | - | UI | - | Diagram labels. |
| 901 | COMP.svc.t | Local services | - | UI | - | same as #900 |
| 902 | COMP.svc.s | Docker, sockets | - | UI | - | same as #900 |
| 903 | COMP.svc.short | Local services | - | UI | - | same as #900 |
| 904 | COMP.mcp.t | MCP servers (local) | - | UI | - | same as #900 |
| 905 | COMP.mcp.s | stdio or local HTTP | mcp-tr | OK | - | MCP local transports are stdio and Streamable HTTP. |
| 906 | COMP.mcp.short | MCP servers | - | UI | - | Diagram labels. |
| 907 | COMP.files.t | Workspace files | - | UI | - | same as #906 |
| 908 | COMP.files.s | .vscode, .git/config, .env | - | UI | - | same as #906 |
| 909 | COMP.creds.t | Credentials | - | UI | - | same as #906 |
| 910 | COMP.creds.s | SSH, git, gh, az, npm tokens | - | UI | - | same as #906 |
| 911 | COMP.adata.t | Agent local data | - | UI | - | same as #906 |
| 912 | COMP.adata.s | Tokens, transcripts, MCP config | - | UI | - | same as #906 |
| 913 | COMP.egress.t | Egress boundary (conceptual) | - | UI | - | same as #906 |
| 914 | COMP.egress.vert | EGRESS | - | UI | - | same as #906 |
| 915 | COMP.egress.short | Egress | - | UI | - | same as #906 |
| 916 | COMP.llm.t | Model providers | - | UI | - | same as #906 |
| 917 | COMP.llm.s | Requests, context, tool output | - | UI | - | same as #906 |
| 918 | COMP.code.t | Code host and CI | - | UI | - | same as #906 |
| 919 | COMP.code.s | Push, pull requests, Actions | - | UI | - | same as #906 |
| 920 | COMP.cloud.t | Cloud and SaaS | - | UI | - | same as #906 |
| 921 | COMP.cloud.s | Azure, M365, MCP-linked apps | - | UI | - | same as #906 |
| 922 | COMP.mcpr.t | Remote MCP servers | - | UI | - | same as #906 |
| 923 | COMP.mcpr.s | HTTP, run by a supplier or you | mcp-tr | OK | - | Remote servers use HTTP. |
| 924 | COMP.mcpr.short | Remote MCP | - | UI | - | Diagram labels. |
| 925 | COMP.inet.t | Any internet domain | - | UI | - | same as #924 |
| 926 | COMP.inet.s | Exfiltration, C2 servers | - | UI | - | same as #924 |
| 927 | COMP.inet.short | Internet | - | UI | - | same as #924 |
| 928 | COMP.policy.t | Device policy (MDM) | - | UI | - | same as #924 |
| 929 | COMP.policy.s | VS Code policies, agent managed settings, Intune | - | UI | - | same as #924 |
| 930 | COMP.policy.short | Device policy | - | UI | - | same as #924 |
| 931 | COMP.edr.t | Endpoint detection | - | UI | - | same as #924 |
| 932 | COMP.edr.s | Defender for Endpoint: process and file events | mde | OK | - | Defender for Endpoint advanced hunting has process events (DeviceProcessEvents) and file events tables. |
| 933 | COMP.tele.t | Agent telemetry and SOC | - | UI | - | Diagram label. |
| 934 | COMP.tele.s | OpenTelemetry, hooks, SIEM, response | cc-setref, vsc-pol | OK | - | Claude Code settings list OTEL\_ exporter variables; Copilot has an OpenTelemetry export policy. Both have hooks. |
| 935 | COMP.tele.short | Agent telemetry | - | UI | - | Diagram labels and arrow labels. What each arrow claims is checked in the map notes above. |

### ARROWS

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 936 | ARROWS M240 160 H296 | open | - | UI | - | same as #935 |
| 937 | ARROWS M240 248 H270 V188 H296 | install | - | UI | - | same as #935 |
| 938 | ARROWS M240 316 H296 | read | - | UI | - | same as #935 |
| 939 | ARROWS M240 424 H276 V328 H296 | add | - | UI | - | same as #935 |
| 940 | ARROWS M240 512 H268 V444 H296 | fetch | - | UI | - | same as #935 |
| 941 | ARROWS M366 204 V240 | hosts | - | UI | - | same as #935 |
| 942 | ARROWS M522 204 V240 | tools | - | UI | - | same as #935 |
| 943 | ARROWS M679 204 V240 | instructions | - | UI | - | same as #935 |
| 944 | ARROWS M836 204 V240 | pages | - | UI | - | same as #935 |
| 945 | ARROWS M443 336 V380 | runs | - | UI | - | same as #935 |
| 946 | ARROWS M818 336 V380 | starts | - | UI | - | same as #935 |
| 947 | ARROWS M872 380 V336 | output | - | UI | - | same as #935 |
| 948 | ARROWS M638 336 V380 | reaches | - | UI | - | same as #935 |
| 949 | ARROWS M556 336 V492 | read, edit | - | UI | - | same as #935 |
| 950 | ARROWS M720 336 V492 | read, edit | - | UI | - | same as #935 |
| 951 | ARROWS M520 460 V492 | writes | - | UI | - | same as #935 |
| 952 | ARROWS M389 460 V492 | reads | - | UI | - | same as #935 |
| 953 | ARROWS M806 460 V492 | tokens | - | UI | - | same as #935 |
| 954 | ARROWS M536 460 V478 H944 | direct network | - | UI | - | same as #935 |
| 955 | ARROWS M560 124 V114 H948 V124 | extension traffic | - | UI | - | same as #935 |
| 956 | ARROWS M312 124 V102 H957 V124 | tunnel: commands come back in | - | UI | - | same as #935 |

### SHORT

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 957 | SHORT.D11 | Required review for what merges, and a separate CI boundary for what runs. | - | OK | - | Short versions of the D11 to D17 controls; each restates a checked row (554-557, 561, 568-569, 573-575, 578, 584, 590). |
| 958 | SHORT.D12 | Keep production credentials off developer machines. | - | OK | - | same as #957 |
| 959 | SHORT.D13 | Dev Tunnels policies on Windows, and alerts on code tunnel processes. | - | OK | - | same as #957 |
| 960 | SHORT.D14 | Turn off unneeded memory, block standalone customisations, and separately restrict plugins and marketplaces. | - | OK | - | same as #957 |
| 961 | SHORT.D15 | Decide session sync, GitHub environments and Claude Code remote control by policy. | - | OK | - | same as #957 |
| 962 | SHORT.D16 | Limit browser tools and the domains they can reach. | - | OK | - | same as #957 |
| 963 | SHORT.D17 | Capture metadata by default, and content only where the SIEM is approved for it. | - | OK | - | same as #957 |

### DIAGRAM

| # | Where | Statement | Evidence | Verdict | Pass | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 964 | svgText L1150 | SANDBOX, IF ENABLED | - | UI | - | Diagram label. |

## Change log

Every sentence this check changed, pass by pass. `-` is the old sentence, `+` the new one. Passes 1 and 2 are taken from the edit scripts; passes 3 to 8 from a diff of the saved copy of the page before and after each pass.

### Pass 1: first corrections

- `-` and its 2026 variants install a payload into every editor on the machine, VS Code included.
  `+` and its 2026 variants also install themselves into other editors on the machine, such as VS Code, Cursor and Windsurf.
- `-` GlassWorm's 2026 variants install into every editor on the machine.
  `+` GlassWorm's 2026 variants also install into other editors, such as VS Code, Cursor and Windsurf.
- `-` in several of the six affected agents the approval named a harmless file instead.
  `+` in Claude Code and Augment the approval named a harmless file, and in Windsurf and Amazon Q the write happened before the prompt.
- `-` In July 2026 researchers found one CLI agent uploading whole Git repositories to the vendor's storage.
  `+` In July 2026 a researcher found xAI's Grok Build CLI uploading whole Git repositories, history included, to xAI's storage.
- `-` GitSpawn by Manifold Security, versions and mitigations; also reports the Grok Build repo upload finding.
  `+` GitSpawn by Manifold Security, versions and mitigations.
- `-` Gen Digital's figure counts users, not detections.
  `+` Gen Digital's figures count protected users with detections, not confirmed infections.
- `-` a developer with local admin rights can edit a file-based policy.
  `+` a developer with local admin rights can edit the managed policy itself.
- `-` Read(./.env) covers the project root only, so add rules for nested files and for ~/.ssh and cloud credential folders.
  `+` Read(./.env) blocks only the .env in the folder Claude Code started in; Read(.env) also blocks every .env below it. Add rules for ~/.ssh and cloud credential folders too.
- `-` Read(./.env) covers the project root only.
  `+` Read(./.env) blocks only the .env in the start folder; Read(.env) blocks every .env below it.
- `-` writes limited to the workspace; it does not limit reads, and
  `+` writes limited to the workspace; it does not limit reads by default, and
- `-` Forever Security found that the settings Codex changed in its Downloads test persist through ~/.codex/config.toml , so the user's sessions across projects ran the attacker's command whatever project was open. The write-up speaks of every Codex session on the machine; this page says the user's sessions because the file is user-level.
  `+` In the case Forever Security reported, the planted file targeted Codex's own config, which applies in every project the user opens; Forever advises checking ~/.codex/config.toml for unfamiliar entries.
- `-` "Git behaviour in throwaway repos on Git 2.43.0, re-run 29 October 2026:
  `+` "Git behaviour in throwaway repos, run 29 October 2026 on Git 2.43.0 and re-run 1 November 2026 on Git 2.54.0:
- `-` No product enforcement tests were run in this correction pass."]}
  `+` No product enforcement tests were run in this correction pass.", "Fact check, 1 November 2026: each statement rechecked against its source; GitHub's sandbox.userPolicy keys confirmed; D03, D04, D07, D08, D09 and D10, the response section, two map notes, one review note and one source note corrected or tightened; a Grok Build source added."]}
- `-` , "The GitHub keys sandbox.userPolicy.filesystem.deniedPaths and sandbox.userPolicy.network.allowOutbound could not be re-confirmed in the second pass, because the page text was cut off."]}
  `+` ]}
- `-` Facts checked 29 Oct 2026; six corrections 30 Oct 2026
  `+` Facts checked 29 Oct 2026; corrections 30 Oct and 1 Nov 2026
- `-` Current as of 29 October 2026
  `+` Current as of 1 November 2026
- `-` The Git behaviour they flagged was re-run on 29 October 2026; see Evidence status.
  `+` The Git behaviour they flagged was re-run on 29 October and 1 November 2026; see Evidence status.
- `-` Dates in brackets are the page's own publication or update date.
  `+` The 1 November fact check rechecked statements against these sources and added the Grok Build source. Dates in brackets are the page's own publication or update date.
- `-` The git commands were re-run on 29 October 2026 on Git 2.43.0 in throwaway repos,
  `+` The git commands were re-run on 29 October 2026 on Git 2.43.0 and on 1 November 2026 on Git 2.54.0 in throwaway repos,
- `-` Unrelated unresolved findings remain open.
  `+` Unrelated unresolved findings remain open. Fact check, 1 November 2026 Each statement was checked against its source. These were wrong or too broad and were changed: GlassWorm spreads to other editors such as VS Code, Cursor and Windsurf, not every editor (D03); the GhostApproval prompt named a harmless file in Claude Code and Augment, and the write came first in Windsurf and Amazon Q (D08); the repo upload was Grok Build, found by one researcher (D10); a local admin can edit any managed policy, not only a file (D09); Read(./.env) is anchored to the start folder (D04); Codex leaves reads open by default (D07); Gen Digital counts protected users with detections; and the Forever Security persistence claim now says only what Forever reported. The Git tests were re-run on Git 2.54.0 with the same results. No product enforcement tests were run. One claim could not be checked: the planted AGENTS.md found on a real machine in October 2026 (map note, D05).

### Pass 2: second corrections and first shortening

- `-` In October 2026 Forever Security found a planted AGENTS.md in a customer's Downloads folder
  `+` In October 2026 Forever Security reported a planted AGENTS.md in a customer's Downloads folder
- `-` A planted AGENTS.md in Downloads was found on a real machine in October 2026.
  `+` Forever Security reported a planted AGENTS.md in a customer's Downloads folder in October 2026.
- `-` In the case Forever Security reported, the planted file targeted Codex's own config, which applies in every project the user opens; Forever advises checking ~/.codex/config.toml for unfamiliar entries.
  `+` In Forever Security's case Codex first changed its own settings, which then applied to every later Codex session in any project.
- `-` Read(./.env) blocks only the .env in the folder Claude Code started in; Read(.env) also blocks every .env below it. Add rules for ~/.ssh and cloud credential folders too.
  `+` Read(./.env) matches only the start folder; use Read(.env) for any depth, and add rules for ~/.ssh and cloud credential folders.
- `-` Read(./.env) blocks only the .env in the start folder; Read(.env) blocks every .env below it.
  `+` Read(./.env) matches only the start folder; Read(.env) matches any depth.
- `-` used symlinks in a repo to make agents write outside the project, for example to ~/.ssh/authorized\_keys ; in Claude Code and Augment the approval named a harmless file, and in Windsurf and Amazon Q the write happened before the prompt. Cursor was also affected. Anthropic disputed that it is a vulnerability.
  `+` used symlinks in a repo to make six agents write outside the project, for example to ~/.ssh/authorized\_keys ; in some, the prompt named a harmless file or came after the write. Anthropic disputed that it is a vulnerability.
- `-` In July 2026 a researcher found xAI's Grok Build CLI uploading whole Git repositories, history included, to xAI's storage.
  `+` In July 2026 a researcher found Grok Build CLI uploading whole Git repositories to xAI's storage.
- `-` and its 2026 variants also install themselves into other editors on the machine, such as VS Code, Cursor and Windsurf.
  `+` and its 2026 variants also install into other editors, such as VS Code, Cursor and Windsurf.
- `-` "Fact check, 1 November 2026: each statement rechecked against its source; GitHub's sandbox.userPolicy keys confirmed; D03, D04, D07, D08, D09 and D10, the response section, two map notes, one review note and one source note corrected or tightened; a Grok Build source added."
  `+` "Fact check, 1 November 2026: statements rechecked against their sources and Git re-run on 2.54.0. GitHub's sandbox.userPolicy keys confirmed. D03 to D05, D07 to D10, the response section and some notes corrected or shortened. Grok Build and Antiy CERT sources added."
- `-` added the Grok Build source.
  `+` added the Grok Build and Antiy CERT sources.
- `-` Each statement was checked against its source. These were wrong or too broad and were changed: GlassWorm spreads to other editors such as VS Code, Cursor and Windsurf, not every editor (D03); the GhostApproval prompt named a harmless file in Claude Code and Augment, and the write came first in Windsurf and Amazon Q (D08); the repo upload was Grok Build, found by one researcher (D10); a local admin can edit any managed policy, not only a file (D09); Read(./.env) is anchored to the start folder (D04); Codex leaves reads open by default (D07); Gen Digital counts protected users with detections; and the Forever Security persistence claim now says only what Forever reported. The Git tests were re-run on Git 2.54.0 with the same results. No product enforcement tests were run. One claim could not be checked: the planted AGENTS.md found on a real machine in October 2026 (map note, D05).
  `+` Statements were checked against their sources. Changed: GlassWorm reaches other editors, not every editor (D03); Read(./.env) matches only the start folder (D04); the planted AGENTS.md was reported in October, with no find date given (D05); Codex leaves reads open by default (D07); GhostApproval's misleading prompts hit some agents, not all (D08); a local admin can edit any managed policy (D09); the repo upload was Grok Build (D10); Gen Digital counts protected users with detections; ClawHavoc's ClawHub count now cites Antiy CERT. The Git tests were re-run on Git 2.54.0 with the same results. No product enforcement tests were run.
- `-` If the plugin's repo has a branch named after the pinned hash set as its default, Git can check out that branch instead; Gemini CLI had a related FETCH\_HEAD variant. The attack needs control of the repo of a plugin you already installed, a routine-looking update so the marketplace re-pins to a new hash, and a Git host that accepts hash-shaped branch names. CSA notes that limiting plugins to hosts that reject such names would still exclude self-hosted Git servers and Bitbucket, which the agents support, and would not help against the Gemini CLI FETCH\_HEAD variant. Where automatic updates were enabled for the plugin's marketplace, no click was needed after that. CSA reports that automatic plugin updates were on by default in both Claude Code and Codex, which made the attack zero-click. Claude Code's current documentation turns automatic updates on for most official Anthropic marketplaces (not all) and for marketplaces added from claude.ai, and leaves them off for every other marketplace, third-party ones included [contested] , so current defaults may differ from those in the affected versions. The Codex default was not checked against OpenAI's documentation [unverified] .
  `+` A default branch named after the pinned hash could be checked out instead; Gemini CLI had a related FETCH\_HEAD variant. The attack needs control of a plugin repo you already installed, an update that re-pins it, and a Git host that accepts hash-shaped branch names. CSA reports that automatic plugin updates were on by default in Claude Code and Codex, which made it zero-click. Claude Code's current documentation leaves them off for third-party marketplaces, so current defaults may differ from the affected versions.
- `-` According to OpenAI, an empty mcp\_servers table disables all MCP servers; how that treats plugin-bundled servers was not confirmed [unverified] . Servers bundled with a plugin use a separate table, plugins.&lt;plugin&gt;.mcp\_servers.&lt;server&gt; , so list those too. For plugin sources, OpenAI documents [marketplaces] restrict\_to\_allowed\_sources = true with marketplaces.allowed\_sources rules in requirements.toml . These rules restrict local and Git marketplace sources in supported local clients, including OpenAI-curated Git catalogs. OpenAI distinguishes bundled plugins and remotely installed workspace plugins from the curated Git source policy; do not assume that a marketplace allowlist governs every plugin route. Check the separate plugin controls and test each route used in your deployment.
  `+` An empty mcp\_servers table disables all MCP servers. Plugin-bundled servers use a separate table, plugins.&lt;plugin&gt;.mcp\_servers.&lt;server&gt; , so list those too. For plugin sources, use [marketplaces] restrict\_to\_allowed\_sources = true with marketplaces.allowed\_sources . It covers local and Git marketplace sources; bundled and remotely installed workspace plugins have separate controls, so test each route you use.
- `-` Plugin4Shell needed no click where automatic updates were enabled for the plugin's marketplace. Claude Code's defaults differ by marketplace; the Codex behaviour comes from secondary sources [unverified].
  `+` Plugin4Shell needed no click where automatic plugin updates were on. Current defaults differ by product and marketplace.

### Pass 3: shortening of long paragraphs

33 changed items. Words in those items: 3,912 before, 2,931 after.

**page text** (50 -> 42 words)

- `-` Everything on the laptop starts with the developer's rights: VS Code, extensions, agents, MCP servers, install scripts.
- `-` A sandbox or per-tool permission can narrow what one of them reaches, but only where it is switched on and covers that tool.
- `-` Anything outside those limits can read what the developer can.
- `+` Everything on the laptop starts with the developer's rights: VS Code, extensions, agents, MCP servers and install scripts.
- `+` A sandbox or per-tool permission narrows that only where it is on and covers the tool.
- `+` Everything else can read what the developer can.

**page text** (60 -> 54 words)

- `-` D01 to D10 are the top 10, coloured by the status you set under Top 10 (what OK means is defined there).
- `+` D01 to D10 are the top 10, coloured by the status you set under Top 10.

**page text** (239 -> 138 words)

- `-` Traffic leaves through the egress boundary to outbound services (3).
- `-` The egress boundary is conceptual: it is only a control point where traffic is actually forced through a proxy or gateway.
- `-` Dashed two-way lines show connections that start outbound but carry commands back in.
- `+` Traffic leaves through the egress boundary (3), which is a control point only where traffic is forced through a proxy or gateway.
- `-` Solid arrows from the agent straight down to workspace files and agent local data are its own Read and Edit tools, which sit outside the shell sandbox.
- `-` Local services (Docker and other sockets, localhost ports) can reach past the sandbox.
- `-` Remote MCP servers send results back into the agent and can act on downstream SaaS, and may be run by a supplier or by your own organisation.
- `-` Their tokens are separate from the agent's: authorisation to the server and the server's authorisation to downstream SaaS both need checking (D06).
- `-` The browser profile holds signed-in sessions, a source of authority separate from files and CLI credentials, and sits outside the shell sandbox [inference].
- `-` Shell commands also reach local services directly.
- `-` Arrows show selected paths, not every data flow: model responses and browser traffic are drawn without labels for space.
- `-` Select a marker to see why the risk sits there, or a box to see all its risks.
- `-` Dashed markers D11 to D17 are the further risks listed below the map.
- `+` Dashed two-way lines start outbound but carry commands back in.
- `+` Solid arrows from the agent to workspace files and agent local data are its own Read and Edit tools, outside the shell sandbox.
- `+` Local services such as the Docker socket can reach past the sandbox.
- `+` The browser profile holds signed-in sessions outside the shell sandbox [inference].
- `+` A remote MCP server can act on the SaaS behind it with its own tokens (D06).
- `+` Arrows show selected paths, not every data flow.
- `+` Select a marker or a box to see its risks.

**page text** (62 -> 52 words)

- `-` Open a risk for its description and the first control to put in place.
- `-` For D01 to D10 the first control and its friction come from Where to start under Top 10, suggested by the endpoint reviewer.
- `+` Open a risk for its description and first control.
- `+` For D01 to D10 the first control and its friction come from Where to start under Top 10.

**page text** (59 -> 47 words)

- `-` This is a reference layout, not your organisation's actual setup.
- `-` Common differences: agents running only in the terminal without VS Code, dev containers or cloud sessions for all agent work, an internal package proxy, and VS Code forks such as Cursor or Windsurf next to VS Code.
- `-` Draw your own variant and move the markers to where they belong.
- `+` This is a reference layout, not your organisation's setup.
- `+` Common differences: agents used only in the terminal, all agent work in dev containers or cloud sessions, an internal package proxy, and VS Code forks such as Cursor or Windsurf.
- `+` Draw your own variant and move the markers.

**page text** (120 -> 97 words)

- `-` A proposed priority order, not a measured ranking.
- `-` It weighs how often each risk appears in the 2025 and 2026 reporting cited here against how far the damage reaches, without an incident dataset or scoring method.
- `-` Before you rely on the order, score likelihood, impact, exposure and confidence separately for your own fleet.
- `+` A proposed priority order, not a measured ranking: it weighs how often each risk appears in the 2025 and 2026 reporting cited here against how far the damage reaches.
- `+` Score likelihood, impact, exposure and confidence for your own fleet before you rely on it.
- `-` VS Code tunnels (D13, under More risks on the Risk map) have been used in real attacks and are the strongest candidate to move up.
- `-` The order and the mapping to OWASP IDs are my judgement.
- `-` [inference] Set a status per risk as you work.
- `-` It is stored only in this browser.
- `+` VS Code tunnels (D13, under More risks) have been used in real attacks and are the strongest candidate to move up.
- `+` The order and the OWASP mapping are my judgement.
- `+` [inference] Status is stored only in this browser.

**page text** (60 -> 58 words)

- `-` GitSpawn: at publication on 1 September 2026, four of eight findings across seven agents were unpatched, including a second path in Claude Code still open on 2.1.252.
- `-` It needs a repo that arrives as files with its.git folder intact; a normal clone does not carry it.
- `-` Setting core.fsmonitor to false globally does not help, because a repo's own config wins.
- `+` GitSpawn: at publication on 1 September 2026, four of eight findings across seven agents were unpatched, including a second Claude Code path still open on 2.1.252.
- `+` It needs a repo that arrives as files with its.git folder; a normal clone does not carry it.
- `+` A global core.fsmonitor of false does not help, because the repo's own config wins.

**page text** (105 -> 83 words)

- `-` OK means the control is in place and was tested for a named product (for example VS Code, Claude Code, Codex or Copilot) on a named operating system, with the evidence and the assessment date written down.
- `-` One green status can hide different coverage across tools and platforms, so record those details beside it; this page stores only the status.
- `-` Partial means some products, platforms or users are covered.
- `-` Missing means the control is not in place.
- `-` Unknown means it was looked at but could not be confirmed.
- `-` Not assessed means nobody has looked yet.
- `-` These definitions are mine, not taken from a framework.
- `+` OK: the control is in place and was tested for a named product (such as VS Code, Claude Code, Codex or Copilot) on a named operating system, with evidence and a date written down.
- `+` One green status can hide different coverage across tools, so record those details elsewhere; this page stores only the status.
- `+` Partial: some products, platforms or users are covered.
- `+` Missing: not in place.
- `+` Unknown: looked at but not confirmed.
- `+` Not assessed: nobody has looked yet.
- `+` These definitions are mine.

**page text** (92 -> 73 words)

- `-` ChainDrop (Microsoft, 4 August 2026) spread through more than 400 npm packages via a preinstall script, stole npm, GitHub and cloud credentials, and republished packages with the stolen tokens.
- `-` Some copies carried valid provenance because they were published from a real CI workflow, so provenance alone does not prove a package is safe.
- `-` In August 2025 the s1ngularity malware, already running through an install script, drove locally installed AI CLIs with their permission checks switched off to search the disk for secrets.
- `+` ChainDrop (Microsoft, 4 August 2026) used a preinstall script in more than 400 npm packages to steal npm, GitHub and cloud credentials and republish packages.
- `+` Some copies had valid provenance from a real CI workflow, so provenance alone does not prove safety.
- `+` In August 2025 the s1ngularity malware ran installed AI CLIs with their permission checks off to search the disk for secrets.

**page text** (274 -> 179 words)

- `-` Do any projects bypass or widen script approval? dangerously-allow-all-scripts runs every dependency install script, whether approved, denied or unreviewed, and npm calls it a migration escape hatch only.
- `-` Review existing allowScripts grants in package.json and.npmrc, since a repo can carry its own grants [inference].
- `+` Do any projects bypass or widen script approval? dangerously-allow-all-scripts runs every dependency install script; npm calls it a migration escape hatch only.
- `+` Review allowScripts grants in package.json and.npmrc, since a repo can carry its own [inference].
- `-` Is project code that runs outside script approval reviewed?
- `-` A root.npm-extension.mjs or.npm-extension.cjs is imported and run by npm install before dependencies resolve; npm ci only checks its recorded hash against the lockfile.
- `-` It may change only the dependency fields of third-party manifests, but its code still runs on the developer's machine. npm documents ignore-extension to skip it, says ignore-scripts implies it, and honours extension-file only from project or command-line config.
- `-` The documentation does not say whether script approval covers the file; approval governs dependency lifecycle scripts, so treat it as uncovered [inference].
- `+` Is project code that runs outside script approval reviewed? npm install runs a root.npm-extension.mjs or.npm-extension.cjs before dependencies resolve; npm ci only checks its recorded hash. ignore-extension or ignore-scripts skips it.
- `+` The docs do not say whether script approval covers it, so treat it as uncovered [inference].
- `-` Is there a cooldown before new versions install?
- `-` Set min-release-age in a managed npmrc as a default, but do not treat it as enforcement. npm applies the command line first, then environment variables, then the project, user and global files, so a flag, an environment variable or a project.npmrc can set a different value.
- `-` Where the cooldown must hold, enforce it at the registry or in a package firewall (GitHub's is in public preview, npm only).
- `+` Is there a cooldown before new versions install? min-release-age in a managed npmrc is only a default: a command-line flag, an environment variable or a project.npmrc overrides it.
- `+` To enforce it, use the registry or a package firewall (GitHub's is in public preview, npm only).
- `-` A cooldown can delay them: when it blocks the fix that npm audit fix would install, npm keeps the vulnerable version and warns. min-release-age-exclude exempts named packages.
- `-` Agree who may grant an exception, and record it and when it ends.
- `+` If a cooldown blocks the fix npm audit fix would install, npm keeps the vulnerable version and warns. min-release-age-exclude exempts named packages.
- `+` Agree who grants exceptions and for how long.

**page text** (163 -> 94 words)

- `-` Many files in a project can name a program to run.
- `-` Two delivery routes matter.
- `-` Tracked files survive a normal clone:.vscode/tasks.json, workspace settings,.devcontainer/devcontainer.json (its initializeCommand runs on the host) and agent project files such as.claude/settings.json and.mcp.json, and for npm projects a root.npm-extension.mjs or.npm-extension.cjs, which npm install runs.
- `-` North Korea's Contagious Interview campaign sends developers fake coding tests whose tasks.json runs on folder open.
- `-` The repo's own.git/config and hooks do not survive a clone; they arrive only when the project is passed on as files with.git inside, such as a zip, shared drive or sync folder.
- `-` That is the GitSpawn route (September 2026): eight findings across seven agents where background Git calls ran a command named in the repo's Git config, in some cases before the trust prompt.
- `-` Most used core.fsmonitor; Claude Code's ultrareview path used another setting, and the Codex variant differed somewhat in mechanism.
- `-` Worms such as ChainDrop push tracked config files into other repos, so the next clone carries the trap.
- `+` Many project files can name a program to run.
- `+` These survive a normal clone:.vscode/tasks.json, workspace settings,.devcontainer/devcontainer.json (its initializeCommand runs on the host), agent files such as.claude/settings.json and.mcp.json, and npm's root.npm-extension files.
- `+` North Korea's Contagious Interview campaign sends fake coding tests whose tasks.json runs on folder open.
- `+` A repo's.git/config and hooks do not survive a clone, but arrive when a project is shared as files, such as a zip.
- `+` That is the GitSpawn route (September 2026): in seven agents, background Git calls ran a command from the repo's Git config, sometimes before the trust prompt.

**page text** (93 -> 69 words)

- `-` An extension runs with the developer's rights and can read any file the developer can.
- `-` The threat is not only unknown publishers.
- `+` An extension runs with the developer's rights.
- `-` GlassWorm has hit Open VSX in waves since October 2025, and its 2026 variants also install into other editors, such as VS Code, Cursor and Windsurf.
- `-` VS Code forks such as Cursor, Windsurf and VSCodium use Open VSX by default.
- `+` GlassWorm has hit Open VSX in waves since October 2025, and its 2026 variants also install into VS Code, Cursor and Windsurf.
- `+` Cursor, Windsurf and VSCodium use Open VSX by default.

**page text** (73 -> 57 words)

- `-` It overrides the user's own setting.
- `-` It is not an integrity control: for a local VSIX the rules match the identifiers the package declares, and Microsoft says they do not verify origin, stop changes to installed extension files, or limit runtime permissions.
- `-` Combine it with a private marketplace and file-integrity monitoring of extension folders.
- `-` [inference] for the monitoring.
- `+` It overrides the user setting.
- `+` It is not an integrity control: for a local VSIX, Microsoft says it does not verify origin, stop changes to installed files, or limit runtime permissions.
- `+` Add a private marketplace and file-integrity monitoring of extension folders [inference].

**page text** (104 -> 100 words)

- `-` A developer laptop holds SSH keys, Git, GitHub, Azure and npm tokens,.env files, and now agent tokens and transcripts.
- `-` Any process running as the user can read credential files that are not protected and can use credentials exposed through a helper or agent, and sandboxes do not change that by default: Claude Code's sandbox can read ~/.ssh and ~/.aws unless you deny it, VS Code passes Git and GitHub CLI credentials into its sandbox, and Dev Containers forward the credential helper and SSH agent.
- `+` A developer laptop holds SSH keys, Git, cloud and npm tokens,.env files, and now agent tokens and transcripts.
- `+` Any process running as the user can read unprotected credential files and use credentials exposed through a helper or agent.
- `+` Sandboxes do not change that by default: Claude Code's sandbox can read ~/.ssh and ~/.aws unless you deny it, VS Code passes Git and GitHub CLI credentials into its sandbox, and Dev Containers forward the SSH agent and reuse local Git credentials.

**page text** (29 -> 22 words)

- `-` It writes credentials in plaintext to ~/.git-credentials.
- `-` This shows every scope, including the system scope that Git for Windows uses.
- `+` It saves credentials unencrypted in ~/.git-credentials.
- `+` The command shows every scope, including system.

**page text** (79 -> 57 words)

- `-` A key loaded in an SSH agent can be used without its file being read, so what matters is who can reach the agent socket [inference].
- `-` Where it applies, load keys with ssh-add -t for a maximum lifetime, -c to require confirmation on each use, and -h to limit the destinations a key may be used for (OpenSSH 8.9 or later, enforced only through a cooperating ssh).
- `+` A key in an SSH agent can be used without reading its file, so control who can reach the agent socket [inference].
- `+` Load keys with ssh-add -t (maximum lifetime), -c (confirm each use) and -h (limit destinations; OpenSSH 8.9 or later, needs a cooperating ssh).

**page text** (151 -> 109 words)

- `-` VS Code: chat.tools.edits.autoApprove with "\*\*/.env": false only requires approval before an edit.
- `-` Built-in tools can still read workspace files into context, and terminal commands can read them.
- `-` For Copilot sessions that use the Agent Host, GitHub's enterprise managed settings can block reads with permissions.deny and Read(...) rules (deny wins over ask, and ask over allow).
- `-` Coverage is limited: VS Code applies these rules only to Agent Host sessions, so other harnesses and extensions need their own controls. sandbox.userPolicy.filesystem.deniedPaths is the matching control for subprocesses the agent starts.
- `-` Keep live secrets out of the workspace as well.
- `-` Claude Code: Read(...) deny rules in permissions.deny block the Read tool and are also merged into the sandbox.
- `-` A sandbox.filesystem.denyRead or sandbox.credentials entry alone covers shell commands only, and does not stop the Read tool.
- `-` Read(./.env) matches only the start folder; use Read(.env) for any depth, and add rules for ~/.ssh and cloud credential folders.
- `+` VS Code: chat.tools.edits.autoApprove with "\*\*/.env": false only requires approval before edits; it does not cover reads, and terminal commands can read the file.
- `+` For Copilot Agent Host sessions, GitHub's managed settings can block reads with permissions.deny and Read(...) rules (deny beats ask, ask beats allow); other harnesses and extensions need their own controls. sandbox.userPolicy.filesystem.deniedPaths covers processes the agent starts.
- `+` Keep live secrets out of the workspace.
- `+` Claude Code: Read(...) deny rules in permissions.deny block the Read tool and are merged into the sandbox. sandbox.filesystem.denyRead or sandbox.credentials alone covers shell commands only.
- `+` Read(./.env) matches only the start folder; Read(.env) matches any depth.
- `+` Add rules for ~/.ssh and cloud credential folders.

**page text** (92 -> 82 words)

- `-` Text the agent reads can redirect it: a web page, an issue, a README, a code comment, a file name or the output of an MCP tool.
- `-` Instruction files such as AGENTS.md and CLAUDE.md carry more weight, because agents are built to follow them.
- `+` Text the agent reads can redirect it: a web page, issue, README, code comment, file name or MCP tool output.
- `+` Instruction files such as AGENTS.md and CLAUDE.md carry more weight, because agents load them as instructions.
- `-` Codex treats Downloads as trusted once the user has worked there, and in testing it followed the file in more than 90% of attempts.
- `+` Codex trusts Downloads once the user has worked there, and in testing it followed the file in more than 90% of attempts.

**page text** (232 -> 137 words)

- `-` Add-ons give an agent new tools and new instructions.
- `-` A local MCP server is a program running as the developer, and its tool descriptions go straight into the model's context.
- `-` A remote MCP server, reached over HTTP, runs elsewhere (at a supplier, or in your own organisation), holds its own tokens, and receives whatever the agent sends it, so it is another data recipient.
- `-` Its replies come back into the model's context and can carry prompt injection, and it can act on the SaaS behind it with the tokens it holds.
- `-` Who runs a server is a separate question from where it runs: one your organisation operates still needs these checks.
- `+` Add-ons give an agent new tools and instructions.
- `+` A local MCP server runs as the developer, and its tool descriptions go straight into the model's context.
- `+` A remote MCP server holds its own tokens, sees what the agent sends, can return prompt injection, and can act on the SaaS behind it.
- `-` Plugin4Shell (September 2026) showed that Claude Code, Codex and Copilot ran git checkout for a pinned plugin without checking where the checkout landed.
- `-` A default branch named after the pinned hash could be checked out instead; Gemini CLI had a related FETCH\_HEAD variant.
- `-` The attack needs control of a plugin repo you already installed, an update that re-pins it, and a Git host that accepts hash-shaped branch names.
- `-` CSA reports that automatic plugin updates were on by default in Claude Code and Codex, which made it zero-click.
- `-` Claude Code's current documentation leaves them off for third-party marketplaces, so current defaults may differ from the affected versions.
- `+` In Plugin4Shell (September 2026), Claude Code, Codex and Copilot ran git checkout for a pinned plugin without checking the result, so a branch named after the hash could win.
- `+` It needs control of an installed plugin's repo, an update that re-pins it, and a Git host that allows hash-named branches.
- `+` CSA says automatic updates, then on by default, made it zero-click; Claude Code's current docs leave them off for third-party marketplaces.

**page text** (170 -> 147 words)

- `-` Microsoft's pages disagree on the values: the security page says registryOnly and off, the source code uses none, registry and all.
- `-` [contested] Confirm with Policy Diagnostics.
- `-` ChatMCP does not cover MCP servers the Copilot runtime discovers on its own.
- `+` Microsoft's security page ( registryOnly, off) and source code ( none, registry, all) disagree on the values [contested], so confirm with Policy Diagnostics.
- `+` It does not cover MCP servers the Copilot runtime finds on its own.
- `-` A list with only URL entries blocks every local stdio server, so list the local servers you allow too.
- `-` Codex: an [mcp\_servers. ] allowlist in requirements.toml, matched on identity.command for stdio servers and identity.url for remote ones.
- `-` The plain string form of identity.command does not check arguments; use the structured form to pin them.
- `-` An empty mcp\_servers table disables all MCP servers.
- `-` Plugin-bundled servers use a separate table, plugins. .mcp\_servers. , so list those too.
- `-` For plugin sources, use [marketplaces] restrict\_to\_allowed\_sources = true with marketplaces.allowed\_sources.
- `-` It covers local and Git marketplace sources; bundled and remotely installed workspace plugins have separate controls, so test each route you use.
- `+` A list with only URL entries blocks local stdio servers, so list the ones you allow too.
- `+` Codex: an [mcp\_servers. ] allowlist in requirements.toml, matched on identity.command (stdio) or identity.url (remote).
- `+` The string form of identity.command does not check arguments; use the structured form to pin them.
- `+` An empty mcp\_servers table disables all servers.
- `+` Plugin-bundled servers need plugins. .mcp\_servers. entries.
- `+` For plugin sources, set [marketplaces] restrict\_to\_allowed\_sources = true with marketplaces.allowed\_sources; it covers local and Git sources, while bundled and remotely installed workspace plugins have separate controls.

**page text** (170 -> 109 words)

- `-` Do the MCP servers you or a supplier operate validate token audience and refuse tokens not issued for them?
- `-` The MCP security guidance forbids token passthrough, where a server accepts a client's token and forwards it unchanged to a downstream API, because it can bypass controls, blur audit trails and cause confused-deputy problems.
- `-` Where a server proxies a third-party OAuth service with a static client ID, check that it asks for consent per client before sending the user on.
- `-` An approved URL and short-lived tokens do not address these failures.
- `+` Do MCP servers you or a supplier run check token audience and refuse tokens not issued for them?
- `+` The MCP security guidance forbids token passthrough, where a server forwards a client's token unchanged to a downstream API.
- `+` A server that proxies a third-party OAuth service with a static client ID should ask for consent per client.
- `-` The source is the draft specification page, and the version your clients implement was not compared [may be outdated].
- `-` Do local MCP servers that use HTTP rather than stdio check the Origin header, bind to localhost only, and require authentication?
- `-` The MCP specification says servers must validate Origin and should bind to localhost and authenticate, to stop DNS rebinding and other local callers (specification version 2025-06-18; newer versions were not compared) [may be outdated].
- `+` Source: the draft specification [may be outdated].
- `+` Do local MCP servers that use HTTP check the Origin header, bind to localhost and require authentication?
- `+` The MCP specification (2025-06-18) says servers must validate Origin and should bind to localhost and authenticate, to stop DNS rebinding [may be outdated].

**page text** (180 -> 106 words)

- `-` Defaults differ by product.
- `-` Claude Code's sandbox is off by default, so its shell commands run with the developer's file and network access until it is switched on; it runs on macOS, Linux and WSL2 but not on native Windows.
- `-` Even when it is on, it covers shell commands only: the Read, Edit and WebFetch tools follow permission rules instead, so allowedDomains does not limit WebFetch, and helper processes that Claude Code starts run outside it with full access: command hooks, local MCP servers, plugin monitors, LSP servers, the status line command and apiKeyHelper.
- `-` Codex sandboxes commands by default, with command network off and writes limited to the workspace; it does not limit reads by default, and a config change can turn network on.
- `-` VS Code's agent sandbox leaves outbound network on by default, and on Windows it is experimental and needs a recent Windows 11 build.
- `-` Microsoft states that its sandbox is not a virtual machine or user-account boundary.
- `-` Microsoft describes a dev container as an additional boundary, but by default it receives Git credentials and the SSH agent.
- `+` Claude Code's sandbox is off by default and runs on macOS, Linux and WSL2, not native Windows.
- `+` It covers shell commands only: the Read, Edit and WebFetch tools follow permission rules instead, and hooks, local MCP servers and apiKeyHelper run outside it.
- `+` Codex sandboxes commands by default, with network off and writes limited to the workspace, but reads stay open unless you deny them.
- `+` VS Code's agent sandbox leaves network on by default and is experimental on Windows; Microsoft says it is not a virtual machine or user-account boundary.
- `+` A dev container adds a boundary, but by default it receives Git credentials and the SSH agent.

**page text** (201 -> 140 words)

- `-` VS Code: the sandbox device policies such as ChatAgentSandboxEnabled are deprecated and do not enforce sandboxing for Copilot harness sessions; Microsoft points to the Copilot managed setting sandbox.enabled, which is in preview.
- `+` VS Code: device policies such as ChatAgentSandboxEnabled are deprecated and do not enforce it for Copilot harness sessions; Microsoft points to the Copilot managed setting sandbox.enabled, and says managed sandbox enforcement is in preview.
- `-` What is the effective policy, not only the recommended settings?
- `-` Requiring the sandbox does not lock every exception.
- `-` When it is admin-required (managed settings set allowUnsandboxedCommands to false or enable allowManagedDomainsOnly), Claude Code ignores loosening settings from a repository but still honours them from user settings and --settings.
- `-` Going by Anthropic's description, those sources can then still add excludedCommands, filesystem.allowWrite paths and Unix socket access unless managed settings cover them [inference].
- `+` What is the effective policy?
- `+` When the sandbox is admin-required (managed settings set allowUnsandboxedCommands to false or enable allowManagedDomainsOnly), Claude Code ignores loosening settings from a repository but still honours user settings and --settings.
- `+` Those can then add excludedCommands, write paths and socket access [inference].
- `-` Pin enableWeakerNestedSandbox, enableWeakerNetworkIsolation, network.allowAllUnixSockets and network.allowLocalBinding to false in managed settings [inference], and review the settings in force on a real machine.
- `-` The sandbox isolates shell commands only.
- `-` The helper processes above and the Read, Edit and WebFetch tools sit outside it, and isolating the whole agent process needs something around it, such as a dev container, virtual machine or cloud session [inference].
- `+` Pin enableWeakerNestedSandbox, enableWeakerNetworkIsolation, network.allowAllUnixSockets and network.allowLocalBinding to false [inference].
- `+` To isolate the whole agent, run it in a dev container, virtual machine or cloud session [inference].

**page text** (290 -> 215 words)

- `-` Claude Code: sandbox.network.allowedDomains with allowManagedDomainsOnly for shell commands.
- `-` Separately review WebFetch(domain:...) permission rules for the WebFetch tool.
- `-` Entries in permissions.allow pre-approve matching fetches; they do not prohibit every other destination.
- `-` Unmatched requests follow the remaining rules and permission mode, and may still be approved.
- `-` Test that behaviour explicitly.
- `-` Where destinations must be prohibited, use an enforced control that covers WebFetch traffic or disable the tool; an approval list alone is not a network allowlist.
- `-` VS Code: sandbox.userPolicy.network.allowOutbound for commands; ChatAgentNetworkFilter covers the fetch tool and the integrated browser, not terminal commands.
- `-` Codex: [experimental\_network] in requirements.toml for command traffic, which needs enabled = true because domain rules alone do not turn the proxy on, and which OpenAI marks experimental with limited Windows support; web search, MCP and apps have separate controls.
- `+` Claude Code: sandbox.network.allowedDomains with allowManagedDomainsOnly covers shell commands.
- `+` WebFetch(domain:...) rules in permissions.allow only pre-approve fetches; other requests can still be approved, so they are not a network allowlist.
- `+` To block destinations, use an enforced control or disable WebFetch.
- `+` VS Code: sandbox.userPolicy.network.allowOutbound for commands; ChatAgentNetworkFilter for the fetch tool and the integrated browser.
- `+` Codex: [experimental\_network] in requirements.toml for commands, with enabled = true, since domain rules alone do not turn it on; it is experimental with limited Windows support.
- `+` Web search, MCP and apps have separate controls.
- `-` An allowed service such as github.com can receive data into an attacker-controlled account.
- `-` Anthropic's documentation warns that broad domains create exfiltration paths and that a hostname-only decision, made without inspecting TLS, can be bypassed, for example by domain fronting; it points to a custom proxy that inspects traffic for stronger guarantees.
- `-` Keep the list short, and where the service offers it restrict by account, tenant or operation as well as by domain.
- `+` An allowed service such as github.com can receive data into an attacker's account.
- `+` Anthropic warns that broad domains create exfiltration paths and that hostname-only filtering without TLS inspection can be bypassed, for example by domain fronting.
- `+` Keep the list short, and restrict by account, tenant or operation where the service allows it.
- `-` Docker sockets, other Unix sockets and unauthenticated localhost services can give a command capabilities well beyond what file and domain rules suggest.
- `-` Anthropic documents the Docker socket and Unix sockets as ways around its sandbox, and has settings such as sandbox.network.allowAllUnixSockets and, on macOS, sandbox.network.allowLocalBinding that widen this.
- `-` Keep the Docker socket out of agent sessions, leave those settings off, and put authentication on local services.
- `+` Docker sockets, other Unix sockets and unauthenticated localhost services can give a command far more power than file and domain rules suggest.
- `+` Anthropic documents the Docker socket and Unix sockets as ways around its sandbox.
- `+` Keep the Docker socket out of agent sessions, leave sandbox.network.allowAllUnixSockets and allowLocalBinding (macOS) off, and require authentication on local services.

**page text** (93 -> 82 words)

- `-` Approval prompts are the main brake on an agent.
- `-` They fail when developers switch them off (Allow all, Autopilot, bypass modes), when a project file switches them off, or when the prompt shows something other than what happens.
- `-` CVE-2025-53773 let a prompt injection make Copilot write "chat.tools.autoApprove": true into the workspace settings.
- `-` GhostApproval (Wiz, July 2026) used symlinks in a repo to make six agents write outside the project, for example to ~/.ssh/authorized\_keys; in some, the prompt named a harmless file or came after the write.
- `+` Approval prompts fail when developers switch them off (Allow all, Autopilot, bypass modes), when a project file switches them off, or when the prompt shows something other than what happens.
- `+` CVE-2025-53773 let a prompt injection make Copilot write "chat.tools.autoApprove": true into workspace settings.
- `+` GhostApproval (Wiz, July 2026) used repo symlinks to make six agents write outside the project, such as to ~/.ssh/authorized\_keys; in some, the prompt named a harmless file or came after the write.

**page text** (72 -> 57 words)

- `-` ChatToolsEligibleForAutoApproval can require approval for tools such as execute/runInTerminal or web/fetch, but it does not stop Assisted permissions or approvals saved earlier in a Copilot harness session.
- `+` ChatToolsEligibleForAutoApproval can require approval for named tools, but it does not stop Assisted permissions or approvals saved earlier in a Copilot harness session.
- `-` Anthropic's current settings reference explicitly accepts disableAutoMode both at top level and under permissions.
- `-` Use one documented form consistently and verify enforcement on the deployed version.
- `+` Anthropic's settings reference also accepts disableAutoMode at top level.
- `+` Check enforcement on the deployed version.

**page text** (72 -> 40 words)

- `-` Codex: on-request does not by itself mean a person decides.
- `-` With automatic review ( approvals\_reviewer = "auto\_review"), a reviewer can evaluate escalation requests instead.
- `-` If you require human approval, also constrain allowed\_approvals\_reviewers in requirements.toml.
- `-` OpenAI explicitly documents "user" as the manual-approval reviewer.
- `-` Set allowed\_approvals\_reviewers = ["user"] to allow only that reviewer.
- `-` This controls who reviews approval requests, not whether every action needs approval.
- `-` Verify enforcement on the deployed version [not run here].
- `+` Codex: on-request does not mean a person decides: with approvals\_reviewer = "auto\_review" an automatic reviewer can answer.
- `+` To require a human, set allowed\_approvals\_reviewers = ["user"] in requirements.toml.
- `+` This sets who reviews requests, not which actions need approval.
- `+` [not run here]

**page text** (125 -> 95 words)

- `-` Endpoint detection records the process tree: a Defender process event carries the command line of the process it records and of the process that started it, and the parent's file name and ID but not the parent's command line.
- `-` So it can often show that an agent started a command, but longer chains need correlation across events.
- `-` What it does not record is the task, the prompt, whether the tool call was approved, and which agent session it belongs to.
- `+` A Defender process event records the command line of the new process and of the process that started it, but only the name and ID one level further up, so longer chains need joining across events.
- `+` It does not record the task, the prompt, the approval or the agent session.

**page text** (61 -> 50 words)

- `-` An initial hunting query for Defender advanced hunting, with incomplete coverage [not run here].
- `-` It only matches events where the initiating process or its parent looks like an agent, so processes further down the tree and agents under other names are missed.
- `-` Rebuild the full chain by joining on process IDs and creation times:
- `+` A first Defender advanced hunting query [not run here].
- `+` It matches only events where the initiating process or its parent looks like an agent, so deeper processes and renamed agents are missed.
- `+` Join on process IDs and creation times to rebuild the chain:

**page text** (76 -> 72 words)

- `-` Requests to the model can include code you selected, files the agent read, terminal output, tool results and sometimes secrets.
- `-` The risk lies in where they go: a personal account, a provider without a company agreement, or an own-key model where VS Code says content filtering is not guaranteed.
- `-` With a local model the recipient boundary moves onto the machine.
- `+` Requests to the model can include selected code, files the agent read, terminal output, tool results and sometimes secrets.
- `+` The risk is where they go: a personal account, a provider without a company agreement, or an own-key model, where VS Code says content filtering is not guaranteed.
- `+` With a local model they stay on the machine.

**page text** (68 -> 48 words)

- `-` Is ChatApprovedAccountOrganizations set to the approved GitHub organisations?
- `-` The gate requires a signed-in account whose organisation memberships intersect that list and resolved account-side policy data.
- `-` A personal GitHub account with the required membership can qualify; this does not require a company-managed identity.
- `-` The \* value accepts any signed-in GitHub or GHE account, so do not use it when organisation membership must be restricted.
- `-` Verify company-managed identity requirements separately.
- `+` Is ChatApprovedAccountOrganizations set to your approved GitHub organisations?
- `+` It checks the signed-in account's organisation membership, so a personal account that is a member can qualify; it does not require a company-managed identity. \* accepts any signed-in GitHub or GHE account, so do not use it to restrict membership.

**page text** (116 -> 86 words)

- `-` Copy to storage the user cannot change: agent transcripts and session logs (they age out; Claude Code has cleanupPeriodDays), user and project agent config including MCP config, shell history, the planted or malicious files as found, package artifacts (lockfiles, tarballs, installed copies), and the endpoint and cloud logs for the window (Defender device timeline, code host audit log, cloud and identity sign-in logs).
- `+` Copy to storage the user cannot change: agent transcripts and session logs (they age out; Claude Code has cleanupPeriodDays), user and project agent and MCP config, shell history, the planted files as found, package artifacts (lockfiles, tarballs, installed copies), and endpoint, code host, cloud and identity logs for the window.
- `-` Microsoft's incident-response guidance says to do no harm and not to destroy forensic evidence; without these records the scope of the compromise cannot be established.
- `-` Collect quickly, so it does not delay revoking access.
- `+` Microsoft's incident-response guidance says not to destroy forensic evidence.
- `+` Collect quickly, so revoking access is not delayed.

**page text** (81 -> 134 words)

- `-` Statements were checked against their sources.
- `-` Changed: GlassWorm reaches other editors, not every editor (D03); Read(./.env) matches only the start folder (D04); the planted AGENTS.md was reported in October, with no find date given (D05); Codex leaves reads open by default (D07); GhostApproval's misleading prompts hit some agents, not all (D08); a local admin can edit any managed policy (D09); the repo upload was Grok Build (D10); Gen Digital counts protected users with detections; ClawHavoc's ClawHub count now cites Antiy CERT.
- `+` Statements were checked against their sources, and long ones were shortened.
- `+` Changed: GlassWorm reaches other editors, not every editor (D03); Read(./.env) matches only the start folder (D04); Dev Containers forward the SSH agent and reuse local Git credentials, as Microsoft words it (D04); the planted AGENTS.md was reported in October, with no find date given (D05); Codex leaves reads open by default (D07); VS Code calls managed sandbox enforcement a preview (D07); GhostApproval's misleading prompts hit some agents, not all (D08); a local admin can edit any managed policy (D09); the repo upload was Grok Build (D10); Gen Digital counts protected users with detections; ClawHavoc's ClawHub count now cites Antiy CERT.
- `+` Removed details no source states: that ChatAgentNetworkFilter skips terminal commands (D07), two example tool names (D08), and an unverified Codex update default (D06).

### Pass 4: map notes, More risks and Evidence

29 changed items. Words in those items: 2,994 before, 2,641 after.

**page text** (138 -> 105 words)

- `-` Traffic leaves through the egress boundary (3), which is a control point only where traffic is forced through a proxy or gateway.
- `+` Traffic leaves through the egress boundary (3), a control point only where traffic is forced through a proxy or gateway.
- `-` Dashed two-way lines start outbound but carry commands back in.
- `-` Solid arrows from the agent to workspace files and agent local data are its own Read and Edit tools, outside the shell sandbox.
- `-` Local services such as the Docker socket can reach past the sandbox.
- `-` The browser profile holds signed-in sessions outside the shell sandbox [inference].
- `-` A remote MCP server can act on the SaaS behind it with its own tokens (D06).
- `+` The dashed two-way line starts outbound but carries commands back in.
- `+` The agent's own Read and Edit tools reach workspace files and agent local data outside the shell sandbox, and local services such as the Docker socket can reach past it.

**page text** (97 -> 88 words)

- `-` Score likelihood, impact, exposure and confidence for your own fleet before you rely on it.
- `+` Score your own fleet before you rely on it.
- `-` VS Code tunnels (D13, under More risks) have been used in real attacks and are the strongest candidate to move up.
- `+` VS Code tunnels (D13) have been used in real attacks and are the strongest candidate to move up.

**page text** (94 -> 82 words)

- `-` These survive a normal clone:.vscode/tasks.json, workspace settings,.devcontainer/devcontainer.json (its initializeCommand runs on the host), agent files such as.claude/settings.json and.mcp.json, and npm's root.npm-extension files.
- `-` North Korea's Contagious Interview campaign sends fake coding tests whose tasks.json runs on folder open.
- `-` A repo's.git/config and hooks do not survive a clone, but arrive when a project is shared as files, such as a zip.
- `-` That is the GitSpawn route (September 2026): in seven agents, background Git calls ran a command from the repo's Git config, sometimes before the trust prompt.
- `+` These survive a normal clone:.vscode/tasks.json, workspace settings,.devcontainer/devcontainer.json (its initializeCommand runs on the host),.claude/settings.json,.mcp.json and npm's root.npm-extension files.
- `+` North Korea's Contagious Interview campaign sends fake coding tests whose tasks.json runs on folder open..git/config and hooks do not survive a clone, but arrive when a project is shared as files, such as a zip.
- `+` In GitSpawn (September 2026), background Git calls in seven agents ran a command from that config, sometimes before the trust prompt.

**page text** (100 -> 93 words)

- `-` Sandboxes do not change that by default: Claude Code's sandbox can read ~/.ssh and ~/.aws unless you deny it, VS Code passes Git and GitHub CLI credentials into its sandbox, and Dev Containers forward the SSH agent and reuse local Git credentials.
- `-` Gen Digital reported in September 2026 that several infostealer families now collect AI agent tokens, MCP configuration and prompt histories.
- `+` Sandboxes do not change that by default: Claude Code's sandbox reads ~/.ssh and ~/.aws unless denied, VS Code passes Git and GitHub CLI credentials in, and Dev Containers forward the SSH agent and reuse local Git credentials.
- `+` Gen Digital reported in September 2026 that infostealers now collect AI agent tokens, MCP configuration and prompt histories.

**page text** (66 -> 51 words)

- `-` VS Code: chat.tools.edits.autoApprove with "\*\*/.env": false only requires approval before edits; it does not cover reads, and terminal commands can read the file.
- `-` For Copilot Agent Host sessions, GitHub's managed settings can block reads with permissions.deny and Read(...) rules (deny beats ask, ask beats allow); other harnesses and extensions need their own controls. sandbox.userPolicy.filesystem.deniedPaths covers processes the agent starts.
- `+` VS Code: chat.tools.edits.autoApprove with "\*\*/.env": false only gates edits; reads and terminal commands are not covered.
- `+` GitHub's managed permissions.deny with Read(...) rules blocks reads in Copilot Agent Host sessions only; other harnesses and extensions need their own controls. sandbox.userPolicy.filesystem.deniedPaths covers processes the agent starts.

**page text** (137 -> 126 words)

- `-` Add-ons give an agent new tools and instructions.
- `-` A remote MCP server holds its own tokens, sees what the agent sends, can return prompt injection, and can act on the SaaS behind it.
- `-` The ClawHavoc campaign put more than 1,000 malicious skills on ClawHub in early 2026.
- `+` A remote MCP server holds its own tokens, sees what the agent sends, can return prompt injection and can act on the SaaS behind it.
- `+` ClawHavoc put more than 1,000 malicious skills on ClawHub in early 2026.
- `-` It needs control of an installed plugin's repo, an update that re-pins it, and a Git host that allows hash-named branches.
- `-` CSA says automatic updates, then on by default, made it zero-click; Claude Code's current docs leave them off for third-party marketplaces.
- `+` This needs control of the plugin's repo, an update that re-pins it, and a Git host that allows hash-named branches.
- `+` CSA says automatic updates, then on by default, made it zero-click; Claude Code's docs now leave them off for third-party marketplaces.

**page text** (106 -> 100 words)

- `-` It covers shell commands only: the Read, Edit and WebFetch tools follow permission rules instead, and hooks, local MCP servers and apiKeyHelper run outside it.
- `-` Codex sandboxes commands by default, with network off and writes limited to the workspace, but reads stay open unless you deny them.
- `-` VS Code's agent sandbox leaves network on by default and is experimental on Windows; Microsoft says it is not a virtual machine or user-account boundary.
- `-` A dev container adds a boundary, but by default it receives Git credentials and the SSH agent.
- `+` It covers shell commands only; the Read, Edit and WebFetch tools follow permission rules, and hooks, local MCP servers and apiKeyHelper run outside it.
- `+` Codex sandboxes commands by default (network off, writes limited to the workspace) but leaves reads open unless you deny them.
- `+` VS Code's agent sandbox leaves network on by default, is experimental on Windows, and is not a virtual machine or user-account boundary.
- `+` A dev container adds a boundary, but by default it gets Git credentials and the SSH agent.

**page text** (79 -> 72 words)

- `-` When the sandbox is admin-required (managed settings set allowUnsandboxedCommands to false or enable allowManagedDomainsOnly), Claude Code ignores loosening settings from a repository but still honours user settings and --settings.
- `-` Those can then add excludedCommands, write paths and socket access [inference].
- `-` Anthropic names allowManagedReadPathsOnly and allowManagedDomainsOnly as managed-only locks.
- `+` When the sandbox is admin-required (managed allowUnsandboxedCommands set to false, or allowManagedDomainsOnly on), Claude Code ignores loosening settings from a repository but still honours user settings and --settings, which can add excludedCommands, write paths and socket access [inference].
- `+` Lock with allowManagedReadPathsOnly and allowManagedDomainsOnly.
- `-` To isolate the whole agent, run it in a dev container, virtual machine or cloud session [inference].
- `+` To isolate the whole agent, use a dev container, virtual machine or cloud session [inference].

**page text** (93 -> 78 words)

- `-` WebFetch(domain:...) rules in permissions.allow only pre-approve fetches; other requests can still be approved, so they are not a network allowlist.
- `-` To block destinations, use an enforced control or disable WebFetch.
- `+` WebFetch(domain:...) rules in permissions.allow only pre-approve fetches, so they are not an allowlist; to block destinations, use an enforced control or disable WebFetch.
- `-` Codex: [experimental\_network] in requirements.toml for commands, with enabled = true, since domain rules alone do not turn it on; it is experimental with limited Windows support.
- `+` Codex: [experimental\_network] in requirements.toml for commands, which needs enabled = true; it is experimental, with limited Windows support.

**page text** (95 -> 87 words)

- `-` A Defender process event records the command line of the new process and of the process that started it, but only the name and ID one level further up, so longer chains need joining across events.
- `-` It does not record the task, the prompt, the approval or the agent session.
- `-` Forever Security caught the planted AGENTS.md because it watched the agent, not only the user.
- `+` A Defender process event records the command lines of the new process and of its parent, but only the name and ID of the grandparent, so longer chains need joining across events.
- `+` It does not record the task, prompt, approval or agent session.
- `+` Forever Security caught the planted AGENTS.md by watching the agent, not only the user.

**page text** (86 -> 79 words)

- `-` Copy to storage the user cannot change: agent transcripts and session logs (they age out; Claude Code has cleanupPeriodDays), user and project agent and MCP config, shell history, the planted files as found, package artifacts (lockfiles, tarballs, installed copies), and endpoint, code host, cloud and identity logs for the window.
- `+` Copy to storage the user cannot change: agent transcripts and session logs (they age out; Claude Code has cleanupPeriodDays), agent and MCP config, shell history, the planted files as found, package artifacts, and endpoint, code host, cloud and identity logs for the window.

**page text** (158 -> 141 words)

- `-` Marketplace coverage was unresolved in this round.
- `-` The 30 October source check confirmed the official source-policy documentation and its distinction between curated Git sources, bundled plugins and remotely installed workspace plugins; D06 now states that scope.
- `+` The 30 October check confirmed that OpenAI documents separate rules for Git marketplace sources, bundled plugins and workspace plugins.

**page text** (134 -> 169 words)

- `-` Changed: GlassWorm reaches other editors, not every editor (D03); Read(./.env) matches only the start folder (D04); Dev Containers forward the SSH agent and reuse local Git credentials, as Microsoft words it (D04); the planted AGENTS.md was reported in October, with no find date given (D05); Codex leaves reads open by default (D07); VS Code calls managed sandbox enforcement a preview (D07); GhostApproval's misleading prompts hit some agents, not all (D08); a local admin can edit any managed policy (D09); the repo upload was Grok Build (D10); Gen Digital counts protected users with detections; ClawHavoc's ClawHub count now cites Antiy CERT.
- `-` Removed details no source states: that ChatAgentNetworkFilter skips terminal commands (D07), two example tool names (D08), and an unverified Codex update default (D06).
- `+` Changed:
- `+` D03: GlassWorm reaches other editors, not every editor.
- `+` D04: Read(./.env) matches only the start folder; Dev Containers reuse local Git credentials and forward the SSH agent, as Microsoft words it.
- `+` D05: the planted AGENTS.md was reported in October; no find date is given.
- `+` D07: Codex leaves reads open by default; VS Code calls managed sandbox enforcement a preview.
- `+` D08: GhostApproval's misleading prompts hit some agents, not all.
- `+` D09: a local admin can edit any managed policy.
- `+` D10: the repo upload was Grok Build.
- `+` Map notes: background Git calls are GitSpawn, not Check Point; the MCP spec says servers must check Origin and should bind to localhost and authenticate; VS Code has an MCP allowlist but no plugin marketplace lock.
- `+` Review and sources: Gen Digital counts protected users with detections; ClawHavoc's ClawHub count cites Antiy CERT.
- `+` Removed, since no source states them: that ChatAgentNetworkFilter skips terminal commands, two example tool names (D08) and a Codex update default (D06).

**MORE[0]** (250 -> 156 words)

- `-` {"id": "D11", "t": "Agent changes reach shared repos and pipelines unchecked", "d": "The agent pushes, opens pull requests or triggers workflows with the developer's identity, through git or a GitHub MCP server.
- `-` Branch protection governs what merges, not what runs: workflows can run on a push, pull request or manual or API trigger before anything merges, so required review does not protect every CI secret or deployment identity.
- `+` {"id": "D11", "t": "Agent changes reach shared repos and pipelines unchecked", "d": "The agent pushes, opens pull requests or starts workflows with the developer's identity, through git or a GitHub MCP server.
- `+` Branch protection governs what merges, not what runs: workflows can run before anything merges.
- `-` The agent can also write code that looks plausible but adds a vulnerability, weakens authorisation or alters tests so that a defect stays hidden, with no workstation compromise involved.
- `-` GitHub's guidance says generated code can look valid while being wrong, and that automated security checks supplement human review rather than replace it.
- `-` The examples of weakened authorisation and altered tests are [inference].", "l": "m", "c": "Branch protection with required review, and narrowly scoped tokens, for what merges.
- `-` Add a separate CI boundary for what runs: least-privilege GITHUB\_TOKEN permissions, protected deployment environments with required reviewers, CODEOWNERS on workflow files, and ephemeral runners.
- `-` Ask rules such as Bash(git push \*) slow this down but are not a boundary: Claude Code notes that git -C . push does not match them.
- `-` For the code itself, require independent human review of agent-written changes, run security testing as a merge gate (static analysis, dependency and secret scanning), and check that agent-written or agent-changed tests still fail when the behaviour they cover breaks.
- `+` The agent can also write plausible code that is wrong or unsafe; GitHub says generated code can look valid while being wrong.", "l": "m", "c": "Required review and narrowly scoped tokens for what merges.
- `+` For what runs: least-privilege GITHUB\_TOKEN permissions, protected deployment environments with required reviewers, CODEOWNERS on workflow files and ephemeral runners.
- `+` Ask rules such as Bash(git push \*) are not a boundary: Claude Code notes that git -C . push does not match them.
- `+` Review agent-written changes, gate merges on security scans, and check that changed tests still fail when the behaviour breaks.

**MORE[3]** (84 -> 76 words)

- `-` AST01 describes skills that write into an agent's identity file.", "l": "m", "c": "Turn agent memory off where it is not needed (Claude Code autoMemoryEnabled).
- `-` Block standalone customisations with VS Code ChatStrictPluginOnlyCustomization or Claude Code strictPluginOnlyCustomization, while recognising that plugin customisations remain eligible.
- `-` Separately restrict permitted plugins and marketplaces; Anthropic recommends combining its setting with strictKnownMarketplaces.
- `-` Plugin-only does not mean centrally managed only."}
- `+` AST01 describes skills that write into an agent's identity file.", "l": "m", "c": "Turn off agent memory where it is not needed (Claude Code autoMemoryEnabled).
- `+` Block standalone customisations with ChatStrictPluginOnlyCustomization (VS Code) or strictPluginOnlyCustomization (Claude Code).
- `+` Customisations from plugins are still allowed, so also restrict plugins and marketplaces; Anthropic recommends pairing its setting with strictKnownMarketplaces."}

**MORE[5]** (123 -> 101 words)

- `-` In Forever Security's customer telemetry about a quarter of agent sessions open a browser (its customers, not a general sample), and it describes the agent as both target and weapon.
- `-` A browser that is already signed in also lets the agent act in those web apps as the user: read, post, approve or change settings.
- `+` In Forever Security's customer telemetry, about a quarter of agent sessions open a browser.
- `+` A browser that is already signed in also lets the agent act in those web apps as the user.

**PERSONAS[1]** (177 -> 174 words)

- `-` Now marked contested.", "ChatAgentNetworkFilter covers the fetch tool and the integrated browser, not terminal commands.
- `+` Now marked contested.", "ChatAgentNetworkFilter covers the fetch tool and the integrated browser.

**EVIDENCE[0]** (331 -> 304 words)

- `-` {"h": "Verified here", "i": ["Setting and policy names against the VS Code and Claude Code docs, both updated in October 2026.", "Git behaviour in throwaway repos, run 29 October 2026 on Git 2.43.0 and re-run 1 November 2026 on Git 2.54.0: a repo's own core.fsmonitor overrides the global value; the environment override and git -c both block it; a normal clone carries no config or hooks but keeps tracked .vscode files; a copied folder with .git runs the command.", "npm 12.0.0 was released on 8 July 2026, 12.2.1 is current, and npm 12 needs Node.js 22.22.2, 24.15.0 or 26 (npm registry).", "Incidents and CVEs against the vendor advisory or the original research where one was available.", "Codex sandbox defaults and requirements.toml keys, VS Code automatic tasks and VSIX allowlist behaviour, GitHub code-owner enforcement, Claude Code sandbox scope and Defender process columns, against the vendor docs on 29 October 2026.
- `-` In the audit round: GitHub Copilot managed permissions, GitHub Actions secure use, npm config precedence, the MCP transport security warning (version 2025-06-18), Claude Code plugin update defaults, Codex automatic review and Microsoft incident-response guidance.", "Second pass, 29 October 2026: npm 12 extension and script-approval settings, Claude Code sandbox helper processes and admin-required behaviour, Codex mcp\_servers tables and approval reviewers, MCP security best practices (draft), ssh-add options, OWASP MCP Top 10 names, GitHub generated-code guidance, VS Code policy names, Claude Code and Codex key names, and the Plugin4Shell, GitSpawn and ChainDrop figures, each against the page named in Sources.", "Source corrections, 30 October 2026: six findings checked against current Microsoft policy, Anthropic settings and permissions, and OpenAI managed-configuration documentation.
- `+` {"h": "Verified here", "i": ["Setting and policy names against the VS Code and Claude Code docs, both updated in October 2026.", "Git behaviour in throwaway repos, run 29 October 2026 on Git 2.43.0 and re-run 1 November 2026 on Git 2.54.0: a repo's own core.fsmonitor overrides the global value; the environment override and git -c both block it; a normal clone carries no config or hooks but keeps tracked .vscode files; a copied folder with .git runs the command.", "npm 12.0.0 was released on 8 July 2026, 12.2.1 is current, and npm 12 needs Node.js 22.22.2, 24.15.0 or 26 (npm registry).", "Incidents and CVEs against the vendor advisory or the original research where one was available.", "Against vendor docs on 29 October 2026: Codex sandbox defaults and requirements.toml keys, VS Code automatic tasks and VSIX allowlists, GitHub code-owner rules, Claude Code sandbox scope and Defender process columns.
- `+` In the audit round: Copilot managed permissions, Actions secure use, npm config precedence, MCP transport security (2025-06-18), Claude Code plugin update defaults, Codex automatic review and Microsoft incident-response guidance.", "Second pass, 29 October 2026: npm 12 script approval, Claude Code sandbox helpers, Codex mcp\_servers tables and approval reviewers, MCP security best practices (draft), ssh-add options, OWASP MCP Top 10 names, GitHub generated-code guidance, VS Code, Claude Code and Codex setting names, and the Plugin4Shell, GitSpawn and ChainDrop figures.", "Source corrections, 30 October 2026: six findings checked against current Microsoft policy, Anthropic settings and permissions, and OpenAI managed-configuration documentation.
- `-` No product enforcement tests were run in this correction pass.", "Fact check, 1 November 2026: statements rechecked against their sources and Git re-run on 2.54.0.
- `+` No product enforcement tests were run in this correction pass.", "Fact check, 1 November 2026: D01 to D10, the response section, map notes and source notes rechecked, then corrected or shortened.
- `+` Git re-run on 2.54.0.
- `-` D03 to D05, D07 to D10, the response section and some notes corrected or shortened.

**EVIDENCE[2]** (177 -> 158 words)

- `-` No source says.", "Copilot's Plugin4Shell status after September 2026.", "The npm, VS Code, PowerShell and Defender hunting commands were not run on a managed machine.", "How an empty Codex mcp\_servers table treats plugin-bundled servers in the deployed client was not tested.
- `-` Marketplace source restrictions are officially documented, with bundled plugins and remotely installed workspace plugins distinguished from the curated Git source policy; verify the separate controls for each route in use.", "Whether npm script approval covers the root .npm-extension file.
- `+` No source says.", "Copilot's Plugin4Shell status after September 2026.", "The npm, VS Code, PowerShell and Defender hunting commands were not run on a managed machine.", "How an empty Codex mcp\_servers table treats plugin-bundled servers was not tested.
- `+` OpenAI documents separate controls for bundled, workspace and Git-sourced plugins; check each route in use.", "Whether npm script approval covers the root .npm-extension file.

**SOURCES[29]** (40 -> 44 words)

- `-` Windows 11 requirements, default network, credential pass-through, preview status."}
- `+` Windows 11 requirements, default network, credential pass-through, managed enforcement in preview."}
- `-` Dev Containers copy .gitconfig and forward credential helper and SSH agent."}
- `+` Dev Containers copy .gitconfig, reuse local Git credentials and forward the SSH agent."}

**PLACE[5]** (42 -> 35 words)

- `-` Archives, shared drives and sync folders keep .git/config and hooks intact; a normal clone does not, but tracked .vscode and .claude files survive it."]
- `+` They keep .git/config and hooks; a normal clone drops those but keeps tracked .vscode and .claude files."]

**PLACE[9]** (26 -> 34 words)

- `-` ["D02", "agent", "Several agents ran repo-supplied commands from background Git calls before or without the trust prompt (GitSpawn, and the Check Point findings in Claude Code)."]
- `+` ["D02", "agent", "GitSpawn: background Git calls in several agents ran a command from the repo's Git config, sometimes before the trust prompt.
- `+` Separately, Check Point found Claude Code running project config before trust (CVE-2025-59536)."]

**PLACE[16]** (15 -> 16 words)

- `-` ["D04", "adata", "Infostealers now collect agent tokens, MCP configuration and transcripts (Gen Digital, September 2026)."]
- `+` ["D04", "adata", "Infostealers now collect agent tokens, MCP configuration and prompt histories (Gen Digital, September 2026)."]

**PLACE[27]** (37 -> 22 words)

- `-` Their tool descriptions enter the model context, where poisoned text acts as instructions.
- `-` A local server that speaks HTTP must also validate Origin, bind to localhost and authenticate."]
- `+` Their tool descriptions enter the model context, where poisoned text acts as instructions."]

**PLACE[29]** (126 -> 120 words)

- `-` ["D06", "cloud", "MCP servers hold tokens for SaaS and cloud, and a remote server can act on that downstream SaaS for the agent.
- `-` A bad server reaches well beyond the laptop.
- `-` Authorisation to the server and the server's authorisation downstream are separate checks (token audience, no token passthrough)."]
- `-` ["D06", "mcpr", "Remote MCP servers are reached over HTTP and can be run by a supplier or by your own organisation.
- `-` Either way they hold their own tokens, receive whatever the agent sends, and return results into the model context.
- `-` Allowlist them by URL identity.
- `-` They should accept only tokens issued for them and never pass a client's token on downstream."]
- `-` ["D06", "policy", "VS Code and Claude Code both support an MCP allowlist and a fixed plugin marketplace."]
- `+` ["D06", "cloud", "MCP servers hold tokens for SaaS and cloud, so a bad server reaches well beyond the laptop.
- `+` Access to the server and the server's access downstream are separate checks (token audience, no token passthrough)."]
- `+` ["D06", "mcpr", "Remote MCP servers, run by a supplier or your own organisation, hold their own tokens, receive what the agent sends and return results into the model context.
- `+` Allowlist them by URL.
- `+` The MCP spec says they must accept only tokens issued for them and must not pass a client's token downstream."]
- `+` ["D06", "policy", "VS Code, Claude Code and Codex each support an MCP allowlist.
- `+` Claude Code and Codex can also restrict plugin marketplace sources; VS Code can set which plugins are enabled."]

**PLACE[33]** (45 -> 34 words)

- `-` ["D07", "agent", "Claude Code's sandbox covers shell commands.
- `-` The Read, Edit and WebFetch tools follow permission rules instead, so sandbox limits do not cover them.
- `-` WebFetch allow rules pre-approve matching requests; unmatched destinations are governed by other rules and the permission mode, not automatically blocked."]
- `+` ["D07", "agent", "Claude Code's sandbox covers shell commands only.
- `+` Read, Edit and WebFetch follow permission rules instead.
- `+` A WebFetch allow rule pre-approves matching requests; others fall to the permission mode, not an automatic block."]

**PLACE[36]** (48 -> 36 words)

- `-` ["D07", "svc", "Docker sockets, other Unix sockets and unauthenticated localhost services can give a command capabilities beyond what file and domain rules suggest.
- `-` Anthropic documents the Docker socket and Unix sockets as ways around the sandbox.
- `-` Shell commands reach local services directly (see the arrow from the terminal)."]
- `+` ["D07", "svc", "Docker sockets, other Unix sockets and unauthenticated localhost services can give a command more reach than file and domain rules suggest.
- `+` Anthropic names the Docker socket and Unix sockets as ways around the sandbox."]

**PLACE[44]** (45 -> 31 words)

- `-` ["D09", "edr", "Endpoint detection records process events with the command lines of the created and initiating process (not of the initiating process's parent).
- `-` That often shows an agent started a command, but not the prompt, task or approval behind it, and longer chains need correlation."]
- `+` ["D09", "edr", "Defender records the command lines of a new process and of its parent.
- `+` That shows an agent started a command, but not the prompt, task or approval behind it."]

**PLACE[76]** (45 -> 29 words)

- `-` A profile that is already signed in carries the user's sessions, a source of authority separate from files and CLI credentials, and the agent reaches it through tools that sit outside the shell sandbox.
- `+` A signed-in profile carries the user's web sessions, which the agent reaches through tools outside the shell sandbox.

### Pass 5: shortening and stale review notes

24 changed items. Words in those items: 1,917 before, 1,699 after.

**page text** (105 -> 75 words)

- `-` The agent's own Read and Edit tools reach workspace files and agent local data outside the shell sandbox, and local services such as the Docker socket can reach past it.

**page text** (88 -> 76 words)

- `-` A proposed priority order, not a measured ranking: it weighs how often each risk appears in the 2025 and 2026 reporting cited here against how far the damage reaches.
- `-` Score your own fleet before you rely on it.
- `+` A proposed priority order, not a measured ranking.
- `+` It weighs how often each risk appears in the reporting cited here against how far the damage reaches.

**page text** (83 -> 64 words)

- `-` OK: the control is in place and was tested for a named product (such as VS Code, Claude Code, Codex or Copilot) on a named operating system, with evidence and a date written down.
- `-` One green status can hide different coverage across tools, so record those details elsewhere; this page stores only the status.
- `+` OK: the control is in place and was tested for a named product on a named operating system, with evidence and a date written down.
- `+` Record those details elsewhere; this page stores only the status.

**page text** (73 -> 69 words)

- `-` ChainDrop (Microsoft, 4 August 2026) used a preinstall script in more than 400 npm packages to steal npm, GitHub and cloud credentials and republish packages.
- `+` ChainDrop (Microsoft, 4 August 2026) used a preinstall script in more than 400 npm packages to steal credentials and republish packages.

**page text** (82 -> 75 words)

- `-` Many project files can name a program to run.
- `-` These survive a normal clone:.vscode/tasks.json, workspace settings,.devcontainer/devcontainer.json (its initializeCommand runs on the host),.claude/settings.json,.mcp.json and npm's root.npm-extension files.
- `-` North Korea's Contagious Interview campaign sends fake coding tests whose tasks.json runs on folder open..git/config and hooks do not survive a clone, but arrive when a project is shared as files, such as a zip.
- `+` Project files that survive a clone can name a program to run:.vscode/tasks.json, workspace settings,.devcontainer/devcontainer.json (its initializeCommand runs on the host),.claude/settings.json,.mcp.json and npm's root.npm-extension files.
- `+` North Korea's Contagious Interview campaign sends fake coding tests whose tasks.json runs on folder open..git/config and hooks arrive only when a project is shared as files, such as a zip.

**page text** (93 -> 86 words)

- `-` Gen Digital reported in September 2026 that infostealers now collect AI agent tokens, MCP configuration and prompt histories.
- `+` Infostealers now collect AI agent tokens too (Gen Digital, September 2026).

**page text** (57 -> 51 words)

- `-` A key in an SSH agent can be used without reading its file, so control who can reach the agent socket [inference].
- `-` Load keys with ssh-add -t (maximum lifetime), -c (confirm each use) and -h (limit destinations; OpenSSH 8.9 or later, needs a cooperating ssh).
- `+` A key in an SSH agent can be used without its file, so control who can reach the agent socket [inference].
- `+` Load keys with ssh-add -t (lifetime), -c (confirm each use) and -h (limit destinations; OpenSSH 8.9 or later).

**page text** (51 -> 30 words)

- `-` VS Code: chat.tools.edits.autoApprove with "\*\*/.env": false only gates edits; reads and terminal commands are not covered.
- `-` GitHub's managed permissions.deny with Read(...) rules blocks reads in Copilot Agent Host sessions only; other harnesses and extensions need their own controls. sandbox.userPolicy.filesystem.deniedPaths covers processes the agent starts.
- `-` Keep live secrets out of the workspace.
- `+` VS Code: chat.tools.edits.autoApprove with "\*\*/.env": false only gates edits.
- `+` GitHub's managed permissions.deny with Read(...) rules blocks reads, but only in Copilot Agent Host sessions. sandbox.userPolicy.filesystem.deniedPaths covers processes the agent starts.

**page text** (82 -> 71 words)

- `-` Instruction files such as AGENTS.md and CLAUDE.md carry more weight, because agents load them as instructions.
- `+` Agents load instruction files such as AGENTS.md and CLAUDE.md as instructions, so these carry more weight.
- `-` Codex trusts Downloads once the user has worked there, and in testing it followed the file in more than 90% of attempts.
- `+` In testing, Codex followed it in more than 90% of attempts.

**page text** (126 -> 118 words)

- `-` A remote MCP server holds its own tokens, sees what the agent sends, can return prompt injection and can act on the SaaS behind it.
- `+` A remote one holds its own tokens, sees what the agent sends and can return prompt injection.
- `-` This needs control of the plugin's repo, an update that re-pins it, and a Git host that allows hash-named branches.
- `+` It needs control of the plugin's repo, an update that re-pins it, and a Git host that allows hash-named branches.

**page text** (54 -> 46 words)

- `-` Microsoft's security page ( registryOnly, off) and source code ( none, registry, all) disagree on the values [contested], so confirm with Policy Diagnostics.
- `+` Microsoft's docs and source code disagree on its values [contested], so confirm with Policy Diagnostics.

**page text** (67 -> 52 words)

- `-` Codex: an [mcp\_servers. ] allowlist in requirements.toml, matched on identity.command (stdio) or identity.url (remote).
- `-` The string form of identity.command does not check arguments; use the structured form to pin them.
- `+` Codex: an [mcp\_servers. ] allowlist in requirements.toml, matched on identity.command (stdio) or identity.url (remote); use the structured command form to pin arguments.
- `-` For plugin sources, set [marketplaces] restrict\_to\_allowed\_sources = true with marketplaces.allowed\_sources; it covers local and Git sources, while bundled and remotely installed workspace plugins have separate controls.
- `+` For plugin sources, set [marketplaces] restrict\_to\_allowed\_sources = true with marketplaces.allowed\_sources; bundled and remotely installed workspace plugins have separate controls.

**page text** (69 -> 55 words)

- `-` Do MCP servers you or a supplier run check token audience and refuse tokens not issued for them?
- `-` The MCP security guidance forbids token passthrough, where a server forwards a client's token unchanged to a downstream API.
- `-` A server that proxies a third-party OAuth service with a static client ID should ask for consent per client.
- `-` For third-party servers, ask the supplier.
- `+` Do MCP servers you or a supplier run refuse tokens not issued for them?
- `+` The MCP security guidance forbids token passthrough: forwarding a client's token unchanged to a downstream API.
- `+` A proxy server with a static client ID for a third-party OAuth service should get consent per client.

**page text** (100 -> 91 words)

- `-` Claude Code's sandbox is off by default and runs on macOS, Linux and WSL2, not native Windows.
- `-` It covers shell commands only; the Read, Edit and WebFetch tools follow permission rules, and hooks, local MCP servers and apiKeyHelper run outside it.
- `-` Codex sandboxes commands by default (network off, writes limited to the workspace) but leaves reads open unless you deny them.
- `+` Claude Code's sandbox is off by default and does not run on native Windows.
- `+` It covers shell commands only; hooks, local MCP servers and apiKeyHelper run outside it, and the Read, Edit and WebFetch tools follow permission rules instead.
- `+` Codex sandboxes commands by default (network off, writes limited to the workspace) but by default leaves reads open.
- `-` A dev container adds a boundary, but by default it gets Git credentials and the SSH agent.
- `+` A dev container gets Git credentials and the SSH agent by default.

**page text** (133 -> 92 words)

- `-` VS Code: device policies such as ChatAgentSandboxEnabled are deprecated and do not enforce it for Copilot harness sessions; Microsoft points to the Copilot managed setting sandbox.enabled, and says managed sandbox enforcement is in preview.
- `-` Claude Code: sandbox.enabled, failIfUnavailable and allowUnsandboxedCommands: false.
- `-` With failIfUnavailable, Claude Code refuses to start where the sandbox cannot run, such as native Windows.
- `+` VS Code: ChatAgentSandboxEnabled is deprecated; Microsoft points to the Copilot managed setting sandbox.enabled and calls managed enforcement a preview.
- `+` Claude Code: sandbox.enabled, failIfUnavailable (refuse to start where the sandbox cannot run, such as native Windows) and allowUnsandboxedCommands: false.
- `-` When the sandbox is admin-required (managed allowUnsandboxedCommands set to false, or allowManagedDomainsOnly on), Claude Code ignores loosening settings from a repository but still honours user settings and --settings, which can add excludedCommands, write paths and socket access [inference].
- `-` Lock with allowManagedReadPathsOnly and allowManagedDomainsOnly.
- `-` Pin enableWeakerNestedSandbox, enableWeakerNetworkIsolation, network.allowAllUnixSockets and network.allowLocalBinding to false [inference].
- `-` To isolate the whole agent, use a dev container, virtual machine or cloud session [inference].
- `+` When the sandbox is admin-required, Claude Code ignores loosening settings from a repository but still honours user settings and --settings, which can add excludedCommands, write paths and socket access [inference].
- `+` Lock with allowManagedReadPathsOnly and allowManagedDomainsOnly, and pin enableWeakerNestedSandbox, enableWeakerNetworkIsolation, network.allowAllUnixSockets and network.allowLocalBinding to false [inference].

**page text** (78 -> 60 words)

- `-` Claude Code: sandbox.network.allowedDomains with allowManagedDomainsOnly covers shell commands.
- `-` WebFetch(domain:...) rules in permissions.allow only pre-approve fetches, so they are not an allowlist; to block destinations, use an enforced control or disable WebFetch.
- `-` VS Code: sandbox.userPolicy.network.allowOutbound for commands; ChatAgentNetworkFilter for the fetch tool and the integrated browser.
- `-` Codex: [experimental\_network] in requirements.toml for commands, which needs enabled = true; it is experimental, with limited Windows support.
- `+` Claude Code: sandbox.network.allowedDomains with allowManagedDomainsOnly covers shell commands; WebFetch(domain:...) allow rules only pre-approve fetches and are not an allowlist.
- `+` VS Code: sandbox.userPolicy.network.allowOutbound for commands, ChatAgentNetworkFilter for the fetch tool and integrated browser.
- `+` Codex: [experimental\_network] in requirements.toml for commands, with enabled = true; limited Windows support.

**page text** (62 -> 61 words)

- `-` Docker sockets, other Unix sockets and unauthenticated localhost services can give a command far more power than file and domain rules suggest.
- `-` Anthropic documents the Docker socket and Unix sockets as ways around its sandbox.
- `+` Docker and other Unix sockets and unauthenticated localhost services can give a command more power than file and domain rules suggest; Anthropic names the Docker socket and Unix sockets as ways around its sandbox.

**page text** (82 -> 79 words)

- `-` Approval prompts fail when developers switch them off (Allow all, Autopilot, bypass modes), when a project file switches them off, or when the prompt shows something other than what happens.
- `+` Approval prompts fail when they are switched off (Allow all, Autopilot, bypass modes, or a project file), or when the prompt shows something other than what happens.

**page text** (87 -> 77 words)

- `-` A Defender process event records the command lines of the new process and of its parent, but only the name and ID of the grandparent, so longer chains need joining across events.
- `+` A Defender process event records the command lines of the new process and its parent, but only the grandparent's name and ID.
- `-` Policies can also fail quietly: VS Code ignores a policy value with a syntax error.
- `+` VS Code ignores a policy value with a syntax error, so policies can fail quietly.

**page text** (72 -> 63 words)

- `-` With a local model they stay on the machine.

**page text** (124 -> 122 words)

- `-` The Codex side rests on secondary sources and is marked [unverified], as are the defaults in the affected versions.
- `+` The Codex side rested on secondary sources and was marked unverified; the 1 November check removed it.

**page text** (70 -> 79 words)

- `-` The caption now says the arrows show selected paths, not every data flow, and separates authorisation to a remote MCP server from the server's authorisation to downstream SaaS.
- `+` The caption said the arrows show selected paths, not every data flow, and separated access to a remote MCP server from its access to downstream SaaS.
- `+` The second point is now in the remote MCP map note.

**page text** (79 -> 87 words)

- `-` Marked contested, and the "GitHub only" remark was replaced with CSA's actual wording.
- `+` It was marked contested, and the "GitHub only" remark was replaced with CSA's wording.
- `+` D06 now attributes the default to CSA.

**page text** (0 -> 20 words)

- `+` Long paragraphs were shortened, and past review notes that no longer match the page were put in the past tense.

### Pass 6: split long lists, trim data notes

20 changed items. Words in those items: 1,891 before, 1,807 after.

**page text** (43 -> 43 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (82 -> 82 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (62 -> 62 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (68 -> 68 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (63 -> 63 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (60 -> 60 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (61 -> 61 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (49 -> 49 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (140 -> 129 words)

- `-` Added allowed\_approvals\_reviewers; the value ["user"] was initially marked as inferred.
- `-` The 30 October source check confirmed that OpenAI explicitly documents "user" for manual approval.
- `+` Added allowed\_approvals\_reviewers with ["user"], which OpenAI documents for manual approval (confirmed 30 October).

**page text** (100 -> 100 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (122 -> 115 words)

- `-` D06: plugin updates are automatic only where the marketplace has them on.
- `-` Claude Code defaults differ by marketplace type.
- `-` The Codex side rested on secondary sources and was marked unverified; the 1 November check removed it.
- `+` D06: plugin updates are automatic only where the marketplace has them on, and Claude Code defaults differ by marketplace type.
- `+` The unverified Codex side was removed on 1 November.
- `-` The query now includes copilot and is labelled an initial query with incomplete coverage. "Most 2025 and 2026 incidents" became "Several documented" incidents.
- `+` The query now includes copilot and is labelled an initial query with incomplete coverage.
- `+` "Most 2025 and 2026 incidents" became "Several documented" incidents.

**page text** (141 -> 131 words)

- `-` npm: a root.npm-extension.mjs or.cjs is run by npm install, not by npm ci (npm v12 docs).
- `+` npm: npm install runs a root.npm-extension.mjs or.cjs; npm ci does not (npm v12 docs).
- `-` The docs do not say whether script approval covers the file, so that point is marked inference.
- `+` Whether script approval covers the file is marked inference.

**page text** (79 -> 70 words)

- `-` Added a browser profile box outside the shell sandbox, a terminal to local services arrow, an output arrow from local MCP servers to the agent and a response arrow from model providers.
- `-` The top row was narrowed to fit the browser box.
- `-` The caption said the arrows show selected paths, not every data flow, and separated access to a remote MCP server from its access to downstream SaaS.
- `-` The second point is now in the remote MCP map note.
- `+` Added a browser profile box outside the shell sandbox, and arrows from the terminal to local services, from local MCP servers to the agent and from model providers back.
- `+` The top row was narrowed to fit.
- `+` The caption said arrows show selected paths, not every data flow, and split access to a remote MCP server from its access to downstream SaaS.
- `+` That split is now in the D06 map notes.

**page text** (82 -> 75 words)

- `-` D11 now covers plausible but wrong or insecure agent code, with human review and security testing as gates.
- `-` GitHub's guidance supports the general point; its text did not address agent-written tests, so that check is marked inference.
- `+` D11 now covers plausible but wrong or insecure agent code, gated by human review and security testing.
- `+` GitHub's guidance does not address agent-written tests, so that check is marked inference.

**page text** (87 -> 75 words)

- `-` Plugin4Shell: CSA reports automatic plugin updates on by default in Claude Code and Codex, while Claude Code's current documentation differs by marketplace type.
- `-` It was marked contested, and the "GitHub only" remark was replaced with CSA's wording.
- `-` D06 now attributes the default to CSA.
- `+` Plugin4Shell: CSA reports automatic plugin updates on by default in Claude Code and Codex; Claude Code's docs differ by marketplace type.
- `+` It was marked contested; D06 now attributes the default to CSA.

**page text** (36 -> 34 words)

- `-` Map notes: background Git calls are GitSpawn, not Check Point; the MCP spec says servers must check Origin and should bind to localhost and authenticate; VS Code has an MCP allowlist but no plugin marketplace lock.
- `+` Map notes: background Git calls are GitSpawn, not Check Point; servers must check Origin and should bind to localhost and authenticate (MCP spec); VS Code has an MCP allowlist but no plugin marketplace lock.

**MORE[0]** (156 -> 147 words)

- `-` {"id": "D11", "t": "Agent changes reach shared repos and pipelines unchecked", "d": "The agent pushes, opens pull requests or starts workflows with the developer's identity, through git or a GitHub MCP server.
- `+` {"id": "D11", "t": "Agent changes reach shared repos and pipelines unchecked", "d": "The agent pushes, opens pull requests or starts workflows with the developer's identity.
- `-` The agent can also write plausible code that is wrong or unsafe; GitHub says generated code can look valid while being wrong.", "l": "m", "c": "Required review and narrowly scoped tokens for what merges.
- `-` For what runs: least-privilege GITHUB\_TOKEN permissions, protected deployment environments with required reviewers, CODEOWNERS on workflow files and ephemeral runners.
- `+` The agent can also write plausible code that is wrong or unsafe; GitHub says generated code can look valid while being wrong.", "l": "m", "c": "For what merges: required review and narrowly scoped tokens.
- `+` For what runs: least-privilege GITHUB\_TOKEN permissions, protected environments with required reviewers, CODEOWNERS on workflow files and ephemeral runners.
- `-` Review agent-written changes, gate merges on security scans, and check that changed tests still fail when the behaviour breaks.
- `+` Gate merges on review and security scans, and check that changed tests still fail when the behaviour breaks.

**MORE[2]** (103 -> 96 words)

- `-` Unit 42 reported this from Stately Taurus in 2024, and SentinelLabs in Operation Digital Eye, where the targets were IT service providers.", "l": "h", "c": "On Windows, use the Dev Tunnels policies (Disable Dev Tunnels, or allow only your Entra tenant).
- `+` Unit 42 reported this from Stately Taurus in 2024, and SentinelLabs in Operation Digital Eye.", "l": "h", "c": "On Windows, use the Dev Tunnels policies (Disable Dev Tunnels, or allow only your Entra tenant).

**EVIDENCE[0]** (304 -> 299 words)

- `-` {"h": "Verified here", "i": ["Setting and policy names against the VS Code and Claude Code docs, both updated in October 2026.", "Git behaviour in throwaway repos, run 29 October 2026 on Git 2.43.0 and re-run 1 November 2026 on Git 2.54.0: a repo's own core.fsmonitor overrides the global value; the environment override and git -c both block it; a normal clone carries no config or hooks but keeps tracked .vscode files; a copied folder with .git runs the command.", "npm 12.0.0 was released on 8 July 2026, 12.2.1 is current, and npm 12 needs Node.js 22.22.2, 24.15.0 or 26 (npm registry).", "Incidents and CVEs against the vendor advisory or the original research where one was available.", "Against vendor docs on 29 October 2026: Codex sandbox defaults and requirements.toml keys, VS Code automatic tasks and VSIX allowlists, GitHub code-owner rules, Claude Code sandbox scope and Defender process columns.
- `-` In the audit round: Copilot managed permissions, Actions secure use, npm config precedence, MCP transport security (2025-06-18), Claude Code plugin update defaults, Codex automatic review and Microsoft incident-response guidance.", "Second pass, 29 October 2026: npm 12 script approval, Claude Code sandbox helpers, Codex mcp\_servers tables and approval reviewers, MCP security best practices (draft), ssh-add options, OWASP MCP Top 10 names, GitHub generated-code guidance, VS Code, Claude Code and Codex setting names, and the Plugin4Shell, GitSpawn and ChainDrop figures.", "Source corrections, 30 October 2026: six findings checked against current Microsoft policy, Anthropic settings and permissions, and OpenAI managed-configuration documentation.
- `+` {"h": "Verified here", "i": ["Setting and policy names against the VS Code and Claude Code docs, both updated in October 2026.", "Git behaviour in throwaway repos, run 29 October 2026 on Git 2.43.0 and re-run 1 November 2026 on Git 2.54.0: a repo's own core.fsmonitor overrides the global value; the environment override and git -c both block it; a normal clone carries no config or hooks but keeps tracked .vscode files; a copied folder with .git runs the command.", "npm 12.0.0 was released on 8 July 2026, 12.2.1 is current, and npm 12 needs Node.js 22.22.2, 24.15.0 or 26 (npm registry).", "Incidents and CVEs against the vendor advisory or the original research where one was available.", "Against vendor docs on 29 October 2026: Codex sandbox defaults and requirements.toml keys, VS Code automatic tasks and VSIX allowlists, GitHub code-owner rules, Claude Code sandbox scope and Defender process columns.", "In the audit round: Copilot managed permissions, Actions secure use, npm config precedence, MCP transport security (2025-06-18), Claude Code plugin update defaults, Codex automatic review and Microsoft incident-response guidance.", "Second pass, 29 October 2026: npm 12 script approval, Claude Code sandbox helpers, Codex mcp\_servers tables and approval reviewers, MCP security best practices (draft), ssh-add options, OWASP MCP Top 10 names, GitHub generated-code guidance, VS Code, Claude Code and Codex setting names, and the Plugin4Shell, GitSpawn and ChainDrop figures.", "Source corrections, 30 October 2026: six findings checked against current Microsoft policy, Anthropic settings and permissions, and OpenAI managed-configuration documentation.
- `-` No product enforcement tests were run in this correction pass.", "Fact check, 1 November 2026: D01 to D10, the response section, map notes and source notes rechecked, then corrected or shortened.
- `+` No product enforcement tests were run in this correction pass.", "Fact check, 1 November 2026: every statement rechecked against its source, then corrected, shortened or cut.

**PLACE[30]** (53 -> 48 words)

- `-` ["D06", "mcpr", "Remote MCP servers, run by a supplier or your own organisation, hold their own tokens, receive what the agent sends and return results into the model context.
- `+` ["D06", "mcpr", "Remote MCP servers, whoever runs them, hold their own tokens, receive what the agent sends and return results into the model context.
- `-` The MCP spec says they must accept only tokens issued for them and must not pass a client's token downstream."]
- `+` The MCP spec says they must accept only tokens issued for them and must not pass a client's token on."]

### Pass 7: source list fixes

3 changed items. Words in those items: 49 before, 49 after.

**SOURCES[6]** (15 -> 15 words)

- `-` MCP01 to MCP03."}
- `+` MCP01 to MCP10."}

**SOURCES[21]** (20 -> 20 words)

- `-` {"t": "AI coding agents' 0-click RCE flaw (Plugin4Shell)", "u": "https://www.theregister.com/a/5297335", "n": "The Register (September 2026), on research by AIR Security."}
- `+` {"t": "AI coding agents' 0-click RCE flaw (Plugin4Shell)", "u": "https://www.theregister.com/a/5297335", "n": "The Register (September 2026), on research by Air Security."}

**SOURCES[24]** (14 -> 14 words)

- `-` {"t": "Stealing MCP tokens in Claude Code via ~/.claude.json", "u": "https://www.mitiga.io/blog/claude-code-mcp-token-theft-mitm", "n": "Mitiga (7.5.2026)."}
- `+` {"t": "Stealing MCP tokens in Claude Code via ~/.claude.json", "u": "https://www.mitiga.io/blog/claude-code-mcp-token-theft-mitm", "n": "Mitiga (5.5.2026)."}

### Pass 8: split the last long review sentence into a list

1 changed items. Words in those items: 63 before, 62 after.

**page text** (63 -> 62 words)

- `-` Six findings were corrected against current official documentation: plugin-only settings still permit plugin customisations (D14); the VS Code account gate checks organisation membership, not company ownership (D10); WebFetch approval rules are not a destination allowlist (D07); both disableAutoMode locations are documented (D08); Codex marketplace source restrictions have an official reference with stated scope limits (D06); and the user approval-reviewer value is documented (D08).
- `+` Six findings were corrected against current official documentation:
- `+` D14: plugin-only settings still permit plugin customisations.
- `+` D10: the VS Code account gate checks organisation membership, not company ownership.
- `+` D07: WebFetch approval rules are not a destination allowlist.
- `+` D08: both disableAutoMode locations are documented.
- `+` D06: Codex marketplace source restrictions have an official reference with stated scope limits.
- `+` D08: the user approval-reviewer value is documented.

### Pass 9: paragraph length

21 changed items. Words in those items: 1,574 before, 1,471 after.

**page text** (75 -> 75 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (76 -> 60 words)

- `-` A proposed priority order, not a measured ranking.
- `-` It weighs how often each risk appears in the reporting cited here against how far the damage reaches.
- `+` Proposed, not measured: the order weighs how often each risk appears in the cited reporting against how far the damage reaches.
- `-` VS Code tunnels (D13) have been used in real attacks and are the strongest candidate to move up.
- `-` The order and the OWASP mapping are my judgement.
- `-` [inference] Status is stored only in this browser.
- `+` VS Code tunnels (D13), used in real attacks, are the strongest candidate to move up.
- `+` The order and OWASP mapping are my judgement.
- `+` [inference]

**page text** (64 -> 56 words)

- `-` OK: the control is in place and was tested for a named product on a named operating system, with evidence and a date written down.
- `-` Record those details elsewhere; this page stores only the status.
- `-` Partial: some products, platforms or users are covered.
- `+` OK: in place and tested on a named product and operating system, with evidence and a date recorded elsewhere; this page stores only the status, in this browser.
- `+` Partial: covers some products, platforms or users.

**page text** (69 -> 69 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (75 -> 76 words)

- `-` North Korea's Contagious Interview campaign sends fake coding tests whose tasks.json runs on folder open..git/config and hooks arrive only when a project is shared as files, such as a zip.
- `+` North Korea's Contagious Interview campaign sends fake coding tests whose tasks.json runs on folder open.
- `+` .git/config and hooks arrive only when a project is shared as files, such as a zip.

**page text** (69 -> 69 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (86 -> 86 words)

- `+` Infostealers now collect AI agent tokens too (Gen Digital, September 2026).
- `-` Infostealers now collect AI agent tokens too (Gen Digital, September 2026).

**page text** (71 -> 71 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (118 -> 118 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (91 -> 91 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (60 -> 57 words)

- `-` Is outbound access limited to an allowlist?
- `+` Is outbound access allowlisted?

**page text** (61 -> 57 words)

- `-` Docker and other Unix sockets and unauthenticated localhost services can give a command more power than file and domain rules suggest; Anthropic names the Docker socket and Unix sockets as ways around its sandbox.
- `+` Docker and other Unix sockets and unauthenticated localhost services can give a command more power than file and domain rules suggest; Anthropic names these sockets as ways around its sandbox.

**page text** (79 -> 79 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (77 -> 77 words)

- Same sentences; only split into separate paragraphs or list items.

**page text** (63 -> 59 words)

- `-` Requests to the model can include selected code, files the agent read, terminal output, tool results and sometimes secrets.
- `+` Model requests can include code, files the agent read, terminal output, tool results and sometimes secrets.
- `-` In July 2026 a researcher found Grok Build CLI uploading whole Git repositories to xAI's storage.
- `+` In July 2026 Grok Build CLI was found uploading whole Git repositories to xAI's storage.

**page text** (79 -> 59 words)

- `-` Copy to storage the user cannot change: agent transcripts and session logs (they age out; Claude Code has cleanupPeriodDays), agent and MCP config, shell history, the planted files as found, package artifacts, and endpoint, code host, cloud and identity logs for the window.
- `-` Record who collected what, and when.
- `-` Collect quickly, so revoking access is not delayed.
- `-` [inference] for the list of items.
- `+` Copy to storage the user cannot change: agent transcripts (they age out; see Claude Code's cleanupPeriodDays), agent and MCP config, shell history, planted files, package artifacts, and endpoint, code host, cloud and identity logs.
- `+` [inference] Collect quickly, so revoking access is not delayed.

**page text** (62 -> 57 words)

- `-` The earlier drafts were checked in persona-based review passes, each taking a different role.
- `+` The earlier drafts were checked in persona-based review passes.

**page text** (73 -> 55 words)

- `-` Each was checked against the page named in Sources before the page changed, and all ten changed the content, in full or in narrower form.
- `-` One extra suggestion, a field for product, operating system, version, assessor, evidence and date, was not built: the page already says it stores status only, so that stays a documented limit.
- `-` Points that could not be confirmed are marked in the text.
- `+` Each was checked against its source before the page changed; all ten changed the content, some in narrower form.
- `+` A suggested field for product, operating system, version, assessor, evidence and date was not built: the page stores status only, a documented limit.
- `+` Unconfirmed points are marked in the text.

**page text** (61 -> 58 words)

- `-` The 1 November fact check rechecked statements against these sources and added the Grok Build and Antiy CERT sources.
- `+` The 1 November fact check rechecked statements against them and added Grok Build and Antiy CERT.

**MORE[0]** (147 -> 124 words)

- `-` The agent can also write plausible code that is wrong or unsafe; GitHub says generated code can look valid while being wrong.", "l": "m", "c": "For what merges: required review and narrowly scoped tokens.
- `-` For what runs: least-privilege GITHUB\_TOKEN permissions, protected environments with required reviewers, CODEOWNERS on workflow files and ephemeral runners.
- `-` Ask rules such as Bash(git push \*) are not a boundary: Claude Code notes that git -C . push does not match them.
- `-` Gate merges on review and security scans, and check that changed tests still fail when the behaviour breaks.
- `+` GitHub also says generated code can look valid while being wrong.", "l": "m", "c": "For what merges: required review and narrowly scoped tokens.
- `+` For what runs: least-privilege GITHUB\_TOKEN permissions, environments with required reviewers, CODEOWNERS on workflow files and ephemeral runners.
- `+` Claude Code ask rules are not a boundary: git -C . push does not match Bash(git push \*).
- `+` Add security scans, and check changed tests still fail when behaviour breaks.

**SOURCES[9]** (18 -> 18 words)

- `-` {"t": "Researchers uncover 30+ flaws in AI coding tools (IDEsaster)", "u": "https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html", "n": "The Hacker News (December 2025)."}
- `+` {"t": "Researcher uncovers 30+ flaws in AI coding tools (IDEsaster)", "u": "https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html", "n": "The Hacker News (December 2025)."}

