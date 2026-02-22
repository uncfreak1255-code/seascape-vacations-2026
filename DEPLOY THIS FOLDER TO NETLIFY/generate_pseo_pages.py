import os
import re

base_file = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY/stays/pet-friendly-vacation-rentals-bradenton/index.html'

with open(base_file, 'r', encoding='utf-8') as f:
    template = f.read()

pages_data = [
    {
        "folder": "holmes-beach-vacation-rentals",
        "title": "Holmes Beach Vacation Rentals | Seascape Vacations",
        "desc": "Find the perfect Holmes Beach vacation rentals. Luxury homes with private pools, just steps from the pristine beaches of Anna Maria Island.",
        "h1": "Holmes Beach Vacation Rentals",
        "subtitle": "Discover luxury vacation homes in the heart of Anna Maria Island. Private pools, beachfront access, and family-friendly amenities.",
        "itemlist_name": "Holmes Beach Vacation Homes"
    },
    {
        "folder": "bradenton-beach-vacation-rentals",
        "title": "Bradenton Beach Vacation Rentals | Seascape Vacations",
        "desc": "Browse Bradenton Beach vacation rentals. Beautiful homes near Bridge Street and Coquina Beach with private pools and Gulf views.",
        "h1": "Bradenton Beach Vacation Rentals",
        "subtitle": "Stay steps away from Coquina Beach and Historic Bridge Street. Enjoy our luxury Bradenton Beach vacation homes with private pools.",
        "itemlist_name": "Bradenton Beach Vacation Homes"
    },
    {
        "folder": "longboat-key-vacation-rentals",
        "title": "Longboat Key Vacation Rentals | Seascape Vacations",
        "desc": "Luxury Longboat Key vacation rentals. Experience upscale island living with beachfront access, private docks, and resort-style amenities.",
        "h1": "Longboat Key Vacation Rentals",
        "subtitle": "Discover the elegance of Longboat Key with our premium vacation rentals offering white sand beaches and incredible sunsets.",
        "itemlist_name": "Longboat Key Vacation Homes"
    },
    {
        "folder": "vacation-rentals-near-siesta-key-beach",
        "title": "Vacation Rentals Near Siesta Key Beach | Seascape Vacations",
        "desc": "Explore top-rated vacation rentals near Siesta Key Beach. Luxury homes with private pools, short drive to the #1 beach in the USA.",
        "h1": "Vacation Rentals Near Siesta Key Beach",
        "subtitle": "Stay close to the world-famous quartz sands of Siesta Key while enjoying the privacy and luxury of our exclusive vacation homes.",
        "itemlist_name": "Vacation Homes Near Siesta Key"
    },
    {
        "folder": "sarasota-waterfront-vacation-rentals",
        "title": "Sarasota Waterfront Vacation Rentals | Seascape Vacations",
        "desc": "Stunning Sarasota waterfront vacation rentals. Enjoy private docks, bay views, and easy access to both downtown and local beaches.",
        "h1": "Sarasota Waterfront Vacation Rentals",
        "subtitle": "Wake up to breathtaking water views. Our Sarasota waterfront rentals feature private docks, heated pools, and close proximity to cultural attractions.",
        "itemlist_name": "Sarasota Waterfront Vacation Homes"
    },
    {
        "folder": "anna-maria-island-beachfront-rentals",
        "title": "Anna Maria Island Beachfront Rentals | Seascape Vacations",
        "desc": "Luxury Anna Maria Island beachfront rentals. Step right onto the sand from your private vacation home on the beautiful Gulf Coast.",
        "h1": "Anna Maria Island Beachfront Rentals",
        "subtitle": "Experience the ultimate beach getaway. Our Anna Maria Island beachfront rentals offer direct access to the sand and spectacular sunset views.",
        "itemlist_name": "Anna Maria Island Beachfront Homes"
    },
    {
        "folder": "vacation-rentals-with-boat-dock-anna-maria",
        "title": "Vacation Rentals With Boat Dock Anna Maria | Seascape Vacations",
        "desc": "Find Anna Maria Island vacation rentals with private boat docks. Perfect for fishing, boating, and enjoying the Florida Gulf Coast waterways.",
        "h1": "Anna Maria Vacation Rentals with Boat Docks",
        "subtitle": "Bring your boat! Our canal-front and bayfront vacation rentals feature private boat docks for easy access to world-class fishing and island hopping.",
        "itemlist_name": "Anna Maria Homes with Boat Docks"
    },
    {
        "folder": "monthly-vacation-rentals-florida-gulf-coast",
        "title": "Monthly Vacation Rentals Florida Gulf Coast | Snowbird Relocations",
        "desc": "Extended stay and monthly vacation rentals on the Florida Gulf Coast. Ideal for snowbirds seeking luxury winter escapes with heated pools.",
        "h1": "Monthly Vacation Rentals Florida Gulf Coast",
        "subtitle": "Escape the winter cold. Our premium monthly vacation rentals provide the perfect home-away-from-home for snowbirds and extended stays.",
        "itemlist_name": "Florida Gulf Coast Monthly Rentals"
    }
]

