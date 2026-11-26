# MCP security page: decisions

26 November 2026

- Diagrams are HTML and CSS, not ASCII files. The owner said design rules in AGENTS.md do not apply to this page. Each figure has a text description.
- The brief's "I would govern this" and "I would distinguish" are written without "I" and tagged `[recommendation]`, because AGENTS.md forbids showing AI-drafted views as a person's own.
- Superseded in part: "Built-in sandboxing: No" stays in the table, with a note that a client or operating system can add one.
- The 13 principles are kept word for word.
- The bridge case has its own diagram beside local and remote, so the exception sits next to the "no local execution" statement.
- The page is static HTML, edited by hand. It has no builder.
- The brief's local and remote wording was corrected after review: "Both processes run locally unless separately isolated" became "Client and server run on the same machine, with the same privileges unless the server is isolated", and "external infrastructure" became "another machine".
- "It can do these things without the AI invoking a single MCP tool" keeps the brief's wording; the figure above it states the no-isolation condition. "Your account's access" was added to the figure.
- The brief's "could potentially" is written "can", which states ability. The figure states the conditions.
- The brief's "MCP should therefore extend" is written "MCP governance should extend", because the paragraph sits with the MCP governance layer.
- The "AI-driven tool invocation" table row stays as supplied.
- Superseded in part: Local transport risks sit in the text under the three figures, so the figures stay equal in size.
- Superseded: The brief's "does not inherently introduce a separate installation mechanism, security boundary or sandbox" is written "adds no ... of its own to this path", limited to what was checked.
- Superseded in part: "After execution" is written "after it starts". The clause on tools, resources and prompts sits in the figure.
- Superseded for the bridge verdict: "Local software execution risk" is written "local code execution risk", matching the brief's diagram. "However" is dropped.
- Section titles are shortened or renamed, and "two separate governance layers" drops "separate".
- "This is an important architectural distinction", "This means that" and the lead-in to the security policy quote are left out.
- The picture's "HTTPS" is written "Streamable HTTP": no MCP source checked states HTTPS for the connection shown.
- Superseded in part: The page opens with a short "What is MCP?" section in very plain words, asked for by the owner: one idea per sentence, key words in bold, no metaphors.
- Superseded in part: The owner asked for `[inference]` tags to be replaced where a source or plainer wording allows it. The opening line, the sandbox sentence, the bridge verdict and the remote risks sentence now state only what sources say, so they differ from the brief. "What a malicious server can do" lost its tag because each item has a quote.
- Superseded: The tag stays on the comparison table, the API comparison and the two gateway statements: no official source states them.
- The brief's sentence that an MCP gateway can help with the second layer is drawn, not written: the gateway sits in the MCP governance column and the first column shows what it does not stop. The figure's text description carries the full sentence.
- The owner set the title to "MCP Security", moved the plain definition to the opening paragraph and removed the "What is MCP?" section. Its id `what-is-mcp` is now on that paragraph.
- The owner removed the quotes under the sections they named and asked for the same style elsewhere, so the page shows no quotes. This is an exception to the AGENTS.md rule on quotes beside diagram claims. The quotes and passage links are in the fact check, and the quote script checks that table.
- The owner named the npm section "MCP servers are installed the same way as other npm packages". The other section titles follow that style and were drafted by AI. Section ids are unchanged.
- Caveat paragraphs that were not in the brief are removed: npx cache behaviour, the SDK sandbox sentence, npm install scripts and client sandboxes, local HTTP and configuration file attacks, and the OAuth URL attack.
- Text uses the full width, like the figures and tables. The owner saw that the opening paragraph was narrower. The limits on the opening, prose and highlighted sentences are removed. The title keeps its limit.
- The page has no `[inference]` tags. The table and its heading rest on added quotes. The API comparison is replaced by the documented point that a remote server needs no installation on each device. The gateway statements now say only that some gateways cover remote servers only, with Cloudflare and Microsoft as evidence. The npx sentence is now advice under the section's `[recommendation]` tag.
- The three npm column cells for MCP-only risks follow from the definitions and have no quote of their own.
