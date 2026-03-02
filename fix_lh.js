const fs = require('fs');
const path = require('path');

const deployDir = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY';
const htmlFiles = [
  path.join(deployDir, 'index.html'),
  path.join(deployDir, 'properties/index.html'),
  path.join(deployDir, 'property-management/index.html')
];

let updatedCount = 0;

for (const file of htmlFiles) {
  if (!fs.existsSync(file)) continue;
  
  let content = fs.readFileSync(file, 'utf8');
  let originalContent = content;

  // 1. FB Pixel interactions (defer pixel) -> use exact string match
  const fbOld = 'setTimeout(function(){var e,t,n,a,o,c;e=window,t=document,n="script",e.fbq||(a=e.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},e._fbq||(e._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],(o=t.createElement(n)).async=!0,o.src="https://connect.facebook.net/en_US/fbevents.js",(c=t.getElementsByTagName(n)[0]).parentNode.insertBefore(o,c)),fbq("init","2748551298816267"),fbq("track","PageView")},3000)';

  const fbNew = `
  var fbLoaded=false;function initFb(){if(fbLoaded)return;fbLoaded=!0;var e,t,n,a,o,c;e=window,t=document,n="script",e.fbq||(a=e.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},e._fbq||(e._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],(o=t.createElement(n)).async=!0,o.src="https://connect.facebook.net/en_US/fbevents.js",(c=t.getElementsByTagName(n)[0]).parentNode.insertBefore(o,c));fbq("init","2748551298816267");fbq("track","PageView")}
  window.addEventListener('scroll',initFb,{passive:!0,once:!0});
  window.addEventListener('mousemove',initFb,{passive:!0,once:!0});
  window.addEventListener('touchstart',initFb,{passive:!0,once:!0});
  setTimeout(initFb,4000)
  `.replace(/\n\s*/g, '');
  
  content = content.split(fbOld).join(fbNew);

  // 2. property image fallback to display:none if WP breaks the URL
  const imgOld1 = '<img src="${property.imageBgUrl}" alt="${property.title}">';
  const imgNew1 = '<img src="${property.imageBgUrl}" alt="${property.title}" onerror="this.onerror=null; this.style.opacity=0;">';
  content = content.split(imgOld1).join(imgNew1);

  // Maybe properties has a slightly different syntax without 'BgUrl'? Let's replace just standard dynamically injected images that don't have onerror
  // Actually, wait: index.html has '<img src="${property.imageBgUrl}" alt="${property.title}">' or similar.
  // We can just rely on the exact string `<img src="${property.thumbnailUrl}" alt="${property.title}">` -- wait, I will check the live source via diff if this fails.
  const imgOld2 = '<img src="${property.thumbnailUrl}" alt="${property.title}">';
  const imgNew2 = '<img src="${property.thumbnailUrl}" alt="${property.title}" onerror="this.onerror=null; this.style.opacity=0;">';
  content = content.split(imgOld2).join(imgNew2);

  // 3. Contrast ratios
  content = content.split('.section-tag{color:var(--brand)}').join('.section-tag{color:var(--brand-dark)}');

  // 4. Hero image AVIF & object-fit instead of CSS bg
  const heroBgTag = '<div class="hero-bg"></div>';
  const pictureHtml = `
  <div class="hero-bg-wrapper" style="position: absolute; inset: 0; overflow: hidden; z-index: 1;">
    <picture style="width: 100%; height: 100%; display: block;">
      <source srcset="/hero-optimized.avif" type="image/avif" media="(min-width: 769px)">
      <source srcset="/hero-mobile.avif" type="image/avif" media="(max-width: 768px)">
      <source srcset="/hero-optimized.webp" type="image/webp" media="(min-width: 769px)">
      <source srcset="/hero-mobile.webp" type="image/webp" media="(max-width: 768px)">
      <img src="/hero-optimized.webp" alt="Seascape Vacations" fetchpriority="high" decoding="async" style="width: 100%; height: 100%; object-fit: cover; animation: heroZoom 20s ease-in-out infinite alternate;">
    </picture>
  </div>
  `.replace(/\n\s*/g, '');
  content = content.split(heroBgTag).join(pictureHtml);
  
  const heroStyle = ".hero-bg{position:absolute;inset:0;background-size:cover;background-position:center;transform:scale(1.1);animation:heroZoom 20s ease-in-out infinite alternate;background-image:url('hero-optimized.webp')}";
  content = content.split(heroStyle).join('');
  
  const mobileStyle = "@media (max-width:768px){.hero-bg{background-image:url('hero-mobile.webp')}}";
  content = content.split(mobileStyle).join('');

  if (content !== originalContent) {
    fs.writeFileSync(file, content, 'utf8');
    console.log('Updated', file);
    updatedCount++;
  }
}

console.log('Files updated:', updatedCount);
