const fs = require('fs');
const report = JSON.parse(fs.readFileSync('lighthouse-mobile.json', 'utf8'));

const scores = {
  Performance: report.categories.performance.score * 100,
  Accessibility: report.categories.accessibility.score * 100,
  BestPractices: report.categories['best-practices'].score * 100,
  SEO: report.categories.seo.score * 100,
};

console.log('--- Lighthouse Mobile Scores ---');
console.log(`Performance: ${scores.Performance.toFixed(0)}`);
console.log(`Accessibility: ${scores.Accessibility.toFixed(0)}`);
console.log(`Best Practices: ${scores.BestPractices.toFixed(0)}`);
console.log(`SEO: ${scores.SEO.toFixed(0)}`);

if (scores.Performance < 90) {
    console.log('\n--- Performance Issues (Top 3) ---');
    const audits = report.audits;
    // Find audits with weight > 0 and score < 1, sort by impact
    // This is complex to extract perfectly without full audit data logic, but we can look for high-impact opportunities
    // Actually, report.audits['largest-contentful-paint'].displayValue is useful
    console.log(`LCP: ${audits['largest-contentful-paint'].displayValue}`);
    console.log(`TBT: ${audits['total-blocking-time'].displayValue}`);
    console.log(`CLS: ${audits['cumulative-layout-shift'].displayValue}`);
}
