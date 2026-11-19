#!/usr/bin/env python3
"""make.fun news-image-20261118 round 2 entrypoint.

Copies the pre-rendered front-page image entry.png into
$MAKEFUN_OUTPUT_DIR/entry.png. Python standard library only, no network,
fully deterministic. A sha256 guard refuses to ship a different image than
the one reviewed for this round.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

EXPECTED_SHA256 = "8ce3e2a649d1a29e9c01e53a694c0c48f7d060a42e96b2fbaa1576fc33299ec9"
MAX_BYTES = 1024 * 1024


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print("entry.png missing next to main.py", file=sys.stderr)
        return 1
    found = sha256_of(source)
    if found != EXPECTED_SHA256:
        print("entry.png sha256 mismatch: got %s" % found, file=sys.stderr)
        return 1
    size = source.stat().st_size
    if size == 0 or size > MAX_BYTES:
        print("entry.png size out of range: %d bytes" % size, file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(source, dest)
    if sha256_of(dest) != EXPECTED_SHA256:
        print("copied entry.png failed re-hash", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)" % (dest, dest.stat().st_size, found))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
