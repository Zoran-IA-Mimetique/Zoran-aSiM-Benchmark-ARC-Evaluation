#!/usr/bin/env python3
import os, hashlib, pathlib, sys

BASE = pathlib.Path(__file__).resolve().parents[1]

def sha256_file(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    for root, dirs, files in os.walk(BASE):
        for fn in sorted(files):
            if fn == "SHA256SUMS.txt":  # skip self
                continue
            p = pathlib.Path(root) / fn
            rel = p.relative_to(BASE).as_posix()
            print(f"{sha256_file(p)}  {rel}")

if __name__ == "__main__":
    main()
