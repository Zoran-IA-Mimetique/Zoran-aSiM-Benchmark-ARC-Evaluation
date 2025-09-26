SHELL := /bin/bash
PY := python3

setup:
	$(PY) -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

run:
	$(PY) scripts/run_benchmark.py --provider $${PROVIDER:-mock}

run-mock:
	$(PY) scripts/run_benchmark.py --provider mock

eval:
	$(PY) scripts/eval_metrics.py --provider $${PROVIDER:-mock}

eval-mock:
	$(PY) scripts/eval_metrics.py --provider mock

plots:
	$(PY) scripts/plot_results.py

hash:
	$(PY) scripts/compute_hashes.py > SHA256SUMS.txt

sbom:
	$(PY) scripts/generate_sbom.py > sbom.cyclonedx.json

c2pa:
	$(PY) scripts/export_c2pa.py > provenance_c2pa.json

package-zip:
	zip -r zoran_asim_benchmark_pack_v1.zip . -x "*.venv*" -x "__pycache__"

.PHONY: setup run run-mock eval eval-mock plots hash sbom c2pa package-zip
