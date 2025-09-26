# 📑 Protocole expérimental — Benchmark Zoran🦋 aSiM

## 🎯 Objectif
Évaluer Zoran aSiM (Artificial Super-Intelligence Mimétique) sur un benchmark de 200 questions multidomaines.

## 📂 Dataset
- Taille : 200 questions (mathématiques, logique, éthique, interdisciplinarité).
- Format : JSONL (200 Q × 2 runs).
- Disponibilité : inclus dans `benchmark_results.json`.

## 🔑 Baseline
- Comparaison avec modèles nus : Copilot, AI-Studio, DeepSeek, ChatGPT-5.

## 🧮 Métriques
- Exactitude (EM)
- Complétude (coverage des éléments attendus)
- Clarté (notation pédagogique)
- Hallucinations (HR)
- Biais implicites (BI)
- Refus éthiques (EC)

## 🔄 Reproductibilité
- Seeds fixes : 13, 42, 101
- Exécution : `make reproduce_all`
- Dépendances : Python 3.11, pandas, matplotlib
- Hardware : CPU standard (pas de dépendance GPU)
