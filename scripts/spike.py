from Bio import SeqIO

# charger les genomes
wuhan = next(SeqIO.parse("data/genomes/wuhan.fasta", "fasta"))
omicron = next(SeqIO.parse("data/genomes/omicron.fasta", "fasta"))

wuhan_seq = str(wuhan.seq).upper()
omicron_seq = str(omicron.seq).upper()

# extraire le gene Spike
# coordonnees officielles dans NC_045512.2
spike_start = 21562
spike_end = 25384

wuhan_spike = wuhan_seq[spike_start:spike_end]
omicron_spike = omicron_seq[spike_start:spike_end]

print("spike wuhan : " + str(len(wuhan_spike)) + " bp")
print("spike omicron : " + str(len(omicron_spike)) + " bp")

# sauvegarder les deux sequences spike dans des fichiers fasta
with open("data/spike/wuhan_spike.fasta", "w") as f:
    f.write(">Wuhan_Spike\n")
    f.write(wuhan_spike + "\n")

with open("data/spike/omicron_spike.fasta", "w") as f:
    f.write(">Omicron_Spike\n")
    f.write(omicron_spike + "\n")

print("fichiers spike sauvegardes dans data/spike/")