import os
import re

guides_dir = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY/guides'

tldr_style = """
<style>
.ai-tldr {
    background: #f0f7f7;
    border-left: 4px solid var(--brand, #5f8a8b);
    padding: 20px;
    margin: 0 0 30px 0;
    border-radius: 0 8px 8px 0;
    font-size: 16px;
    line-height: 1.6;
}
.ai-tldr strong {
    font-family: 'Playfair Display', serif;
    color: var(--brand-dark, #3d5c5d);
    font-size: 18px;
    display: block;
    margin-bottom: 8px;
}
</style>
"""

# Process all html files in guides
for filename in os.listdir(guides_dir):
    if not filename.endswith('.html'):
        continue
        
    filepath = os.path.join(guides_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'ai-tldr' in content:
        print(f"Skipping {filename} - already has TL;DR")
        continue

    # Extract meta description
    meta_desc_match = re.search(r'<meta name="description" content="([^"]+)">', content)
    if not meta_desc_match:
        print(f"Skipping {filename} - no meta description found")
        continue
        
    desc = meta_desc_match.group(1)
    
    # Create TL;DR box
    tldr_box = f"""{tldr_style}
<div class="ai-tldr">
    <strong>TL;DR Quick Summary</strong>
    {desc}
</div>
"""

    # Inject immediately after <div class="guide-content">
    content = re.sub(r'(<div class="guide-content">)', lambda m: m.group(1) + "\n" + tldr_box, content, count=1)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Added TL;DR to {filename}")

