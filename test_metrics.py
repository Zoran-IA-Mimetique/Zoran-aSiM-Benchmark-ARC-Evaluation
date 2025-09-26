import pathlib, json, csv

def test_basic_metrics_loading():
    base = pathlib.Path(__file__).resolve().parents[1]
    sum_csv = base / "results" / "mock" / "metrics_summary.csv"
    assert sum_csv.exists(), "metrics_summary.csv not found"

    with open(sum_csv, "r", encoding="utf-8") as f:
        header = f.readline().strip().split(",")
    assert "accuracy" in header and "completeness" in header and "clarity" in header

