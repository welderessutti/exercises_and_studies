file = open(r'dataset/rosalind_revc.txt')

dna = file.read().upper()
dna_complement = ''

for nucleotide in dna:
    if nucleotide == 'A':
        dna_complement = dna_complement + 'T'
    elif nucleotide == 'T':
        dna_complement = dna_complement + 'A'
    elif nucleotide == 'C':
        dna_complement = dna_complement + 'G'
    elif nucleotide == 'G':
        dna_complement = dna_complement + 'C'

print(dna_complement[::-1])
