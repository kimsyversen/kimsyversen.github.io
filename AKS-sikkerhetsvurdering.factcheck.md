# AKS-sikkerhetsvurdering: fact check

Belongs to [AKS-sikkerhetsvurdering.html](AKS-sikkerhetsvurdering.html). Decisions: [AKS-sikkerhetsvurdering.decisions.md](AKS-sikkerhetsvurdering.decisions.md).

Checked 13 Nov 2026. Each source page was fetched that day and the claim was compared with the page text. Four full passes were made. The second led to three added source entries. The third changed the control plane wording in two places and added the REST reference. The fourth read the final page again from the header to the end of the script, including the text the script builds, and found nothing to change. The stylesheet holds no reader text.

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
| NAT alone does not filter destinations. | [secure-nat-gateway](https://learn.microsoft.com/en-us/azure/nat-gateway/secure-nat-gateway) | Confirmed |
| Admission runs after authentication and authorisation, can block some connections, reads bypass it. | [Admission Control](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) | Confirmed |
| Pod Security Admission enforce acts on pods, not on the owning Deployment. Baseline allows root. Audit and Warn do not reject. | [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/), [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) | Confirmed |
| Deployment safeguards have Warn and Enforce, with namespace exclusions. | [deployment-safeguards](https://learn.microsoft.com/en-us/azure/aks/deployment-safeguards) | Confirmed |
| Azure Policy uses Gatekeeper pods. Effects such as Deny and Audit are set in Azure. | [policy-for-kubernetes](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/policy-for-kubernetes) | Confirmed |
| AKS storage encryption is always on. KMS is an optional extra layer. | [kms-data-encryption-concepts](https://learn.microsoft.com/en-us/azure/aks/kms-data-encryption-concepts) | Confirmed |
| Secrets Store CSI Driver mounts Key Vault secrets. | [csi-secrets-store-driver](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver) | Confirmed |
| `kube-audit-admin` leaves out get and list. `kube-audit` logs them. `guard` category exists. | [monitor-aks](https://learn.microsoft.com/en-us/azure/aks/monitor-aks#aks-audit-policy): "excludes the get and list audit events" | Confirmed |
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

## Interpretation by AI

These are tagged `[inference]` on the page and are not stated in a source: the main question in the short version, the platform and app team split, the manual review advice next to tools, the link between attack paths and items, the placement of risks and owners in the risk map, CIS checks of control plane nodes not being visible, service mesh as a security control, and IMDS calls as a false positive.

## Gaps

- **No cluster was examined.** The az and kubectl commands were compared with the documentation only.
- **The jq pod filter** was run on seven sample pods on 13 Nov 2026. It listed the five with hostNetwork, hostPID, a privileged container, a privileged init container or hostPath, and skipped the two plain ones. It has not been run against a live cluster. Tagged `[unverified]` on the page.
- **Source conflict on Pod Sandboxing.** Its own page has no preview label. [concepts-security](https://learn.microsoft.com/en-us/azure/aks/concepts-security) still says "(preview)". The page follows the feature's own page.
- **Azure Linux 2.0 image removal.** The source says removal begins on 31 Oct 2026. Whether images are already gone in a given region is not stated.
