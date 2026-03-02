import os

deploy_dir = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY'
html_files = [
    os.path.join(deploy_dir, 'index.html'),
    os.path.join(deploy_dir, 'properties/index.html'),
    os.path.join(deploy_dir, 'property-management/index.html')
]

updated_count = 0

for file_path in html_files:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modified = False
    
    # 1. FB Pixel
    fb_old = 'e.fbq||(a=e.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},e._fbq||(e._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],(o=t.createElement(n)).async=!0,o.src="https://connect.facebook.net/en_US/fbevents.js",(c=t.getElementsByTagName(n)[0]).parentNode.insertBefore(o,c)),fbq("init","2748551298816267"),fbq("track","PageView")},3000)'
    fb_new = '''var fbLoaded=false;function initFb(){if(fbLoaded)return;fbLoaded=!0;var e,t,n,a,o,c;e=window,t=document,n="script",e.fbq||(a=e.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},e._fbq||(e._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],(o=t.createElement(n)).async=!0,o.src="https://connect.facebook.net/en_US/fbevents.js",(c=t.getElementsByTagName(n)[0]).parentNode.insertBefore(o,c));fbq("init","2748551298816267");fbq("track","PageView")}window.addEventListener('scroll',initFb,{passive:!0,once:!0});window.addEventListener('mousemove',initFb,{passive:!0,once:!0});window.addEventListener('touchstart',initFb,{passive:!0,once:!0});setTimeout(initFb,4000)'''
    
    if fb_old in content:
        content = content.replace(fb_old, fb_new)
        print(f"[{file_path}] Replaced FB Pixel")
        modified = True
        
    # 2. Property Images
    img_old1 = '<img src="${property.imageBgUrl}" alt="${property.title}">'
    img_new1 = '<img src="${property.imageBgUrl}" alt="${property.title}" onerror="this.onerror=null; this.style.opacity=0;">'
    if img_old1 in content:
        content = content.replace(img_old1, img_new1)
        print(f"[{file_path}] Replaced imageBgUrl fallback")
        modified = True
        
    img_old2 = '<img src="${property.thumbnailUrl}" alt="${property.title}">'
    img_new2 = '<img src="${property.thumbnailUrl}" alt="${property.title}" onerror="this.onerror=null; this.style.opacity=0;">'
    if img_old2 in content:
        content = content.replace(img_old2, img_new2)
        print(f"[{file_path}] Replaced thumbnailUrl fallback")
        modified = True
        
    # 3. Contrast Ratios
    tag_old = '.section-tag{color:var(--brand)}'
    tag_new = '.section-tag{color:var(--brand-dark)}'
    if tag_old in content:
        content = content.replace(tag_old, tag_new)
        print(f"[{file_path}] Replaced contrast ratio for section-tag")
        modified = True
        
    brand_old = 'color:var(--brand);'
    brand_new = 'color:var(--brand-dark);'
    # we don't apply this blindly to avoid breaking buttons or valid uses
        
    # 4. Hero AVIF
    hero_tag = '<div class="hero-bg"></div>'
    hero_html = '''<div class="hero-bg-wrapper" style="position: absolute; inset: 0; overflow: hidden; z-index: 1;">
            <picture style="width: 100%; height: 100%; display: block;">
              <source srcset="/hero-optimized.avif" type="image/avif" media="(min-width: 769px)">
              <source srcset="/hero-mobile.avif" type="image/avif" media="(max-width: 768px)">
              <source srcset="/hero-optimized.webp" type="image/webp" media="(min-width: 769px)">
              <source srcset="/hero-mobile.webp" type="image/webp" media="(max-width: 768px)">
              <source srcset="/hero-optimized.jpg" type="image/jpeg" media="(min-width: 769px)">
              <source srcset="/hero-mobile.jpg" type="image/jpeg" media="(max-width: 768px)">
              <img src="/hero-optimized.webp" alt="Seascape Vacations" fetchpriority="high" decoding="async" style="width: 100%; height: 100%; object-fit: cover; animation: heroZoom 20s ease-in-out infinite alternate;">
            </picture>
          </div>'''.replace('\n', '').replace('  ', '')
          
    if hero_tag in content:
        content = content.replace(hero_tag, hero_html)
        print(f"[{file_path}] Replaced hero-bg with picture element")
        modified = True
        
    hero_style = ".hero-bg{position:absolute;inset:0;background-size:cover;background-position:center;transform:scale(1.1);animation:heroZoom 20s ease-in-out infinite alternate;background-image:url('hero-optimized.webp')}"
    if hero_style in content:
        content = content.replace(hero_style, '')
        print(f"[{file_path}] Removed basic hero style")
        modified = True
        
    mob_style = "@media (max-width:768px){.hero-bg{background-image:url('hero-mobile.webp')}}"
    if mob_style in content:
        content = content.replace(mob_style, '')
        print(f"[{file_path}] Removed mobile hero style")
        modified = True
        
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1
        
print(f"Python script finished. Updated {updated_count} files.")
