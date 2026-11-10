# AKS-sikkerhetsvurdering: content assessment

Belongs to [AKS-sikkerhetsvurdering.html](AKS-sikkerhetsvurdering.html). Written by AI on 10 November 2026.

Page version assessed: working tree on `dev`, last commit `e728279`, with uncommitted edits (three lines changed to "interpretation by AI"). SHA-256 `cdec5713ff02facb28eb0c6ef6837047768dc363b55e0cdfb1957416e1d7cabb`. The page was not changed.

## Verdict

No factual error was found. Every sourced claim that was checked matches its source as fetched on 10 November 2026.

Five observations are listed below. All are rated low. One of them has a deadline: the Ingress NGINX note goes stale on 1 December 2026.

This verdict covers what the sources say. It does not cover whether the commands work on a real cluster, or the items the page itself labels `[inference]` or `[unverified]`.

## What was checked, and how

| Area | Method | Result |
|---|---|---|
| Source links | All 41 URLs on the page fetched with curl on 10 November 2026 | All returned HTTP 200 |
| Deep links | The 5 links with a `#fragment` checked against the ids in the fetched HTML | All 5 ids exist |
| Sourced claims | Fetched pages stripped to text, then searched for the passage behind each claim | All checked claims found, see below |
| jq pod filter (Runtime tab) | Run with jq against 7 made-up pod specs | Listed the 5 risky pods, skipped the 2 safe ones, exit 0 |
| Section links | `python3 -I scripts/section_anchors.py --check` | Exit 0 |

### Confirmed: OWASP

- The ten names K01 to K10 match the OWASP Kubernetes Top 10 (2025) exactly.
- Supply Chain Vulnerabilities was K02 in the 2022 list and is not in the 2025 list.

### Confirmed: dated lifecycle facts

- Ingress NGINX: the Kubernetes blog says maintenance ran until March 2026. Microsoft supports critical security patches for NGINX in the application routing add-on "through November 2026".
- Azure Linux 2.0: no security updates from 30 November 2025. Node images removed from 31 October 2026, after which node pools cannot scale.
- Pod-managed identity: deprecated 24 October 2022. The AKS add-on was supported through September 2025.
- Versions: platform support lists security patches as "Not supported". LTS must be enabled to get extended support.

### Confirmed: identity and access

- On clusters without Entra ID, the Cluster User role "has same effect of clusterAdmin role".
- AKS RBAC Reader cannot view roles, role bindings or Secrets.
- Local accounts are turned off with `disableLocalAccounts`. Cluster certificates must be rotated afterwards.
- Microsoft says to avoid cluster-admin credentials for pipeline identities and to use workload identity federation.
- Workload identity swaps a ServiceAccount token for an Entra token through OIDC federation. The `azure.workload.identity/use: "true"` label is required.
- Kubernetes RBAC good practices: the right to create workloads gives access to Secrets and ServiceAccounts in the namespace.

### Confirmed: control plane and network

- Each cluster has its own single-tenant control plane. The API server is public by default.
- Hostile multitenancy needs separate clusters.
- `az aks command invoke` reaches private clusters through the Azure API.
- The authorized IP ranges query matches the docs. An empty range turns the feature off.
- API server VNet integration works for public and private clusters.
- IMDS restriction is in preview and only covers pods that do not use the host network.
- Cilium network policies do not apply to host network pods.
- NetworkPolicy works at layer 3 and 4, needs a plugin that enforces it, and pods are open by default.

### Confirmed: admission, pods and nodes

- Admission runs after authentication and authorization. Reads skip it.
- Pod Security Admission in enforce mode acts on pods, not on workload resources. Exemptions exist.
- `runAsNonRoot` is only in the Restricted profile, so Baseline allows root.
- Deployment safeguards have Warn and Enforce levels. AKS Automatic uses Enforce by default, and namespaces can be excluded.
- AKS Automatic defaults: Azure RBAC, API server VNet integration, workload identity and OIDC, deployment safeguards, baseline Pod Security Standards, Image Cleaner.
- Azure Policy for AKS uses Gatekeeper v3 with audit and deny effects.
- Pod Sandboxing uses Kata and gives each pod its own kernel.
- Confidential Containers (preview) "currently only supports Azure Linux 2.0".

### Confirmed: data, logging and detection

- Azure Storage encryption of etcd is always on. KMS is an optional extra layer.
- The Secrets Store CSI driver mounts Key Vault secrets.
- `kube-audit-admin` leaves out get and list calls. Secrets are logged at Metadata level. A `guard` log category exists.
- Defender rescans daily the images pushed or pulled in the last 30 days, or running. Other images fall outside.
- Image Cleaner does not support Windows node pools or AKS virtual nodes.
- Defender documents a Kubernetes alerts simulation tool. Some alerts take up to an hour.
- `az aks get-upgrades`, `az aks show`, `kubectl get -L` and `-A` exist as written.

## Observations

1. **The Ingress NGINX note goes stale on 1 December 2026. Low.** The page says Microsoft supports critical fixes "until the end of November 2026". That is true today. In three weeks it describes the past, and the "Plan a migration" advice becomes late. How it is known: the AKS docs say "through November 2026", fetched 10 November 2026. Related: the Azure Linux 2.0 removal date (31 October 2026) has already passed. The page wording is still accurate, but "removes node images from" now reads as history.

2. **The page does not mention forced upgrades. Low, a gap and not an error.** The supported versions page now has a "Platform-initiated upgrade" column. It shows June 2027 for 1.29 to 1.32. The page's Versions note says nothing about it. How it is known: the column is in the table fetched 10 November 2026. Whether it was there on 1 November 2026 was not checked.

3. **"NAT alone does not filter destinations" is the page's wording, not the source's. Low.** The NAT Gateway docs say NAT does not inspect traffic and recommend Azure Firewall for that. The meaning holds up. The exact words are not in the source. Interpretation by AI: the claim is supported.

4. **There is no fact check file. Low, a process gap.** AGENTS.md asks for a fact check that records the date and verdict per claim. The page says "Facts checked 1 Nov 2026", but `AKS-sikkerhetsvurdering.factcheck.md` does not exist. So the 1 November check cannot be traced. How it is known: the file is not in the repo.

5. **Microsoft is not consistent about Pod Sandboxing being a preview. Low.** The AKS security concepts page calls it "(preview)" in one passage. The Pod Sandboxing page itself has no preview label. The page gives no label, which matches the feature's own page. Not observed to cause a wrong statement on the page.

## Not checked

- No command was run against a real cluster. That includes every `az` and `kubectl` command on the page.
- The jq filter was only run on made-up data. The page already labels it `[unverified]`.
- Items marked `[inference]` have no source to check against. That includes the attack path links, the risk placement in the architecture diagram, and the ownership split between platform team and app team.
- The page was not opened in a browser. Tabs, filters, the diagram and saved settings were not tested.
- Sources were searched for the relevant passages. They were not each read from start to finish, so a contradicting passage elsewhere on a source page could have been missed.
- Whether the sources changed between 1 November and 10 November 2026 was not checked.
- Completeness was not assessed. This checks that what the page says is right, not whether it covers everything an AKS review should.
