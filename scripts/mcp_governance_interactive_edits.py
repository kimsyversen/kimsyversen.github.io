"""Wording edits applied to the interactive page after it is built.

These were made by hand on the page after the builder last matched it (commit abcafa4, 2026-11-12):
the three gateway options, the removed "Interpretation by AI:" prefixes, the Agent 365 and AI Gateway
scope wording, the pipeline target counts, and the tests that follow from them.
Each pair is (text in the built page, replacement). Each old text must occur exactly once.
When you next change any of this wording, move the change into the builder's source text and
delete its pair here.
"""

EDITS = [
    ('response</button></div><p class="cl-note">Content filters on the user input and the final answer are left out: they are not MCP controls.</p></details>',
     'response</button></div></details>'),
    ('Interpretation by AI: a',
     'A'),
    ('Interpretation by AI: calls',
     'Calls'),
    ('pipeline separately.',
     'pipeline separately. The list limits the tools of one connection; it does not stop a developer from adding another server. <a href="#ctrl-foundry-network">Foundry network and sandbox</a> covers isolated toolboxes. See the <a href="#ctrl-foundry-egress">Network guardrail</a> for hosted-agent egress. Check <a href="#gap-foundry-prompt-agents">egress coverage</a> before claiming a server boundary.'),
    ('results <span class="rt">Product guardrail · layer',
     'results <span class="rt">Guidance, not a product control · layer'),
    (' This is advice, not a control.',
     ''),
    ('i">inference</span> Interpretation by AI: the list',
     'i">inference</span> The list'),
    (' i">inference</span> Interpretation by AI: Defender',
     ' i">inference</span> Defender'),
    ('i">inference</span> Interpretation by AI: the source',
     'i">inference</span> The source'),
    ('href="https://github.com/kimsyversen/kimsyversen.github.io/blob/master/mcp-governance-microsoft-interactive.factcheck.md#ev-V140">V140</a>.</dd></dl></div><p class="q-note">No released',
     'href="https://github.com/kimsyversen/kimsyversen.github.io/blob/master/mcp-governance-microsoft-interactive.factcheck.md#ev-V140">V140</a>.</dd></dl></div><p class="q-note">For Copilot Studio agents, no released'),
    (' Interpretation by AI: MCP',
     ' MCP'),
    ('data-label="Test">Edit a target ',
     'data-label="Test">Edit a pipeline target '),
    ('covers it. Pilot',
     'covers them. Pilot'),
    ('gateway and backend.',
     'server.'),
    ('tool in the API Management integration</td><td data-label="Expected result">Denied,',
     'tool in the Agent 365 integration</td><td data-label="Expected result">Denied,'),
    ('a supported gateway',
     'the AI Gateway product'),
    ('checks the tool call before it runs. <span class=\\"tg i\\">inference<\\/span> Interpretation by AI: the sources do not say where Defender runs.", "preview": false}, "cs":',
     'checks the tool call before it runs. <span class=\\"tg i\\">inference<\\/span> The sources do not say where Defender runs.", "preview": false}, "cs":'),
    ('checks the tool call before it runs. <span class=\\"tg i\\">inference<\\/span> Interpretation by AI: the sources do not say where Defender runs.", "preview": false}, "direct":',
     'checks the tool call before it runs. <span class=\\"tg i\\">inference<\\/span> The sources do not say where Defender runs.", "preview": false}, "direct":'),
    ('<a class="sec-link" href="#h-rollout">Rollout and tests</a></h2>\n    <p class="goal"><b>Goal</b>Do not rely on API Management alone for objectives A and B.</p></header>',
     '<a class="sec-link" href="#h-rollout">Rollout and tests</a></h2></header>'),
    ('risk class. Change it only',
     'risk class. List a company server at its gateway address, so clients reach it only through the gateway. Change it only'),
    ('so they do not cover Microsoft 365 Copilot.',
     'so they do not cover the clients that call from the cloud: Microsoft 365 Copilot, Copilot Studio and Foundry agents.'),
    ('build the pipeline that applies it.</li>',
     'build the pipeline that applies it. Set the Microsoft 365 admin center by hand.</li>'),
    ('<li><strong id="gap-windows-outbound">',
     '<li><strong id="gap-foundry-prompt-agents">Foundry prompt agents outside the Copilot harness.</strong> The Network control does not affect them <a class="ev" href="https://github.com/kimsyversen/kimsyversen.github.io/blob/master/mcp-governance-microsoft-interactive.factcheck.md#ev-V101">V101</a>. <span class="tg i">inference</span> A connection tool list does not prevent another server connection. Verify project egress restrictions for these agents. Backend isolation still keeps the company MCP server behind the gateway.</li>\n<li><strong id="gap-windows-outbound">'),
]
