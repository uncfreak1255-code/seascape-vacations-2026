const fs=require('fs');
let c=fs.readFileSync('./DEPLOY THIS FOLDER TO NETLIFY/properties/index.html','utf8');
if(!c.includes('function slugifyTitle(')){
  c=c.replace('function optimizePropertyImages(','function slugifyTitle(t){return(t||"").toString().trim().toLowerCase().replace(/&/g,"and").replace(/[^a-z0-9]+/g,"-").replace(/-+/g,"-").replace(/^-|-$/g,"")}function optimizePropertyImages(');
}
// Find the exact mapping logic
const regex = /imagesThumb:\(([a-zA-Z]+)\.images\|\|\[\]\)\.map\(\([a-zA-Z]+\)=>optimizeImage\([a-zA-Z]+,400\)\)/g;
let replaced = false;
c = c.replace(regex, (match, varName) => {
  replaced = true;
  return match + ',pageUrl:' + varName + '.pageUrl||`/properties/${slugifyTitle(' + varName + '.title)}/`'; 
});
fs.writeFileSync('./DEPLOY THIS FOLDER TO NETLIFY/properties/index.html', c, 'utf8');
console.log('Fixed properties pageUrls. Replaced?', replaced);
