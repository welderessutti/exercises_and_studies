class Ordenador:

    def selecao_direta(self, lista):
        fim = len(lista)
        for i in range(fim - 1):
            posicao_do_minimo = i
            for j in range(i + 1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
        return lista

    def bubble_sort(self, lista):
        fim = len(lista)
        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    def short_bubble_sort(self, lista):
        fim = len(lista)
        for i in range(fim - 1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocou = True
            if not trocou:
                return lista
        return lista


abc = [1, 25, 63, 4, 0, 88, 114, 153, 77, 11, 22, 95, 91, 12]

o = Ordenador()
print(abc)
o.selecao_direta(abc)
print(abc)

abc = [1, 25, 63, 4, 0, 88, 114, 153, 77, 11, 22, 95, 91, 12]

print(abc)
o.bubble_sort(abc)
print(abc)
