import re
import os

base_dir = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY/guides'
template_path = os.path.join(base_dir, 'anna-maria-island-beaches.html')

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

guides_data = [
    {
        'file': 'srq-airport-to-anna-maria-island.html',
        'title': 'How to Get From SRQ Airport to Anna Maria Island | 2026 Guide',
        'desc': 'Complete transportation guide: getting from Sarasota-Bradenton International Airport (SRQ) to Anna Maria Island. Rental cars, Ubers, private shuttles, and driving directions.',
        'h1': 'How to Get From SRQ Airport to Anna Maria Island',
        'subtitle': 'Transportation options, driving directions, and local tips from SRQ (Sarasota-Bradenton) to AMI.',
        'content': """
<p>Flying into Sarasota-Bradenton International Airport (SRQ) is by far the most convenient way to reach Anna Maria Island. Located just 15 to 20 miles from the island, the drive from the airport to your vacation rental typically takes between 30 and 45 minutes, depending on traffic and where exactly you are staying. This guide breaks down all your transportation options, driving directions, and tips to ensure a smooth arrival.</p>

<h2>Why SRQ is the Best Airport for Anna Maria Island</h2>
<p>While Tampa International Airport (TPA) offers more direct flights, SRQ is exponentially closer and less stressful. The airport is small, easy to navigate, and getting from your gate to baggage claim to your ground transportation rarely takes more than 15 minutes. During peak winter season, the 90-minute drive from TPA can easily turn into 2.5 hours of stop-and-go traffic on I-75. If you can fly into SRQ, it is almost always worth the slight premium in airfare.</p>

<h2>Transportation Options</h2>
<h3>1. Rental Cars (Most Popular)</h3>
<p>If you plan to leave Anna Maria Island during your stay—perhaps to visit Siesta Key, downtown Sarasota, or Robinson Preserve—renting a car is recommended. SRQ has all the major rental car agencies directly across from baggage claim. There is no shuttle required to reach the rental car lot.</p>

<h3>2. Uber and Lyft</h3>
<p>Rideshare services are prevalent at SRQ. A ride to Anna Maria Island typically costs between $40 and $60 depending on surge pricing and the time of day. The pickup area is clearly marked just outside the main terminal doors. This is a great option if you plan to rely on the free island trolley and bike rentals once you arrive.</p>

<h3>3. Private Car Services and Shuttles</h3>
<p>For groups traveling with a lot of luggage or those arriving late at night, booking a private car service in advance provides peace of mind. Local companies like AMI Taxi and Paradise Car Service monitor your flight and meet you at baggage claim. A private SUV holding up to 6 people generally runs around $80 to $100 one-way.</p>

<h2>Driving Directions from SRQ to Anna Maria Island</h2>
<p>There are two primary routes to get to the island from SRQ. Your GPS will likely direct you based on current traffic conditions, but here is what to expect:</p>

<h3>Route 1: Via Cortez Road (Best for Bradenton Beach)</h3>
<ul>
    <li>Exit the airport and turn right (north) onto US-41 / Tamiami Trail.</li>
    <li>Continue north to Cortez Road W / 44th Ave W.</li>
    <li>Turn left onto Cortez Road W and take it all the way to the water.</li>
    <li>Cross the Cortez Bridge onto Anna Maria Island. You will be in Bradenton Beach.</li>
</ul>

<h3>Route 2: Via Manatee Avenue (Best for Holmes Beach and Anna Maria City)</h3>
<ul>
    <li>Exit the airport and turn right (north) onto US-41 / Tamiami Trail.</li>
    <li>Continue north through Bradenton to Manatee Avenue W / SR 64.</li>
    <li>Turn left onto Manatee Avenue W and take it all the way to the water.</li>
    <li>Cross the Anna Maria Island Bridge. You will arrive directly in Holmes Beach.</li>
</ul>

<h2>Frequently Asked Questions</h2>
<h3>Should I fly into TPA or SRQ for Anna Maria Island?</h3>
<p>SRQ is definitely preferred. It is 30-45 minutes from AMI, whereas TPA is 1 hour and 15 minutes away without traffic. However, TPA often has significantly cheaper flights and more direct options, making it a viable alternative.</p>

<h3>Is there a public bus from SRQ to Anna Maria Island?</h3>
<p>Technically yes, via the Manatee County Area Transit (MCAT), but it involves multiple transfers and can take over two hours. We do not recommend this option for visitors carrying luggage.</p>
        """
    },
    {
        'file': 'do-you-need-a-car-anna-maria-island.html',
        'title': 'Do You Need a Car on Anna Maria Island? | 2026 Guide',
        'desc': 'Wondering if you need to rent a car for your Anna Maria Island vacation? Learn about the free trolley, Monkey Bus, golf carts, bike rentals, and walkability.',
        'h1': 'Do You Need a Car on Anna Maria Island?',
        'subtitle': 'A complete guide to getting around AMI without a rental car: The free trolley, golf carts, and bike rentals.',
        'content': """
<p>One of the most common questions we get from guests booking a vacation rental is, "Do I need to rent a car for our Anna Maria Island vacation?" The short answer is: <strong>No, you do not absolutely need a car.</strong> In fact, many visitors find that ditching the car and relying on island transportation significantly enhances their "old Florida" vacation experience.</p>
<p>However, whether it is the right choice for <em>your</em> specific trip depends on where you are staying, who you are traveling with, and what you plan to do. Here is a comprehensive breakdown of getting around Anna Maria Island without a car.</p>

<h2>The Free Anna Maria Island Trolley</h2>
<p>The crown jewel of AMI's transportation system is the free Manatee County Area Transit (MCAT) trolley. It runs the entire 7-mile length of the island from the Anna Maria City Pier in the north to Coquina Beach in the south.</p>
<ul>
    <li><strong>Schedule:</strong> The trolley runs daily from 6:00 AM to 10:30 PM.</li>
    <li><strong>Frequency:</strong> Typically every 20 minutes (though traffic can cause delays during peak season).</li>
    <li><strong>Stops:</strong> Marked by green signs with a trolley logo, located every few blocks along Pine Avenue, Gulf Drive, and Marina Drive.</li>
    <li><strong>Features:</strong> Air-conditioned, wheelchair accessible, and equipped with a bike rack on the front.</li>
</ul>
<p>If your vacation rental is located near a trolley stop (and almost all properties in Holmes Beach and Bradenton Beach are), you can easily reach restaurants, grocery stores, and any beach access point on the island for free.</p>

<h2>Golf Cart Rentals: The Local Way to Travel</h2>
<p>If you want the convenience of a vehicle without the hassle of a rental car, Street Legal Golf Carts (Low Speed Vehicles or LSVs) are incredibly popular. You will see them everywhere on the island.</p>
<p>LSVs are electric or gas-powered carts that are street-legal on roads with a speed limit of 35 MPH or less—which covers the entire island. They are easier to park than cars and offer a fun, open-air way to explore. Expect to pay between $400 and $600 per week for a 4- or 6-passenger cart. Be sure to book these months in advance if visiting during Spring Break or summer.</p>

<h2>Bicycles and Walking</h2>
<p>Anna Maria Island is completely flat, making it an absolute paradise for cyclists. There are dedicated bike lanes and multi-use paths covering much of the island. Renting a beach cruiser for the week costs about $60, and many rental companies will deliver the bikes directly to your vacation rental before you arrive. Biking is often faster than driving during peak traffic hours.</p>

<h2>The AMI "Monkey Bus"</h2>
<p>In the evenings when the trolley stops running or if you prefer a direct ride, the "Monkey Bus" (and similar private shuttle services) operates on an a tips-only basis. You simply call them, they pick you up, and you tip the driver. This is a fantastic option for returning home after dinner or visiting the local bars on Bridge Street.</p>

<h2>When You DO Need a Car</h2>
<p>You should absolutely consider renting a car if:</p>
<ul>
    <li>You plan to take multiple day trips off the island (e.g., Sarasota, St. Armand's Circle, Siesta Key, or Tampa theme parks).</li>
    <li>You are flying into Tampa International Airport (TPA) or Orlando (MCO) and the cost of round-trip private shuttles exceeds the cost of a rental car.</li>
    <li>You have mobility issues that make walking to trolley stops or riding in a golf cart difficult.</li>
    <li>Your vacation rental is located far from Gulf Drive or Marina Drive, making the walk to the trolley stop impractical with beach gear.</li>
</ul>

<h2>Frequently Asked Questions</h2>
<h3>Can I take the trolley to the grocery store?</h3>
<p>Yes. The trolley stops directly at the Publix Super Market in Holmes Beach, which is located in the center of the island. Many visitors take the trolley to the store and take an Uber or Monkey Bus back if they have heavy groceries.</p>

<h3>Is it hard to park a car on Anna Maria Island?</h3>
<p>During peak season (February - April), public beach parking lots fill up by 10 AM, and street parking in Anna Maria City is strictly enforced. If you have a car, you will want to leave it parked at your vacation rental and use a bike, golf cart, or trolley to get to the beach or dinner.</p>
        """
    },
    {
        'file': 'anna-maria-island-noise-ordinance-guide.html',
        'title': 'Anna Maria Island Noise Ordinance Guide 2026 | Seascape Vacations',
        'desc': 'Everything vacationers need to know about the Anna Maria Island noise ordinance. Quiet hours, enforcement penalties, and how to be a good neighbor during your stay.',
        'h1': 'Understanding the Anna Maria Island Noise Ordinance',
        'subtitle': 'A guide to quiet hours and local regulations to ensure a stress-free vacation without fines.',
        'content': """
<p>Anna Maria Island is famous for its peaceful, "Old Florida" atmosphere. To protect this tranquil environment and balance the needs of full-time residents with vacationers, all three cities on the island—Anna Maria City, Holmes Beach, and Bradenton Beach—have strictly enforced noise ordinances. If you are renting a vacation home, understanding these rules is critical, as violations can result in immediate fines or even eviction.</p>

<h2>What Are the Quiet Hours?</h2>
<p>While the exact legal language differs slightly between the three municipalities, the practical application is universal across the island: <strong>Quiet hours are strictly enforced from 10:00 PM to 8:00 AM daily.</strong></p>
<p>During these hours, noise from your property cannot be audible from the property line. This means you cannot be heard by your neighbors.</p>

<h2>What Constitutes a Violation?</h2>
<p>Local law enforcement and code enforcement officers issue citations based on the "plainly audible" standard. If they can hear the noise from the street or the neighbor's property line, you are in violation. Common triggers include:</p>
<ul>
    <li>Playing music outside (even quietly) after 10:00 PM.</li>
    <li>Loud conversations, laughing, or shouting on patios, balconies, or around the pool after 10:00 PM.</li>
    <li>Late-night swimming where splashing and voices carry over the fence.</li>
    <li>Excessive vehicle noise or slamming car doors late at night.</li>
</ul>
<p>Even during the daytime, "unreasonably loud" noise that disturbs the peace can result in a warning or citation. Amplified music outdoors should always be kept to a respectable volume.</p>

<h2>Fines and Penalties</h2>
<p>The cities on Anna Maria Island do not take noise complaints lightly. If a neighbor calls the police to complain about noise at your vacation rental:</p>
<ol>
    <li><strong>The Police Will Visit:</strong> An officer will assess the noise level from the property line.</li>
    <li><strong>No Warnings Required:</strong> While officers sometimes issue warnings, they are legally authorized to issue a citation immediately without giving you a chance to turn the music down.</li>
    <li><strong>Steep Fines:</strong> Citations typically range from $250 to $500 for the first offense and scale up dramatically for repeat offenses.</li>
    <li><strong>Eviction Risk:</strong> Almost all vacation rental companies, including Seascape Vacations, have a "zero tolerance" policy for police-issued noise citations. A citation is considered a breach of your rental agreement and can result in immediate eviction without a refund.</li>
</ol>

<h2>How to Be a Good Neighbor on AMI</h2>
<p>Most vacationers have no intention of causing a disturbance. Noise carrying over fences happens accidentally when guests do not realize how far sound travels over water or in quiet neighborhoods.</p>
<ul>
    <li><strong>Move the party inside at 10:00 PM:</strong> When 10 PM hits, take the drinks and conversation indoors and close the sliding glass doors.</li>
    <li><strong>Turn off outdoor speakers:</strong> If you are enjoying the patio in the evening, turn off any Bluetooth speakers before 10 PM.</li>
    <li><strong>Mind the pool:</strong> Pools act like acoustic amplifiers. Splashing and talking in a pool carry directly into the windows of the house next door.</li>
</ul>

<h2>Frequently Asked Questions</h2>
<h3>What if a neighboring property is keeping me awake?</h3>
<p>If you are disturbed by excessive noise after 10:00 PM, you have the right to contact the local police department via their non-emergency number. Let them handle the situation professionally rather than confronting the neighbors yourself.</p>

<h3>Are the rules different for holidays like New Year's Eve?</h3>
<p>No. The noise ordinance applies 365 days a year. While police might exercise slightly more discretion on major holidays, the 10:00 PM quiet hour remains legally in effect.</p>
        """
    },
    {
        'file': 'best-waterfront-restaurants-with-boat-dock.html',
        'title': 'Best Waterfront Restaurants with Boat Dock Access Near AMI | 2026',
        'desc': 'The best restaurants near Anna Maria Island and Bradenton where you can arrive by boat. Discover waterfront dining with dock access on the Florida Gulf Coast.',
        'h1': 'Best Waterfront Restaurants with Boat Dock Access',
        'subtitle': 'Arrive by water. A boater’s guide to dining around Anna Maria Island, Bradenton, and Sarasota Bay.',
        'content': """
<p>Renting a vacation home with a private boat dock opens up an entirely different way to experience Florida's Gulf Coast. Boating to dinner is a quintessential local experience. The waters surrounding Anna Maria Island, Bradenton, and Longboat Key offer numerous excellent restaurants where you can literally pull up your boat, tie off at the dock, and step right onto the patio for fresh seafood and a cold drink.</p>
<p>Here are the best waterfront restaurants with boat dock access in the area.</p>

<h2>Anna Maria Island \u0026 Cortez</h2>

<h3>1. Tide Tables Restaurant and Marina (Cortez)</h3>
<p>Located in the historic fishing village of Cortez just across the bridge from Bradenton Beach, Tide Tables is arguably the most authentic "old Florida" fish camp in the area. The seafood is remarkably fresh—often caught by local commercial fishermen right off their docks. The vibe is ultra-casual, with picnic tables outside right on the water.<br>
<strong>Docking:</strong> They have a long dock parallel to the channel. The current can be swift here, so approach with caution. It fills up fast on weekends.</p>

<h3>2. Seafood Shack Marina Bar \u0026 Grill (Cortez)</h3>
<p>A landmark in Cortez since 1971, the Seafood Shack offers a huge menu, sweeping views of Sarasota Bay, and a large outdoor deck. It is slightly more structured than Tide Tables but retains a very relaxed atmosphere.<br>
<strong>Docking:</strong> Plentiful deep-water slips available at their marina for dining guests.</p>

<h3>3. The Rod and Reel Pier (Anna Maria City)</h3>
<p>While technically a fishing pier, this two-story structure at the northern end of Anna Maria Island features a fantastic, no-frills seafood restaurant at the end. It is famous for its grouper sandwiches and cheap beer.<br>
<strong>Docking:</strong> Very limited. There are a few cleats on the lower deck of the pier where small to medium center consoles can tie up, but it is exposed to the elements and wakes.</p>

<h2>Bradenton (Manatee River)</h2>

<h3>4. Pier 22</h3>
<p>Located in downtown Bradenton right on the Manatee River, Pier 22 offers an upscale dining experience with an extensive menu featuring sushi, steaks, and fresh catch. The large outdoor terrace overlooks the river and the marina.<br>
<strong>Docking:</strong> Excellent. Tie up at the Twin Dolphin Marina right in front of the restaurant. Call ahead (VHF Channel 16 or by phone) and the dockmaster will assign you a transient slip for dining.</p>

<h3>5. Caddy's Bradenton</h3>
<p>Situated near the mouth of the Manatee River, Caddy's is a lively, tropical-themed venue with two bars, live music, and a sandy beach area with fire pits. It is a fantastic spot to watch the sun go down.<br>
<strong>Docking:</strong> Excellent. They have a newly renovated, extensive floating dock system specifically for restaurant guests.</p>

<h2>Sarasota \u0026 Longboat Key</h2>

<h3>6. Shore (Longboat Key)</h3>
<p>For mid-century modern aesthetics and elevated coastal cuisine, Shore on Longboat Key is spectacular. Located in the Broadway Promenade, it offers a sophisticated menu in a beautifully designed open-air environment.<br>
<strong>Docking:</strong> They have their own private dock for guests arriving via Sarasota Bay, just south of the Longboat Pass bridge.</p>

<h3>7. Mar Vista Dockside Restaurant \u0026 Pub</h3>
<p>Tucked away on the north end of Longboat Key, Mar Vista is a hidden gem sheltered under ancient buttonwood trees. Their "Edible Sand" and fresh fish dishes are legendary, and the old-Florida ambiance is perfectly preserved.<br>
<strong>Docking:</strong> Very good. They have a brand new, extensive dock with 14 slips available for guests in a protected cove.</p>

<h2>Tips for Dining by Boat</h2>
<ul>
    <li><strong>Check the Tides:</strong> The waters around Anna Maria Island are heavily influenced by tides. Some restaurants have shallow approaches that become impassable on a negative low tide.</li>
    <li><strong>Designated Skipper:</strong> The Coast Guard and local marine patrol strictly enforce BUI (Boating Under the Influence) laws. Penalties are severe.</li>
    <li><strong>Mind Your Wake:</strong> Almost all restaurants with docks are located in active "Idle Speed" or "No Wake" zones.</li>
</ul>
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
    # The template might not have a guide-subtitle, wait it has guide-meta. Let's not use subtitle if it doesn't exist, just replace content.
    
    # Replace content inside <div class="guide-content"> ... </div>
    # Using regex with DOTALL to replace everything inside guide-content
    content_pattern = re.compile(r'<div class="guide-content">.*?</div>\s*<div class="guide-cta">', re.DOTALL)
    replacement = f'<div class="guide-content">\n{page["content"]}\n</div>\n<div class="guide-cta">'
    new_html = content_pattern.sub(replacement, new_html)
    
    # Update breadcrumb
    new_html = re.sub(r'<span class="guide-tag">.*?</span>', f'<span class="guide-tag">Travel Guide</span>', new_html)
    new_html = re.sub(r'>Anna Maria Island Beaches<', f'>{page["h1"]}<', new_html)
    
    filepath = os.path.join(base_dir, page['file'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Created {page['file']}")

