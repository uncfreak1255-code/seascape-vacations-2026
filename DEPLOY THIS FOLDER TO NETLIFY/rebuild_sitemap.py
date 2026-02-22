import os
import xml.etree.ElementTree as ET
from urllib.parse import quote
from datetime import datetime

base_dir = '/Users/sawbeck/Downloads/LIVE Seascape Website!! copy1-working/DEPLOY THIS FOLDER TO NETLIFY'
base_url = 'https://seascape-vacations.com'

def find_html_files(directory):
    html_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                # Avoid some preview or dev files
                if '-preview' in file:
                    continue
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, directory)
                
                # Replace backslashes on Windows
                rel_path = rel_path.replace('\\', '/')
                
                # Strip index.html for clean URLs
                if rel_path.endswith('index.html'):
                    url_path = rel_path[:-10]
                else:
                    url_path = rel_path
                    
                html_files.append(url_path)
    return html_files

html_files = find_html_files(base_dir)

# Create XML
urlset = ET.Element("urlset")
urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

today = datetime.now().strftime('%Y-%m-%d')

for path in sorted(html_files):
    # Determine priority based on path
    priority = "0.8"
    if path == "":
        priority = "1.0"
    elif path.startswith("properties/"):
        priority = "0.9"
    elif path.startswith("guides/") or path.startswith("area-guide"):
        priority = "0.7"
    elif path.startswith("stays/"):
        priority = "0.6"
    elif path.startswith("property-management/"):
        priority = "0.8"

    url = ET.SubElement(urlset, "url")
    loc = ET.SubElement(url, "loc")
    # Don't quote the whole thing to keep / but quote segments 
    full_url = f"{base_url}/{path}"
    loc.text = full_url.rstrip('/') if full_url.endswith('/') and len(full_url) > len(base_url) + 1 else full_url
    
    lastmod = ET.SubElement(url, "lastmod")
    lastmod.text = today
    
    pri = ET.SubElement(url, "priority")
    pri.text = priority

# Write out
tree = ET.ElementTree(urlset)
ET.indent(tree, space="    ", level=0)
tree.write(os.path.join(base_dir, 'sitemap.xml'), encoding='utf-8', xml_declaration=True)

print("Sitemap rebuilt successfully with", len(html_files), "URLs.")
