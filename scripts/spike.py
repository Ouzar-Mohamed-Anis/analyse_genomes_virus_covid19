from Bio import SeqIO

# charger et extraire le Spike de Wuhan
for record in SeqIO.parse("data/genomes/wuhan.fasta", "fasta"):
    sequence_w = record.seq
    wuhan_spike = sequence_w[21562:25384]

# charger et extraire le Spike de Omicron
for record in SeqIO.parse("data/genomes/omicron.fasta", "fasta"):
    sequence_o = record.seq
    omicron_spike = sequence_o[21534:25347]

print("spike wuhan :", len(wuhan_spike), "bp")
print("spike omicron :", len(omicron_spike), "bp")

# sauvegarder
with open("data/spike/wuhan_spike.fasta", "w") as f:
    f.write(">Wuhan_Spike\n")
    f.write(str(wuhan_spike) + "\n")

with open("data/spike/omicron_spike.fasta", "w") as f:
    f.write(">Omicron_Spike\n")
    f.write(str(omicron_spike) + "\n")

print("fichiers spike sauvegardes")