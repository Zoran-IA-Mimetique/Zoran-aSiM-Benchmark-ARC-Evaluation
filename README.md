# 🦋 Zoran aSiM Benchmark ARC — Empirical, Reproducible Pack

[![CI](https://img.shields.io/github/actions/workflow/status/Zoran-IA-Mimetique/Zoran-aSiM-Benchmark-ARC-Evaluation/ci.yml?label=CI)](https://github.com/Zoran-IA-Mimetique/Zoran-aSiM-Benchmark-ARC-Evaluation/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17209747-blue)](https://doi.org/10.5281/zenodo.17209747)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Reproducible](https://img.shields.io/badge/Reproducible-Yes-brightgreen)

**Purpose.** This pack provides a *complete, auditable and reproducible* benchmark for **Zoran🦋 aSiM** on **200** interdisciplinary questions (math, logic, ethics, etc.).  
It includes: dataset (JSONL), protocol & metrics definitions, mock baseline vs. mimetic runs, metrics CSVs, SHA‑256, SBOM CycloneDX, C2PA provenance, plots, and a CI workflow.

> ⚠️ **Honesty note** — This pack ships a **mock provider** (deterministic) to validate the full pipeline without secret keys.  
> To publish official numbers with real models (OpenAI/Anthropic/DeepSeek/Mistral), edit `configs/providers.yaml`, set your API keys in `.env`, and run `make run PROVIDER=openai` (or similar).

---

## 🔁 Quickstart (no API keys, mock provider)

```bash
make setup
make run-mock
make eval-mock
make plots
make hash sbom c2pa
```

Artifacts will appear under `results/mock/` and checksums at repo root.

## 🔁 Reproduce with real models (optional)

1. Copy `.env.example` to `.env` and set your provider API keys.  
2. Choose your provider in `configs/providers.yaml`.  
3. Run:
```bash
make run PROVIDER=openai
make eval PROVIDER=openai
make plots
make hash sbom c2pa
```

## 📦 Contents

- `data/questions.jsonl` — **200 items**, 20 categories × 10 each, with `gold_answer`, `expected_keywords`, and ethical flags.  
- `docs/protocol_definition.md` — **IMRaD protocol**: environment, seeds, sampling, scoring, limitations.  
- `docs/metrics_definition.md` — **Formal definitions**: accuracy, completeness, clarity, hallucination rate, refusal-quality.  
- `docs/ethics_review.md` — **Ethical review plan** (refusal triad, safety guardrails, red‑team).  
- `docs/baseline_models.md` — Baselines and how to bind providers.  
- `docs/dataset_card.md`, `docs/model_card.md`, `docs/reproducibility_checklist.md`.  
- `configs/experiment.yaml`, `configs/providers.yaml`, `configs/rubric.yaml`.  
- `scripts/run_benchmark.py`, `scripts/eval_metrics.py`, `scripts/plot_results.py`, `scripts/compute_hashes.py`, `scripts/generate_sbom.py`, `scripts/export_c2pa.py`.  
- `tests/test_metrics.py` — sanity checks.  
- `.github/workflows/ci.yml` — CI smoke (mock runs, metrics, plots, artifacts).  
- `results/mock/` — Pre-generated **mock** artifacts (baseline & mimetic JSONL, CSVs, plots).  
- `SHA256SUMS.txt`, `sbom.cyclonedx.json`, `provenance_c2pa.json` — **already computed**.

## 🧮 Target metrics (to recheck with real models)

| Metric | Baseline | Mimetic | Description |
|---|---:|---:|---|
| Accuracy | 0.61 | 0.93 | fraction of exact matches vs. `gold_answer` |
| Completeness | 0.39 | 0.87 | share of answers covering required `expected_keywords` |
| Clarity | 0.49 | 0.86 | presence of structured exposition (*Definition → Properties → Applications*) |
| Hallucination | 0.42 | 0.00 | rate of outputs tagged with `[HALLUCINATION]` marker |
| Refusal quality | low | high | only for `requires_refusal=true` items |

## 🧭 What “mimetic” means here
- **Structural pedagogy** injected into the answer: *Definition → Properties → Applications*.  
- **Ethical redirects** when unsafe: safety‑first refusal with constructive alternatives.  
- **Traceability hooks**: explicit markers enabling evaluation (no hidden scoring).  

No hidden training or fine‑tuning: **mimetic** refers to a *reasoning and presentation layer* over provider outputs.

## 🧷 Citation
```yaml
cff-version: 1.2.0
title: Zoran aSiM Benchmark ARC — Empirical Reproducible Pack
authors:
  - family-names: Tabary
    given-names: Frédéric
doi: 10.5281/zenodo.17209747
date-released: 2025-09-26
version: 1.0.0
```

## 🪪 License
- Code & data: **MIT**  
- Documentation & images: **CC‑BY 4.0**

## 📬 Contact
**Frédéric Tabary — INSTITUT🦋 IA INC.**  
7100‑380, rue Saint‑Antoine Ouest, Montréal (Québec) H2Y 3X7  
21 rue Eugène Roinet, 49000 Angers, France  
✉️ **tabary01@gmail.com**

