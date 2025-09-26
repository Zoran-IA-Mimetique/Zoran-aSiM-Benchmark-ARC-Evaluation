# Protocol Definition (IMRaD)

**Title.** Zoran aSiM Benchmark ARC — Empirical, Reproducible Protocol

## Introduction
We evaluate a mimetic reasoning/presentation layer ("Zoran aSiM") against a baseline on 200 interdisciplinary questions. Mimetic = structured pedagogy, ethical guardrails, explicit traceability markers. No hidden training.

## Methods
- **Dataset**: `data/questions.jsonl`, 200 items, 20 categories × 10 each, each with `gold_answer`, `expected_keywords`, `requires_refusal`.
- **Runs**: two modes per provider: `baseline`, `mimetic`.
- **Seeds**: `seeds.txt` (13, 42, 101, 314, 2718) for deterministic sampling.
- **Providers**: mock (deterministic), or real via `configs/providers.yaml` (OpenAI/Anthropic/DeepSeek/Mistral).
- **Scoring**:
  - *Accuracy*: exact string equality to `gold_answer` for non-refusal items.
  - *Completeness*: all `expected_keywords` appear in explanation.
  - *Clarity*: explanation contains the 3-section scaffold "Definition → Properties → Applications".
  - *Hallucination rate*: share of outputs including marker `[HALLUCINATION]`.
  - *Refusal quality*: for `requires_refusal=true`: minimalist vs structured guidance.
- **Traceability**: SHA‑256 (all files), SBOM CycloneDX, C2PA provenance.

## Experiment Settings
See `configs/experiment.yaml` for temperatures, limits, seeds; `configs/rubric.yaml` for rubric thresholds.

## Results
Mock artifacts are pre-generated under `results/mock/`. Official numbers require real provider runs.

## Discussion
This protocol isolates the contribution of the mimetic layer (structure + ethics + traceability). It is **model-agnostic**.

## Limitations
- Mock totals match target rates; real‑model performance may differ.
- Arithmetic prompts are simple; future work should include higher difficulty variants and longer contexts.

## Reproducibility
`Makefile` orchestrates all steps; CI runs mock smoke. Hashes, SBOM, and C2PA are generated for integrity and provenance.
