def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f"\033[0;31mERRO! Digite um número inteiro válido.\033[m")
        if ok:
            break
    return valor


n = leiaint("Digite um número: ")
print(f"Vcoê acabou de digitar o número {n}.")

# OUTRA FORMA QUE POSTARAM NOS COMETÁRIOS:


def leiaint(a: str):
    while True:
        valor = input(a)
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[31mERRO! Digite um número válido\033[m')


n = leiaint('Digite um valor: ')
print(f'Você acabou de digitar o número {n}')
