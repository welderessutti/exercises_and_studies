# AQUI AS FUNÇÕES ESTÃO BUSCANDO A LISTA COMO VARIÁVEL GLOBAL, CONFORME ENUNCIADO:
fim = 3
tabela = list()


def entrada():
    for c in range(0, fim):
        tabela.append(input("Nome: "))
    processamento()


def processamento():
    ordenacao(tabela)
    saida(tabela)


def ordenacao(lista):
    for a in range(0, len(lista) - 1):
        for b in range(1, len(lista)):
            if lista[a] > lista[b]:
                lista[a], lista[b] = troca(lista[a], lista[b])


def troca(a, b):
    x = a
    a = b
    b = x
    return a, b


def saida(lista):
    for a in lista:
        print(a)


entrada()
print(tabela)
