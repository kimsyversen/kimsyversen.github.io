# MCP Governance and Assessment Process

**Purpose:** Ensure MCP servers are security assessed, approved and securely configured before use within the organization.

**Scope:** All local, internally hosted and externally hosted MCP servers.

## Process overview

| Step | Activity | Responsible | Outcome |
|---|---|---|---|
| 1 | Request | Requester | Completed intake request |
| 2 | Classify | Platform team | Deployment model and risk level |
| 3 | Assess | Security team | Completed security assessment |
| 4 | Approve | Designated approver | Documented approval decision |
| 5 | Enable and monitor | Platform team | Securely configured and monitored integration |

<a id="step-1-request"></a>

## Step 1 - Request

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

<a id="step-2-classify"></a>

## Step 2 - Classify

Determine how the MCP server is deployed and the risk associated with its intended use.

### Deployment model

| Type | Description |
|---|---|
| Local | Executed on the user's device |
| Internally hosted | Operated by the organization on shared infrastructure, including its own deployments on cloud services |
| Externally hosted | Operated remotely by a third party |

<a id="risk-level"></a>

### Proposed risk levels

| Risk | Criteria |
|---|---|
| Low | Public data or no data access, with read-only access where applicable and restricted execution |
| Medium | Non-sensitive internal data or limited write access, with restricted execution |
| High | Sensitive data, privileged access, broad write access, destructive operations or unrestricted execution |

Check what the execution identity and tools can actually access or change, including inherited credentials and data reachable through other tools. If the available information cannot establish the tier, use the highest plausible tier to plan the assessment. Security confirms the final tier during assessment. If evidence still cannot establish the tier, keep the request pending and access disabled while security seeks evidence.

Use the highest risk level that applies to the server’s **effective privileges**. For example, limited write access with restricted execution is medium risk. Access to sensitive data raises it to high risk.

**Outcome:** Deployment model and risk classification.

<a id="step-3-assess"></a>

## Step 3 - Assess

