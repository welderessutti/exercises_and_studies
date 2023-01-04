# AQUI AS FUNÇÕES ESTÃO HERDANDO A LISTA ATRAVÉS DOS PARÂMETROS:
fim_1 = 3


def entrada_1():
    tabela_1 = list()
    for c in range(0, fim_1):
        tabela_1.append(input("Nome: "))
    processamento_1(tabela_1)


def processamento_1(lista):
    ordenacao_1(lista)
    saida_1(lista)


def ordenacao_1(lista):
    for a in range(0, len(lista) - 1):
        for b in range(1, len(lista)):
            if lista[a] > lista[b]:
                lista[a], lista[b] = troca_1(lista[a], lista[b])
    return lista


def troca_1(a, b):
    x = a
    a = b
    b = x
    return a, b


def saida_1(lista):
    for a in lista:
        print(a)


entrada_1()
