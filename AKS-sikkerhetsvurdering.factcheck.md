# AKS-sikkerhetsvurdering: fact check

Belongs to [AKS-sikkerhetsvurdering.html](AKS-sikkerhetsvurdering.html). Decisions: [AKS-sikkerhetsvurdering.decisions.md](AKS-sikkerhetsvurdering.decisions.md).

First checked 13 Nov 2026 and fully rechecked 24 Nov 2026 (see the section below). Each source page was fetched that day and the claim was compared with the page text. Four full passes were made. The second led to three added source entries. The third changed the control plane wording in two places and added the REST reference. The fourth read the final page again from the header to the end of the script, including the text the script builds, and found nothing to change. The stylesheet holds no reader text.

Round 9 (24 Nov 2026): the glossary entries on cluster tenancy, root versus privileged and base64 Secrets now link to concepts-security, the Pod Security Standards page and the Kubernetes Secrets page. The node-breakout line and the platform-team ownership line are tagged [inference]. Both audit halves found no wrong claims.

Round 10 (24 Nov 2026): fixed three items, each confirmed by a second persona against live pages. NetworkPolicy selects by pods, namespaces and IP blocks (kubernetes.io network-policies). Ubuntu 22.04 support ends 30 June 2027 (upgrade-os-version) and ACL FIPS needs AKS 1.34 or later (enable-fips-nodes). Pod Sandboxing is Azure Linux only, no Ubuntu, Windows or Azure Container Linux, no FIPS, Trusted Launch or Arm64, and the limits are listed under both kata-vm-isolation and kata-vm-isolation-v2 (use-pod-sandboxing); NAP is not supported with v2.

Round 11 (24 Nov 2026): the outbound control label no longer says it filters traffic, because the outbound type only sets how traffic leaves (egress-outboundtype). The IMDS bullet notes that Azure Policy is unsupported with IMDS restriction (imds-restriction) and that deployment safeguards need the Azure Policy add-on (deployment-safeguards); the combined effect is tagged [inference]. Three other items were rejected: the SSH wording matches concepts-security, the Ingress NGINX deadline wording is correct, and no other claim differed from its source.

Round 13 (25 Nov 2026): added five caveats, each confirmed by a second persona against live pages. Azure Policy: a Deny assignment does not stop pre-existing resources, and the add-on auto-excludes kube-system and gatekeeper-system (policy-for-kubernetes). Kubernetes: default-deny egress blocks DNS, node traffic is always allowed, hostNetwork behaviour is undefined (network-policies). AKS: Azure NPM ends on Windows 30 Sep 2026 and on Linux 30 Sep 2028, and policies might not process LoadBalancer traffic, so use loadBalancerSourceRanges (use-network-policies). Audit: the policy is AKS-managed and logs some reads at level None (monitor-aks). Defender: the sensor host OS list names Azure Linux 1.0 and 2.0 and Ubuntu up to 22.04 only, and most runtime features show Linux only, with exceptions such as advanced hunting and agentless malware detection (support-matrix-defender-for-containers). Rejected: a claim that an unset networkPolicy field means no enforcement, which the page does not state. The effect for newer OS versions is interpretation by AI.

## Claims and verdicts

