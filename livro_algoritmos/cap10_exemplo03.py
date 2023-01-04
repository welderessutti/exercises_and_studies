a = 0
b = 0
r = 0


def menu():
    while True:
        opcao = int(input("1 - ADIÇÃO\n"
                          "2 - SUBTRAÇÃO\n"
                          "3 - MULTIPLICAÇÃO\n"
                          "4 - DIVISÃO\n"
                          "5 - FIM DE PROGRAMA\n"
                          "Escolha uma opção: "))
        if 1 <= opcao <= 5:
            break
        else:
            print("\nOpção inválida!\n")
    if opcao == 1:
        adicao()
    elif opcao == 2:
        subtracao()
    elif opcao == 3:
        multiplicacao()
    elif opcao == 4:
        divisao()
    elif opcao == 5:
        fim()


def adicao():
    global a, b, r
    entrada()
    r = calculo(a, b, "+")
    saida()
    menu()


def subtracao():
    global a, b, r
    entrada()
    r = calculo(a, b, "-")
    saida()
    menu()


def multiplicacao():
    global a, b, r
    entrada()
    r = calculo(a, b, "*")
    saida()
    menu()


def divisao():
    global a, b, r
    while True:
        entrada()
        if b != 0:
            break
        else:
            print("Divisor não pode ser zero. Digite novamente.")
    r = calculo(a, b, "/")
    saida()
    menu()


def entrada():
    global a, b
    a = float(input("\nDigite o primeiro número: "))
    b = float(input("Digite o segundo número: "))


def calculo(w, y, x):
    res = 0
    if x == "+":
        res = w + y
    elif x == "-":
        res = w - y
    elif x == "*":
        res = w * y
    elif x == "/":
        res = w / y
    return res


def saida():
    global r
    print(r)


def fim():
    print("\nFim do programa.")


menu()
