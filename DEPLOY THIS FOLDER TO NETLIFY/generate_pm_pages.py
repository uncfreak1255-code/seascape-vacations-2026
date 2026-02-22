import re
import os

base_dir = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY/property-management'
template_path = os.path.join(base_dir, 'vacation-rental-management-anna-maria-island/index.html')

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

pages_data = [
    {
        'dir_name': 'vacation-rental-management-holmes-beach',
        'title': 'Holmes Beach Vacation Rental Management | Seascape Vacations',
        'desc': 'Expert vacation rental management in Holmes Beach, FL. Maximize your rental income with local, full-service property management designed for the Gulf Coast.',
        'h1': 'Holmes Beach Vacation Rental Management',
        'content': """
<p>Owning a vacation rental in Holmes Beach, the geographic and commercial heart of Anna Maria Island, should be a highly lucrative investment. However, between stringent local noise ordinances, intensive guest turnover, and the logistical challenges of island maintenance, self-managing or using an under-resourced national chain often leaves money on the table and creates unnecessary stress for owners.</p>

<h2>The Seascape Difference in Holmes Beach</h2>
<p>Seascape Vacations provides boutique, full-service property management exclusively focused on the Florida Gulf Coast. Because we are locally based, we understand the unique nuances of the Holmes Beach market—from maximizing rates during peak season to ensuring your property complies seamlessly with city regulations.</p>

<h3>1. Revenue Optimization Driven by Data</h3>
<p>We do not rely on "set it and forget it" pricing. Our revenue management team utilizes advanced dynamic pricing tools alongside deep local market knowledge to adjust your nightly rates based on demand, local events, and historical trends. On average, owners switching to Seascape see a 20-30% increase in gross revenue within their first year.</p>

<h3>2. Direct Booking Advantage</h3>
<p>While we heavily market your property on all major OTAs (Airbnb, VRBO, Booking.com), our ultimate goal is direct bookings. By driving traffic directly to our platform, we save guests from exorbitant OTA fees and return more margin to you. A significant percentage of our bookings come from highly vetted, loyal repeat guests.</p>

<h3>3. Proactive Care and Strict Compliance</h3>
<p>Holmes Beach enforces some of the strictest short-term rental regulations in Florida, including rigorous noise ordinances. We install environmentally conscious, non-invasive noise monitors to prevent issues before they occur. Our dedicated local maintenance team performs exhaustive pre-arrival and post-departure inspections, treating your home as if it were our own.</p>

<h2>Get Your Free Income Projection</h2>
<p>Whether you are considering purchasing an investment property in Holmes Beach or are unsatisfied with your current management, we can help. Contact us today for a comprehensive, no-obligation income projection based on real-world data from comparable Holmes Beach properties.</p>
        """
    },
    {
        'dir_name': 'vacation-rental-management-bradenton-beach',
        'title': 'Bradenton Beach Vacation Rental Management | Seascape Vacations',
        'desc': 'Top-tier vacation rental management for Bradenton Beach properties. Increase your ROI and eliminate the stress of ownership with Seascape Vacations.',
        'h1': 'Bradenton Beach Vacation Rental Management',
        'content': """
<p>Bradenton Beach, with its vibrant Bridge Street, stunning Gulf views, and lively atmosphere, is one of the most highly sought-after vacation destinations on Florida's Gulf Coast. For property owners, this translates to massive revenue potential. However, capitalizing on that potential requires more than just listing your property online; it requires aggressive marketing, meticulous care, and a localized strategy.</p>

<h2>Why Partner with Seascape Vacations?</h2>
<p>As a specialized local property manager, Seascape Vacations is uniquely equipped to handle the specific demands of Bradenton Beach rentals. We act as your true partner, protecting your asset while driving maximum return on investment.</p>

<h3>Market-Leading Marketing and Visibility</h3>
<p>Your property deserves to be seen. We utilize professional architectural photography, immersive 3D tours, and optimized listing copy to ensure your Bradenton Beach home stands out. Your property will securely syndicate across every major booking channel, but we actively prioritize our direct-booking engine to increase your net revenue.</p>

<h3>Uncompromising Cleanliness and Maintenance</h3>
<p>The coastal environment is harsh on homes. Sand, salt, and humidity require constant vigilance. Our proprietary housekeeping protocols and preventative maintenance schedules guarantee that your property remains in pristine condition year-round, securing those critical 5-star reviews from guests.</p>

<h3>24/7 Local Support</h3>
<p>When a guest has a problem at 10 PM on a Saturday, you do not want to take the call—and you shouldn't have to. Our Bradenton-based team is on call 24/7/365. We handle everything from minor maintenance requests to emergency situations, ensuring your guests have a flawless experience.</p>

<h2>Discover Your Property's True Potential</h2>
<p>Are you earning what your Bradenton Beach property is truly worth? Let our experts analyze your home and current performance. We will provide a completely transparent, data-driven revenue projection outlining exactly how Seascape Vacations can elevate your investment.</p>
        """
    },
    {
        'dir_name': 'case-study',
        'title': 'Case Study: The Seascape Effect | Seascape Vacations',
        'desc': 'See exactly how Seascape Vacations increased revenue by 42% for a Bradenton property in just 12 months. Real numbers, real results.',
        'h1': 'Case Study: The Seascape Effect',
        'content': """
<p>At Seascape Vacations, we believe the numbers speak for themselves. We partnered with the owners of a 4-bedroom pool home in Bradenton who were frustrated with their previous management company's lackluster performance and poor communication. They were considering selling the property entirely. Here is what happened in their first 12 months with Seascape.</p>

<h2>The Challenge</h2>
<p>"The Oasis" (Name changed for privacy) was a beautiful home, but it was underperforming. Prior to joining Seascape, the property suffered from:</p>
<ul>
    <li><strong>Stagnant Revenue:</strong> Stalled at $65,000 gross annual revenue.</li>
    <li><strong>Poor Reviews:</strong> Averaging 4.2 stars on Airbnb due to cleanliness issues and slow response times from the previous manager.</li>
    <li><strong>Low Off-Season Occupancy:</strong> The property sat empty for weeks during the late summer and early fall.</li>
</ul>

<h2>The Seascape Solution</h2>
<p>We immediately implemented our comprehensive management strategy to turn the property around.</p>

<h3>1. Listing Optimization & Photography</h3>
<p>We commissioned professional twilight photography to highlight the home’s best feature: its spectacular outdoor pool area. We completely rewrote the listing copy, optimizing it for SEO and highlighting its proximity to the IMG Academy to capture sports-tourism families.</p>

<h3>2. Dynamic Revenue Management</h3>
<p>The previous manager used static seasonal pricing. We implemented dynamic pricing algorithms that adjusted rates daily based on local demand, events, and booking windows. This allowed us to capture premium rates during peak weeks while aggressively filling calendar gaps in the off-season.</p>

<h3>3. Elevating the Guest Experience</h3>
<p>We assigned the home to our premium housekeeping tier and implemented strict pre-arrival inspections. We also installed smart locks for seamless check-in and provided a curated digital welcome book outlining local Bradenton attractions.</p>

<h2>The Results (Year 1)</h2>
<div style="background: var(--cream-dark); padding: 30px; border-radius: 12px; margin: 30px 0;">
    <h3 style="margin-top:0;">12-Month Performance Metrics</h3>
    <ul style="font-size: 18px; line-height: 1.8; list-style-type: none; padding-left: 0;">
        <li>📈 <strong>Gross Revenue:</strong> Increased from $65,000 to <strong>$92,500 (+42%)</strong></li>
        <li>📅 <strong>Total Occupancy:</strong> Increased from 62% to <strong>78%</strong></li>
        <li>⭐ <strong>Guest Rating:</strong> Improved from 4.2 to <strong>4.93 stars</strong></li>
        <li>💻 <strong>Direct Bookings:</strong> Reached <strong>28%</strong> of total reservations (saving thousands in OTA fees)</li>
    </ul>
</div>

<h2>Owner Testimonial</h2>
<p><em>"We were ready to sell the house because it just wasn't worth the headache. Seascape took over and completely changed our perspective. Not only is the house making significantly more money, but it is actually in better condition than when we managed it ourselves. We finally have peace of mind." — John & Sarah M., Property Owners</em></p>

<h2>Ready to Experience The Seascape Effect?</h2>
<p>If your Gulf Coast vacation rental is underperforming, we can help. Contact our owner success team today for a free revenue analysis.</p>
        """
    }
]

