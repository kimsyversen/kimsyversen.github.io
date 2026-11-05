# GitHub two-enterprise reference architecture

Reference design, checked against GitHub documentation on 4 November 2026. All organization and system names are illustrative. No live enterprise settings were changed.

## Files

Open `github-two-enterprise-reference.drawio` in diagrams.net / draw.io. It contains three editable pages:

1. Architecture: Gate 0 hosting decision, then seven rows per enterprise (people and devices, identity, enterprise policies, organizations, repositories, execution, evidence). The centre channel holds the logical boundary, the approved transfer service (export A to B in red, intake B to A in green) and the common SOC view.
2. Policy layers: a matrix of enterprise, organization and repository layers for A and B, with accountable owners, 14 controls per cell, and an implementation gate of negative tests.
3. Operations: build and deploy paths (A, B untrusted, B release), monitoring per domain, incident response, controlled transfer lanes, platform operations and accountability.

`github-two-enterprise-reference-compact.drawio` is a second version with everything on one page. Each enterprise is drawn as a top-to-bottom stack (identity, enterprise policy, organizations with repositories, execution, evidence), with the transfer service and common SOC view in the centre and the operations material in a band below. It is a condensed view of the same design, so use the three-page file for the full policy matrix and implementation gate.

`github-two-enterprise-interactive.html` is a single-page interactive version of the same diagram, styled like `AKS-sikkerhetsvurdering.html`. Click a box for what it does and how to check it, and use the filters to follow a flow, a policy layer or a type of control. It needs no server, and a link like `#n=A.p8` or `#f=fl:export` opens a box or a filter directly.

Tags: G is a GitHub control. X is an external service, automation or organizational process. G+X means both are needed. These are target controls, not a claim that one policy switch implements each line.

Export to SVG or PNG from draw.io (File > Export as) when needed. No exports are stored here.

## 1. Hosting and classification decision

The reference assumes GitHub Enterprise Cloud for both enterprises, with the sensitive service deployment subject to approval by the organization's security authority. The actual classification, national requirements, service accreditation and jurisdiction have not been specified. Therefore this drawing does not assert that classified critical-system source or IaC is permitted on GitHub Enterprise Cloud.

Obtain approval for the specific service, hosting region, administrators/support access, identity platform, runners, security scanners, logs, backups and other integrations before loading classified content. A residency selection is not an accreditation decision. If the service is unsuitable, replace the sensitive hosting design with an accredited solution, potentially an assessed self-hosted platform. GitHub Enterprise Server identity and operational capabilities must then be designed separately; the Cloud EMU design cannot simply be relabeled as Server.

The two enterprises are separate identity and governance domains within a SaaS service. They are not an air gap or independent physical security enclaves. Organizations and private repositories provide access partitions, but privileged administrators and broadly scoped integrations can cross them. Different classification compartments may require additional enterprise or hosting separation after threat assessment.

## 2. Identity design and the SAML / SCIM tradeoff

### Enterprise A: sensitive, Enterprise Managed Users

Use a dedicated IdP application with SAML SSO and enterprise SCIM provisioning. The IdP owns account lifecycle. Scope assignments to authorized personnel and map approved groups to teams. Managed accounts cannot collaborate outside their enterprise or create public repositories. Restrict organization-owned repositories to private visibility, disable user-owned repository creation, and restrict private forking in this target baseline. [EMU setup](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/getting-started-with-enterprise-managed-users), [managed-account restrictions](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/abilities-and-restrictions-of-managed-user-accounts).

Apply phishing-resistant MFA and device controls at the IdP and endpoint layer. This design chooses SAML. GitHub's specific Entra Conditional Access integration uses OIDC and must be evaluated separately if selected. Keep limited named enterprise owners, protected emergency recovery access and tested IdP-outage procedures. Review privileged changes and recovery credential use independently.

### Enterprise B: personal accounts, organization SAML and SCIM

Users retain their personal GitHub accounts, linked to corporate SAML identities. They are not converted into enterprise-owned user accounts. Configure and enforce a separate SAML plus SCIM integration in each organization. SCIM manages organization membership only, and the personal GitHub account stays user-owned. [Enterprise type choices](https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/choose-an-enterprise-type), [organization SCIM](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/about-scim-for-organizations).

GitHub does not support SCIM for a personal-account enterprise itself. Switching to enterprise-level SAML removes organization SCIM functionality. The alternative is enterprise SAML plus independently implemented membership/offboarding automation, which is outside the selected baseline. [SAML scope decision](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/deciding-whether-to-configure-saml-for-your-enterprise-or-your-organizations), [switching SAML scope](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/switching-your-saml-configuration-from-an-organization-to-an-enterprise-account).

Use private visibility for internal work in this design. GitHub's visibility named `internal` grants broad enterprise-member read access, and organization-level SAML does not protect access to internal repositories in the same way as enterprise SAML. Private repositories plus explicit grants avoid relying on this combination. This deliberately distinguishes the business classification "internal" from the GitHub visibility value `internal`. [Internal visibility](https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-best-practices/use-innersource), [SAML scope decision](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/deciding-whether-to-configure-saml-for-your-enterprise-or-your-organizations).

SCIM does not replace access governance. Test removal from every organization, privilege removal, and revocation of credentials or access paths that are not ordinary membership: outside collaborators, deploy keys, app installations, webhooks and cloud identities. External contributors can still interact with public repositories without corporate SSO; public resources are public. Give personal-account collaborators only approved repository access, with separate expiry and review procedures.

