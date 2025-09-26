# Makefile — Zoran Benchmark ARC

reproduce_all:
	python3 run_benchmark.py --input dataset.jsonl --output benchmark_results.json
	python3 analyze.py benchmark_results.json --csv metriques.csv --plots ./
	sha256sum benchmark_results.json metriques.csv > SHA256SUMS.txt