Follow [assessment execution](#1-assessment-execution) to collect static evidence before running artifacts you control and to prepare isolated, authorized tests.

Use [the domain verification methods](#3-security-signals-and-verification-methods) to automate checks where possible. Verify controls manually where automated evidence is insufficient.

Wiz reported that about 70% of the exposed MCP servers it studied returned their full tool catalog to anonymous callers. Verify that capability discovery and invocation each follow the approved caller policy. [Wiz Research](https://www.wiz.io/blog/the-risk-hiding-behind-exposed-mcp-servers)

| Assessment domain | Key question |
|---|---|
| **Identity and authentication** | Can we trust the server's identity and authentication mechanisms? |
| **Permissions and tool surface** | Does the server only have the access and functionality it needs? |
| **Provenance** | Can we trust where the server and its software originate from? |
| **Change control** | Can we detect, control and respond to changes? |


Send the [control results and evidence](#4-evaluate-and-record-evidence), proposed approval baseline and recommended safeguards to the designated approver.

**Outcome:** A completed security assessment with findings and recommended safeguards.

<a id="step-4-approve"></a>

## Step 4 - Approve

The designated approver checks the control results and N/A justifications. Record the decision, date, approver names, rationale and, for approvals, the approved baseline and any restrictions.

| Outcome | Meaning |
|---|---|
| Control: PASS | Requirement satisfied, supported by evidence |
| Control: FAIL | Requirement not satisfied |
| Control: UNKNOWN | Insufficient evidence |
| Control: N/A | Not applicable, with justification |
| Approval: Approved | Production requirements are satisfied without additional approval restrictions |
| Approval: Approved with restrictions | Production requirements are satisfied with additional, tested and enforceable safeguards |
| Approval: Rejected | Security risks are unacceptable or a mandatory control fails or lacks sufficient evidence |

<a id="approval-authority"></a>

### Proposed approval authority

| Risk level | Approver |
|---|---|
| Low | Platform team |
| Medium | Security team |
| High | Security team and relevant system or data owner, with escalation where required |

Approve for production only when every applicable [mandatory control](#mandatory-controls-for-production-approval) has passed. This also applies to approval with restrictions.

**Outcome:** A documented approval decision with any conditions.

<a id="step-5-enable-and-monitor"></a>

## Step 5 - Enable and monitor

Before enabling production access, the platform team verifies that the deployed configuration and restrictions match the documented approval. Keep access disabled if approval is missing or production checks fail. Refer deviations for reassessment and approval.

Before enablement, the platform team records which production events to monitor, who reviews them and when to investigate or escalate. Confirm that the reviewer receives a representative test event through the normal monitoring channel. Once the checks pass, the platform team registers or updates the integration in the approved MCP catalogue, enables access, then marks it active.

Monitor [configuration drift](#mcp-client-configuration-scanning), publisher or operator notifications and new security risks. Reassessment is required when there is a material change to:

- Software version or artifact.
- Client configuration, available tools, agent capabilities, permissions, accessible credentials or enforcement controls.
- Authentication mechanisms.
- Server operator or hosting environment.
- Intended use, content sources or data access.
- Known security risks.

Reassess planned material changes before enabling them. Revisit [classification](#step-2-classify) if deployment or risk inputs changed. Repeat the affected assessment checks and obtain [a new approval decision](#step-4-approve) before enabling changed or suspended access.

If an unexpected change invalidates a mandatory control or another approval condition, the platform team suspends affected access and updates the catalogue. Keep the affected access suspended until the new approval and release checks pass.

The designated approver may revoke approval at any time and records the decision and rationale with the approval record. The platform team disables the integration, removes its access and updates the catalogue status.

**Outcome:** A securely configured and continuously governed MCP integration.

---

<a id="enterprise-controls-that-put-the-principles-into-practice"></a>

## How to govern MCP servers

### Governing principles

| Principle | Requirement |
|---|---|
| **Default deny** | Allow only approved servers for organizational use. Permit pre-approval execution or connection only for [isolated, authorized assessment](#1-assessment-execution). |
| **Automation first** | Automate security verification wherever possible. |
| **Risk-based** | Assessment effort must be proportional to risk. |
| **Least privilege** | Only necessary permissions and capabilities are permitted. |
| **Verifiable trust** | Approval must be supported by evidence and bound to an identified artifact or remote integration. |
| **Continuous assurance** | Material changes require reassessment, and trust must be revocable. |

### Recommended controls

When an MCP client starts a local server with `npx`, it runs code from an npm package. Apply the same controls you use for other third-party packages and reuse the review evidence for that version.

MCP also lets a model choose which tools to call. Malicious instructions in one tool's description can steer the model into misusing a tool from another server. Review [the tools available to the model and their combined permissions](#permissions-and-tool-surface).

| Control | Recommendation |
|---|---|
| Package governance | Approved publishers and packages |
| Software distribution | Controlled internal artifact registry |
| Version management | Pinned versions and locked dependencies |
| Supply chain security | Verify package provenance and scan the package and its direct and transitive dependencies for vulnerabilities and malware. |
| Execution isolation | Run local servers in a restricted container, sandbox or VM. Without isolation, package code can read local credentials available to its process. |
| Network security | Restricted outbound connectivity |
| Identity | Dedicated, least-privileged credentials per server |
| MCP governance | Approved servers and tools |
| Change management | Review package and tool definition changes |

## Security assessment methodology

Adapt the proposed risk tiers, approval authorities and scanning matrix to your organization's governance. The four-domain structure is adapted from the [NHI MCP Server Trust Assessment Guide](https://nhimg.org/mcp-server-trust-assessment-guide), with endpoint and agent-context guidance from [Backslash Security](https://www.backslash.security/learning/how-to-evaluate-an-mcp-server-s-risk-before-employees-install-it).

<a id="3-assessment-execution"></a>

### 1. Assessment execution

**Before connecting or running code**, prepare an isolated test environment with restricted network access and synthetic data. Use dedicated least-privileged test credentials for authentication and mock secrets when testing credential isolation. Keep unapproved servers off employee workstations. Assess the configuration and policy intended for production in the test environment. Step 5 verifies the deployed configuration before release. Complete applicable static checks before running artifacts you control. Obtain authorization for any active testing, including testing of a third-party service.

| Order | Activity | Output |
|---|---|---|
| 1 | Identify the publisher, operator, package or endpoint. Identify the applicable [mandatory controls](#mandatory-controls-for-production-approval) and [select checks for the deployment model](#2-scanning-techniques-and-applicability). Record the intended client, execution identity, accessible credentials, other tools, untrusted content sources and runtime controls. | Assessment scope and selected checks |
| 2 | Obtain available artifacts without executing them. Use the [domain verification methods](#3-security-signals-and-verification-methods) to check provenance and scan code, dependencies, malware indicators and embedded secrets. | Static assessment evidence |

| Order | Activity | Output |
|---|---|---|
| 3 | Connect from the test environment. List the server's capabilities and identify its authentication requirements. | Capability and authentication inventory |
| 4 | Inspect tool definitions, resources, prompts and sample responses. Treat server content as untrusted, including during AI-assisted scanning. Check who controls that content and what the agent can do with its other tools. | Findings on server content and combined tool access |
| 5 | Test authentication, permissions, credential isolation, runtime behavior and proposed restrictions within the authorized scope. For untrusted input, scale indirect prompt injection testing to the assessed risk. Keep destructive tests off production systems. | Test results and evidence of enforcement |
| 6 | Record artifact and dependency identities, client and endpoint settings, permissions, capability fingerprints and required runtime restrictions. | Proposed approval baseline |
| 7 | [Record the evidence](#4-evaluate-and-record-evidence), identify unresolved controls and specify any safeguards needed for approval. | Completed assessment and recommendation |

#### Mandatory controls for production approval

For any additional mandatory control, the security team records when it applies and what evidence counts as a pass before testing.

| Mandatory control | Applies to | Pass condition |
|---|---|---|
| Server identity and connection security | All integrations | Verify the publisher or operator and record the reviewed artifact or endpoint in the proposed baseline. For executable artifacts under organizational control, verify the identities and integrity of the artifact and resolved executable dependencies using digests or other integrity evidence. For network connections, verify endpoint identity and encrypted transport. Verify that only approved callers can discover capabilities or invoke operations. Allow anonymous access only where explicitly approved. For local process connections, verify who controls the launch configuration, which account runs the server and which credentials it inherits. |
| Access limits | All integrations | Record the permitted system and network access. Test that the configuration intended for production enforces those limits for the execution identity, including filesystem access and outbound connectivity. For externally hosted servers, test the client-side restrictions and obtain evidence from the operator for boundaries it controls. |
| Permitted data use | Integrations that access or transmit data | Record the applicable data-handling rule and evidence that it permits the intended use and recipients. Resolve unclear cases with the data owner before approval. |
| Token handling | Servers accepting MCP OAuth access tokens | Verify that the server rejects invalid tokens, including those from untrusted issuers, expired tokens and tokens issued for another audience. It checks sufficient scope for the requested operation. If the server calls a downstream API, it uses a credential issued for that API and never forwards the inbound MCP access token. |
| Enforcement of restrictions | All integrations | Test that the intended production policy permits only approved servers and configurations, and enforces each integration restriction, such as denying a write under read-only access. Where the agent reads untrusted content, use representative input to confirm that an out-of-scope action stays blocked and any required human approval still applies. |
| Human approval for sensitive actions | Tool actions that policy requires a person to approve | In a test, the action has no effect while approval is pending or after it is denied. It proceeds only when an authorized person approves that specific action. |
| Action traceability | All integrations | Using the logging configuration intended for production, the reviewer traces a representative test action from the initiating user or accountable workload owner through the operation requested, authorization decision and outcome. |
| Resource limits and secure failure | All integrations | One test shows that a configured resource limit stops or rejects excess work. If an operation requires authorization, test that it has no effect when authorization is denied or the check cannot complete. |
| Revocation | All integrations | A test confirms that the platform team can disable the integration and cut off its access. |

### 2. Scanning techniques and applicability

- **Required** means collect evidence for this area.
- **As applicable** means perform the check when the feature or control is in scope.
- **If available** means use the source, artifact or other material if you can obtain it.
- **Risk-based** means choose the depth of testing based on exposure, effective privileges and potential impact. Record your rationale.

If evidence is missing for an applicable control, record UNKNOWN and assess alternative evidence or enforceable safeguards. Use N/A only when the control does not apply, and record why.

| Technique | Local or internally hosted | Externally hosted |
|---|---|---|
| Provenance and identity verification | Required | Required |
| Dependency inventory and vulnerability scanning | Required | If available |
| Static code analysis (SAST) | Required | If available |
| Static malware indicator scanning | Required | If available |
| Secret scanning | Required | If available |
| MCP-specific scanning and capability discovery | Required | Required |
| Connection security and caller access | Required for the configured transport | Required for the configured transport |
| Ambient credential and execution identity analysis | Required | Required for client/agent; operator evidence for server |
| Untrusted content and cross-tool exposure analysis | Required | Required |
| Indirect prompt injection testing | Required for untrusted input, with risk-based depth | Required for untrusted input, with risk-based depth |
| Runtime behavioral analysis | Required | Required for observable behavior |
| Third-party operator security assessment | As applicable | Required |
| Update mechanism analysis | Required | Operator evidence and inspection of observable changes |
| MCP client configuration scanning | Required | Required |
| Change baseline and runtime enforcement verification | Required | Required |
| Action traceability | Required | Required |

For externally hosted servers, check whether available audit reports, security test summaries or operator documentation cover the service, period and controls under review. Tests from outside the service can establish only what you observe.

Reuse enterprise tools where possible. Maintain tool versions and configurations separately. Check how a scanner handles data before sending code, tool metadata or responses to an external service.

#### MCP client configuration scanning

Inspect user, workspace and centrally managed configurations, including startup executables and arguments, package versions or digests, remote URLs, credential references and inherited environment settings. Verify policy precedence and whether user or repository configuration can bypass the approved configuration. Do not collect raw credential values.

During assessment, inspect the proposed configuration. To detect configuration drift, repeat discovery and compare settings with the approval baseline. Verify enforcement separately at the relevant client, endpoint or gateway.

<a id="1-security-signals-and-verification-methods"></a>

### 3. Security signals and verification methods

Collect the applicable signals in each of the four assessment domains. Use deterministic tests where possible, heuristic scanning to identify suspicious behavior, and manual review where technical evidence is insufficient.

Automation: **Automatable** means machine-checkable; **Partial** means automated evidence still needs human review; **Manual** means document or judgment review.

#### Identity and authentication

| Signal to collect | Verification method | Automation |
|---|---|---|
| Server identity, URL, domain and operator | Verify publisher affiliation, endpoint identity and TLS where applicable | Partial |
| Authentication mechanism and OAuth metadata | Protocol discovery, configuration review and metadata validation | Partial |
| Token audience, issuer and expiration | Use test credentials to confirm that valid tokens work and tokens with the wrong audience, an untrusted issuer or an expired lifetime are rejected | Partial |
| Requested and granted scopes | Compare the scopes requested and granted during authorization with the permissions the use case requires | Partial |
| Credential handling and inherited environment variables | Source-code and configuration scanning; sandbox inspection | Partial |
| Effective execution identity and ambient credentials (SSH keys, Git, cloud and package registry credentials) | Inspect process identity, inherited privileges and accessible credential stores; test isolation using synthetic credentials | Partial |
| Token passthrough and downstream credentials | Trace credential use and verify that downstream API calls use credentials intended for that API | Partial |
| Shared or long-lived credentials | Configuration and documentation review | Partial |

**Investigate:** Invalid credentials being accepted, insecure token handling, token passthrough, unnecessarily privileged credentials and access to unrelated credentials.

#### Permissions and tool surface

| Signal to collect | Verification method | Automation |
|---|---|---|
| Available tools, resources and prompts | List capabilities for each relevant identity and follow pagination until the inventory is complete | Automatable |
| Tool names, descriptions, schemas and annotations | MCP-specific scanning and baseline comparison | Automatable |
| Read, write, delete and administrative capabilities | Semantic classification, source analysis and controlled testing | Partial |
| Prompt injection and tool poisoning indicators | Signature-based and AI-assisted analysis of metadata and representative responses | Partial |
| Exposure to untrusted content and indirect prompt injection | Identify who can control retrieved content; perform risk-based adversarial tests with synthetic content in the intended client or agent | Partial |
| Cross-tool attack potential | Review the combined permissions of available tools. Check with representative synthetic inputs that out-of-scope actions stay blocked. | Partial |
| Effective permissions to underlying systems | Inspect the granted permissions and test whether the identity can access systems or actions outside the business need | Partial |
| Filesystem access, network destinations and child processes | Inspect the code and observe which files, network destinations and child processes the server accesses in the sandbox | Partial |
| Telemetry, external data recipients and sensitive data disclosure | Use data-flow analysis, source inspection, controlled network monitoring or available operator documentation as applicable | Partial |
| Hidden functionality and input validation | Source analysis and authorized negative testing | Partial |
| Tool naming collisions | Verify that the client or gateway distinguishes tools with the same name across approved servers | Automatable |

**Investigate:** Excessive privileges, model-directed malicious instructions, arbitrary command execution, unexpected data destinations, disclosure of sensitive data, unsafe combinations of tools and discrepancies between declared and observed behavior. Tool annotations are not proof of actual behavior.

#### Provenance and supply chain

| Signal to collect | Verification method | Automation |
|---|---|---|
| Publisher, maintainer and vendor affiliation | Check that the registry and repository identify the publisher named in official vendor documentation | Partial |
| Relationship between repository and distributed artifact | Build provenance and attestation verification where available | Partial |
| Package version and artifact digest pinning | Compare the version and digest with independently approved values | Automatable |
| Signatures and attestations | Verify signatures, trusted signer identity and artifact binding | Automatable |
| Direct and transitive dependencies | SBOM generation and software composition analysis (SCA) | Automatable |
| Known vulnerabilities and malware | Vulnerability databases, malware signatures and threat intelligence | Automatable |
| Suspicious code, obfuscation, installation scripts and dynamic downloads | Static code analysis, malware scanning and AI-assisted review | Partial |
| Embedded credentials | Secret scanning | Automatable |
| Maintenance, publisher and release history | Review package age, release activity, maintainer and ownership changes, and changes in signing identity where historical evidence is available | Partial |
| Package impersonation and typosquatting | Compare names and publisher namespaces against official vendor and registry information | Partial |
| Externally hosted service security | Operator documentation and security assessment | Manual |

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
| Ability to disable the integration and revoke access | Disable the test integration and verify that its managed access path no longer reaches the target system. If the integration has credentials, revoke them and verify they no longer work | Partial |
| Audit logging and action traceability | Correlate a test request with its authorization and execution records. For unattended actions, use the workload identity to look up its accountable owner. Exclude secrets and unnecessary sensitive payloads. | Partial |
| Third-party operator change notification | Check available operator documentation and agreements for which changes are reported and how notice is delivered | Manual |

**Investigate:** Unapproved changes, mutable execution dependencies, uncontrolled upgrades, unauthorized client configurations, bypassable policies, missing audit evidence and inability to revoke access. Remote capability fingerprints detect observable interface changes, not changes to hidden backend behavior.

### 4. Evaluate and record evidence

The security team records a result for every mandatory control and each additional control selected for assessment, including a reason for each N/A. Use these fields for the controls that apply.

| Field | Example |
|---|---|
| Domain / control | Provenance / artifact integrity |
| Signal | SHA-256 digest of executable artifact |
| Verification method | Compare with independently established pinned digest |
| Expected result | Digests match |
| Observed result | Digests match (illustrative) |
| Status | PASS |
| Evidence | Artifact verification report |
| Assessment context | Date, assessor, target identity, scanner version, configuration and test scope |

Use the [control results defined in Step 4](#step-4-approve). A clean scan means no findings were detected within its scope; it does not independently prove the absence of vulnerabilities or malicious behavior. Heuristic or AI-generated findings require appropriate validation before a decision. Failed or unknown mandatory controls block production approval as defined in Step 4.

Retain evidence with the approval record. Protect sensitive information and exclude raw credentials from stored reports. After a reassessment, retain the updated evidence with the new decision.

---

## Supporting documentation

Maintain four components initially:

| Component | Purpose | Audience |
|---|---|---|
| MCP Governance and Assessment Process | The five-step process above (target: 1–2 pages) | Everyone |
| MCP Request Form | The seven questions the requester must answer (target: 5 minutes) | Requesters |
| MCP Security Assessment Checklist | Detailed security controls, verification methods, automated scan results, evidence and approval decision | Security and platform teams |
| Approved MCP Catalogue | Searchable register of approved servers, configurations, restrictions and owners | Everyone |
