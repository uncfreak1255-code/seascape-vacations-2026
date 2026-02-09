const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const headers = fs.readFileSync(path.join(root, '_headers'), 'utf8');

function expect(condition, message) {
  if (!condition) throw new Error(message);
}

// We iterate frequently. HTML routes like /guides/ and /stays/.../ are directories,
// so they MUST NOT be cached as immutable for a year.
expect(/\/[\s\S]*Cache-Control:\s*public,\s*max-age=0/.test(headers), 'Expected default /* Cache-Control to be max-age=0');
expect(!/\/[\s\S]*Cache-Control:[^\n]*immutable/.test(headers.split('\n\n')[0] || ''), 'Default /* Cache-Control must not include immutable');

console.log('Cache headers tests passed.');
