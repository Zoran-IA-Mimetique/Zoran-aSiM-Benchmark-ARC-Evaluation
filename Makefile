all: reproduce_all

reproduce_all:
	python3 scripts/reproduce.py --input benchmark_results.json --output verification.log
