tabela = list()
cargos = dict()
cont = 0

while True:
    iniciar = input("Deseja cadastrar um cargo e salário? [S/N]: ").upper().strip()
    while iniciar not in "SN":
        iniciar = input("Opção inválida. Deseja cadastrar um cargo e salário? [S/N]: ").upper().strip()

    if iniciar == "N":
        break
    else:
        cargos["Código"] = cont
        cargos["Cargo"] = input(f"Cargo posição {cont}: ").title().strip()
        cargos["Salário"] = float(input(f"Salário cargo \"{cargos['Cargo']}\": ").strip())
        tabela.append(cargos.copy())
        cont += 1
    print()

while True:
    pesquisar = input("Deseja pesquisar um cargo? [S/N]: ").upper().strip()
    while pesquisar not in "SN":
        pesquisar = input("Opção inválida. Deseja pesquisar um cargo [S/N]: ").upper().strip()

    if pesquisar == "N":
        break
    else:
        codigo_pesquisado = int(input(f"Qual o número do cargo? ").strip())
        i = 0
        acha = False

        while i <= len(tabela) - 1 and acha is False:
            if codigo_pesquisado == tabela[i]["Código"]:
                acha = True
            else:
                i += 1

    if acha is True:
        for k in cargos.keys():
            print(f"{k:<30}", end="")
        print()
        for v in tabela[i].values():
            print(f"{v:<30}", end="")
        print()
    else:
        print("Cargo inexistente.")

    print()

print(tabela)
