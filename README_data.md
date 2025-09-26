# Zoran🦋 aSiM Benchmark ARC — Données empiriques

Ce dossier contient **toutes les preuves empiriques** du benchmark ARC appliqué à Zoran🦋 aSiM.

## 📂 Contenu
- `lot_01.jsonl` → `lot_11.jsonl` : lots bruts de questions/réponses
- `metrics.csv` : consolidation statistique
- `benchmark_results.json` : résumé chiffré (200 Q × 2 runs)
- `SHA256SUMS.txt` : empreintes d’intégrité SHA-256 pour chaque fichier

## 🔬 Définition des métriques
- **Exactitude** : proportion de réponses correctes / totales
- **Complétude** : couverture des concepts requis dans la réponse
- **Clarté** : lisibilité et structure pédagogique (notation 0–1)
- **Hallucinations** : proportion de réponses contenant des faits inventés
- **Refus éthiques** : % de refus conformes aux principes RGPD / AI Act

## 🔐 Traçabilité
- Empreintes SHA256 incluses → vérifiez avec `sha256sum -c SHA256SUMS.txt`
- Reproductibilité assurée avec `make reproduce_all`

## 📖 Références
Zenodo DOI : https://doi.org/10.5281/zenodo.17209747
