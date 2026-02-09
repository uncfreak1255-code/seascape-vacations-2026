#!/usr/bin/env python3
"""Basic SEO URL health checks.

This is a pragmatic, local-only check: verifies that the sitemap only contains
URLs we actually serve and that key landing pages exist.
"""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _path_for_url(url: str) -> Path | None:
    prefix = "https://seascape-vacations.com/"
    if not url.startswith(prefix):
        return None
    rel = url[len(prefix):]
    if rel == "":
        return ROOT / "index.html"
    if rel.endswith("/"):
        return ROOT / rel / "index.html"
    return ROOT / rel


def main() -> int:
    sitemap = ROOT / "sitemap.xml"
    if not sitemap.exists():
        print("FAIL: sitemap.xml missing")
        return 1

    xml = sitemap.read_text("utf-8", errors="ignore")
    try:
        tree = ET.fromstring(xml)
    except Exception as e:
        print(f"FAIL: sitemap.xml parse error: {e}")
        return 1

    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [el.text.strip() for el in tree.findall("sm:url/sm:loc", ns) if el.text and el.text.strip()]

    # We want properties indexed as a first-class landing page.
    required_in_sitemap = [
        "https://seascape-vacations.com/properties/",
    ]
    missing_required = [u for u in required_in_sitemap if u not in locs]
    if missing_required:
        print("FAIL: sitemap missing required URLs: " + ", ".join(missing_required))
        return 1

    bad = []
    for loc in locs:
        p = _path_for_url(loc)
        if p is None or not p.exists():
            bad.append((loc, str(p) if p else "(unmapped)"))

    if bad:
        print(f"FAIL: {len(bad)} sitemap URLs don't map to files")
        for loc, p in bad[:50]:
            print(f"- {loc} -> {p}")
        return 1

    # Key pages we care about for direct bookings + owners
    key = [
        ROOT / "index.html",
        ROOT / "guides" / "index.html",
        ROOT / "about-us" / "index.html",
        ROOT / "property-management" / "index.html",
        ROOT / "properties" / "index.html",
    ]
    missing = [str(p.relative_to(ROOT)) for p in key if not p.exists()]
    if missing:
        print("FAIL: missing key pages: " + ", ".join(missing))
        return 1

    print("PASS: sitemap + key pages look consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
