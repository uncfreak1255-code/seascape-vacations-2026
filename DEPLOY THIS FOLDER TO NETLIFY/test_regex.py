import re
with open('/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY/the-oasis/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
# Find nav-dropdown-content
match = re.search(r'<div class="nav-dropdown-content"[^>]*>.*?</div>', content, flags=re.DOTALL)
if match:
    print("MATCHED:")
    print(match.group(0))
else:
    print("NO MATCH")
