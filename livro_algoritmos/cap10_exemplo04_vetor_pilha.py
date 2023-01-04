pilha = list()
limite = 3
topo = 0


def criar():
    global pilha, topo
    pilha.clear()
    topo = 0
    print("Pilha criada com sucesso.")
    menu()


def empilhar():
    add = int(input("Adicionar: "))
    if adicionar(add):
        print(f"Elemento {add} adicionado na pilha com sucesso.")
    else:
        print(f"Pilha cheia. Impossível adicionar o elemento {add}.")
    menu()


def adicionar(n):
    global topo
    if cheia():
        return False
    else:
        pilha.insert(topo, n)
        topo += 1
        return True


def desempilhar():
    global pilha
    if retirar():
        print(f"Elemento retirado do topo da pilha com sucesso.")
    else:
        print("Pilha vazia. Impossível remover elementos.")
    menu()


def retirar():
    global topo
    if vazia():
        return False
    else:
        del pilha[topo - 1]
        topo -= 1
        return True


def mostrar():
    if vazia():
        print("Impossível visualizar, pilha está vazia!")
        print(pilha)
    else:
        print(pilha)
    menu()


def sair():
    print("Fim do programa.")


def menu():
    while True:
        opcao = int(input("1 - EMPILHAR\n"
                          "2 - DESEMPILHAR\n"
                          "3 - MOSTRAR PILHA\n"
                          "4 - CRIAR PILHA\n"
                          "5 - SAIR\n"
                          "Escolha uma opção: "))
        if 1 <= opcao <= 5:
            break
        else:
            print("\nOpção inválida!\n")
    if opcao == 1:
        empilhar()
    elif opcao == 2:
        desempilhar()
    elif opcao == 3:
        mostrar()
    elif opcao == 4:
        criar()
    elif opcao == 5:
        sair()


def cheia():
    global topo, limite
    if topo == limite:
        return True
    else:
        return False


def vazia():
    global topo
    if topo == 0:
        return True
    else:
        return False


menu()
print(pilha)
