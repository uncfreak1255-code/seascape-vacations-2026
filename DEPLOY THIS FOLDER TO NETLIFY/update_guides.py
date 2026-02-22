import re
import os

base_dir = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY'

guides_data = [
    {
        'file': 'area-guide-holmes-beach.html',
        'links': [
            {'url': '/stays/holmes-beach-vacation-rentals/', 'text': 'Holmes Beach Vacation Rentals'},
            {'url': '/stays/family-vacation-rentals-anna-maria-island/', 'text': 'Family Vacation Rentals Near AMI'},
            {'url': '/stays/vacation-rentals-with-heated-pool/', 'text': 'Holmes Beach Rentals with Heated Pools'}
        ]
    },
    {
        'file': 'area-guide-bradenton-beach.html',
        'links': [
            {'url': '/stays/bradenton-beach-vacation-rentals/', 'text': 'Bradenton Beach Vacation Rentals'},
            {'url': '/stays/coquina-beach-vacation-rentals/', 'text': 'Coquina Beach Rentals'},
            {'url': '/stays/vacation-rentals-with-boat-dock-anna-maria/', 'text': 'Rentals with Boat Docks'}
        ]
    },
    {
        'file': 'area-guide-longboat-key.html',
        'links': [
            {'url': '/stays/longboat-key-vacation-rentals/', 'text': 'Longboat Key Vacation Rentals'},
            {'url': '/stays/luxury-vacation-rentals-sarasota/', 'text': 'Luxury Sarasota Rentals'},
            {'url': '/stays/sarasota-waterfront-vacation-rentals/', 'text': 'Waterfront Rentals Near Longboat Key'}
        ]
    }
]

style_block = """<style>
.guide-related-stays { padding: 30px 0; background: #f8f9fa; margin: 30px 0; border-radius: 12px; }
.guide-related-stays .container { max-width: 800px; margin: 0 auto; padding: 0 20px; }
.guide-related-stays h3 { font-size: 20px; color: var(--brand-dark, #2c3e50); margin-bottom: 15px; }
.guide-related-stays ul { list-style: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 10px; }
.guide-related-stays a { display: block; padding: 12px 16px; background: #fff; border-radius: 8px; color: var(--brand-dark, #2c3e50); text-decoration: none; font-size: 14px; border: 1px solid #e8e8e8; transition: all 0.2s; }
.guide-related-stays a:hover { background: var(--brand-gold, #c1b196); color: #fff; border-color: var(--brand-gold, #c1b196); }
.guide-footer { text-align: center; padding: 40px 24px; color: var(--stone-light); font-size: 14px; }
.guide-footer a { color: var(--brand); text-decoration: none; }
</style>"""

for data in guides_data:
    filepath = os.path.join(base_dir, data['file'])
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} - not found")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if already has related stays
    if 'guide-related-stays' in content:
        print(f"Already updated {filepath}")
        continue
        
    links_html = "".join([f'<li><a href="{l["url"]}">{l["text"]}</a></li>' for l in data['links']])
    
    inject_html = f"""
{style_block}
<div class="guide-related-stays">
    <div class="container">
        <h3>Related Vacation Rentals</h3>
        <ul>
            {links_html}
        </ul>
    </div>
</div>
<footer class="guide-footer">
    <p>© 2025 Seascape Vacations · <a href="https://seascape-vacations.com">seascape-vacations.com</a></p>
</footer>
</body>"""

    content = re.sub(r'</section>\s*</body>', f'</section>{inject_html}', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filepath}")

