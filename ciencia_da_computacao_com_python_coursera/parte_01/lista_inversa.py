lista = []

while True:
    a = int(input("Digite um número: "))
    if a % 10 == 0 and a != 0:
        lista.append(a)
    elif a == 0:
        break

print(lista)

cont = 0
cont_1 = -1
for a in range(len(lista) // 2):  # ALTERA INVERSAMENTE AS POSIÇÕES DA LISTA CONFORME DIGITADO.
    x = lista[cont]
    lista[cont] = lista[cont_1]
    lista[cont_1] = x
    cont += 1
    cont_1 -= 1

print(lista)

flores = ["margarida", "rosa", "tulipa", "cravo"]

tam = len(flores) - 1

while tam >= 0:
    print(flores[tam], end=", ")  # APENAS IMPRIME A LISTA EM ORDEM INVERSA.
    tam -= 1

# OU

print(flores[-1::-1])
