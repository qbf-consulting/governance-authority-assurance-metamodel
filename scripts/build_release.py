#!/usr/bin/env python3
"""Build a byte-reproducible GAAM source distribution."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REL = json.loads((ROOT / "release.json").read_text())
VERSION = REL["version"]
OUT = ROOT / "dist"
TARGET = OUT / f"governance-authority-assurance-metamodel-v{VERSION}.zip"
RECORD = OUT / f"governance-authority-assurance-metamodel-v{VERSION}.release.json"
EXCLUDED_PARTS = {
    ".git", ".bundle", ".gems", ".jekyll-cache", ".mypy_cache", ".pytest_cache",
    ".ruff_cache", ".venv", "__pycache__", "dist", "node_modules", "vendor", "_site",
}


def source_epoch() -> int:
    explicit = os.environ.get("SOURCE_DATE_EPOCH")
    if explicit:
        return int(explicit)
    try:
        value = subprocess.check_output(
            ["git", "log", "-1", "--format=%ct"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
        return int(value)
    except (OSError, subprocess.CalledProcessError, ValueError):
        return int(datetime.datetime.fromisoformat(REL["releaseDate"]).replace(tzinfo=datetime.timezone.utc).timestamp())


epoch = max(source_epoch(), 315532800)  # ZIP timestamps cannot predate 1980.
stamp = datetime.datetime.fromtimestamp(epoch, datetime.timezone.utc)
zip_stamp = (stamp.year, stamp.month, stamp.day, stamp.hour, stamp.minute, stamp.second - stamp.second % 2)
files = [p for p in ROOT.rglob("*") if p.is_file() and not EXCLUDED_PARTS.intersection(p.parts)]
OUT.mkdir(exist_ok=True)
with zipfile.ZipFile(TARGET, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in sorted(files, key=lambda p: str(p.relative_to(ROOT))):
        info = zipfile.ZipInfo(
            str(Path(f"governance-authority-assurance-metamodel-v{VERSION}") / path.relative_to(ROOT)),
            date_time=zip_stamp,
        )
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        info.create_system = 3
        archive.writestr(info, path.read_bytes())

digest = hashlib.sha256(TARGET.read_bytes()).hexdigest()
record = {
    "releaseVersion": VERSION,
    "normativeVersion": REL["normativeVersion"],
    "candidateBaseline": REL["candidateBaseline"],
    "sourceDateEpoch": epoch,
    "archive": TARGET.name,
    "sha256": digest,
    "fileCount": len(files),
}
RECORD.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
