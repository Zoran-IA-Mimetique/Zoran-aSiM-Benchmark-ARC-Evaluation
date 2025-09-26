#!/usr/bin/env python3
import json, os, pathlib, hashlib, datetime

BASE = pathlib.Path(__file__).resolve().parents[1]

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

manifest = {
  "type": "c2pa-lite",
  "author": "Frédéric Tabary",
  "date": datetime.datetime.utcnow().isoformat() + "Z",
  "files": []
}

for root, dirs, files in os.walk(BASE):
    for fn in files:
        p = pathlib.Path(root) / fn
        rel = p.relative_to(BASE).as_posix()
        if fn in ["provenance_c2pa.json","sbom.cyclonedx.json","SHA256SUMS.txt"]:
            # They'll be produced too — acceptable to include self-hash or skip
            pass
        manifest["files"].append({"path": rel, "sha256": sha256(p)})

print(json.dumps(manifest, indent=2))
