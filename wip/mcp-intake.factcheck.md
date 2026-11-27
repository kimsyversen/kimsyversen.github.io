# MCP server intake: fact check

## Interactive diagram, 2026-11-26

Reviewed the 31 new diagram statements as intake instructions. Matched all 181 quotations against the saved source copies. The 570 outstanding verdicts in the detailed guide predate this change.

Chrome checks passed at 1280, 390 and 320 pixels. All 18 diagram disclosures opened and closed, keyboard activation worked, and links opened the relevant reference sections. No horizontal page overflow or browser console errors were observed.

## Simplified guide, 2026-11-26

- Verified all 181 quotes against their sources. The nine revised statements describe the existing intake procedure. The 570 retained statements with blank verdicts still need review.
- Verified all 185 existing fragment IDs, links within the site and generated page output.
- Tested the overview, native disclosures and representative shared links in Chrome at 1280, 390 and 320 pixels. Keyboard activation and disclosures without JavaScript worked. No horizontal page overflow or console errors.

<!-- ledger -->
| # | Basis | Statement | Verdict |
|---|---|---|---|
| 1 | requirement | Owner, purpose, data and access | OK: intake instruction |
| 2 | requirement | Name the person responsible. List the task, the data it needs and any changes the server should be allowed to make. | OK: intake instruction |
| 3 | requirement | Reuse a server if it meets the need. | OK: intake instruction |
| 4 | requirement | Compare the request with the existing approval. If the task needs broader access, send that change for review before granting it. | OK: intake instruction |
| 5 | requirement | Match the package or URL to vendor documentation. | OK: intake instruction |
| 6 | requirement | Start at the publisher's own site. Follow its link to the package, image or endpoint and check the exact name and owner. | OK: intake instruction |
| 7 | requirement | Complete the desk checks before fetching a new artifact or contacting a candidate endpoint. | OK: intake instruction |
| 8 | requirement | Pin local artifacts. Record the remote URL. | OK: intake instruction |
| 9 | requirement | For a package or image, record the version, digest and locked dependencies. For a hosted service, verify the endpoint and obtain evidence from its operator. | OK: intake instruction |
| 10 | requirement | Check for malware, vulnerabilities and excessive access. | OK: intake instruction |
| 11 | requirement | Scan local files without installing or starting the server. For a remote service, review the operator's scan evidence. Compare tool descriptions, instructions and requested permissions with the stated task. | OK: intake instruction |
| 12 | requirement | Use test data and disposable credentials. | OK: intake instruction |
| 13 | requirement | Make the first connection or launch in isolation. Capture the tools and other metadata the client sees. Check observed file and network access against the request. | OK: intake instruction |
| 14 | requirement | Keep the candidate out of production until every blocking check passes. Record how each finding was resolved. | OK: intake instruction |
| 15 | requirement | Use the approver for the risk tier. | OK: intake instruction |
| 16 | requirement | Assign the tier from the server's highest-risk capability. Give the designated approver the findings and proposed limits before rollout. | OK: intake instruction |
| 17 | requirement | Save the configuration, access limits and expiry. | OK: intake instruction |
| 18 | requirement | Record the reviewed artifact or endpoint, tool definitions, permissions, owner, approver and review date. Keep this baseline for later comparisons. | OK: intake instruction |
| 19 | requirement | Enforce the approved configuration. | OK: intake instruction |
| 20 | requirement | Start with a limited pilot. Confirm the client applies the approved access limits and that the team can disable or roll back the server before widening access. | OK: intake instruction |
| 21 | requirement | Release only the configuration covered by the decision. Keep a held or rejected candidate out of use. | OK: intake instruction |
| 22 | requirement | Check tool definitions and permissions. | OK: intake instruction |
| 23 | requirement | Compare the live tool list, descriptions and access with the saved baseline. Hold newly exposed capabilities until the affected checks pass. | OK: intake instruction |
| 24 | requirement | Check dependencies and vendor notices. | OK: intake instruction |
| 25 | requirement | Match alerts to the deployed version and its dependencies. For a hosted service, ask the operator whether the deployed service is affected. | OK: intake instruction |
| 26 | requirement | Suspend access and investigate. | OK: intake instruction |
| 27 | requirement | Disable access, preserve relevant logs and identify affected installations. Revoke exposed credentials and investigate before restoring service. | OK: intake instruction |
| 28 | requirement | Have the owner confirm the need and the approver renew the record. Remove access when approval ends. | OK: intake instruction |
| 29 | requirement | Resolve blockers or record why you declined. | OK: intake instruction |
| 30 | requirement | For a hold, assign each blocker to an owner and repeat the failed checks. For a rejection, record the decision and stop the rollout. | OK: intake instruction |
| 31 | requirement | Use the change type to decide which checks to repeat and whether the current deployment can stay in use during review. | OK: intake instruction |
| 32 | requirement | Purpose and named owner |  |
| 33 | requirement | Link to the vendor's own documentation |  |
| 34 | requirement | Exact version, image digest or URL |  |
| 35 | requirement | Transport: local process or HTTP |  |
| 36 | requirement | Data it will reach |  |
| 37 | requirement | Tools wanted |  |
| 38 | requirement | Credentials and scopes |  |
| 39 | requirement | Look in the approved catalog first. If an approved server covers the need, use it. |  |
| 40 | requirement | Install nothing. |  |
| 41 | requirement | Nothing from the server. |  |
| 42 | requirement | A request record. |  |
| 43 | requirement | Every input is filled in and an owner has accepted the role. |  |
| 44 | quote:l-run | A local server is downloaded code that runs under your user account. |  |
| 45 | quote:t-authz | Which tools a server lists can depend on the access it is given, so the requested scopes belong in the request. |  |
| 46 | requirement | Request record |  |
| 47 | requirement | Publisher, repository and registry pages |  |
| 48 | requirement | Malicious package reports |  |
| 49 | requirement | Run the hygiene checks. |  |
| 50 | requirement | Give the server a provisional risk tier. |  |
| 51 | requirement | Stop at the first check marked Block that fails. |  |
| 52 | requirement | Nothing from the server. This is desk work. |  |
| 53 | requirement | Go or stop, with a provisional tier. |  |
| 54 | requirement | No blocking hygiene check has failed. |  |
| 55 | quote:l-listing | A listing on a registry is not an endorsement. |  |
| 56 | quote:vs-trust | Trusting a publisher does not show that every tool result is safe. |  |
| 57 | quote:l-popular | Popularity or a good name does not show that a package is safe or current. |  |
| 58 | requirement | Exact version, image or URL |  |
| 59 | requirement | Local or container: fetch into quarantine or an internal mirror, record digests, lock the dependency tree and build an SBOM. |  |
| 60 | requirement | Remote: record the URL, the certificate-protected connection and the authorization metadata. |  |
| 61 | requirement | Verify signatures and provenance. |  |
| 62 | requirement | On a change, compare the new local dependency tree and install scripts with the approved ones. For a remote server, record the endpoint details again. | OK (2026-11-26). Restates the existing intake procedure. |
| 63 | requirement | Only the fetch tool, in a quarantine area. No install scripts. |  |
| 64 | requirement | Digests, lock file, SBOM and provenance result, or the remote endpoint details. |  |
| 65 | requirement | Every blocking check in this stage passes. |  |
| 66 | quote:l-toponly | Pinning a package version with a launcher such as npx or uvx fixes only the top package. Its dependencies are usually resolved again at install. |  |
| 67 | quote:slsa-l1 | Provenance at the first SLSA build level is easy to bypass or forge. |  |
| 68 | inference quote:d-selfreport | A server's own name and version are self-reported. Identify it by digest or URL. |  |
| 69 | requirement | Quarantined copy |  |
| 70 | requirement | SBOM |  |
| 71 | requirement | Run the vulnerability, malware, code, secret and configuration scans. |  |
| 72 | requirement | Scan the locked dependency list and the SBOM. Do not let a scanner install the package. |  |
| 73 | requirement | Triage every finding: exploited, reachable, fix available. |  |
| 74 | requirement | For a new version, run all scans again or get fresh results from the remote vendor. Report what differs from the approved version. | OK (2026-11-26). Restates the existing intake procedure. |
| 75 | requirement | Scanners, in an isolated job without secrets. |  |
| 76 | requirement | Findings with a disposition each. |  |
| 77 | quote:pa-static | pip-audit is not a static code analyzer. |  |
| 78 | quote:pa-exec,pa-equiv | pip-audit -r can run code from what it audits, so isolate the scan job. |  |
| 79 | quote:pa-nopip | Given a hashed requirements file, pip-audit can skip pip's dependency resolution with --disable-pip. |  |
| 80 | requirement | Source code |  |
| 81 | requirement | Configuration and launch command |  |
| 82 | requirement | Scan findings |  |
| 83 | requirement | Go through the MCP review checks. |  |
| 84 | requirement | Remote: there is no code to read. Ask the vendor for evidence on each check marked remote, and test what you can in Sandbox. |  |
| 85 | requirement | Scale the depth to the tier. |  |
| 86 | requirement | On a change, read the code diff or the remote vendor's new evidence. Check for changes to tools, dependencies, destinations, scopes and install scripts. | OK (2026-11-26). Restates the existing intake procedure. |
| 87 | requirement | Nothing from the server. People and tools read code and settings. |  |
| 88 | requirement | Review findings. |  |
| 89 | requirement | Every blocking check in this stage passes. For a remote server, the vendor's evidence can show that it passes. |  |
| 90 | quote:l-noproof | A scanner finding nothing does not show how the server will behave. |  |
| 91 | requirement | Pinned copy or URL |  |
| 92 | requirement | Fake data and canary credentials |  |
| 93 | requirement | Egress proxy |  |
| 94 | requirement | Start with outbound traffic denied and allow only declared destinations. |  |
| 95 | requirement | Capture and hash everything the server tells the model or shows the user. |  |
| 96 | requirement | Run MCP scanners, authentication probes and abuse tests. |  |
| 97 | requirement | Use the tools, then capture again. |  |
| 98 | requirement | A local server for the first time, in a disposable environment. A remote server is called from there with a test account. |  |
| 99 | requirement | Surface hashes, observed behaviour and findings. |  |
| 100 | quote:tob-uninvoked | A server can influence the model before any of its tools is called. |  |
| 101 | quote:as-exec | Starting a server to scan it can run commands or send traffic. |  |
| 102 | inference quote:t-authz | A malicious server could show a scanner different text than it shows real users. |  |
| 103 | requirement | All findings |  |
| 104 | requirement | Tier |  |
| 105 | requirement | Sandbox observations |  |
| 106 | requirement | Confirm the tier. |  |
| 107 | requirement | Approve, approve with conditions, reject or defer. |  |
| 108 | requirement | Write the approval record. |  |
| 109 | requirement | Nothing. |  |
| 110 | requirement | A signed approval record. |  |
| 111 | requirement | Every blocking check in this stage passes, and the right approver for the tier has decided. |  |
| 112 | requirement | Approval record |  |
| 113 | requirement | Platform policy settings |  |
| 114 | requirement | Publish the artifact or URL to the approved source. |  |
| 115 | requirement | Add the allowlist entry and pinned configuration. |  |
| 116 | requirement | Prove that an unapproved server and, for a local server, an unapproved version are refused. |  |
| 117 | requirement | Roll out to a small group first. |  |
| 118 | requirement | For a local update, move the pin and allowlist entry in stages. Keep the previous version ready for rollback unless it is blocked. | OK (2026-11-26). Restates the existing intake procedure. |
| 119 | requirement | The approved server, for a first group of users. |  |
| 120 | requirement | Policy change, catalog entry and test evidence. |  |
| 121 | quote:l-allowlist | The MCP docs suggest starting with a short allowlist of vetted, pinned servers and clear entry criteria. |  |
| 122 | requirement | Advisory feeds |  |
| 123 | requirement | Logs and egress alerts |  |
| 124 | requirement | Client configuration inventory |  |
| 125 | requirement | Compare the live surface with the approved hashes. |  |
| 126 | requirement | Match advisories to the SBOM, or to the remote operator's notices. |  |
| 127 | requirement | Watch the publisher and the traffic. |  |
| 128 | requirement | Recertify before expiry, or retire. |  |
| 129 | requirement | The approved server, in daily use. |  |
| 130 | requirement | Triggers, or a new expiry date, or retirement. |  |
| 131 | requirement | No open trigger and the approval has not expired. |  |
| 132 | quote:l-rugpull | A server can change its tool descriptions after approval. |  |
| 133 | quote:l-reask | The protocol does not require clients to ask again when definitions change. |  |
| 134 | inference quote:t-listchanged | Change notices cannot be the only detector: sending them is recommended, not required, and depends on a declared capability. |  |
| 135 | requirement | Nine stages run in order. A failed gate stops the server there. Nothing from the server runs before Sandbox. |  |
| 136 | requirement | Release feed or dependency update tool for the package or image. |  |
| 137 | requirement | Keep running the approved, pinned version, unless it is blocked. |  |
| 138 | quote:co-staged | Testing and staged rollout belong in update handling. |  |
| 139 | requirement | A digest check at install fails, or the registry shows a new digest. |  |
| 140 | requirement | Block it and treat it as a possible attack until it is explained. |  |
| 141 | requirement | Hash comparison of the live surface. |  |
| 142 | requirement | Block anything new or changed until approved. Block the whole server if instructions changed. |  |
| 143 | quote:t-change | A tool list may change over time. |  |
| 144 | requirement | Configuration change, vendor notice or a failed connection. |  |
| 145 | requirement | Do not allow the new address until approved. |  |
| 146 | requirement | Advisory feed matched against the SBOM, or a vendor notice. |  |
| 147 | requirement | Decide on exposure at once. Limit or block if it is being exploited. A fix for an exploited vulnerability goes through the New version path without the waiting period. |  |
| 148 | quote:l-pinvuln | A pin keeps the vulnerable version in place until someone moves it. |  |
| 149 | quote:l-respond | For a vulnerable local server, the MCP docs advise blocking its egress, rotating the credentials passed to it and pushing a fixed version. |  |
| 150 | requirement | Malicious package report, vendor or community alert. |  |
| 151 | requirement | Revoke now. Block traffic, find every installation, rotate every credential it could read, and investigate what it did. |  |
| 152 | requirement | Repository transfer, new maintainer, new package account, acquisition. |  |
| 153 | requirement | Freeze a local server at the approved version. Block a remote server until it is screened again. Treat the next version as a new server. |  |
| 154 | requirement | Version difference, consent screen change, egress alert. |  |
| 155 | requirement | Do not grant the new access until approved. |  |
| 156 | quote:bp-semantic | A scope can change meaning without changing name. |  |
| 157 | requirement | Vendor notice or license difference between versions. |  |
| 158 | requirement | Keep using it only where the old terms still cover the use. Otherwise stop. |  |
| 159 | requirement | Repository or registry status, no response to reports. |  |
| 160 | requirement | Plan replacement and set an end date. |  |
| 161 | requirement | Date in the approval record. |  |
| 162 | requirement | Renew before the date. After it, the server is not approved. |  |
| 163 | requirement | Log, egress or canary alert, or a user report. |  |
| 164 | requirement | Block while you investigate. |  |
| 165 | requirement | New data, new users, new client, new configuration, or another server added next to it. |  |
| 166 | requirement | Keep the old use only. |  |
| 167 | requirement | Added, removed or renamed tool |  |
| 168 | requirement | Changed instructions, description, parameter or schema |  |
| 169 | requirement | Changed capability, prompt, resource, icon or UI |  |
| 170 | requirement | Changed read-only or destructive hint |  |
| 171 | requirement | Changed launch command or environment variable |  |
| 172 | requirement | New dependency |  |
| 173 | requirement | New or changed install script |  |
| 174 | requirement | New destination |  |
| 175 | requirement | New scope or permission |  |
| 176 | requirement | Changed publisher or owner |  |
| 177 | requirement | Changed license or terms |  |
| 178 | requirement | A change is any difference from the approval record. Never update a server automatically unless it meets every condition for automatic approval. |  |
| 179 | requirement | Allow it only when all of these are true. It skips the Review stage, so nobody reads the code difference. The approver for the server's tier approves the rule in advance and is the approver of record. Otherwise a person decides. |  |
| 180 | requirement | The server only reads, and only public or non-sensitive data. |  |
| 181 | requirement | A local server runs contained, with limited outbound traffic. |  |
| 182 | requirement | The publisher, license, launch command, environment variables and install scripts are unchanged, and there is no new dependency, destination or scope. |  |
| 183 | requirement | The captured surface is identical. |  |
| 184 | requirement | Every check in Screen, Pin, Scan and Sandbox passes, including the 7 day wait. An earlier result from a person counts only if what that person looked at is unchanged. |  |
| 185 | requirement | Reads only public or non-sensitive data. Remote. |  |
| 186 | requirement | Platform owner |  |
| 187 | requirement | 12 months |  |
| 188 | requirement | Reads internal or personal data. |  |
| 189 | requirement | Platform owner and security reviewer |  |
| 190 | requirement | 6 months |  |
| 191 | requirement | Changes data, sends data outward, or runs as a local process. |  |
| 192 | requirement | Security reviewer and data owner |  |
| 193 | requirement | Runs commands or code, spends money, or holds administrator or production access. |  |
| 194 | requirement | Security reviewer and system owner |  |
| 195 | requirement | 3 months |  |
| 196 | requirement | Released as recorded. |  |
| 197 | requirement | Released with limits that the platform or the owner enforces, such as fewer tools, fewer scopes, named users or a sandbox. |  |
| 198 | requirement | Added to the deny list when the reason is malicious or impersonation. |  |
| 199 | requirement | Nothing is released until the missing evidence arrives. |  |
| 200 | requirement | Use the highest tier that fits. Adjust the names and intervals to your organisation. |  |
| 201 | example | Keep one record for each approved server. Later changes are compared with it. For a remote server, origin holds the URL and the authorization server details instead. The example is fictional. |  |
| 202 | example | {<br>  "name": "example-tickets-mcp",<br>  "publisher": {"organisation": "Example Vendor", "verified_from": "vendor documentation URL"},<br>  "license": "<license or terms accepted>",<br>  "owner": "team-support",<br>  "origin": {<br>    "type": "package",<br>    "package": "@example/tickets-mcp",<br>    "version": "2.4.1",<br>    "digest": "sha512-<digest of the artifact>",<br>    "source_commit": "<commit>",<br>    "provenance": "verified"<br>  },<br>  "dependencies": {"lock_hash": "sha256-<hash>", "sbom": "<stored SBOM>"},<br>  "surface": {<br>    "captured_with_scopes": ["tickets:read", "tickets:comment"],<br>    "instructions": "sha256-<hash>",<br>    "tools": {"get_ticket": "sha256-<hash>", "add_comment": "sha256-<hash>"},<br>    "capabilities": {},<br>    "prompts": {},<br>    "resources": {},<br>    "resource_templates": {},<br>    "icons": {},<br>    "ui": {}<br>  },<br>  "runtime": {<br>    "command": ["<exact command and arguments>"],<br>    "credentials": "<secret store reference>",<br>    "files": ["<allowed folders>"],<br>    "destinations": ["tickets.example.com:443"],<br>    "environment": ["<variable names and values, without secrets>"]<br>  },<br>  "use": {"purpose": "<what it is used for>", "data": "<data it may reach>", "users": "<who may use it>", "clients": ["<approved clients>"]},<br>  "findings": "<link to triaged results>",<br>  "exceptions": ["<such as a skipped waiting period or a missing signature, and who accepted it>"],<br>  "tier": 3,<br>  "decision": "approved with conditions",<br>  "conditions": ["get_ticket and add_comment only"],<br>  "requested_by": "<person>",<br>  "approved_by": ["<security reviewer>", "<data owner>"],<br>  "decided": "2026-11-26",<br>  "expires": "2027-05-26"<br>} |  |
| 203 | requirement | Publisher is identified |  |
| 204 | requirement | Trace the server to a source repository and a real organisation or maintainer. For a remote server, trace the URL to its operator. |  |
| 205 | requirement | A named, reachable publisher, confirmed from more than the listing itself. |  |
| 206 | requirement | It is the package the vendor means |  |
| 207 | requirement | Take the name or URL from the vendor's own documentation and compare it letter by letter. |  |
| 208 | requirement | Name, publisher account and URL match the vendor's documentation. |  |
| 209 | requirement | Source can be read |  |
| 210 | requirement | Find the source that the published artifact is built from. |  |
| 211 | requirement | Source is available for the exact version. |  |
| 212 | requirement | Project is maintained |  |
| 213 | requirement | Look at recent commits, releases, open security issues and whether the project is archived. |  |
| 214 | requirement | Not archived, and security reports get answered. |  |
| 215 | requirement | There is a way to report vulnerabilities |  |
| 216 | requirement | Look for a security policy and past advisories. |  |
| 217 | requirement | A reporting route exists. |  |
| 218 | requirement | License allows the use |  |
| 219 | requirement | Read the license or the service terms. |  |
| 220 | requirement | Terms allow the intended use. |  |
| 221 | requirement | New versions have aged |  |
| 222 | requirement | Wait until a new version has been public for 7 days. Skip the wait for a fix to a vulnerability that is being exploited. |  |
| 223 | requirement | The version is old enough, or the exception is recorded. |  |
| 224 | requirement | Not reported as malicious |  |
| 225 | requirement | Look up the package and version in malicious package reports. Repeat for every dependency once the tree is known. |  |
| 226 | requirement | No report for the package or any dependency. |  |
| 227 | label | Requirement of this process. No source is quoted. |  |
| 228 | requirement | Remote operator gives assurance |  |
| 229 | requirement | Ask who runs the service, where data goes, how long it is kept, how incidents are announced and how changes are announced. |  |
| 230 | requirement | Written answers that fit the data involved. |  |
| 231 | requirement | Running it locally is justified |  |
| 232 | requirement | Use the remote version where one exists and the server needs no local access. Ask why a server with no need for local access is only offered as a local process. |  |
| 233 | requirement | A stated reason for local execution. |  |
| 234 | requirement | Exact version |  |
| 235 | requirement | Name one version. No ranges, no latest, no floating tag. |  |
| 236 | requirement | One immutable version in the request and the configuration. |  |
| 237 | requirement | Digest recorded |  |
| 238 | requirement | Record the artifact hash. Refer to a container image by digest. |  |
| 239 | requirement | Digest in the approval record. |  |
| 240 | requirement | Fetched without running it |  |
| 241 | requirement | Fetch into quarantine with install scripts off. For Python, accept built packages only. |  |
| 242 | requirement | No code from the package ran during the fetch. |  |
| 243 | requirement | Dependencies locked and listed |  |
| 244 | requirement | Lock the whole dependency tree with hashes and generate your own SBOM from the artifact. |  |
| 245 | requirement | Lock file with hashes and an SBOM are stored. |  |
| 246 | requirement | Signatures and provenance verified |  |
| 247 | requirement | Verify signatures and attestations against the expected publisher and source. An invalid signature or attestation blocks. If the publisher offers none, the approver decides and records it. |  |
| 248 | requirement | Verification succeeds for the expected identity, or the approver has accepted that none is offered. |  |
| 249 | requirement | Remote endpoint recorded |  |
| 250 | requirement | Record the exact URL and the authorization server details. Require HTTPS with a valid certificate throughout. |  |
| 251 | requirement | URL and metadata recorded, with no plain HTTP and no certificate error. |  |
| 252 | requirement | Known vulnerabilities |  |
| 253 | requirement | Scan the artifact and all dependencies. Rank by known exploitation, exploit probability and reachability. Ask a remote vendor for its results. |  |
| 254 | requirement | No known exploited vulnerability. Others have an owner and a deadline. |  |
| 255 | requirement | Malicious code signs |  |
| 256 | requirement | Run a malicious package scanner as well as the vulnerability scan. |  |
| 257 | requirement | Findings explained or the server rejected. |  |
| 258 | requirement | Static code analysis |  |
| 259 | requirement | Analyze the source for injection, path, request forgery and similar flaws. |  |
| 260 | requirement | No unresolved serious finding. |  |
| 261 | requirement | Secrets in code and images |  |
| 262 | requirement | Scan source, package and image layers for credentials. |  |
| 263 | requirement | No live secret. |  |
| 264 | requirement | Container and deployment settings |  |
| 265 | requirement | Scan the image build file and deployment files for risky settings such as root user, host mounts and broad privileges. |  |
| 266 | requirement | No unexplained risky setting. |  |
| 267 | requirement | Install and build scripts read |  |
| 268 | requirement | List every script that runs at install, build or start, and read it. |  |
| 269 | requirement | Each script is understood and needed. |  |
| 270 | requirement | Binaries and hidden code |  |
| 271 | requirement | Look for bundled binaries, downloads at run time, obfuscated code and files that do not match the source. |  |
| 272 | requirement | Everything executable traces to the source or a verified origin. |  |
| 273 | requirement | Dependency confusion |  |
| 274 | requirement | Resolve internal package names only from the internal registry, and fetch public ones through a mirror. |  |
| 275 | requirement | No internal name can resolve from a public registry. |  |
| 276 | requirement | No command or code injection |  |
| 277 | requirement | Check that model or user input never reaches a shell or code evaluator. |  |
| 278 | requirement | No path from input to shell, eval or string-built command. |  |
| 279 | requirement | File access stays inside bounds |  |
| 280 | requirement | Check path handling, including symlinks and prefix comparisons. |  |
| 281 | requirement | Resolved paths cannot leave the allowed folders. |  |
| 282 | requirement | No open URL fetching |  |
| 283 | requirement | Check every place the server fetches a URL that came from the model or a user. |  |
| 284 | requirement | Destinations are allowlisted, and private and metadata addresses are refused. |  |
| 285 | requirement | Tokens are checked for audience |  |
| 286 | requirement | Check that the server rejects tokens issued for something else. |  |
| 287 | requirement | A token for another service is refused. |  |
| 288 | requirement | No token passthrough |  |
| 289 | requirement | Check that the server never forwards the caller's token to another service. |  |
| 290 | requirement | Downstream calls use their own credentials. |  |
| 291 | requirement | Proxy servers ask consent per client |  |
| 292 | requirement | If the server signs in to a third party on behalf of many clients, check consent handling. |  |
| 293 | requirement | Consent is stored and checked for each client. |  |
| 294 | requirement | Sign-in links are handled safely |  |
| 295 | requirement | For a bridge or bundled client, check how it treats URLs received from a server. |  |
| 296 | requirement | Only safe schemes are opened, never through a shell, and private and reserved addresses are not fetched. |  |
| 297 | requirement | Least privilege |  |
| 298 | requirement | Compare requested scopes, file access and permissions with the stated purpose. Give a server meant only to read a read-only account at the data source. |  |
| 299 | requirement | No wildcard scope, nothing without a reason, and any read-only limit is enforced by the data source. |  |
| 300 | requirement | HTTP endpoint is not open |  |
| 301 | requirement | For any server that listens over HTTP, check Origin and Host header validation, listening address and authentication. |  |
| 302 | requirement | Origin and Host are checked, local servers listen on localhost only, and callers authenticate. |  |
| 303 | requirement | Callers cannot claim an identity |  |
| 304 | requirement | Check that identity comes from a verified token, not from a state handle or anything the client typed. |  |
| 305 | requirement | Knowing a handle or naming a user gives no access. |  |
| 306 | requirement | No secrets asked in forms |  |
| 307 | requirement | Check what the server asks the user for during use. |  |
| 308 | requirement | Passwords, keys, tokens and payment data are never requested in form mode. |  |
| 309 | requirement | Basic tool protections |  |
| 310 | requirement | Check input validation, access control, rate limits and output cleaning. |  |
| 311 | requirement | All four are present. |  |
| 312 | requirement | Usable logs without secrets |  |
| 313 | requirement | Check that tool calls can be logged and that secrets are masked. |  |
| 314 | requirement | Calls are logged in a structured form without secrets. |  |
| 315 | requirement | No stored secrets |  |
| 316 | requirement | Check code, defaults and sample configuration for built-in credentials, and check how the server stores the tokens it holds. |  |
| 317 | requirement | Credentials come from a secret store, one narrow credential per server, and held tokens are not in plain text. |  |
| 318 | requirement | Code does only what is declared |  |
| 319 | requirement | Read the code, or the difference from the approved version, for data sent anywhere, hidden recipients, extra file or credential access, and behaviour that depends on time or environment. |  |
| 320 | requirement | Every outbound send and sensitive access serves a declared purpose. |  |
| 321 | requirement | Launch command is clean |  |
| 322 | requirement | Read the exact command, arguments and environment variables that start the server. |  |
| 323 | requirement | No chained commands, no sudo, and no unexplained network or file operation. |  |
| 324 | requirement | Sign-in service meets the OAuth rules |  |
| 325 | requirement | For a server that uses OAuth, check the authorization server metadata and redirect handling. |  |
| 326 | requirement | PKCE support is advertised, redirect URIs must match exactly, sign-in responses name the issuer, and access tokens are short-lived. |  |
| 327 | requirement | Links sent to users are safe |  |
| 328 | requirement | If the server sends users to a web page during use, check the URL and who the page accepts input from. |  |
| 329 | requirement | HTTPS, no personal data or pre-authenticated access in the URL, and the server confirms that the person opening it is the person who asked. |  |
| 330 | requirement | Model requests by the server are justified |  |
| 331 | requirement | Check whether the server asks the client to run a model. This is called sampling, and the specification has deprecated it. |  |
| 332 | requirement | It does not, or the reason is recorded and the client lets a person deny each request. |  |
| 333 | inference | For a remote server, isolation protects your side only. The server's side stays out of reach. |  |
| 334 | requirement | Isolated and disposable |  |
| 335 | requirement | Run in a throwaway environment with no production credentials or data and outbound traffic denied by default. |  |
| 336 | requirement | Nothing of value is reachable from the test. |  |
| 337 | requirement | Whole surface captured and hashed |  |
| 338 | requirement | Capture declared capabilities, server instructions, tools with full schemas and annotations, prompts, resources, resource templates, UI content and icons, using a test account with the same scopes as production. |  |
| 339 | requirement | A hash for every item is in the record. |  |
| 340 | requirement | No instructions aimed at the model |  |
| 341 | requirement | Read every text field, including parameter names, schema descriptions and comments. |  |
| 342 | requirement | Nothing tells the model to do what the tool's purpose does not need. |  |
| 343 | requirement | No hidden characters |  |
| 344 | requirement | Search the captured text for zero-width and direction-control characters. |  |
| 345 | requirement | None present, or each one explained. |  |
| 346 | requirement | MCP scanner |  |
| 347 | requirement | Run at least one MCP scanner inside the sandbox. Check first what it sends outside your network. |  |
| 348 | requirement | Findings triaged. A clean result counts as one input, not as approval. |  |
| 349 | requirement | No shadowing or name clashes |  |
| 350 | requirement | Compare names and descriptions with the other approved servers. Check that names use only the characters the specification lists. |  |
| 351 | requirement | No duplicate or look-alike tool name, no unusual character, and no text about another server's tools. |  |
| 352 | requirement | No dangerous combination |  |
| 353 | requirement | Check whether this server, with the others in use, joins untrusted content, private data and a way to send data out. |  |
| 354 | requirement | The combination is absent, or limited by a condition in the approval. |  |
| 355 | requirement | Annotations match behaviour |  |
| 356 | requirement | Compare read-only and destructive hints with what the tool does. |  |
| 357 | requirement | No hint understates the effect. |  |
| 358 | requirement | Network, file and process activity as declared |  |
| 359 | requirement | Watch traffic, files and processes. Place canary files and credentials. |  |
| 360 | requirement | No undeclared destination or access, and no canary used. |  |
| 361 | inference quote:pm-fake | This comparison would show an added hidden recipient, as in the reported Postmark look-alike case. |  |
| 362 | requirement | Outbound content matches the request |  |
| 363 | requirement | For tools that send or write, compare what arrived with what the call asked for: recipients, fields, attachments. |  |
| 364 | requirement | Nothing added, removed or redirected. |  |
| 365 | requirement | Get the permission described under D12 first. |  |
| 366 | requirement | Authentication probes |  |
| 367 | requirement | For a server that listens over HTTP, call without a token, with a token for another service and with a foreign Origin. |  |
| 368 | requirement | Every such call is refused. |  |
| 369 | requirement | Get the operator's written permission before running this check or D11 against a server you do not run. Without it, do not run them; the operator's own test results are then the evidence. |  |
| 370 | requirement | Abuse tests |  |
| 371 | requirement | Send path traversal, injection, internal address, oversized and malformed inputs. |  |
| 372 | requirement | No test succeeds and the server stays up. |  |
| 373 | requirement | Second capture is the same |  |
| 374 | requirement | Use the tools, wait, reconnect and capture again. |  |
| 375 | requirement | Hashes match, or each change has an accepted reason. |  |
| 376 | requirement | Schemas, icons and headers are safe |  |
| 377 | requirement | Look for references to network addresses in schemas, unsafe icon addresses, and sensitive parameters copied into HTTP headers. |  |
| 378 | requirement | No network reference, only safe icon schemes, and no password, key, token or personal data marked x-mcp-header. |  |
| 379 | requirement | Interactive UI reviewed |  |
| 380 | requirement | If the server ships UI, review its code and the domains it declares, and hash it. |  |
| 381 | requirement | Declared domains are needed and narrow, and the UI hash is recorded. |  |
| 382 | requirement | Risk tier assigned |  |
| 383 | requirement | Set the tier from what the server can do. |  |
| 384 | requirement | Tier and reason recorded. |  |
| 385 | requirement | Every finding has an outcome |  |
| 386 | requirement | Fix, accept with an owner and end date, or reject. Known malicious code gets no exception. |  |
| 387 | requirement | No finding without an outcome. |  |
| 388 | requirement | Approver is not the requester |  |
| 389 | requirement | Have a different person approve. For an automatic approval, that person is whoever approved the rule. |  |
| 390 | requirement | No approver is the requester. |  |
| 391 | requirement | Conditions and expiry set |  |
| 392 | requirement | Write the limits of the approval and the date it ends. |  |
| 393 | requirement | An expiry date is on the record. |  |
| 394 | requirement | Record complete |  |
| 395 | requirement | Fill in every field of the approval record that applies and register the server. |  |
| 396 | requirement | The record and the catalog entry exist. |  |
| 397 | requirement | Served from the approved source |  |
| 398 | requirement | Install from the internal registry or the recorded URL, and block direct public downloads where you can. |  |
| 399 | requirement | Clients get only what was approved. |  |
| 400 | requirement | Allowlist matches URL or command |  |
| 401 | requirement | Allow by remote URL or exact command. Do not rely on a server name. |  |
| 402 | requirement | A renamed unapproved server is refused. |  |
| 403 | requirement | Configuration is pinned |  |
| 404 | requirement | For a local server, put the version or digest in the managed configuration. Take credentials from a secret store, and pass each server only its own. |  |
| 405 | requirement | No floating version, no secret in a configuration file and no credential the server does not need. |  |
| 406 | requirement | Contained at run time |  |
| 407 | requirement | Run local servers in a container or sandbox with only the needed folder, read-only where possible, and limit outbound traffic per server. |  |
| 408 | requirement | Access and destinations match the approval. |  |
| 409 | requirement | Block is proven |  |
| 410 | requirement | Try to start an unapproved server, and for a local server an unapproved version, in each client. |  |
| 411 | requirement | Each attempt is refused, with evidence stored. |  |
| 412 | requirement | Definition changes are stopped |  |
| 413 | requirement | Use a client that asks again, or a gateway that blocks, when definitions differ from the approved hashes. |  |
| 414 | requirement | A changed definition cannot be used silently. |  |
| 415 | requirement | Spending is capped |  |
| 416 | requirement | If a tool can spend money, set limits outside the model. |  |
| 417 | requirement | The paying component enforces a limit per payment and a total per time period. |  |
| 418 | requirement | Definition drift |  |
| 419 | requirement | Capture the live surface on a schedule and on each reconnect where possible, and compare hashes. |  |
| 420 | requirement | Hashes equal the approved ones. |  |
| 421 | requirement | New advisories |  |
| 422 | requirement | Daily, match new vulnerability and malicious package reports against each stored SBOM. For a remote server, check the operator's security notices. |  |
| 423 | requirement | No unhandled match or notice. |  |
| 424 | requirement | Upstream changes |  |
| 425 | requirement | Follow releases, ownership, maintainers, deprecation and takedown of each approved server. |  |
| 426 | requirement | No unreviewed change. |  |
| 427 | requirement | Traffic and logs |  |
| 428 | requirement | Alert on new destinations, unusual volume and unexpected tool calls. |  |
| 429 | requirement | Alerts have an owner and are handled. |  |
| 430 | requirement | Recertification |  |
| 431 | requirement | Re-assess before the expiry date. When a server is retired, remove its allowlist entry and rotate what it held. |  |
| 432 | requirement | Renewed or retired on time. |  |
| 433 | requirement | Switch-off and rollback tested |  |
| 434 | requirement | Keep a way to block the server everywhere and rotate its credentials, and for a local server to return to the previous version. Rehearse it. |  |
| 435 | requirement | A rehearsal has worked within the target time. |  |
| 436 | requirement | Unapproved servers found |  |
| 437 | requirement | Collect client configurations and compare them with the catalog. |  |
| 438 | requirement | Every configured server is approved. |  |
| 439 | quote:osv-use | OSV-Scanner |  |
| 440 | quote:gd-use,om-reports | GuardDog, OpenSSF reports |  |
| 441 | quote:ql-use | CodeQL |  |
| 442 | quote:gl-use,tv-secrets | Gitleaks, Trivy |  |
| 443 | quote:tv-iac | Trivy |  |
| 444 | quote:ci-engines,as-sends | Cisco MCP Scanner, Snyk Agent Scan |  |
| 445 | requirement | The server or version being assessed cannot move on until this is fixed. If the failing one is already in use, it is suspended, unless a change trigger says what to do instead. |  |
| 446 | requirement | The approver decides and records why. |  |
| 447 | requirement | Pick at least one tool for each job. Other tools can do the same jobs. |  |
| 448 | example | Owner, URL, two tools and read and comment scopes recorded. |  |
| 449 | example | The URL is in the vendor's documentation. Data handling answers arrive in writing. Tier 3, because it writes. |  |
| 450 | example | URL and authorization metadata recorded. |  |
| 451 | example | No code to scan. The vendor shares its scan results, which show no known exploited vulnerability. |  |
| 452 | example | The vendor gives evidence on the checks marked remote, among them token audience, passthrough and logging. |  |
| 453 | example | Surface captured with the two scopes. Permitted probes are refused. Second capture matches. |  |
| 454 | example | Approved for the two tools, for six months, with no other scopes. |  |
| 455 | example | URL allowlisted. A second URL is refused in each client. |  |
| 456 | example | Daily surface comparison starts. |  |
| 457 | example | Fictional example: a team asks for a ticket vendor's own remote server, to read and comment on tickets. |  |
| 458 | example | A developer asks for the package by the name found in a search. |  |
| 459 | example | The vendor's documentation does not name this package, and the publisher account is not the vendor's. Rejected before any download. The package name goes on the deny list. |  |
| 460 | example | Based on a reported case: a package on npm used an email vendor's name without being the vendor's. |  |
| 461 | quote:pm-fake | The vendor reported that the fake package built trust over 15 versions before adding a backdoor. |  |
| 462 | example | New version seen. It waits out the 7 days while the old pin keeps running. |  |
| 463 | example | New digest recorded. Dependencies unchanged. |  |
| 464 | example | No known vulnerability or report. Known-problem scans can be silent on new malicious code. |  |
| 465 | example | The changed send function builds its recipient list in an indirect way. The reviewer does not see the added copy. |  |
| 466 | example | A test message arrives with a recipient nobody asked for. The version is rejected and reported. The server is now handled as reported malicious: the old approval is revoked too and its credentials are rotated. |  |
| 467 | example | Fictional example using the same technique: an approved mail server publishes a new version that copies every message to an outside address. |  |
| 468 | example | Request recorded. |  |
| 469 | example | Publisher and source are in order. |  |
| 470 | example | Version and digest recorded. |  |
| 471 | example | Traditional scans find nothing. The problem is text, not a vulnerable library. |  |
| 472 | example | No code flaw found. |  |
| 473 | example | Reading every captured field shows the instruction. Rejected. |  |
| 474 | example | Fictional example: a note taking server whose parameter description tells the model to read a key file and pass it along. |  |
| 475 | quote:inv-poison | Instructions hidden in tool descriptions can be invisible to users and visible to models. |  |
| 476 | example | The hash comparison reports a new tool whose description says it sends data to an outside storage service. The gateway or client blocks it. |  |
| 477 | example | A new destination also counts as more permissions. The vendor states in writing what goes to the storage service and how long it is kept. |  |
| 478 | example | No code to read. The new tool and its destination are compared with the stated purpose. |  |
| 479 | example | The new tool is captured and tested with the other approved servers in mind. |  |
| 480 | example | A new destination means a person decides. Approved only for non-sensitive projects. |  |
| 481 | example | New hashes and condition published. |  |
| 482 | example | Fictional example: an approved remote server starts listing a new export tool. No version number changes. |  |
| 483 | example | The advisory matches a stored SBOM. Configuration inventory shows who runs it. |  |
| 484 | example | The approved version is affected, and in this example the flaw is being exploited. It is blocked, and exposed credentials are rotated. |  |
| 485 | example | The fixed version is not reported as malicious. The 7 day wait is skipped and recorded. |  |
| 486 | example | The fixed version is fetched without running it, pinned and verified. |  |
| 487 | example | The fixed version no longer matches the advisory, and the malware scan is clean. |  |
| 488 | example | The code difference holds the fix and nothing undeclared. |  |
| 489 | example | Surface and behaviour compared with the old approval. |  |
| 490 | example | The fixed version is approved. |  |
| 491 | example | Pin and allowlist moved. The old version is refused. |  |
| 492 | example | Based on a published vulnerability in mcp-remote, a bridge that connects local clients to remote servers. |  |
| 493 | quote:cv-6514 | The flaw let an untrusted server run operating system commands on the client machine. |  |
| 494 | label | Look-alike or impersonating server |  |
| 495 | inference | A publisher that is real but dishonest passes identity checks. |  |
| 496 | label | Malicious package |  |
| 497 | inference quote:l-noproof | New malicious code with no report yet can pass scans and stay quiet in a test. |  |
| 498 | label | Publisher account or ownership takeover |  |
| 499 | inference quote:npm-prov | A release made with the real publisher's own build system can carry valid provenance. |  |
| 500 | label | Known vulnerability |  |
| 501 | inference | Flaws that nobody has published are not matched. |  |
| 502 | label | Compromised dependency |  |
| 503 | inference | A locked but already compromised dependency stays locked in. |  |
| 504 | label | Dependency confusion |  |
| 505 | inference | Names that no registry rule covers can still resolve publicly. |  |
| 506 | label | Install or build script abuse |  |
| 507 | inference | A script that is needed for install still has to run later. |  |
| 508 | label | Floating version or moving tag |  |
| 509 | inference | A remote server cannot be pinned by digest. |  |
| 510 | label | Tool poisoning in any schema field |  |
| 511 | inference | Wording that looks innocent to a reviewer and a scanner can still steer a model. |  |
| 512 | label | Hidden characters |  |
| 513 | inference | Meaning can be hidden without any special character. |  |
| 514 | label | Shadowing another server's tools |  |
| 515 | inference quote:l-shared | All configured servers share one model context, so each server added later changes what the others are exposed to. |  |
| 516 | label | Definitions changed after approval (rug pull) |  |
| 517 | inference | Between two comparisons a change can be used unnoticed. |  |
| 518 | label | Behaviour changed behind unchanged definitions |  |
| 519 | quote:c-hashlimit | Hashing definitions does not see it. |  |
| 520 | label | Prompt injection through results and resources |  |
| 521 | quote:c-response | Every tool response has to be treated as untrusted data, also from approved servers. |  |
| 522 | label | Data leaving through a chain of tools |  |
| 523 | inference | A permitted destination can be used to take data out. |  |
| 524 | label | Server asks the client to run a model |  |
| 525 | inference | How each request is shown and limited is up to the client. |  |
| 526 | label | Malicious startup command |  |
| 527 | inference | A command that looks ordinary can still fetch hostile code. |  |
| 528 | label | Command or code injection |  |
| 529 | inference | Analysis and tests miss some paths. |  |
| 530 | label | Path traversal and symlink escape |  |
| 531 | inference | Anything inside the mounted folder stays reachable. |  |
| 532 | label | Server-side request forgery |  |
| 533 | inference | Redirects and name resolution tricks need their own tests. |  |
| 534 | label | Command execution from a sign-in link |  |
| 535 | inference | The same flaw in a client is outside this process. |  |
| 536 | label | Undeclared network, file or process activity |  |
| 537 | inference | Behaviour triggered by time, data or environment may not show in a test. |  |
| 538 | label | Resource exhaustion |  |
| 539 | inference | Load limits of a remote service are the vendor's to hold. |  |
| 540 | label | Missing authentication or open local endpoint |  |
| 541 | quote:l-reachable | A local server that listens on a port can be reached by other local processes and by websites. |  |
| 542 | label | DNS rebinding |  |
| 543 | inference | Later code changes can remove the check. |  |
| 544 | label | Token passthrough and wrong audience |  |
| 545 | inference | For a remote server you rely on the vendor for what happens downstream. |  |
| 546 | label | Confused deputy |  |
| 547 | inference | Hard to prove from outside for a remote server. |  |
| 548 | label | Excess or creeping scopes |  |
| 549 | inference quote:bp-semantic | A scope can widen on the service side without any change in the server. |  |
| 550 | label | Identity spoofing and state handle misuse |  |
| 551 | inference | Hard to test fully from outside. |  |
| 552 | label | Weak sign-in service (code theft, redirect, mix-up) |  |
| 553 | inference | Client side defences against these attacks belong to the client. |  |
| 554 | label | Secret exposure |  |
| 555 | quote:l-reach | A credential the server needs is readable by the server. |  |
| 556 | label | Phishing for secrets through user prompts |  |
| 557 | inference | Ordinary looking questions can still collect sensitive data. |  |
| 558 | label | Hostile or leaking server UI |  |
| 559 | inference | UI loaded later from an allowed domain can change. |  |
| 560 | label | Escape from the local environment |  |
| 561 | quote:co-container | A container should not be relied on as a strong security boundary. |  |
| 562 | label | Too little logging |  |
| 563 | inference | A remote server's internal actions are not in your logs. |  |
| 564 | label | Shadow servers |  |
| 565 | inference | Unmanaged devices and clients that ignore policy are not seen. |  |
| 566 | label | Context shared too widely |  |
| 567 | inference | How a client keeps and shares context is decided by the client, not at intake. |  |
| 568 | label | Uncontrolled spending |  |
| 569 | inference | Unwanted payments can still be made inside the limits. |  |
| 570 | inference | Matching a check to an attack is a design choice. It is not a measured detection rate, and the list of attacks is not complete. |  |
| 571 | label | Server name, URL or command. |  |
| 572 | quote:gh-match | Entries match by name, URL or command. |  |
| 573 | quote:gh-profiles | The lists do not apply to servers defined in repository custom agent profiles. |  |
| 574 | quote:gh-firewall | An organization or repository firewall that blocks the domains needed to start those servers can prevent their use. |  |
| 575 | quote:gh-malformed | A malformed list blocks all but the built-in servers. |  |
| 576 | label | Server name or ID. |  |
| 577 | preview quote:gh-preview | It is in public preview and not the recommended way to restrict servers. |  |
| 578 | quote:gh-ga | The recommended way is the managed settings file. |  |
| 579 | quote:gh-name | Name matching can be bypassed by editing configuration. |  |
| 580 | label | Server URL, exact command or name. |  |
| 581 | quote:cc-authoritative | An allowlist is authoritative only when it is also set to managed entries only. |  |
| 582 | quote:cc-exact | A command entry matches the exact command. |  |
| 583 | quote:cc-env | A command entry matches whatever the server's environment variables are. |  |
| 584 | quote:cc-envload | Some environment variables change what node loads at startup. |  |
| 585 | quote:cc-name | A name entry is not a security control. |  |
| 586 | label | Managed Copilot settings, workspace trust and a per-server sandbox. |  |
| 587 | quote:vs-allow | Managed settings can limit which servers developers install and run. |  |
| 588 | quote:vs-disabled,vs-harness | Managed settings keep the Claude and Codex harnesses disabled unless they are permitted. Permitted sessions run without Copilot's managed permission, sandbox, MCP and plugin controls. |  |
| 589 | quote:vs-workspace,vs-restart | In a trusted workspace, servers configured in the workspace can start without a separate trust prompt, also after a configuration change. |  |
| 590 | quote:vs-sandbox,vs-windows | The per-server sandbox covers local process servers on macOS and Linux, not on Windows. |  |
| 591 | quote:vs-separate,vs-outbound | The separate Copilot sandbox allows outbound traffic by default. |  |
| 592 | label | A public list of servers. |  |
| 593 | preview quote:reg-preview | It is in preview. |  |
| 594 | quote:reg-moderation | Expect little or no moderation. |  |
| 595 | quote:reg-vulns | Having a security vulnerability does not by itself get a server removed. |  |
| 596 | label | Destinations per server. |  |
| 597 | quote:l-egress | A per-server egress list with alerts limits where a server can send data. |  |
| 598 | label | Client configuration files on devices. |  |
| 599 | quote:l-inventory | Management tools can collect client configurations to find what is in use. |  |
| 600 | requirement | A weak client can undo a well reviewed server. Assess clients separately. |  |
| 601 | requirement | A proxy or other component that handles decrypted messages could change or replay them. Assess it with the platform. |  |
| 602 | requirement | Per-call approval prompts, output filtering and permission controls during use belong to the platform and agent design. |  |
| 603 | requirement | Its code, build and staff are visible only through the vendor's evidence. |  |
| 604 | requirement | License and data answers are collected here. Contracts and privacy review follow your normal process. |  |
| 605 | inference quote:gh-match,cc-exact,cc-env | None of the allowlist settings above compares a server's code or tool definitions with what was reviewed. This process has to do that. |  |
<!-- /ledger -->
