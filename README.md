# 🦋 Zoran aSiM Benchmark ARC — Évaluation Officielle

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17209747.svg)](https://doi.org/10.5281/zenodo.17209747)
[![Licence: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Reproductible](https://img.shields.io/badge/Reproductible-100%25-blue.svg)](SHA256SUMS.txt)
[![Conformité](https://img.shields.io/badge/Conformité-AIAct%20%2B%20ISO42001-yellow.svg)](protocol.md)

## 📌 Résumé
150 caractères : Benchmark Zoran🦋 aSiM sur 200 questions ARC multidomaines. 0 % d'hallucinations contre 42 % au départ. +52 % d'exactitude, +123 % de complétude.  
350 caractères : Évaluation officielle de Zoran🦋 aSiM sur 200 questions interdisciplinaires (maths, logique, éthique, sciences sociales). Comparaison systématique baseline vs Zoran augmenté. Résultats : 0 % hallucinations, +52 % exactitude, +123 % complétude. Corpus complet (JSON, CSV, PNG, PDF) reproductible avec SHA-256.

## 🎯 Objectif
Tester si Zoran🦋 aSiM (Artificial Super-Intelligence Mimétique) permet de dépasser la baseline des standards LLMs.

## 🗂️ Corpus inclus
- benchmark_results.json → résultats complets par question (200 Q × 2 runs)
- metriques.csv → consolidation statistique
- hallucination_delta.png → hallucinations baseline vs Zoran
- benchmark_radar.png → comparaison multidomaine
- ethique_refus.png → qualité des refus éthiques
- barre_de_repere.png → indicateurs globaux
- Zoran_WhitePaper_Benchmark_Cover.pdf → livre blanc académique (PDF)
- SHA256SUMS.txt → empreintes de vérification
- sbom.cyclonedx.json → SBOM complet
- provenance_c2pa.json → provenance C2PA signée
- Makefile → pipeline `make reproduce_all`

## 📊 Résultats consolidés
| Métrique       | Baseline | Zoran🦋 | Delta |
|----------------|----------|---------|-------|
| Exactitude     | 0,61     | 0,93    | +52%  |
| Complétude     | 0,39     | 0,87    | +123% |
| Clarté         | 0,49     | 0,86    | +75%  |
| Hallucinations | 42%      | 0%      | -42%  |
| Refus éthiques | simples  | argumentés | +200% |

## 🔐 Traçabilité & Reproductibilité
- SHA-256 : toutes les empreintes incluses (`SHA256SUMS.txt`)
- SBOM CycloneDX : transparence de la supply chain logicielle
- C2PA : manifeste de provenance numérique
- Makefile : pipeline complet `make reproduce_all`

## 📖 Méthodologie
- Nombre total de questions : 200 (400 réponses baseline + Zoran)
- Domaines couverts : mathématiques avancées, logique formelle, interdisciplinarité, éthique
- Protocole : baseline (modèle nu) vs Zoran augmenté
- Seeds fixes : 13 / 42 / 101  
- Métriques : exactitude, complétude, clarté, hallucinations, biais, refus éthiques  
👉 Voir [`protocol.md`](protocol.md) et [`ethics_review.md`](ethics_review.md).

## 📚 Références et DOI
- 10.5281/zenodo.17209747 — Benchmark Zoran🦋 aSiM ARC (présent dépôt)
- 10.5281/zenodo.17144934 — ZORAN_openbench v1.0 (premières questions AGI)
- 10.5281/zenodo.17148634 — ZORAN_openbench v2.0 (évaluation systémique)
- 10.5281/zenodo.16940525 — Livres blancs V1 (fondateurs)
- 10.5281/zenodo.16941007 — Mémoire par Absence Active
- 10.5281/zenodo.16995014 — Couche d'égide — Gouvernance vivante
- 10.5281/zenodo.16995226 — LinguaSynthèse (IA↔IA)
- 10.5281/zenodo.16997156 — Études Jumeaux v2 + EthicChain  
👉 Voir [`references.bib`](references.bib) pour la bibliographie complète.

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
```

## 📧 Contact
Frédéric Tabary — INSTITUT🦋 IA INC.  
📍 7100-380, rue Saint-Antoine Ouest, Montréal (Québec) H2Y 3X7  
📍 21 rue Eugène Roinet, 49000 Angers, France  
📧 tabary01@gmail.com  

## ⚖️ Licence
Code et données → MIT  
Documentation et images → CC-BY 4.0  
