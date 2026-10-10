from Bio import SeqIO

# stats du genome Wuhan
print("-- Wuhan-Hu-1 --")

for record in SeqIO.parse("data/genomes/wuhan.fasta", "fasta"):
    longueur_w = len(record.seq)
    nbre_A_w = record.seq.count("A")
    nbre_T_w = record.seq.count("T")
    nbre_G_w = record.seq.count("G")
    nbre_C_w = record.seq.count("C")
    gc_w = (nbre_G_w + nbre_C_w) / longueur_w * 100

    print("longueur :", longueur_w, "bp")
    print("A :", nbre_A_w)
    print("T :", nbre_T_w)
    print("G :", nbre_G_w)
    print("C :", nbre_C_w)
    print("GC% :", round(gc_w, 2))

# stats du genome Omicron
print("-- Omicron BA.1 --")

for record in SeqIO.parse("data/genomes/omicron.fasta", "fasta"):
    longueur_o = len(record.seq)
    nbre_A_o = record.seq.count("A")
    nbre_T_o = record.seq.count("T")
    nbre_G_o = record.seq.count("G")
    nbre_C_o = record.seq.count("C")
    gc_o = (nbre_G_o + nbre_C_o) / longueur_o * 100

    print("longueur :", longueur_o, "bp")
    print("A :", nbre_A_o)
    print("T :", nbre_T_o)
    print("G :", nbre_G_o)
    print("C :", nbre_C_o)
    print("GC% :", round(gc_w, 2))

# comparaison
print("-- comparaison --")
diff = longueur_o - longueur_w
print("difference de taille :", diff, "bp")