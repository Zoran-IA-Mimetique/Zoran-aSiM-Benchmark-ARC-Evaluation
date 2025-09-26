# Protocole expérimental — Zoran🦋 aSiM Benchmark ARC

## Définition des métriques
- **Exactitude** : proportion de réponses exactes sur les 200 questions (mesure standard EM/F1).
- **Complétude** : taux de couverture des concepts attendus dans la réponse (mesuré via annotation + scoring).
- **Clarté** : lisibilité et structuration (score sur 5 par annotateurs).
- **Hallucination (HR)** : détection de contenu factuellement incorrect ou inventé (manuel + automatique).
- **Biais (BI)** : présence de stéréotypes implicites ou explicites.
- **Refus éthiques** : détection et qualité des refus sur questions sensibles.

## Baselines
- **Copilot** (Microsoft)
- **AI-Studio** (baseline académique interne)
- **DeepSeek**
- **ChatGPT-5 Pro (OpenAI)**

## Corpus
- 200 questions ARC : Mathématiques avancées, logique, interdisciplinarité, éthique.
- Format JSONL standardisé.

## Exécution
- Python 3.11
- Dépendances : pandas, matplotlib
- Hardware : CPU standard (AMD Ryzen 7 / équivalent), 32 GB RAM
- Seeds fixes : 13, 42, 101

## Reproductibilité
Pipeline automatisé :

```bash
make reproduce_all
```
