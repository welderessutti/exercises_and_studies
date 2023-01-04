nomes = list()
notas = list()
medias = list()
soma_md = 0

for a in range(0, 3):
    nomes.append(input("Aluno: "))
    notas.append([])
    soma_nt = 0
    for b in range(0, 4):
        notas[a].append(float(input(f"Nota {b + 1}: ")))
        soma_nt += notas[a][b]
    medias.append(soma_nt / 4)
    soma_md += medias[a]

media_gp = soma_md / len(nomes)

for c in range(0, 2):
    for d in range(c + 1, 3):
        if nomes[c] > nomes[d]:
            x = nomes[c]
            nomes[c] = nomes[d]
            nomes[d] = x
            y = notas[c]
            notas[c] = notas[d]
            notas[d] = y
            z = medias[c]
            medias[c] = medias[d]
            medias[d] = z

for e in range(0, 3):
    print(f"O aluno {nomes[e]} teve as notas {notas[e]} obtendo a média {medias[e]}.")
print(f"A média geral da sala foi {media_gp}.")

print(nomes)
print(notas)
print(medias)
print(soma_md)
print(media_gp)
