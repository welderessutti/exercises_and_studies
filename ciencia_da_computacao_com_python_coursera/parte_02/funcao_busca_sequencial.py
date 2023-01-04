def busca_sequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return True
    return False


abc = list(range(0, 61))

x = int(input("Buscar qual valor?: "))

print(busca_sequencial(abc, x))
