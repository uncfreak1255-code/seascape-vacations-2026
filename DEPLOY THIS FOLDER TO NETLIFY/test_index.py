import re

file = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY/index.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

print("Original content sample:")
print(content[content.find('nav-dropdown-content'):content.find('nav-dropdown-content')+200])

desktop_nav_content = """<div class="nav-dropdown-content">
    <a href="/area-guide-ami.html">Anna Maria Island</a>
    <a href="/area-guide-bradenton.html">Bradenton</a>
    <a href="/area-guide-bradenton-beach.html">Bradenton Beach</a>
    <a href="/area-guide-holmes-beach.html">Holmes Beach</a>
    <a href="/area-guide-longboat-key.html">Longboat Key</a>
    <a href="/area-guide-sarasota.html">Sarasota</a>
    <a href="/area-guide-siesta-key.html">Siesta Key</a>
</div>"""

pattern = r'<div class="nav-dropdown-content"[^>]*>.*?</div>'
new_content = re.sub(pattern, desktop_nav_content, content, flags=re.DOTALL)

if new_content != content:
    print("Desktop replaced")
else:
    print("Desktop NOT replaced")

mobile_pattern = r'<a[^>]*href="[/]?(?:properties|properties/index\.html)[^>]*>.*?</a>.*?(?:<a[^>]*href=".*?(?:page=experiences|about-us)[^>]*>.*?</a>)'

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

new_mobile = re.sub(mobile_pattern, mobile_standard, new_content, flags=re.DOTALL | re.IGNORECASE)

if new_mobile != new_content:
    print("Mobile replaced")
else:
    print("Mobile NOT replaced")

