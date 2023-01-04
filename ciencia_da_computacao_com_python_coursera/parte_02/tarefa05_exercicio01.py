def busca(lista, elemento):
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        meio = (inicio + final) // 2
        print(meio)
        if elemento == lista[meio]:
            return meio
        else:
            if elemento > lista[meio]:
                inicio = meio + 1
            else:
                final = meio - 1
    return False
