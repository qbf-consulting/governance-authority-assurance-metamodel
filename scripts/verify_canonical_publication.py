#!/usr/bin/env python3
"""Verify retained GAAM schema bytes at the current publication location.

The v0.9.0 schema $id values are retained normative identifiers and are not
rewritten when repository stewardship or hosting changes. release.json may
therefore declare a publicationBase distinct from schemaBase. Verification
checks the published bytes at publicationBase while reporting the retained
schema identity separately.
"""
from pathlib import Path
import argparse
import hashlib
import json
import time
import urllib.error
import urllib.request
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "schemas/catalog.json").read_text())
RELEASE = json.loads((ROOT / "release.json").read_text())
PUBLICATION_BASE = RELEASE.get("publicationBase", RELEASE["schemaBase"])
ALLOWED_PUBLICATION_BASES = RELEASE.get("allowedPublicationBases", [PUBLICATION_BASE])


def publication_url_allowed(requested_url, resolved_url):
    """Require HTTPS and preserve the schema-relative path across approved publication origins."""
    requested = urlparse(requested_url)
    resolved = urlparse(resolved_url)
    if requested.scheme != "https" or resolved.scheme != "https":
        return False
    relative_path = requested.path[len(urlparse(PUBLICATION_BASE).path):].lstrip("/")
    for base in ALLOWED_PUBLICATION_BASES:
        parsed_base = urlparse(base)
        expected_path = parsed_base.path.rstrip("/") + "/" + relative_path
        if (resolved.scheme, resolved.netloc, resolved.path) == (parsed_base.scheme, parsed_base.netloc, expected_path):
            return True
    return False


def remote_bytes(url, attempts):
    last = None
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "gaam-publication-verifier/0.9.1"})
            with urllib.request.urlopen(request, timeout=20) as response:
                return response.read(), response.geturl()
        except (urllib.error.URLError, TimeoutError) as error:
            last = error
            if attempt + 1 < attempts:
                time.sleep(min(2 ** attempt, 8))
    raise last


parser = argparse.ArgumentParser(description=__doc__)
source = parser.add_mutually_exclusive_group(required=True)
source.add_argument("--site-root", type=Path, help="rendered site directory")
source.add_argument("--remote", action="store_true", help="retrieve current publication URLs")
parser.add_argument("--attempts", type=int, default=4)
parser.add_argument("--output", type=Path)
args = parser.parse_args()

checks = []
for entry in CATALOG["schemas"]:
    expected_path = ROOT / "schemas" / entry["name"]
    expected = expected_path.read_bytes()
    declared_id = entry["id"]
    publication_url = PUBLICATION_BASE.rstrip("/") + "/" + entry["name"]
    try:
        if args.site_root:
            version = RELEASE["normativeVersion"]
            published_path = args.site_root / f"v{version}" / "schemas" / entry["name"]
            actual = published_path.read_bytes()
            resolved = str(published_path)
            ok = actual == expected
        else:
            actual, resolved = remote_bytes(publication_url, args.attempts)
            ok = actual == expected and publication_url_allowed(publication_url, resolved)
        detail = "published bytes match retained source" if ok else f"content or publication URL mismatch; resolved={resolved}"
    except Exception as error:
        ok = False
        detail = str(error)
    checks.append({
        "schema": entry["name"],
        "declaredId": declared_id,
        "publicationUrl": publication_url,
        "status": "pass" if ok else "fail",
        "sourceSha256": hashlib.sha256(expected).hexdigest(),
        "detail": detail,
    })

report = {
    "releaseVersion": RELEASE["version"],
    "normativeVersion": RELEASE["normativeVersion"],
    "mode": "remote" if args.remote else "rendered-site",
    "status": "pass" if all(check["status"] == "pass" for check in checks) else "fail",
    "checks": checks,
}
encoded = json.dumps(report, indent=2) + "\n"
if args.output:
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(encoded)
print(encoded, end="")
raise SystemExit(0 if report["status"] == "pass" else 1)
