# Analyse des génomes du virus COVID-19
## Wuhan-Hu-1 vs Omicron BA.1

Auteur : Ouzar Mohamed Anis  
Date : 5 Septembre 2026

---

## Description

Ce projet compare les génomes de deux variants du SARS-CoV-2 :
la souche originale Wuhan-Hu-1 et le variant Omicron BA.1.

J'ai analysé la composition des génomes, extrait le gène Spike,
aligné les deux séquences avec MAFFT et identifié les mutations.

---

## Outils utilisés

- Python + BioPython
- BLAST
- MAFFT
- Matplotlib

---

## Comment lancer le projet

```bash
python3 scripts/genome_stats.py
python3 scripts/graphiques.py
python3 scripts/spike.py
cat data/spike/wuhan_spike.fasta data/spike/omicron_spike.fasta > data/spike/les_deux_spike.fasta
mafft --auto data/spike/les_deux_spike.fasta > data/spike/spike_aligne.fasta
python3 scripts/mutations.py
```

---

## Résultats

| | Wuhan-Hu-1 | Omicron BA.1 |
|--|------------|--------------|
| Longueur | 29 903 bp | 29 767 bp |
| GC% | 37.97% | 37.97% |

Mutations dans le gène Spike :
- Substitutions : 31
- Délétions : 18
- Insertions : 9
- Total : 58