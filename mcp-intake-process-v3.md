# MCP Server Intake Process

**Purpose:** Ensure MCP servers are security assessed, approved and securely configured before use within the organization.

**Scope:** All local, internally hosted and externally hosted MCP servers.

## Process overview

| Step | Activity | Responsible | Outcome |
|---|---|---|---|
| 1 | Request | Requester | Completed intake request |
| 2 | Classify | Platform team | Deployment model and risk level |
| 3 | Assess | Security team / automation | Completed security assessment |
| 4 | Approve | Designated approver | Documented approval decision |
| 5 | Enable and monitor | Platform team | Securely configured and monitored integration |

The platform team may skip steps 2 to 4 if a current approval covers the same server, configuration and intended use. Check its recorded scope against the requested client, execution identity, available tools, data access and restrictions.

## Step 1 – Request

The requester provides the following information:

| Information | Example |
|---|---|
| MCP server | GitHub MCP Server |
| Link to server or package | Official repository |
| Business justification | Assist developers with issue management |
| Intended users | Development team |
| Systems and data accessed | Internal GitHub repositories |
| Required permissions | Read repositories, create issues |
| Business owner | Development team manager |

The requester should not be expected to answer technical security questions.

**Outcome:** A completed intake request.

## Step 2 – Classify

Determine how the MCP server is deployed and the risk associated with its intended use.

### Deployment model

| Type | Description |
|---|---|
| Local | Executed on the user's device |
| Internally hosted | Executed in organization-controlled infrastructure |
| Externally hosted | Executed in third-party infrastructure |

### Risk level

| Risk | Criteria |
|---|---|
| Low | Public data, read-only access and restricted execution |
| Medium | Internal data or limited write access |
| High | Sensitive data, privileged access, destructive operations or unrestricted local execution |

Use the highest applicable risk level. The classification must consider the server's **effective privileges**, not just its advertised functionality.

**Outcome:** Deployment model and risk classification.

## Step 3 – Assess