Personnel who use both enterprises use two GitHub identities and separated work environments. A separate browser profile alone does not prevent copying data. Use managed workstations or isolated sessions, distinct credential stores and controlled network egress.

## 3. Policy enforcement model

The policy page assigns the enforcement scope and owner. Keep enterprise baselines active and targeted to all repositories in scope. Use organization controls to specialize access, runners and integrations. Repository owners supply CODEOWNERS, meaningful checks and system-specific deployment controls.

Use enterprise repository policies for controlled repository lifecycle and public creation limited to the publishing organization. Restrict visibility changes and transfers so a user cannot move internal source into a publishing path without review. Use enterprise rulesets for branch/tag protections and no bypass by default and, if an emergency bypass is unavoidable, a short named list with every use reviewed (the Learn Governance page says rulesets should not allow bypass, so this is a deliberate narrow exception); apply additional organization/repository rules where needed. [Repository governance policies](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-repositories-in-your-enterprise/governing-how-people-use-repositories-in-your-enterprise), [enterprise rulesets](https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-governance).

For sensitive repositories, require at least two PR approvals including an appropriate code-owner review, dismiss stale approvals, require approval of the latest push, and protect security workflow and IaC ownership files. The two approvals are an organizational target, not a GitHub default. CODEOWNERS by itself does not enforce reviews; the ruleset must require them. Required check names must correspond to trustworthy jobs or integrations. Signing commits proves identity binding, not correctness of the code.

