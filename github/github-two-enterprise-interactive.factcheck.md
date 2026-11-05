Belongs to: [GitHub two-enterprise reference](github-two-enterprise-interactive.html)

# Statement review, 5 November 2026

Scope: the interactive HTML, all 106 boxes, their titles, summaries, descriptions, checks, chips, steps, four design-choice explanations, five flow summaries, and surrounding text. Primary sources were opened or searched on this date. The earlier drawings and their 4 November review are historical, not revalidated here.

Nothing was tested on a real GitHub tenant. No classification, accreditation, device isolation, provisioning, security scan, token policy, deployment trust, transfer service, backup or recovery drill was tested. Proposed checks describe acceptance criteria, not observed results. Product documentation proves capability, not implementation or accreditation.

Verdicts: **Requirement** is a proposed control defined by this design, not an empirical claim. **Supported/requirement** combines documented capability with a proposed configuration; the linked sources support capability only. **Inference** is explicitly labelled. **Label** identifies an illustrative name, UI control or proposed sequence. Every description sentence is listed individually below; all other visible box fields are included too.

## Corrections

- GHE.com is an A-only alternative. It requires managed users and cannot host B's public repositories; regional storage has exceptions.
- B needs per-organization SAML/SCIM integrations. Organization SCIM does not manage team grants or personal-account ownership.
- Repository lifecycle controls cannot stop copying by an authorised reader. Base permission none does not override owner, direct or security-manager access.
- Evaluate rulesets do not enforce protection. SHA policy covers actions but permits reusable-workflow tags.
- PAT policy blocks resource access, not creation or global token validity. Lifetime is the configured lifetime, not token age. SSH keys and administrator exemptions need separate checks.
- Security-manager roles include organization-wide repository read access. Platform automation and shared workflows remain trust paths.
- Copilot firewall excludes MCP and setup processes. Hosted CI can have OS admin privileges and public internet access.
- npm trusted publishing and provenance have separate prerequisites. Push protection does not detect arbitrary secret strings.
- State/environment names and dev containers alone do not prove isolation. Unverified framework comparisons were replaced with explicit design choices; stable IDs remain unchanged.

## Sources checked on 5 November 2026

