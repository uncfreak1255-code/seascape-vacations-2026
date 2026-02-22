import re
import os

base_dir = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY/properties'
properties = ['dockside-dreams', 'the-oasis', 'bradenton-pool-home', 'sarasota-luxe']

# Build the sections to inject
section_html = """
<style>
.prop-internal-links { padding: 60px 24px; background: var(--cream); margin-top: 40px; border-top: 1px solid rgba(0,0,0,0.05); }
.prop-internal-links .container { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }
.prop-internal-links h3 { font-family: 'Playfair Display', serif; font-size: 24px; color: var(--brand-dark); margin-bottom: 20px; border-bottom: 2px solid var(--gold); padding-bottom: 10px; display: inline-block; }
.prop-links-list { list-style: none; padding: 0; }
.prop-links-list li { margin-bottom: 12px; }
.prop-links-list a { color: var(--stone); text-decoration: none; font-size: 15px; display: flex; align-items: center; gap: 8px; transition: color 0.3s ease; }
.prop-links-list a:hover { color: var(--brand); }
.prop-links-list a::before { content: '→'; color: var(--gold); }
@media (max-width: 768px) { .prop-internal-links .container { grid-template-columns: 1fr; } }
</style>
<div class="prop-internal-links">
    <div class="container">
        <div>
            <h3>Related Properties</h3>
            <ul class="prop-links-list">
                <li><a href="/stays/beach-house-rentals-florida-gulf-coast/">Florida Gulf Coast Beach Houses</a></li>
                <li><a href="/stays/family-vacation-rentals-anna-maria-island/">Family Rentals Near Anna Maria Island</a></li>
                <li><a href="/stays/vacation-rentals-with-heated-pool/">Vacation Rentals with Heated Pools</a></li>
                <li><a href="/stays/vacation-rentals-with-boat-dock-anna-maria/">Rentals with Boat Docks</a></li>
            </ul>
        </div>
        <div>
            <h3>Nearby Attractions & Guides</h3>
            <ul class="prop-links-list">
                <li><a href="/area-guide-ami.html">Anna Maria Island Area Guide</a></li>
                <li><a href="/area-guide-bradenton.html">Bradenton Area Guide</a></li>
                <li><a href="/guides/anna-maria-island-beaches.html">Ultimate Beach Guide</a></li>
                <li><a href="/guides/fishing-guide-anna-maria-sarasota.html">Fishing Charters & Piers</a></li>
            </ul>
        </div>
    </div>
</div>
"""

for prop in properties:
    filepath = os.path.join(base_dir, prop, 'index.html')
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} - not found")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'prop-internal-links' in content:
        print(f"Already updated {filepath}")
        continue

    # Inject right before the first <footer
    content = re.sub(r'(<footer)', lambda m: section_html + m.group(1), content, count=1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filepath}")

