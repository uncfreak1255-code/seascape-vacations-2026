const fs = require('fs');
const file = './DEPLOY THIS FOLDER TO NETLIFY/properties/index.html';
let content = fs.readFileSync(file, 'utf8');

// Insert slugifyTitle
if (!content.includes('function slugifyTitle(')) {
    const slugifyHtml = 'function slugifyTitle(title){return(title||"").toString().trim().toLowerCase().replace(/&/g,"and").replace(/[^a-z0-9]+/g,"-").replace(/-+/g,"-").replace(/^-|-$/g,"")}';
    content = content.replace('function optimizePropertyImages(', slugifyHtml + 'function optimizePropertyImages(');
}

// Add pageUrl to mapped object
content = content.replace(/imagesThumb:\([a-zA-Z]+\.images\|\|\[\]\)\.map\(\([a-zA-Z]+\)=>optimizeImage\([a-zA-Z]+,400\)\)/g, '$&,pageUrl:$&.split(".images")[0] + ".pageUrl||`/properties/${slugifyTitle(" + $&.split(".images")[0] + ".title)}/`"');

// Wait, doing $&.split string manipulation inside replace is JS logic applied to string literal? No, that's not how regex replace works.

fs.writeFileSync('temp.js', '');
