f = open("dataset/dna2.fasta")

seqs = dict()

for line in f:
    line = line.rstrip()
    if line[0] == ">":
        words = line.split()
        name = words[0][1:]
        seqs[name] = ""
    else:
        seqs[name] = seqs[name] + line

'''print(seqs)'''

cont = 0
for k in seqs.keys():
    cont += 1
print(f"There are {cont} records in the FASTA file.")

longest = 0
for v in seqs.values():
    if len(v) > longest:
        longest = len(v)
print(f"The longest sequence in the file has {longest} nucleotides.")

cont = 0
shortest = 0
for v in seqs.values():
    if cont == 0 or len(v) < shortest:
        shortest = len(v)
        cont += 1
print(f"The shortest sequence in the file has {shortest} nucleotides.")

