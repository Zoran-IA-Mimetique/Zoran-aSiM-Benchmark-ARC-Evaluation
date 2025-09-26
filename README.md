# 🦋 Zoran aSiM Benchmark ARC — Évaluation officielle

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17209747.svg)](https://doi.org/10.5281/zenodo.17209747)
[![Licence: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Reproductibilité](https://img.shields.io/badge/Reproducibility-100%25-blue.svg)]()
[![Conformité](https://img.shields.io/badge/Compliance-AIAct%20%2B%20ISO42001-yellow.svg)]()

Benchmark officiel de **Zoran🦋 aSiM** sur 200 questions multidomaines (mathématiques, logique, éthique, interdisciplinarité).

## 📊 Résultats clés
- Exactitude : 0,61 → 0,93 (+52%)
- Complétude : 0,39 → 0,87 (+123%)
- Clarté : 0,49 → 0,86 (+75%)
- Hallucinations : 42% → 0% (-42%)
- Refus éthiques : +200% qualité (argumentés)

## 📂 Corpus inclus
- `benchmark_results.json` → résultats complets (200 Q × 2 runs)
- `metriques.csv` → consolidation statistique
- `hallucination_delta.png` → comparaison hallucinations baseline vs Zoran
- `benchmark_radar.png` → radar multidomaine
- `ethique_refus.png` → qualité des refus éthiques
- `barre_de_repere.png` → indicateurs globaux
- `Zoran_WhitePaper_Benchmark_Cover.pdf` → livre blanc académique (PDF)
- `SHA256SUMS.txt` → empreintes de vérification
- `sbom.cyclonedx.json` → SBOM complet
- `provenance_c2pa.json` → provenance C2PA signée
- `Makefile` → pipeline `make reproduce_all`

## 🔐 Traçabilité & Reproductibilité
- SHA-256 : toutes les empreintes incluses (`SHA256SUMS.txt`)
- SBOM CycloneDX : transparence de la chaîne logicielle
- C2PA : manifeste de provenance numérique
- Seeds fixes : [13, 42, 101]

## 📖 Citation académique
Frédéric Tabary (2025). *Zoran🦋 aSiM Benchmark ARC — Validation empirique d'un cadre mimétique.*  
Zenodo. DOI : [10.5281/zenodo.17209747](https://doi.org/10.5281/zenodo.17209747)

---
