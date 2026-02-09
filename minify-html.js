const fs = require('fs');
const path = require('path');
const { minify } = require('html-minifier-terser');

const deployDir = path.resolve(__dirname, 'DEPLOY THIS FOLDER TO NETLIFY');

// Configuration for html-minifier-terser
const minifyOptions = {
  collapseWhitespace: true,
  removeComments: true,
  minifyCSS: true,
  minifyJS: true,
  removeEmptyAttributes: true,
  removeRedundantAttributes: true,
  removeScriptTypeAttributes: true,
  removeStyleLinkTypeAttributes: true,
  useShortDoctype: true
};

function getAllHtmlFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);

  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      if (file !== 'node_modules' && file !== '.git') {
        getAllHtmlFiles(filePath, fileList);
      }
    } else {
      if (path.extname(file).toLowerCase() === '.html') {
        fileList.push(filePath);
      }
    }
  });

  return fileList;
}

async function optimize() {
  console.log(`Scanning for HTML files in ${deployDir}...`);
  if (!fs.existsSync(deployDir)) {
    console.error(`Directory not found: ${deployDir}`);
    return;
  }

  const htmlFiles = getAllHtmlFiles(deployDir);
  console.log(`Found ${htmlFiles.length} HTML files.`);

  let totalOriginalSize = 0;
  let totalMinifiedSize = 0;

  for (const file of htmlFiles) {
    try {
      const originalContent = fs.readFileSync(file, 'utf8');
      const originalSize = Buffer.byteLength(originalContent, 'utf8');
      
      const minifiedContent = await minify(originalContent, minifyOptions);
      const minifiedSize = Buffer.byteLength(minifiedContent, 'utf8');

      fs.writeFileSync(file, minifiedContent, 'utf8');

      totalOriginalSize += originalSize;
      totalMinifiedSize += minifiedSize;
      
      const savings = originalSize - minifiedSize;
      const percent = ((savings / originalSize) * 100).toFixed(2);
      
      console.log(`Minified ${path.basename(file)}: ${originalSize} -> ${minifiedSize} bytes (-${percent}%)`);
    } catch (err) {
      console.error(`Error minifying ${file}:`, err.message);
    }
  }

  const totalSavings = totalOriginalSize - totalMinifiedSize;
  const totalPercent = ((totalSavings / totalOriginalSize) * 100).toFixed(2);
  
  console.log('--- Summary ---');
  console.log(`Total Original: ${(totalOriginalSize / 1024).toFixed(2)} KB`);
  console.log(`Total Minified: ${(totalMinifiedSize / 1024).toFixed(2)} KB`);
  console.log(`Total Savings: ${(totalSavings / 1024).toFixed(2)} KB (-${totalPercent}%)`);
}

optimize();
