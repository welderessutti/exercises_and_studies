f = open('dataset/rosalind_ini5.txt', 'r')
g = open('dataset/rosalind_ini5_explanation.txt', 'w')

for x in f.readlines()[1::2]:
    g.write(x)

g.close()
