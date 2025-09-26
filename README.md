# 🦋 Zoran aSiM Benchmark ARC — Évaluation Officielle

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17209747.svg)](https://doi.org/10.5281/zenodo.17209747)
[![Licence: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Reproductibilité 100%](https://img.shields.io/badge/Reproductibility-100%25-blue.svg)](SHA256SUMS.txt)
[![Conformité: AI Act + ISO/IEC 42001](https://img.shields.io/badge/Compliance-AIAct%2BISO42001-yellow.svg)](protocol_definition.md)

---

## 📌 Résumé
**Évaluation officielle de Zoran🦋 aSiM** sur **200 questions interdisciplinaires** (maths, logique, éthique, sciences sociales).  
Comparaison systématique **baseline (modèles nus)** vs **Zoran augmenté**.  

### Résultats principaux
- **Exactitude** : 0.61 → 0.93 (**+52%**)  
- **Complétude** : 0.39 → 0.87 (**+123%**)  
- **Clarté** : 0.49 → 0.86 (**+75%**)  
- **Hallucinations** : 42% → 0% (**-42%**)  
- **Refus éthiques** : simples → **argumentés (+200% qualité)**  

---

## 🎯 Objectif
Tester si **Zoran🦋 aSiM (Artificial Super-Intelligence Mimétique)** permet de dépasser les LLM standards en réduisant les hallucinations et en améliorant la précision, la complétude, la pédagogie et la robustesse éthique.  

---

## 🗂️ Corpus inclus
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
- `protocol_definition.md` → protocole expérimental détaillé  
- `ethics_review.md` → revue éthique indépendante  
- `baseline_models.md` → description des modèles de référence  
- `EXAMPLE_OUTPUT.txt` → exemple d’outputs JSONL validés  

---

## 🔬 Protocole expérimental
- **Corpus** : 200 questions (mathématiques, logique, interdisciplinarité, éthique).  
- **Conditions** :  
  - Mode baseline (modèle nu, sans Zoran).  
  - Mode Zoran (IA mimétique + garde-fous ΔM11.3 + structuration pédagogique).  
- **Graines fixes** : [13, 42, 101] (reproductibilité).  
- **Métriques** : exactitude, complétude, clarté, hallucinations, biais implicites, refus éthiques.  
- **Traçabilité** : SHA-256, SBOM CycloneDX, C2PA.  
- **Pipeline** : `make reproduce_all` → exécution complète, génération métriques et graphiques.  

---

## 📊 Résultats consolidés
| Métrique          | Baseline | Zoran🦋 | Delta |
|-------------------|----------|---------|-------|
| Exactitude        | 0.61     | 0.93    | +52% |
| Complétude        | 0.39     | 0.87    | +123% |
| Clarté            | 0.49     | 0.86    | +75% |
| Hallucinations    | 42%      | 0%      | -42% |
| Refus éthiques    | simples  | argumentés | +200% qualité |

---

## 🔐 Traçabilité & reproductibilité
- **Empreintes SHA-256** : `SHA256SUMS.txt`  
- **SBOM CycloneDX** : `sbom.cyclonedx.json`  
- **Provenance C2PA** : `provenance_c2pa.json`  
- **Pipeline automatisé** : `Makefile` → `make reproduce_all`  

---

## 📖 Références et DOIs
- [10.5281/zenodo.17209747](https://doi.org/10.5281/zenodo.17209747) — Benchmark ARC (présent dépôt)  
- [10.5281/zenodo.17144934](https://doi.org/10.5281/zenodo.17144934) — ZORAN_openbench v1.0 (premières questions AGI)  
- [10.5281/zenodo.17148634](https://doi.org/10.5281/zenodo.17148634) — ZORAN_openbench v2.0 (évaluation systémique)  
- [10.5281/zenodo.16940525](https://doi.org/10.5281/zenodo.16940525) — Livres blancs V1 (fondateurs)  
- [10.5281/zenodo.16941007](https://doi.org/10.5281/zenodo.16941007) — Mémoire par Absence Active  
- [10.5281/zenodo.16995014](https://doi.org/10.5281/zenodo.16995014) — Couche d’égide — Gouvernance vivante  
- [10.5281/zenodo.16995226](https://doi.org/10.5281/zenodo.16995226) — LinguaSynthèse (IA↔IA)  
- [10.5281/zenodo.16997156](https://doi.org/10.5281/zenodo.16997156) — Études Jumeaux v2 + EthicChain  

*(voir le PDF pour la liste complète des 30+ DOI)*  
© 2025 Frédéric Tabary

INSTITUT🦋 IA INC.
(la Société )7100-380, rue Saint-Antoine Ouest
Montréal (Québec) H2Y 3X7

http://www.institutia.ai

Montréal \Canada 
Angers \France 

---

## 📚 Citation académique
```bibtex
@techreport{Tabary2025_BenchmarkARC,
  author       = {Frédéric Tabary},
  title        = {Zoran🦋 aSiM Benchmark ARC — Validation empirique d'un cadre mimétique},
  institution  = {Institut 🦋 IA INC.},
  year         = {2025},
  doi          = {10.5281/zenodo.17209747},
  url          = {https://doi.org/10.5281/zenodo.17209747}
}