for page in pages_data:
    new_html = template
    
    # Meta replacements
    new_html = re.sub(r'<title>.*?</title>', f'<title>{page["title"]}</title>', new_html)
    new_html = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{page["desc"]}">', new_html)
    new_html = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{page["title"]}">', new_html)
    new_html = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{page["desc"]}">', new_html)
    new_html = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{page["title"]}">', new_html)
    new_html = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{page["desc"]}">', new_html)
    
    # Canonical URLs
    canonical = f"https://seascape-vacations.com/property-management/{page['dir_name']}/"
    new_html = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{canonical}">', new_html)
    new_html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{canonical}">', new_html)
    
    # Hero Title
    new_html = re.sub(r'<h1 class="guide-title">.*?</h1>', f'<h1 class="guide-title">{page["h1"]}</h1>', new_html)
    
    # Replace content inside <div class="guide-content"> ... </div>
    content_pattern = re.compile(r'<div class="guide-content">.*?</div>\s*<div class="guide-cta">', re.DOTALL)
    replacement = f'<div class="guide-content">\n{page["content"]}\n</div>\n<div class="guide-cta">'
    new_html = content_pattern.sub(replacement, new_html)
    
    # Create directory if it doesn't exist
    target_dir = os.path.join(base_dir, page['dir_name'])
    os.makedirs(target_dir, exist_ok=True)
    
    filepath = os.path.join(target_dir, 'index.html')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Created {page['dir_name']}/index.html")

