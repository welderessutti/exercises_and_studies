sobra = 10
maximo = 5

mm = maximo

'''for c in range(0, mm):
    resto = sobra - mm
    if resto % (maximo + 1) == 0:
        print(mm)
        print("multiplo")
        mm -= 1
    else:
        print(mm)
        mm -= 1'''

cont = 1
jogada = 0
while cont <= maximo:
    resto = sobra - mm
    if resto % (maximo + 1) == 0:
        jogada = mm
        break
    else:
        mm -= 1
        cont += 1

print(jogada)
