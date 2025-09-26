all: reproduce_all

reproduce_all:
	python run_benchmark.py --provider mock --output benchmark_results.json
	python run_metrics.py --input benchmark_results.json --output metriques.csv
	sha256sum benchmark_results.json metriques.csv > SHA256SUMS.txt
