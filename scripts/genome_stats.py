from Bio import SeqIO

# charger les deux genomes
wuhan = next(SeqIO.parse("data/genomes/wuhan.fasta", "fasta"))
omicron = next(SeqIO.parse("data/genomes/omicron.fasta", "fasta"))

wuhan_seq = str(wuhan.seq).upper()
omicron_seq = str(omicron.seq).upper()

print("genomes charges")

# stats wuhan
longueur_w = len(wuhan_seq)
A_w = wuhan_seq.count("A")
T_w = wuhan_seq.count("T")
G_w = wuhan_seq.count("G")
C_w = wuhan_seq.count("C")
gc_w = (G_w + C_w) / longueur_w * 100


print("-- Wuhan-Hu-1 --")
print("longueur : " + str(longueur_w) + " bp")
print("A : " + str(A_w))
print("T : " + str(T_w))
print("G : " + str(G_w))
print("C : " + str(C_w))
print("GC% : " + str(round(gc_w, 2)))

# stats omicron
longueur_o = len(omicron_seq)
A_o = omicron_seq.count("A")
T_o = omicron_seq.count("T")
G_o = omicron_seq.count("G")
C_o = omicron_seq.count("C")
gc_o = (G_o + C_o) / longueur_o * 100


print("-- Omicron BA.1 --")
print("longueur : " + str(longueur_o) + " bp")
print("A : " + str(A_o))
print("T : " + str(T_o))
print("G : " + str(G_o))
print("C : " + str(C_o))
print("GC% : " + str(round(gc_o, 2)))

# comparaison

print("-- comparaison --")
diff = longueur_o - longueur_w
print("difference de taille : " + str(diff) + " bp")