from Bio import SeqIO
import matplotlib.pyplot as plt

# charger l alignement
sequences = list(SeqIO.parse("data/spike/spike_aligne.fasta", "fasta"))

wuhan = str(sequences[0].seq).upper()
omicron = str(sequences[1].seq).upper()

print("alignement charge")

# comparer les deux sequences position par position
substitutions = []
nb_deletions = 0
nb_insertions = 0

for i in range(len(wuhan)):
    w = wuhan[i]
    o = omicron[i]

    if w == o:
        continue

    if o == "-":
        nb_deletions = nb_deletions + 1
        continue

    if w == "-":
        nb_insertions = nb_insertions + 1
        continue

    position = i + 1
    substitutions.append([position, w, o])

print("substitutions : " + str(len(substitutions)))
print("deletions : " + str(nb_deletions))
print("insertions : " + str(nb_insertions))

# afficher les substitutions
print("")
print("position | wuhan | omicron")
for s in substitutions:
    print(str(s[0]) + " | " + s[1] + " | " + s[2])

# sauvegarder dans un fichier
f = open("results/stats/mutations.txt", "w")
f.write("mutations spike wuhan vs omicron\n\n")
f.write("substitutions : " + str(len(substitutions)) + "\n")
f.write("deletions : " + str(nb_deletions) + "\n")
f.write("insertions : " + str(nb_insertions) + "\n\n")
for s in substitutions:
    ligne = str(s[0]) + " | " + s[1] + " | " + s[2] + "\n"
    f.write(ligne)
f.close()

print("")
print("mutations sauvegardees dans results/stats/mutations.txt")

# graphique
positions = []
for s in substitutions:
    positions.append(s[0])

plt.figure(figsize=(14, 4))
plt.vlines(positions, 0, 1, color="red", linewidth=1.5)
plt.title("positions des substitutions dans le gene Spike")
plt.xlabel("position (bp)")
plt.savefig("results/plots/04_mutations_spike.png")
plt.close()
print("graphique sauvegarde")