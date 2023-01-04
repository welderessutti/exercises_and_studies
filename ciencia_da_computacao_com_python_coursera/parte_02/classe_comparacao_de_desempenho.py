import random
import time


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


class ContaTempos:

    def lista_aletoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara(self, n):
        lista1 = self.lista_aletoria(n)
        lista2 = lista1[:]
        lista3 = lista1[:]
        lista4 = self.lista_quase_ordenada(n)
        lista5 = lista4[:]
        lista6 = lista4[:]

        o = Ordenador()

        print("Comparando com listas aleatórias:")
        antes = time.time()
        o.bubble_sort(lista1)
        depois = time.time()
        print(f"Bubble Sort demorou {depois - antes}")

        antes = time.time()
        o.short_bubble_sort(lista2)
        depois = time.time()
        print(f"Short Bubble Sort demorou {depois - antes}")

        antes = time.time()
        o.selecao_direta(lista3)
        depois = time.time()
        print(f"Seleção Direta demorou {depois - antes}")

        print("\nComparando com listas quase ordenadas:")
        antes = time.time()
        o.bubble_sort(lista4)
        depois = time.time()
        print(f"Bubble Sort demorou {depois - antes}")

        antes = time.time()
        o.short_bubble_sort(lista5)
        depois = time.time()
        print(f"Short Bubble Sort demorou {depois - antes}")

        antes = time.time()
        o.selecao_direta(lista6)
        depois = time.time()
        print(f"Seleção Direta demorou {depois - antes}")


c = ContaTempos()

c.compara(5000)
