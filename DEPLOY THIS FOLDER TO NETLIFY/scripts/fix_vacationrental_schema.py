#!/usr/bin/env python3
"""Fix VacationRental JSON-LD fields across the static site.

Goal: satisfy Search Console's Vacation rental enhancement requirements by
ensuring each VacationRental has: identifier, geo, containsPlace, image.

We only use approximate (city-level) geo; no street address required.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]

SCRIPT_RE = re.compile(
    r"(<script[^>]+type=[\"']application/ld\+json[\"'][^>]*>)(.*?)(</script>)",
    re.IGNORECASE | re.DOTALL,
)

CITY_GEO = {
    # City-level centers (approx)
    # Use 5+ decimals so Google treats these as precise coordinates (still approximate).
    "bradenton": (27.49891, -82.57481),
    "sarasota": (27.33643, -82.53072),
    "anna maria": (27.53031, -82.73431),
    "anna maria island": (27.53031, -82.73431),
    "siesta key": (27.26711, -82.54071),
    "longboat key": (27.41251, -82.66041),
}

DEFAULT_GEO = (27.45011, -82.55011)  # Central-ish Manatee/Sarasota (approx)

DEFAULT_IMAGE = "https://seascape-vacations.com/hero-optimized.jpg"


def _slugify(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"(^-|-$)", "", s)
    return s or "vacation-rental"


def _iter_jsonld_scripts(html: str) -> Iterable[tuple[str, str, str]]:
    for m in SCRIPT_RE.finditer(html):
        yield m.group(1), m.group(2).strip(), m.group(3)


def _try_load_json(blob: str) -> Any | None:
    try:
        return json.loads(blob)
    except Exception:
        return None


def _find_geo_for_address(addr: Any) -> tuple[float, float]:
    if isinstance(addr, dict):
        loc = (addr.get("addressLocality") or "").strip().lower()
        if loc:
            if loc in CITY_GEO:
                return CITY_GEO[loc]
            # Handle e.g. "Anna Maria Island"
            for k, v in CITY_GEO.items():
                if k in loc:
                    return v
    return DEFAULT_GEO


def _ensure_vacation_rental_fields(vr: dict[str, Any], fallback_name: str | None = None) -> None:
    name = (vr.get("name") or fallback_name or "").strip()

    # identifier
    ident = vr.get("identifier")
    if not ident or (isinstance(ident, str) and not ident.strip()):
        if isinstance(vr.get("@id"), str) and vr["@id"].strip():
            vr["identifier"] = vr["@id"].strip()
        elif name:
            vr["identifier"] = _slugify(name)
        else:
            vr["identifier"] = "seascape-vacation-rental"

    # image
    img = vr.get("image")
    if not img or (isinstance(img, str) and not img.strip()):
        vr["image"] = DEFAULT_IMAGE

    # geo + containsPlace (approx, city-level)
    addr = vr.get("address")
    lat, lng = _find_geo_for_address(addr)

    geo = vr.get("geo")
    if not isinstance(geo, dict) or ("latitude" not in geo or "longitude" not in geo):
        vr["geo"] = {
            "@type": "GeoCoordinates",
            "latitude": lat,
            "longitude": lng,
        }

    # containsPlace: Search Console is currently rejecting our @type=Accommodation objects
    # ("Invalid object type for field 'containsPlace'"). Use a Place object instead.
    cp = vr.get("containsPlace")
    has_ok_cp = isinstance(cp, dict) and cp.get("@type") == "Place"
    if not has_ok_cp:
        place: dict[str, Any] = {
            "@type": "Place",
            "name": name or "Vacation Rental",
            # Hint "accommodation" semantics without requiring street address.
            "additionalType": "https://schema.org/Accommodation",
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": lat,
                "longitude": lng,
            },
        }
        if isinstance(addr, dict):
            place["address"] = addr

        vr["containsPlace"] = place


def _walk_and_fix(data: Any) -> None:
    if isinstance(data, dict):
        if data.get("@type") == "VacationRental":
            _ensure_vacation_rental_fields(data)

        if data.get("@type") == "ItemList":
            for el in data.get("itemListElement", []) or []:
                if isinstance(el, dict) and isinstance(el.get("item"), dict) and el["item"].get("@type") == "VacationRental":
                    _ensure_vacation_rental_fields(el["item"], fallback_name=el["item"].get("name"))

        if "@graph" in data:
            _walk_and_fix(data["@graph"])

        for v in data.values():
            _walk_and_fix(v)

    elif isinstance(data, list):
        for v in data:
            _walk_and_fix(v)


@dataclass
class UpdateResult:
    path: Path
    updated: bool


def fix_file(path: Path) -> UpdateResult:
    html = path.read_text("utf-8", errors="ignore")
    updated = False

    def repl(m: re.Match[str]) -> str:
        nonlocal updated
        open_tag, blob, close_tag = m.group(1), m.group(2).strip(), m.group(3)
        data = _try_load_json(blob)
        if data is None:
            return m.group(0)

        before = json.dumps(data, sort_keys=True)
        _walk_and_fix(data)
        after = json.dumps(data, sort_keys=True)
        if before == after:
            return m.group(0)

        updated = True
        pretty = json.dumps(data, indent=4, ensure_ascii=False)
        return f"{open_tag}\n{pretty}\n{close_tag}"

    new_html = SCRIPT_RE.sub(repl, html)
    if updated and new_html != html:
        path.write_text(new_html, "utf-8")
    return UpdateResult(path=path, updated=updated)


def main() -> int:
    files = [ROOT / "index.html"]
    files += list((ROOT / "stays").rglob("index.html"))
    if (ROOT / "properties" / "index.html").exists():
        files.append(ROOT / "properties" / "index.html")

    changed = 0
    for p in files:
        r = fix_file(p)
        if r.updated:
            changed += 1

    print(f"Updated {changed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
