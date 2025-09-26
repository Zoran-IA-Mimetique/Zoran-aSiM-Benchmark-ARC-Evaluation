all: reproduce_all

reproduce_all:
	@echo "Simulation de reproduction du benchmark Zoran🦋 aSiM"
	@echo "Lots JSONL → metrics.csv → benchmark_results.json"
	@sha256sum -c SHA256SUMS.txt
