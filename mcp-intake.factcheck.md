# MCP server intake: fact check

<!-- ledger -->
| # | Basis | Statement | Verdict |
|---|---|---|---|
| 1 | requirement | A process to decide whether an MCP server may be used, and to decide again when it changes. It builds on enterprise controls. |  |
| 2 | inference quote:l-noproof | Passing intake lowers risk. It does not prove that a server is safe. |  |
| 3 | requirement | If you cannot do everything yet, do these first. |  |
| 4 | label | Say what is wanted |  |
| 5 | label | Judge publisher and need |  |
| 6 | label | Fix what is assessed |  |
| 7 | label | Traditional scanners |  |
| 8 | label | MCP code and design |  |
| 9 | label | Run it where it cannot hurt |  |
| 10 | label | Approve, limit or reject |  |
| 11 | label | Allow only what was approved |  |
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
| 40 | requirement | Repeat for the new version or changed service. Publisher, ownership, license, age and malicious reports can all differ. |  |
| 41 | quote:l-listing | A listing on a registry is not an endorsement. |  |
| 42 | quote:vs-trust | Trusting a publisher does not show that every tool result is safe. |  |
| 43 | quote:l-popular | Popularity or a good name does not show that a package is safe or current. |  |
| 44 | requirement | Fix what is being assessed, so every later stage looks at the same thing: one exact copy of a local server, or the address of a remote one. |  |
| 45 | requirement | Only the fetch tool, in a quarantine area. No install scripts. |  |
| 46 | requirement | Exact version, image or URL |  |
| 47 | requirement | Local or container: fetch into quarantine or an internal mirror, record digests, lock the dependency tree and build an SBOM. |  |
| 48 | requirement | Remote: record the URL, the certificate-protected connection and the authorization metadata. |  |
| 49 | requirement | Verify signatures and provenance. |  |
| 50 | requirement | Digests, lock file, SBOM and provenance result, or the remote endpoint details. |  |
| 51 | requirement | Every blocking check in this stage passes. |  |
| 52 | requirement | For a local server, fetch the new version and compare its dependency tree and install scripts with the approved ones. For a remote server, record the endpoint details again. |  |
| 53 | quote:l-toponly | Pinning a package version with a launcher such as npx or uvx fixes only the top package. Its dependencies are usually resolved again at install. |  |
| 54 | quote:slsa-l1 | Provenance at the first SLSA build level is easy to bypass or forge. |  |
| 55 | inference quote:d-selfreport | A server's own name and version are self-reported. Identify it by digest or URL. |  |
| 56 | requirement | Find known problems with ordinary application security tools. |  |
| 57 | requirement | Scanners, in an isolated job without secrets. |  |
| 58 | requirement | Quarantined copy |  |
| 59 | requirement | SBOM |  |
| 60 | requirement | Run the vulnerability, malware, code, secret and configuration scans. |  |
| 61 | requirement | Scan the locked dependency list and the SBOM. Do not let a scanner install the package. |  |
| 62 | requirement | Triage every finding: exploited, reachable, fix available. |  |
| 63 | requirement | Findings with a disposition each. |  |
| 64 | requirement | Run all scans on the new copy, or get new results from the remote vendor, and report what is new compared with the approved version. |  |
| 65 | quote:pa-static | pip-audit is not a static code analyzer. |  |
| 66 | quote:pa-exec,pa-equiv | pip-audit -r can run code from what it audits, so isolate the scan job. |  |
| 67 | quote:pa-nopip | Given a hashed requirements file, pip-audit can skip pip's dependency resolution with --disable-pip. |  |
| 68 | requirement | Check the server against the MCP security rules that generic scanners may not know. |  |
| 69 | requirement | Nothing from the server. People and tools read code and settings. |  |
| 70 | requirement | Source code |  |
| 71 | requirement | Configuration and launch command |  |
| 72 | requirement | Scan findings |  |
| 73 | requirement | Go through the MCP review checks. |  |
| 74 | requirement | Remote: there is no code to read. Ask the vendor for evidence on each check marked remote, and test what you can in Sandbox. |  |
| 75 | requirement | Scale the depth to the tier. |  |
| 76 | requirement | Review findings. |  |
| 77 | requirement | Every blocking check in this stage passes. For a remote server, the vendor's evidence can show that it passes. |  |
| 78 | requirement | Read the code difference, or the vendor's new evidence for a remote server, with first attention on new tools, new dependencies, new destinations, new scopes and new install scripts. |  |
| 79 | quote:l-noproof | A scanner finding nothing does not show how the server will behave. |  |
| 80 | requirement | See what the server says and does when it runs. |  |
| 81 | requirement | A local server for the first time, in a disposable environment. A remote server is called from there with a test account. |  |
| 82 | requirement | Pinned copy or URL |  |
| 83 | requirement | Fake data and canary credentials |  |
| 84 | requirement | Egress proxy |  |
| 85 | requirement | Start with outbound traffic denied and allow only declared destinations. |  |
| 86 | requirement | Capture and hash everything the server tells the model or shows the user. |  |
| 87 | requirement | Run MCP scanners, authentication probes and abuse tests. |  |
| 88 | requirement | Use the tools, then capture again. |  |
| 89 | requirement | Surface hashes, observed behaviour and findings. |  |
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
| 103 | requirement | Every blocking check in this stage passes, and the right approver for the tier has decided. |  |
| 104 | requirement | Decide on the difference. The old record stays valid until it is replaced, revoked or expires. |  |
| 105 | requirement | Let people use what was approved and nothing else. |  |
| 106 | requirement | The approved server, for a first group of users. |  |
| 107 | requirement | Approval record |  |
| 108 | requirement | Platform policy settings |  |
| 109 | requirement | Publish the artifact or URL to the approved source. |  |
| 110 | requirement | Add the allowlist entry and pinned configuration. |  |
| 111 | requirement | Prove that an unapproved server and, for a local server, an unapproved version are refused. |  |
| 112 | requirement | Roll out to a small group first. |  |
| 113 | requirement | Policy change, catalog entry and test evidence. |  |
| 114 | requirement | For a local server, move the pin and the allowlist entry to the new version in stages, and keep the previous version ready for rollback unless it is blocked. |  |
| 115 | quote:l-allowlist | The MCP docs suggest starting with a short allowlist of vetted, pinned servers and clear entry criteria. |  |
| 116 | requirement | Notice any difference from the approval record, and be able to switch the server off. |  |
| 117 | requirement | The approved server, in daily use. |  |
| 118 | requirement | Advisory feeds |  |
| 119 | requirement | Logs and egress alerts |  |
| 120 | requirement | Client configuration inventory |  |
| 121 | requirement | Compare the live surface with the approved hashes. |  |
| 122 | requirement | Match advisories to the SBOM, or to the remote operator's notices. |  |
| 123 | requirement | Watch the publisher and the traffic. |  |
| 124 | requirement | Recertify before expiry, or retire. |  |
| 125 | requirement | Triggers, or a new expiry date, or retirement. |  |
| 126 | requirement | No open trigger and the approval has not expired. |  |
| 127 | requirement | A trigger sends the server back to the stages listed under When something changes. |  |
| 128 | quote:l-rugpull | A server can change its tool descriptions after approval. |  |
| 129 | quote:l-reask | The protocol does not require clients to ask again when definitions change. |  |
| 130 | inference quote:t-listchanged | Change notices cannot be the only detector: sending them is recommended, not required, and depends on a declared capability. |  |
| 131 | requirement | Nine stages run in order. A failed gate stops the server there. Nothing from the server runs before Sandbox. |  |
| 132 | requirement | Release feed or dependency update tool for the package or image. |  |
| 133 | requirement | Keep running the approved, pinned version, unless it is blocked. |  |
| 134 | quote:co-staged | Testing and staged rollout belong in update handling. |  |
| 135 | requirement | A digest check at install fails, or the registry shows a new digest. |  |
| 136 | requirement | Block it and treat it as a possible attack until it is explained. |  |
| 137 | requirement | Hash comparison of the live surface. |  |
| 138 | requirement | Block anything new or changed until approved. Block the whole server if instructions changed. |  |
| 139 | quote:t-change | A tool list may change over time. |  |
| 140 | requirement | Configuration change, vendor notice or a failed connection. |  |
| 141 | requirement | Do not allow the new address until approved. |  |
| 142 | requirement | Advisory feed matched against the SBOM, or a vendor notice. |  |
| 143 | requirement | Decide on exposure at once. Limit or block if it is being exploited. A fix for an exploited vulnerability goes through the New version path without the waiting period. |  |
| 144 | quote:l-pinvuln | A pin keeps the vulnerable version in place until someone moves it. |  |
| 145 | quote:l-respond | For a vulnerable local server, the MCP docs advise blocking its egress, rotating the credentials passed to it and pushing a fixed version. |  |
| 146 | requirement | Malicious package report, vendor or community alert. |  |
| 147 | requirement | Revoke now. Block traffic, find every installation, rotate every credential it could read, and investigate what it did. |  |
| 148 | requirement | Repository transfer, new maintainer, new package account, acquisition. |  |
| 149 | requirement | Freeze a local server at the approved version. Block a remote server until it is screened again. Treat the next version as a new server. |  |
| 150 | requirement | Version difference, consent screen change, egress alert. |  |
| 151 | requirement | Do not grant the new access until approved. |  |
| 152 | quote:bp-semantic | A scope can change meaning without changing name. |  |
| 153 | requirement | Vendor notice or license difference between versions. |  |
| 154 | requirement | Keep using it only where the old terms still cover the use. Otherwise stop. |  |
| 155 | requirement | Repository or registry status, no response to reports. |  |
| 156 | requirement | Plan replacement and set an end date. |  |
| 157 | requirement | Date in the approval record. |  |
| 158 | requirement | Renew before the date. After it, the server is not approved. |  |
| 159 | requirement | Log, egress or canary alert, or a user report. |  |
| 160 | requirement | Block while you investigate. |  |
| 161 | requirement | New data, new users, new client, new configuration, or another server added next to it. |  |
| 162 | requirement | Keep the old use only. |  |
| 163 | requirement | Added, removed or renamed tool |  |
| 164 | requirement | Changed instructions, description, parameter or schema |  |
| 165 | requirement | Changed capability, prompt, resource, icon or UI |  |
| 166 | requirement | Changed read-only or destructive hint |  |
| 167 | requirement | Changed launch command or environment variable |  |
| 168 | requirement | New dependency |  |
| 169 | requirement | New or changed install script |  |
| 170 | requirement | New destination |  |
| 171 | requirement | New scope or permission |  |
| 172 | requirement | Changed publisher or owner |  |
| 173 | requirement | Changed license or terms |  |
| 174 | requirement | A change is any difference from the approval record. Never update a server automatically unless it meets every condition for automatic approval. |  |
| 175 | requirement | Allow it only when all of these are true. It skips the Review stage, so nobody reads the code difference. The approver for the server's tier approves the rule in advance and is the approver of record. Otherwise a person decides. |  |
| 176 | requirement | The server only reads, and only public or non-sensitive data. |  |
| 177 | requirement | A local server runs contained, with limited outbound traffic. |  |
| 178 | requirement | The publisher, license, launch command, environment variables and install scripts are unchanged, and there is no new dependency, destination or scope. |  |
| 179 | requirement | The captured surface is identical. |  |
| 180 | requirement | Every check in Screen, Pin, Scan and Sandbox passes, including the 7 day wait. An earlier result from a person counts only if what that person looked at is unchanged. |  |
| 181 | example | Owner, URL, two tools and read and comment scopes recorded. |  |
| 182 | example | The URL is in the vendor's documentation. Data handling answers arrive in writing. Tier 3, because it writes. |  |
| 183 | example | URL and authorization metadata recorded. |  |
| 184 | example | No code to scan. The vendor shares its scan results, which show no known exploited vulnerability. |  |
| 185 | example | The vendor gives evidence on the checks marked remote, among them token audience, passthrough and logging. |  |
| 186 | example | Surface captured with the two scopes. Permitted probes are refused. Second capture matches. |  |
| 187 | example | Approved for the two tools, for six months, with no other scopes. |  |
| 188 | example | URL allowlisted. A second URL is refused in each client. |  |
| 189 | example | Daily surface comparison starts. |  |
| 190 | example | Fictional example: a team asks for a ticket vendor's own remote server, to read and comment on tickets. |  |
| 191 | example | A developer asks for the package by the name found in a search. |  |
| 192 | example | The vendor's documentation does not name this package, and the publisher account is not the vendor's. Rejected before any download. The package name goes on the deny list. |  |
| 193 | example | Based on a reported case: a package on npm used an email vendor's name without being the vendor's. |  |
| 194 | quote:pm-fake | The vendor reported that the fake package built trust over 15 versions before adding a backdoor. |  |
| 195 | example | New version seen. It waits out the 7 days while the old pin keeps running. |  |
| 196 | example | New digest recorded. Dependencies unchanged. |  |
| 197 | example | No known vulnerability or report. Known-problem scans can be silent on new malicious code. |  |
| 198 | example | The changed send function builds its recipient list in an indirect way. The reviewer does not see the added copy. |  |
| 199 | example | A test message arrives with a recipient nobody asked for. The version is rejected and reported. The server is now handled as reported malicious: the old approval is revoked too and its credentials are rotated. |  |
| 200 | example | Fictional example using the same technique: an approved mail server publishes a new version that copies every message to an outside address. |  |
| 201 | example | Request recorded. |  |
| 202 | example | Publisher and source are in order. |  |
| 203 | example | Version and digest recorded. |  |
| 204 | example | Traditional scans find nothing. The problem is text, not a vulnerable library. |  |
| 205 | example | No code flaw found. |  |
| 206 | example | Reading every captured field shows the instruction. Rejected. |  |
| 207 | example | Fictional example: a note taking server whose parameter description tells the model to read a key file and pass it along. |  |
| 208 | quote:inv-poison | Instructions hidden in tool descriptions can be invisible to users and visible to models. |  |
| 209 | example | The hash comparison reports a new tool whose description says it sends data to an outside storage service. The gateway or client blocks it. |  |
| 210 | example | A new destination also counts as more permissions. The vendor states in writing what goes to the storage service and how long it is kept. |  |
| 211 | example | No code to read. The new tool and its destination are compared with the stated purpose. |  |
| 212 | example | The new tool is captured and tested with the other approved servers in mind. |  |
| 213 | example | A new destination means a person decides. Approved only for non-sensitive projects. |  |
| 214 | example | New hashes and condition published. |  |
| 215 | example | Fictional example: an approved remote server starts listing a new export tool. No version number changes. |  |
| 216 | example | The advisory matches a stored SBOM. Configuration inventory shows who runs it. |  |
| 217 | example | The approved version is affected, and in this example the flaw is being exploited. It is blocked, and exposed credentials are rotated. |  |
| 218 | example | The fixed version is not reported as malicious. The 7 day wait is skipped and recorded. |  |
| 219 | example | The fixed version is fetched without running it, pinned and verified. |  |
| 220 | example | The fixed version no longer matches the advisory, and the malware scan is clean. |  |
| 221 | example | The code difference holds the fix and nothing undeclared. |  |
| 222 | example | Surface and behaviour compared with the old approval. |  |
| 223 | example | The fixed version is approved. |  |
| 224 | example | Pin and allowlist moved. The old version is refused. |  |
| 225 | example | Based on a published vulnerability in mcp-remote, a bridge that connects local clients to remote servers. |  |
| 226 | quote:cv-6514 | The flaw let an untrusted server run operating system commands on the client machine. |  |
| 227 | requirement | Publisher is identified |  |
| 228 | requirement | Trace the server to a source repository and a real organisation or maintainer. For a remote server, trace the URL to its operator. |  |
| 229 | requirement | A named, reachable publisher, confirmed from more than the listing itself. |  |
| 230 | requirement | It is the package the vendor means |  |
| 231 | requirement | Take the name or URL from the vendor's own documentation and compare it letter by letter. |  |
| 232 | requirement | Name, publisher account and URL match the vendor's documentation. |  |
| 233 | requirement | Source can be read |  |
| 234 | requirement | Find the source that the published artifact is built from. |  |
| 235 | requirement | Source is available for the exact version. |  |
| 236 | requirement | Project is maintained |  |
| 237 | requirement | Look at recent commits, releases, open security issues and whether the project is archived. |  |
| 238 | requirement | Not archived, and security reports get answered. |  |
| 239 | requirement | There is a way to report vulnerabilities |  |
| 240 | requirement | Look for a security policy and past advisories. |  |
| 241 | requirement | A reporting route exists. |  |
| 242 | requirement | License allows the use |  |
| 243 | requirement | Read the license or the service terms. |  |
| 244 | requirement | Terms allow the intended use. |  |
| 245 | requirement | New versions have aged |  |
| 246 | requirement | Wait until a new version has been public for 7 days. Skip the wait for a fix to a vulnerability that is being exploited. |  |
| 247 | requirement | The version is old enough, or the exception is recorded. |  |
| 248 | requirement | Not reported as malicious |  |
| 249 | requirement | Look up the package and version in malicious package reports. Repeat for every dependency once the tree is known. |  |
| 250 | requirement | No report for the package or any dependency. |  |
| 251 | label | Requirement of this process. No source is quoted. |  |
| 252 | requirement | Remote operator gives assurance |  |
| 253 | requirement | Ask who runs the service, where data goes, how long it is kept, how incidents are announced and how changes are announced. |  |
| 254 | requirement | Written answers that fit the data involved. |  |
| 255 | requirement | Running it locally is justified |  |
| 256 | requirement | Use the remote version where one exists and the server needs no local access. Ask why a server with no need for local access is only offered as a local process. |  |
| 257 | requirement | A stated reason for local execution. |  |
| 258 | requirement | Exact version |  |
| 259 | requirement | Name one version. No ranges, no latest, no floating tag. |  |
| 260 | requirement | One immutable version in the request and the configuration. |  |
| 261 | requirement | Digest recorded |  |
| 262 | requirement | Record the artifact hash. Refer to a container image by digest. |  |
| 263 | requirement | Digest in the approval record. |  |
| 264 | requirement | Fetched without running it |  |
| 265 | requirement | Fetch into quarantine with install scripts off. For Python, accept built packages only. |  |
| 266 | requirement | No code from the package ran during the fetch. |  |
| 267 | requirement | Dependencies locked and listed |  |
| 268 | requirement | Lock the whole dependency tree with hashes and generate your own SBOM from the artifact. |  |
| 269 | requirement | Lock file with hashes and an SBOM are stored. |  |
| 270 | requirement | Signatures and provenance verified |  |
| 271 | requirement | Verify signatures and attestations against the expected publisher and source. An invalid signature or attestation blocks. If the publisher offers none, the approver decides and records it. |  |
| 272 | requirement | Verification succeeds for the expected identity, or the approver has accepted that none is offered. |  |
| 273 | requirement | Remote endpoint recorded |  |
| 274 | requirement | Record the exact URL and the authorization server details. Require HTTPS with a valid certificate throughout. |  |
| 275 | requirement | URL and metadata recorded, with no plain HTTP and no certificate error. |  |
| 276 | requirement | Known vulnerabilities |  |
| 277 | requirement | Scan the artifact and all dependencies. Rank by known exploitation, exploit probability and reachability. Ask a remote vendor for its results. |  |
| 278 | requirement | No known exploited vulnerability. Others have an owner and a deadline. |  |
| 279 | requirement | Malicious code signs |  |
| 280 | requirement | Run a malicious package scanner as well as the vulnerability scan. |  |
| 281 | requirement | Findings explained or the server rejected. |  |
| 282 | requirement | Static code analysis |  |
| 283 | requirement | Analyze the source for injection, path, request forgery and similar flaws. |  |
| 284 | requirement | No unresolved serious finding. |  |
| 285 | requirement | Secrets in code and images |  |
| 286 | requirement | Scan source, package and image layers for credentials. |  |
| 287 | requirement | No live secret. |  |
| 288 | requirement | Container and deployment settings |  |
| 289 | requirement | Scan the image build file and deployment files for risky settings such as root user, host mounts and broad privileges. |  |
| 290 | requirement | No unexplained risky setting. |  |
| 291 | requirement | Install and build scripts read |  |
| 292 | requirement | List every script that runs at install, build or start, and read it. |  |
| 293 | requirement | Each script is understood and needed. |  |
| 294 | requirement | Binaries and hidden code |  |
| 295 | requirement | Look for bundled binaries, downloads at run time, obfuscated code and files that do not match the source. |  |
| 296 | requirement | Everything executable traces to the source or a verified origin. |  |
| 297 | requirement | Dependency confusion |  |
| 298 | requirement | Resolve internal package names only from the internal registry, and fetch public ones through a mirror. |  |
| 299 | requirement | No internal name can resolve from a public registry. |  |
| 300 | requirement | No command or code injection |  |
| 301 | requirement | Check that model or user input never reaches a shell or code evaluator. |  |
| 302 | requirement | No path from input to shell, eval or string-built command. |  |
| 303 | requirement | File access stays inside bounds |  |
| 304 | requirement | Check path handling, including symlinks and prefix comparisons. |  |
| 305 | requirement | Resolved paths cannot leave the allowed folders. |  |
| 306 | requirement | No open URL fetching |  |
| 307 | requirement | Check every place the server fetches a URL that came from the model or a user. |  |
| 308 | requirement | Destinations are allowlisted, and private and metadata addresses are refused. |  |
| 309 | requirement | Tokens are checked for audience |  |
| 310 | requirement | Check that the server rejects tokens issued for something else. |  |
| 311 | requirement | A token for another service is refused. |  |
| 312 | requirement | No token passthrough |  |
| 313 | requirement | Check that the server never forwards the caller's token to another service. |  |
| 314 | requirement | Downstream calls use their own credentials. |  |
| 315 | requirement | Proxy servers ask consent per client |  |
| 316 | requirement | If the server signs in to a third party on behalf of many clients, check consent handling. |  |
| 317 | requirement | Consent is stored and checked for each client. |  |
| 318 | requirement | Sign-in links are handled safely |  |
| 319 | requirement | For a bridge or bundled client, check how it treats URLs received from a server. |  |
| 320 | requirement | Only safe schemes are opened, never through a shell, and private and reserved addresses are not fetched. |  |
| 321 | requirement | Least privilege |  |
| 322 | requirement | Compare requested scopes, file access and permissions with the stated purpose. Give a server meant only to read a read-only account at the data source. |  |
| 323 | requirement | No wildcard scope, nothing without a reason, and any read-only limit is enforced by the data source. |  |
| 324 | requirement | HTTP endpoint is not open |  |
| 325 | requirement | For any server that listens over HTTP, check Origin and Host header validation, listening address and authentication. |  |
| 326 | requirement | Origin and Host are checked, local servers listen on localhost only, and callers authenticate. |  |
| 327 | requirement | Callers cannot claim an identity |  |
| 328 | requirement | Check that identity comes from a verified token, not from a state handle or anything the client typed. |  |
| 329 | requirement | Knowing a handle or naming a user gives no access. |  |
| 330 | requirement | No secrets asked in forms |  |
| 331 | requirement | Check what the server asks the user for during use. |  |
| 332 | requirement | Passwords, keys, tokens and payment data are never requested in form mode. |  |
| 333 | requirement | Basic tool protections |  |
| 334 | requirement | Check input validation, access control, rate limits and output cleaning. |  |
| 335 | requirement | All four are present. |  |
| 336 | requirement | Usable logs without secrets |  |
| 337 | requirement | Check that tool calls can be logged and that secrets are masked. |  |
| 338 | requirement | Calls are logged in a structured form without secrets. |  |
| 339 | requirement | No stored secrets |  |
| 340 | requirement | Check code, defaults and sample configuration for built-in credentials, and check how the server stores the tokens it holds. |  |
| 341 | requirement | Credentials come from a secret store, one narrow credential per server, and held tokens are not in plain text. |  |
| 342 | requirement | Code does only what is declared |  |
| 343 | requirement | Read the code, or the difference from the approved version, for data sent anywhere, hidden recipients, extra file or credential access, and behaviour that depends on time or environment. |  |
| 344 | requirement | Every outbound send and sensitive access serves a declared purpose. |  |
| 345 | requirement | Launch command is clean |  |
| 346 | requirement | Read the exact command, arguments and environment variables that start the server. |  |
| 347 | requirement | No chained commands, no sudo, and no unexplained network or file operation. |  |
| 348 | requirement | Sign-in service meets the OAuth rules |  |
| 349 | requirement | For a server that uses OAuth, check the authorization server metadata and redirect handling. |  |
| 350 | requirement | PKCE support is advertised, redirect URIs must match exactly, sign-in responses name the issuer, and access tokens are short-lived. |  |
| 351 | requirement | Links sent to users are safe |  |
| 352 | requirement | If the server sends users to a web page during use, check the URL and who the page accepts input from. |  |
| 353 | requirement | HTTPS, no personal data or pre-authenticated access in the URL, and the server confirms that the person opening it is the person who asked. |  |
| 354 | requirement | Model requests by the server are justified |  |
| 355 | requirement | Check whether the server asks the client to run a model. This is called sampling, and the specification has deprecated it. |  |
| 356 | requirement | It does not, or the reason is recorded and the client lets a person deny each request. |  |
| 357 | inference | For a remote server, isolation protects your side only. The server's side stays out of reach. |  |
| 358 | requirement | Isolated and disposable |  |
| 359 | requirement | Run in a throwaway environment with no production credentials or data and outbound traffic denied by default. |  |
| 360 | requirement | Nothing of value is reachable from the test. |  |
| 361 | requirement | Whole surface captured and hashed |  |
| 362 | requirement | Capture declared capabilities, server instructions, tools with full schemas and annotations, prompts, resources, resource templates, UI content and icons, using a test account with the same scopes as production. |  |
| 363 | requirement | A hash for every item is in the record. |  |
| 364 | requirement | No instructions aimed at the model |  |
| 365 | requirement | Read every text field, including parameter names, schema descriptions and comments. |  |
| 366 | requirement | Nothing tells the model to do what the tool's purpose does not need. |  |
| 367 | requirement | No hidden characters |  |
| 368 | requirement | Search the captured text for zero-width and direction-control characters. |  |
| 369 | requirement | None present, or each one explained. |  |
| 370 | requirement | MCP scanner |  |
| 371 | requirement | Run at least one MCP scanner inside the sandbox. Check first what it sends outside your network. |  |
| 372 | requirement | Findings triaged. A clean result counts as one input, not as approval. |  |
| 373 | requirement | No shadowing or name clashes |  |
| 374 | requirement | Compare names and descriptions with the other approved servers. Check that names use only the characters the specification lists. |  |
| 375 | requirement | No duplicate or look-alike tool name, no unusual character, and no text about another server's tools. |  |
| 376 | requirement | No dangerous combination |  |
| 377 | requirement | Check whether this server, with the others in use, joins untrusted content, private data and a way to send data out. |  |
| 378 | requirement | The combination is absent, or limited by a condition in the approval. |  |
| 379 | requirement | Annotations match behaviour |  |
| 380 | requirement | Compare read-only and destructive hints with what the tool does. |  |
| 381 | requirement | No hint understates the effect. |  |
| 382 | requirement | Network, file and process activity as declared |  |
| 383 | requirement | Watch traffic, files and processes. Place canary files and credentials. |  |
| 384 | requirement | No undeclared destination or access, and no canary used. |  |
| 385 | inference quote:pm-fake | This comparison would show an added hidden recipient, as in the reported Postmark look-alike case. |  |
| 386 | requirement | Outbound content matches the request |  |
| 387 | requirement | For tools that send or write, compare what arrived with what the call asked for: recipients, fields, attachments. |  |
| 388 | requirement | Nothing added, removed or redirected. |  |
| 389 | requirement | Get the permission described under D12 first. |  |
| 390 | requirement | Authentication probes |  |
| 391 | requirement | For a server that listens over HTTP, call without a token, with a token for another service and with a foreign Origin. |  |
| 392 | requirement | Every such call is refused. |  |
| 393 | requirement | Get the operator's written permission before running this check or D11 against a server you do not run. Without it, do not run them; the operator's own test results are then the evidence. |  |
| 394 | requirement | Abuse tests |  |
| 395 | requirement | Send path traversal, injection, internal address, oversized and malformed inputs. |  |
| 396 | requirement | No test succeeds and the server stays up. |  |
| 397 | requirement | Second capture is the same |  |
| 398 | requirement | Use the tools, wait, reconnect and capture again. |  |
| 399 | requirement | Hashes match, or each change has an accepted reason. |  |
| 400 | requirement | Schemas, icons and headers are safe |  |
| 401 | requirement | Look for references to network addresses in schemas, unsafe icon addresses, and sensitive parameters copied into HTTP headers. |  |
| 402 | requirement | No network reference, only safe icon schemes, and no password, key, token or personal data marked x-mcp-header. |  |
| 403 | requirement | Interactive UI reviewed |  |
| 404 | requirement | If the server ships UI, review its code and the domains it declares, and hash it. |  |
| 405 | requirement | Declared domains are needed and narrow, and the UI hash is recorded. |  |
| 406 | requirement | Risk tier assigned |  |
| 407 | requirement | Set the tier from what the server can do. |  |
| 408 | requirement | Tier and reason recorded. |  |
| 409 | requirement | Every finding has an outcome |  |
| 410 | requirement | Fix, accept with an owner and end date, or reject. Known malicious code gets no exception. |  |
| 411 | requirement | No finding without an outcome. |  |
| 412 | requirement | Approver is not the requester |  |
| 413 | requirement | Have a different person approve. For an automatic approval, that person is whoever approved the rule. |  |
| 414 | requirement | No approver is the requester. |  |
| 415 | requirement | Conditions and expiry set |  |
| 416 | requirement | Write the limits of the approval and the date it ends. |  |
| 417 | requirement | An expiry date is on the record. |  |
| 418 | requirement | Record complete |  |
| 419 | requirement | Fill in every field of the approval record that applies and register the server. |  |
| 420 | requirement | The record and the catalog entry exist. |  |
| 421 | requirement | Served from the approved source |  |
| 422 | requirement | Install from the internal registry or the recorded URL, and block direct public downloads where you can. |  |
| 423 | requirement | Clients get only what was approved. |  |
| 424 | requirement | Allowlist matches URL or command |  |
| 425 | requirement | Allow by remote URL or exact command. Do not rely on a server name. |  |
| 426 | requirement | A renamed unapproved server is refused. |  |
| 427 | requirement | Configuration is pinned |  |
| 428 | requirement | For a local server, put the version or digest in the managed configuration. Take credentials from a secret store, and pass each server only its own. |  |
| 429 | requirement | No floating version, no secret in a configuration file and no credential the server does not need. |  |
| 430 | requirement | Contained at run time |  |
| 431 | requirement | Run local servers in a container or sandbox with only the needed folder, read-only where possible, and limit outbound traffic per server. |  |
| 432 | requirement | Access and destinations match the approval. |  |
| 433 | requirement | Block is proven |  |
| 434 | requirement | Try to start an unapproved server, and for a local server an unapproved version, in each client. |  |
| 435 | requirement | Each attempt is refused, with evidence stored. |  |
| 436 | requirement | Definition changes are stopped |  |
| 437 | requirement | Use a client that asks again, or a gateway that blocks, when definitions differ from the approved hashes. |  |
| 438 | requirement | A changed definition cannot be used silently. |  |
| 439 | requirement | Spending is capped |  |
| 440 | requirement | If a tool can spend money, set limits outside the model. |  |
| 441 | requirement | The paying component enforces a limit per payment and a total per time period. |  |
| 442 | requirement | Definition drift |  |
| 443 | requirement | Capture the live surface on a schedule and on each reconnect where possible, and compare hashes. |  |
| 444 | requirement | Hashes equal the approved ones. |  |
| 445 | requirement | New advisories |  |
| 446 | requirement | Daily, match new vulnerability and malicious package reports against each stored SBOM. For a remote server, check the operator's security notices. |  |
| 447 | requirement | No unhandled match or notice. |  |
| 448 | requirement | Upstream changes |  |
| 449 | requirement | Follow releases, ownership, maintainers, deprecation and takedown of each approved server. |  |
| 450 | requirement | No unreviewed change. |  |
| 451 | requirement | Traffic and logs |  |
| 452 | requirement | Alert on new destinations, unusual volume and unexpected tool calls. |  |
| 453 | requirement | Alerts have an owner and are handled. |  |
| 454 | requirement | Recertification |  |
| 455 | requirement | Re-assess before the expiry date. When a server is retired, remove its allowlist entry and rotate what it held. |  |
| 456 | requirement | Renewed or retired on time. |  |
| 457 | requirement | Switch-off and rollback tested |  |
| 458 | requirement | Keep a way to block the server everywhere and rotate its credentials, and for a local server to return to the previous version. Rehearse it. |  |
| 459 | requirement | A rehearsal has worked within the target time. |  |
| 460 | requirement | Unapproved servers found |  |
| 461 | requirement | Collect client configurations and compare them with the catalog. |  |
| 462 | requirement | Every configured server is approved. |  |
| 463 | quote:osv-use | OSV-Scanner |  |
| 464 | quote:gd-use,om-reports | GuardDog, OpenSSF reports |  |
| 465 | quote:ql-use | CodeQL |  |
| 466 | quote:gl-use,tv-secrets | Gitleaks, Trivy |  |
| 467 | quote:tv-iac | Trivy |  |
| 468 | quote:ci-engines,as-sends | Cisco MCP Scanner, Snyk Agent Scan |  |
| 469 | requirement | The server or version being assessed cannot move on until this is fixed. If the failing one is already in use, it is suspended, unless a change trigger says what to do instead. |  |
| 470 | requirement | The approver decides and records why. |  |
| 471 | requirement | Pick at least one tool for each job. Other tools can do the same jobs. |  |
| 472 | label | Look-alike or impersonating server |  |
| 473 | inference | A publisher that is real but dishonest passes identity checks. |  |
| 474 | label | Malicious package |  |
| 475 | inference quote:l-noproof | New malicious code with no report yet can pass scans and stay quiet in a test. |  |
| 476 | label | Publisher account or ownership takeover |  |
| 477 | inference quote:npm-prov | A release made with the real publisher's own build system can carry valid provenance. |  |
| 478 | label | Known vulnerability |  |
| 479 | inference | Flaws that nobody has published are not matched. |  |
| 480 | label | Compromised dependency |  |
| 481 | inference | A locked but already compromised dependency stays locked in. |  |
| 482 | label | Dependency confusion |  |
| 483 | inference | Names that no registry rule covers can still resolve publicly. |  |
| 484 | label | Install or build script abuse |  |
| 485 | inference | A script that is needed for install still has to run later. |  |
| 486 | label | Floating version or moving tag |  |
| 487 | inference | A remote server cannot be pinned by digest. |  |
| 488 | label | Tool poisoning in any schema field |  |
| 489 | inference | Wording that looks innocent to a reviewer and a scanner can still steer a model. |  |
| 490 | label | Hidden characters |  |
| 491 | inference | Meaning can be hidden without any special character. |  |
| 492 | label | Shadowing another server's tools |  |
| 493 | inference quote:l-shared | All configured servers share one model context, so each server added later changes what the others are exposed to. |  |
| 494 | label | Definitions changed after approval (rug pull) |  |
| 495 | inference | Between two comparisons a change can be used unnoticed. |  |
| 496 | label | Behaviour changed behind unchanged definitions |  |
| 497 | quote:c-hashlimit | Hashing definitions does not see it. |  |
| 498 | label | Prompt injection through results and resources |  |
| 499 | quote:c-response | Every tool response has to be treated as untrusted data, also from approved servers. |  |
| 500 | label | Data leaving through a chain of tools |  |
| 501 | inference | A permitted destination can be used to take data out. |  |
| 502 | label | Server asks the client to run a model |  |
| 503 | inference | How each request is shown and limited is up to the client. |  |
| 504 | label | Malicious startup command |  |
| 505 | inference | A command that looks ordinary can still fetch hostile code. |  |
| 506 | label | Command or code injection |  |
| 507 | inference | Analysis and tests miss some paths. |  |
| 508 | label | Path traversal and symlink escape |  |
| 509 | inference | Anything inside the mounted folder stays reachable. |  |
| 510 | label | Server-side request forgery |  |
| 511 | inference | Redirects and name resolution tricks need their own tests. |  |
| 512 | label | Command execution from a sign-in link |  |
| 513 | inference | The same flaw in a client is outside this process. |  |
| 514 | label | Undeclared network, file or process activity |  |
| 515 | inference | Behaviour triggered by time, data or environment may not show in a test. |  |
| 516 | label | Resource exhaustion |  |
| 517 | inference | Load limits of a remote service are the vendor's to hold. |  |
| 518 | label | Missing authentication or open local endpoint |  |
| 519 | quote:l-reachable | A local server that listens on a port can be reached by other local processes and by websites. |  |
| 520 | label | DNS rebinding |  |
| 521 | inference | Later code changes can remove the check. |  |
| 522 | label | Token passthrough and wrong audience |  |
| 523 | inference | For a remote server you rely on the vendor for what happens downstream. |  |
| 524 | label | Confused deputy |  |
| 525 | inference | Hard to prove from outside for a remote server. |  |
| 526 | label | Excess or creeping scopes |  |
| 527 | inference quote:bp-semantic | A scope can widen on the service side without any change in the server. |  |
| 528 | label | Identity spoofing and state handle misuse |  |
| 529 | inference | Hard to test fully from outside. |  |
| 530 | label | Weak sign-in service (code theft, redirect, mix-up) |  |
| 531 | inference | Client side defences against these attacks belong to the client. |  |
| 532 | label | Secret exposure |  |
| 533 | quote:l-reach | A credential the server needs is readable by the server. |  |
| 534 | label | Phishing for secrets through user prompts |  |
| 535 | inference | Ordinary looking questions can still collect sensitive data. |  |
| 536 | label | Hostile or leaking server UI |  |
| 537 | inference | UI loaded later from an allowed domain can change. |  |
| 538 | label | Escape from the local environment |  |
| 539 | quote:co-container | A container should not be relied on as a strong security boundary. |  |
| 540 | label | Too little logging |  |
| 541 | inference | A remote server's internal actions are not in your logs. |  |
| 542 | label | Shadow servers |  |
| 543 | inference | Unmanaged devices and clients that ignore policy are not seen. |  |
| 544 | label | Context shared too widely |  |
| 545 | inference | How a client keeps and shares context is decided by the client, not at intake. |  |
| 546 | label | Uncontrolled spending |  |
| 547 | inference | Unwanted payments can still be made inside the limits. |  |
| 548 | inference | Matching a check to an attack is a design choice. It is not a measured detection rate, and the list of attacks is not complete. |  |
| 549 | requirement | Reads only public or non-sensitive data. Remote. |  |
| 550 | requirement | Platform owner |  |
| 551 | requirement | 12 months |  |
| 552 | requirement | Reads internal or personal data. |  |
| 553 | requirement | Platform owner and security reviewer |  |
| 554 | requirement | 6 months |  |
| 555 | requirement | Changes data, sends data outward, or runs as a local process. |  |
| 556 | requirement | Security reviewer and data owner |  |
| 557 | requirement | Runs commands or code, spends money, or holds administrator or production access. |  |
| 558 | requirement | Security reviewer and system owner |  |
| 559 | requirement | 3 months |  |
| 560 | requirement | Released as recorded. |  |
| 561 | requirement | Released with limits that the platform or the owner enforces, such as fewer tools, fewer scopes, named users or a sandbox. |  |
| 562 | requirement | Added to the deny list when the reason is malicious or impersonation. |  |
| 563 | requirement | Nothing is released until the missing evidence arrives. |  |
| 564 | requirement | Use the highest tier that fits. Adjust the names and intervals to your organisation. |  |
| 565 | example | Keep one record for each approved server. Later changes are compared with it. For a remote server, origin holds the URL and the authorization server details instead. The example is fictional. |  |
| 566 | example | {<br>  "name": "example-tickets-mcp",<br>  "publisher": {"organisation": "Example Vendor", "verified_from": "vendor documentation URL"},<br>  "license": "<license or terms accepted>",<br>  "owner": "team-support",<br>  "origin": {<br>    "type": "package",<br>    "package": "@example/tickets-mcp",<br>    "version": "2.4.1",<br>    "digest": "sha512-<digest of the artifact>",<br>    "source_commit": "<commit>",<br>    "provenance": "verified"<br>  },<br>  "dependencies": {"lock_hash": "sha256-<hash>", "sbom": "<stored SBOM>"},<br>  "surface": {<br>    "captured_with_scopes": ["tickets:read", "tickets:comment"],<br>    "instructions": "sha256-<hash>",<br>    "tools": {"get_ticket": "sha256-<hash>", "add_comment": "sha256-<hash>"},<br>    "capabilities": {},<br>    "prompts": {},<br>    "resources": {},<br>    "resource_templates": {},<br>    "icons": {},<br>    "ui": {}<br>  },<br>  "runtime": {<br>    "command": ["<exact command and arguments>"],<br>    "credentials": "<secret store reference>",<br>    "files": ["<allowed folders>"],<br>    "destinations": ["tickets.example.com:443"],<br>    "environment": ["<variable names and values, without secrets>"]<br>  },<br>  "use": {"purpose": "<what it is used for>", "data": "<data it may reach>", "users": "<who may use it>", "clients": ["<approved clients>"]},<br>  "findings": "<link to triaged results>",<br>  "exceptions": ["<such as a skipped waiting period or a missing signature, and who accepted it>"],<br>  "tier": 3,<br>  "decision": "approved with conditions",<br>  "conditions": ["get_ticket and add_comment only"],<br>  "requested_by": "<person>",<br>  "approved_by": ["<security reviewer>", "<data owner>"],<br>  "decided": "2026-11-26",<br>  "expires": "2027-05-26"<br>} |  |
| 567 | label | Server name, URL or command. |  |
| 568 | quote:gh-match | Entries match by name, URL or command. |  |
| 569 | quote:gh-profiles | The lists do not apply to servers defined in repository custom agent profiles. |  |
| 570 | quote:gh-firewall | An organization or repository firewall that blocks the domains needed to start those servers can prevent their use. |  |
| 571 | quote:gh-malformed | A malformed list blocks all but the built-in servers. |  |
| 572 | label | Server name or ID. |  |
| 573 | preview quote:gh-preview | It is in public preview and not the recommended way to restrict servers. |  |
| 574 | quote:gh-ga | The recommended way is the managed settings file. |  |
| 575 | quote:gh-name | Name matching can be bypassed by editing configuration. |  |
| 576 | label | Server URL, exact command or name. |  |
| 577 | quote:cc-authoritative | An allowlist is authoritative only when it is also set to managed entries only. |  |
| 578 | quote:cc-exact | A command entry matches the exact command. |  |
| 579 | quote:cc-env | A command entry matches whatever the server's environment variables are. |  |
| 580 | quote:cc-envload | Some environment variables change what node loads at startup. |  |
| 581 | quote:cc-name | A name entry is not a security control. |  |
| 582 | label | Managed Copilot settings, workspace trust and a per-server sandbox. |  |
| 583 | quote:vs-allow | Managed settings can limit which servers developers install and run. |  |
| 584 | quote:vs-disabled,vs-harness | Managed settings keep the Claude and Codex harnesses disabled unless they are permitted. Permitted sessions run without Copilot's managed permission, sandbox, MCP and plugin controls. |  |
| 585 | quote:vs-workspace,vs-restart | In a trusted workspace, servers configured in the workspace can start without a separate trust prompt, also after a configuration change. |  |
| 586 | quote:vs-sandbox,vs-windows | The per-server sandbox covers local process servers on macOS and Linux, not on Windows. |  |
| 587 | quote:vs-separate,vs-outbound | The separate Copilot sandbox allows outbound traffic by default. |  |
| 588 | label | A public list of servers. |  |
| 589 | preview quote:reg-preview | It is in preview. |  |
| 590 | quote:reg-moderation | Expect little or no moderation. |  |
| 591 | quote:reg-vulns | Having a security vulnerability does not by itself get a server removed. |  |
| 592 | label | Destinations per server. |  |
| 593 | quote:l-egress | A per-server egress list with alerts limits where a server can send data. |  |
| 594 | label | Client configuration files on devices. |  |
| 595 | quote:l-inventory | Management tools can collect client configurations to find what is in use. |  |
| 596 | requirement | A weak client can undo a well reviewed server. Assess clients separately. |  |
| 597 | requirement | A proxy or other component that handles decrypted messages could change or replay them. Assess it with the platform. |  |
| 598 | requirement | Per-call approval prompts, output filtering and permission controls during use belong to the platform and agent design. |  |
| 599 | requirement | Its code, build and staff are visible only through the vendor's evidence. |  |
| 600 | requirement | License and data answers are collected here. Contracts and privacy review follow your normal process. |  |
| 601 | inference quote:gh-match,cc-exact,cc-env | None of the allowlist settings above compares a server's code or tool definitions with what was reviewed. This process has to do that. |  |
<!-- /ledger -->
