# MCP server intake: fact check

<!-- ledger -->
| # | Basis | Statement | Verdict |
|---|---|---|---|
| 1 | requirement | A process to decide whether an MCP server may be used, and to decide again when it changes. It builds on enterprise controls. |  |
| 2 | inference quote:l-noproof | Passing intake lowers risk. It does not prove that a server is safe. |  |
| 3 | requirement | If you can only do ten things, do these. |  |
| 4 | label | Say what is wanted |  |
| 5 | label | Judge publisher and need |  |
| 6 | label | Fetch and fix the bytes |  |
| 7 | label | Traditional scanners |  |
| 8 | label | MCP code and design |  |
| 9 | label | Run it where it cannot hurt |  |
| 10 | label | Approve, limit or reject |  |
| 11 | label | Make only that copy runnable |  |
| 12 | label | Detect change, revoke |  |
| 13 | requirement | No checks of its own. The gate is the condition. |  |
| 14 | requirement | Record what is asked for, so the later stages have something to test against. |  |
| 15 | requirement | Nothing from the server. |  |
| 16 | requirement | Purpose and named owner |  |
| 17 | requirement | Link to the vendor's own documentation |  |
| 18 | requirement | Exact version, image digest or URL |  |
| 19 | requirement | Transport: local process or HTTP |  |
| 20 | requirement | Data it will reach |  |
| 21 | requirement | Tools wanted |  |
| 22 | requirement | Credentials and scopes |  |
| 23 | requirement | Look in the approved catalog first. If an approved server covers the need, use it. |  |
| 24 | requirement | Install nothing. |  |
| 25 | requirement | A request record. |  |
| 26 | requirement | Every input is filled in and an owner has accepted the role. |  |
| 27 | requirement | Compare the new request with the approval record and write down what differs. |  |
| 28 | quote:l-run | A local server is downloaded code that runs under your user account. |  |
| 29 | quote:t-authz | Which tools a server lists can depend on the access it is given, so the requested scopes belong in the request. |  |
| 30 | requirement | Reject bad candidates before anything is downloaded, and set the risk tier. |  |
| 31 | requirement | Nothing from the server. This is desk work. |  |
| 32 | requirement | Request record |  |
| 33 | requirement | Publisher, repository and registry pages |  |
| 34 | requirement | Malicious package reports |  |
| 35 | requirement | Run the hygiene checks. |  |
| 36 | requirement | Give the server a provisional risk tier. |  |
| 37 | requirement | Stop at the first check marked Block that fails. |  |
| 38 | requirement | Go or stop, with a provisional tier. |  |
| 39 | requirement | No blocking hygiene check has failed. |  |
| 40 | requirement | Repeat for the new version: publisher, ownership, license, age and malicious reports can all differ. |  |
| 41 | quote:l-listing | A registry listing does not show that a server is safe. |  |
| 42 | quote:vs-trust | Trusting a publisher does not show that every tool result is safe. |  |
| 43 | inference quote:pm-fake | Stars and download counts are weak evidence: a look-alike package built trust over many versions before turning malicious. |  |
| 44 | requirement | Get one exact copy, and make sure every later stage looks at that same copy. |  |
| 45 | requirement | Only the fetch tool, in a quarantine area. No install scripts. |  |
| 46 | requirement | Exact version, image or URL |  |
| 47 | requirement | Local or container: fetch into quarantine or an internal mirror, record digests, lock the dependency tree and build an SBOM. |  |
| 48 | requirement | Remote: record the URL, the certificate-protected connection and the authorization metadata. |  |
| 49 | requirement | Verify signatures and provenance. |  |
| 50 | requirement | Digests, lock file, SBOM and provenance result, or the remote endpoint details. |  |
| 51 | requirement | Digest or URL recorded, and no invalid signature. |  |
| 52 | requirement | Fetch the new version and compare its dependency tree and install scripts with the approved ones. |  |
| 53 | quote:l-toponly | Pinning the version of the top package does not pin its dependencies. |  |
| 54 | quote:slsa-l1 | Provenance at the first SLSA build level is easy to bypass or forge. |  |
| 55 | inference quote:d-selfreport | A server's own name and version are self-reported. Identify it by digest or URL. |  |
| 56 | requirement | Find known problems with ordinary application security tools. |  |
| 57 | requirement | Scanners, in an isolated job without secrets. |  |
| 58 | requirement | Quarantined copy |  |
| 59 | requirement | SBOM |  |
| 60 | requirement | Run the vulnerability, malware, code, secret and configuration scans. |  |
| 61 | requirement | Triage every finding: exploited, reachable, fix available. |  |
| 62 | requirement | Findings with a disposition each. |  |
| 63 | requirement | No known malicious package, no known exploited vulnerability and no live secret. |  |
| 64 | requirement | Run all scans on the new copy and report what is new compared with the approved version. |  |
| 65 | quote:pa-static | A dependency audit tool is not a code analyzer. |  |
| 66 | quote:pa-exec | A dependency audit tool can run code from what it audits, so isolate the scan job. |  |
| 67 | requirement | Check the server against the MCP security rules that generic scanners may not know. |  |
| 68 | requirement | Nothing from the server. People and tools read code and settings. |  |
| 69 | requirement | Source code |  |
| 70 | requirement | Configuration and launch command |  |
| 71 | requirement | Scan findings |  |
| 72 | requirement | Go through the MCP review checks. |  |
| 73 | requirement | Remote: there is no code to read. Ask the vendor for evidence on each check marked remote, and test what you can in Sandbox. |  |
| 74 | requirement | Scale the depth to the tier. |  |
| 75 | requirement | Review findings. |  |
| 76 | requirement | Every blocking review check passes or has vendor evidence. |  |
| 77 | requirement | Read the code difference, with first attention on new tools, new dependencies, new destinations, new scopes and new install scripts. |  |
| 78 | quote:l-noproof | A scanner finding nothing does not show how the server will behave. |  |
| 79 | requirement | See what the server says and does when it runs. |  |
| 80 | requirement | The server, for the first time, in a disposable environment. |  |
| 81 | requirement | Pinned copy or URL |  |
| 82 | requirement | Fake data and canary credentials |  |
| 83 | requirement | Egress proxy |  |
| 84 | requirement | Start with outbound traffic denied and allow only declared destinations. |  |
| 85 | requirement | Capture and hash everything the server tells the model or shows the user. |  |
| 86 | requirement | Run MCP scanners, authentication probes and abuse tests. |  |
| 87 | requirement | Use the tools, then capture again. |  |
| 88 | requirement | Surface hashes, observed behaviour and findings. |  |
| 89 | requirement | Behaviour matches what was declared and the surface is unchanged on second capture, or each difference is explained. |  |
| 90 | requirement | Capture the surface again and compare it with the approved hashes. |  |
| 91 | quote:tob-uninvoked | A server can influence the model before any of its tools is called. |  |
| 92 | quote:as-exec | Starting a server to scan it can run commands or send traffic. |  |
| 93 | inference quote:t-authz | A malicious server could show a scanner different text than it shows real users. |  |
| 94 | requirement | Make one accountable decision on the evidence. |  |
| 95 | requirement | Nothing. |  |
| 96 | requirement | All findings |  |
| 97 | requirement | Tier |  |
| 98 | requirement | Sandbox observations |  |
| 99 | requirement | Confirm the tier. |  |
| 100 | requirement | Approve, approve with conditions, reject or defer. |  |
| 101 | requirement | Write the approval record. |  |
| 102 | requirement | A signed approval record. |  |
| 103 | requirement | The right approver for the tier has decided, and the record is complete. |  |
| 104 | requirement | Decide on the difference. The old record stays valid until the new one replaces it or is revoked. |  |
| 105 | quote:l-noproof | Approval is a judgement about risk. Passing every check does not prove a server safe. |  |
| 106 | requirement | Let people run the approved copy and nothing else. |  |
| 107 | requirement | The approved server, for a first group of users. |  |
| 108 | requirement | Approval record |  |
| 109 | requirement | Platform policy settings |  |
| 110 | requirement | Publish the artifact or URL to the approved source. |  |
| 111 | requirement | Add the allowlist entry and pinned configuration. |  |
| 112 | requirement | Prove that an unapproved server and an unapproved version are refused. |  |
| 113 | requirement | Roll out to a small group first. |  |
| 114 | requirement | Policy change, catalog entry and test evidence. |  |
| 115 | requirement | The block test has passed in each client in use. |  |
| 116 | requirement | Move the pin and the allowlist entry to the new version in stages, and keep the previous version ready for rollback. |  |
| 117 | quote:l-allowlist | A short list of vetted, pinned servers with entry criteria is the recommended shape. |  |
| 118 | requirement | Notice any difference from the approval record, and be able to switch the server off. |  |
| 119 | requirement | The approved server, in daily use. |  |
| 120 | requirement | Advisory feeds |  |
| 121 | requirement | Logs and egress alerts |  |
| 122 | requirement | Client configuration inventory |  |
| 123 | requirement | Compare the live surface with the approved hashes. |  |
| 124 | requirement | Match advisories to the SBOM. |  |
| 125 | requirement | Watch the publisher and the traffic. |  |
| 126 | requirement | Recertify before expiry, or retire. |  |
| 127 | requirement | Triggers, or a new expiry date, or retirement. |  |
| 128 | requirement | No open trigger and the approval has not expired. |  |
| 129 | requirement | A trigger sends the server back to the stages listed under When something changes. |  |
| 130 | quote:l-rugpull | A server can change its tool descriptions after approval. |  |
| 131 | quote:l-reask | The protocol does not require clients to ask again when definitions change. |  |
| 132 | inference quote:t-listchanged | Change notices cannot be the only detector: sending them is recommended, not required, and depends on a declared capability. |  |
| 133 | requirement | Nine stages run in order. A failed gate stops the server there. Nothing from the server runs before Sandbox. |  |
| 134 | requirement | Release feed or dependency update tool for the package or image. |  |
| 135 | requirement | Keep running the approved, pinned version. |  |
| 136 | quote:co-staged | Testing and staged rollout belong in update handling. |  |
| 137 | requirement | Hash comparison of the live surface. |  |
| 138 | requirement | Block the changed and new tools until approved. Block the whole server if instructions changed. |  |
| 139 | quote:t-change | A tool list may change over time. |  |
| 140 | requirement | Configuration change, vendor notice or a failed connection. |  |
| 141 | requirement | Do not allow the new address until approved. |  |
| 142 | requirement | Advisory feed matched against the SBOM, or a vendor notice. |  |
| 143 | requirement | Decide on exposure at once. Limit or block if it is being exploited. A fixed version goes through the New version path without the waiting period. |  |
| 144 | quote:l-pinvuln | A pin keeps the vulnerable version in place until someone moves it. |  |
| 145 | requirement | Malicious package report, vendor or community alert. |  |
| 146 | requirement | Revoke now. Block traffic, find every installation, rotate every credential it could read, and investigate what it did. |  |
| 147 | quote:l-respond | The response is to block, rotate and replace. |  |
| 148 | requirement | Repository transfer, new maintainer, new package account, acquisition. |  |
| 149 | requirement | Freeze at the approved version. Treat the next version as a new server. |  |
| 150 | requirement | Version difference, consent screen change, egress alert. |  |
| 151 | requirement | Do not grant the new access until approved. |  |
| 152 | quote:bp-semantic | A scope can change meaning without changing name. |  |
| 153 | requirement | Vendor notice or license difference between versions. |  |
| 154 | requirement | Keep the approved version where the old terms still cover it. Otherwise stop. |  |
| 155 | requirement | Repository or registry status, no response to reports. |  |
| 156 | requirement | Plan replacement and set an end date. |  |
| 157 | requirement | Date in the approval record. |  |
| 158 | requirement | Renew before the date. After it, the server is not approved. |  |
| 159 | requirement | Log, egress or canary alert, or a user report. |  |
| 160 | requirement | Block while you investigate. |  |
| 161 | requirement | New data, new users, new client, new configuration, or another server added next to it. |  |
| 162 | requirement | Keep the old use only. |  |
| 163 | requirement | New or renamed tool |  |
| 164 | requirement | Changed description or parameter |  |
| 165 | requirement | Changed read-only or destructive hint |  |
| 166 | requirement | New dependency |  |
| 167 | requirement | New or changed install script |  |
| 168 | requirement | New destination |  |
| 169 | requirement | New scope or permission |  |
| 170 | requirement | A change is any difference from the approval record. Never update a server automatically unless it meets every condition for automatic approval. |  |
| 171 | requirement | Allow it only when all of these are true. Otherwise a person decides. |  |
| 172 | requirement | The server is in the lowest tier. |  |
| 173 | requirement | Every automated check in Screen, Pin, Scan and Sandbox passes. |  |
| 174 | requirement | The captured surface is identical. |  |
| 175 | requirement | No new dependency, install script, destination or scope, and the same publisher. |  |
| 176 | example | Owner, URL, two tools and read and comment scopes recorded. |  |
| 177 | example | The URL is in the vendor's documentation. Data handling answers arrive in writing. Tier 3, because it writes. |  |
| 178 | example | URL and authorization metadata recorded. |  |
| 179 | example | No code to scan. The vendor shares its vulnerability handling. |  |
| 180 | example | The vendor gives evidence on token audience, passthrough and logging. |  |
| 181 | example | Surface captured with the two scopes. Permitted probes are refused. Second capture matches. |  |
| 182 | example | Approved for the two tools, for six months, with no other scopes. |  |
| 183 | example | URL allowlisted. A second URL is refused in each client. |  |
| 184 | example | Daily surface comparison starts. |  |
| 185 | example | Fictional example: a team asks for a ticket vendor's own remote server, to read and comment on tickets. |  |
| 186 | example | A developer asks for the package by the name found in a search. |  |
| 187 | example | The vendor's documentation does not name this package, and the publisher account is not the vendor's. Rejected before any download. The package name goes on the deny list. |  |
| 188 | example | Based on a reported case: a package on npm used an email vendor's name without being the vendor's. |  |
| 189 | quote:pm-fake | The vendor reported that the fake package built trust over 15 versions before adding a backdoor. |  |
| 190 | example | New version seen. It waits out the 7 days while the old pin keeps running. |  |
| 191 | example | New digest recorded. Dependencies unchanged. |  |
| 192 | example | No known vulnerability or report. Known-problem scans can be silent on new malicious code. |  |
| 193 | example | The code difference touches the send function. The reviewer flags it. |  |
| 194 | example | A test message arrives with a recipient nobody asked for. The version is rejected, the publisher is reported and the approval of the old version is reviewed. |  |
| 195 | example | Fictional example using the same technique: an approved mail server publishes a new version that copies every message to an outside address. |  |
| 196 | example | Request recorded. |  |
| 197 | example | Publisher and source are in order. |  |
| 198 | example | Version and digest recorded. |  |
| 199 | example | Traditional scans find nothing. The problem is text, not a vulnerable library. |  |
| 200 | example | No code flaw found. |  |
| 201 | example | Reading every captured field shows the instruction. Rejected. |  |
| 202 | example | Fictional example: a note taking server whose parameter description tells the model to read a key file and pass it along. |  |
| 203 | quote:inv-poison | Instructions hidden in tool descriptions can be invisible to users and visible to models. |  |
| 204 | example | The hash comparison reports a new tool. The gateway or client blocks it. |  |
| 205 | example | The new tool is captured and tested. It sends data to a storage service. |  |
| 206 | example | A new destination means a person decides. Approved only for non-sensitive projects. |  |
| 207 | example | New hashes and condition published. |  |
| 208 | example | Fictional example: an approved remote server starts listing a new export tool. No version number changes. |  |
| 209 | example | The advisory matches a stored SBOM. Configuration inventory shows who runs it. |  |
| 210 | example | The approved version is affected. It is blocked, and exposed credentials are rotated. |  |
| 211 | example | The fixed version is fetched and pinned. The 7 day wait is skipped and recorded. |  |
| 212 | example | Surface and behaviour compared with the old approval. |  |
| 213 | example | The fixed version is approved. |  |
| 214 | example | Pin and allowlist moved. The old version is refused. |  |
| 215 | example | Based on a published vulnerability in mcp-remote, a bridge that connects local clients to remote servers. |  |
| 216 | quote:cv-6514 | The flaw let an untrusted server run operating system commands on the client machine. |  |
| 217 | requirement | Publisher is identified |  |
| 218 | requirement | Trace the server to a source repository and a real organisation or maintainer. For a remote server, trace the URL to its operator. |  |
| 219 | requirement | A named, reachable publisher, confirmed from more than the listing itself. |  |
| 220 | requirement | It is the package the vendor means |  |
| 221 | requirement | Take the name or URL from the vendor's own documentation and compare it letter by letter. |  |
| 222 | requirement | Name, publisher account and URL match the vendor's documentation. |  |
| 223 | requirement | Source can be read |  |
| 224 | requirement | Find the source that the published artifact is built from. |  |
| 225 | requirement | Source is available for the exact version. |  |
| 226 | requirement | Project is maintained |  |
| 227 | requirement | Look at recent commits, releases, open security issues and whether the project is archived. |  |
| 228 | requirement | Not archived, and security reports get answered. |  |
| 229 | requirement | There is a way to report vulnerabilities |  |
| 230 | requirement | Look for a security policy and past advisories. |  |
| 231 | requirement | A reporting route exists. |  |
| 232 | requirement | License allows the use |  |
| 233 | requirement | Read the license or the service terms. |  |
| 234 | requirement | Terms allow the intended use. |  |
| 235 | requirement | New versions have aged |  |
| 236 | requirement | Wait until a new version has been public for 7 days. Skip the wait for a fix to a vulnerability that is being exploited. |  |
| 237 | requirement | The version is old enough, or the exception is recorded. |  |
| 238 | requirement | Not reported as malicious |  |
| 239 | requirement | Look up the package and version in malicious package reports. Repeat for every dependency once the tree is known. |  |
| 240 | requirement | No report for the package or any dependency. |  |
| 241 | label | Requirement of this process. No source is quoted. |  |
| 242 | requirement | Remote operator gives assurance |  |
| 243 | requirement | Ask who runs the service, where data goes, how long it is kept, how incidents are announced and how changes are announced. |  |
| 244 | requirement | Written answers that fit the data involved. |  |
| 245 | requirement | Running it locally is justified |  |
| 246 | requirement | Use the remote version where one exists. Ask why a server with no need for local access is only offered as a local process. |  |
| 247 | requirement | A stated reason for local execution. |  |
| 248 | requirement | Exact version |  |
| 249 | requirement | Name one version. No ranges, no latest, no floating tag. |  |
| 250 | requirement | One immutable version in the request and the configuration. |  |
| 251 | requirement | Digest recorded |  |
| 252 | requirement | Record the artifact hash. Refer to a container image by digest. |  |
| 253 | requirement | Digest in the approval record. |  |
| 254 | requirement | Fetched without running it |  |
| 255 | requirement | Fetch into quarantine with install scripts off. For Python, accept built packages only. |  |
| 256 | requirement | No code from the package ran during the fetch. |  |
| 257 | requirement | Dependencies locked and listed |  |
| 258 | requirement | Lock the whole dependency tree with hashes and generate your own SBOM from the artifact. |  |
| 259 | requirement | Lock file with hashes and an SBOM are stored. |  |
| 260 | requirement | Signatures and provenance verified |  |
| 261 | requirement | Verify signatures and attestations against the expected publisher and source. Invalid blocks. Missing goes to the approver. |  |
| 262 | requirement | Verification succeeds for the expected identity. |  |
| 263 | requirement | Remote endpoint recorded |  |
| 264 | requirement | Record the exact URL and the authorization server details. Require HTTPS throughout. |  |
| 265 | requirement | URL and metadata recorded, no plain HTTP. |  |
| 266 | requirement | Known vulnerabilities |  |
| 267 | requirement | Scan the artifact and all dependencies. Rank by known exploitation, exploit probability and reachability. Ask a remote vendor for its results. |  |
| 268 | requirement | No known exploited vulnerability. Others have an owner and a deadline. |  |
| 269 | requirement | Malicious code signs |  |
| 270 | requirement | Run a malicious package scanner as well as the vulnerability scan. |  |
| 271 | requirement | Findings explained or the server rejected. |  |
| 272 | requirement | Static code analysis |  |
| 273 | requirement | Analyze the source for injection, path, request forgery and similar flaws. |  |
| 274 | requirement | No unresolved serious finding. |  |
| 275 | requirement | Secrets in code and images |  |
| 276 | requirement | Scan source, package and image layers for credentials. |  |
| 277 | requirement | No live secret. |  |
| 278 | requirement | Container and deployment settings |  |
| 279 | requirement | Scan the image build file and deployment files for risky settings such as root user, host mounts and broad privileges. |  |
| 280 | requirement | No unexplained risky setting. |  |
| 281 | requirement | Install and build scripts read |  |
| 282 | requirement | List every script that runs at install, build or start, and read it. |  |
| 283 | requirement | Each script is understood and needed. |  |
| 284 | requirement | Binaries and hidden code |  |
| 285 | requirement | Look for bundled binaries, downloads at run time, obfuscated code and files that do not match the source. |  |
| 286 | requirement | Everything executable traces to the source or a verified origin. |  |
| 287 | requirement | Dependency confusion |  |
| 288 | requirement | Resolve internal package names only from the internal registry, and fetch public ones through a mirror. |  |
| 289 | requirement | No internal name can resolve from a public registry. |  |
| 290 | requirement | No command or code injection |  |
| 291 | requirement | Check that model or user input never reaches a shell or code evaluator. |  |
| 292 | requirement | No path from input to shell, eval or string-built command. |  |
| 293 | requirement | File access stays inside bounds |  |
| 294 | requirement | Check path handling, including symlinks and prefix comparisons. |  |
| 295 | requirement | Resolved paths cannot leave the allowed folders. |  |
| 296 | requirement | No open URL fetching |  |
| 297 | requirement | Check every place the server fetches a URL that came from the model or a user. |  |
| 298 | requirement | Destinations are allowlisted, and private and metadata addresses are refused. |  |
| 299 | requirement | Tokens are checked for audience |  |
| 300 | requirement | Check that the server rejects tokens issued for something else. |  |
| 301 | requirement | A token for another service is refused. |  |
| 302 | requirement | No token passthrough |  |
| 303 | requirement | Check that the server never forwards the caller's token to another service. |  |
| 304 | requirement | Downstream calls use their own credentials. |  |
| 305 | requirement | Proxy servers ask consent per client |  |
| 306 | requirement | If the server signs in to a third party on behalf of many clients, check consent handling. |  |
| 307 | requirement | Consent is stored and checked for each client. |  |
| 308 | requirement | Sign-in links are handled safely |  |
| 309 | requirement | For a bridge or bundled client, check how it treats URLs received from a server. |  |
| 310 | requirement | Only safe schemes are opened, never through a shell. |  |
| 311 | requirement | Least privilege |  |
| 312 | requirement | Compare requested scopes, file access and permissions with the stated purpose. |  |
| 313 | requirement | No wildcard scope and nothing without a reason. |  |
| 314 | requirement | HTTP endpoint is not open |  |
| 315 | requirement | For any server that listens over HTTP, check Origin validation, listening address and authentication. |  |
| 316 | requirement | Origin checked, local servers listen on localhost only, callers authenticate. |  |
| 317 | requirement | Handles are not logins |  |
| 318 | requirement | If the server hands out state handles, check that each use is authorized. |  |
| 319 | requirement | Knowing a handle alone gives no access. |  |
| 320 | requirement | No secrets asked in forms |  |
| 321 | requirement | Check what the server asks the user for during use. |  |
| 322 | requirement | Passwords, keys, tokens and payment data are never requested in form mode. |  |
| 323 | requirement | Basic tool protections |  |
| 324 | requirement | Check input validation, access control, rate limits and output cleaning. |  |
| 325 | requirement | All four are present. |  |
| 326 | requirement | Usable logs without secrets |  |
| 327 | requirement | Check that tool calls can be logged and that secrets are masked. |  |
| 328 | requirement | Calls are logged in a structured form without secrets. |  |
| 329 | requirement | No stored secrets |  |
| 330 | requirement | Check code, defaults and sample configuration for built-in credentials. |  |
| 331 | requirement | Credentials come from a secret store, one narrow credential per server. |  |
| 332 | inference | For a remote server, isolation protects your side only. The server's side stays out of reach. |  |
| 333 | requirement | Isolated and disposable |  |
| 334 | requirement | Run in a throwaway environment with no real credentials or data and outbound traffic denied by default. |  |
| 335 | requirement | Nothing of value is reachable from the test. |  |
| 336 | requirement | Whole surface captured and hashed |  |
| 337 | requirement | Capture server instructions, tools with full schemas and annotations, prompts, resources, resource templates, UI content and icons, with the access it will have in production. |  |
| 338 | requirement | A hash for every item is in the record. |  |
| 339 | requirement | No instructions aimed at the model |  |
| 340 | requirement | Read every text field, including parameter names, schema descriptions and comments. |  |
| 341 | requirement | Nothing tells the model to do what the tool's purpose does not need. |  |
| 342 | requirement | No hidden characters |  |
| 343 | requirement | Search the captured text for zero-width and direction-control characters. |  |
| 344 | requirement | None present, or each one explained. |  |
| 345 | requirement | MCP scanner |  |
| 346 | requirement | Run at least one MCP scanner inside the sandbox. Check first what it sends outside your network. |  |
| 347 | requirement | Findings triaged. A clean result counts as one input, not as approval. |  |
| 348 | requirement | No shadowing or name clashes |  |
| 349 | requirement | Compare names and descriptions with the other approved servers. |  |
| 350 | requirement | No duplicate tool name, and no text about another server's tools. |  |
| 351 | requirement | No dangerous combination |  |
| 352 | requirement | Check whether this server, with the others in use, joins untrusted content, private data and a way to send data out. |  |
| 353 | requirement | The combination is absent, or limited by a condition in the approval. |  |
| 354 | requirement | Annotations match behaviour |  |
| 355 | requirement | Compare read-only and destructive hints with what the tool does. |  |
| 356 | requirement | No hint understates the effect. |  |
| 357 | requirement | Network, file and process activity as declared |  |
| 358 | requirement | Watch traffic, files and processes. Place canary files and credentials. |  |
| 359 | requirement | No undeclared destination or access, and no canary used. |  |
| 360 | inference quote:pm-fake | This comparison would show an added hidden recipient, as in the reported Postmark look-alike case. |  |
| 361 | requirement | Outbound content matches the request |  |
| 362 | requirement | For tools that send or write, compare what arrived with what the call asked for: recipients, fields, attachments. |  |
| 363 | requirement | Nothing added, removed or redirected. |  |
| 364 | requirement | Authentication probes |  |
| 365 | requirement | Call without a token, with a token for another service and with a foreign Origin. Get written permission before probing a server you do not run. |  |
| 366 | requirement | Every such call is refused. |  |
| 367 | requirement | Get the operator's written permission before testing a remote server this way. |  |
| 368 | requirement | Abuse tests |  |
| 369 | requirement | Send path traversal, injection, internal address, oversized and malformed inputs. |  |
| 370 | requirement | No test succeeds and the server stays up. |  |
| 371 | requirement | Second capture is the same |  |
| 372 | requirement | Use the tools, wait, reconnect and capture again. |  |
| 373 | requirement | Hashes match, or each change has an accepted reason. |  |
| 374 | requirement | Schemas and icons are safe |  |
| 375 | requirement | Look for references to network addresses in schemas, and for unsafe icon addresses. |  |
| 376 | requirement | No network reference and only safe icon schemes. |  |
| 377 | requirement | Interactive UI reviewed |  |
| 378 | requirement | If the server ships UI, review its code and the domains it declares, and hash it. |  |
| 379 | requirement | Declared domains are needed and narrow, and the UI hash is recorded. |  |
| 380 | requirement | Risk tier assigned |  |
| 381 | requirement | Set the tier from what the server can do. |  |
| 382 | requirement | Tier and reason recorded. |  |
| 383 | requirement | Every finding has an outcome |  |
| 384 | requirement | Fix, accept with an owner and end date, or reject. Known malicious code gets no exception. |  |
| 385 | requirement | No finding without an outcome. |  |
| 386 | requirement | Approver is not the requester |  |
| 387 | requirement | Have a different person approve. |  |
| 388 | requirement | Two different people on the record. |  |
| 389 | requirement | Conditions and expiry set |  |
| 390 | requirement | Write the limits of the approval and the date it ends. |  |
| 391 | requirement | An expiry date is on the record. |  |
| 392 | requirement | Record complete |  |
| 393 | requirement | Fill in every field of the approval record and register the server. |  |
| 394 | requirement | The record and the catalog entry exist. |  |
| 395 | requirement | Served from the approved source |  |
| 396 | requirement | Install from the internal registry or the recorded URL, and block direct public downloads where you can. |  |
| 397 | requirement | Clients can only get the approved copy. |  |
| 398 | requirement | Allowlist matches URL or command |  |
| 399 | requirement | Allow by remote URL or exact command. Do not rely on a server name. |  |
| 400 | requirement | A renamed unapproved server is refused. |  |
| 401 | requirement | Configuration is pinned |  |
| 402 | requirement | Put the version or digest in the managed configuration and take credentials from a secret store. |  |
| 403 | requirement | No floating version and no secret in a configuration file. |  |
| 404 | requirement | Contained at run time |  |
| 405 | requirement | Run local servers in a container or sandbox with only the needed folder, and limit outbound traffic per server. |  |
| 406 | requirement | Access and destinations match the approval. |  |
| 407 | requirement | Block is proven |  |
| 408 | requirement | Try to start an unapproved server and an unapproved version in each client. |  |
| 409 | requirement | Both are refused, with evidence stored. |  |
| 410 | requirement | Definition changes are stopped |  |
| 411 | requirement | Use a client that asks again, or a gateway that blocks, when definitions differ from the approved hashes. |  |
| 412 | requirement | A changed definition cannot be used silently. |  |
| 413 | requirement | Definition drift |  |
| 414 | requirement | Capture the live surface on a schedule and on each reconnect where possible, and compare hashes. |  |
| 415 | requirement | Hashes equal the approved ones. |  |
| 416 | requirement | New advisories |  |
| 417 | requirement | Match new vulnerability and malicious package reports against each stored SBOM, daily. |  |
| 418 | requirement | No unhandled match. |  |
| 419 | requirement | Upstream changes |  |
| 420 | requirement | Follow releases, ownership, maintainers, deprecation and takedown of each approved server. |  |
| 421 | requirement | No unreviewed change. |  |
| 422 | requirement | Traffic and logs |  |
| 423 | requirement | Alert on new destinations, unusual volume and unexpected tool calls. |  |
| 424 | requirement | Alerts have an owner and are handled. |  |
| 425 | requirement | Recertification |  |
| 426 | requirement | Re-assess before the expiry date. |  |
| 427 | requirement | Renewed or retired on time. |  |
| 428 | requirement | Switch-off and rollback tested |  |
| 429 | requirement | Keep a way to block the server everywhere, return to the previous version and rotate its credentials. Rehearse it. |  |
| 430 | requirement | A rehearsal has worked within the target time. |  |
| 431 | requirement | Unapproved servers found |  |
| 432 | requirement | Collect client configurations and compare them with the catalog. |  |
| 433 | requirement | Every configured server is approved. |  |
| 434 | quote:osv-use | OSV-Scanner |  |
| 435 | quote:gd-use,om-reports | GuardDog, OpenSSF reports |  |
| 436 | quote:ql-use | CodeQL |  |
| 437 | quote:gl-use,tv-secrets | Gitleaks, Trivy |  |
| 438 | quote:tv-iac | Trivy |  |
| 439 | quote:ci-engines,as-sends | Cisco MCP Scanner, Snyk Agent Scan |  |
| 440 | requirement | The server cannot move on, or is suspended if already in use, until this is fixed. |  |
| 441 | requirement | The approver decides and records why. |  |
| 442 | requirement | Pick at least one tool for each job. Other tools can do the same jobs. |  |
| 443 | label | Look-alike or impersonating server |  |
| 444 | inference | A publisher that is real but dishonest passes identity checks. |  |
| 445 | label | Malicious package |  |
| 446 | inference quote:l-noproof | New malicious code with no report yet can pass scans and stay quiet in a test. |  |
| 447 | label | Publisher account or ownership takeover |  |
| 448 | inference quote:npm-prov | A release made with the real publisher's own build system can carry valid provenance. |  |
| 449 | label | Known vulnerability |  |
| 450 | inference | Flaws that nobody has published are not matched. |  |
| 451 | label | Compromised dependency |  |
| 452 | inference | A locked but already compromised dependency stays locked in. |  |
| 453 | label | Dependency confusion |  |
| 454 | inference | Names that no registry rule covers can still resolve publicly. |  |
| 455 | label | Install or build script abuse |  |
| 456 | inference | A script that is needed for install still has to run later. |  |
| 457 | label | Floating version or moving tag |  |
| 458 | inference | A remote server cannot be pinned by digest. |  |
| 459 | label | Tool poisoning in any schema field |  |
| 460 | inference quote:o3-static | Wording that looks innocent to a reviewer and a scanner can still steer a model. |  |
| 461 | label | Hidden characters |  |
| 462 | inference | Meaning can be hidden without any special character. |  |
| 463 | label | Shadowing another server's tools |  |
| 464 | quote:l-shared | A server added later changes the combination. |  |
| 465 | label | Definitions changed after approval (rug pull) |  |
| 466 | inference | Between two comparisons a change can be used unnoticed. |  |
| 467 | label | Behaviour changed behind unchanged definitions |  |
| 468 | quote:c-hashlimit | Hashing definitions does not see it. |  |
| 469 | label | Prompt injection through results and resources |  |
| 470 | quote:c-response,o6-untrusted | Intake cannot test content that does not exist yet. |  |
| 471 | label | Data leaving through a chain of tools |  |
| 472 | inference | A permitted destination can be used to take data out. |  |
| 473 | label | Command or code injection |  |
| 474 | inference | Analysis and tests miss some paths. |  |
| 475 | label | Path traversal and symlink escape |  |
| 476 | inference | Anything inside the mounted folder stays reachable. |  |
| 477 | label | Server-side request forgery |  |
| 478 | inference | Redirects and name resolution tricks need their own tests. |  |
| 479 | label | Command execution from a sign-in link |  |
| 480 | inference | The same flaw in a client is outside this process. |  |
| 481 | label | Undeclared network, file or process activity |  |
| 482 | inference | Behaviour triggered by time, data or environment may not show in a test. |  |
| 483 | label | Resource exhaustion |  |
| 484 | inference | Load limits of a remote service are the vendor's to hold. |  |
| 485 | label | Missing authentication or open local endpoint |  |
| 486 | quote:l-loopback | A local process on the same machine can reach what listens there. |  |
| 487 | label | DNS rebinding |  |
| 488 | inference | Later code changes can remove the check. |  |
| 489 | label | Token passthrough and wrong audience |  |
| 490 | inference | For a remote server you rely on the vendor for what happens downstream. |  |
| 491 | label | Confused deputy |  |
| 492 | inference | Hard to prove from outside for a remote server. |  |
| 493 | label | Excess or creeping scopes |  |
| 494 | inference quote:bp-semantic | A scope can widen on the service side without any change in the server. |  |
| 495 | label | State handle misuse |  |
| 496 | inference | Hard to test fully from outside. |  |
| 497 | label | Secret exposure |  |
| 498 | quote:l-reach | A credential the server needs is readable by the server. |  |
| 499 | label | Phishing for secrets through user prompts |  |
| 500 | inference | Ordinary looking questions can still collect sensitive data. |  |
| 501 | label | Hostile or leaking server UI |  |
| 502 | inference | UI loaded later from an allowed domain can change. |  |
| 503 | label | Escape from the local environment |  |
| 504 | quote:co-container | A container lowers access but can be escaped. |  |
| 505 | label | Too little logging |  |
| 506 | inference | A remote server's internal actions are not in your logs. |  |
| 507 | label | Shadow servers |  |
| 508 | quote:vs-harness | Unmanaged devices and clients that ignore policy are not seen. |  |
| 509 | label | Context shared too widely |  |
| 510 | quote:o10-session | How a client keeps and shares context is outside server intake. |  |
| 511 | inference | Matching a check to an attack is a design choice. It is not a measured detection rate, and the list of attacks is not complete. |  |
| 512 | requirement | Reads only public or non-sensitive data. Remote. |  |
| 513 | requirement | Platform owner |  |
| 514 | requirement | 12 months |  |
| 515 | requirement | Reads internal or personal data. |  |
| 516 | requirement | Platform owner and security reviewer |  |
| 517 | requirement | 6 months |  |
| 518 | requirement | Changes data, sends data outward, or runs as a local process. |  |
| 519 | requirement | Security reviewer and data owner |  |
| 520 | requirement | Runs commands or code, or holds administrator or production access. |  |
| 521 | requirement | Security reviewer and system owner |  |
| 522 | requirement | 3 months |  |
| 523 | requirement | Released as recorded. |  |
| 524 | requirement | Released with limits that the platform or the owner enforces, such as fewer tools, fewer scopes, named users or a sandbox. |  |
| 525 | requirement | Added to the deny list when the reason is malicious or impersonation. |  |
| 526 | requirement | Nothing is released until the missing evidence arrives. |  |
| 527 | requirement | Use the highest tier that fits. Adjust the names and intervals to your organisation. |  |
| 528 | example | Keep one record for each approved server. Later changes are compared with it. The example is fictional. |  |
| 529 | example | {<br>  "name": "example-tickets-mcp",<br>  "publisher": {"organisation": "Example Vendor", "verified_from": "vendor documentation URL"},<br>  "owner": "team-support",<br>  "origin": {<br>    "type": "package",<br>    "package": "@example/tickets-mcp",<br>    "version": "2.4.1",<br>    "digest": "sha512-<digest of the artifact>",<br>    "source_commit": "<commit>",<br>    "provenance": "verified"<br>  },<br>  "dependencies": {"lock_hash": "sha256-<hash>", "sbom": "<stored SBOM>"},<br>  "surface": {<br>    "captured_with_scopes": ["tickets:read", "tickets:comment"],<br>    "instructions": "sha256-<hash>",<br>    "tools": {"get_ticket": "sha256-<hash>", "add_comment": "sha256-<hash>"},<br>    "prompts": {},<br>    "resources": {},<br>    "ui": {}<br>  },<br>  "runtime": {<br>    "command": ["<exact command and arguments>"],<br>    "credentials": "<secret store reference>",<br>    "files": ["<allowed folders>"],<br>    "destinations": ["tickets.example.com:443"]<br>  },<br>  "findings": "<link to triaged results>",<br>  "tier": 3,<br>  "decision": "approved with conditions",<br>  "conditions": ["get_ticket and add_comment only"],<br>  "requested_by": "<person>",<br>  "approved_by": "<another person>",<br>  "expires": "2027-05-26"<br>} |  |
| 530 | label | Server name, URL or command. |  |
| 531 | quote:gh-match | Entries match by name, URL or command. |  |
| 532 | quote:gh-profiles | The lists do not apply to servers defined in repository custom agent profiles. |  |
| 533 | quote:gh-malformed | A malformed list blocks all but the built-in servers. |  |
| 534 | label | Server name or ID. |  |
| 535 | preview quote:gh-preview | It is in public preview and not the recommended way to restrict servers. |  |
| 536 | quote:gh-ga | The recommended way is the managed settings file. |  |
| 537 | quote:gh-name | Name matching can be bypassed by editing configuration. |  |
| 538 | label | Server URL, exact command or name. |  |
| 539 | quote:cc-authoritative | An allowlist is authoritative only when it is also set to managed entries only. |  |
| 540 | quote:cc-exact | A command entry matches the exact command. |  |
| 541 | quote:cc-env | Environment variables in the entry are not compared. |  |
| 542 | quote:cc-name | A name entry is not a security control. |  |
| 543 | label | Managed Copilot settings, workspace trust and a per-server sandbox. |  |
| 544 | quote:vs-allow | Managed settings can limit which servers developers install and run. |  |
| 545 | quote:vs-harness | Claude and Codex sessions run without those Copilot controls. |  |
| 546 | quote:vs-restart | In a trusted workspace a server can start again after a configuration change without a trust prompt. |  |
| 547 | quote:vs-sandbox | The per-server sandbox covers local process servers on macOS and Linux. |  |
| 548 | quote:vs-windows | It is not available on Windows. |  |
| 549 | quote:vs-outbound | The Copilot sandbox allows outbound traffic by default. |  |
| 550 | label | A public list of servers. |  |
| 551 | preview quote:reg-preview | It is in preview. |  |
| 552 | quote:reg-moderation | Expect little or no moderation. |  |
| 553 | quote:reg-vulns | Having a security vulnerability does not by itself get a server removed. |  |
| 554 | label | Destinations per server. |  |
| 555 | quote:l-egress | A per-server egress list with alerts limits where a server can send data. |  |
| 556 | label | Client configuration files on devices. |  |
| 557 | quote:l-inventory | Management tools can collect client configurations to find what is in use. |  |
| 558 | requirement | A weak client can undo a well reviewed server. Assess clients separately. |  |
| 559 | requirement | Approval, filtering and permission controls at run time belong to the platform and agent design. |  |
| 560 | requirement | Its code, build and staff are visible only through the vendor's evidence. |  |
| 561 | requirement | How well the named scanners find these attacks was not measured. |  |
| 562 | requirement | License and data answers are collected here. Contracts and privacy review follow your normal process. |  |
| 563 | inference quote:gh-match,cc-exact,cc-env | None of the allowlist settings above compares a server's code or tool definitions with what was reviewed. This process has to do that. |  |
<!-- /ledger -->
