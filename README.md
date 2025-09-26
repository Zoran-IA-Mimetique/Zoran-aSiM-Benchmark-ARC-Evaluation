# 🦋 Zoran aSiM Benchmark ARC — Évaluation officielle

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17209747.svg)](https://doi.org/10.5281/zenodo.17209747)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Reproducibility](https://img.shields.io/badge/Reproducibility-100%25-blue)](./SHA256SUMS.txt)
[![Compliance](https://img.shields.io/badge/Compliance-AIAct%20%2F%20ISO42001-yellow)](./ethics_review.md)

Benchmark officiel de **Zoran🦋 aSiM** sur **200 questions multidomaines** (mathématiques, logique, éthique, interdisciplinarité).

---

## 📊 Résultats clés
- Exactitude : 0,61 → 0,93 (**+52%**)
- Complétude : 0,39 → 0,87 (**+123%**)
- Clarté : 0,49 → 0,86 (**+75%**)
- Hallucinations : 42% → 0% (**-42%**)
- Refus éthiques : +200% qualité (argumentés)

---

## 📂 Corpus inclus
- `benchmark_results.json` → résultats complets par question (200 × 2 runs)
- `metrics.csv` → consolidation statistique
- `hallucination_delta.png` → hallucinations baseline vs Zoran
- `benchmark_radar.png` → comparaison multidomaine
- `ethique_refus.png` → qualité des refus éthiques
- `barre_de_repere.png` → indicateurs globaux
- `Zoran_WhitePaper_Benchmark_Cover.pdf` → livre blanc académique (PDF)
- `SHA256SUMS.txt` → empreintes de vérification
- `sbom.cyclonedx.json` → SBOM complet
- `provenance_c2pa.json` → provenance C2PA signée
- `Makefile` → pipeline `make reproduce_all` pour vérification

---

## 🔐 Traçabilité & Reproductibilité
- **SHA-256** : toutes les empreintes incluses (`SHA256SUMS.txt`)
- **SBOM CycloneDX** : transparence de la chaîne logicielle
- **C2PA** : manifeste de provenance numérique
- **Makefile** : pipeline complet (`make reproduce_all`)

---

## 📖 Méthodologie
- Nombre total de questions : **200** (400 réponses baseline + Zoran)
- Domaines couverts :
  - Mathématiques avancées (analyse, topologie, algèbre, catégories, logique formelle)
  - Interdisciplinarité (climat, neurosciences, linguistique, droit, anthropologie)
  - Éthique & sécurité (cybersécurité, IA générative, armes autonomes, fraude académique)
- Protocole :
  - Mode baseline (modèle nu)
  - Mode Zoran (mimétique + garde-fous éthiques + structuration pédagogique)
- Métriques suivies : exactitude, complétude, clarté, hallucinations, biais, refus éthiques

---

## 📚 Références et DOI
- 10.5281/zenodo.17209747 — Benchmark Zoran🦋 aSiM ARC (présent dépôt)
- 10.5281/zenodo.17144934 — ZORAN_openbench v1.0 (premières questions AGI)
- 10.5281/zenodo.17148634 — ZORAN_openbench v2.0 (évaluation systémique)
- 10.5281/zenodo.16940525 — Livres blancs V1 (fondateurs)
- 10.5281/zenodo.16941007 — Mémoire par Absence Active
- 10.5281/zenodo.16995014 — Couche d'égide — Gouvernance vivante
- 10.5281/zenodo.16995226 — LinguaSynthèse (IA↔IA)
- 10.5281/zenodo.16997156 — Études Jumeaux v2 + EthicChain

(voir `references.bib` pour la liste complète des 30+ DOI)

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
```

---

## 📧 Contact
**Frédéric Tabary — INSTITUT🦋 IA INC.**  
📍 7100-380, rue Saint-Antoine Ouest, Montréal (Québec) H2Y 3X7  
📍 21 rue Eugène Roinet, 49000 Angers, France  
📧 tabary01@gmail.com  

---

## ⚖️ Licence
- Code et données → MIT  
- Documentation et images → CC-BY 4.0  