Perform a security assessment using the four domains from the [MCP Server Trust Assessment Guide](https://nhimg.org/mcp-server-trust-assessment-guide). Use automated scanning wherever possible. Manually assess controls where automated verification is insufficient. Follow the [Security assessment methodology](#security-assessment-methodology) for signals, scanning techniques and assessment execution.

Wiz reported that about 70% of exposed MCP servers it tested returned their full tool catalog to anonymous callers, reinforcing the need to verify authentication and authorization ([Wiz Research](https://www.wiz.io/blog/the-risk-hiding-behind-exposed-mcp-servers)).

| Assessment domain | Key question |
|---|---|
| **Identity and authentication** | Can we trust the server's identity and authentication mechanisms? |
| **Permissions and tool surface** | Does the server only have the access and functionality it needs? |
| **Provenance** | Can we trust where the server and its software originate from? |
| **Change control** | Can we detect, control and respond to changes? |


Each security control receives one of four results:

| Result | Meaning |
|---|---|
| PASS | Requirement satisfied, supported by evidence |
| FAIL | Requirement not satisfied |
| UNKNOWN | Insufficient evidence |
| N/A | Not applicable, with justification |

**Outcome:** A completed security assessment with findings and recommended safeguards.

## Step 4 – Approve

The designated approver reviews the assessment and makes a decision.

| Decision | Description |
|---|---|
| Approved | Security requirements are satisfied |
| Approved with restrictions | Identified risks are mitigated through enforceable safeguards |
| Rejected | Security risks are unacceptable or mandatory requirements cannot be verified |

### Approval authority

| Risk level | Approver |
|---|---|
| Low | Platform team |
| Medium | Security team |
| High | Security team and relevant system or data owner, with escalation where required |

Use these mandatory controls as the minimum production approval checklist. For any additional mandatory control, the security team records when it applies and what evidence counts as a pass before testing.

| Mandatory control | Applies to | Pass condition |
|---|---|---|
| Server identity | All integrations | The artifact or endpoint matches the verified publisher or operator and is identified in the approval record. |
| Access limits | All integrations | Checks of the execution identity and effective permissions confirm that access stays within the approved scope. |
| Token handling | Servers accepting MCP OAuth access tokens | The server rejects tokens issued for another audience. If it calls a downstream API, it uses a separate credential intended for that API. |
| Enforcement of restrictions | Approvals that depend on a restriction | A test in the intended configuration shows that the restriction works. For read-only access, verify that a write is denied. |
| Revocation | All integrations | A test confirms that the platform team can disable the integration and cut off its access. |

Every applicable mandatory control must pass for production approval, including approval with restrictions. A FAIL or UNKNOWN blocks approval until evidence supports a PASS.

**Outcome:** A documented approval decision with any conditions.

## Step 5 – Enable and monitor

The platform team registers the server in the approved MCP catalogue and ensures the approved configuration and restrictions are enforced.

Reassessment is required when there is a material change to:

- Software version or artifact.
- Client configuration, available tools, agent capabilities, permissions, accessible credentials or enforcement controls.
- Authentication mechanisms.
- Server operator or hosting environment.
- Intended use, content sources or data access.
- Known security risks.

Reassess planned material changes before enabling them. If an unexpected change invalidates a mandatory approval condition, the platform team suspends affected access pending reassessment. Approval can be revoked at any time.

**Outcome:** A securely configured and continuously governed MCP integration.

---

## Security assessment methodology

This section supports Step 3. It defines what evidence to collect, how to collect it and how to evaluate it. The intake workflow remains independent of specific scanning products.

Assess the MCP server in the context of its intended execution environment: the MCP client, execution identity, accessible credentials, other available tools, exposure to untrusted content and runtime security controls. A server that is acceptable in isolation may introduce unacceptable risk when combined with other agent capabilities.

### 1. Security signals and verification methods

Collect the applicable signals in each of the four assessment domains. Use deterministic tests where possible, heuristic scanning to identify suspicious behavior, and manual review where technical evidence is insufficient.

Automation: **Automatable** means machine-checkable; **Partial** means automated evidence still needs human review; **Manual** means document or judgment review.

#### Identity and authentication

| Signal to collect | Verification method | Automation |
|---|---|---|
| Server identity, URL, domain and operator | Verify publisher affiliation, endpoint identity and TLS where applicable | Partial |
| Authentication mechanism and OAuth metadata | Protocol discovery, configuration review and metadata validation | Partial |
| Token audience, issuer and expiration | Positive and negative authentication tests using dedicated test credentials | Partial |
| Requested and granted scopes | OAuth flow inspection and comparison with required permissions | Partial |
| Credential handling and inherited environment variables | Source-code and configuration scanning; sandbox inspection | Partial |
| Effective execution identity and ambient credentials (SSH keys, Git, cloud and package registry credentials) | Inspect process identity, inherited privileges and accessible credential stores; test isolation using synthetic credentials | Partial |
| Token passthrough and downstream credentials | Trace credential use and verify that downstream API calls use credentials intended for that API | Partial |
| Shared or long-lived credentials | Configuration and documentation review | Partial |

**Investigate:** Invalid credentials being accepted, insecure token handling, token passthrough, unnecessarily privileged credentials and access to unrelated credentials.

#### Permissions and tool surface

| Signal to collect | Verification method | Automation |
|---|---|---|
| Available tools, resources and prompts | MCP protocol enumeration, including pagination and relevant identity contexts | Automatable |
| Tool names, descriptions, schemas and annotations | MCP-specific scanning and baseline comparison | Automatable |
| Read, write, delete and administrative capabilities | Semantic classification, source analysis and controlled testing | Partial |
| Prompt injection and tool poisoning indicators | Signature-based and AI-assisted analysis of metadata and representative responses | Partial |
| Exposure to untrusted content and indirect prompt injection | Identify who can control retrieved content; perform risk-based adversarial tests with synthetic content in the intended client or agent | Partial |
| Cross-tool attack potential | Review other available tools and their combined permissions; test representative attack paths where warranted | Partial |
| Effective permissions to underlying systems | Credential inspection, authorization tests and comparison with business needs | Partial |
| Filesystem access, network destinations and child processes | Static analysis and sandbox monitoring | Partial |
| Telemetry, external data recipients and sensitive data disclosure | Data-flow analysis, source inspection, controlled network monitoring and supplier documentation | Partial |
| Hidden functionality and input validation | Source analysis and authorized negative testing | Partial |
| Tool naming collisions | Comparison with other approved servers | Automatable |

**Investigate:** Excessive privileges, model-directed malicious instructions, arbitrary command execution, unexpected data destinations, disclosure of sensitive data, unsafe combinations of tools and discrepancies between declared and observed behavior. Tool annotations are not proof of actual behavior.

#### Provenance and supply chain

| Signal to collect | Verification method | Automation |
|---|---|---|
| Publisher, maintainer and vendor affiliation | Registry, repository and official vendor documentation comparison | Partial |
| Relationship between repository and distributed artifact | Build provenance and attestation verification where available | Partial |
| Package version and artifact digest | Compare against an independently established approved digest | Automatable |
| Signatures and attestations | Verify signatures, trusted signer identity and artifact binding | Automatable |
| Direct and transitive dependencies | SBOM generation and software composition analysis (SCA) | Automatable |
| Known vulnerabilities and malware | Vulnerability databases, malware signatures and threat intelligence | Automatable |
| Suspicious code, obfuscation, installation scripts and dynamic downloads | Static code analysis, malware scanning and AI-assisted review | Partial |
| Embedded credentials | Secret scanning | Automatable |
| Maintenance, publisher and release history | Review package age, release activity, maintainer and ownership changes, and changes in signing identity where historical evidence is available | Partial |
| Package impersonation and typosquatting | Compare names and publisher namespaces against official vendor and registry information | Partial |
| External hosting and supplier security | Supplier documentation and security assessment | Manual |

**Investigate:** Unverified publishers, impersonation, compromised packages, exploitable vulnerabilities, unexplained obfuscation and unverified executable dependencies. Provenance does not prove that software is safe. Package age, popularity and ownership changes are risk signals, not proof of compromise or trustworthiness.

#### Change control

| Signal to collect | Verification method | Automation |
|---|---|---|
| Approved artifact and resolved dependency identities | Digest and dependency integrity verification | Automatable |
| Approved endpoint, transport and authentication configuration | Configuration and protocol inspection | Partial |
| Tool, resource and prompt definitions | Canonicalized metadata fingerprints and baseline comparison | Automatable |
| Changes to code, dependencies and permissions | Differential scanning and configuration comparison | Automatable |
| Update mechanisms, floating versions/tags and runtime code downloads | Inspect startup commands, package configuration and source code; monitor controlled execution | Partial |
| Deployed MCP client configuration and configuration drift | Enumerate configured servers and compare endpoints, commands, arguments, environment and overrides with the approved baseline | Automatable |
| Enforcement of approved servers, tools and access restrictions | Test that unauthorized connections, execution and tool calls are blocked at the relevant client, endpoint or gateway | Partial |
| Ability to disable the integration and revoke access | Functional testing of enforcement and revocation mechanisms | Partial |
| Audit logging and agent-to-tool traceability | Generate test events and correlate initiating user or agent, tool call, authorization decision and outcome where supported; avoid recording secrets or unnecessary sensitive payloads | Partial |
| Supplier change notification | Documentation and contractual review | Manual |

**Investigate:** Unapproved changes, mutable execution dependencies, uncontrolled upgrades, unauthorized client configurations, bypassable policies, missing audit evidence and inability to revoke access. Remote capability fingerprints detect observable interface changes, not changes to hidden backend behavior.

### 2. Scanning techniques and applicability

Select the techniques appropriate to the deployment model. Reuse existing enterprise security tooling where possible.

For externally hosted servers, review provider-supplied security information when available, such as independent audit reports, penetration-test summaries and security documentation. Check its scope and date against the service being assessed.

| Technique | Local | Internally hosted | Externally hosted | Example tools or methods |
|---|---|---|---|---|
| Provenance and identity verification | Required | Required | Required | MCP Registry, Sigstore, npm provenance, vendor verification |
| Dependency inventory and vulnerability scanning | Required | Required | If available | Syft (SBOM), OSV-Scanner (SCA) |
| Static code analysis (SAST) | Required | Required | If available | Semgrep, CodeQL |
| Malware and behavioral code analysis | Required | Required | If available | YARA, Cisco MCP Scanner |
| Secret scanning | Required | Required | If available | Gitleaks |
| MCP-specific scanning and capability discovery | Required | Required | Required | Cisco MCP Scanner, MCP Inspector |
| Authentication and authorization testing | As applicable | As applicable | As applicable | MCP Inspector, dedicated protocol and access-control tests |
| Ambient credential and execution identity analysis | Required | Required | Required for client/agent; supplier evidence for server | Process identity, environment and credential isolation tests |
| Untrusted content and cross-tool exposure analysis | Required | Required | Required | Data-flow and agent capability analysis |
| Indirect prompt injection testing | Risk-based | Risk-based | Risk-based | Synthetic adversarial content and controlled agent tests |
| Runtime behavioral analysis | Required | Required | Limited to observable behavior | Isolated sandbox, filesystem, network and process monitoring |
| Supplier security assessment | As applicable | As applicable | Required | Existing supplier assessment process |
| Update mechanism analysis | Required | Required | Supplier evidence; inspect observable changes | Startup and dependency configuration, code and runtime inspection |
| MCP client configuration scanning | Required | Required | Required | Managed configuration inventory and comparison against approved catalogue |
| Change baseline and runtime enforcement verification | Required | Required | Required | Artifact hashes, metadata fingerprints, configuration and functional tests |
| Agent-to-tool activity traceability | As applicable | As applicable | As applicable | Correlated audit events and representative tool-call tests |

Required means evidence is expected for that assessment area, not that every named product must be used. Risk-based testing is selected according to exposure, effective privileges and potential impact; document the rationale. Supplier evidence must be evaluated for scope and adequacy. Where an applicable control cannot be verified, record UNKNOWN and assess alternative evidence or enforceable compensating controls. N/A requires a justification. External black-box testing cannot establish the absence of hidden server-side behavior.

The named tools are illustrative candidates, not mandated products or validated detection-coverage guarantees. Maintain the actual toolset, versions and configurations separately. Verify scanner data handling before sending code, tool metadata or responses to external services.

#### MCP client configuration scanning

Inspect user, workspace and centrally managed configurations, including startup executables and arguments, package versions or digests, remote URLs, credential references and inherited environment settings. Verify policy precedence and whether user or repository configuration can bypass the approved configuration. Do not collect raw credential values.

During intake, inspect the proposed configuration. Before production enablement, verify that the deployed configuration and runtime restrictions match the approved baseline. After approval, repeat discovery and comparison to detect unauthorized servers and drift. Configuration discovery alone does not prove that unapproved servers cannot execute; test enforcement separately.

### 3. Assessment execution

| Order | Activity | Output |
|---|---|---|
| 1 | Identify the publisher, operator, deployment model, package or endpoint, intended client configuration and agent environment | Identified assessment target and execution context |
| 2 | Acquire available artifacts without executing untrusted code; verify provenance and perform static, dependency, malware and secret scans | Static assessment evidence |
| 3 | Connect from an isolated test environment and enumerate capabilities and authentication requirements | Capability and authentication inventory |
| 4 | Scan tool definitions, resources, prompts and representative responses; evaluate untrusted content exposure and combined tool capabilities | MCP-specific and agent-context findings |
| 5 | Perform authorized authentication, authorization, credential isolation, behavioral and risk-based indirect prompt injection tests; verify proposed enforcement controls | Protocol, runtime and enforcement findings |
| 6 | Record artifact and dependency identities, client and endpoint configuration, permissions, capability fingerprints and required runtime restrictions | Proposed approval baseline |
| 7 | Evaluate findings and unresolved controls; identify required safeguards | Completed assessment and recommendation |

**Safe execution:** Do not install or execute unapproved MCP servers on ordinary employee workstations. Use isolated test environments, restricted network access, synthetic data and dedicated least-privileged test credentials. Perform static scanning before launching local servers. Active testing of external services requires authorization. Treat server-provided content as untrusted data, including when using AI-assisted scanners. Use synthetic credentials and isolated test systems for adversarial tests; do not invoke destructive actions against production systems.

### 4. Evaluate and record evidence

Record each applicable control using the following fields:

| Field | Example |
|---|---|
| Domain / control | Provenance / artifact integrity |
| Signal | SHA-256 digest of executable artifact |
| Verification method | Compare with independently established approved digest |
| Expected result | Digests match |
| Observed result | Digests match (illustrative) |
| Status | PASS |
| Evidence | Artifact verification report |
| Assessment context | Date, assessor, target identity, scanner version, configuration and test scope |

Use the PASS, FAIL, UNKNOWN and N/A results defined in Step 3. A clean scan means no findings were detected within its scope; it does not independently prove the absence of vulnerabilities or malicious behavior. Heuristic or AI-generated findings require appropriate validation before a decision. Failed or unknown mandatory controls block production approval as defined in Step 4.

Retain evidence with the approval record. Protect sensitive information and exclude raw credentials from stored reports. Repeat relevant checks when Step 5 reassessment triggers occur, and retain the updated evidence. Monitor deployed configuration and publisher changes where feasible and investigate drift.

### Tool references

- [Cisco MCP Scanner](https://github.com/cisco-ai-defense/mcp-scanner)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [OSV-Scanner](https://google.github.io/osv-scanner/)
- [Syft](https://github.com/anchore/syft)
- [Semgrep](https://semgrep.dev/)
- [Gitleaks](https://github.com/gitleaks/gitleaks)
- [Sigstore](https://www.sigstore.dev/)
- [Official MCP Registry](https://registry.modelcontextprotocol.io/)

---

## Supporting documentation

Maintain four components initially:

| Component | Purpose | Audience |
|---|---|---|
| MCP Intake Process | The five-step process above (target: 1–2 pages) | Everyone |
| MCP Request Form | The seven questions the requester must answer (target: 5 minutes) | Requesters |
| MCP Security Assessment Checklist | Detailed security controls, verification methods, automated scan results, evidence and approval decision | Security and platform teams |
| Approved MCP Catalogue | Searchable register of approved servers, configurations, restrictions and owners | Everyone |

## Governing principles

| Principle | Requirement |
|---|---|
| **Default deny** | Only approved MCP servers may be used. |
| **Automation first** | Automate security verification wherever possible. |
| **Risk-based** | Assessment effort must be proportional to risk. |
| **Least privilege** | Only necessary permissions and capabilities are permitted. |
| **Verifiable trust** | Approval must be supported by evidence and bound to an identified artifact or remote integration. |
| **Continuous assurance** | Material changes require reassessment, and trust must be revocable. |

## Implementation notes

Keep the five-step process simple. Use the separate security assessment methodology to guide evidence collection and place detailed control tests in the security assessment checklist and supporting automation. Developers only need to understand how to request a server and where to find approved servers. Security assessors should have a repeatable checklist rather than having to interpret a lengthy policy for every request.

Avoid numerical trust scores, complicated RACI matrices and additional risk tiers initially.

The three risk levels and approval authorities are proposed organizational choices rather than requirements from the original guide. Adapt them to the existing security governance model. The separate security assessment methodology provides a common evidence collection procedure. Use the Step 4 minimum controls in the detailed checklist and add platform-specific tests where needed. The scanning applicability matrix is a proposed organizational baseline and should be validated against the available tooling and deployment environments.

**References:** [NHI MCP Server Trust Assessment Guide](https://nhimg.org/mcp-server-trust-assessment-guide) (four assessment domains); [Backslash Security – How to Evaluate an MCP Server’s Risk Before Employees Install It](https://www.backslash.security/learning/how-to-evaluate-an-mcp-server-s-risk-before-employees-install-it) (supplementary vendor guidance on endpoint and agent-context risks). The added verification methods and applicability decisions are proposed engineering requirements, not independently benchmarked scanner coverage.
