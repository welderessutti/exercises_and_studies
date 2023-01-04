file = open(r'dataset/rosalind_dna.txt')

codigo_dna = file.read().upper()

print(codigo_dna)

print(codigo_dna.count('A'), codigo_dna.count('T'), codigo_dna.count('C'), codigo_dna.count('G'))
