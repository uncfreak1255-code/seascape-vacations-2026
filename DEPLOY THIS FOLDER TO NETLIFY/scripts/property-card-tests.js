const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');

function expect(condition, message) {
  if (!condition) throw new Error(message);
}

const occurrences = (str, sub) => (str.match(new RegExp(sub, 'g')) || []).length;

expect(html.includes('class="prop-btn prop-details-btn"'), 'Missing prop-details-btn element');
expect(occurrences(html, 'class=\\"prop-btn prop-details-btn\\"') >= 2, 'Expected prop-details-btn element in both property templates');
expect(html.includes('onclick="showPropertyDetail(\'${p.id}\')"') || html.includes('onclick="showPropertyDetail(\'${p.id}\');'), 'Missing showPropertyDetail onclick for View Details');
expect(!html.includes('href="${p.bookingUrl}"'), 'View Details should not deep-link to bookingUrl (should open on-site property detail)');

console.log('Property card link tests passed.');
