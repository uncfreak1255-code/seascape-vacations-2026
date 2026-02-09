const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');

function expect(condition, message) {
  if (!condition) throw new Error(message);
}

function read(file) {
  return fs.readFileSync(path.join(root, file), 'utf8');
}

const indexHtml = read('index.html');
expect(indexHtml.includes('class="nav-link" href="/guides/"'), 'Missing Guides link in desktop nav');
expect(indexHtml.includes('class="mobile-item" href="/guides/"'), 'Missing Guides link in mobile nav');

const guidesIndex = read('guides/index.html');
expect(guidesIndex.includes('href="#main"'), 'Guides hub should include a skip link to #main');
expect(guidesIndex.includes('<main') && guidesIndex.includes('id="main"'), 'Guides hub should include a <main id="main"> landmark');

const guidePages = [
  'area-guide-ami.html',
  'area-guide-bradenton.html',
  'area-guide-sarasota.html',
  'area-guide-siesta-key.html'
];

for (const page of guidePages) {
  const html = read(page);
  expect(html.includes('data-guides-block="true"'), `Missing guides block in ${page}`);
  expect(html.includes('href="/guides/"'), `Missing /guides/ link in ${page}`);
  expect(html.includes('https://seascape-vacations.com/guides/'), `Missing guides breadcrumb URL in ${page}`);
}

console.log('SEO Guides tests passed.');
