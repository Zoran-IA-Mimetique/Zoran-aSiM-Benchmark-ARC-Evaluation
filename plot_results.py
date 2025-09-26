#!/usr/bin/env python3
import pathlib, csv
import matplotlib.pyplot as plt

BASE = pathlib.Path(__file__).resolve().parents[1]
SUM = BASE / "results" / "mock" / "metrics_summary.csv"
PLOTS = BASE / "results" / "mock" / "plots"
PLOTS.mkdir(parents=True, exist_ok=True)

def read_summary():
    rows = {}
    with open(SUM, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows[r["mode"]] = r
    return rows

def to_float(s): 
    try: return float(s)
    except: return 0.0

rows = read_summary()

# Bar: Accuracy, Completeness, Clarity
for metric in ["accuracy","completeness","clarity"]:
    fig = plt.figure()
    xs = ["baseline","mimetic"]
    ys = [to_float(rows["baseline"][metric]), to_float(rows["mimetic"][metric])]
    plt.bar(xs, ys)
    plt.title(metric.capitalize())
    plt.ylim(0, 1)
    fig.savefig(PLOTS / f"{metric}_bar.png", bbox_inches="tight")
    plt.close(fig)

# Bar: Hallucination
fig = plt.figure()
xs = ["baseline","mimetic"]
ys = [to_float(rows["baseline"]["hallucination_rate"]), to_float(rows["mimetic"]["hallucination_rate"])]
plt.bar(xs, ys)
plt.title("Hallucination rate")
plt.ylim(0, 1)
fig.savefig(PLOTS / "hallucination_bar.png", bbox_inches="tight")
plt.close(fig)

# Bar: Refusal quality (structured)
fig = plt.figure()
xs = ["baseline","mimetic"]
ys = [to_float(rows["baseline"]["rq_structured"]), to_float(rows["mimetic"]["rq_structured"])]
plt.bar(xs, ys)
plt.title("Refusal quality (structured)")
plt.ylim(0, 1)
fig.savefig(PLOTS / "refusal_quality_structured_bar.png", bbox_inches="tight")
plt.close(fig)
