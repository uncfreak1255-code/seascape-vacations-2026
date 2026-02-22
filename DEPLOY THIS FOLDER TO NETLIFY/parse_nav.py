import os
import glob
import re

directory = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY'
html_files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)

desktop_navs = set()
mobile_navs = set()

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # Desktop
        desktop_match = re.search(r'<div class="nav-dropdown-content"[^>]*>(.*?)</div>', content, re.DOTALL)
        if desktop_match:
            desktop_navs.add(desktop_match.group(1).strip())
            
        # Mobile
        mobile_match = re.search(r'(<span[^>]*>Destinations</span>.*?)(?:<a[^>]*>About Us|<a[^>]*href="/\?page=experiences")', content, re.DOTALL | re.IGNORECASE)
        if mobile_match:
            mobile_navs.add(mobile_match.group(1).strip())

print("--- Desktop Nav Variations ---")
for n in desktop_navs:
    print(n)
    print("-------")
    
print("\n--- Mobile Nav Variations ---")
for n in mobile_navs:
    print(n)
    print("-------")
