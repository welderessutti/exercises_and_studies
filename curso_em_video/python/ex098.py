from time import sleep


def contador(inicio, fim, passo):
    print("-=" * 20)
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    if inicio < fim:
        print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:")
        fim += 1
    if inicio > fim:
        print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:")
        passo = -passo
        fim -= 1
    for x in range(inicio, fim, passo):
        print(x, end=" ")
        sleep(0.5)
    print("FIM!")


contador(1, 10, 1)
contador(10, 0, 2)

print("-=" * 20)
print("Agora é sua vez de personalizar a contagem!")
contador(int(input("Início: ")), int(input("Fim: ")), int(input("Passo: ")))

# PROFESSOR FEZ ASSIM:


def contador_1(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print("-=" * 20)
    print(f"Contagem de {i} até {f} de {p} em {p}:")
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=" ")
            sleep(0.5)
            cont += p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(f"{cont}", end=" ")
            sleep(0.5)
            cont -= p
        print("FIM!")


contador_1(1, 10, 1)
contador_1(10, 0, 2)

print("-=" * 20)
print("Agora é sua vez de personalizar a contagem!")
contador_1(int(input("Início: ")), int(input("Fim: ")), int(input("Passo: ")))