- **DEPROVISION**: [SCIM suspension and IdP triggers](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/deprovisioning-and-reinstating-users).
- **EMU**: [Managed account restrictions](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/abilities-and-restrictions-of-managed-user-accounts).
- **TEAMS**: [Enterprise teams](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/create-enterprise-teams).
- **SAML**: [SAML scope](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/deciding-whether-to-configure-saml-for-your-enterprise-or-your-organizations).
- **SCIM**: [Organization SCIM](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/about-scim-for-organizations).
- **SWITCH**: [Switching SAML scope](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/switching-your-saml-configuration-from-an-organization-to-an-enterprise-account).
- **RESIDENCY**: [Data storage and exceptions](https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/about-storage-of-your-data-with-data-residency).
- **GHE**: [GHE.com feature differences](https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/feature-overview-for-github-enterprise-cloud-with-data-residency).
- **REPO**: [Repository policies (preview)](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-repositories-in-your-enterprise/governing-how-people-use-repositories-in-your-enterprise).
- **PRIVILEGES**: [Repository management policies](https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise).
- **RULES**: [Enterprise rulesets](https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-governance).
- **AVAILABLE**: [Available rules](https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets).
- **LAYER**: [Ruleset layering](https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).
- **OWNERS**: [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
- **SECURITY**: [Security configurations](https://docs.github.com/en/enterprise-cloud@latest/code-security/how-tos/secure-at-scale/configure-enterprise-security/establish-complete-coverage/create-custom-configuration).
- **LICENSE**: [Advanced Security products](https://docs.github.com/en/enterprise-cloud@latest/get-started/learning-about-github/about-github-advanced-security).
- **BYPASS**: [Delegated secret bypass](https://docs.github.com/en/enterprise-cloud@latest/code-security/concepts/secret-security/delegated-bypass).
- **PUSH**: [Push protection limits](https://docs.github.com/en/code-security/concepts/secret-security/command-line-push-protection).
- **CAMPAIGN**: [Security campaigns](https://docs.github.com/en/enterprise-cloud@latest/code-security/concepts/security-at-scale/about-security-campaigns).
- **ACTIONS**: [Enterprise Actions policies](https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise).
- **SECURE**: [Secure workflow use](https://docs.github.com/en/actions/reference/security/secure-use).
- **TOKEN**: [PAT policies](https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise).
- **AUDIT**: [Audit coverage and retention](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/accessing-the-audit-log-for-your-enterprise).
- **STREAM**: [Audit streaming](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise).
- **IP**: [Source IP limitations](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/displaying-ip-addresses-in-the-audit-log-for-your-enterprise).
- **ALLOW**: [IP allow list exclusions](https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/hardening-security-for-your-enterprise/restricting-network-traffic-to-your-enterprise-with-an-ip-allow-list).
- **PROXY**: [Corporate proxy restrictions](https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/hardening-security-for-your-enterprise/restricting-access-to-githubcom-using-a-corporate-proxy).
- **CAP**: [Entra Conditional Access limits](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/configuring-authentication-for-enterprise-managed-users/about-support-for-your-idps-conditional-access-policy).
- **PROPERTIES**: [Custom properties](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-repositories-in-your-enterprise/managing-custom-properties-for-repositories-in-your-enterprise).
- **AGENT**: [Copilot cloud policies](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/manage-copilot-in-the-cloud).
- **FIREWALL**: [Copilot firewall exclusions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-the-firewall).
- **THIRD**: [Third-party agent enablement](https://docs.github.com/copilot/managing-github-copilot-in-your-organization/managing-policies-and-features-for-copilot-in-your-organization).
- **ROLE**: [Security manager role](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).
- **DEPENDENCY**: [Dependency review](https://docs.github.com/en/enterprise-cloud@latest/code-security/concepts/supply-chain-security/dependency-review).
- **DEPENDABOT**: [Supported Dependabot ecosystems](https://docs.github.com/en/enterprise-cloud@latest/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories).
- **ATTEST**: [Artifact attestations](https://docs.github.com/en/enterprise-cloud@latest/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations).
- **REUSE**: [Reusable workflows](https://docs.github.com/en/enterprise-cloud@latest/actions/how-tos/reuse-automations/reuse-workflows).
- **2FA**: [Enterprise security policies](https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-security-settings-in-your-enterprise).
- **ORGS**: [Adding organizations](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/adding-organizations-to-your-enterprise).
- **ARCHIVE**: [Organization archiving](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/archiving-an-organization).
- **NPM**: [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/).
- **PYPI**: [PyPI trusted publishing](https://docs.pypi.org/trusted-publishers/).
- **RUNNER**: [Runner groups](https://docs.github.com/en/enterprise-cloud@latest/actions/how-tos/manage-runners/self-hosted-runners/manage-access).
- **AZURE**: [Azure private networking](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization).
- **HOSTED**: [Hosted runner OS privileges](https://docs.github.com/en/actions/reference/runners/github-hosted-runners).
- **FORK**: [Safe fork PR workflow context](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target).
- **OIDC**: [OIDC issuer, audience and subject](https://docs.github.com/en/enterprise-cloud@latest/actions/reference/security/oidc).
- **WEBHOOK**: [Webhook verification and delivery IDs](https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks).
- **ENV**: [Deployment environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments).

## Surrounding text and controls

- Title, enterprise headings, organization/repository names: illustrative design labels, not a claim about a deployed tenant.
- Date and basis: this review used primary GitHub, npm and PyPI documentation on 5 November 2026. No Well-Architected conformance claim remains.
- G/X/G+X and E/O/R: design notation. Boxes can combine capabilities and proposed requirements; a policy-layer tag is not proof that one enterprise switch configures every item.
- Hosting connector and boundary caption: explicitly limited to the github.com baseline. GHE.com and self-hosted alternatives require reassessment.
- Filters, popovers, related links and hash links: verified by browser interaction checks recorded below. Existing node and filter IDs are preserved.
- Drawings: local files exist; page labels them as earlier versions not rechecked in this review.
- AI note: matches the repository's required wording exactly.
- Operations, owners, transfer, SOC separation, classification approval, review frequency, deadlines, RPO/RTO and restore coverage are requirements. No external standard or legal accreditation is claimed.

## Box statements

### g0: Gate 0: approve the hosting service before loading classified content

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Gate 0: approve the hosting service before loading classified content
- **Summary, Label / proposed control:** A decision for the security authority, not a product setting. If no option is accredited, do not proceed.
- **Description, Requirement:** Nothing classified is loaded until the specific service, hosting region, administrator and support access, identity platform, runners, scanners, logs and backups are approved.
- **Description, Requirement:** A residency choice is not an accreditation decision.
- **Proposed check, Requirement (not run):** An approval record exists for the service, the region, support access and every connected data processor.

### g1: 1  Enterprise Cloud on github.com

Checked 5 November 2026. Corrected or qualified. Basis: GHE.

- **Title, Label / proposed control:** 1  Enterprise Cloud on github.com
- **Description, Supported/requirement:** Multi-tenant SaaS on github.com.
- **Description, Supported/requirement:** This is the baseline shown for A and B.
- **Description, Supported/requirement:** A requires explicit hosting approval before any classified content is loaded.

### g2: 2  Cloud with data residency (GHE.com)

Checked 5 November 2026. Corrected or qualified. Basis: RESIDENCY, GHE.

- **Title, Label / proposed control:** 2  Cloud with data residency (GHE.com)
- **Description, Supported/requirement:** Alternative for A only: GHE.com stores specified data in a chosen region, with documented exceptions and transfers outside it.
- **Description, Supported/requirement:** GHE.com requires managed users and does not support public repositories.
- **Description, Supported/requirement:** B stays on github.com.
- **Description, Supported/requirement:** Reassess feature availability, endpoints and integrations; residency alone is not accreditation.

### g3: 3  Self-hosted or accredited platform

Checked 5 November 2026. Corrected or qualified. Basis: GHE.

- **Title, Label / proposed control:** 3  Self-hosted or accredited platform
- **Description, Supported/requirement:** Alternative for A if Cloud is unsuitable.
- **Description, Supported/requirement:** An assessed self-hosted or accredited platform needs a separate identity, feature and operations design.
- **Description, Supported/requirement:** The Cloud controls below do not automatically apply; B remains on github.com for public work.

### c.bound: Logical boundary

Checked 5 November 2026. Corrected or qualified. Basis: EMU, PRIVILEGES.

- **Title, Label / proposed control:** Logical boundary
- **Description, Supported/requirement:** The baseline has two governance domains on github.com, without an air gap.
- **Description, Supported/requirement:** People with privileges in both domains and broadly scoped integrations can bridge them.
- **Description, Supported/requirement:** Keep credentials and app installations separate.
- **Description, Inference:** [inference] Some compartments may require additional hosting separation after a threat assessment.
- **Proposed check, Requirement (not run):** List every admin and app that can see both enterprises. The list should be empty or justified.

### c.ident: Keep identities apart

Checked 5 November 2026. Corrected or qualified. Basis: SCIM, SWITCH.

- **Title, Label / proposed control:** Keep identities apart
- **Summary, Label / proposed control:** Dedicated IdP integration for A; separate SAML and SCIM integration for each B organization. No shared admin or service accounts across domains.
- **Description, Supported/requirement:** People who work in both enterprises use two GitHub identities and separate work environments.
- **Description, Supported/requirement:** A separate browser profile alone does not stop copying.
- **Description, Supported/requirement:** Use managed workstations or isolated sessions, distinct credential stores and controlled egress.
- **Proposed check, Requirement (not run):** A sensitive workstation cannot upload through an unapproved GitHub account or app.

### c.xfer: Approved transfer service

Checked 5 November 2026. Corrected or qualified. Basis: Design definition on this page.

- **Title, Label / proposed control:** Approved transfer service
- **Description, Requirement:** Proposed external transfer process.
- **Description, Requirement:** Export: the release authority decides that content may leave A, history, secrets and IaC topology are inspected, and a signed manifest with a hash is logged.
- **Description, Requirement:** Intake: origin is verified, content is quarantined, scanned and pinned before it enters A.
- **Description, Requirement:** Never mirror sensitive repos into B automatically.
- **Description, Requirement:** Remove the whole path if transfers are prohibited.
- **Proposed check, Requirement (not run):** Show that an approved transfer works end to end, or show that the path is blocked.
- **Step, requirement:** Release authority decides
- **Step, requirement:** Inspect history, secrets, IaC topology
- **Step, requirement:** Signed manifest, hash logged
- **Step, requirement:** Intake: verify, quarantine, scan, pin

### c.soc: Common SOC view

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Common SOC view
- **Summary, Label / proposed control:** Approved, minimized metadata only.
- **Description, Requirement:** A common SOC can share procedures and approved summaries.
- **Description, Requirement:** Detailed logs stay in each domain because repository names, paths and identities can reveal critical-system details.
- **Description, Requirement:** Even sanitised sharing needs classification approval.
- **Proposed check, Requirement (not run):** Sample the shared feed and confirm it holds no repo names, paths or user identities from A.

### A.people: Cleared people

Checked 5 November 2026. Corrected or qualified. Basis: Design definition on this page.

- **Title, Label / proposed control:** Cleared people
- **Summary, Label / proposed control:** Need-to-know groups. Managed workstation, signed commits, controlled egress.
- **Description, Requirement:** Only authorised personnel are assigned to A.
- **Description, Requirement:** Access follows need-to-know groups.
- **Description, Requirement:** Require managed workstations or assessed isolated sessions, signed commits and controlled egress.
- **Description, Requirement:** Dev containers may run non-root inside that environment; a container alone is not the domain boundary.
- **Description, Requirement:** Limit developer tools, AI assistants and extensions to an approved list.
- **Proposed check, Requirement (not run):** Try to reach GitHub from an unmanaged device and from a managed one with a personal account.

### A.idp: Corporate IdP

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Corporate IdP
- **Summary, Label / proposed control:** Dedicated app for A. Phishing-resistant MFA, privileged access through PAM.
- **Description, Requirement:** A dedicated IdP application for A owns the account lifecycle.
- **Description, Requirement:** Phishing-resistant MFA, privileged access through PAM, a short list of named enterprise owners and protected emergency recovery access.
- **Description, Requirement:** This design chooses SAML.
- **Proposed check, Requirement (not run):** Run an IdP outage drill and use the emergency recovery access. Review that use independently.

### A.scim: SAML + SCIM to EMU

Checked 5 November 2026. Corrected or qualified. Basis: EMU, TEAMS, DEPROVISION.

- **Title, Label / proposed control:** SAML + SCIM to EMU
- **Summary, Label / proposed control:** Enterprise SCIM. IdP groups drive enterprise teams. Keep managed users inside the enterprise. (Reworded 5 Nov 2026 to a requirement; the product facts are sourced in the description.)
- **Description, Supported/requirement:** Enterprise Managed Users: the IdP owns the account.
- **Description, Supported/requirement:** Enterprise SCIM provisions accounts and suspends them when deprovisioned; it does not delete the accounts.
- **Description, Supported/requirement:** IdP groups can sync to enterprise teams.
- **Description, Supported/requirement:** Managed users cannot create public repos, and cannot collaborate outside the enterprise.
- **Proposed check, Requirement (not run):** Trigger SCIM deprovisioning through the configured IdP integration and verify suspension and access loss. An IdP-only suspension may not send a SCIM request. Check privileged and exceptional paths separately.

### B.people: Workforce and partners

Checked 5 November 2026. Corrected or qualified. Basis: SAML, SCIM.

- **Title, Label / proposed control:** Workforce and partners
- **Summary, Label / proposed control:** Assigned by IdP group. Separate device zone from A. Public contributions require no corporate SSO.
- **Description, Supported/requirement:** Employees and approved partners are assigned through the relevant organization IdP integrations.
- **Description, Supported/requirement:** Require a separate device zone from A.
- **Description, Supported/requirement:** Public contributions do not require corporate SSO; contributors may also hold separately approved private access, so review grants rather than assuming identity categories are exclusive.
- **Proposed check, Requirement (not run):** Confirm a partner has access only to the repos approved for them, with an expiry date.

### B.idp: Corporate IdP

Checked 5 November 2026. Corrected or qualified. Basis: SCIM, SWITCH.

- **Title, Label / proposed control:** Corporate IdP
- **Summary, Label / proposed control:** Separate integration per organization in B. The IdP owns provisioned membership; reconcile team grants separately.
- **Description, Supported/requirement:** Use a separate SAML and SCIM integration for each B organization, with credentials separate from A.
- **Description, Supported/requirement:** Organization SCIM manages membership, not team grants.
- **Description, Supported/requirement:** Configure supported team synchronization or separate automation and reconcile it.
- **Proposed check, Requirement (not run):** Compare the admin lists of A and B. They share no accounts.

### B.scim: SAML + SCIM per org

Checked 5 November 2026. Corrected or qualified. Basis: SAML, SCIM, SWITCH.

- **Title, Label / proposed control:** SAML + SCIM per org
- **Summary, Label / proposed control:** SAML enforced and SCIM configured in every org. Use per-org SAML, not enterprise SAML. Keep personal accounts. (Reworded 5 Nov 2026 to a requirement; the product facts are sourced in the description.)
- **Description, Supported/requirement:** People retain personal GitHub accounts linked to SAML identities.
- **Description, Supported/requirement:** Enforce SAML and configure SCIM separately in each organization.
- **Description, Supported/requirement:** SCIM manages organization membership, not personal-account ownership or team grants.
- **Description, Supported/requirement:** Enterprise-level SAML does not support organization SCIM.
- **Description, Supported/requirement:** GitHub offers no enterprise SCIM for personal-account enterprises.
- **Proposed check, Requirement (not run):** Remove a person and check every org, outside-collaborator grants, deploy keys, app installs, webhooks and cloud identities.

### A.p1: Private repos only, no forks

Checked 5 November 2026. Retained after review. Basis: EMU, PRIVILEGES.

- **Title, Label / proposed control:** Private repos only, no forks
- **Description, Supported/requirement:** Organization repos are private only.
- **Description, Supported/requirement:** User-owned repos and private forking are turned off, and visibility changes are restricted.
- **Proposed check, Requirement (not run):** Create a repo in each org, then try to make it public or fork it.

### A.p2: Limit repo create, delete, transfer

Checked 5 November 2026. Corrected or qualified. Basis: REPO, PRIVILEGES.

- **Title, Label / proposed control:** Limit repo create, delete, transfer
- **Description, Supported/requirement:** Restrict repository creation, deletion and transfer to approved actors.
- **Description, Supported/requirement:** Repository policies support these restrictions and are currently in public preview.
- **Description, Supported/requirement:** Review allow lists and member-privilege settings.
- **Description, Supported/requirement:** This governs repository lifecycle operations; it cannot stop an authorised reader from copying source elsewhere.
- **Proposed check, Requirement (not run):** Try each action as a normal member.

### A.p3: Enterprise rulesets, signed commits

Checked 5 November 2026. Corrected or qualified. Basis: RULES, AVAILABLE, LAYER, OWNERS.

- **Title, Label / proposed control:** Enterprise rulesets, signed commits
- **Description, Supported/requirement:** Use enterprise branch and tag rulesets targeting all in-scope repositories or custom-property selections.
- **Description, Supported/requirement:** For protected branches require two approvals, code-owner review, stale-review dismissal, latest-push approval and signed commits.
- **Description, Supported/requirement:** Restrict force pushes and deletions.
- **Description, Supported/requirement:** Review bypass lists and uses.
- **Description, Supported/requirement:** Evaluate previews impact without enforcing rules; keep existing protection active until the replacement is Active.
- **Proposed check, Requirement (not run):** Negative tests: push to main, force push, and bypass by an actor who is not on the list.

### A.p4: Security configs on all repos

Checked 5 November 2026. Corrected or qualified. Basis: SECURITY, LICENSE, BYPASS, CAMPAIGN.

- **Title, Label / proposed control:** Security configs on all repos
- **Description, Supported/requirement:** A security configuration is attached to every repo and set as the default for new ones.
- **Description, Supported/requirement:** It needs GitHub Code Security and Secret Protection licences, or approved equivalents.
- **Description, Supported/requirement:** Configure delegated push-protection bypass; review the named list and built-in owner/security-manager privileges.
- **Description, Supported/requirement:** Alerts carry a severity deadline, and security campaigns clear backlogs.
- **Proposed check, Requirement (not run):** Create a new repo and confirm the baseline appears with no manual steps.

### A.p5: Approved Actions, read-only token

Checked 5 November 2026. Corrected or qualified. Basis: ACTIONS, SECURE.

- **Title, Label / proposed control:** Approved Actions, read-only token
- **Description, Supported/requirement:** Allow approved actions and reusable workflows.
- **Description, Supported/requirement:** Require action references to use full commit SHAs; this policy still permits reusable workflows by tag, so check their SHA pinning separately.
- **Description, Supported/requirement:** Set the default GITHUB_TOKEN to read contents and packages, grant extra permissions per job, and disable PR creation/approval.
- **Description, Supported/requirement:** Never execute untrusted contributor code in privileged pull_request_target or workflow_run contexts.
- **Proposed check, Requirement (not run):** Try a workflow with an unapproved action. Expected: it fails. Record the result.

### A.p6: Classic PATs blocked

Checked 5 November 2026. Corrected or qualified. Basis: TOKEN.

- **Title, Label / proposed control:** Classic PATs blocked
- **Description, Supported/requirement:** Block classic PAT access to organization resources.
- **Description, Supported/requirement:** This does not prevent token creation or revoke SSH keys previously created using a token.
- **Description, Supported/requirement:** Require approval and bounded lifetimes for fine-grained PATs.
- **Description, Supported/requirement:** Prefer narrowly scoped GitHub Apps.
- **Description, Supported/requirement:** Review OAuth grants, app installations and webhook destinations separately.
- **Proposed check, Requirement (not run):** Create a classic PAT, then try to read a private organization repo with it. Expected: access is refused. Check SSH keys separately and record results.

### A.p7: Audit stream with source IP

Checked 5 November 2026. Retained after review. Basis: AUDIT, STREAM, IP.

- **Title, Label / proposed control:** Audit stream with source IP
- **Description, Supported/requirement:** Audit and Git events stream to A's own archive.
- **Description, Supported/requirement:** API request events and source IP disclosure are on.
- **Description, Supported/requirement:** Neither covers every operation, so correlate with proxy and endpoint evidence.
- **Description, Supported/requirement:** GitHub keeps Git events for only 7 days, so the stream must run from day one.
- **Proposed check, Requirement (not run):** Trigger a test event and find it, with the source IP, in the archive.

### A.p8: IP allow list, proxy only

Checked 5 November 2026. Corrected or qualified. Basis: ALLOW, PROXY, CAP.

- **Title, Label / proposed control:** IP allow list, proxy only
- **Description, Supported/requirement:** Access only through a mandatory corporate proxy plus network allow lists.
- **Description, Supported/requirement:** Block Git over SSH and unsupported upload paths.
- **Description, Supported/requirement:** An IP allow list controls inbound access, not all data leaving, and has documented exclusions.
- **Description, Supported/requirement:** For EMU with Entra ID and OIDC, GitHub can enforce the IdP's Conditional Access IP conditions instead of its own IP allow list, with documented exclusions.
- **Description, Supported/requirement:** It cannot enforce device compliance conditions.
- **Description, Supported/requirement:** Choose per accreditation.
- **Proposed check, Requirement (not run):** Try to push from outside the proxy, and over SSH.

### A.p9: Custom properties on every repo

Checked 5 November 2026. Retained after review. Basis: PROPERTIES, RULES.

- **Title, Label / proposed control:** Custom properties on every repo
- **Description, Supported/requirement:** Every repo carries properties such as system, class and owner.
- **Description, Supported/requirement:** Rulesets can target repos by custom property, so those baselines follow the data, not the repo name.
- **Proposed check, Requirement (not run):** List repos with a missing property. The list should be empty.

### A.p10: Enterprise teams from IdP groups

Checked 5 November 2026. Retained after review. Basis: TEAMS.

- **Title, Label / proposed control:** Enterprise teams from IdP groups
- **Description, Supported/requirement:** Enterprise teams are filled from IdP groups, so membership is decided in one place.
- **Description, Supported/requirement:** Organizations grant access to these teams.
- **Proposed check, Requirement (not run):** Move a person between IdP groups and confirm team access follows.

### A.p11: Orgs by class, no sandbox

Checked 5 November 2026. Corrected or qualified. Basis: ARCHIVE.

- **Title, Label / proposed control:** Orgs by class, no sandbox
- **Description, Supported/requirement:** Organizations follow classification and need-to-know, not the management chart.
- **Description, Supported/requirement:** A has no sandbox organization: experiments run in B with no classified data.
- **Description, Supported/requirement:** This is a design choice.
- **Proposed check, Requirement (not run):** Confirm no organization in A holds unclassified experiments.

### A.p12: Threat model per system

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Threat model per system
- **Description, Requirement:** Each critical system has a threat model that decides which controls are required.
- **Description, Requirement:** It is kept up to date as the system changes.
- **Proposed check, Requirement (not run):** Pick a system and ask for its threat model and its last review date.

### A.p13: Agents and AI, off until approved

Checked 5 November 2026. Corrected or qualified. Basis: AGENT, FIREWALL, THIRD.

- **Title, Label / proposed control:** Agents and AI, off until approved
- **Description, Supported/requirement:** Keep Copilot and agents disabled until approved for the system.
- **Description, Supported/requirement:** If approved, scope policies, models and MCP integrations to the reviewed feature.
- **Description, Supported/requirement:** Require normal PR protections and code-owner review of agent configuration.
- **Description, Supported/requirement:** Assess runner or sandbox isolation and spending controls.
- **Description, Supported/requirement:** The Copilot cloud agent firewall has exclusions, including MCP processes and setup steps; require independent network controls.
- **Proposed check, Requirement (not run):** Open an agent pull request that edits a workflow file. Expected: it will need a code-owner review. Record the result.

### A.p14: Scoped roles, review security-manager access

Checked 5 November 2026. Corrected or qualified. Basis: ROLE, PRIVILEGES.

- **Title, Label / proposed control:** Scoped roles, review security-manager access
- **Description, Supported/requirement:** Delegate organization duties with security manager or custom roles instead of broad Admin where suitable.
- **Description, Supported/requirement:** Security manager includes read access to every repository in its organization, so assign it only within an approved compartment.
- **Description, Supported/requirement:** This design requires two owners per organization, no Admin base permission, named app managers and a short enterprise-owner list.
- **Proposed check, Requirement (not run):** List users with Admin on any repo. Each one should have a recorded reason.

### A.p15: Dependency and provenance controls

Checked 5 November 2026. Retained after review. Basis: DEPENDENCY, DEPENDABOT, ATTEST.

- **Title, Label / proposed control:** Dependency and provenance controls
- **Description, Supported/requirement:** Dependency review is a required check.
- **Description, Supported/requirement:** Lockfiles are mandatory, and install-time lifecycle scripts are off in builds.
- **Description, Supported/requirement:** Builds produce signed artifacts with provenance, and deploys verify them.
- **Description, Supported/requirement:** Dependabot keeps actions and packages current.
- **Proposed check, Requirement (not run):** Add a dependency with a known advisory in a PR. The check should block it.

### A.p16: Shared workflow platform

Checked 5 November 2026. Retained after review. Basis: REUSE, ACTIONS.

- **Title, Label / proposed control:** Shared workflow platform
- **Description, Supported/requirement:** Approved workflows and actions live in one dedicated organization in A, owned by a platform team.
- **Description, Supported/requirement:** They are versioned (major tags, changelog, migration notes), protected by code owners and required reviews, and pinned by consumers.
- **Description, Supported/requirement:** Teams consume them with no copy-paste.
- **Description, Supported/requirement:** A and B never share workflows, because the enterprises stay apart.
- **Description, Supported/requirement:** Each has its own copy.
- **Proposed check, Requirement (not run):** Change a shared workflow without a code-owner review. Expected: it is blocked. Record the result. Check that a consumer repo pins a version.

### B.p1: 2FA, owner-added orgs

Checked 5 November 2026. Retained after review. Basis: 2FA, ORGS.

- **Title, Label / proposed control:** 2FA, owner-added orgs
- **Description, Supported/requirement:** Two-factor is required for every organization in the enterprise.
- **Description, Supported/requirement:** Enterprise owners add organizations to the enterprise: they create a new one, invite an existing one, or transfer one.
- **Description, Supported/requirement:** Watch for organizations that appear outside the enterprise.
- **Proposed check, Requirement (not run):** Try to add an org to the enterprise as a normal member and record the result. Monitor for orgs outside the enterprise.

### B.p2: Public repos only in publishing org

Checked 5 November 2026. Retained after review. Basis: REPO, PRIVILEGES.

- **Title, Label / proposed control:** Public repos only in publishing org
- **Description, Supported/requirement:** Public visibility is allowed only in public-open-source.
- **Description, Supported/requirement:** In every other organization, repository creation is limited to private repositories and visibility changes are restricted, so a private repo cannot be made public by mistake.
- **Description, Supported/requirement:** The enterprise policy sets which of these the organizations may choose.
- **Proposed check, Requirement (not run):** Set a repo to public in internal-engineering. Expected: it is blocked. Record the result.

### B.p3: Enterprise rulesets baseline

Checked 5 November 2026. Corrected or qualified. Basis: RULES, AVAILABLE, LAYER, OWNERS.

- **Title, Label / proposed control:** Enterprise rulesets baseline
- **Description, Supported/requirement:** Apply enterprise branch and tag rulesets to all in-scope repositories or custom-property selections.
- **Description, Supported/requirement:** Allow no bypass by default; document any emergency exception and review its use.
- **Description, Supported/requirement:** Overlapping rulesets aggregate, with the most restrictive version of each rule applying.
- **Description, Supported/requirement:** Evaluate mode does not enforce protection; keep existing protection until the replacement is Active.
- **Proposed check, Requirement (not run):** Negative tests as in A: push to main, force push, bypass.

### B.p4: Security configs on all repos

Checked 5 November 2026. Corrected or qualified. Basis: SECURITY, LICENSE, BYPASS, CAMPAIGN.

- **Title, Label / proposed control:** Security configs on all repos
- **Description, Supported/requirement:** Apply security configurations to existing repositories and set defaults for new ones.
- **Description, Supported/requirement:** Enable licensed Code Security and Secret Protection features for private repositories as required by the baseline.
- **Description, Supported/requirement:** Some security features are free for public repositories on github.com; verify coverage and entitlements per feature.
- **Proposed check, Requirement (not run):** Create a repo in each org and confirm the baseline appears.

### B.p5: Approved Actions, read-only token

Checked 5 November 2026. Corrected or qualified. Basis: ACTIONS, SECURE.

- **Title, Label / proposed control:** Approved Actions, read-only token
- **Description, Supported/requirement:** Allow approved actions and reusable workflows.
- **Description, Supported/requirement:** Require action references to use full commit SHAs; this policy still permits reusable workflows by tag, so check their SHA pinning separately.
- **Description, Supported/requirement:** Set the default GITHUB_TOKEN to read contents and packages, grant extra permissions per job, and disable PR creation/approval.
- **Description, Supported/requirement:** Never execute untrusted contributor code in privileged pull_request_target or workflow_run contexts.
- **Proposed check, Requirement (not run):** Check that a workflow from a fork cannot read any secret.

### B.p6: PAT lifetimes bounded

Checked 5 November 2026. Corrected or qualified. Basis: TOKEN.

- **Title, Label / proposed control:** PAT lifetimes bounded
- **Description, Supported/requirement:** Set maximum permitted lifetimes separately for fine-grained and classic PATs, and require fine-grained scope approval.
- **Description, Supported/requirement:** Noncompliant member tokens are blocked from organization access, not revoked globally.
- **Description, Supported/requirement:** Review administrator exemptions and test their effects.
- **Description, Supported/requirement:** Public resources remain accessible.
- **Proposed check, Requirement (not run):** Test organization access using member tokens whose configured lifetime exceeds the limit, including a newly created token. Check administrator exemptions separately; token age alone is not the policy criterion.

### B.p7: Audit stream with source IP

Checked 5 November 2026. Retained after review. Basis: AUDIT, STREAM, IP.

- **Title, Label / proposed control:** Audit stream with source IP
- **Description, Supported/requirement:** Audit and Git events stream to B's own archive.
- **Description, Supported/requirement:** Activity by a personal account outside organization resources is not fully visible, and public activity has source-IP gaps.
- **Description, Supported/requirement:** Correlate with endpoint and network evidence.
- **Description, Supported/requirement:** GitHub keeps Git events for only 7 days, so the stream must run from day one.
- **Proposed check, Requirement (not run):** Trigger a test event and find it in the archive.

### B.p8: Reconcile SAML + SCIM in every org

Checked 5 November 2026. Retained after review. Basis: SAML, SCIM.

- **Title, Label / proposed control:** Reconcile SAML + SCIM in every org
- **Description, Supported/requirement:** A scheduled job compares IdP groups with the members and linked identities of every organization.
- **Description, Supported/requirement:** It reports drift, and any org without SAML enforced.
- **Proposed check, Requirement (not run):** Add a test org without SAML. The job should flag it.

### B.p9: Custom properties on every repo

Checked 5 November 2026. Retained after review. Basis: PROPERTIES, RULES.

- **Title, Label / proposed control:** Custom properties on every repo
- **Description, Supported/requirement:** Every repo carries properties such as system, class and owner.
- **Description, Supported/requirement:** Rulesets can target repos by custom property.
- **Proposed check, Requirement (not run):** List repos with a missing property. The list should be empty.

### B.p10: Orgs by class, open source apart

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Orgs by class, open source apart
- **Description, Requirement:** Organizations follow classification and need-to-know.
- **Description, Requirement:** Open source work has its own organization with its own owners and release approvers.
- **Proposed check, Requirement (not run):** Confirm no public repo lives outside public-open-source.

### B.p11: Sandbox org, private only

Checked 5 November 2026. Corrected or qualified. Basis: ARCHIVE.

- **Title, Label / proposed control:** Sandbox org, private only
- **Description, Supported/requirement:** sandbox-lab is the place for experiments.
- **Description, Supported/requirement:** It is private only, holds no secrets or internal data, and is archived when unused.
- **Description, Supported/requirement:** This design puts unclassified experiments in B, not A.
- **Proposed check, Requirement (not run):** List sandbox-lab repos with no activity for 90 days. They should be archived.

### B.p12: Keep per-org SAML and org SCIM

Checked 5 November 2026. Corrected or qualified. Basis: SAML, SCIM, SWITCH.

- **Title, Label / proposed control:** Keep per-org SAML and org SCIM
- **Description, Supported/requirement:** Enterprise-level SAML would remove organization SCIM, and GitHub has no SCIM for a personal-account enterprise.
- **Description, Supported/requirement:** So B keeps SAML and SCIM per organization.
- **Description, Supported/requirement:** This is a design choice.
- **Proposed check, Requirement (not run):** Confirm every org shows SAML enforced and SCIM active.

### B.p13: Agents and AI, reviewed models only

Checked 5 November 2026. Corrected or qualified. Basis: AGENT, FIREWALL, THIRD.

- **Title, Label / proposed control:** Agents and AI, reviewed models only
- **Description, Supported/requirement:** Pilot approved Copilot and agent features in selected organizations.
- **Description, Supported/requirement:** Third-party coding agents require enterprise enablement before organization enablement.
- **Description, Supported/requirement:** Require reviewed models, MCP integrations, PR protections and code-owner review of agent configuration.
- **Description, Supported/requirement:** Assess each execution environment and enforce spending controls; a cloud-agent firewall alone does not cover MCP processes or setup steps.
- **Proposed check, Requirement (not run):** Open an agent pull request that edits a workflow file. Expected: it will need a code-owner review. Record the result.

### B.p14: Scoped roles, review security-manager access

Checked 5 November 2026. Corrected or qualified. Basis: ROLE, PRIVILEGES.

- **Title, Label / proposed control:** Scoped roles, review security-manager access
- **Description, Supported/requirement:** Delegate organization duties with security manager or custom roles instead of broad Admin where suitable.
- **Description, Supported/requirement:** Security manager includes read access to every repository in its organization, so assign it only within an approved compartment.
- **Description, Supported/requirement:** This design requires two owners per organization, no Admin base permission, named app managers and a short enterprise-owner list.
- **Proposed check, Requirement (not run):** List users with Admin on any repo. Each one should have a recorded reason.

### B.p15: Dependency and provenance controls

Checked 5 November 2026. Corrected or qualified. Basis: DEPENDENCY, DEPENDABOT, ATTEST, NPM, PYPI.

- **Title, Label / proposed control:** Dependency and provenance controls
- **Description, Supported/requirement:** Require dependency review checks, lockfiles and disabled install-time lifecycle scripts where supported.
- **Description, Supported/requirement:** Use OIDC trusted publishing where supported, including npm and PyPI.
- **Description, Supported/requirement:** npm requires GitHub-hosted runners; its automatic provenance is limited to public packages from public repositories and can be disabled.
- **Description, Supported/requirement:** Verify release provenance separately.
- **Description, Supported/requirement:** Use Dependabot for supported package and action updates.
- **Proposed check, Requirement (not run):** Add a dependency with a known advisory in a PR. The check should block it.

### B.p16: Shared workflow platform

Checked 5 November 2026. Corrected or qualified. Basis: REUSE, ACTIONS.

- **Title, Label / proposed control:** Shared workflow platform
- **Description, Supported/requirement:** Approved workflows and actions live in one dedicated organization in B, owned by a platform team, with versions, changelog, code owners and required reviews.
- **Description, Supported/requirement:** Public CI reuses only workflows without deployment grants.
- **Description, Supported/requirement:** B has its own copy and never reads A.
- **Proposed check, Requirement (not run):** Change a shared workflow without a code-owner review. Expected: it is blocked. Record the result.

### A.o1: critical-system-a

Checked 5 November 2026. Corrected or qualified. Basis: PRIVILEGES, ROLE, RUNNER.

- **Title, Label / proposed control:** critical-system-a
- **Description, Supported/requirement:** One organization per critical system.
- **Description, Supported/requirement:** Teams come from IdP groups and base access is none, so people only see what they are granted.
- **Description, Supported/requirement:** It has its own runner group, and only approved GitHub Apps are installed.
- **Proposed check, Requirement (not run):** Test a non-owner member with no team, direct or organization-wide role grant. They must not read private repositories; public organization metadata can remain visible.
- **Chip, proposed control:** Teams from IdP, base none
- **Chip, proposed control:** Own runner group, apps approved

### A.o1.src: source (private)

Checked 5 November 2026. Retained after review. Basis: AVAILABLE, OWNERS, PUSH.

- **Title, Label / proposed control:** source (private)
- **Summary, Label / proposed control:** 2+ approvals, CODEOWNERS, signed commits, push protection.
- **Description, Supported/requirement:** Source repos hold the code.
- **Description, Supported/requirement:** Two approvals and CODEOWNERS review, signed commits, push protection, a SECURITY.md and the secure coding standard apply.
- **Description, Supported/requirement:** CODEOWNERS enforces nothing by itself: the ruleset must require the review.
- **Proposed check, Requirement (not run):** Open a PR that changes a CODEOWNERS path with one approval. Expected: it will not merge. Record the result.

### A.o1.iac: infrastructure as code

Checked 5 November 2026. Retained after review. Basis: ENV, OIDC.

- **Title, Label / proposed control:** infrastructure as code
- **Summary, Label / proposed control:** IaC policy checks, protected environments, plan review.
- **Description, Supported/requirement:** IaC repos run policy checks and plan review before a protected environment approves a deploy.
- **Description, Supported/requirement:** State and plans that contain secrets never live in Git.
- **Description, Supported/requirement:** State is encrypted in the approved backend with locking.
- **Proposed check, Requirement (not run):** Search the repo history for state files and plan output. There should be none.

### A.o2: critical-system-b

Checked 5 November 2026. Retained after review. Basis: RUNNER.

- **Title, Label / proposed control:** critical-system-b
- **Description, Supported/requirement:** A second critical system with its own owners, security leads and runner group.
- **Description, Supported/requirement:** Its credentials and teams are not shared with critical-system-a.
- **Proposed check, Requirement (not run):** Check that no team or app has access to both system organizations without a recorded reason.
- **Chip, proposed control:** Own owners and security leads
- **Chip, proposed control:** Own runner group

### A.o2.src: source (private)

Checked 5 November 2026. Retained after review. Basis: AVAILABLE, OWNERS.

- **Title, Label / proposed control:** source (private)
- **Summary, Label / proposed control:** Same baseline, system-specific CODEOWNERS.
- **Description, Supported/requirement:** Same baseline as the other system, with CODEOWNERS that name this system's reviewers.
- **Proposed check, Requirement (not run):** As for the first system.

### A.o2.iac: infrastructure as code

Checked 5 November 2026. Corrected or qualified. Basis: ENV, OIDC.

- **Title, Label / proposed control:** infrastructure as code
- **Summary, Label / proposed control:** Same checks, separate state and environments.
- **Description, Supported/requirement:** Apply the same checks with separate state, protected environments and credentials.
- **Description, Inference:** [inference] Separate state and environment names alone do not isolate systems; backend access controls and deployment trust policies must reject the other system.
- **Proposed check, Requirement (not run):** Try to point this repo's pipeline at the other system's state. Expected: it is refused. Record the result.

### A.o3: platform-security

Checked 5 November 2026. Corrected or qualified. Basis: ROLE, REUSE, RUNNER.

- **Title, Label / proposed control:** platform-security
- **Description, Supported/requirement:** Holds shared tooling and policy automation.
- **Description, Supported/requirement:** Do not grant platform-team members blanket read access to system repositories.
- **Description, Inference:** [inference] Policy credentials, reusable workflows and runner administration can still affect system code or builds; scope those privileges and review platform changes as a supply-chain trust path.
- **Proposed check, Requirement (not run):** Review human and automation grants separately, including security-manager roles, app permissions, reusable workflows and runner administration.
- **Chip, proposed control:** Shared tooling, policy as code
- **Chip, proposed control:** No blanket read to systems

### A.o3.pol: policy-as-code

Checked 5 November 2026. Retained after review. Basis: RULES.

- **Title, Label / proposed control:** policy-as-code
- **Summary, Label / proposed control:** Changes reviewed by security, two approvals.
- **Description, Supported/requirement:** Settings and rules as code.
- **Description, Supported/requirement:** Changes need two approvals including security, and the result is compared with live settings to catch drift.
- **Proposed check, Requirement (not run):** Change a live setting by hand. The drift check should flag it.

### A.o3.tool: shared-tooling

Checked 5 November 2026. Retained after review. Basis: REUSE.

- **Title, Label / proposed control:** shared-tooling
- **Summary, Label / proposed control:** Pinned, signed and reviewed before builds use it.
- **Description, Supported/requirement:** Shared actions and tools used by builds are pinned to commits, signed and reviewed before any system uses them.
- **Description, Supported/requirement:** Imports from outside enter here through the intake path.
- **Proposed check, Requirement (not run):** Check that builds reference tools by commit, not by tag.

### B.o1: internal-engineering

Checked 5 November 2026. Corrected or qualified. Basis: PRIVILEGES, ROLE.

- **Title, Label / proposed control:** internal-engineering
- **Description, Supported/requirement:** Internal work.
- **Description, Supported/requirement:** Repos are private with explicit team grants and base access none.
- **Description, Supported/requirement:** It has an internal runner group.
- **Proposed check, Requirement (not run):** Test a non-owner member with no team, direct or organization-wide role grant. They must not read private repositories; public organization metadata can remain visible.
- **Chip, proposed control:** Team grants, base access none
- **Chip, proposed control:** Internal runner group

### B.o1.app: internal-app

Checked 5 November 2026. Corrected or qualified. Basis: PUSH, OWNERS.

- **Title, Label / proposed control:** internal-app
- **Summary, Label / proposed control:** PR review, CODEOWNERS, secret protection, pinned action refs.
- **Description, Supported/requirement:** Internal application code.
- **Description, Supported/requirement:** PR review, CODEOWNERS, secret protection and pinned action references apply.
- **Proposed check, Requirement (not run):** Push a safe test fixture matching a supported push-protection pattern. Expect a block when coverage and bypass settings apply. Record the result; arbitrary secret strings are not guaranteed to be detected.

### B.o1.tools: internal-tools

Checked 5 November 2026. Corrected or qualified. Basis: SAML, EMU.

- **Title, Label / proposed control:** internal-tools
- **Summary, Label / proposed control:** Private only. GitHub internal visibility not used.
- **Description, Supported/requirement:** Use private visibility with explicit grants.
- **Description, Supported/requirement:** GitHub internal visibility grants read access broadly to enterprise members, with exceptions such as managed guest collaborators.
- **Description, Supported/requirement:** With organization-level SAML, members need not authenticate through SAML to access internal repositories.
- **Description, Supported/requirement:** Private visibility is the design choice here.
- **Proposed check, Requirement (not run):** Confirm no repo in B uses the internal visibility value.

### B.o2: public-open-source

Checked 5 November 2026. Corrected or qualified. Basis: SAML.

- **Title, Label / proposed control:** public-open-source
- **Description, Supported/requirement:** The only organization where this design permits public repositories.
- **Description, Supported/requirement:** Name release approvers.
- **Description, Supported/requirement:** Public contributions do not require corporate SSO; access to non-public resources requires separate approved grants.
- **Proposed check, Requirement (not run):** List repos with public visibility. All of them belong to this org.
- **Chip, proposed control:** Only place public repos live
- **Chip, proposed control:** Named release approvers

### B.o2.proj: public-project

Checked 5 November 2026. Corrected or qualified. Basis: NPM, PYPI.

- **Title, Label / proposed control:** public-project
- **Summary, Label / proposed control:** Release review. History and artifacts checked before publishing.
- **Description, Supported/requirement:** Check history, artifacts, metadata and logs before publishing.
- **Description, Supported/requirement:** Content from A requires approved transfer.
- **Description, Supported/requirement:** npm and PyPI support OIDC trusted publishing.
- **Description, Supported/requirement:** For GitHub Actions, npm requires GitHub-hosted runners; automatic npm provenance applies to public packages built from public repositories and can be disabled.
- **Description, Supported/requirement:** Verify provenance rather than assuming authentication supplies it.
- **Proposed check, Requirement (not run):** Run a secret and metadata scan over the full history before the first public release.

### B.o2.pr: untrusted pull requests

Checked 5 November 2026. Corrected or qualified. Basis: FORK, HOSTED, SECURE.

- **Title, Label / proposed control:** untrusted pull requests
- **Summary, Label / proposed control:** Treated as hostile. No secrets, no internal runners.
- **Description, Supported/requirement:** Pull requests from outside run on separate hosted runners without deployment grants.
- **Description, Supported/requirement:** No secrets, no route to internal runners, registries or targets.
- **Proposed check, Requirement (not run):** Open a fork PR that tries to print a secret. Expected: it will get none. Record the result.

### B.o3: sandbox-lab

Checked 5 November 2026. Corrected or qualified. Basis: SAML, SCIM.

- **Title, Label / proposed control:** sandbox-lab
- **Description, Supported/requirement:** The place for experiments in this design.
- **Description, Supported/requirement:** Private only, no public repos, SAML enforced and SCIM configured like every other org.
- **Description, Supported/requirement:** It holds no secrets or internal data.
- **Proposed check, Requirement (not run):** Search the org for secrets and internal data. There should be none.
- **Chip, proposed control:** Private only, no public repos
- **Chip, proposed control:** SAML enforced, SCIM configured

### B.o3.exp: experiments

Checked 5 November 2026. Corrected or qualified. Basis: ARCHIVE.

- **Title, Label / proposed control:** experiments
- **Summary, Label / proposed control:** No secrets or internal data. Archived when unused.
- **Description, Supported/requirement:** Throwaway work.
- **Description, Supported/requirement:** No secrets and no internal data.
- **Description, Supported/requirement:** Archived when unused, and review remaining access separately.
- **Proposed check, Requirement (not run):** List repos with no activity for 90 days. They should be archived.

### B.o3.part: Partners recertified

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Partners recertified
- **Summary, Label / proposed control:** Own review cycle, scoped publisher roles.
- **Description, Requirement:** Partners are recertified on their own review cycle, with scoped roles and an expiry.
- **Proposed check, Requirement (not run):** List partner grants without an expiry date. There should be none.

### A.e1: Ephemeral runners

Checked 5 November 2026. Corrected or qualified. Basis: RUNNER, AZURE, SECURE.

- **Title, Label / proposed control:** Ephemeral runners
- **Summary, Label / proposed control:** Per-system pool, egress allow list.
- **Description, Supported/requirement:** Require disposable runners per system or trust level, selected repository/workflow access, restricted repository-level runner creation, patched images, removed disks/caches and controlled egress.
- **Description, Supported/requirement:** For private network access, assess self-hosted ephemeral runners or supported Linux/Windows GitHub-hosted larger runners with Azure private networking.
- **Description, Supported/requirement:** Neither runner groups nor disposal alone isolate untrusted code.
- **Proposed check, Requirement (not run):** Run a job that tries to reach a host outside the allow list.

### A.e2: Vault and OIDC

Checked 5 November 2026. Corrected or qualified. Basis: OIDC.

- **Title, Label / proposed control:** Vault and OIDC
- **Summary, Label / proposed control:** Short-lived tokens, rejects B.
- **Description, Supported/requirement:** Use short-lived OIDC deployment credentials.
- **Description, Supported/requirement:** On github.com, configure the enterprise-specific issuer and require the exact issuer, audience and approved repository/environment subject in target trust policies.
- **Description, Supported/requirement:** Match enterprise claims where supported, or encode required constraints in the subject.
- **Description, Supported/requirement:** Cloud-provider claim support varies.
- **Description, Supported/requirement:** Test rejection of B identities and unapproved A repositories.
- **Proposed check, Requirement (not run):** Use an identity from B to deploy to A. It must fail.

### A.e3: Private registry

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Private registry
- **Summary, Label / proposed control:** Signed artifacts, SBOM, mirror.
- **Description, Requirement:** Signed artifacts with an SBOM, and a mirror of approved dependencies.
- **Description, Requirement:** Builds in A pull from the mirror, not from the open internet.
- **Description, Requirement:** Provenance attestations are verified before a deploy, and the attestation bundle is kept with the artifact.
- **Proposed check, Requirement (not run):** Try to build with a dependency that is not on the mirror.

### B.e1: Internal CI pool

Checked 5 November 2026. Retained after review. Basis: RUNNER, SECURE.

- **Title, Label / proposed control:** Internal CI pool
- **Summary, Label / proposed control:** Own runners, own credentials.
- **Description, Supported/requirement:** Self-hosted runners for internal work, with their own credentials, separate from A and from public CI.
- **Proposed check, Requirement (not run):** Check that internal runners are not reachable from public pull requests.

### B.e2: Public CI, isolated

Checked 5 November 2026. Corrected or qualified. Basis: FORK, HOSTED, SECURE.

- **Title, Label / proposed control:** Public CI, isolated
- **Summary, Label / proposed control:** Hosted runners, no secrets.
- **Description, Supported/requirement:** Run public fork PRs on separate GitHub-hosted workers with a read-only job token, no deployment secrets and no private-network connection.
- **Description, Supported/requirement:** Hosted runner users can have OS administrator privileges; isolation depends on separate workers, network routing and absent credentials.
- **Proposed check, Requirement (not run):** Open a fork PR and confirm it cannot read secrets or reach internal hosts.

### B.e3: Vault and OIDC

Checked 5 November 2026. Retained after review. Basis: OIDC.

- **Title, Label / proposed control:** Vault and OIDC
- **Summary, Label / proposed control:** B targets only, rejects A.
- **Description, Supported/requirement:** Short-lived OIDC identity for B targets only.
- **Description, Supported/requirement:** B targets reject identities from A.
- **Proposed check, Requirement (not run):** Use an identity from A to deploy to B. It must fail.

### A.v1: Audit and security events

Checked 5 November 2026. Corrected or qualified. Basis: AUDIT, STREAM, IP, WEBHOOK.

- **Title, Label / proposed control:** Audit and security events
- **Summary, Label / proposed control:** Git, alerts, IdP, proxy, EDR.
- **Description, Supported/requirement:** Audit and Git events, security alerts through supported APIs or webhooks, IdP and privileged-access logs, proxy, endpoint and runner telemetry.
- **Description, Supported/requirement:** Webhook receivers validate signatures and handle replays and duplicates.
- **Proposed check, Requirement (not run):** Trigger a test alert and follow it to the archive.

### A.v2: Collector and archive

Checked 5 November 2026. Retained after review. Basis: AUDIT, STREAM.

- **Title, Label / proposed control:** Collector and archive
- **Summary, Label / proposed control:** Immutable store, lag monitoring.
- **Description, Supported/requirement:** Events go to an immutable archive in the sensitive zone.
- **Description, Supported/requirement:** Ingestion lag and stream health are monitored, expected sources are reconciled, and events are deduplicated.
- **Description, Supported/requirement:** Do not rely on GitHub's short native Git-event retention.
- **Proposed check, Requirement (not run):** Stop the collector. Someone should be alerted.

### A.v3: Sensitive SIEM and SOC

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Sensitive SIEM and SOC
- **Summary, Label / proposed control:** Cleared analysts only.
- **Description, Requirement:** Detailed sensitive logs stay in the sensitive zone, with cleared analysts only.
- **Proposed check, Requirement (not run):** Check that analyst access is limited to cleared staff.

### B.v1: Audit and security events

Checked 5 November 2026. Corrected or qualified. Basis: AUDIT, STREAM, IP.

- **Title, Label / proposed control:** Audit and security events
- **Summary, Label / proposed control:** Git, alerts, IdP, proxy, CI.
- **Description, Supported/requirement:** Audit and Git events, security alerts, IdP and proxy logs, CI and registry telemetry.
- **Proposed check, Requirement (not run):** Trigger a test alert and follow it to the archive.

### B.v2: Collector and archive

Checked 5 November 2026. Retained after review. Basis: STREAM.

- **Title, Label / proposed control:** Collector and archive
- **Summary, Label / proposed control:** Immutable store, lag monitoring.
- **Description, Supported/requirement:** Events go to B's own immutable archive.
- **Description, Supported/requirement:** Lag and stream health are monitored, and expected sources are reconciled.
- **Proposed check, Requirement (not run):** Stop the collector. Someone should be alerted.

### B.v3: Domain B SIEM and SOC

Checked 5 November 2026. Retained after review. Basis: IP.

- **Title, Label / proposed control:** Domain B SIEM and SOC
- **Summary, Label / proposed control:** Do not claim full visibility of public activity. (Reworded 5 Nov 2026 to a requirement; the visibility limit is sourced in the description.)
- **Description, Supported/requirement:** A SIEM and SOC for domain B.
- **Description, Supported/requirement:** Activity in public resources and personal-account activity outside organization resources are only partly visible.
- **Description, Supported/requirement:** Do not claim full observation.
- **Proposed check, Requirement (not run):** Document which activities in B the SIEM cannot see.

### L.a: A · Sensitive

Checked 5 November 2026. Retained after review. Basis: ENV, OIDC, ATTEST.

- **Title, Label / proposed control:** A · Sensitive
- **Description, Supported/requirement:** Code reaches a classified target only through an approved PR, an isolated ephemeral runner, required checks, a signed artifact, an approval on a protected environment and a short-lived OIDC identity.
- **Description, Supported/requirement:** Targets reject identities from B.
- **Proposed check, Requirement (not run):** Try to deploy by skipping a step. Each step should block.
- **Step, requirement:** Approved PR
- **Step, requirement:** Isolated CI
- **Step, requirement:** Checks
- **Step, requirement:** Signed artifact
- **Step, requirement:** Env approval
- **Step, requirement:** Protected target

### L.brel: B · Release

Checked 5 November 2026. Retained after review. Basis: ENV, ATTEST.

- **Title, Label / proposed control:** B · Release
- **Description, Supported/requirement:** Public and internal releases come from a reviewed commit, a trusted build, checks, a signed release and a release approval, then deploy to B targets only.
- **Proposed check, Requirement (not run):** Try to publish a release without the approval.
- **Step, requirement:** Reviewed commit
- **Step, requirement:** Trusted build
- **Step, requirement:** Checks
- **Step, requirement:** Signed release
- **Step, requirement:** Release approval
- **Step, requirement:** B target

### L.bpr: B · Untrusted PR

Checked 5 November 2026. Corrected or qualified. Basis: FORK, HOSTED, SECURE.

- **Title, Label / proposed control:** B · Untrusted PR
- **Description, Supported/requirement:** Pull requests from outside are treated as hostile.
- **Description, Supported/requirement:** They run without deployment grants and only report status back.
- **Description, Supported/requirement:** No secrets and no route to internal or sensitive systems.
- **Proposed check, Requirement (not run):** Use a fork PR to try reading a deployment secret and reaching controlled internal test endpoints. Expected: both fail. Standard hosted runners still have public internet access; record results.
- **Step, requirement:** Public PR
- **Step, requirement:** Isolated CI
- **Step, requirement:** Status only
- **Lane note, requirement:** No secrets. No route to internal or sensitive systems.

### L.exp: Export A → B

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Export A → B
- **Description, Requirement:** Content leaves A only after a release request and a decision by the release authority.
- **Description, Requirement:** It is inspected, minimised and signed, staged, and published in B.
- **Description, Requirement:** Scanning alone cannot declassify information.
- **Proposed check, Requirement (not run):** Request an export without the authority's decision. Expected: it is blocked. Record the result.
- **Step, requirement:** Release request
- **Step, requirement:** Release authority
- **Step, requirement:** Inspect
- **Step, requirement:** Minimize and sign
- **Step, requirement:** Stage
- **Step, requirement:** Publish in B

### L.imp: Intake B → A

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Intake B → A
- **Description, Requirement:** Outside content enters A through a mirror.
- **Description, Requirement:** Origin is verified, content is quarantined and scanned for malware and licence issues, versions are pinned, then it is admitted to the approved mirror and used in A.
- **Proposed check, Requirement (not run):** Import a package with a known bad hash. Expected: it will be stopped in quarantine. Record the result.
- **Step, requirement:** Upstream source
- **Step, requirement:** Verify origin
- **Step, requirement:** Quarantine
- **Step, requirement:** Scan and pin
- **Step, requirement:** Admit to mirror
- **Step, requirement:** Use in A

### L.ir: Incident response

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Incident response
- **Description, Requirement:** Detect, contain, rotate credentials and preserve evidence, recover, then learn.
- **Description, Requirement:** Exercises cover the cases where the IdP, the collector or GitHub itself is the problem.
- **Proposed check, Requirement (not run):** Run a tabletop exercise on a leaked token and on an IdP outage.
- **Step, requirement:** Detect
- **Step, requirement:** Contain
- **Step, requirement:** Rotate, preserve
- **Step, requirement:** Recover
- **Step, requirement:** Learn

### ops.1: Inventory: owner, class, retention

Checked 5 November 2026. Retained after review. Basis: PROPERTIES.

- **Title, Label / proposed control:** Inventory: owner, class, retention
- **Description, Supported/requirement:** Every repo has an owner, a class and a retention rule, kept in custom properties and checked for gaps.

### ops.2: Policy as code, drift checks

Checked 5 November 2026. Retained after review. Basis: REPO.

- **Title, Label / proposed control:** Policy as code, drift checks
- **Description, Supported/requirement:** Enterprise and organization settings live in code.
- **Description, Supported/requirement:** A scheduled job reports any setting that has drifted.

### ops.3: Back up Git, LFS, issues, packages

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Back up Git, LFS, issues, packages
- **Description, Requirement:** Backups cover Git history, LFS, issues, packages and settings.
- **Description, Requirement:** Check what the tool really restores.

### ops.4: Tested restore, RPO and RTO

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Tested restore, RPO and RTO
- **Description, Requirement:** Restores are tested, with recovery point and recovery time targets agreed with each system owner.

### ops.5: Reconcile groups, keys, apps

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Reconcile groups, keys, apps
- **Description, Requirement:** Review IdP groups, deploy keys, app installations, webhooks and outside collaborators on a schedule.

### ops.6: Patch and attest runners

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Patch and attest runners
- **Description, Requirement:** Runner images are patched on a schedule, and their state is attested.

### ops.7: Protect IaC state and plans

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Protect IaC state and plans
- **Description, Requirement:** State and plans are encrypted, locked, and reachable only by the pipeline that needs them.

### ops.8: Test collector, stream, IdP outage

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Test collector, stream, IdP outage
- **Description, Requirement:** Regularly break the log collector, the audit stream and the IdP, and check that people notice and recover.

### ops.9: Access reviews, pen tests, evidence

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Access reviews, pen tests, evidence
- **Description, Requirement:** Access is recertified on a schedule.
- **Description, Requirement:** Pen tests and compliance audits produce evidence that is kept.

### ops.10: Review org model, archive stale orgs

Checked 5 November 2026. Retained after review. Basis: ARCHIVE.

- **Title, Label / proposed control:** Review org model, archive stale orgs
- **Description, Supported/requirement:** Organizations are reviewed against classification and need-to-know.
- **Description, Supported/requirement:** Stale organizations are archived.

### ops.11: Training and security champions

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Training and security champions
- **Description, Requirement:** Developers get secure coding training.
- **Description, Requirement:** Champions inside teams carry the secure coding standard.

### ops.12: Threat model upkeep per system

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Threat model upkeep per system
- **Description, Requirement:** Threat models are reviewed whenever a system changes, and after incidents.

### ops.13: Continuity mirror, rehearsed

Checked 5 November 2026. Corrected or qualified. Basis: Design definition on this page.

- **Title, Label / proposed control:** Continuity mirror, rehearsed
- **Description, Requirement:** For critical systems, a copy of deployable revisions sits in a separate failure domain, with its own credentials and build path.
- **Description, Requirement:** Deployment logic lives in scripts, not only in workflow files, and a separate identity can deploy without GitHub Actions.
- **Description, Requirement:** Drills run with the primary blocked, and recovery after an erroneous force push is tested too.
- **Description, Requirement:** Break-glass credentials are short-lived.

### ops.14: Metrics and developer feedback

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Metrics and developer feedback
- **Description, Requirement:** Track CI duration, queue time and flake rate, plus alert age and time to fix.
- **Description, Requirement:** Developers have a channel to report friction and ask for exceptions, and the answers feed back into the baseline.

### ops.15: Onboarding, knowledge base, champions

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Onboarding, knowledge base, champions
- **Description, Requirement:** New engineers get a short path: tools, review rules, how to report a finding.
- **Description, Requirement:** One knowledge repository holds the standards and how-tos.
- **Description, Requirement:** Discussions are on for questions, so answers stay next to the code.
- **Description, Requirement:** A champion in each team keeps the practice alive.
- **Description, Requirement:** A and B keep separate copies, and the A copy never lists classified detail in B.

### acc.1: Security authority: classification, hosting, export

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Security authority: classification, hosting, export
- **Description, Requirement:** Decides classification, approves the hosting service, and owns export decisions.

### acc.2: Enterprise owners: baseline, audit delivery

Checked 5 November 2026. Corrected or qualified. Basis: ROLE, AGENT.

- **Title, Label / proposed control:** Enterprise owners: baseline, audit delivery
- **Description, Supported/requirement:** Own the enterprise baseline and make sure audit data is delivered.
- **Description, Supported/requirement:** Keep a short named owner list.
- **Description, Supported/requirement:** Delegate through suitable enterprise roles such as AI manager.
- **Description, Supported/requirement:** Security manager is an organization role and includes read access to all its repositories.

### acc.3: Org owners: teams, apps, runners

Checked 5 November 2026. Retained after review. Basis: RUNNER.

- **Title, Label / proposed control:** Org owners: teams, apps, runners
- **Description, Supported/requirement:** Own organization teams, installed apps and runner groups.

### acc.4: Repo owners: review, remediation, deploys

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Repo owners: review, remediation, deploys
- **Description, Requirement:** Own code review, remediation of findings and deployments for their repo.

### acc.5: SOC: detection, response, evidence

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** SOC: detection, response, evidence
- **Description, Requirement:** Own detection and response, and keep the evidence.

### acc.6: Governance: exceptions, vendor review, exercises

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Governance: exceptions, vendor review, exercises
- **Description, Requirement:** Grant exceptions with an expiry, review vendors and apps, and run exercises.

### acc.7: System security leads: threat model

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** System security leads: threat model
- **Description, Requirement:** Own the threat model of their system and keep it current.

### acc.8: Champions: training, coding standard

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Champions: training, coding standard
- **Description, Requirement:** Run training and maintain the secure coding standard.

### acc.9: Compliance: audits, access reviews

Checked 5 November 2026. Retained after review. Basis: Design definition on this page.

- **Title, Label / proposed control:** Compliance: audits, access reviews
- **Description, Requirement:** Run compliance audits and access reviews and keep the results.

## Design-choice explanations

- **1, design requirement with documented capabilities above:** B uses personal accounts with SAML and SCIM per organization to retain membership provisioning. Enterprise SAML does not support organization SCIM. Evidence row DEV.1; verdict: documented.
- **2, design requirement with documented capabilities above:** A has no sandbox. Unclassified experiments run in the private sandbox-lab organization in B. This is a design choice.
- **3, design requirement with documented capabilities above:** Private visibility supports explicit grants. Internal visibility grants broad enterprise-member read access, subject to guest-collaborator exceptions. Organization SAML does not require authentication for internal repositories. Evidence rows DEV.3 (three quotes) in the evidence table; verdict: documented.
- **4, design requirement with documented capabilities above:** Private CI requires assessed private-network runners and separate credentials. Azure private networking for hosted runners is available only for larger Ubuntu and Windows runners. Where assessed, use them as an alternative to self-hosted runners. Evidence row DEV.4 covers the first sentence; the second is a design requirement. Public fork PRs use separate hosted workers.
## Flow summaries

- **build, design requirement with documented capabilities above:** Code reaches a protected target. A and B must use separate runners, identities and targets.
- **untrusted, design requirement with documented capabilities above:** Public fork pull requests must run without deployment grants: no secrets and no route to internal or sensitive systems.
- **export, design requirement with documented capabilities above:** A to B only through the approved transfer service, after the release authority decides.
- **intake, design requirement with documented capabilities above:** B to A only after verification, quarantine, scanning and pinning.
- **respond, design requirement with documented capabilities above:** Detect, contain, rotate, recover, learn. Logs must stay in each domain. The common SOC may see only minimized metadata.

## Validation

- Browser: headless Google Chrome, local HTML, 5 November 2026. All 106 boxes opened and closed, and all 16 filter buttons activated without failures. Rapid synthetic hash updates initially hit browser history throttling; repeating at normal interaction speed passed without a page change.
- Light and dark mode at 1568px and 375px inspected. Document width never exceeded viewport width. At 375px the diagram stacks vertically and does not require sideways scrolling.
- A fresh saved link to `#n=B.p15` opened the right popover at 375px, inside the viewport. Escape closed it, cleared the selection hash and restored focus to its box.
- No browser runtime exceptions or error-level console/log entries. All rendered popover paragraphs are within 60 words. Source links appear beside relevant claims.
- Static checks: all 106 original node IDs preserved; every title, summary, description sentence and proposed check appears in this ledger. Local index links resolve, the AI note matches the reference page, and edited files contain no em or en dashes.
- No build step exists for this hand-written HTML site. JavaScript parsing and browser execution passed. Final diff checked for scope, whitespace, accidental changes and secrets.
- Per-claim evidence, 5 November 2026: the verifier passed (62 sourced, 12 inference, 256 design requirement or label sentences; 90 quotes against 33 pages) and a deliberately broken quote made it fail. Paced click test: 106 boxes and 414 Part of and Related links, 0 failures. Real mouse clicks, saved `#n=` and `#f=` links, and one text-fragment highlight in Chrome were checked. Contrast and page width were read from computed styles at 332 px in light and dark. Not tested: Firefox and Safari. Details are in the decisions note.
- Nothing was tested on a real GitHub tenant. The earlier draw.io versions were not rechecked.

## Per-claim evidence (5 November 2026)

- Each sourced fact in a popup description, and in the four design-choice notes (DEV.1 to DEV.4), has a row in `github-two-enterprise-interactive.evidence.tsv` with the sentence start, a source from that box's list and a verbatim quote. The page shows the quote and a link that opens the source at the passage. Inference sentences carry an "[inference]" label on the page.
- Mechanical check: `node github/verify-evidence.mjs` fetched each source and found every quote word for word. Result on 5 November 2026: 62 sourced facts, 12 inferences, 256 design requirement or label sentences; 90 quotes checked against 33 pages; OK. A deliberately corrupted quote and a stale inline copy both made the script fail.
- Rewordings made so the sentence no longer goes beyond its source: standard GitHub Enterprise Cloud on github.com (was "multi-tenant SaaS"); Ubuntu/Windows runners; SCIM deprovisioning suspends the account and does not delete it; the PAT sentence no longer claims revocation of existing tokens or SSH keys; four "Proposed check" texts reduced to test steps; the push-protection limit is now a sourced description sentence.
- Not verified: that Chrome, Firefox and Safari highlight the passage from the text-fragment link. The quote is shown beside the link regardless.
- Summary lines, chips and check texts are design requirements or test steps. Where they repeat a documented fact, the sourced version is in the description of the same box.
