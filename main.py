#!/usr/bin/env python3
"""Copy the entry image to the output directory.

Reads entry.png (shipped beside this file) and writes it byte for byte to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output). No network, deterministic.
"""
import hashlib
import os
import sys
from pathlib import Path

MAX_BYTES = 1048576
EXPECTED_SHA256 = "fcd4dc01110d8e454ec4e57914e14ffc5af05920b793252b4c5afbe0f6e82fce"


def main() -> int:
    src = Path(__file__).resolve().with_name("entry.png")
    if not src.is_file():
        print(f"missing entry image: {src}", file=sys.stderr)
        return 1
    data = src.read_bytes()
    if len(data) > MAX_BYTES:
        print(f"entry image too large: {len(data)} bytes", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"entry image digest mismatch: {digest}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "entry.png"
    out.write_bytes(data)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
