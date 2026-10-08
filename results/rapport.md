# Analyse comparative des variants SARS-CoV-2
## Wuhan-Hu-1 vs Omicron BA.1

Auteur : Ouzar Mohamed Anis
Date : 5 Septembre 2026
Outils : Python, BioPython, MAFFT, Matplotlib

---

## 1. Introduction

Le SARS-CoV-2 est le virus responsable de la pandémie de COVID-19.
Depuis la souche originale Wuhan-Hu-1 en 2019, le virus a évolué
en plusieurs variants. Omicron BA.1 est apparu fin 2021 et est
connu pour avoir beaucoup de mutations dans le gène Spike.

L'objectif de ce projet est de comparer les deux génomes et
d'identifier les mutations du gène Spike avec des outils
bioinformatiques.

---

## 2. Données utilisées

| Genome | ID NCBI | Longueur |
|--------|---------|----------|
| Wuhan-Hu-1 | NC_045512.2 | 29 903 bp |
| Omicron BA.1 | OX315743.1 | 29 767 bp |

Les séquences ont été téléchargées depuis NCBI.

---

## 3. Ce que j'ai fait

### Etape 1 : statistiques des génomes
J'ai écrit un script Python pour calculer la longueur,
la composition en bases (A, T, G, C) et le GC% de chaque génome.

### Etape 2 : extraction du gène Spike
J'ai extrait le gène Spike des deux génomes en utilisant
ses coordonnées dans le génome de référence (positions 21562-25384).

### Etape 3 : alignement
J'ai aligné les deux séquences Spike avec MAFFT depuis
le terminal pour pouvoir les comparer correctement.

### Etape 4 : analyse des mutations
J'ai écrit un script Python qui compare les deux séquences
alignées position par position pour identifier les mutations.

---

## 4. Résultats

### Statistiques des génomes

| | Wuhan-Hu-1 | Omicron BA.1 |
|--|------------|--------------|
| Longueur | 29 903 bp | 29 767 bp |
| GC% | 37.97% | 37.97% |

Omicron est plus court de 136 bp que Wuhan.
Le GC% est identique dans les deux variants.

### Mutations du gène Spike

| Type | Nombre |
|------|--------|
| Substitutions | 31 |
| Délétions | 46 |
| Insertions | 46 |
| Total | 123 |

---

## 5. Graphiques

- `plots/01_composition_wuhan.png`
- `plots/02_composition_omicron.png`
- `plots/03_taille_genomes.png`
- `plots/04_mutations_spike.png`

---

## 6. Conclusion

Ce projet m'a permis de mettre en pratique ce que j'ai appris
pendant mes 7 semaines de formation en bioinformatique.

J'ai utilisé Python avec BioPython pour manipuler des séquences
biologiques, MAFFT pour aligner deux séquences, et Matplotlib
pour visualiser les résultats.

Les résultats montrent que le variant Omicron BA.1 a 123 mutations
dans le gène Spike par rapport à la souche Wuhan originale, ce qui
explique pourquoi ce variant est si différent immunologiquement.