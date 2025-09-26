# 🦋 Zoran aSiM Benchmark ARC — Évaluation Officielle

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17209747.svg)](https://doi.org/10.5281/zenodo.17209747)
[![Licence: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Reproductible](https://img.shields.io/badge/Reproductibility-100%25-blue.svg)](#)
[![Conformité](https://img.shields.io/badge/AI%20Act-ISO42001-yellow.svg)](#)

## 🎯 Objectif
Évaluer les performances de **Zoran🦋 aSiM** (Artificial Super-Intelligence Mimétique) sur un benchmark de **200 questions interdisciplinaires** (mathématiques, logique, éthique).

## 📊 Résultats consolidés
| Métrique        | Baseline | Zoran | Delta  |
|-----------------|----------|-------|--------|
| Exactitude      | 0.61     | 0.93  | +52 % |
| Complétude      | 0.39     | 0.87  | +123 % |
| Clarté          | 0.49     | 0.86  | +75 % |
| Hallucinations  | 42 %     | 0 %   | -42 % |
| Refus éthiques  | simples  | argumentés | +200 % |

## 📂 Corpus inclus
- `benchmark_results.json` → résultats complets (200 × 2 runs)
- `metrics.csv` → consolidation statistique
- `comparisons.csv` → baseline vs Zoran
- `hallucination_delta.png`, `benchmark_radar.png`, `barre_de_repere.png`, `ethique_refus.png` → visuels
- `SHA256SUMS.txt` → empreintes
- `sbom.cyclonedx.json` → SBOM complet
- `provenance_c2pa.json` → manifeste C2PA
- `Zoran_WhitePaper_Benchmark_Cover.pdf` → white paper académique

## 🔐 Traçabilité & Reproductibilité
- **SHA-256** : empreintes de tous les fichiers
- **SBOM CycloneDX** : transparence supply chain logicielle
- **C2PA** : provenance signée
- **Makefile** : pipeline `make reproduce_all`

## 📖 Citation académique
Frédéric Tabary (2025). *Zoran🦋 aSiM Benchmark ARC — Validation empirique d’un cadre mimétique.* Zenodo. DOI: [10.5281/zenodo.17209747](https://doi.org/10.5281/zenodo.17209747)

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
Frédéric Tabary — **INSTITUT🦋 IA INC.**  
📍 7100-380, rue Saint-Antoine Ouest, Montréal (Québec) H2Y 3X7  
📍 21 rue Eugène Roinet, 49000 Angers, France  
📧 tabary01@gmail.com  

---
Licence : MIT (code/données) + CC-BY 4.0 (docs/images)
