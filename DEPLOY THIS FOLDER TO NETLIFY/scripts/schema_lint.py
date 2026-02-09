#!/usr/bin/env python3
"""Schema linter for Seascape static site.

Fails if VacationRental items are missing fields that Google Search Console's
"Vacation rental" enhancement is flagging on this site.

This is intentionally simple and tailored to our HTML structure.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]

SCRIPT_RE = re.compile(
    r"<script[^>]+type=[\"']application/ld\+json[\"'][^>]*>(.*?)</script>",
    re.IGNORECASE | re.DOTALL,
)


@dataclass
class Finding:
    file: Path
    where: str
    name: str | None
    missing: list[str]


def _iter_jsonld_blobs(html: str) -> Iterable[str]:
    for m in SCRIPT_RE.finditer(html):
        blob = m.group(1)
        if blob and blob.strip():
            yield blob.strip()


def _try_load_json(blob: str) -> Any | None:
    try:
        return json.loads(blob)
    except Exception:
        return None


def _is_nonempty_image(v: Any) -> bool:
    if isinstance(v, str):
        return bool(v.strip())
    if isinstance(v, list):
        return any(_is_nonempty_image(x) for x in v)
    if isinstance(v, dict):
        # ImageObject
        return _is_nonempty_image(v.get("url"))
    return False


def _has_geo(v: Any) -> bool:
    if not isinstance(v, dict):
        return False
    lat = v.get("latitude")
    lng = v.get("longitude")
    if isinstance(lat, (int, float)) and isinstance(lng, (int, float)):
        return True
    # Sometimes stored as strings
    try:
        float(lat)
        float(lng)
        return True
    except Exception:
        return False


def _has_contains_place(v: Any) -> bool:
    # Search Console is flagging our VacationRental objects with:
    # "Invalid object type for field 'containsPlace'" when we use @type=Accommodation.
    # To match what Google is accepting for this site, require @type=Place here.
    if isinstance(v, dict):
        return v.get("@type") == "Place"
    if isinstance(v, list):
        return any(isinstance(x, dict) and x.get("@type") == "Place" for x in v)
    return False


def _has_contains_place_occupancy_value(v: Any) -> bool:
    # Some examples include containsPlace.occupancy.value, but Search Console is
    # currently only flagging missing containsPlace itself for this site.
    if not isinstance(v, dict):
        return False
    occ = v.get("occupancy")
    if not isinstance(occ, dict):
        return False
    val = occ.get("value")
    return isinstance(val, int)


def _check_vacation_rental(obj: Any, file: Path, where: str) -> Finding | None:
    if not isinstance(obj, dict):
        return None
    if obj.get("@type") != "VacationRental":
        return None

    missing: list[str] = []

    ident = obj.get("identifier")
    if ident is None or (isinstance(ident, str) and not ident.strip()):
        missing.append("identifier")

    geo = obj.get("geo")
    if not _has_geo(geo):
        missing.append("geo")

    cp = obj.get("containsPlace")
    if not _has_contains_place(cp):
        missing.append("containsPlace")

    img = obj.get("image")
    if not _is_nonempty_image(img):
        missing.append("image")

    if missing:
        return Finding(file=file, where=where, name=obj.get("name"), missing=missing)
    return None


def _walk_for_vacation_rentals(data: Any, file: Path, where_prefix: str) -> list[Finding]:
    out: list[Finding] = []

    if isinstance(data, dict):
        f = _check_vacation_rental(data, file, where_prefix)
        if f:
            out.append(f)

        # Common patterns we use:
        # - ItemList.itemListElement[].item
        if data.get("@type") == "ItemList":
            for i, el in enumerate(data.get("itemListElement", []) or []):
                if isinstance(el, dict) and "item" in el:
                    out.extend(_walk_for_vacation_rentals(el.get("item"), file, f"{where_prefix}.ItemList[{i}].item"))

        # - @graph arrays
        if "@graph" in data:
            out.extend(_walk_for_vacation_rentals(data.get("@graph"), file, f"{where_prefix}.@graph"))

        # - generic dict walk for nested objects
        for k, v in data.items():
            if k in {"itemListElement", "@graph"}:
                continue
            out.extend(_walk_for_vacation_rentals(v, file, f"{where_prefix}.{k}"))

    elif isinstance(data, list):
        for i, v in enumerate(data):
            out.extend(_walk_for_vacation_rentals(v, file, f"{where_prefix}[{i}]"))

    return out


def lint_files(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for file in files:
        html = file.read_text("utf-8", errors="ignore")
        for blob in _iter_jsonld_blobs(html):
            data = _try_load_json(blob)
            if data is None:
                continue
            findings.extend(_walk_for_vacation_rentals(data, file, "jsonld"))
    return findings


def main() -> int:
    # Scope: homepage + stays + properties page if present.
    files = [ROOT / "index.html"]
    files += list((ROOT / "stays").rglob("index.html"))
    if (ROOT / "properties" / "index.html").exists():
        files.append(ROOT / "properties" / "index.html")

    files = [f for f in files if f.exists()]

    findings = lint_files(files)

    if findings:
        print(f"FAIL: VacationRental schema missing required fields in {len(findings)} items")
        for f in findings[:80]:
            print(f"- {f.file.relative_to(ROOT)} :: {f.where} :: {f.name!r} missing={','.join(f.missing)}")
        if len(findings) > 80:
            print(f"... {len(findings) - 80} more")
        return 1

    print("PASS: VacationRental schema required fields present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
