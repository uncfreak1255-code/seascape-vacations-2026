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

mobile_destinations = """<span class="mobile-item" style="color:var(--brand);font-weight:600">Destinations</span>
    <a href="/area-guide-ami.html" class="mobile-item" style="padding-left:24px;font-size:14px">› Anna Maria Island</a>
    <a href="/area-guide-bradenton.html" class="mobile-item" style="padding-left:24px;font-size:14px">› Bradenton</a>
    <a href="/area-guide-bradenton-beach.html" class="mobile-item" style="padding-left:24px;font-size:14px">› Bradenton Beach</a>
    <a href="/area-guide-holmes-beach.html" class="mobile-item" style="padding-left:24px;font-size:14px">› Holmes Beach</a>
    <a href="/area-guide-longboat-key.html" class="mobile-item" style="padding-left:24px;font-size:14px">› Longboat Key</a>
    <a href="/area-guide-sarasota.html" class="mobile-item" style="padding-left:24px;font-size:14px">› Sarasota</a>
    <a href="/area-guide-siesta-key.html" class="mobile-item" style="padding-left:24px;font-size:14px">› Siesta Key</a>"""

count = 0
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = re.sub(r'<div class="nav-dropdown-content"[^>]*>.*?</div>', desktop_nav_content, content, flags=re.DOTALL)
        
        # Replace the Destinations mobile span and the links following it up until, and including, Siesta Key.
        # This will work for all pages that have the 'Destinations' span.
        mobile_pattern = r'<span[^>]*>\s*Destinations\s*</span>.*?Siesta Key[^<]*</a>'
        new_mobile = re.sub(mobile_pattern, mobile_destinations, new_content, flags=re.DOTALL | re.IGNORECASE)
        
        if file.endswith('properties/index.html') or file.endswith('/index.html'):
            # Also catch if some pages use <a>Destinations</a>
            a_mobile_pattern = r'<a[^>]*>\s*Destinations\s*</a>.*?Siesta Key[^<]*</a>'
            new_mobile = re.sub(a_mobile_pattern, mobile_destinations, new_mobile, flags=re.DOTALL | re.IGNORECASE)
        
        # One last ditch attempt for ones that completely missed the Destinations span/a due to formatting
        # Some had NO Destinations span in mobile menu and just threw the links under Properties! Look at my original Oasis.
        fallback_pattern = r'(<a[^>]*href="[/]?(?:area-guide-ami|area-guide-bradenton)[^>]*>.*?Anna Maria Island.*?Siesta Key[^<]*</a>)'
        if 'Destinations' not in new_mobile and 'Anna Maria Island' in new_mobile and 'Siesta Key' in new_mobile:
             new_mobile = re.sub(fallback_pattern, mobile_destinations, new_mobile, flags=re.DOTALL | re.IGNORECASE)


        if new_mobile != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_mobile)
            print(f"Updated {file}")
            count += 1
    except Exception as e:
        print(f"Failed processing {file}: {e}")

print(f"Done. Updated {count} out of {len(html_files)}")
