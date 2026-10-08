from Bio import SeqIO

# charger les genomes
wuhan = next(SeqIO.parse("data/genomes/wuhan.fasta", "fasta"))
omicron = next(SeqIO.parse("data/genomes/omicron.fasta", "fasta"))

wuhan_seq = str(wuhan.seq).upper()
omicron_seq = str(omicron.seq).upper()

# extraire le gene Spike
# coordonnees Wuhan : officielles NC_045512.2
wuhan_start = 21562
wuhan_end = 25384

# coordonnees Omicron : trouvees avec BLAST
omicron_start = 21534
omicron_end = 25347

wuhan_spike = wuhan_seq[wuhan_start:wuhan_end]
omicron_spike = omicron_seq[omicron_start:omicron_end]

print("spike wuhan : " + str(len(wuhan_spike)) + " bp")
print("spike omicron : " + str(len(omicron_spike)) + " bp")

# verifier que les deux commencent par ATG
print("debut wuhan spike : " + wuhan_spike[:6])
print("debut omicron spike : " + omicron_spike[:6])

# sauvegarder
with open("data/spike/wuhan_spike.fasta", "w") as f:
    f.write(">Wuhan_Spike\n")
    f.write(wuhan_spike + "\n")

with open("data/spike/omicron_spike.fasta", "w") as f:
    f.write(">Omicron_Spike\n")
    f.write(omicron_spike + "\n")

print("fichiers spike sauvegardes dans data/spike/")