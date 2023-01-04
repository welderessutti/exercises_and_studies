largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

cont = 1

while cont <= altura:
    cont_1 = 1
    while cont_1 <= largura:
        if cont == 1 or cont == altura:
            print("#", end="")
            cont_1 += 1
        else:
            if cont_1 == 1 or cont_1 == largura:
                print("#", end="")
                cont_1 += 1
            else:
                print(" ", end="")
                cont_1 += 1
    cont += 1
    print()
