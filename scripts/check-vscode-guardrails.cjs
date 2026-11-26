// Exercise the simulator's own decision logic without executing any example action.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const html = fs.readFileSync(path.join(__dirname, '../vscode-guardrails.html'), 'utf8');
const rules = html.match(/<script>\s*\(function\(\)\{([\s\S]+?)var gatesEl=/)[1];
const { st, evaluate, verdict, Q } = vm.runInNewContext(rules + '\n({ st, evaluate, verdict, Q })');

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
// With the sandbox network blocked, the Copilot SDK says a fetch needs approval to run outside it.
const fenced = { act: 'fetch', sandbox: 'on', net: 'blocked' };
assert.equal(simulate(fenced).asks, 2);
assert.equal(simulate({ ...fenced, esc: 'never' }).why, 'fence');
assert.equal(simulate({ ...fenced, level: 'all', answer: 'no' }).why, 'fence-no');
assert.equal(simulate({ ...fenced, net: 'open' }).asks, 1);

const network = { act: 'curl', sandbox: 'on', net: 'blocked' };
assert.equal(simulate({ ...network, level: 'all', answer: 'no' }).why, 'fence-no');
const reviewed = { ...network, level: 'assisted', judge: 'no' };
assert.equal(simulate(reviewed).asks, 2);
const blocked = simulate({ ...reviewed, esc: 'never' });
assert.equal(blocked.asks, 1);
assert.equal(blocked.ran, false);
assert.doesNotMatch(verdict(blocked).join(' '), /did not need to ask/);
console.log('Guardrails simulator checks passed.');
