import os

deploy_dir = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY'
html_files = [
    os.path.join(deploy_dir, 'index.html'),
]

for file_path in html_files:
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Fix the View all -> links
    old_span = 'style="color:var(--brand);cursor:pointer;font-weight:500"'
    new_span = 'style="color:var(--brand-dark);cursor:pointer;font-weight:500"'
    if old_span in content:
        content = content.replace(old_span, new_span)
        print(f"[{file_path}] Replaced inline brand color for a11y")
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
