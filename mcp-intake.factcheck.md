# MCP server intake: fact check

## Simplified guide, 2026-11-26

- Verified all 181 quotes against their sources. The nine revised statements describe the existing intake procedure. The 570 retained statements with blank verdicts still need review.
- Verified all 185 existing fragment IDs, links within the site and generated page output.
- Tested the overview, native disclosures and representative shared links in Chrome at 1280, 390 and 320 pixels. Keyboard activation and disclosures without JavaScript worked. No horizontal page overflow or console errors.

<!-- ledger -->
| # | Basis | Statement | Verdict |
|---|---|---|---|
| 1 | requirement | Record the owner, purpose, data and access needed. Check the approved catalog and verify the publisher before downloading or connecting. | OK (2026-11-26). Restates the existing intake procedure. |
| 2 | requirement | Pin the local artifact and dependencies, or record the remote URL and get vendor evidence. Scan for vulnerabilities and malware, review tools and permissions, then test in isolation with test data. | OK (2026-11-26). Restates the existing intake procedure. |
| 3 | requirement | Have an independent approver review the findings. Record the approved configuration, limits and expiry. Roll it out to a small group first. | OK (2026-11-26). Restates the existing intake procedure. |
| 4 | requirement | Compare live tool definitions with the approval record and track vulnerability alerts. Reassess changes before allowing them. Suspend access if you suspect compromise. | OK (2026-11-26). Restates the existing intake procedure. |
| 5 | requirement | Review new servers before use and reassess them when they change. | OK (2026-11-26). Restates the existing intake procedure. |
| 6 | requirement | Purpose and named owner |  |
| 7 | requirement | Link to the vendor's own documentation |  |
| 8 | requirement | Exact version, image digest or URL |  |
| 9 | requirement | Transport: local process or HTTP |  |
| 10 | requirement | Data it will reach |  |
| 11 | requirement | Tools wanted |  |
| 12 | requirement | Credentials and scopes |  |
| 13 | requirement | Look in the approved catalog first. If an approved server covers the need, use it. |  |
| 14 | requirement | Install nothing. |  |
| 15 | requirement | Nothing from the server. |  |
| 16 | requirement | A request record. |  |
| 17 | requirement | Every input is filled in and an owner has accepted the role. |  |
| 18 | quote:l-run | A local server is downloaded code that runs under your user account. |  |
| 19 | quote:t-authz | Which tools a server lists can depend on the access it is given, so the requested scopes belong in the request. |  |
| 20 | requirement | Request record |  |
| 21 | requirement | Publisher, repository and registry pages |  |
| 22 | requirement | Malicious package reports |  |
| 23 | requirement | Run the hygiene checks. |  |
| 24 | requirement | Give the server a provisional risk tier. |  |
| 25 | requirement | Stop at the first check marked Block that fails. |  |
| 26 | requirement | Nothing from the server. This is desk work. |  |
| 27 | requirement | Go or stop, with a provisional tier. |  |
| 28 | requirement | No blocking hygiene check has failed. |  |
| 29 | quote:l-listing | A listing on a registry is not an endorsement. |  |
| 30 | quote:vs-trust | Trusting a publisher does not show that every tool result is safe. |  |
| 31 | quote:l-popular | Popularity or a good name does not show that a package is safe or current. |  |
| 32 | requirement | Exact version, image or URL |  |
| 33 | requirement | Local or container: fetch into quarantine or an internal mirror, record digests, lock the dependency tree and build an SBOM. |  |
| 34 | requirement | Remote: record the URL, the certificate-protected connection and the authorization metadata. |  |
| 35 | requirement | Verify signatures and provenance. |  |
| 36 | requirement | On a change, compare the new local dependency tree and install scripts with the approved ones. For a remote server, record the endpoint details again. | OK (2026-11-26). Restates the existing intake procedure. |
| 37 | requirement | Only the fetch tool, in a quarantine area. No install scripts. |  |
| 38 | requirement | Digests, lock file, SBOM and provenance result, or the remote endpoint details. |  |
| 39 | requirement | Every blocking check in this stage passes. |  |
| 40 | quote:l-toponly | Pinning a package version with a launcher such as npx or uvx fixes only the top package. Its dependencies are usually resolved again at install. |  |
| 41 | quote:slsa-l1 | Provenance at the first SLSA build level is easy to bypass or forge. |  |
| 42 | inference quote:d-selfreport | A server's own name and version are self-reported. Identify it by digest or URL. |  |
| 43 | requirement | Quarantined copy |  |
| 44 | requirement | SBOM |  |
| 45 | requirement | Run the vulnerability, malware, code, secret and configuration scans. |  |
| 46 | requirement | Scan the locked dependency list and the SBOM. Do not let a scanner install the package. |  |
| 47 | requirement | Triage every finding: exploited, reachable, fix available. |  |
| 48 | requirement | For a new version, run all scans again or get fresh results from the remote vendor. Report what differs from the approved version. | OK (2026-11-26). Restates the existing intake procedure. |
| 49 | requirement | Scanners, in an isolated job without secrets. |  |
| 50 | requirement | Findings with a disposition each. |  |
| 51 | quote:pa-static | pip-audit is not a static code analyzer. |  |
| 52 | quote:pa-exec,pa-equiv | pip-audit -r can run code from what it audits, so isolate the scan job. |  |
| 53 | quote:pa-nopip | Given a hashed requirements file, pip-audit can skip pip's dependency resolution with --disable-pip. |  |
| 54 | requirement | Source code |  |
| 55 | requirement | Configuration and launch command |  |
| 56 | requirement | Scan findings |  |
| 57 | requirement | Go through the MCP review checks. |  |
| 58 | requirement | Remote: there is no code to read. Ask the vendor for evidence on each check marked remote, and test what you can in Sandbox. |  |
| 59 | requirement | Scale the depth to the tier. |  |
| 60 | requirement | On a change, read the code diff or the remote vendor's new evidence. Check for changes to tools, dependencies, destinations, scopes and install scripts. | OK (2026-11-26). Restates the existing intake procedure. |
| 61 | requirement | Nothing from the server. People and tools read code and settings. |  |
| 62 | requirement | Review findings. |  |
| 63 | requirement | Every blocking check in this stage passes. For a remote server, the vendor's evidence can show that it passes. |  |
| 64 | quote:l-noproof | A scanner finding nothing does not show how the server will behave. |  |
| 65 | requirement | Pinned copy or URL |  |
| 66 | requirement | Fake data and canary credentials |  |
| 67 | requirement | Egress proxy |  |
| 68 | requirement | Start with outbound traffic denied and allow only declared destinations. |  |
| 69 | requirement | Capture and hash everything the server tells the model or shows the user. |  |
| 70 | requirement | Run MCP scanners, authentication probes and abuse tests. |  |
| 71 | requirement | Use the tools, then capture again. |  |
| 72 | requirement | A local server for the first time, in a disposable environment. A remote server is called from there with a test account. |  |
| 73 | requirement | Surface hashes, observed behaviour and findings. |  |
| 74 | quote:tob-uninvoked | A server can influence the model before any of its tools is called. |  |
| 75 | quote:as-exec | Starting a server to scan it can run commands or send traffic. |  |
| 76 | inference quote:t-authz | A malicious server could show a scanner different text than it shows real users. |  |
| 77 | requirement | All findings |  |
| 78 | requirement | Tier |  |
| 79 | requirement | Sandbox observations |  |
| 80 | requirement | Confirm the tier. |  |
| 81 | requirement | Approve, approve with conditions, reject or defer. |  |
| 82 | requirement | Write the approval record. |  |
| 83 | requirement | Nothing. |  |
| 84 | requirement | A signed approval record. |  |
| 85 | requirement | Every blocking check in this stage passes, and the right approver for the tier has decided. |  |
| 86 | requirement | Approval record |  |
| 87 | requirement | Platform policy settings |  |
| 88 | requirement | Publish the artifact or URL to the approved source. |  |
| 89 | requirement | Add the allowlist entry and pinned configuration. |  |
| 90 | requirement | Prove that an unapproved server and, for a local server, an unapproved version are refused. |  |
| 91 | requirement | Roll out to a small group first. |  |
| 92 | requirement | For a local update, move the pin and allowlist entry in stages. Keep the previous version ready for rollback unless it is blocked. | OK (2026-11-26). Restates the existing intake procedure. |
| 93 | requirement | The approved server, for a first group of users. |  |
| 94 | requirement | Policy change, catalog entry and test evidence. |  |
| 95 | quote:l-allowlist | The MCP docs suggest starting with a short allowlist of vetted, pinned servers and clear entry criteria. |  |
| 96 | requirement | Advisory feeds |  |
| 97 | requirement | Logs and egress alerts |  |
| 98 | requirement | Client configuration inventory |  |
| 99 | requirement | Compare the live surface with the approved hashes. |  |
| 100 | requirement | Match advisories to the SBOM, or to the remote operator's notices. |  |
| 101 | requirement | Watch the publisher and the traffic. |  |
| 102 | requirement | Recertify before expiry, or retire. |  |
| 103 | requirement | The approved server, in daily use. |  |
| 104 | requirement | Triggers, or a new expiry date, or retirement. |  |
| 105 | requirement | No open trigger and the approval has not expired. |  |
| 106 | quote:l-rugpull | A server can change its tool descriptions after approval. |  |
| 107 | quote:l-reask | The protocol does not require clients to ask again when definitions change. |  |
| 108 | inference quote:t-listchanged | Change notices cannot be the only detector: sending them is recommended, not required, and depends on a declared capability. |  |
| 109 | requirement | Nine stages run in order. A failed gate stops the server there. Nothing from the server runs before Sandbox. |  |
| 110 | requirement | Release feed or dependency update tool for the package or image. |  |
| 111 | requirement | Keep running the approved, pinned version, unless it is blocked. |  |
| 112 | quote:co-staged | Testing and staged rollout belong in update handling. |  |
| 113 | requirement | A digest check at install fails, or the registry shows a new digest. |  |
| 114 | requirement | Block it and treat it as a possible attack until it is explained. |  |
| 115 | requirement | Hash comparison of the live surface. |  |
| 116 | requirement | Block anything new or changed until approved. Block the whole server if instructions changed. |  |
| 117 | quote:t-change | A tool list may change over time. |  |
| 118 | requirement | Configuration change, vendor notice or a failed connection. |  |
| 119 | requirement | Do not allow the new address until approved. |  |
| 120 | requirement | Advisory feed matched against the SBOM, or a vendor notice. |  |
| 121 | requirement | Decide on exposure at once. Limit or block if it is being exploited. A fix for an exploited vulnerability goes through the New version path without the waiting period. |  |
| 122 | quote:l-pinvuln | A pin keeps the vulnerable version in place until someone moves it. |  |
| 123 | quote:l-respond | For a vulnerable local server, the MCP docs advise blocking its egress, rotating the credentials passed to it and pushing a fixed version. |  |
| 124 | requirement | Malicious package report, vendor or community alert. |  |
| 125 | requirement | Revoke now. Block traffic, find every installation, rotate every credential it could read, and investigate what it did. |  |
| 126 | requirement | Repository transfer, new maintainer, new package account, acquisition. |  |
| 127 | requirement | Freeze a local server at the approved version. Block a remote server until it is screened again. Treat the next version as a new server. |  |
| 128 | requirement | Version difference, consent screen change, egress alert. |  |
| 129 | requirement | Do not grant the new access until approved. |  |
| 130 | quote:bp-semantic | A scope can change meaning without changing name. |  |
| 131 | requirement | Vendor notice or license difference between versions. |  |
| 132 | requirement | Keep using it only where the old terms still cover the use. Otherwise stop. |  |
| 133 | requirement | Repository or registry status, no response to reports. |  |
| 134 | requirement | Plan replacement and set an end date. |  |
| 135 | requirement | Date in the approval record. |  |
| 136 | requirement | Renew before the date. After it, the server is not approved. |  |
| 137 | requirement | Log, egress or canary alert, or a user report. |  |
| 138 | requirement | Block while you investigate. |  |
| 139 | requirement | New data, new users, new client, new configuration, or another server added next to it. |  |
| 140 | requirement | Keep the old use only. |  |
| 141 | requirement | Added, removed or renamed tool |  |
| 142 | requirement | Changed instructions, description, parameter or schema |  |
| 143 | requirement | Changed capability, prompt, resource, icon or UI |  |
| 144 | requirement | Changed read-only or destructive hint |  |
| 145 | requirement | Changed launch command or environment variable |  |
| 146 | requirement | New dependency |  |
| 147 | requirement | New or changed install script |  |
| 148 | requirement | New destination |  |
| 149 | requirement | New scope or permission |  |
| 150 | requirement | Changed publisher or owner |  |
| 151 | requirement | Changed license or terms |  |
| 152 | requirement | A change is any difference from the approval record. Never update a server automatically unless it meets every condition for automatic approval. |  |
| 153 | requirement | Allow it only when all of these are true. It skips the Review stage, so nobody reads the code difference. The approver for the server's tier approves the rule in advance and is the approver of record. Otherwise a person decides. |  |
| 154 | requirement | The server only reads, and only public or non-sensitive data. |  |
| 155 | requirement | A local server runs contained, with limited outbound traffic. |  |
| 156 | requirement | The publisher, license, launch command, environment variables and install scripts are unchanged, and there is no new dependency, destination or scope. |  |
| 157 | requirement | The captured surface is identical. |  |
| 158 | requirement | Every check in Screen, Pin, Scan and Sandbox passes, including the 7 day wait. An earlier result from a person counts only if what that person looked at is unchanged. |  |
| 159 | requirement | Reads only public or non-sensitive data. Remote. |  |
| 160 | requirement | Platform owner |  |
| 161 | requirement | 12 months |  |
| 162 | requirement | Reads internal or personal data. |  |
| 163 | requirement | Platform owner and security reviewer |  |
| 164 | requirement | 6 months |  |
| 165 | requirement | Changes data, sends data outward, or runs as a local process. |  |
| 166 | requirement | Security reviewer and data owner |  |
| 167 | requirement | Runs commands or code, spends money, or holds administrator or production access. |  |
| 168 | requirement | Security reviewer and system owner |  |
| 169 | requirement | 3 months |  |
| 170 | requirement | Released as recorded. |  |
| 171 | requirement | Released with limits that the platform or the owner enforces, such as fewer tools, fewer scopes, named users or a sandbox. |  |
| 172 | requirement | Added to the deny list when the reason is malicious or impersonation. |  |
| 173 | requirement | Nothing is released until the missing evidence arrives. |  |
| 174 | requirement | Use the highest tier that fits. Adjust the names and intervals to your organisation. |  |
| 175 | example | Keep one record for each approved server. Later changes are compared with it. For a remote server, origin holds the URL and the authorization server details instead. The example is fictional. |  |
| 176 | example | {<br>  "name": "example-tickets-mcp",<br>  "publisher": {"organisation": "Example Vendor", "verified_from": "vendor documentation URL"},<br>  "license": "<license or terms accepted>",<br>  "owner": "team-support",<br>  "origin": {<br>    "type": "package",<br>    "package": "@example/tickets-mcp",<br>    "version": "2.4.1",<br>    "digest": "sha512-<digest of the artifact>",<br>    "source_commit": "<commit>",<br>    "provenance": "verified"<br>  },<br>  "dependencies": {"lock_hash": "sha256-<hash>", "sbom": "<stored SBOM>"},<br>  "surface": {<br>    "captured_with_scopes": ["tickets:read", "tickets:comment"],<br>    "instructions": "sha256-<hash>",<br>    "tools": {"get_ticket": "sha256-<hash>", "add_comment": "sha256-<hash>"},<br>    "capabilities": {},<br>    "prompts": {},<br>    "resources": {},<br>    "resource_templates": {},<br>    "icons": {},<br>    "ui": {}<br>  },<br>  "runtime": {<br>    "command": ["<exact command and arguments>"],<br>    "credentials": "<secret store reference>",<br>    "files": ["<allowed folders>"],<br>    "destinations": ["tickets.example.com:443"],<br>    "environment": ["<variable names and values, without secrets>"]<br>  },<br>  "use": {"purpose": "<what it is used for>", "data": "<data it may reach>", "users": "<who may use it>", "clients": ["<approved clients>"]},<br>  "findings": "<link to triaged results>",<br>  "exceptions": ["<such as a skipped waiting period or a missing signature, and who accepted it>"],<br>  "tier": 3,<br>  "decision": "approved with conditions",<br>  "conditions": ["get_ticket and add_comment only"],<br>  "requested_by": "<person>",<br>  "approved_by": ["<security reviewer>", "<data owner>"],<br>  "decided": "2026-11-26",<br>  "expires": "2027-05-26"<br>} |  |
| 177 | requirement | Publisher is identified |  |
| 178 | requirement | Trace the server to a source repository and a real organisation or maintainer. For a remote server, trace the URL to its operator. |  |
| 179 | requirement | A named, reachable publisher, confirmed from more than the listing itself. |  |
| 180 | requirement | It is the package the vendor means |  |
| 181 | requirement | Take the name or URL from the vendor's own documentation and compare it letter by letter. |  |
| 182 | requirement | Name, publisher account and URL match the vendor's documentation. |  |
| 183 | requirement | Source can be read |  |
| 184 | requirement | Find the source that the published artifact is built from. |  |
| 185 | requirement | Source is available for the exact version. |  |
| 186 | requirement | Project is maintained |  |
| 187 | requirement | Look at recent commits, releases, open security issues and whether the project is archived. |  |
| 188 | requirement | Not archived, and security reports get answered. |  |
| 189 | requirement | There is a way to report vulnerabilities |  |
| 190 | requirement | Look for a security policy and past advisories. |  |
| 191 | requirement | A reporting route exists. |  |
| 192 | requirement | License allows the use |  |
| 193 | requirement | Read the license or the service terms. |  |
| 194 | requirement | Terms allow the intended use. |  |
| 195 | requirement | New versions have aged |  |
| 196 | requirement | Wait until a new version has been public for 7 days. Skip the wait for a fix to a vulnerability that is being exploited. |  |
| 197 | requirement | The version is old enough, or the exception is recorded. |  |
| 198 | requirement | Not reported as malicious |  |
| 199 | requirement | Look up the package and version in malicious package reports. Repeat for every dependency once the tree is known. |  |
| 200 | requirement | No report for the package or any dependency. |  |
| 201 | label | Requirement of this process. No source is quoted. |  |
| 202 | requirement | Remote operator gives assurance |  |
| 203 | requirement | Ask who runs the service, where data goes, how long it is kept, how incidents are announced and how changes are announced. |  |
| 204 | requirement | Written answers that fit the data involved. |  |
| 205 | requirement | Running it locally is justified |  |
| 206 | requirement | Use the remote version where one exists and the server needs no local access. Ask why a server with no need for local access is only offered as a local process. |  |
| 207 | requirement | A stated reason for local execution. |  |
| 208 | requirement | Exact version |  |
| 209 | requirement | Name one version. No ranges, no latest, no floating tag. |  |
| 210 | requirement | One immutable version in the request and the configuration. |  |
| 211 | requirement | Digest recorded |  |
| 212 | requirement | Record the artifact hash. Refer to a container image by digest. |  |
| 213 | requirement | Digest in the approval record. |  |
| 214 | requirement | Fetched without running it |  |
| 215 | requirement | Fetch into quarantine with install scripts off. For Python, accept built packages only. |  |
| 216 | requirement | No code from the package ran during the fetch. |  |
| 217 | requirement | Dependencies locked and listed |  |
| 218 | requirement | Lock the whole dependency tree with hashes and generate your own SBOM from the artifact. |  |
| 219 | requirement | Lock file with hashes and an SBOM are stored. |  |
| 220 | requirement | Signatures and provenance verified |  |
| 221 | requirement | Verify signatures and attestations against the expected publisher and source. An invalid signature or attestation blocks. If the publisher offers none, the approver decides and records it. |  |
| 222 | requirement | Verification succeeds for the expected identity, or the approver has accepted that none is offered. |  |
| 223 | requirement | Remote endpoint recorded |  |
| 224 | requirement | Record the exact URL and the authorization server details. Require HTTPS with a valid certificate throughout. |  |
| 225 | requirement | URL and metadata recorded, with no plain HTTP and no certificate error. |  |
| 226 | requirement | Known vulnerabilities |  |
| 227 | requirement | Scan the artifact and all dependencies. Rank by known exploitation, exploit probability and reachability. Ask a remote vendor for its results. |  |
| 228 | requirement | No known exploited vulnerability. Others have an owner and a deadline. |  |
| 229 | requirement | Malicious code signs |  |
| 230 | requirement | Run a malicious package scanner as well as the vulnerability scan. |  |
| 231 | requirement | Findings explained or the server rejected. |  |
| 232 | requirement | Static code analysis |  |
| 233 | requirement | Analyze the source for injection, path, request forgery and similar flaws. |  |
| 234 | requirement | No unresolved serious finding. |  |
| 235 | requirement | Secrets in code and images |  |
| 236 | requirement | Scan source, package and image layers for credentials. |  |
| 237 | requirement | No live secret. |  |
| 238 | requirement | Container and deployment settings |  |
| 239 | requirement | Scan the image build file and deployment files for risky settings such as root user, host mounts and broad privileges. |  |
| 240 | requirement | No unexplained risky setting. |  |
| 241 | requirement | Install and build scripts read |  |
| 242 | requirement | List every script that runs at install, build or start, and read it. |  |
| 243 | requirement | Each script is understood and needed. |  |
| 244 | requirement | Binaries and hidden code |  |
| 245 | requirement | Look for bundled binaries, downloads at run time, obfuscated code and files that do not match the source. |  |
| 246 | requirement | Everything executable traces to the source or a verified origin. |  |
| 247 | requirement | Dependency confusion |  |
| 248 | requirement | Resolve internal package names only from the internal registry, and fetch public ones through a mirror. |  |
| 249 | requirement | No internal name can resolve from a public registry. |  |
| 250 | requirement | No command or code injection |  |
| 251 | requirement | Check that model or user input never reaches a shell or code evaluator. |  |
| 252 | requirement | No path from input to shell, eval or string-built command. |  |
| 253 | requirement | File access stays inside bounds |  |
| 254 | requirement | Check path handling, including symlinks and prefix comparisons. |  |
| 255 | requirement | Resolved paths cannot leave the allowed folders. |  |
| 256 | requirement | No open URL fetching |  |
| 257 | requirement | Check every place the server fetches a URL that came from the model or a user. |  |
| 258 | requirement | Destinations are allowlisted, and private and metadata addresses are refused. |  |
| 259 | requirement | Tokens are checked for audience |  |
| 260 | requirement | Check that the server rejects tokens issued for something else. |  |
| 261 | requirement | A token for another service is refused. |  |
| 262 | requirement | No token passthrough |  |
| 263 | requirement | Check that the server never forwards the caller's token to another service. |  |
| 264 | requirement | Downstream calls use their own credentials. |  |
| 265 | requirement | Proxy servers ask consent per client |  |
| 266 | requirement | If the server signs in to a third party on behalf of many clients, check consent handling. |  |
| 267 | requirement | Consent is stored and checked for each client. |  |
| 268 | requirement | Sign-in links are handled safely |  |
| 269 | requirement | For a bridge or bundled client, check how it treats URLs received from a server. |  |
| 270 | requirement | Only safe schemes are opened, never through a shell, and private and reserved addresses are not fetched. |  |
| 271 | requirement | Least privilege |  |
| 272 | requirement | Compare requested scopes, file access and permissions with the stated purpose. Give a server meant only to read a read-only account at the data source. |  |
| 273 | requirement | No wildcard scope, nothing without a reason, and any read-only limit is enforced by the data source. |  |
| 274 | requirement | HTTP endpoint is not open |  |
| 275 | requirement | For any server that listens over HTTP, check Origin and Host header validation, listening address and authentication. |  |
| 276 | requirement | Origin and Host are checked, local servers listen on localhost only, and callers authenticate. |  |
| 277 | requirement | Callers cannot claim an identity |  |
| 278 | requirement | Check that identity comes from a verified token, not from a state handle or anything the client typed. |  |
| 279 | requirement | Knowing a handle or naming a user gives no access. |  |
| 280 | requirement | No secrets asked in forms |  |
| 281 | requirement | Check what the server asks the user for during use. |  |
| 282 | requirement | Passwords, keys, tokens and payment data are never requested in form mode. |  |
| 283 | requirement | Basic tool protections |  |
| 284 | requirement | Check input validation, access control, rate limits and output cleaning. |  |
| 285 | requirement | All four are present. |  |
| 286 | requirement | Usable logs without secrets |  |
| 287 | requirement | Check that tool calls can be logged and that secrets are masked. |  |
| 288 | requirement | Calls are logged in a structured form without secrets. |  |
| 289 | requirement | No stored secrets |  |
| 290 | requirement | Check code, defaults and sample configuration for built-in credentials, and check how the server stores the tokens it holds. |  |
| 291 | requirement | Credentials come from a secret store, one narrow credential per server, and held tokens are not in plain text. |  |
| 292 | requirement | Code does only what is declared |  |
| 293 | requirement | Read the code, or the difference from the approved version, for data sent anywhere, hidden recipients, extra file or credential access, and behaviour that depends on time or environment. |  |
| 294 | requirement | Every outbound send and sensitive access serves a declared purpose. |  |
| 295 | requirement | Launch command is clean |  |
| 296 | requirement | Read the exact command, arguments and environment variables that start the server. |  |
| 297 | requirement | No chained commands, no sudo, and no unexplained network or file operation. |  |
| 298 | requirement | Sign-in service meets the OAuth rules |  |
| 299 | requirement | For a server that uses OAuth, check the authorization server metadata and redirect handling. |  |
| 300 | requirement | PKCE support is advertised, redirect URIs must match exactly, sign-in responses name the issuer, and access tokens are short-lived. |  |
| 301 | requirement | Links sent to users are safe |  |
| 302 | requirement | If the server sends users to a web page during use, check the URL and who the page accepts input from. |  |
| 303 | requirement | HTTPS, no personal data or pre-authenticated access in the URL, and the server confirms that the person opening it is the person who asked. |  |
| 304 | requirement | Model requests by the server are justified |  |
| 305 | requirement | Check whether the server asks the client to run a model. This is called sampling, and the specification has deprecated it. |  |
| 306 | requirement | It does not, or the reason is recorded and the client lets a person deny each request. |  |
| 307 | inference | For a remote server, isolation protects your side only. The server's side stays out of reach. |  |
| 308 | requirement | Isolated and disposable |  |
| 309 | requirement | Run in a throwaway environment with no production credentials or data and outbound traffic denied by default. |  |
| 310 | requirement | Nothing of value is reachable from the test. |  |
| 311 | requirement | Whole surface captured and hashed |  |
| 312 | requirement | Capture declared capabilities, server instructions, tools with full schemas and annotations, prompts, resources, resource templates, UI content and icons, using a test account with the same scopes as production. |  |
| 313 | requirement | A hash for every item is in the record. |  |
| 314 | requirement | No instructions aimed at the model |  |
| 315 | requirement | Read every text field, including parameter names, schema descriptions and comments. |  |
| 316 | requirement | Nothing tells the model to do what the tool's purpose does not need. |  |
| 317 | requirement | No hidden characters |  |
| 318 | requirement | Search the captured text for zero-width and direction-control characters. |  |
| 319 | requirement | None present, or each one explained. |  |
| 320 | requirement | MCP scanner |  |
| 321 | requirement | Run at least one MCP scanner inside the sandbox. Check first what it sends outside your network. |  |
| 322 | requirement | Findings triaged. A clean result counts as one input, not as approval. |  |
| 323 | requirement | No shadowing or name clashes |  |
| 324 | requirement | Compare names and descriptions with the other approved servers. Check that names use only the characters the specification lists. |  |
| 325 | requirement | No duplicate or look-alike tool name, no unusual character, and no text about another server's tools. |  |
| 326 | requirement | No dangerous combination |  |
| 327 | requirement | Check whether this server, with the others in use, joins untrusted content, private data and a way to send data out. |  |
| 328 | requirement | The combination is absent, or limited by a condition in the approval. |  |
| 329 | requirement | Annotations match behaviour |  |
| 330 | requirement | Compare read-only and destructive hints with what the tool does. |  |
| 331 | requirement | No hint understates the effect. |  |
| 332 | requirement | Network, file and process activity as declared |  |
| 333 | requirement | Watch traffic, files and processes. Place canary files and credentials. |  |
| 334 | requirement | No undeclared destination or access, and no canary used. |  |
| 335 | inference quote:pm-fake | This comparison would show an added hidden recipient, as in the reported Postmark look-alike case. |  |
| 336 | requirement | Outbound content matches the request |  |
| 337 | requirement | For tools that send or write, compare what arrived with what the call asked for: recipients, fields, attachments. |  |
| 338 | requirement | Nothing added, removed or redirected. |  |
| 339 | requirement | Get the permission described under D12 first. |  |
| 340 | requirement | Authentication probes |  |
| 341 | requirement | For a server that listens over HTTP, call without a token, with a token for another service and with a foreign Origin. |  |
| 342 | requirement | Every such call is refused. |  |
| 343 | requirement | Get the operator's written permission before running this check or D11 against a server you do not run. Without it, do not run them; the operator's own test results are then the evidence. |  |
| 344 | requirement | Abuse tests |  |
| 345 | requirement | Send path traversal, injection, internal address, oversized and malformed inputs. |  |
| 346 | requirement | No test succeeds and the server stays up. |  |
| 347 | requirement | Second capture is the same |  |
| 348 | requirement | Use the tools, wait, reconnect and capture again. |  |
| 349 | requirement | Hashes match, or each change has an accepted reason. |  |
| 350 | requirement | Schemas, icons and headers are safe |  |
| 351 | requirement | Look for references to network addresses in schemas, unsafe icon addresses, and sensitive parameters copied into HTTP headers. |  |
| 352 | requirement | No network reference, only safe icon schemes, and no password, key, token or personal data marked x-mcp-header. |  |
| 353 | requirement | Interactive UI reviewed |  |
| 354 | requirement | If the server ships UI, review its code and the domains it declares, and hash it. |  |
| 355 | requirement | Declared domains are needed and narrow, and the UI hash is recorded. |  |
| 356 | requirement | Risk tier assigned |  |
| 357 | requirement | Set the tier from what the server can do. |  |
| 358 | requirement | Tier and reason recorded. |  |
| 359 | requirement | Every finding has an outcome |  |
| 360 | requirement | Fix, accept with an owner and end date, or reject. Known malicious code gets no exception. |  |
| 361 | requirement | No finding without an outcome. |  |
| 362 | requirement | Approver is not the requester |  |
| 363 | requirement | Have a different person approve. For an automatic approval, that person is whoever approved the rule. |  |
| 364 | requirement | No approver is the requester. |  |
| 365 | requirement | Conditions and expiry set |  |
| 366 | requirement | Write the limits of the approval and the date it ends. |  |
| 367 | requirement | An expiry date is on the record. |  |
| 368 | requirement | Record complete |  |
| 369 | requirement | Fill in every field of the approval record that applies and register the server. |  |
| 370 | requirement | The record and the catalog entry exist. |  |
| 371 | requirement | Served from the approved source |  |
| 372 | requirement | Install from the internal registry or the recorded URL, and block direct public downloads where you can. |  |
| 373 | requirement | Clients get only what was approved. |  |
| 374 | requirement | Allowlist matches URL or command |  |
| 375 | requirement | Allow by remote URL or exact command. Do not rely on a server name. |  |
| 376 | requirement | A renamed unapproved server is refused. |  |
| 377 | requirement | Configuration is pinned |  |
| 378 | requirement | For a local server, put the version or digest in the managed configuration. Take credentials from a secret store, and pass each server only its own. |  |
| 379 | requirement | No floating version, no secret in a configuration file and no credential the server does not need. |  |
| 380 | requirement | Contained at run time |  |
| 381 | requirement | Run local servers in a container or sandbox with only the needed folder, read-only where possible, and limit outbound traffic per server. |  |
| 382 | requirement | Access and destinations match the approval. |  |
| 383 | requirement | Block is proven |  |
| 384 | requirement | Try to start an unapproved server, and for a local server an unapproved version, in each client. |  |
| 385 | requirement | Each attempt is refused, with evidence stored. |  |
| 386 | requirement | Definition changes are stopped |  |
| 387 | requirement | Use a client that asks again, or a gateway that blocks, when definitions differ from the approved hashes. |  |
| 388 | requirement | A changed definition cannot be used silently. |  |
| 389 | requirement | Spending is capped |  |
| 390 | requirement | If a tool can spend money, set limits outside the model. |  |
| 391 | requirement | The paying component enforces a limit per payment and a total per time period. |  |
| 392 | requirement | Definition drift |  |
| 393 | requirement | Capture the live surface on a schedule and on each reconnect where possible, and compare hashes. |  |
| 394 | requirement | Hashes equal the approved ones. |  |
| 395 | requirement | New advisories |  |
| 396 | requirement | Daily, match new vulnerability and malicious package reports against each stored SBOM. For a remote server, check the operator's security notices. |  |
| 397 | requirement | No unhandled match or notice. |  |
| 398 | requirement | Upstream changes |  |
| 399 | requirement | Follow releases, ownership, maintainers, deprecation and takedown of each approved server. |  |
| 400 | requirement | No unreviewed change. |  |
| 401 | requirement | Traffic and logs |  |
| 402 | requirement | Alert on new destinations, unusual volume and unexpected tool calls. |  |
| 403 | requirement | Alerts have an owner and are handled. |  |
| 404 | requirement | Recertification |  |
| 405 | requirement | Re-assess before the expiry date. When a server is retired, remove its allowlist entry and rotate what it held. |  |
| 406 | requirement | Renewed or retired on time. |  |
| 407 | requirement | Switch-off and rollback tested |  |
| 408 | requirement | Keep a way to block the server everywhere and rotate its credentials, and for a local server to return to the previous version. Rehearse it. |  |
| 409 | requirement | A rehearsal has worked within the target time. |  |
| 410 | requirement | Unapproved servers found |  |
| 411 | requirement | Collect client configurations and compare them with the catalog. |  |
| 412 | requirement | Every configured server is approved. |  |
| 413 | quote:osv-use | OSV-Scanner |  |
| 414 | quote:gd-use,om-reports | GuardDog, OpenSSF reports |  |
| 415 | quote:ql-use | CodeQL |  |
| 416 | quote:gl-use,tv-secrets | Gitleaks, Trivy |  |
| 417 | quote:tv-iac | Trivy |  |
| 418 | quote:ci-engines,as-sends | Cisco MCP Scanner, Snyk Agent Scan |  |
| 419 | requirement | The server or version being assessed cannot move on until this is fixed. If the failing one is already in use, it is suspended, unless a change trigger says what to do instead. |  |
| 420 | requirement | The approver decides and records why. |  |
| 421 | requirement | Pick at least one tool for each job. Other tools can do the same jobs. |  |
| 422 | example | Owner, URL, two tools and read and comment scopes recorded. |  |
| 423 | example | The URL is in the vendor's documentation. Data handling answers arrive in writing. Tier 3, because it writes. |  |
| 424 | example | URL and authorization metadata recorded. |  |
| 425 | example | No code to scan. The vendor shares its scan results, which show no known exploited vulnerability. |  |
| 426 | example | The vendor gives evidence on the checks marked remote, among them token audience, passthrough and logging. |  |
| 427 | example | Surface captured with the two scopes. Permitted probes are refused. Second capture matches. |  |
| 428 | example | Approved for the two tools, for six months, with no other scopes. |  |
| 429 | example | URL allowlisted. A second URL is refused in each client. |  |
| 430 | example | Daily surface comparison starts. |  |
| 431 | example | Fictional example: a team asks for a ticket vendor's own remote server, to read and comment on tickets. |  |
| 432 | example | A developer asks for the package by the name found in a search. |  |
| 433 | example | The vendor's documentation does not name this package, and the publisher account is not the vendor's. Rejected before any download. The package name goes on the deny list. |  |
| 434 | example | Based on a reported case: a package on npm used an email vendor's name without being the vendor's. |  |
| 435 | quote:pm-fake | The vendor reported that the fake package built trust over 15 versions before adding a backdoor. |  |
| 436 | example | New version seen. It waits out the 7 days while the old pin keeps running. |  |
| 437 | example | New digest recorded. Dependencies unchanged. |  |
| 438 | example | No known vulnerability or report. Known-problem scans can be silent on new malicious code. |  |
| 439 | example | The changed send function builds its recipient list in an indirect way. The reviewer does not see the added copy. |  |
| 440 | example | A test message arrives with a recipient nobody asked for. The version is rejected and reported. The server is now handled as reported malicious: the old approval is revoked too and its credentials are rotated. |  |
| 441 | example | Fictional example using the same technique: an approved mail server publishes a new version that copies every message to an outside address. |  |
| 442 | example | Request recorded. |  |
| 443 | example | Publisher and source are in order. |  |
| 444 | example | Version and digest recorded. |  |
| 445 | example | Traditional scans find nothing. The problem is text, not a vulnerable library. |  |
| 446 | example | No code flaw found. |  |
| 447 | example | Reading every captured field shows the instruction. Rejected. |  |
| 448 | example | Fictional example: a note taking server whose parameter description tells the model to read a key file and pass it along. |  |
| 449 | quote:inv-poison | Instructions hidden in tool descriptions can be invisible to users and visible to models. |  |
| 450 | example | The hash comparison reports a new tool whose description says it sends data to an outside storage service. The gateway or client blocks it. |  |
| 451 | example | A new destination also counts as more permissions. The vendor states in writing what goes to the storage service and how long it is kept. |  |
| 452 | example | No code to read. The new tool and its destination are compared with the stated purpose. |  |
| 453 | example | The new tool is captured and tested with the other approved servers in mind. |  |
| 454 | example | A new destination means a person decides. Approved only for non-sensitive projects. |  |
| 455 | example | New hashes and condition published. |  |
| 456 | example | Fictional example: an approved remote server starts listing a new export tool. No version number changes. |  |
| 457 | example | The advisory matches a stored SBOM. Configuration inventory shows who runs it. |  |
| 458 | example | The approved version is affected, and in this example the flaw is being exploited. It is blocked, and exposed credentials are rotated. |  |
| 459 | example | The fixed version is not reported as malicious. The 7 day wait is skipped and recorded. |  |
| 460 | example | The fixed version is fetched without running it, pinned and verified. |  |
| 461 | example | The fixed version no longer matches the advisory, and the malware scan is clean. |  |
| 462 | example | The code difference holds the fix and nothing undeclared. |  |
| 463 | example | Surface and behaviour compared with the old approval. |  |
| 464 | example | The fixed version is approved. |  |
| 465 | example | Pin and allowlist moved. The old version is refused. |  |
| 466 | example | Based on a published vulnerability in mcp-remote, a bridge that connects local clients to remote servers. |  |
| 467 | quote:cv-6514 | The flaw let an untrusted server run operating system commands on the client machine. |  |
| 468 | label | Look-alike or impersonating server |  |
| 469 | inference | A publisher that is real but dishonest passes identity checks. |  |
| 470 | label | Malicious package |  |
| 471 | inference quote:l-noproof | New malicious code with no report yet can pass scans and stay quiet in a test. |  |
| 472 | label | Publisher account or ownership takeover |  |
| 473 | inference quote:npm-prov | A release made with the real publisher's own build system can carry valid provenance. |  |
| 474 | label | Known vulnerability |  |
| 475 | inference | Flaws that nobody has published are not matched. |  |
| 476 | label | Compromised dependency |  |
| 477 | inference | A locked but already compromised dependency stays locked in. |  |
| 478 | label | Dependency confusion |  |
| 479 | inference | Names that no registry rule covers can still resolve publicly. |  |
| 480 | label | Install or build script abuse |  |
| 481 | inference | A script that is needed for install still has to run later. |  |
| 482 | label | Floating version or moving tag |  |
| 483 | inference | A remote server cannot be pinned by digest. |  |
| 484 | label | Tool poisoning in any schema field |  |
| 485 | inference | Wording that looks innocent to a reviewer and a scanner can still steer a model. |  |
| 486 | label | Hidden characters |  |
| 487 | inference | Meaning can be hidden without any special character. |  |
| 488 | label | Shadowing another server's tools |  |
| 489 | inference quote:l-shared | All configured servers share one model context, so each server added later changes what the others are exposed to. |  |
| 490 | label | Definitions changed after approval (rug pull) |  |
| 491 | inference | Between two comparisons a change can be used unnoticed. |  |
| 492 | label | Behaviour changed behind unchanged definitions |  |
| 493 | quote:c-hashlimit | Hashing definitions does not see it. |  |
| 494 | label | Prompt injection through results and resources |  |
| 495 | quote:c-response | Every tool response has to be treated as untrusted data, also from approved servers. |  |
| 496 | label | Data leaving through a chain of tools |  |
| 497 | inference | A permitted destination can be used to take data out. |  |
| 498 | label | Server asks the client to run a model |  |
| 499 | inference | How each request is shown and limited is up to the client. |  |
| 500 | label | Malicious startup command |  |
| 501 | inference | A command that looks ordinary can still fetch hostile code. |  |
| 502 | label | Command or code injection |  |
| 503 | inference | Analysis and tests miss some paths. |  |
| 504 | label | Path traversal and symlink escape |  |
| 505 | inference | Anything inside the mounted folder stays reachable. |  |
| 506 | label | Server-side request forgery |  |
| 507 | inference | Redirects and name resolution tricks need their own tests. |  |
| 508 | label | Command execution from a sign-in link |  |
| 509 | inference | The same flaw in a client is outside this process. |  |
| 510 | label | Undeclared network, file or process activity |  |
| 511 | inference | Behaviour triggered by time, data or environment may not show in a test. |  |
| 512 | label | Resource exhaustion |  |
| 513 | inference | Load limits of a remote service are the vendor's to hold. |  |
| 514 | label | Missing authentication or open local endpoint |  |
| 515 | quote:l-reachable | A local server that listens on a port can be reached by other local processes and by websites. |  |
| 516 | label | DNS rebinding |  |
| 517 | inference | Later code changes can remove the check. |  |
| 518 | label | Token passthrough and wrong audience |  |
| 519 | inference | For a remote server you rely on the vendor for what happens downstream. |  |
| 520 | label | Confused deputy |  |
| 521 | inference | Hard to prove from outside for a remote server. |  |
| 522 | label | Excess or creeping scopes |  |
| 523 | inference quote:bp-semantic | A scope can widen on the service side without any change in the server. |  |
| 524 | label | Identity spoofing and state handle misuse |  |
| 525 | inference | Hard to test fully from outside. |  |
| 526 | label | Weak sign-in service (code theft, redirect, mix-up) |  |
| 527 | inference | Client side defences against these attacks belong to the client. |  |
| 528 | label | Secret exposure |  |
| 529 | quote:l-reach | A credential the server needs is readable by the server. |  |
| 530 | label | Phishing for secrets through user prompts |  |
| 531 | inference | Ordinary looking questions can still collect sensitive data. |  |
| 532 | label | Hostile or leaking server UI |  |
| 533 | inference | UI loaded later from an allowed domain can change. |  |
| 534 | label | Escape from the local environment |  |
| 535 | quote:co-container | A container should not be relied on as a strong security boundary. |  |
| 536 | label | Too little logging |  |
| 537 | inference | A remote server's internal actions are not in your logs. |  |
| 538 | label | Shadow servers |  |
| 539 | inference | Unmanaged devices and clients that ignore policy are not seen. |  |
| 540 | label | Context shared too widely |  |
| 541 | inference | How a client keeps and shares context is decided by the client, not at intake. |  |
| 542 | label | Uncontrolled spending |  |
| 543 | inference | Unwanted payments can still be made inside the limits. |  |
| 544 | inference | Matching a check to an attack is a design choice. It is not a measured detection rate, and the list of attacks is not complete. |  |
| 545 | label | Server name, URL or command. |  |
| 546 | quote:gh-match | Entries match by name, URL or command. |  |
| 547 | quote:gh-profiles | The lists do not apply to servers defined in repository custom agent profiles. |  |
| 548 | quote:gh-firewall | An organization or repository firewall that blocks the domains needed to start those servers can prevent their use. |  |
| 549 | quote:gh-malformed | A malformed list blocks all but the built-in servers. |  |
| 550 | label | Server name or ID. |  |
| 551 | preview quote:gh-preview | It is in public preview and not the recommended way to restrict servers. |  |
| 552 | quote:gh-ga | The recommended way is the managed settings file. |  |
| 553 | quote:gh-name | Name matching can be bypassed by editing configuration. |  |
| 554 | label | Server URL, exact command or name. |  |
| 555 | quote:cc-authoritative | An allowlist is authoritative only when it is also set to managed entries only. |  |
| 556 | quote:cc-exact | A command entry matches the exact command. |  |
| 557 | quote:cc-env | A command entry matches whatever the server's environment variables are. |  |
| 558 | quote:cc-envload | Some environment variables change what node loads at startup. |  |
| 559 | quote:cc-name | A name entry is not a security control. |  |
| 560 | label | Managed Copilot settings, workspace trust and a per-server sandbox. |  |
| 561 | quote:vs-allow | Managed settings can limit which servers developers install and run. |  |
| 562 | quote:vs-disabled,vs-harness | Managed settings keep the Claude and Codex harnesses disabled unless they are permitted. Permitted sessions run without Copilot's managed permission, sandbox, MCP and plugin controls. |  |
| 563 | quote:vs-workspace,vs-restart | In a trusted workspace, servers configured in the workspace can start without a separate trust prompt, also after a configuration change. |  |
| 564 | quote:vs-sandbox,vs-windows | The per-server sandbox covers local process servers on macOS and Linux, not on Windows. |  |
| 565 | quote:vs-separate,vs-outbound | The separate Copilot sandbox allows outbound traffic by default. |  |
| 566 | label | A public list of servers. |  |
| 567 | preview quote:reg-preview | It is in preview. |  |
| 568 | quote:reg-moderation | Expect little or no moderation. |  |
| 569 | quote:reg-vulns | Having a security vulnerability does not by itself get a server removed. |  |
| 570 | label | Destinations per server. |  |
| 571 | quote:l-egress | A per-server egress list with alerts limits where a server can send data. |  |
| 572 | label | Client configuration files on devices. |  |
| 573 | quote:l-inventory | Management tools can collect client configurations to find what is in use. |  |
| 574 | requirement | A weak client can undo a well reviewed server. Assess clients separately. |  |
| 575 | requirement | A proxy or other component that handles decrypted messages could change or replay them. Assess it with the platform. |  |
| 576 | requirement | Per-call approval prompts, output filtering and permission controls during use belong to the platform and agent design. |  |
| 577 | requirement | Its code, build and staff are visible only through the vendor's evidence. |  |
| 578 | requirement | License and data answers are collected here. Contracts and privacy review follow your normal process. |  |
| 579 | inference quote:gh-match,cc-exact,cc-env | None of the allowlist settings above compares a server's code or tool definitions with what was reviewed. This process has to do that. |  |
<!-- /ledger -->
