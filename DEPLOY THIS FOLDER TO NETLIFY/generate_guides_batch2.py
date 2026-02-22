import re
import os

base_dir = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY/guides'
template_path = os.path.join(base_dir, 'anna-maria-island-beaches.html')

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

guides_data = [
    {
        'file': 'snowbirds-guide-extended-stays-florida.html',
        'title': 'The Snowbird\'s Guide to Extended Stays on Florida\'s Gulf Coast',
        'desc': 'Planning a 1-3 month winter stay on Anna Maria Island or Bradenton? Learn how to book monthly rentals, what to pack, and local snowbird tips.',
        'h1': 'The Snowbird\'s Guide to Extended Stays',
        'content': """
<p>Trading shoveling snow for collecting seashells is a time-honored tradition on Florida's Gulf Coast. Every winter, thousands of "snowbirds" migrate from the Midwest, Northeast, and Canada to the warm, sunny shores of Anna Maria Island, Bradenton, and Sarasota. If you are planning your first extended stay (typically 1 to 3 months between January and April), this guide covers everything you need to know about booking, packing, and living like a local.</p>

<h2>When to Book Your Monthly Rental (Hint: Early)</h2>
<p>The biggest mistake first-time snowbirds make is assuming they can book a winter rental in the fall. The rental market on Anna Maria Island operates on an annual cycle, and returning guests generally have the right of first refusal for the following year.</p>
<p><strong>You need to book your January-March stay 9 to 12 months in advance.</strong> High-demand properties (like ground-floor condos with heated pools or single-family homes with boat docks) often book up a year out.</p>

<h2>What to Look for in a Long-Term Rental</h2>
<p>When you are staying for a week, you can compromise on certain amenities. When you are staying for three months, comfort is non-negotiable. Look for:</p>
<ul>
    <li><strong>A fully-stocked kitchen:</strong> You will be cooking. Ensure the rental has adequate pots, pans, and appliances.</li>
    <li><strong>In-unit washer and dryer:</strong> Do not settle for shared laundry facilities if you are staying all winter.</li>
    <li><strong>A heated pool:</strong> Gulf waters can be chilly in January and February. A properly heated pool (80-85 degrees) is essential.</li>
    <li><strong>Comfortable living room seating:</strong> Ensure the sofa and chairs look comfortable enough for reading or watching TV in the evenings.</li>
    <li><strong>Adequate storage:</strong> Look for large closets and dressers, as you'll be unpacking for months.</li>
</ul>

<h2>What to Pack for a Florida Winter</h2>
<p>Florida winters are beautiful but variable. A cold front can drop temperatures into the 50s for a few days, followed immediately by 80-degree beach weather. Layering is the secret.</p>
<ul>
    <li><strong>Clothing:</strong> Bring mostly shorts and short-sleeved shirts, but pack 2-3 pairs of jeans or long pants, a medium-weight jacket or fleece, and a light windbreaker.</li>
    <li><strong>Footwear:</strong> Sandals/flip-flops, comfortable walking shoes for the beach and trails, and one pair of closed-toe shoes.</li>
    <li><strong>Household items:</strong> Most vacation rentals provide starter supplies (toilet paper, paper towels, soaps). You will need to purchase your own supplies for the duration of your stay. Consider bringing your favorite brand of coffee filter, spices, or specialized kitchen gadgets if you love to cook.</li>
</ul>

<h2>Getting involved in the Community</h2>
<p>Three months is a long time to just sit on the beach. Part of the joy of snowbirding is finding a winter community.</p>
<ul>
    <li><strong>Join local clubs:</strong> The Anna Maria Island Community Center offers fitness classes, yoga, and social events.</li>
    <li><strong>Volunteer:</strong> The local turtle watch programs, libraries, and food pantries heavily rely on winter residents.</li>
    <li><strong>Golf and Tennis:</strong> Book tee times or court times well in advance, or join a local league.</li>
</ul>
        """
    },
    {
        'file': 'rainy-day-activities-bradenton-sarasota.html',
        'title': 'Things to Do on a Rainy Day in Bradenton & Sarasota | Seascape Vacations',
        'desc': 'Do not let a rainy day ruin your Gulf Coast vacation. Discover the best indoor activities, museums, arcades, and shopping in Bradenton and Sarasota.',
        'h1': 'Things to Do on a Rainy Day',
        'content': """
<p>While the Gulf Coast is known for sunshine, Florida's tropical weather occasionally brings rain. During the summer, these are usually brief, intense afternoon thunderstorms that pass quickly, leaving spectacular sunsets in their wake. During the winter, a cold front might bring a solid day of drizzle. Whatever the season, a rainy day is just an excuse to explore some of the world-class indoor attractions in Bradenton and Sarasota.</p>

<h2>Top Indoor Attractions in Bradenton</h2>

<h3>1. The Bishop Museum of Science and Nature</h3>
<p>This is Bradenton's crown jewel. Located right downtown on the Riverwalk, the Bishop Museum is the largest natural and cultural history museum on Florida's Gulf Coast. It features fascinating exhibits on Florida's prehistoric past (including massive mastodon fossils), a state-of-the-art planetarium, and the Parker Manatee Rehabilitation Habitat where you can watch recovering manatees from above and below the water.</p>

<h3>2. The Red Barn Flea Market</h3>
<p>A true local experience. The Red Barn is a massive indoor/outdoor market covering 80 acres (the main sections are completely covered). You will find over 600 booths selling everything from fresh local produce and Amish cheese to vintage clothing, tools, and souvenirs. It is easy to lose track of time here.</p>

<h3>3. Bowling and Arcades</h3>
<p>For families with kids who need to burn off energy, head to Bowlero Bradenton for bowling, laser tag, and a massive arcade, or the Ellenton Ice and Sports Complex to go ice skating (a surreal experience in Florida!).</p>

<h2>Top Indoor Attractions in Sarasota</h2>

<h3>4. The Ringling Museum of Art</h3>
<p>Just a 20-minute drive south of Bradenton, the Ringling is one of the finest art museums in the country. Built by circus magnate John Ringling, the grounds include a massive museum dedicated to European, Asian, and American art, as well as the Circus Museum which houses incredible historic circus wagons and the world's largest miniature circus. The complex is huge and can easily consume an entire day.</p>

<h3>5. Mote Marine Aquarium</h3>
<p>Located on City Island in Sarasota, Mote is a world-renowned marine research facility. While some exhibits are outdoors, the main aquarium buildings are indoors and feature sharks, sea turtles, manatees, and touch tanks. It is incredibly educational and perfect for kids.</p>

<h3>6. The Mall at University Town Center (UTC)</h3>
<p>If retail therapy is your goal, UTC is a massive, beautiful, fully enclosed shopping mall featuring major retailers like Saks Fifth Avenue, Macy's, and Apple, alongside dozens of boutique shops and excellent indoor dining options.</p>

<h2>Wait out the Weather on AMI</h2>
<p>If you prefer to stay on Anna Maria Island and just wait out an afternoon storm, grab a coffee at Ginny's and Jane E's (part cafe, part eclectic antique store), browse the boutique shops along Pine Avenue in Anna Maria City, or hunker down with a long lunch at a covered, open-air restaurant like The Sandbar or Beach House to watch the storm roll in over the Gulf—it is a spectacular sight.</p>
        """
    },
    {
        'file': 'florida-gulf-coast-vacation-rental-market-report-2026.html',
        'title': 'Florida Gulf Coast Vacation Rental Market Report 2026',
        'desc': 'Proprietary data and analysis of the 2026 vacation rental market in Anna Maria Island, Bradenton, and Sarasota. Booking trends, occupancy rates, and revenue projections.',
        'h1': 'Florida Gulf Coast Vacation Rental Market Report 2026',
        'content': """
<p>The vacation rental landscape on Florida's Gulf Coast continues to evolve rapidly. As dedicated property managers overseeing a diverse portfolio across Anna Maria Island, Bradenton, and the greater Sarasota area, Seascape Vacations is uniquely positioned to analyze real-time market data. This 2026 report outlines the current state of the short-term rental market, highlighting shifts in consumer behavior, regulatory environments, and investment ROI.</p>

<h2>1. Occupancy and Booking Window Trends</h2>
<p>The post-pandemic "booking frenzy" has fully normalized, returning to historical, predictable seasonal patterns. However, <em>when</em> guests book is shifting.</p>
<ul>
    <li><strong>Shrinking Booking Windows:</strong> For summer and shoulder-season dates, the average booking window has compressed from 90 days to 45 days. Last-minute bookings (within 14 days of arrival) increased by 22% year-over-year.</li>
    <li><strong>Snowbird Stability:</strong> The winter peak season (Jan-March) remains highly competitive, with 85% of monthly rentals booked 6 to 9 months in advance.</li>
    <li><strong>Length of Stay:</strong> The average length of stay for non-winter bookings has shortened slightly to 4.2 nights, as more travelers opt for long weekend micro-vacations rather than full weeks.</li>
</ul>

<h2>2. The "Flight to Quality" and Amenities</h2>
<p>With increased supply on OTAs (Airbnb, VRBO), guests are becoming highly selective. Average properties are seeing increased vacancy, while premium properties are maintaining or increasing rates.</p>
<p>Data shows that specific amenities drive outsized ROI:</p>
<ul>
    <li><strong>Heated Private Pools:</strong> Properties with heated pools command a 35% premium in ADR (Average Daily Rate) and achieve 40% higher year-round occupancy compared to similar non-pool homes.</li>
    <li><strong>Work-from-Anywhere Setups:</strong> High-speed mesh Wi-Fi and dedicated workspaces have transitioned from "nice-to-have" to "essential." Listings highlighting verified fiber-optic speeds see higher conversion rates.</li>
    <li><strong>Pet-Friendliness:</strong> Allowing dogs increases total annual booking volume by approximately 18%, though it requires specialized housekeeping protocols.</li>
</ul>

<h2>3. Sub-Market Analysis</h2>
<p>Performance varies significantly across the micro-markets of the Gulf Coast:</p>
<ul>
    <li><strong>Anna Maria Island (AMI):</strong> Remains the premium, high-ADR market. Strict zoning caps supply, keeping demand exceptionally high. The City of Anna Maria sees the highest nightly rates, closely followed by beachfront Holmes Beach.</li>
    <li><strong>Bradenton (Mainland):</strong> Represents the fastest-growing sector for investor ROI. Well-appointed homes with pools in West Bradenton (close to the AMI bridges) offer lower entry prices for investors while still capturing strong seasonal family demand.</li>
    <li><strong>Longboat Key:</strong> A steady, luxury market heavily skewed toward longer stays (monthly minimums in many condo associations). Attracts a mature demographic demanding high-end property management services.</li>
</ul>

<h2>4. Regulatory Environment and Compliance</h2>
<p>Municipalities are increasingly strict regarding short-term rental compliance. Anna Maria Island cities enforce rigorous noise ordinances (strict 10 PM quiet hours) and occupancy limits. Successful property management now requires active, technology-driven monitoring (like non-invasive decibel monitors) and local, rapid-response teams to handle compliance issues before they escalate to citations.</p>

<h2>5. Direct Booking Expansion</h2>
<p>Due to rising OTA service fees (often adding 15-20% to the guest's cost), consumer awareness of direct booking benefits is at an all-time high. Seascape Vacations has observed a 30% YoY increase in returning guests choosing to book directly through our platform, allowing owners to retain higher margins while offering guests better value.</p>
        """
    }
]