| Claim on the page | Source | Verdict |
|---|---|---|
| OWASP 2025 names for K01 to K10. Supply chain was K02 in 2022 and has no item of its own in 2025. | [OWASP Kubernetes Top Ten](https://kubernetes-top10.owasp.org/) | Confirmed |
| Microsoft has a separate section on images and supply chain. | [secure-aks](https://learn.microsoft.com/en-us/azure/aks/secure-aks), section "Container image and supply chain security" | Confirmed |
| Platform support gives no Kubernetes security fixes and lasts 60 days. | [supported-kubernetes-versions](https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions): "Platform support gives you a 60-day grace period to upgrade on your own terms." | Confirmed |
| From 1 June 2027 AKS upgrades clusters left on an unsupported version, outside the maintenance window. | Same page: "Starting on June 1, 2027, AKS automatically upgrades any cluster that stays on an unsupported Kubernetes version after its 60-day platform support grace period ends." and "a platform-initiated upgrade doesn't follow your maintenance window" | Confirmed |
| Ingress NGINX project maintenance ended March 2026. | [Kubernetes blog, 11 Nov 2025](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/) | Confirmed |
| Microsoft supports critical security fixes for NGINX in application routing through November 2026. | [concepts-network-ingress](https://learn.microsoft.com/en-us/azure/aks/concepts-network-ingress): "Microsoft will provide official support for critical security patches for application routing add-on NGINX Ingress resources through November 2026." Also the [AKS blog](https://blog.aks.azure.com/2025/11/13/ingress-nginx-update). | Confirmed |
| Azure Linux 2.0: security support ended 30 Nov 2025, node image removal from 31 Oct 2026, scaling then fails. | [upgrade-os-version](https://learn.microsoft.com/en-us/azure/aks/upgrade-os-version): "Beginning on October 31, 2026, node images will be removed, and you'll be unable to scale your node pools." | Confirmed. The source still uses future tense after the date. |
| Pod-managed identity: deprecated 2022, add-on support ended September 2025. | [use-azure-ad-pod-identity](https://learn.microsoft.com/en-us/azure/aks/use-azure-ad-pod-identity) | Confirmed |
| Cluster User fetches the kubeconfig. Without Entra integration it equals Cluster Admin. | [control-kubeconfig-access](https://learn.microsoft.com/en-us/azure/aks/control-kubeconfig-access) | Confirmed |
| AKS RBAC Reader cannot read roles, bindings or Secrets. | [built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/containers#azure-kubernetes-service-rbac-reader) | Confirmed |
| Local accounts, `disableLocalAccounts`, certificate rotation to revoke old certificates. | [local-accounts](https://learn.microsoft.com/en-us/azure/aks/local-accounts) | Confirmed |
| Run Command reaches a private cluster through the Azure API. | [access-private-cluster](https://learn.microsoft.com/en-us/azure/aks/access-private-cluster) | Confirmed |
| Microsoft advises against cluster-admin for pipelines. | [concepts-security](https://learn.microsoft.com/en-us/azure/aks/concepts-security): "Avoid cluster-admin credentials." | Confirmed |
| Microsoft provides, manages and maintains the control plane components. Each cluster has its own control plane. | Same page: "the Kubernetes primary components are part of the managed service provided, managed, and maintained by Microsoft. Each AKS cluster has its own single-tenanted, dedicated Kubernetes primary". [monitor-aks](https://learn.microsoft.com/en-us/azure/aks/monitor-aks) lists "the API server, etcd, and the scheduler" as control plane components. | Confirmed. No source says Microsoft "hardens and patches" it, so the page no longer does. |
| API server is public by default. Authorized IP ranges limit it. An empty range turns the filter off. The `--query` path. | [api-server-authorized-ip-ranges](https://learn.microsoft.com/en-us/azure/aks/api-server-authorized-ip-ranges) | Confirmed |
| VNet integration alone does not make the API server private. | [api-server-vnet-integration](https://learn.microsoft.com/en-us/azure/aks/api-server-vnet-integration): supported "for public or private clusters" | Confirmed |
| IMDS restriction is preview and covers only pods without hostNetwork. | [imds-restriction](https://learn.microsoft.com/en-us/azure/aks/imds-restriction) | Confirmed |
| Cilium policies do not cover hostNetwork pods. | [azure-cni-powered-by-cilium](https://learn.microsoft.com/en-us/azure/aks/azure-cni-powered-by-cilium): "Network policies aren't applied to pods using host networking" | Confirmed |
| NetworkPolicy: both directions open by default, isolation is per direction, needs an enforcing plugin. | [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) | Confirmed |
| NAT Gateway gives outbound addresses and scale. Microsoft pairs it with Azure Firewall for traffic inspection. | [secure-nat-gateway](https://learn.microsoft.com/en-us/azure/nat-gateway/secure-nat-gateway): "combine outbound SNAT scalability with centralized traffic inspection and threat protection" | Confirmed. The source has no sentence saying NAT does not filter, so the old wording was replaced. |
| Admission runs after authentication and authorisation, can block some connections, reads bypass it. | [Admission Control](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) | Confirmed |
| Pod Security Admission enforce acts on pods, not on the owning Deployment. Baseline allows root. Audit and Warn do not reject. | [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/), [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) | Confirmed |
| Deployment safeguards have Warn and Enforce, with namespace exclusions. | [deployment-safeguards](https://learn.microsoft.com/en-us/azure/aks/deployment-safeguards) | Confirmed |
| Azure Policy uses Gatekeeper pods. Effects such as Deny and Audit are set in Azure. | [policy-for-kubernetes](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/policy-for-kubernetes) | Confirmed |
| AKS storage encryption is always on. KMS is an optional extra layer. | [kms-data-encryption-concepts](https://learn.microsoft.com/en-us/azure/aks/kms-data-encryption-concepts) | Confirmed |
| Secrets Store CSI Driver mounts Key Vault secrets. | [csi-secrets-store-driver](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver) | Confirmed |
| `kube-audit-admin` leaves out get and list. `kube-audit` logs them. | [monitor-aks](https://learn.microsoft.com/en-us/azure/aks/monitor-aks#aks-audit-policy): "excludes the get and list audit events" | Confirmed. The `guard` category is listed without a description in [monitor-aks-reference](https://learn.microsoft.com/en-us/azure/aks/monitor-aks-reference), so the page no longer mentions it. |
| Defender rescans registry images by activity, so inactive images can fall outside. | [agentless vulnerability assessment](https://learn.microsoft.com/en-us/azure/defender-for-cloud/agentless-vulnerability-assessment-azure) | Confirmed |
| Defender documents a Kubernetes alerts simulation tool. | [alerts-containers](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-containers#kubernetes-alerts-simulation-tool) | Confirmed |
| Image Cleaner does not support Windows node pools or AKS virtual nodes. | [image-cleaner](https://learn.microsoft.com/en-us/azure/aks/image-cleaner) | Confirmed |
| Cluster and node OS upgrade channels exist. | [auto-upgrade-cluster](https://learn.microsoft.com/en-us/azure/aks/auto-upgrade-cluster) | Confirmed |
| Workload ID exchanges a ServiceAccount token for an Entra token and needs the pod label. | [workload-identity-overview](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) | Confirmed |
| Automatic mounting of the ServiceAccount token can be turned off. | [Configure Service Accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) | Confirmed |
| The right to create pods can give access to Secrets and ServiceAccounts in the namespace. | [RBAC Good Practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/#workload-creation) | Confirmed |
| AKS Automatic: Azure RBAC and Workload ID pre-configured, deployment safeguards and baseline Pod Security enforced by default. | [intro-aks-automatic](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic) | Confirmed |
| FIPS node pools give FIPS 140-3 cryptographic modules. | [enable-fips-nodes](https://learn.microsoft.com/en-us/azure/aks/enable-fips-nodes): "create Linux and Windows node pools with FIPS 140-3 enabled" | Confirmed |
| Pod Sandboxing uses Kata and gives each pod its own kernel. | [use-pod-sandboxing](https://learn.microsoft.com/en-us/azure/aks/use-pod-sandboxing) | Confirmed |
| Confidential Containers (preview) lists only Azure Linux 2.0. | [confidential-containers-overview](https://learn.microsoft.com/en-us/azure/aks/confidential-containers-overview#limitations) | Confirmed |
| Application Gateway for Containers has its data plane outside the cluster. | [AGC overview](https://learn.microsoft.com/en-us/azure/application-gateway/for-containers/overview): "Azure operates the underlying data plane outside the cluster" | Confirmed |
| `az aks get-upgrades`, `az aks show`, `kubectl get -L` exist as used. | [az aks](https://learn.microsoft.com/en-us/cli/azure/aks?view=azure-cli-latest), [kubectl get](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/) | Confirmed |
| Field names read from `az aks show`: `disableLocalAccounts`, `aadProfile`, `apiServerAccessProfile`, `networkProfile`, `securityProfile`. | [Managed Clusters Get](https://learn.microsoft.com/en-us/rest/api/aks/managed-clusters/get) | Confirmed |

## Request-flow figure, checked 16 Nov 2026

Scope: only the quotes in the figure "How a request gets into AKS". Each source page was fetched on 16 Nov 2026. A script compared all 22 quotes, and the words in each link, with the fetched page text. Result: 22 of 22 match. The claims from 13 Nov 2026 were not rechecked, so the "Current as of" date did not move.

| Claim in the figure | Source | Verdict |
|---|---|---|
| A change must reach the API server over the network. AKS gives it a public address by default. | [API server authorized IP ranges](https://learn.microsoft.com/en-us/azure/aks/api-server-authorized-ip-ranges) | Confirmed |
| Authentication comes first after TLS. A request that fails it gets 401. | [Controlling Access to the Kubernetes API](https://kubernetes.io/docs/concepts/security/controlling-access/) | Confirmed |
| Local accounts use an admin certificate that bypasses Entra ID. | [Access and identity options for AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-identity) | Confirmed |
| Authorization follows. A request no module allows gets 403. AKS can pass the decision to Entra ID with Azure role assignments. | Controlling Access, and Access and identity options for AKS | Confirmed |
| Admission runs mutating controllers first, then validating ones. Reads skip admission. | [Admission Control](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) and Controlling Access | Confirmed |
| Azure Policy extends Gatekeeper v3 as an admission webhook. Pod Security Admission is built in. | [Azure Policy for Kubernetes](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/policy-for-kubernetes), [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) | Confirmed |
| Deployment safeguards enforce through Azure Policy controls. | [Deployment safeguards](https://learn.microsoft.com/en-us/azure/aks/deployment-safeguards). Not quoted in the figure, the step only names it. | Confirmed |
| After admission the object is validated and written to the object store. KMS is an optional layer for secrets in etcd. | Controlling Access, [Data encryption at rest](https://learn.microsoft.com/en-us/azure/aks/kms-data-encryption-concepts) | Confirmed |
| The scheduler assigns pods to nodes. The kubelet makes sure they run. | [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/) | Confirmed |
| Resource logs are not collected until a diagnostic setting routes them. | [Monitor AKS](https://learn.microsoft.com/en-us/azure/aks/monitor-aks) | Confirmed |
| A LoadBalancer Service creates an Azure load balancer with an external IP. An internal one has only a private IP. | [Kubernetes Services in AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-network-services) | Confirmed |
| Ingress controllers can route HTTP traffic by inbound URL. | [Ingress in AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-network-ingress) | Confirmed |
| A Service exposes an app that runs as one or more pods. | [Service](https://kubernetes.io/docs/concepts/services-networking/service/) | Confirmed |
| Pods are non-isolated for ingress and egress by default. | [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) | Confirmed |
| The outbound type affects only egress traffic of the cluster. | [Outbound types](https://learn.microsoft.com/en-us/azure/aks/egress-outboundtype) | Confirmed |
| Workload identity uses a Kubernetes token and OIDC federation to reach Azure resources with Entra ID. | [Microsoft Entra Workload ID](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) | Confirmed |

The plain-language pass on 16 Nov 2026 changed wording only. One explanation was added: IMDS as "the Azure service on each node that can hand out identity tokens". It rests on the IMDS claims already checked above. `[inference]`

## Full recheck, 24 Nov 2026

All claims above and the request-flow quotes were fetched again on 24 Nov 2026 by four auditors (platform, identity and network, policy and logging, request flow). A second reviewer with a support engineer role fetched the sources again for each proposed change. 16 of 19 were confirmed and applied, 3 were rejected (certificate rotation wording already adequate, flow.txt is a shortened copy with the same facts, control plane upgrades are covered under Versions). Round 1 found no outright errors. Changes:

| Change on the page | Source | Verdict |
|---|---|---|
| Root in a container versus root on the node. | No source states it. | `[inference]` tag added |
| K04: Standard defaults to Privileged, Automatic to Baseline. Gatekeeper fails open. Compliance dashboard. | [deployment-safeguards](https://learn.microsoft.com/en-us/azure/aks/deployment-safeguards): "On AKS Standard clusters, Pod Security Standards default to the `Privileged` level, which doesn't enforce any restrictions." and "`fail-open` model" | Confirmed |
| K03: CSI driver can sync to a Kubernetes Secret. | [csi-secrets-store-driver](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver): "Syncs with Kubernetes secrets." The etcd and RBAC consequence is `[inference]`. | Confirmed |
| Defender daily rescan leaves out images not pushed or pulled in 30 days and not running in a monitored cluster. | [agentless vulnerability assessment](https://learn.microsoft.com/en-us/azure/defender-for-cloud/agentless-vulnerability-assessment-azure) | Confirmed |
| K02: Run Command RBAC actions and `disableRunCommand`. | [access-private-cluster](https://learn.microsoft.com/en-us/azure/aks/access-private-cluster) | Confirmed |
| K08: IMDS restriction on an existing cluster needs a node reimage. Privileged pods and SSH can change iptables rules. | [imds-restriction](https://learn.microsoft.com/en-us/azure/aks/imds-restriction) | Confirmed |
| Platform-initiated upgrade ignores deprecated API use and can override a Pod Disruption Budget. | [supported-kubernetes-versions](https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions) | Confirmed |
| Ingress NGINX migration targets. | [AKS blog](https://blog.aks.azure.com/2025/11/13/ingress-nginx-update) | Confirmed |
| Azure Linux 2.0 removal worded as the docs word it. Region status not stated. | [upgrade-os-version](https://learn.microsoft.com/en-us/azure/aks/upgrade-os-version) | Confirmed |
| Pod Sandboxing: Azure Linux only, no FIPS or Trusted Launch, not assessed by Defender. | [use-pod-sandboxing](https://learn.microsoft.com/en-us/azure/aks/use-pod-sandboxing) | Confirmed |
| Confidential Containers page says both "Azure Linux only" and "Azure Linux 2.0". Not on Automatic. | [confidential-containers-overview](https://learn.microsoft.com/en-us/azure/aks/confidential-containers-overview) | Confirmed |
| Ubuntu FIPS node pools use Ubuntu 22.04. Azure Linux 3.0 and later and Azure Container Linux also support FIPS. No FIPS with Pod Sandboxing ([use-pod-sandboxing](https://learn.microsoft.com/en-us/azure/aks/use-pod-sandboxing)). | [enable-fips-nodes](https://learn.microsoft.com/en-us/azure/aks/enable-fips-nodes): "Ubuntu 24.04 doesn't currently support FIPS" | Confirmed |
| jq filter also lists hostIPC. | [deployment-safeguards](https://learn.microsoft.com/en-us/azure/aks/deployment-safeguards) error table | Confirmed. The edited filter was run on three sample pods on 24 Nov 2026: it listed the hostIPC and hostNetwork pods and skipped the plain one. |

Round 8 (24 Nov 2026): Ingress NGINX migration sentence now names Application Gateway for Containers and the application routing Gateway API implementation first, with the Istio add-on as a service mesh option. concepts-network-ingress says "Consider Gateway API ingress with the Istio service mesh add-on" under "Service mesh or advanced ingress requirements", and the Istio add-on page says it "supports both Istio's own ingress traffic management API and the Kubernetes Gateway API". The same ingress page has a Note: "The Istio add-on currently doesn't support Gateway API for Istio ingress traffic". No page says GA or preview, so the conflict is tagged `[unverified]`. Kubescape: no Microsoft Learn page mentions it. kubescape.io calls it a "Cloud Native Computing Foundation (CNCF) incubating project"; cncf.io: "moved to the Incubating maturity level on January 13, 2025". Alert sentence now follows alerts-containers: "The alerts available in an environment depend on the Kubernetes distribution (AKS, EKS, GKE, or Arc-enabled), the installed components, and the specific activities being monitored."

Round 7 (24 Nov 2026) linked "Physical security and hypervisor: Microsoft" to [shared-responsibility](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility): "Microsoft is responsible for the underlying cloud infrastructure, which includes: Physical security ... Physical hosts ... Hypervisor". Added to Sources.

Round 6 (24 Nov 2026) widened the IMDS unsupported list on the page to match imds-restriction ("Unsupported add-ons include: ..." with virtual nodes and the cluster extensions Flux, Dapr, Azure App Configuration, Azure Machine Learning, Azure Container Storage and Azure Backup).

Round 4 (24 Nov 2026) added two checks from [concepts-security](https://learn.microsoft.com/en-us/azure/aks/concepts-security): K01 seccomp ("Built-in Linux security features such as AppArmor and seccomp are recommended as best practices") and K07 node SSH ("SSH is enabled by default and only accessible using the internal IP address. Disabling SSH ... is in preview").

Round 3 (24 Nov 2026, verified against live pages by a second reviewer): IMDS restriction (imds-restriction) now lists the unsupported add-ons and Windows node pools, and the iptables quote "can be modified with SSH or node-shell, so we recommend using Disable SSH or using a policy to disable privileged pods". Confidential Containers: "isn't supported with... AKS Automatic". Pod Sandboxing GA and preview variants noted. K09 MFA and Conditional Access: concepts-identity says only "A built-in cluster admin certificate that bypasses Entra ID", local-accounts says "non-auditable backdoor"; neither mentions MFA or Conditional Access, so that part is tagged `[inference]`. The "False positives or need context" bullets are tagged `[inference]`.

Round 2 (24 Nov 2026) changed the FIPS and IMDS sentences to the exact scope the sources give, listed seven body-linked pages in Sources, and fixed one awkward sentence in K10.

Not added, low value: newer node OS retirement dates (Ubuntu 20.04 and 22.04, Azure Linux with OS Guard), external OIDC provider (preview), TLS wording for the change lane.

## Interpretation by AI

Also tagged: the K09 MFA and Conditional Access effect of the admin certificate, and the six bullets under "False positives or need context" (legitimate causes of alerts).

These are tagged `[inference]` on the page and are not stated in a source: the main question in the short version, the platform and app team split, the manual review advice next to tools, the link between attack paths and items, the placement of risks and owners in the risk map, CIS checks of control plane nodes not being visible, service mesh as a security control, IMDS calls as a false positive, and the owner shown per step in the request-flow figure.

## Gaps

- **No cluster was examined.** The az and kubectl commands were compared with the documentation only.
- **The jq pod filter** was run on seven sample pods on 13 Nov 2026 and, with hostIPC added, on three sample pods on 24 Nov 2026. It listed the five with hostNetwork, hostPID, a privileged container, a privileged init container or hostPath, and skipped the two plain ones. It has not been run against a live cluster. Tagged `[unverified]` on the page.
- **Pod Sandboxing variants (24 Nov 2026).** use-pod-sandboxing says "`runtimeClassName: kata-vm-isolation` (GA)" and "`kata-vm-isolation-v2` (preview)". The listed limits (Azure Linux only, no FIPS or Trusted Launch, no Defender assessment) apply to both. [concepts-security](https://learn.microsoft.com/en-us/azure/aks/concepts-security) still says "(preview)" for the feature. The page follows the feature's own page.
- **Azure Linux 2.0 image removal.** The source says removal begins on 31 Oct 2026. Whether images are already gone in a given region is not stated.
- **Request-flow figure.** The order of the network steps for a user's request (load balancer, ingress, Service, NetworkPolicy, pod) is the common setup and is not stated as one sequence in a single source. Each step has its own quote. The risk ids per step are interpretation by AI. The text-fragment links were not opened in a browser one by one.
- **TLS at the ingress controller** is left out of the figure. No clean source sentence was found on 16 Nov 2026.

## 26 Nov 2026, inference tags checked against sources

Only the statements below were checked. "Facts checked" on the page stays at 24 Nov 2026. This section replaces the entries for these statements under "Interpretation by AI".

| Claim on the page | Source and quote | Verdict |
|---|---|---|
| Old: "Root in a container is not root on the node ... Privileged mode, hostPath or extra capabilities can give node access." | [user-namespaces](https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/): "Without using a user namespace a container running as root, in the case of a container breakout, has root privileges on the node." | The first sentence was wrong without user namespaces. Replaced. |
| Without a user namespace, root has root privileges on the node after a breakout | Same quote | Confirmed, tag removed |
| Privileged pods disable most security mechanisms | [pod-security-standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/): "Privileged Pods disable most security mechanisms and must be disallowed." | Confirmed |
| Root in a privileged container might use CAP_SYS_ADMIN on the node | [linux-kernel-security-constraints](https://kubernetes.io/docs/concepts/security/linux-kernel-security-constraints/): "a root user in a privileged container might be able to use the CAP_SYS_ADMIN and CAP_NET_ADMIN capabilities on the node" | Confirmed |
| Kubescape reports workload misconfigurations and access control risks | [README](https://github.com/kubescape/kubescape#readme): "Access control risks", "Workload misconfigurations" | Confirmed, tag removed. The next sentence is advice. |
| Syncing to a Kubernetes Secret stores the value in etcd; limit access with RBAC | [csi options](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-configuration-options): "You might want to create a Kubernetes secret to mirror your mounted secrets content." [secret](https://kubernetes.io/docs/concepts/configuration/secret/): "stored unencrypted in the API server's underlying data store (etcd)", "Enable or configure RBAC rules with least-privilege access to Secrets." | Confirmed, tag removed |
| The admin certificate breaks centralized audit, Conditional Access and PIM | [operator-best-practices-identity](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-identity): "Any caller who can list this credential gets full cluster admin access without going through Entra ID, which breaks centralized audit, Conditional Access, and Privileged Identity Management." | Confirmed, tag removed. The claim about MFA was dropped; the source does not name it. |
| Sensor host OS list | [support matrix](https://learn.microsoft.com/en-us/azure/defender-for-cloud/support-matrix-defender-for-containers#supported-host-operating-systems): lists Azure Linux 1.0 and 2.0 and Ubuntu 16.04 to 22.04, "Ensure your Kubernetes node runs on one of these verified operating systems." | Confirmed, tag removed |
| CIS checks of control plane node files are not applicable | [cis-kubernetes](https://learn.microsoft.com/en-us/azure/aks/cis-kubernetes): "N/A because AKS is a managed solution" (checks 1.1.x) | Confirmed, tag removed. Narrowed: some other control plane checks have results, so "not visible" was dropped. |
| Apps that use managed identity can request tokens from IMDS | [how-to-use-vm-token](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-to-use-vm-token): "The managed identities for Azure resources endpoint for the Instance Metadata Service." | Confirmed, tag removed. Listing it as needing context is interpretation by AI. |
| Risk map, K01 on nodes: a breakout reaches the node and its processes and files | [multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/#sandboxing-containers): "container escapes, where an attacker exploits a vulnerability to gain access to the host system and all the processes/files running on that host" | Confirmed, tag removed. The quote and link show in the map detail. |
| Service mesh: "consider if this is used as a security control" | None | Advice, so the tag was removed. Not confirmed by a source. |

Still tagged: the main question, the platform and app team split, the owner per step and per layer, the link between attack paths and items, the placement of risks and owners in the map, the IMDS restriction and deployment safeguards combination, and five of the six false positive bullets. No source was found that states these.
