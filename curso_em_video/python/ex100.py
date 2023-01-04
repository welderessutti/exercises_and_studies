from random import randint
from time import sleep
numeros = list()


def sorteia(lista):
    print(f"Sorteando 5 valores da lista:", end=" ")
    for z in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[z], end=" ")
        sleep(0.3)
    print("PRONTO!")


def soma_par(lista_1):
    par = 0
    for w in lista_1:
        if w % 2 == 0:
            par += w
    print(f"Somando os valores pares de {lista_1}, temos {par}.")


sorteia(numeros)
soma_par(numeros)
