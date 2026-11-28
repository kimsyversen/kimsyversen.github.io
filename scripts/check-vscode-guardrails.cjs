// Exercise the simulator's own decision logic without executing any example action.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const html = fs.readFileSync(path.join(__dirname, '../vscode-guardrails.html'), 'utf8');
const rules = html.match(/<script>\s*\(function\(\)\{([\s\S]+?)var gatesEl=/)[1];
const { st, evaluate, verdict, Q, ACTS, OPTS } =
  vm.runInNewContext(rules + '\n({ st, evaluate, verdict, Q, ACTS, OPTS })');

function simulate(options) {
  const result = evaluate({ ...st, ...options });
  for (const gate of result.g) {
    for (const id of gate.qs) assert.ok(Q[id], 'Missing evidence for ' + id);
  }
  return result;
}

const fetch = simulate({ act: 'fetch' });
assert.equal(fetch.asks, 1);
assert.match(fetch.g[1].say, /host/);
assert.equal(simulate({ act: 'fetch', answer: 'no' }).ran, false);
// The model assumes a blocked fetch requests separate approval to run outside the sandbox.
const fenced = { act: 'fetch', sandbox: 'on', net: 'blocked' };
assert.equal(simulate(fenced).asks, 2);
assert.equal(simulate(fenced).g[2].tag, 'inference');
const declinedRetry = simulate({ ...fenced, answer: 'yes', retry: 'no' });
assert.equal(declinedRetry.asks, 2);
assert.equal(declinedRetry.why, 'fence-no');
assert.deepEqual(Array.from(declinedRetry.g, gate => gate.state), ['pass', 'ask', 'stop']);
assert.match(verdict(simulate(fenced)).join(' '), /approved the tool call.*approved the request to run outside/);
assert.match(verdict(simulate({ ...fenced, level: 'assisted' })).join(' '),
  /AI reviewer approved the tool call.*You approved the request to run outside/);
assert.equal(simulate({ ...fenced, answer: 'no', retry: 'yes' }).g.length, 2);
assert.equal(simulate({ ...fenced, esc: 'never' }).why, 'fence');
assert.equal(simulate({ ...fenced, level: 'all', retry: 'no' }).why, 'fence-no');
assert.equal(simulate({ ...fenced, net: 'open' }).asks, 1);

const network = { act: 'curl', sandbox: 'on', net: 'blocked' };
assert.equal(simulate({ ...network, level: 'all', retry: 'no' }).why, 'fence-no');
const reviewed = { ...network, level: 'assisted', judge: 'no' };
assert.equal(simulate(reviewed).asks, 2);
const blocked = simulate({ ...reviewed, esc: 'never' });
assert.equal(blocked.asks, 1);
assert.equal(blocked.ran, false);
assert.match(verdict(blocked).join(' '), /Requests to run outside the sandbox are disabled/);

// Stopping at a check must prevent later checks from running in every configuration.
const settings = Object.entries(OPTS).reduce((combinations, [key, options]) =>
  combinations.flatMap(combination => options.map(([value]) => ({ ...combination, [key]: value }))), [{}]);
for (const { id } of ACTS) {
  for (const state of settings) {
    const result = simulate({ ...state, act: id });
    assert.deepEqual(Array.from(result.g, gate => gate.g),
      ['trust', 'approval', 'sandbox', 'review'].slice(0, result.g.length));
    assert.equal(result.ran, result.g.at(-1).state === 'after');
    assert.equal(result.ran ? 0 : 1, result.g.filter(gate => gate.state === 'stop').length);
  }
}
console.log(`Guardrails simulator checks passed for ${ACTS.length * settings.length} configurations.`);
