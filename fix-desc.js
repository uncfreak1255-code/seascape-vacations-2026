const fs = require('fs');
const file = './DEPLOY THIS FOLDER TO NETLIFY/properties/index.html';
let content = fs.readFileSync(file, 'utf8');

// The minified HTML has this exact string:
// <div class="prop-card-top">\n                            <div>\n                                <h3 class="prop-title">${e.title}</h3>\n                                <p class="prop-location">${e.location} · ${e.specs}</p>\n                            </div>\n                            <div class="prop-badge"><span class="star" aria-hidden="true">★</span> ${e.rating}</div>\n                        </div>\n                        <div>\n                            <div class="prop-highlights">

// Or because it's minified, it might be:
// <div class="prop-card-top">\n                            <div>\n                                <h3 class="prop-title">${e.title}</h3>\n                                <p class="prop-location">${e.location} · ${e.specs}</p>\n                            </div>\n                            <div class="prop-badge"><span class="star" aria-hidden="true">★</span> ${e.rating}</div>\n                        </div>\n                        <div>\n                            <div class="prop-highlights">\n

const newSnippet1 = `
                        <div class="prop-card-top">
                            <div>
                                <h3 class="prop-title">\${e.title}</h3>
                                <p class="prop-location">\${e.location} · \${e.specs}</p>
                            </div>
                            <div class="prop-badge"><span class="star" aria-hidden="true">★</span> \${e.rating}</div>
                        </div>
                        <div>
                            <p class="prop-desc-snippet" style="font-size: 15px; color: rgba(255,255,255,0.95); margin-bottom: 20px; line-height: 1.6; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; text-shadow: 0 1px 12px rgba(0,0,0,0.8);">\${e.description}</p>
                            <div class="prop-highlights">`;

const newSnippet2 = `
                        <div class="prop-card-top">
                            <div>
                                <h3 class="prop-title">\${t.title}</h3>
                                <p class="prop-location">\${t.location} · \${t.specs}</p>
                            </div>
                            <div class="prop-badge"><span class="star" aria-hidden="true">★</span> \${t.rating}</div>
                        </div>
                        <div>
                            <p class="prop-desc-snippet" style="font-size: 15px; color: rgba(255,255,255,0.95); margin-bottom: 20px; line-height: 1.6; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; text-shadow: 0 1px 12px rgba(0,0,0,0.8);">\${t.description}</p>
                            <div class="prop-highlights">`;

// Try to replace it using regex for flexibility
content = content.replace(/(<div class="prop-card-top">[\s\S]*?<div class="prop-badge"><span class="star" aria-hidden="true">★<\/span>\s*\$\{e\.rating\}<\/div>\s*<\/div>\s*<div>)\s*(<div class="prop-highlights">)/, `$1\n<p class="prop-desc-snippet" style="font-size: 15px; color: rgba(255,255,255,0.95); margin-bottom: 20px; line-height: 1.6; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; text-shadow: 0 1px 12px rgba(0,0,0,0.8);">\${e.description}</p>\n$2`);

content = content.replace(/(<div class="prop-card-top">[\s\S]*?<div class="prop-badge"><span class="star" aria-hidden="true">★<\/span>\s*\$\{t\.rating\}<\/div>\s*<\/div>\s*<div>)\s*(<div class="prop-highlights">)/, `$1\n<p class="prop-desc-snippet" style="font-size: 15px; color: rgba(255,255,255,0.95); margin-bottom: 20px; line-height: 1.6; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; text-shadow: 0 1px 12px rgba(0,0,0,0.8);">\${t.description}</p>\n$2`);

fs.writeFileSync(file, content, 'utf8');
console.log("Updated properties/index.html");
