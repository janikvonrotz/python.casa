seq = "ACTNGTGCTYGATRGTAGC"
dna_count = seq.count("A") + seq.count("T") + seq.count("G") + seq.count("C")
dna_fraction = (dna_count / len(seq)) * 100

print(f'{dna_fraction:.4} %')