base_dir = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY/stays/'

for page in pages_data:
    new_html = template
    
    # Replacements
    new_html = re.sub(r'<title>.*?</title>', f'<title>{page["title"]}</title>', new_html)
    new_html = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{page["desc"]}">', new_html)
    
    # OG tags
    new_html = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{page["title"]}">', new_html)
    new_html = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{page["desc"]}">', new_html)
    new_html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="https://seascape-vacations.com/stays/{page["folder"]}/">', new_html)
    
    # Twitter tags
    new_html = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{page["title"]}">', new_html)
    new_html = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{page["desc"]}">', new_html)
    
    # Canonical
    new_html = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="https://seascape-vacations.com/stays/{page["folder"]}/">', new_html)
    
    # Breadcrumb schema
    new_html = re.sub(r'{"@type": "ListItem", "position": 2, "name": "[^"]*", "item": "[^"]*"}', f'{{"@type": "ListItem", "position": 2, "name": "{page["h1"]}", "item": "https://seascape-vacations.com/stays/{page["folder"]}/"}}', new_html)
    
    # ItemList schema name & description
    new_html = re.sub(r'"name": "Bradenton Pet-Friendly Vacation Homes"', f'"name": "{page["itemlist_name"]}"', new_html)
    new_html = re.sub(r'"description": "Bring your furry friend! Pet-friendly vacation rentals in Bradenton with private yards and pools."', f'"description": "{page["desc"]}"', new_html)
    
    # H1 and subtitle
    new_html = re.sub(r'<h1 style="font-size:clamp\(32px, 5vw, 48px\);margin-bottom:20px;color:#fff">.*?</h1>', f'<h1 style="font-size:clamp(32px, 5vw, 48px);margin-bottom:20px;color:#fff">{page["h1"]}</h1>', new_html)
    new_html = re.sub(r'<p style="max-width:700px;margin:0 auto;opacity:.9;font-size:18px">.*?</p>', f'<p style="max-width:700px;margin:0 auto;opacity:.9;font-size:18px">{page["subtitle"]}</p>', new_html)
    
    # Breadcrumb HTML (nav element)
    # The template has: <li><a href="/stays/">Stays</a></li><li style="color:var(--stone-light)">›</li><li style="color:var(--stone)" aria-current="page">Pet-Friendly Rentals in Bradenton</li>
    # Actually wait, I didn't grep the breadcrumb html in the script. Let's do a generic replace:
    new_html = re.sub(r'<li style="color:var\(--stone\)" aria-current="page">.*?</li>', f'<li style="color:var(--stone)" aria-current="page">{page["h1"]}</li>', new_html)
    
    target_folder = os.path.join(base_dir, page["folder"])
    os.makedirs(target_folder, exist_ok=True)
    with open(os.path.join(target_folder, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    print(f'Created {page["folder"]}/index.html')
