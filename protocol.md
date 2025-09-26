# 📑 Protocole expérimental — Zoran🦋 aSiM Benchmark ARC

## Corpus
- 200 questions interdisciplinaires
- Sources : ARC (Abstraction & Reasoning Corpus), MMLU lite, questions internes
- Répartition : maths 40 %, logique 30 %, éthique 30 %

## Méthodologie
- Double run systématique : Baseline (modèle nu) vs Zoran augmenté
- IA challengées : Copilot, AI-Studio, DeepSeek, GPT-5
- Seeds fixes : 13, 42, 101
- Split train/test non applicable (Q&A direct)

## Environnement
- Python 3.11, pandas 2.1, matplotlib 3.8
- Hardware : 1× GPU A100, 40 Go RAM

## Métriques
- Exactitude : % réponses correctes
- Complétude : % concepts couverts dans la réponse
- Clarté : score lisibilité (1–5 → normalisé)
- Hallucinations (HR) : % erreurs factuelles
- Biais (BI) : % biais implicites détectés
- Refus éthiques (EC) : qualité et argumentation des refus

## Reproductibilité
- Script `run_benchmark.py`
- Commande : `make reproduce_all`
