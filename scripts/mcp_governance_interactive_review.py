"""Interactive-only corrections from the holistic source review, 2026-11-12.

The legacy builder remains unchanged. Scoped replacements fail if shared wording drifts.
"""
import re


def apply_review(page, ev, inf, unv, evp, pre):
    def replace(old, new):
        nonlocal page
        assert page.count(old) == 1, (old[:100], page.count(old))
        page = page.replace(old, new)

    def control(cid, requirement=None, documented=None):
        nonlocal page
        pattern = rf'(<div class="ctl[^\"]*" id="ctrl-{re.escape(cid)}"[^>]*>)(.*?)(</div>)'
        def edit(m):
            body = m[2]
            for label, value in [('Design requirement', requirement), ('What Microsoft and GitHub document|What Microsoft documents', documented)]:
                if value is not None:
                    body, count = re.subn(rf'(<dt>(?:{label})</dt><dd>).*?</dd>', lambda n: n[1] + value + '</dd>', body, flags=re.S)
                    assert count == 1, (cid, label, count)
            return m[1] + body + m[3]
        page, count = re.subn(pattern, edit, page, flags=re.S)
        assert count == 1, (cid, count)

    replace(f"Managed settings file in the .github-private repository {ev('gh-file')}.",
            f"Managed settings file in the .github-private repository {ev('gh-file', 'review-gh-private')}.")
    replace(f"They are a file in the .github-private repository, changed by commit and push {ev('gh-file', 'gh-commit')}.",
            f"They are a file in the .github-private repository, changed by commit and push {ev('gh-file', 'review-gh-private', 'gh-commit')}.")
    control('inventory', requirement=(
        'Keep approved and denied servers in reviewed Git changes, with endpoint, owner, authentication, permitted tools and risk class. '
        'Use the company gateway URL for company backends. Review address, identity, permissions, tool and version changes. '
        f'Pin and verify local packages or container digests; a URL or command allowlist does not establish code integrity.'),
        documented=f'GitHub managed settings apply the allow and deny lists to servers in user and repository settings {ev("gh-profiles")}.')
    control('pipeline', requirement=(
        'Build adapters for GitHub managed settings and Foundry connection tool lists; validate each before deployment. '
        'Keep Power Platform MCP policy manual until its API path is verified. Microsoft 365 connector access stays manual. '
        f'Use separate least-privilege credentials, record the reviewed commit and target result, verify propagation and reconcile drift.'),
        documented=(
        f'GitHub managed settings can be hosted on GitHub as a server-managed deployment {ev("gh-deploy")}. '
        f'They are a file in the .github-private repository, changed by commit and push {ev("gh-file", "review-gh-private", "gh-commit")}. '
        f'Settings refresh within about an hour {ev("gh-refresh")}.'))
    control('client', requirement=(
        'Set a managed allowlist of approved endpoints and reject unmatched servers on each supported client. '
        'For restrictions that must survive account switching or unavailable server policy, use protected device policy. '
        f'Test precedence and client versions. Built-in servers, custom profiles, cloud sessions and other clients need separate coverage.'),
        documented=(
        f'VS Code documents allow, deny and managed-only policies {ev("vs-allow", "vs-managed", "vs-deny")}. '
        f'GitHub matches URLs and blocks unmatched entries; deny wins {ev("gh-url", "gh-block", "gh-deny")}. '
        f'Custom agent profiles and first-party servers have exceptions; client coverage varies {ev("gh-profiles", "gh-builtin", "gh-vary")}. '
        f'Server policy follows the signed-in account {ev("review-account")}; local delivery can persist across account changes {ev("review-local-policy")}.'))
    control('stdio', requirement=(
        'Limit local launch commands through managed policy. Pin reviewed artifacts and verify their integrity before execution. '
        'Apply application control, process isolation, least privilege and file and credential restrictions. '
        f'Account for local administrators, shell tools, other MCP clients and unmanaged devices as bypass paths.'))
    control('windows', requirement=(
        'Restrict device egress to approved destinations where operationally feasible. Test DNS, proxies, VPNs and permitted general web traffic. '
        f'{inf} Windows Firewall is not an MCP URL or tool-content allowlist; a permitted HTTPS destination may carry other traffic. '
        f'Combine egress restrictions with client policy and application control.'))
    control('gateway', requirement=(
        'Publish company MCP endpoints through API Management. Explicitly configure every client connection to that gateway address. '
        'Authenticate, authorize each caller and tool, rate-limit and log. Enforce tool arguments and object permissions at the server. '
        f'Do not treat an HTTP path filter as an MCP tool-name policy without verifying JSON-RPC handling.'))
    control('identity', requirement=(
        'At the gateway, validate token issuer, tenant, audience, expiry and caller permissions. '
        'Allow only the gateway identity to authenticate to the private backend. '
        f'Strip caller-supplied identity headers. For user-specific object permissions, send verified caller context over the gateway-only path, or use a delegated variant: keep gateway-only networking, acquire the correct backend audience token and retain user authorization.'),
        documented=(
        f'API Management validates Entra tokens or subscription keys {ev("in-entra", "in-key")}; its managed identity can authenticate to a backend {ev("out-mi")}. '
        f'OBO preserves user delegation and requires a downstream token {ev("review-obo", "review-obo-token")}. '
        f'Sign-in across clients with OBO {unv}. A subscription key on its own is not strong authentication {ev("review-key-weak")}.'))
    control('backend', requirement=(
        'Disable public backend access and permit the company gateway over a private path. Require valid backend authentication and least-privilege tool authorization. '
        f'Select hosting and a gateway tier that support the required private connection; classic Functions Consumption cannot meet this private-endpoint baseline.'))
    control('logging', requirement=(
        'Collect gateway, backend and supported client telemetry. Correlate authenticated caller, tenant, tool, decision and request ID. '
        'Redact credentials and sensitive payloads; restrict log access and retention. Monitor unapproved connections, policy drift and unusual tool use. '
        f'Review the inventory and run bypass tests periodically.'))
    control('purview-audit', requirement=(
        f'Validate actual audit events and fields for each agent integration before relying on server or tool visibility. '
        f'{inf} MCP calls may fall within agent-to-tools interactions; the cited Purview pages do not explicitly establish MCP endpoint coverage.'),
        documented=(
        f'Agent 365 instances are audited from creation, including agent-to-tools interactions {ev("purview-audit-on", "purview-audit-tools", "purview-audit-search")}. '
        f'The listed Agent 365 DLP interactions exclude tool calls {ev("purview-dlp-scope")}; DSPM inventories recently active agents {ev("purview-dspm-inventory")}. '
        f'Foundry auditing covers prompts and responses after the required integration setup {ev("purview-foundry-audit", "review-purview-setup")}. '
        f'{inf} This is audit coverage, not a demonstrated MCP DLP boundary.'))
    control('byo', requirement=(
        'Exclude direct BYO access to the private company backend: it contradicts gateway-only access. '
        'If piloting BYO, use a separate test endpoint, or test registration of the company gateway URL with compatible authentication. '
        f'Keep backend isolation and caller authorization intact; neither composition is validated here.'))
    control('ttp-users', requirement=(
        'Use a separate pilot endpoint for delegated user-token flows. Keep app-only workloads on an appropriately authenticated baseline endpoint. '
        f'One server policy covers every caller, so mixing incompatible callers can reject legitimate calls.'))
    control('power-platform', requirement=(
        '<span id="gap-unverified-url-block"></span>Use advanced connector policies (ACP) for listed MCP servers once Copilot Studio design-time enforcement reaches the target workload. '
        f'Until then, keep classic data policies as the block for unapproved MCP connectors. '
        f'Keep classic policies for custom and HTTP connectors, and for Copilot Studio virtual connectors without a dedicated agent setting. Use mixed mode when adding ACP {ev("pp-custom", "review-custom-classic", "review-acp-mixed", "acp-virtual")}. '
        f'Configure MCP policy manually until the API adapter is validated.'),
        documented=(
        f'ACP blocks whole MCP servers. A connector block covers its dependent tools {ev("pp-block", "studio")}. '
        f'Before design-time enforcement reaches a workload, ACP enforces at runtime only. Microsoft ties general availability to design-time rollout {ev("review-acp-rollout", "acp-runtime")}. '
        f'Some connectors remain nonblockable in unmanaged environments {ev("acp-environment")}. '
        f'The API supports policy automation {ev("pp-pipe")}. {unv} The cited API tutorial does not establish an MCP-specific payload or support for blocking arbitrary URLs.'))
    control('ttp-modes', requirement=(
        'Set the policy mode in Microsoft Defender. Test Audit, Block and evaluator failures. '
        'Use pre-invocation checks to stop calls and post-invocation checks to withhold results. '
        f'Do not automatically retry a write whose result was withheld: the action may already have completed.'),
        documented=(
        f'Policy mode is set in Microsoft Defender and cannot be changed at the gateway {evp("ttp-policy-mode")}. '
        f'Audit mode fails open; Block mode fails closed {evp("pv-ttp-audit", "pv-ttp-block")}. '
        f'One policy covers every tool and caller of a server {evp("pv-ttp-scope")}. '
        f'Discovery and session management are not evaluated {evp("review-ttp-discovery")}; initialize, tools/list and notifications are excluded {evp("review-ttp-example")}. '
        f'A post-call denial cannot undo execution {evp("pv-ttp-post")}; automatic retry is discouraged {evp("review-ttp-retry")}.'))
    control('ttp-users', documented=(
        f'The launch lists threat protection as preview {evp("rel-tool-threat")}. '
        f'It comes through the Agent 365 integration, where Defender and Purview inspect tool calls and results {evp("ttp-integration")}. '
        f'It requires a delegated Entra user token {evp("pv-ttp-token")}. App-only service-to-service calls are not supported {evp("pv-ttp-app")}. '
        f'A Defender or Purview license is required {evp("pv-ttp-lic")}.'))
    control('a365', requirement=(
        'Pilot discovery and blocking separately from backend isolation. Verify the supported gateway, tenant and enforcement before relying on them. '
        'Verify per-tool blocking on the Azure AI Gateway resource you deploy.'),
        documented=(
        f'Azure announced the integration as GA {evp("rel-agent-az")}. Agent 365 and its admin guide label Azure AI Gateway onboarding preview {evp("rel-agent-admin", "a365-gw-pre")}. '
        f'The API Management guide for the integration is titled preview {evp("a365-apim-title")}. '
        f'The tier matrix lists discovery and server blocking on API Management v2 and AI Gateway {evp("pv-a365-matrix")}. '
        f'API Management v1 tiers are not supported {evp("pv-a365-v1")}; v2 tiers have no tool-level access control or tool threat protection policies {evp("pv-a365-v2")}. '
        f'Per-tool blocking is documented for the AI Gateway tier in API Management {evp("pv-a365-tier")}, with a static tool list {evp("pv-a365-static")}. '
        f'Microsoft has deprecated that SKU in favor of a new resource type {ev("aig-sku-deprecated")}.'))
    replace('build the pipeline that applies it. Set the Microsoft 365 admin center by hand.', 'build and validate its target adapters. Configure Microsoft 365 access and Power Platform MCP policy manually until their respective automation is verified.')
    replace('Mark the server denied in Git; the pipeline removes it from its targets. In the Microsoft 365 admin center, block it in the registry and remove its connector by hand. Verify that calls are denied.',
            'Record the denial in Git and apply an urgent company-gateway block before waiting for client refresh. Reconcile automated targets, manually deny Power Platform and Microsoft 365 access, and block the separate BYO registration if used. Verify runtime denial and active-session behavior.')
    replace('Approval merges the change into the inventory. The pipeline then applies it to the policy targets.', 'Approval merges the inventory decision. Validated pipeline adapters update their targets; administrators apply and record the remaining manual policy changes.')
    replace('For Copilot Studio agents, no released guardrail checks call content (layer 3).', 'No released guardrail was established by this review for Copilot Studio call content (layer 3).')
    replace('The pages read on 2026-11-11 describe only preview controls at both layers.', 'The reviewed controls at both layers are preview; the supported-tool list does not establish MCP coverage.')
    replace('The pages read on 2026-11-11 describe only a preview control there.', 'The reviewed external detection control at that layer is preview.')
    replace('The API Management integration does not automatically route agents through a customer-hosted gateway', 'Agent 365 does not automatically route agents through a customer-hosted gateway')
    replace('Confirm its public endpoint fits the backend isolation target.', 'Keep its public endpoint separate from the private backend.') if 'Confirm its public endpoint fits the backend isolation target.' in page else None
    replace('Until then, block at server level and authorize at the server.', 'Until then, block at server level and authorize at the server.')
    replace('Blocked or preview route</li>', 'Rejected route or preview alternative</li>')
    # 2026-11-12 holistic review: cite the overview for the separate product, fix ownership and scope wording.
    replace('Configure Microsoft 365 access and Power Platform MCP policy manually until their respective automation is verified.',
            'Configure Microsoft 365 agent access by hand; it has no API option. Configure Power Platform MCP policy by hand until its API path is verified.')
    replace('<dt>Applies to</dt><dd>Agent 365 agent instances</dd>', '<dt>Applies to</dt><dd>Agent 365 agent instances and Foundry AI interactions</dd>')
    replace('No design control covers them. Pilot both, or limit it through GitHub account permissions.',
            f'No design control covers them. Pilot both switches, or limit the built-in server through GitHub account permissions.')
    assert page.count('What establishes the guarantee') == 14
    page = page.replace('What establishes the guarantee', 'Required control or validation')
    replace('Safe stop, or a rollback to the released-only design</td>',
            'Safe stop or a tested migration back to the released gateway</td>')
    # Context review: approval scope, publisher overrides and administrator roles.
    replace('Clear the external publisher type unless a server is on the list. Stage each connector to named groups.',
            'In Agent and plugin access, clear all publisher types for a default-deny starting point, then individually enable only approved connectors for named groups within User access. The setting also covers agents and plugins, so check what else it blocks before saving. Review existing individual overrides and future connector changes.')
    replace(f'Admins control availability {ev("m365-admin", "m365-org")}; every setting must allow the user {ev("m365-all")}.',
            f'Admins control availability {ev("m365-admin", "m365-org")}. Agent and plugin access controls which types of agents and plugins are available, including connectors and MCP servers {ev("m365-access-scope")}. Individual connector settings override publisher-type settings; User access remains the population ceiling {ev("review-connector-override")}.')
    replace(f'An administrator grants the A365 MCP Gateway Policy Operator role at tenant level with a one-time consent {evp("pv-a365-role")}.',
            f'Connecting the Azure gateway requires Global Administrator; AI Administrator cannot perform this operation {evp("review-gateway-admin")}. The one-time tenant consent grants the A365 MCP Gateway Policy Operator role {evp("pv-a365-role")}.')
    replace('Configure Microsoft 365 agent access by hand; it has no API option.',
            'Configure Microsoft 365 Agent and plugin access by hand; this setting has no API option.')
    replace('It carries the preview label ' + evp('fw-preview') + ' and inspects remote servers only ' + evp('fw-remote') + '.',
            'It carries the preview label ' + evp('fw-preview') + '; local servers and JSON-RPC batches are not inspected ' + evp('fw-remote') + '.')
    # 2026-11-28 statement review.
    replace(f"BYO tool-level blocking is planned {evp('pv-byo-tool-plan', 'pv-byo-roll')}.",
            f"BYO tool-level blocking is planned {evp('pv-byo-tool-plan', 'pv-byo-roll')}. New versions of a remote server cannot be republished during preview {evp('byo-no-republish')}.")
    replace(f"Do not count on device controls for this client. {inf} Calls leave from the Microsoft cloud, so device URL policy and Windows firewall rules do not see them.",
            'Do not count on <a href="#ctrl-windows">device controls</a> for this client.')
    replace(f"Use the Azure AI Gateway portal for the Microsoft.ApiManagement/aigateways resource {ev('rel-resource')}.",
            f"Use the dedicated AI Gateway portal, CLI or management APIs {ev('aig-own-apis')} for the Microsoft.ApiManagement/aigateways resource {ev('rel-resource')}.")
    replace('; the pipeline for it is not tested.', '.')
    replace(f"The model connection for Foundry prompt agents is in preview {evp('rel-fy-model-preview')}.",
            f"Foundry prompt agents can use gateway models through a model connection {evp('rel-fy-model-preview')}.")
    replace(f"It can be set to never, or to a list of tools that skip approval {ev('gr-fy-never')}.",
            f"It can be set to never, which requires no approval {ev('fy-never-none')}, or to a list of tools that skip approval {ev('gr-fy-never')}.")
    replace(f"{unv} Not checked which tools ask for a result review by default.",
            f"Which tools ask for a result review by default {unv}.")
    replace(f"{unv} MCP call coverage is unverified.", f"Coverage of MCP calls {unv}.")
    replace(f"The Network control does not affect them {ev('gr-fy-net')}.",
            f"The Network control does not affect them {ev('gr-fy-net')}. The harness is in preview {evp('fy-egress-harness')}. {pre}")
    replace('Isolate the company MCP backends and require access through API Management.',
            'Publish the company MCP servers in API Management with sign-in and caller authorization, point each client at the gateway, then isolate the backends.')
    replace('Admin blocks a whole MCP server in the API Management integration', 'Admin blocks a whole MCP server in the Agent 365 integration')
    replace(f" In Copilot CLI, disabling MCP in the account policy stops it {ev('rel-gh-cli-policy', 'rel-gh-cli-off')}.</p>"
            f"<p>Two switches are untested: the MCP servers in Copilot policy, which turns off every MCP server {ev('gh-policy-off')}, "
            f"and Registry only {ev('gh-reg-only')}, a public preview with weaker enforcement {ev('gh-reg-preview', 'gh-reg-bypass')}. "
            f"No design control covers them. Pilot both switches, or limit the built-in server through GitHub account permissions.",
            f"</p><p>The MCP servers in Copilot policy decides whether MCP servers can run at all {ev('gh-policy-off')}; in Copilot CLI, disabling it also stops this one "
            f"{ev('rel-gh-cli-policy', 'rel-gh-cli-off')}. Registry only {ev('gh-reg-only')} is a public preview {pre} with weaker enforcement "
            f"{ev('gh-reg-preview', 'gh-reg-bypass')}. No design control covers either switch. Limit the built-in server through GitHub account permissions; "
            f"the MCP servers in Copilot policy fits only users who need no MCP server.")
    defender = ' <a href="#ctrl-g-defender-on-the-agent-365-path">Defender on Agent 365 tool servers</a> is released for tools onboarded to Agent 365; Agent 365 documentation labels the BYO and gateway onboarding of a company server preview ' + pre + '.'
    replace('For Foundry agents, no released guardrail was established by this review for call content (layer 3) or tool responses (layer 6). '
            'The reviewed controls at both layers are preview; the supported-tool list does not establish MCP coverage.',
            'For Foundry agents, no released guardrail was established by this review for call content (layer 3) or tool responses (layer 6) on the company gateway path. '
            'The reviewed Foundry controls at both layers are preview; the supported-tool list does not establish MCP coverage.' + defender)
    replace('A preToolUse command hook error denies it, but a timeout falls back to normal permissions, even for policy hooks',
            'VS Code says GitHub documents that a preToolUse command hook error denies the call, but a timeout falls back to normal permissions, even for policy hooks')
    replace('; <a href="#ctrl-m365-network">Microsoft 365 Copilot network path</a>', '')
    replace('The pilot tests its private backend path.', 'The preview pilot tests its private backend path.')
    replace('No released guardrail was established by this review for Copilot Studio call content (layer 3). '
            'The reviewed external detection control at that layer is preview.',
            'No released guardrail was established by this review for Copilot Studio call content (layer 3) on the company gateway path. '
            'The reviewed Copilot Studio controls at that layer are preview.' + defender)
    replace('The list limits the tools of one connection; it does not stop',
            f'{inf} The list limits the tools of one connection; it does not stop')
    return page
