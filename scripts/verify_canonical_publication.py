#!/usr/bin/env python3
"""Verify canonical GAAM schema publication locally or over HTTPS."""
from pathlib import Path
import argparse
import hashlib
import json
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "schemas/catalog.json").read_text())


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
source.add_argument("--remote", action="store_true", help="retrieve canonical catalog URLs")
parser.add_argument("--attempts", type=int, default=4)
parser.add_argument("--output", type=Path)
args = parser.parse_args()

checks = []
for entry in CATALOG["schemas"]:
    expected_path = ROOT / "schemas" / entry["name"]
    expected = expected_path.read_bytes()
    canonical = entry["id"]
    try:
        if args.site_root:
            marker = "/governance-authority-assurance-metamodel/"
            published_path = args.site_root / canonical.split(marker, 1)[1]
            actual = published_path.read_bytes()
            resolved = str(published_path)
        else:
            actual, resolved = remote_bytes(canonical, args.attempts)
        ok = actual == expected and resolved == canonical if args.remote else actual == expected
        detail = "canonical bytes match source" if ok else f"content or canonical URL mismatch; resolved={resolved}"
    except Exception as error:
        ok = False
        detail = str(error)
    checks.append({"schema": entry["name"], "canonicalId": canonical, "status": "pass" if ok else "fail", "sourceSha256": hashlib.sha256(expected).hexdigest(), "detail": detail})

report = {
    "releaseVersion": "0.9.1",
    "normativeVersion": "0.9.0",
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
