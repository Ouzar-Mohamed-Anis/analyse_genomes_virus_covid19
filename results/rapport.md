# Analyse comparative des variants SARS-CoV-2
## Wuhan-Hu-1 vs Omicron BA.1

Auteur : Ouzar Mohamed Anis
Date : 5 Septembre 2026
Outils : Python, BioPython, BLAST, MAFFT, Matplotlib

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

|   Génome     |                         ID NCBI                                 | Longueur  |
|--------------|-----------------------------------------------------------------|-----------|
| Wuhan-Hu-1   | [NC_045512.2](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2) | 29 903 bp |
| Omicron BA.1 | [OX315743.1](https://www.ncbi.nlm.nih.gov/nuccore/OX315743.1)   | 29 767 bp |


---

## 3. Méthodologie

### Étape 1 : statistiques des génomes
J'ai écrit un script Python pour calculer la longueur,
la composition en bases (A, T, G, C) et le GC% de chaque génome.

### Étape 2 : extraction du gène Spike
J'ai extrait le Spike de Wuhan avec les coordonnées officielles
(21562-25384). Pour Omicron BA.1, j'ai utilisé BLAST afin de
repérer la région correspondant au gène Spike dans le génome
de référence étudié, puis d'en extraire la séquence pour
l'analyse comparative (21534-25347).

### Étape 3 : alignement
J'ai aligné les deux séquences Spike avec MAFFT depuis
le terminal pour pouvoir les comparer correctement.

### Étape 4 : analyse des mutations
J'ai écrit un script Python qui compare les deux séquences
alignées position par position pour identifier les différences.

---

## 4. Résultats

### Statistiques des génomes

|          | Wuhan-Hu-1 | Omicron BA.1 |
|----------|------------|--------------|
| Longueur | 29 903 bp  | 29 767 bp    |
| GC%      | 37,97%     | 37,97%       |

Omicron est plus court de 136 bp que Wuhan.
Le GC% est identique dans les deux variants.

### Différences dans le gène Spike

| Type de différence | Nombre de positions |
|--------------------|---------------------|
| Substitutions      | 31                  |
| Délétions          | 18                  |
| Insertions         | 9                   |
| Total              | 58                  |

Les différences sont comptées position par position dans
l'alignement des deux séquences. Les nombres de délétions
et d'insertions correspondent à des positions dans l'alignement,
et non nécessairement à des événements mutationnels distincts.

---

## 5. Graphiques

- plots/01_composition_wuhan.png
- plots/02_composition_omicron.png
- plots/03_taille_genomes.png
- plots/04_mutations_spike.png

---

## 6. Reproductibilité

Les commandes suivantes permettent de relancer l'analyse complète :

```bash
python3 scripts/genome_stats.py
python3 scripts/graphiques.py
python3 scripts/spike.py
cat data/spike/wuhan_spike.fasta data/spike/omicron_spike.fasta > data/spike/les_deux_spike.fasta
mafft --auto data/spike/les_deux_spike.fasta > data/spike/spike_aligne.fasta
python3 scripts/mutations.py
```


---


## 7. Conclusion

Ce projet m'a permis de mettre en pratique les connaissances
acquises pendant mes sept semaines de formation en bioinformatique.

J'ai utilisé Python et Biopython pour manipuler des séquences
biologiques, BLAST pour rechercher les coordonnées de la région
Spike d'Omicron BA.1, MAFFT pour aligner les séquences et
Matplotlib pour visualiser les résultats.

La comparaison des séquences alignées a permis d'identifier
58 différences comptées position par position, réparties entre
substitutions, délétions et insertions. Ce travail m'a permis
de découvrir les principales étapes d'une analyse comparative
de séquences virales et de développer mes compétences pratiques
en bioinformatique.