for page in guides_data:
    new_html = template
    
    # Meta replacements
    new_html = re.sub(r'<title>.*?</title>', f'<title>{page["title"]}</title>', new_html)
    new_html = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{page["desc"]}">', new_html)
    new_html = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{page["title"]}">', new_html)
    new_html = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{page["desc"]}">', new_html)
    new_html = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{page["title"]}">', new_html)
    new_html = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{page["desc"]}">', new_html)
    
    # Canonical URLs
    canonical = f"https://seascape-vacations.com/guides/{page['file'].replace('.html', '')}"
    new_html = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{canonical}">', new_html)
    new_html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{canonical}">', new_html)
    
    # Hero Title and Subtitle
    new_html = re.sub(r'<h1 class="guide-title">.*?</h1>', f'<h1 class="guide-title">{page["h1"]}</h1>', new_html)
    
    # Replace content inside <div class="guide-content"> ... </div>
    content_pattern = re.compile(r'<div class="guide-content">.*?</div>\s*<div class="guide-cta">', re.DOTALL)
    replacement = f'<div class="guide-content">\n{page["content"]}\n</div>\n<div class="guide-cta">'
    new_html = content_pattern.sub(replacement, new_html)
    
    # Update breadcrumb
    new_html = re.sub(r'<span class="guide-tag">.*?</span>', f'<span class="guide-tag">Local Guide</span>', new_html)
    new_html = re.sub(r'>Anna Maria Island Beaches<', f'>{page["h1"]}<', new_html)
    
    filepath = os.path.join(base_dir, page['file'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Created {page['file']}")

