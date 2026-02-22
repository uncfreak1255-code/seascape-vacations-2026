const fs = require('fs');
const file = './DEPLOY THIS FOLDER TO NETLIFY/properties/index.html';
let content = fs.readFileSync(file, 'utf8');

// The click handler for the card might be: `onclick:()=>showPropertyDetail`
// Or something similar

// 1. Add slugifyTitle
if (!content.includes('function slugifyTitle(')) {
    content = content.replace('<body>', '<body><script>function slugifyTitle(e){return(e||"").toString().trim().toLowerCase().replace(/&/g,"and").replace(/[^a-z0-9]+/g,"-").replace(/-+/g,"-").replace(/^-|-$/g,"")}</script>');
}

// 2. Fix the "View Details" button href
// From <a href="${e.pageUrl||'/properties/'}"
content = content.replace(/<a href="\$\{([a-zA-Z]+)\.pageUrl\|\|'\/properties\/'\}"/g, '<a href="${$1.pageUrl || \'/properties/\' + slugifyTitle($1.title) + \'/\'}"');

// 3. Fix the card click
// From card.onclick=()=>{if(e.pageUrl){window.location.href=e.pageUrl}else{showPropertyDetail(e.id)}}
// or something like that. In minified code it's `onclick:()=>e.pageUrl?window.location.href=e.pageUrl:showPropertyDetail(e.id)`
const onclickRegex = /onclick\s*=\s*\(\)\s*=>\s*\{\s*if\s*\(\s*([a-zA-Z]+)\.pageUrl\s*\)\s*\{\s*window\.location\.href\s*=\s*\1\.pageUrl;\s*\}\s*else\s*\{\s*showPropertyDetail\(\1\.id\);\s*\}\s*\}/g;
let c = content.replace(onclickRegex, 'onclick=()=>{window.location.href=$1.pageUrl || "/properties/" + slugifyTitle($1.title) + "/"}');

const onclickRegex2 = /onclick=\(\)=>\s*([a-zA-Z]+)\.pageUrl\?window\.location\.href=\1\.pageUrl:showPropertyDetail\(\1\.id\)/g;
c = c.replace(onclickRegex2, 'onclick=()=>{window.location.href=$1.pageUrl || "/properties/" + slugifyTitle($1.title) + "/"}');

fs.writeFileSync(file, c, 'utf8');
console.log('Fixed link logic:', c !== content);
