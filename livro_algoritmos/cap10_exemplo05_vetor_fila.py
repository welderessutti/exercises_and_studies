fila = list()
inicio = 0
fim = 3


def criar():
    global fila, inicio
    fila.clear()
    inicio = 0
    print("Fila criada com sucesso.")
    menu()


def entrar():
    global fila
    add = int(input("Adicionar: "))
    if adicionar(add):
        print(f"Elemento {add} adicionado com sucesso.")
    else:
        print(f"Lista cheia. Impossível adicionar elemento {add}")
        print(fila)
    menu()


def adicionar(add):
    global fila, inicio
    if cheia():
        return False
    else:
        fila.insert(inicio, add)
        inicio += 1
        return True


def saida():
    global fila
    if retirar():
        print("Elemento removido da primeira posição.")
    else:
        print("Lista vazia. Impossível remover elemento.")
        print(fila)
    menu()


def retirar():
    global fila, inicio
    if vazia():
        return False
    else:
        del fila[0]
        inicio -= 1
        return True


def visualizar_primeiro():
    global fila
    if vazia():
        print("Impossível, fila vazia!")
        print(fila)
    else:
        print(f"O primeiro elemento é {fila[0]}.")
    menu()


def visualizar_tudo():
    global fila
    if vazia():
        print("Impossível, fila vazia!")
        print(fila)
    else:
        print("O(s) elemento(s) da fila são: ", end="")
        for a in fila:
            if a is not fila[-1]:
                print(a, end=", ")
            else:
                print(f"{a}.")
    menu()


def sair():
    print("Programa encerrado.")


def menu():
    while True:
        opcao = int(input("1 - ENTRAR NA FILA\n"
                          "2 - REMOVER PRIMEIRO DA FILA\n"
                          "3 - PRIMEIRO ELEMENTO DA FILA\n"
                          "4 - VISUALIZAR FILA\n"
                          "5 - CRIA FILA\n"
                          "6 - SAIR\n"
                          "Escolha uma opção: "))
        if 1 <= opcao <= 6:
            break
        else:
            print("\nOpção inválida!\n")
    if opcao == 1:
        entrar()
    elif opcao == 2:
        saida()
    elif opcao == 3:
        visualizar_primeiro()
    elif opcao == 4:
        visualizar_tudo()
    elif opcao == 5:
        criar()
    elif opcao == 6:
        sair()


def cheia():
    global inicio, fim
    if inicio == fim:
        return True
    else:
        return False


def vazia():
    global inicio
    if inicio == 0:
        return True
    else:
        return False


menu()
print(fila)
