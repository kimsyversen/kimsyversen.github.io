const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const read = (name) => fs.readFileSync(path.join(__dirname, '..', name), 'utf8');
const legacy = read('agentic-devsecops.html');
const destination = read('devsecops.html');
const redirect = legacy.match(/<script>([\s\S]*?)<\/script>/)[1];
const route = destination.match(/  function route\(scroll\) \{[\s\S]*?\n  \}/)[0];
const agenticStart = destination.indexOf('<div class="view" id="view-agentic"');
const footerStart = destination.indexOf('<footer id="shared-risk-audit">');
assert.ok(agenticStart > 0 && footerStart > agenticStart);

const targets = new Map();
for (const match of destination.matchAll(/<[a-z][^<>]*\sid="([^"]+)"[^<>]*>/gi)) {
  const [tag, id] = match;
  assert.ok(!targets.has(id), `Duplicate ID ${id}`);
  const containerView = match.index >= agenticStart && match.index < footerStart ? 'agentic' : null;
  const anchorView = tag.match(/data-anchor-view="([^"]+)"/)?.[1] ?? null;
  targets.set(id, {
    closest: () => containerView && { getAttribute: () => containerView },
    getAttribute: (name) => name === 'data-anchor-view' ? anchorView : null,
  });
}

function follow(hash, expected) {
  let url;
  vm.runInNewContext(redirect, { location: { hash, replace: (value) => { url = value; } } });
  assert.equal(url, 'devsecops.html#' + expected, hash);
  assert.ok(targets.has(expected), `Missing destination ${expected}`);
  let selected;
  vm.runInNewContext(route + '\nroute(false);', {
    location: { hash: '#' + expected },
    document: { getElementById: (id) => targets.get(id) },
    presentation: null,
    current: '',
    maps: [],
    showView: (view) => { selected = view; },
  });
  assert.equal(selected, 'agentic', hash);
}

// IDs from both revisions of the former standalone page.
for (const id of ['lifecycle', 'map-heading', 'tag-key', 'h-tag-key']) {
  follow('#' + id, 'agentic-' + id);
}
for (const phase of ['plan', 'code', 'review', 'build', 'test', 'release', 'deploy', 'operate']) {
  follow('#' + phase, 'agentic-' + phase);
  follow('#phase-' + phase, 'agentic-phase-' + phase);
}
for (const id of ['agent-risks', 'what-changes', 'risk-untrusted-input',
  'risk-agent-access', 'risk-human-approval', 'risk-traceable-handoffs']) {
  follow('#' + id, id);
}
follow('#%72isk-agent-access', 'risk-agent-access');
follow('#%74ag-key', 'agentic-tag-key');
follow('#%70lan', 'agentic-plan');
for (const hash of ['', '#', '#unknown', '#risk-p-g1', '#%', '#%E0%A4%A']) {
  follow(hash, 'view-agentic');
}

assert.match(legacy, /http-equiv="refresh" content="0; url=devsecops\.html#view-agentic"/);
assert.match(legacy, /href="devsecops\.html#view-agentic">Agentic DevSecOps<\/a>/);
const switcher = destination.match(/<nav class="switch"[^>]*>[\s\S]*?<\/nav>/)[0];
assert.doesNotMatch(switcher, /aria-current/);
console.log('Agentic DevSecOps redirect checks passed.');