Enforce security configurations and ensure new repositories receive the baseline. Budget for GitHub Code Security and Secret Protection for private repositories, or approved equivalents. IaC scanning, IaC policy checks and release approval require selected tools/workflows and process; enabling code scanning alone is insufficient. Validate data handling for scanner uploads and alerts. [Enterprise security configurations](https://docs.github.com/en/enterprise-cloud@latest/code-security/how-tos/secure-at-scale/configure-enterprise-security/establish-complete-coverage/create-custom-configuration).

Prefer narrowly scoped GitHub Apps over long-lived personal credentials for integrations. Restrict classic PATs, constrain fine-grained token lifetime and approve their repository scope. Review OAuth apps, GitHub Apps and their webhook destinations. Keep app keys and installation identities separate between A and B. [Programmatic access controls](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization).

Disable unapproved AI, Codespaces, Pages and other optional data-processing or publishing features in the sensitive baseline. Introduce each only after a service-specific review. Not every target is a single enterprise policy: enforce supporting restrictions with organization settings, endpoint/network controls and drift checks.

## 4. Execution and cross-domain movement

Use isolated ephemeral runners for sensitive jobs. Divide runner pools by system/trust level, limit allowed repositories and workflows, restrict repository-level runner creation, remove residual disks/caches, patch images, monitor runners and constrain network access. A disposable runner still needs network isolation and minimal credentials.

Run untrusted public pull requests on separate unprivileged workers, normally GitHub-hosted runners, without deployment secrets or routes into internal networks. Avoid privileged workflow patterns that execute contributor-controlled code, including unsafe use of `pull_request_target`. Pin approved Actions and reusable workflows to immutable commits; use minimal job token permissions. [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use), [runner group access](https://docs.github.com/en/enterprise-cloud@latest/actions/how-tos/manage-runners/self-hosted-runners/manage-access).

Use short-lived OIDC deployment identity with trust scoped to the exact enterprise/domain, repository and approved environment. Where both enterprises use GitHub.com, the default issuer is the same for both. Turn on the per-enterprise issuer (`include_enterprise_slug`, set by an enterprise admin through the REST API) and match the `enterprise` or `enterprise_id` claim in the trust policy. Each target must reject identities from the other domain. [OIDC reference](https://docs.github.com/en/enterprise-cloud@latest/actions/reference/security/oidc). Keep state files, plans containing secrets, production credentials and signing keys out of Git. Store IaC state encrypted in the approved backend with locking and access controls.

The transfer box is an external approved process or service, not a built-in GitHub security boundary. Outbound transfer requires the release authority to decide that content can leave its classification domain. Inspect history, topology, secrets, metadata, packages and logs; scanning alone cannot declassify information. If transfers are prohibited, remove this path entirely.

Use mediated staging and domain-local credentials rather than a bot with broad read/write access to both enterprises. Imports require origin verification, quarantine, malware/license review, scanning, pinned dependency versions and admission to an approved mirror. Do not automatically mirror sensitive repositories into B.

For GitHub.com EMU, consider enterprise access restrictions through a mandatory corporate proxy plus network allow lists. Block or control unsupported bypass paths, including Git SSH; review alternative upload endpoints and anonymous access. IP allow lists control inbound access to protected GitHub resources, not all outbound data leakage. Their coverage has documented exclusions. [Enterprise proxy restriction](https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/hardening-security-for-your-enterprise/restricting-access-to-githubcom-using-a-corporate-proxy), [IP allow lists](https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/hardening-security-for-your-enterprise/restricting-network-traffic-to-your-enterprise-with-an-ip-allow-list).

## 5. Monitoring and shared capabilities

Stream audit and Git events from each enterprise to its domain's protected archive and SIEM. Enable security-relevant API request events and source IP disclosure, understanding that neither covers every operation. Add security alerts via supported APIs/webhooks, IdP and privileged access logs, endpoint/proxy/DLP evidence, runner telemetry, registry events and cloud control-plane logs. Protect webhook receivers with signature validation and replay/duplicate handling.

Monitor ingestion latency and stream health, reconcile expected sources, and deduplicate events. Select retention based on investigation needs and applicable rules; do not rely on GitHub's short native Git-event retention. Security alerts and audit logs are complementary feeds. [Enterprise audit coverage](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/accessing-the-audit-log-for-your-enterprise), [audit streaming](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise).

Do not claim complete observation of a personal account's GitHub sign-in or its activity outside organizational resources. Source IP coverage also has gaps for public-resource activity and some API/app events. Correlate with endpoint and network evidence. Clone/download detection will not capture every local copy or anonymous public download. [Source IP and personal-account limitations](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/displaying-ip-addresses-in-the-audit-log-for-your-enterprise).

A common SOC can share procedures and approved summaries. Detailed sensitive logs can expose repository names, identities, paths and critical-system metadata, so they remain in the sensitive zone. Even sanitized alert sharing needs classification approval.

Common standards include inventory, policy drift detection, vulnerability remediation SLAs and pen tests, threat modeling per system, training and security champions, compliance audits, access recertification, exception expiry, business continuity, backup/restore tests, support escalation and incident exercises. Deploy them independently per domain. Backups must cover required repository metadata, LFS, packages and settings as well as Git history; verify tool coverage and restore semantics. Set explicit RPO/RTO targets with the system owner.

## 6. Acceptance checks before onboarding

- Approve classification, service, region, support access and all connected data processors.
- Test a representative new repository in each organization for baseline coverage, lifecycle restrictions, visibility controls and absence of unintended access.
- Verify IdP suspension and SCIM deprovisioning end to end, including privileged and exceptional access paths.
- Exercise branch/tag protections, code-owner reviews, bypass alerts, security check enforcement and deployment approvals with negative tests.
- Confirm that public PR code cannot obtain deployment credentials or reach internal/sensitive runners, registries or targets.
- Verify that an OIDC identity from B cannot deploy to A, and that a sensitive workstation cannot upload through an unapproved GitHub account or app.
- Trigger test audit/security events and a collector failure; verify detection, correlation, retention and domain separation.
- Restore repositories and required metadata, exercise emergency recovery access, and validate the approved transfer process or demonstrate that it is blocked.

Open decisions: actual classification and accreditation, jurisdiction/residency, IdP and tenant separation, permissible cross-domain transfers, number of sensitive compartments, scanner and AI service approval, retention, recovery targets and product entitlements.

## 7. QA against the five Well-Architected pillars

QA done on 4 November 2026 against learn.github.com/well-architected, all five pillars. Checked: the three-page drawing, the one-page drawing, the interactive page and these notes. Method: read the pillar pages, compare each recommendation with the design, fix real gaps in all artifacts, and record what was not read. Findings are comparisons of the design with the documentation. None were tested on a real GitHub tenant.

Tags used on the drawings: G is a GitHub control, X is an external control or process, G+X needs both.

### What was read, and what was not

For every pillar I read the overview, design principles, checklist and recommendations overview, then the recommendation articles that touch this design.

- **Read in full or in large part:** Governance principles, "Essentials of governance and administration", Governing agents, Mirroring, Resilient CI/CD, Effective CI, Champion program, the Application Security checklist and its main recommendation articles, the Productivity checklist.
- **Opened and searched on 4 November 2026, after the first QA:** the ARC runner article, Private networking, the polyrepo article, Managing AI credits, Threat model, Enforce GHAS at scale and the Scaling Git overview. Each page's full text was searched for the claims this design makes about it. Where a claim is ours, the notes say so.
- **Read in full, 4 November 2026:** the enterprise custom agents context article, the three Scaling Git sub-articles (repository architecture strategy, large repositories, when to use LFS), and the Governance articles on agentic workflows, agentic engineering, the taxonomy, shared knowledge, repository management at scale and policy best practices. Nothing on them contradicts a design statement. The policy best practices and taxonomy pages support the baseline: rulesets, CODEOWNERS, signed commits, audit streaming, bypass limits, read-only default workflow token, no auto-approval of pull requests by Actions, security configurations and custom properties. Two points are worth knowing. The custom agents article prefers fine-grained tokens but falls back to a classic `repo` token, which clashes with A's classic-token block; A has agents off and the design does not cite that article. The agentic workflows article says organization-level runner group enforcement and ARC with Docker-in-Docker are not yet fully available, and the design makes no claim about either. No design statement cites the other pages.

### Per pillar

**Governance (main pillar).** Confirmed on the Learn Governance pages (read 4 November 2026): enterprise-level SAML is recommended for most deployments, organization SCIM is the non-EMU option, a sandbox organization is one of the listed models, repository rulesets are recommended, push-protection bypass should be limited to specific roles and teams, and a runner group for all repositories is called a risk. Not found on those pages and so this design's own choices: enterprise as a separate control plane, custom properties, enterprise teams from IdP groups, streaming with source IP, organizations by need-to-know, open source in its own org. Gaps found and fixed:
- No role model beyond owners. Added a security manager role, delegated custom roles and no default Admin.
- No AI governance in the enterprise layer. Added "agents off until approved" in A and "agents per org, pilot first" in B.
- Git events are kept by GitHub for only 7 days. The notes and page now say the stream must run from day one.
- Rulesets had no rollout step. New or changed rules now run in Evaluate mode first, and bypass requests are recorded and reviewed.
- Shared workflows had no owner. Added a shared workflow platform org with versioned, code-owner-protected workflows. A and B never share workflows, each has its own copy.

**Application Security.** Confirmed on the Learn Application Security pages (read 4 November 2026): lifecycle scripts off by default, lockfiles, OIDC trusted publishing, validating package attestations, OIDC for Actions with granular claims, job-level permissions, pinning actions to a commit hash, avoiding `pull_request_target`, delegated bypass for push protection. A threat model has its own Learn page. Dependency review as a required check, code scanning and security campaigns with deadlines were not re-confirmed on Learn; campaigns exist in the GitHub docs, and the deadlines are this design's choice. Signed releases, SBOM, SECURITY.md and vulnerability SLAs are in the design but I did not find them on the Application Security pages, so they are this design's own choices, not framework alignment. Gaps found and fixed:
- Dependency and provenance controls were scattered. Added one explicit control: required dependency review, lockfiles, lifecycle scripts off, provenance verified before deploy (A) or trusted publishing with OIDC where the registry supports it, such as npm and PyPI (B).
- Agent instruction and MCP files were not covered. Added: code-owner review for them, and agent PRs pass the same gates as human PRs.
- Push-protection bypass is now limited to named roles or teams. Severity deadlines and security campaigns were added.

**Architecture.** Confirmed on the Learn Architecture pages (read 4 November 2026): private network access for GitHub-hosted larger runners (static IPs, an API gateway with OIDC, or Azure private networking), a separate authentication path for CI/CD recovery, and a page on repository mirroring. Not found there: separate enterprises as failure domains and runner groups per system, which are this design's own choices. The IP allow list and Conditional Access option is not a Learn claim. It comes from the GitHub docs: with EMU, Entra ID and OIDC, GitHub can use the IdP's Conditional Access policy instead of its own IP allow list. Gaps found and fixed:
- No rehearsed continuity path. Added a continuity mirror in a separate failure domain, portable deploy logic, an alternate identity path without Actions, drills with the primary blocked, and short-lived break-glass credentials.
- Runner choice was unstated. A now says self-hosted ephemeral runners, or hosted larger runners with Azure private networking, as the accreditation decides. Agents run on ephemeral runners with a firewall.
- Jobs now ask for extra token permissions by name, and GitHub Actions approving pull requests stays off (the default for new organizations).

**Collaboration.** Not re-confirmed on Learn: CODEOWNERS and required reviews, a champions program and training. The Governance page says rulesets should not allow bypass, and this design allows only a short named emergency list, so that differs. Gaps found and fixed: champions and a developer feedback channel are now named controls, and a new ops item covers onboarding, a knowledge base and Discussions, with separate copies in A and B. Not covered: inner source practice, issue and project conventions, a Projects-based status view. These stay with the platform team.

**Productivity.** Mostly out of scope for a security architecture. Gap fixed: CI duration, queue time, flake rate, alert age and time to fix are now listed as metrics, with a friction and exception channel, so security controls do not silently slow teams. Not covered: DORA wording, caching, path filters, required workflows, a tiered ruleset-by-property scheme, and the polyrepo integration-repo pattern. These are guidance for repo owners. The design makes no repo-count claim, so they were not added.

### Deliberate deviations

1. **Per-org SAML and SCIM in Enterprise B, not enterprise-level SAML.** The Governance guidance names organization SCIM as the option outside EMU, and the GitHub docs say SCIM provisioning is not supported with enterprise-level SAML. The same guidance recommends enterprise-level SAML for most enterprises, which is why this is listed as a deviation. B uses personal accounts, so per-org SAML and SCIM is the only way to keep provisioning. The cost is one configuration per org, which is why reconciliation is a drawn control.
2. **No sandbox organization in Enterprise A.** The Learn Governance page lists a red, green, sandbox and archive model. A holds classified source and IaC, so experiments run in B with no classified data. B has a private-only sandbox-lab that is archived when unused.
3. **Private visibility instead of GitHub `internal`.** Kept from section 2. Internal work uses private repositories with explicit team grants.
4. **Self-hosted or private-network runners, not plain GitHub-hosted runners.** The Productivity checklist says to use GitHub-hosted runners. A and B use ephemeral self-hosted runners, or hosted larger runners with Azure private networking, so jobs can reach private targets and the accreditation can name the choice. Untrusted public PRs in B still run on hosted runners.

### Statement verification pass (4 November 2026)

Method: each statement about a GitHub feature was checked by fetching the GitHub documentation page and searching its full text for the claim. Learn pages were loaded in a browser and their full text was searched for each claim, then the matching passage was read. This is a targeted check of every claim the files make, not a line by line read of every paragraph of every page. The three drawio files and the interactive page were checked by listing all their text and checking each factual statement against the same sources. Statements that are design choices (owners, drills, two-person change process, SLAs, SOC process) are this design's own and are not claims about GitHub.

**Found wrong or imprecise, and fixed in all files:**

- The OIDC issuer is not the same for A and B. An enterprise-level issuer exists and the token carries an enterprise claim, so a trust policy can tell them apart (section 4, A.e2).
- The Governance guidance did not say enterprise SAML removes SCIM. That comes from the GitHub docs (deviation 1).
- Security configurations are not targeted by custom property in the docs I read. Enterprise rulesets and repository policies are (A.p9, B.p9).
- A claim that only named roles can create organizations in B had no support in the docs. What is documented is that enterprise owners add organizations to the enterprise. The claim was removed from the page and the drawings, and B.p1 now states only the documented part.
- SHA pinning does not cover reusable workflows, which can still be referenced by tag (A.p5, B.p5).
- Agent features are not cloud-only. Most need Enterprise Cloud, and some exist on Enterprise Server (A.p13, Limits).
- The push-protection bypass "needs a reason" is not in the delegated bypass pages. Removed. Bypass by named roles or teams is documented.
- "About ten controls per cell" on the policy page was 14.

**Checked and true:** enterprise teams syncing from IdP groups (EMU only, 1,000 organizations per team), user-owned repo and private-fork policies, default read-only GITHUB_TOKEN and Actions not approving pull requests by default, audit and Git streaming, API request events, source IP display, `agent_session_id`, third-party agents needing to be enabled, budgets that can stop metered usage, Azure private networking for hosted runners, artifact attestations, internal visibility with organization-level SAML, delegated bypass, security campaigns, free features for public repos, `pull_request_target` guidance, webhook signature validation, custom repository roles and the security manager role.

**Also checked and true:** runner groups limited to repositories and workflows, an enterprise setting that disables repository-level runner creation, Dependabot version updates for GitHub Actions, and the dependency review action blocking merges when required.

**Learn pages, re-read 4 November 2026:** Governing agents, Governance essentials, Mirroring, Resilient CI/CD, Effective CI, Champion program, the Application Security and Productivity checklists, and the Application Security articles on dependency threats, Actions security, prioritizing alerts, GHAS at scale, threat model and design principles. Each claim in section 7 was compared with the page text. Two were not supported and are fixed above: the Application Security alignment list (SBOM, SECURITY.md, signed releases, vulnerability SLAs are not on those pages) and the "accountability panel" and "admin-only" wording. The 7-day Git event retention is in the audit log docs. Trusted publishing is confirmed for npm (GitHub-hosted runners only, provenance added automatically) and PyPI, and the Learn page on dependency threats recommends it (B.p15).

**Drawio text, checked 4 November 2026:** all text in the three-page and one-page drawings was listed and compared with the page. New facts found only there and now checked: GHE.com uses Enterprise Managed Users, enterprise policy can block classic tokens and set maximum token lifetime, environments have a Prevent self-review option, rulesets have Require signed commits and Require approval of the most recent reviewable push, email notifications can be restricted to verified or approved domains. The ARC page does not use the word ephemeral. Ephemeral runners come from the Governing agents page and the design principles, and the per-system pool follows the ARC page's point that separate clusters are separate security boundaries.

**Evidence per drawio and page claim.** Docs pages were fetched on 4 November 2026 with a script that strips the page to its main text and searches it. Paths are under `docs.github.com/en/enterprise-cloud@latest/`.

| Claim in the drawings or page | Page | What the page says |
|---|---|---|
| IdP groups sync to enterprise teams, EMU only | `admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/create-enterprise-teams` | Lists "Syncing with an IdP group (Enterprise Managed Users only)" as a way to add users. |
| Enterprise teams give different capabilities with EMU than with personal accounts | `admin/concepts/enterprise-fundamentals/teams-in-an-enterprise` | Says the feature depends on whether you use EMU or personal accounts. |
| SCIM per organization exists outside EMU | `organizations/managing-saml-single-sign-on-for-your-organization/about-scim-for-organizations` | Describes SCIM for organizations. |
| Enterprise SAML drops org SCIM | `admin/managing-iam/using-saml-for-enterprise-iam/deciding-whether-to-configure-saml-for-your-enterprise-or-your-organizations` | SCIM is not supported with enterprise SAML on personal accounts (read earlier in this pass). |
| Audit stream, source IP | `admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise`, `.../displaying-ip-addresses-in-the-audit-log-for-your-enterprise` | Streaming audit and Git events to an external system; source IP can be displayed. |
| Custom properties target rulesets and repository policies | `admin/managing-accounts-and-repositories/managing-repositories-in-your-enterprise/managing-custom-properties-for-repositories-in-your-enterprise` | Governance by creating a ruleset or repository policy that targets repositories with certain properties. |
| Rulesets can require signed commits | `repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets` | "Require signed commits" rule exists. |
| Enterprise policy for classic and fine-grained tokens | `admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise` | Restrictions are set for classic and fine-grained tokens independently. |
| Limit repo create, delete, transfer, forking, outside collaborators | `admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise` | Enterprise policies for repository creation, deletion and transfer, forking and outside collaborators. |
| Push protection bypass by named roles or teams | `code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection` | Delegated bypass describes who may bypass. |
| Enterprise owners add organizations | `admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/adding-organizations-to-your-enterprise` | Page is addressed to enterprise owners and lists three ways to add organizations. It does not say members are blocked from creating organizations on their own. |
| Hosted runners with Azure private networking | `organizations/managing-organization-settings/configuring-private-networking-for-github-hosted-runners-in-your-organization` | Describes using GitHub-hosted runners with an Azure private network. |
| OIDC claims, enterprise level | `actions/reference/security/oidc` | Describes the token claims, including enterprise-related ones. |
| Self-hosted runners only for private repositories | `actions/how-tos/manage-runners/self-hosted-runners/manage-access` | Warns to use self-hosted runners only with private repositories. |

**Second pass, sentence by sentence (4 November 2026).** For each statement below, the docs sentence was printed and read, not just found by search. Method: fetch the page, split it into sentences, print the ones that match, read them.

| Claim in the HTML or drawings | Supported by | Result |
|---|---|---|
| Git events are kept for 7 days | Enterprise and organization audit log pages: "The audit log retains Git events for seven days." | Supported. |
| Two-factor can be required for all orgs in an enterprise | Security-settings policy page: enterprise owners can require 2FA for members, billing managers and outside collaborators in all organizations. | Supported. |
| Spending limits stop usage | Copilot budgets page: budgets "determine how Copilot usage is served, metered, or blocked", and "Stop usage when budget limit is reached" must be enabled, otherwise the budget only alerts. | Supported, with the caveat that the stop option must be switched on. |
| AI manager role | "Establishing AI managers": AI managers manage most AI features in AI Controls. | Supported. |
| GitHub App manager role | App managers page: owners can designate users or teams as App managers. | Supported. |
| Dependabot keeps actions current | Dependabot for Actions page: references in workflow files and reusable workflows are kept up to date. | Supported. |
| Dependency review blocks merges | Dependency review concept page: a failed check blocks a PR when the owner requires it, enforced through rulesets. | Supported, and only when set as required. |
| Webhook receivers validate signatures and handle replays | Webhook pages: validate the signature before processing; use the X-GitHub-Delivery header against replay; redeliver missed deliveries. | Supported. |
| Per-job GITHUB_TOKEN permissions | Automatic token authentication page: examples set `permissions` per job and advise least access. | Supported. |
| Organization SCIM manages membership | About SCIM for organizations: SCIM adds, manages and removes organization members' access. | Supported. Wording now says membership only. |
| Several owners per organization | Ownership continuity page: more than one owner avoids lapses. | Supported. "At least two" is this design's own rule. |
| Enterprise rulesets cover future repos | Not found. | Wording softened to "targets all repos in the selected orgs, or a dynamic list of repos by custom property (orgs can be chosen by name or property)". The Learn page's "current and future" is quoted only in the Learn paragraph. |
| Security configuration applies to new repos | Page describes setting a default. | Wording changed to "set as the default for new ones". |
| Third-party agents are off by default | Agents page: third-party agents "must be enabled in your account settings, your organization policies, or the 'Agents' section of an enterprise's AI controls". The Copilot in the cloud policy is enabled by default. | Supported as "must be enabled before use". Turning the cloud agent off is a setting the design has to make. |
| A member can create an organization outside the enterprise | Not found in the docs. | Statement removed from B.p1, the check text now says "record the result", and the page only says to watch for organizations outside the enterprise. |

Claims about owners, drills, two-person change, SLAs, SOC process, the transfer process, "default permission is never Admin" and "at least two approvals" are this design's own choices, not statements about GitHub.

**Third pass, sentence by sentence (4 November 2026, same method).**

| Claim | Sentence read | Result |
|---|---|---|
| Rulesets: stale approvals dismissed, approval of the latest push, code owner review | Available rules page: "Dismiss stale pull request approvals when new commits are pushed", "Require approval of the most recent reviewable push", and an option to require reviews from code owners. | Supported. |
| CODEOWNERS enforces nothing by itself | About code owners: admins "can require that pull requests have to be approved by code owners"; the option is "Require review from Code Owners". | Supported. The review must be required. |
| Tokens: maximum lifetime for fine-grained and classic | PAT policy page: owners "can set and remove maximum lifetime allowances for both fine-grained personal access tokens and personal access tokens (classic)". | Supported. |
| API request events and source IP do not cover everything | Streaming page: "Not all API requests are included", "limited to security relevant endpoints". IP page: no IP for api.request events without repository context, or when a bot acts. | Supported. |
| B: personal-account and public activity is partly invisible | IP page, non-EMU: no event or IP for authentication, for resources owned by the personal account, or for a public repository owned by an organization. | Supported. |
| IP allow list has exclusions and is about access | IP allow list page: lists what it does and does not restrict, including anonymous access to public resources. | Supported. "Not all data leaving" is a plain reading of that, not a quoted sentence. |
| Conditional Access instead of the IP allow list | Conditional Access page: with OIDC SSO for EMU (Entra ID only) owners can use the IdP's policy "instead of GitHub's IP allow list". | Supported. HTML and drawings now say "EMU with Entra ID and OIDC". The "framework's alternative" wording was removed. |
| Corporate proxy cannot restrict SSH | Proxy page: "You cannot use the enterprise header to restrict Git activity over SSH." Block the port instead. | Supported. |
| Security features are paid, public repos get some free | About GitHub Advanced Security: Code Security and Secret Protection are purchased; some features are free for public repos. | Supported. |
| Rulesets should not allow bypass | Learn Governance page (read earlier in this pass). | The design allows a short named emergency list. HTML and drawings now say "no bypass by default" and call the list a deliberate exception. |
| Org can limit repositories to private and restrict visibility changes (B.p2) | Restricting repository creation page: "Enterprise owners can restrict the options you have available for your organization's repository creation policy." and "Organization owners can restrict the type of repositories members can create to private or internal". | Supported. B.p2 says the enterprise policy sets which options the organizations may choose. |
| Deployment environments have required reviewers and "Prevent self-review" | Managing environments page: "Select Required reviewers", and "to prevent users from approving workflows runs that they triggered, select Prevent self-review". | Supported. |
| Email notifications can be limited to verified or approved domains | Org page: members "can only use an email address associated with a verified or approved domain to receive email notifications". Enterprise page: owners can restrict domains; available with Enterprise Cloud. Outside collaborators are not subject to it. | Supported. |

**Drawio strings.** Every text string in both drawio files was extracted from the XML and each one was assigned by hand to a basis. 650 unique file and string pairs: 3-page file 436 (G 75, G* 64, D 210, T 87), 1-page file 214 (G 24, G* 25, D 99, T 66). A check script confirmed that the strings in `drawio-string-evidence.tsv` and the strings in the two files are the same set, in both directions. G means the whole label rests on a GitHub statement: its basis column names the evidence row and `docs-quotes.tsv` holds the quoted sentence. G* means a GitHub feature in the label is quoted, but the label also contains a design choice (the basis column says which part), so only the feature is verified, not the whole label. D means this design's own rule, owner, process or an external control (IdP, proxy, EDR, SIEM, vault), which is a choice and not a GitHub statement. T means a title, label, legend or arrow caption with no claim. Every G string was traced one by one to a sentence; 19 that turned out to be design only were moved to D. Strings reworded in this pass because no sentence supported them: "No public repos or outside collaborators" (now: managed users cannot contribute outside the enterprise), "Public contributors have no SSO" (now: not in the IdP), "ruleset bypass" audit alert (now: ruleset changes), "bypass alerts" (now: bypass lists), "The strictest applicable rule wins" (now the documented ruleset sentence), "Lower layers tighten, never relax" and "Enforced higher-layer rules stay in force" (now labelled design rules), "Rulesets and reports use them" (now: searches). Earlier changes: four "audited bypass" strings, "Emergency only: a short named list, every use reviewed.", "Baselines target all repos in scope.", "Set security configurations as the default for new repos, verify coverage.". The classing is mine, not a tool's guarantee.

**Evidence rows added in the last pass (4 November 2026, sentences read).**

| Ref | Page | Sentence |
|---|---|---|
| N1 | `admin/managing-iam/understanding-iam-for-enterprises/abilities-and-restrictions-of-managed-user-accounts` | "Managed user accounts can contribute only to private and internal repositories within their enterprise and their own private repositories." "Only private and internal repositories can be created in organizations owned by an enterprise with managed users". "On GitHub.com, managed user accounts can view all public repositories, but cannot interact with repositories outside of the enterprise". |
| N2 | `repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets` | "if multiple rulesets target the same branch or tag in a repository, the rules in each of these rulesets are aggregated." "the most restrictive version of the rule applies." |
| N3 | `admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise` | Lists the actions `org.add_member`, `repo.access`, `repo.transfer`, `integration.create`, `personal_access_token.access_granted`, `repository_ruleset.create`, `.update`, `.destroy`. No ruleset bypass action is listed. |
| N4 | Security configuration pages | "The default security configuration for an organization is only automatically applied to new repositories". Separate pages say you apply a configuration to existing repositories. |
| N5 | `actions/concepts/security/openid-connect` | Example token has `sub` of `repo:octo-org/octo-repo:environment:prod` and an `environment` claim. |
| N6 | `admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/create-enterprise-teams` | Teams can "Be added to organizations, where organization administrators can grant the team additional access", "Receive bypass access on rulesets", and members "receive the base level of repository permissions for the organization". |
| N7 | `.../managing-rulesets/available-rules-for-rulesets` | "Block force pushes", "Restrict deletions". |
| N8 | App install, org secrets and runner group pages | Apps: "select All repositories or Only select repositories". Org secrets can use selected repositories. A runner group needs a policy "which repositories and workflows have access". Webhook pages: validate the signature; redeliver missed deliveries. |
| RG | Section 7, "Also checked and true" | Runner groups limited to repositories and workflows; enterprise setting disables repository-level runner creation. |

**Item by item, A.p1 to A.p16 and B.p1 to B.p16 (4 November 2026, sentences read from docs.github.com Enterprise Cloud, npm docs for npm).** "Design" means a rule of this design that no GitHub page can confirm.

| Item | GitHub claims and the sentence that supports them | Design only |
|---|---|---|
| A.p1 | Forking policy: owners can "never allow forking of private or internal repositories". Repository creation and visibility-change policies exist at enterprise level. EMU: user-owned repositories are something owners "allowed", so a setting exists. | Which values to choose. |
| A.p2 | "who can create, delete, or transfer repositories" is available in a repository policy. | Named roles only. |
| A.p3 | Enterprise rulesets: "target many organizations, repositories, and branches", organizations by all, list, name pattern or custom property, repositories by custom property. Evaluate status previews impact. Stale approval dismissal, latest-push approval, signed commits are rules. Bypass list exists. Wording fixed this pass: repositories are targeted by custom property, organizations by name or property. | Two approvals, review of bypass uses. |
| A.p4 | Default security configuration applies to new repositories. Delegated bypass for push protection: named users, teams or roles. Security campaigns exist. Code Security and Secret Protection are "available" on Enterprise Cloud (purchased). | Severity deadlines. |
| A.p5 | Pinning policy "Require actions to be pinned to a full-length commit SHA". Default token has read access to contents and packages. Creating and approving pull requests is "disabled by default" (enterprise) and not allowed by default for new organizations. | Approved list contents. |
| A.p6 | Enterprise can restrict classic tokens from accessing organizations, with a separate fine-grained approval policy. OAuth app access restrictions exist and are on for new organizations. Wording now says "blocked from accessing the organizations". Maximum lifetimes: third pass. | Preferring narrow Apps. |
| A.p7 | Third pass (streaming, 7 days, source IP gaps). | Archive design. |
| A.p8 | Third pass (IP allow list, proxy and SSH, Conditional Access). | Block upload paths. |
| A.p9 | "You can use those properties to target repositories with rulesets." The claim that repository policies can target properties was not found, so it was removed. | Which properties. |
| A.p10 | Enterprise teams can be synced with an IdP group. | Orgs grant to these teams. |
| A.p11 | Learn lists a sandbox organization as one option. | The deviation and its reasons. |
| A.p12 | None. | All of it. |
| A.p13 | Cloud agent has an ephemeral environment and "access to the internet is limited by a firewall". Audit streaming can include agent session activity. Model enable and disable policies exist. Budgets exist. Third-party agents "must be enabled". | Reviewed MCP servers, code-owner review of instruction files. |
| A.p14 | Security manager role and custom repository roles exist (custom roles need Enterprise Cloud). | Two owners, never Admin by default. |
| A.p15 | Dependency review action fails by default on vulnerable packages. Dependabot supports actions and packages. Artifact attestations establish build provenance. | Lockfiles, scripts off, deploy verification. |
| A.p16 | Reusable workflows can be referenced by tag or SHA (design pins them). | Platform org, versioning, code owners. |
| B.p1 | Enterprise owners add organizations in three ways. Two-factor can be required for all organizations. | Reconciling, watching for organizations outside the enterprise. Whether a member can create one on their own is not stated anywhere on the page. |
| B.p2 | Enterprise repository creation policy, org owners can limit to private. Visibility change policy exists. | Which orgs may be public. |
| B.p3 | As A.p3. Learn says rulesets should not allow bypass. | Emergency list. |
| B.p4 | Some Advanced Security features are free for public repositories on GitHub.com. | Baseline. |
| B.p5 | As A.p5. pull_request_target: Learn Application Security. | Test. |
| B.p6 | Maximum lifetime for fine-grained and classic: third pass. | Approved scope. |
| B.p7 | Third pass (personal-account and public gaps, 7 days). | Archive. |
| B.p8 | None. | Drift job. |
| B.p9 | As A.p9. | Properties. |
| B.p10 | None. | Org model. |
| B.p11 | Learn lists a sandbox organization. | Its use here. |
| B.p12 | Organization SCIM: "You cannot use this implementation of SCIM with an enterprise account or with an organization with managed users." Enterprise SCIM is documented under Enterprise Managed Users. | The deviation. |
| B.p13 | As A.p13 for third-party agents. | Pilot first, reviewed models. |
| B.p14 | As A.p14. | Two owners. |
| B.p15 | PyPI trusted publishing via OIDC (GitHub docs). npm trusted publishing via OIDC, GitHub-hosted runners only, automatic provenance for public packages from public repositories (npm docs). | Lockfiles, scripts off. |
| B.p16 | As A.p16. | Platform org. |

Operations, accountability, exchange, intake, incident and build-and-deploy items in the HTML and drawings (owners, drills, backups, RPO and RTO, transfer service, intake, incident steps, patching) are this design's own rules. No GitHub page can confirm them, so they are labelled as design choices.

**Quoted evidence.** `docs-quotes.tsv` holds 78 sentences copied from the fetched GitHub docs, the npm and PyPI docs, and the GitHub Learn pages (Learn is a JavaScript app, so those were read in a browser). They cover 37 refs. Every G row in `drawio-string-evidence.tsv` points to refs that have a quote, except the design half of one row (`DS`, grants per repo). A quote proves the feature or statement exists on that page. It does not prove that a whole drawing label is true, because many labels mix a GitHub feature with a design choice. The G* rows are mostly recommendations phrased as instructions ("verify coverage", "keep the bypass list short", "no secrets"). A recommendation is a design choice, not a claim that GitHub can be checked against, so it is left as design. The audit event lines in the N3 rows are the event name plus the description from the audit log events page, joined with a colon. The fine print is in the basis column.

**Not verified, and not claimed.** Product behaviour after 4 November 2026. Anything on a real tenant. Whether a member can create an organization outside the enterprise: searched in four ways, nothing found, so no file asserts it either way. The HTML and drawings no longer claim an audit event for "ruleset bypass" (only ruleset create, update and destroy events are listed), a "strictest layer wins" rule across enterprise and organization policy (only the ruleset rule is documented), or "no outside collaborators" for managed users. "Reviewed models" and "reviewed MCP servers" are design rules.

**Remaining limit:** anything on GitHub that changed after 4 November 2026 is not covered. Nothing was tested on a real GitHub tenant.

### Limits of this QA

- GitHub's Enterprise Server docs say most Copilot features need a presence on GitHub Enterprise Cloud and only some are available on Enterprise Server. Hosting option 3 (self-hosted) therefore has far fewer agent controls. [Copilot on Enterprise Server](https://docs.github.com/en/enterprise-server@latest/copilot).
- The interactive page counts 106 elements from its data. It was checked in headless Chrome with no console errors, and not on a real phone.
- The drawio files carry the new controls only as short in-place chip text, because the layout is fixed. The interactive page holds the full wording.
- The drawings were rendered and viewed, not opened in diagrams.net itself.
- Nothing here has been tested against a real GitHub tenant.
