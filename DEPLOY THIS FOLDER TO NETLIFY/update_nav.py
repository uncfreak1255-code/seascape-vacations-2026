import os
import glob
import re

directory = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY'
html_files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)

desktop_nav_content = """<div class="nav-dropdown-content">
    <a href="/area-guide-ami.html">Anna Maria Island</a>
    <a href="/area-guide-bradenton.html">Bradenton</a>
    <a href="/area-guide-bradenton-beach.html">Bradenton Beach</a>
    <a href="/area-guide-holmes-beach.html">Holmes Beach</a>
    <a href="/area-guide-longboat-key.html">Longboat Key</a>
    <a href="/area-guide-sarasota.html">Sarasota</a>
    <a href="/area-guide-siesta-key.html">Siesta Key</a>
</div>"""

mobile_standard = """<a href="/properties/" class="mobile-item">Properties</a>
    <span class="mobile-item" style="color:var(--brand);font-weight:600">Destinations</span>
    <a href="/area-guide-ami.html" class="mobile-item" style="padding-left:24px;font-size:14px">› Anna Maria Island</a>
    <a href="/area-guide-bradenton.html" class="mobile-item" style="padding-left:24px;font-size:14px">› Bradenton</a>
    <a href="/area-guide-bradenton-beach.html" class="mobile-item" style="padding-left:24px;font-size:14px">› Bradenton Beach</a>
    <a href="/area-guide-holmes-beach.html" class="mobile-item" style="padding-left:24px;font-size:14px">› Holmes Beach</a>
    <a href="/area-guide-longboat-key.html" class="mobile-item" style="padding-left:24px;font-size:14px">› Longboat Key</a>
    <a href="/area-guide-sarasota.html" class="mobile-item" style="padding-left:24px;font-size:14px">› Sarasota</a>
    <a href="/area-guide-siesta-key.html" class="mobile-item" style="padding-left:24px;font-size:14px">› Siesta Key</a>
    <a href="/?page=experiences" class="mobile-item">About Us</a>"""

success_count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Desktop replacement
    # Some have role="menu" or other attributes on the nav-dropdown-content
    new_content = re.sub(r'<div class="nav-dropdown-content"[^>]*>.*?</div>', desktop_nav_content, content, flags=re.DOTALL)
    
    # 2. Mobile replacement
    # We want to replace everything between the "Properties" link and the "About Us" link in the mobile menu
    # So we match <a ... href="/properties/" ...> ... <a ... href="/?page=experiences" ...>
    # and replace the whole block (including the endpoints) with our custom block
    # Note: Sometimes it's href="/properties/index.html" or similar.
    # We use a non-greedy match to find the block.
    mobile_pattern = r'<a[^>]*href="[/]?(?:properties|properties/index\.html)[^>]*>.*?</a>.*?(?:<a[^>]*href=".*?(?:page=experiences|about-us)[^>]*>.*?</a>)'
    new_mobile = re.sub(mobile_pattern, mobile_standard, new_content, flags=re.DOTALL | re.IGNORECASE)
    
    if new_mobile != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_mobile)
        success_count += 1
        print(f"Updated {file}")
    else:
        print(f"No changes made to {file}")

print(f"Successfully updated {success_count} files out of {len(html_files)}")
