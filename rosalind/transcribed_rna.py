file = open(r'dataset/rosalind_rna.txt')

dna = file.read().upper()

rna = dna.replace('T', 'U')

print(rna)
