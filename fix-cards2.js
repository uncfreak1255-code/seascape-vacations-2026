const fs = require('fs');

function fixFile(path) {
    let content = fs.readFileSync(path, 'utf8');
    
    // Fix card height
    const oldCardCSS = '.prop-card{position:relative;border-radius:24px;overflow:hidden;cursor:pointer;height:520px;margin-bottom:32px;transform-style:preserve-3d;transition:transform .6s cubic-bezier(.175, .885, .32, 1.275)}';
    const newCardCSS = '.prop-card{position:relative;border-radius:24px;overflow:hidden;cursor:pointer;height:580px;margin-bottom:32px;transform-style:preserve-3d;transition:transform .6s cubic-bezier(.175, .885, .32, 1.275)}';
    content = content.replace(oldCardCSS, newCardCSS);
    
    fs.writeFileSync(path, content, 'utf8');
    console.log(`Fixed ${path}`);
}

fixFile('DEPLOY THIS FOLDER TO NETLIFY/index.html');
fixFile('DEPLOY THIS FOLDER TO NETLIFY/properties/index.html');

