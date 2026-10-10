from Bio import SeqIO
import matplotlib.pyplot as plt

# compter les bases pour Wuhan
for record in SeqIO.parse("data/genomes/wuhan.fasta", "fasta"):
    nbre_A_w = record.seq.count("A")
    nbre_T_w = record.seq.count("T")
    nbre_G_w = record.seq.count("G")
    nbre_C_w = record.seq.count("C")
    longueur_w = len(record.seq)

# compter les bases pour Omicron
for record in SeqIO.parse("data/genomes/omicron.fasta", "fasta"):
    nbre_A_o = record.seq.count("A")
    nbre_T_o = record.seq.count("T")
    nbre_G_o = record.seq.count("G")
    nbre_C_o = record.seq.count("C")
    longueur_o = len(record.seq)

# graphique 1 : composition Wuhan
bases = ["A", "T", "G", "C"]
valeurs_w = [nbre_A_w, nbre_T_w, nbre_G_w, nbre_C_w]

plt.bar(bases, valeurs_w, color=["blue", "red", "green", "orange"])
plt.title("Composition nucleotidique Wuhan-Hu-1")
plt.xlabel("base")
plt.ylabel("nombre")
plt.savefig("results/plots/01_composition_wuhan.png")
plt.close()
print("graphique 1 sauvegarde")

# graphique 2 : composition Omicron
valeurs_o = [nbre_A_o, nbre_T_o, nbre_G_o, nbre_C_o]

plt.bar(bases, valeurs_o, color=["blue", "red", "green", "orange"])
plt.title("Composition nucleotidique Omicron BA.1")
plt.xlabel("base")
plt.ylabel("nombre")
plt.savefig("results/plots/02_composition_omicron.png")
plt.close()
print("graphique 2 sauvegarde")

# graphique 3 : taille des deux genomes
noms = ["Wuhan-Hu-1", "Omicron BA.1"]
tailles = [longueur_w, longueur_o]

plt.bar(noms, tailles, color=["steelblue", "tomato"])
plt.title("Taille des genomes SARS-CoV-2")
plt.ylabel("longueur (bp)")
plt.savefig("results/plots/03_taille_genomes.png")
plt.close()
print("graphique 3 sauvegarde")