alunos = list()

for a in range(0, 3):
    alunos.append(dict())
    alunos[a]["Nome"] = input("Nome Aluno: ").title().strip()
    alunos[a]["Turma"] = input("Turma: ").strip()
    alunos[a]["Sala"] = int(input("Sala: ").strip())
    alunos[a]["Notas"] = list()
    for b in range(0, 4):
        alunos[a]["Notas"].append(input(f"Nota {b + 1}: ").strip())

for c in range(0, 2):
    for d in range(c + 1, 3):
        if alunos[c]["Nome"] > alunos[d]["Nome"]:
            x = alunos[c]
            alunos[c] = alunos[d]
            alunos[d] = x

for e in alunos:
    print(f"O aluno {e['Nome']} da turma {e['Turma']}, sala {e['Sala']} obteve as notas: ", end="")
    for f in e["Notas"]:
        print(f"{f}", end=", ")
    print()

print(alunos)
