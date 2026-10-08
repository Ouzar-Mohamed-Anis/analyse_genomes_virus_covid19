from Bio import SeqIO
import matplotlib.pyplot as plt

# charger les genomes
wuhan = next(SeqIO.parse("data/genomes/wuhan.fasta", "fasta"))
omicron = next(SeqIO.parse("data/genomes/omicron.fasta", "fasta"))

wuhan_seq = str(wuhan.seq).upper()
omicron_seq = str(omicron.seq).upper()

# compter les bases
bases = ["A", "T", "G", "C"]

wuhan_counts = []
wuhan_counts.append(wuhan_seq.count("A"))
wuhan_counts.append(wuhan_seq.count("T"))
wuhan_counts.append(wuhan_seq.count("G"))
wuhan_counts.append(wuhan_seq.count("C"))

omicron_counts = []
omicron_counts.append(omicron_seq.count("A"))
omicron_counts.append(omicron_seq.count("T"))
omicron_counts.append(omicron_seq.count("G"))
omicron_counts.append(omicron_seq.count("C"))

# graphique 1 : composition wuhan
plt.bar(bases, wuhan_counts, color=["blue", "red", "green", "orange"])
plt.title("Composition nucleotidique Wuhan-Hu-1")
plt.xlabel("base")
plt.ylabel("nombre")
plt.savefig("results/plots/01_composition_wuhan.png")
plt.close()
print("graphique 1 sauvegarde")

# graphique 2 : composition omicron
plt.bar(bases, omicron_counts, color=["blue", "red", "green", "orange"])
plt.title("Composition nucleotidique Omicron BA.1")
plt.xlabel("base")
plt.ylabel("nombre")
plt.savefig("results/plots/02_composition_omicron.png")
plt.close()
print("graphique 2 sauvegarde")

# graphique 3 : taille des deux genomes
noms = ["Wuhan-Hu-1", "Omicron BA.1"]
tailles = [len(wuhan_seq), len(omicron_seq)]

plt.bar(noms, tailles, color=["steelblue", "tomato"])
plt.title("Taille des genomes SARS-CoV-2")
plt.ylabel("longueur (bp)")
plt.savefig("results/plots/03_taille_genomes.png")
plt.close()
print("graphique 3 sauvegarde")


print("tous les graphiques sont dans results/plots/")