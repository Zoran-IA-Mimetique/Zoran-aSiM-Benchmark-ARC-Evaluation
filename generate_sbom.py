#!/usr/bin/env python3
import json, pathlib, hashlib, os
BASE = pathlib.Path(__file__).resolve().parents[1]

components = [
  {"name": "python", "version": "3.11", "type": "platform"},
  {"name": "pandas", "version": "2.2.2", "type": "library"},
  {"name": "matplotlib", "version": "3.8.4", "type": "library"},
  {"name": "pyyaml", "version": "6.0.1", "type": "library"},
]

doc = {
  "bomFormat": "CycloneDX",
  "specVersion": "1.5",
  "version": 1,
  "metadata": {
    "timestamp": __import__("datetime").datetime.utcnow().isoformat() + "Z",
    "tools": [{"vendor":"zoran","name":"sbom-lite","version":"1.0"}]
  },
  "components": components
}
print(json.dumps(doc, indent=2))
