def main():
    menu()


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
    a = float(input("\nDigite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    res = a + b
    print(f"{a} + {b} = {res}\n")
    menu()


def subtracao():
    a = float(input("\nDigite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    res = a - b
    print(f"{a} - {b} = {res}\n")
    menu()


def multiplicacao():
    a = float(input("\nDigite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    res = a * b
    print(f"{a} * {b} = {res}\n")
    menu()


def divisao():
    a = float(input("\nDigite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    res = a / b
    print(f"{a} / {b} = {res}\n")
    menu()


def fim():
    print("\nFim do programa.")
