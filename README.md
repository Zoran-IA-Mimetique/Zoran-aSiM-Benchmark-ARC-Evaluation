# 🦋 Zoran aSiM Benchmark ARC — Évaluation officielle

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17209747.svg)](https://doi.org/10.5281/zenodo.17209747)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Reproducibility: 100%](https://img.shields.io/badge/Reproducibility-100%25-blue.svg)](SHA256SUMS.txt)
[![Compliance: AI Act + ISO 42001](https://img.shields.io/badge/Compliance-AIAct%20%2B%20ISO42001-orange.svg)](provenance_c2pa.json)

Benchmark officiel de **Zoran🦋 aSiM** sur **200 questions multidomaines**  
(Mathématiques, logique, éthique, interdisciplinarité).

---

## 📊 Résultats clés
- **Exactitude** : 0.61 → 0.93 (+52%)
- **Complétude** : 0.39 → 0.87 (+123%)
- **Clarté** : 0.49 → 0.86 (+75%)
- **Hallucinations** : 42% → 0% (-42%)
- **Refus éthiques** : +200% qualité (argumentés)

---

## 📂 Corpus inclus
- `benchmark_results.json` → résultats complets par question (200 Q × 2 runs)
- `metriques.csv` → consolidation statistique
- `hallucination_delta.png` → comparaison hallucinations baseline vs Zoran
- `benchmark_radar.png` → radar multidomaine
- `ethique_refus.png` → qualité des refus éthiques
- `barre_de_repere.png` → indicateurs globaux
- `SHA256SUMS.txt` → empreintes de vérification
- `sbom.cyclonedx.json` → SBOM complet
- `provenance_c2pa.json` → provenance C2PA signée
- `Zoran_WhitePaper_Benchmark_Cover.pdf` → white paper académique (PDF)

---

## 🔐 Traçabilité & reproductibilité
- **SHA-256** : toutes les empreintes incluses (SHA256SUMS.txt)
- **SBOM CycloneDX** : transparence de la chaîne logicielle
- **C2PA** : manifeste de provenance numérique
- **Makefile** : pipeline `make reproduce_all` pour vérification complète

---

## 📖 Citation académique
Frédéric Tabary (2025). *Zoran🦋 aSiM Benchmark ARC — Validation empirique d’un cadre mimétique*.  
Zenodo. DOI: [10.5281/zenodo.17209747](https://doi.org/10.5281/zenodo.17209747)

---

## 📧 Contact
**Frédéric Tabary — INSTITUT🦋 IA INC.**  
7100-380, rue Saint-Antoine Ouest, Montréal (Québec) H2Y 3X7  
21 rue Eugène Roinet, 49000 Angers, France  
📩 tabary01@gmail.com
