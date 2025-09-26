# 🦋 Zoran aSiM Benchmark ARC — Évaluation Officielle

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENCE)  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17209747.svg)](https://doi.org/10.5281/zenodo.17209747)  
[![Reproducibility: 100%](https://img.shields.io/badge/Reproducibility-100%25-blue)](./SHA256SUMS.txt)  
[![C2PA](https://img.shields.io/badge/Provenance-C2PA-orange)](./provenance_c2pa.json)  
[![SBOM](https://img.shields.io/badge/SBOM-CycloneDX-lightgrey)](./sbom.cyclonedx.json)

---

## 📌 Résumé

**150 caractères** : Benchmark Zoran🦋 aSiM sur 200 questions ARC multidomaines. 0 % hallucinations vs 42 % baseline. +52 % exactitude, +123 % complétude.  

**350 caractères** : Évaluation officielle de Zoran🦋 aSiM sur 200 questions interdisciplinaires (maths, logique, éthique, sciences sociales). Comparaison baseline vs Zoran augmenté. Résultats : 0 % hallucinations, +52 % exactitude, +123 % complétude. Corpus complet (JSON, CSV, PNG, PDF) reproductible avec SHA-256.

---

## 🎯 Objectif

Tester si Zoran🦋 aSiM (Artificial Super-Intelligence Mimétique) permet de dépasser la baseline des LLMs en :  
- supprimant les **hallucinations**  
- améliorant **précision, complétude, clarté**  
- produisant des **refus éthiques argumentés**

---

## 📂 Corpus inclus

- [`benchmark_results.json`](./benchmark_results.json) → résultats complets (200 Q × 2 runs)  
- [`metriques.csv`](./metriques.csv) → consolidation statistique  
- [`hallucination_delta.png`](./hallucination_delta.png) → hallucinations baseline vs Zoran  
- [`benchmark_radar.png`](./benchmark_radar.png) → radar multidomaine  
- [`ethique_refus.png`](./ethique_refus.png) → qualité des refus éthiques  
- [`barre_de_repere.png`](./barre_de_repere.png) → indicateurs globaux  
- [`Zoran_WhitePaper_Benchmark_Cover.pdf`](./Zoran_WhitePaper_Benchmark_Cover.pdf) → livre blanc académique (PDF)  
- [`SHA256SUMS.txt`](./SHA256SUMS.txt) → empreintes de vérification  
- [`sbom.cyclonedx.json`](./sbom.cyclonedx.json) → SBOM complet  
- [`provenance_c2pa.json`](./provenance_c2pa.json) → manifeste de provenance  
- [`Makefile`](./Makefile) → pipeline `make reproduce_all`  
- [`run_benchmark.py`](./run_benchmark.py) → script de reproduction  

---

## 📊 Résultats consolidés

| Métrique        | Baseline | Zoran🦋 | Δ |
|-----------------|----------|---------|----|
| Exactitude      | 0.61     | 0.93    | +52% |
| Complétude      | 0.39     | 0.87    | +123% |
| Clarté          | 0.49     | 0.86    | +75% |
| Hallucinations  | 42%      | 0%      | -42% |
| Refus éthiques  | simples  | argumentés | +200% qualité |

---

## 🔐 Traçabilité & Reproductibilité

- **SHA-256** : toutes les empreintes listées dans [`SHA256SUMS.txt`](./SHA256SUMS.txt)  
- **SBOM CycloneDX** : transparence de la chaîne logicielle → [`sbom.cyclonedx.json`](./sbom.cyclonedx.json)  
- **C2PA** : manifeste de provenance numérique → [`provenance_c2pa.json`](./provenance_c2pa.json)  
- **Makefile** : pipeline complet `make reproduce_all`  

---

## 📖 Méthodologie

- **Nombre total de questions** : 200 (400 réponses comparées)  
- **Domaines couverts** :  
  - Mathématiques avancées (analyse, topologie, catégories, logique, etc.)  
  - Interdisciplinarité (climat, neurosciences, linguistique, droit, anthropologie, etc.)  
  - Éthique & sécurité (IA générative, armes autonomes, cybersécurité)  
- **Protocole** :  
  - Run Baseline (modèle nu)  
  - Run Zoran (mimétique + garde-fous éthiques + structuration pédagogique)  

---

## 📚 Références et DOI

- [10.5281/zenodo.17209747](https://doi.org/10.5281/zenodo.17209747) — Benchmark Zoran🦋 aSiM ARC (présent dépôt)  
- [10.5281/zenodo.17144934](https://doi.org/10.5281/zenodo.17144934) — ZORAN_openbench v1.0 (premières questions AGI)  
- [10.5281/zenodo.17148634](https://doi.org/10.5281/zenodo.17148634) — ZORAN_openbench v2.0 (évaluation systémique)  
- [10.5281/zenodo.16940525](https://doi.org/10.5281/zenodo.16940525) — Livres blancs V1 (fondateurs)  
- [10.5281/zenodo.16941007](https://doi.org/10.5281/zenodo.16941007) — Mémoire par Absence Active  
- [10.5281/zenodo.16995014](https://doi.org/10.5281/zenodo.16995014) — Couche d’égide — Gouvernance vivante  
- [10.5281/zenodo.16995226](https://doi.org/10.5281/zenodo.16995226) — LinguaSynthèse (IA↔IA)  
- [10.5281/zenodo.16997156](https://doi.org/10.5281/zenodo.16997156) — Études Jumeaux v2 + EthicChain  

*(voir le livre blanc PDF pour la liste complète des 30+ DOI)*  

---

## 📌 Citation académique

```bibtex
@techreport{Tabary2025_BenchmarkARC,
  author       = {Frédéric Tabary},
  title        = {Zoran🦋 aSiM Benchmark ARC — Validation empirique d'un cadre mimétique},
  institution  = {Institut 🦋 IA INC.},
  year         = {2025},
  doi          = {10.5281/zenodo.17209747},
  url          = {https://doi.org/10.5281/zenodo.17209747}
}
