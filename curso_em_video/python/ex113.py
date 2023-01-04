def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: Por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: Por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


num = leia_int("Digite um inteiro: ")
num_2 = leia_float("Digite um real: ")

print(f"O valor inteiro digitado foi {num} e o real foi {num_2}.")
