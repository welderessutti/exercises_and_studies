def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    :param i: Início da contagem.
    :param f: Fim da contagem.
    :param p: Passo da contagem.
    :return: Sem retorno.
    """
    c = i
    while c <= f:
        print(f"{c}", end=" ")
        c += p
    print("FIM!")


print(contador.__doc__)
help(contador)


def somar(a_1=0, b=0, c=0):  # Difere do desempacotamento "*num".
    s = a_1 + b + c
    print(s)


somar(10, 8)


def teste(b):
    global a
    a = 8  # Escopo local.
    b += 4
    c = 2
    print(f"\nA dentro vale {a}.")
    print(f"B dentro vale {b}.")
    print(f"C dentro vale {c}.")


a = 5  # Escopo global.
teste(a)
print(f"A fora vale {a}.")
# print(f"B fora vale {b}.")  Dá erro pois a variável "b" está fora do escopo global.
# print(f"C fora vale {c}.")  Dá erro pois a variável "c" está fora do escopo global.


def somar_1(x=0, y=0, z=0):
    soma = x + y + z
    return soma


print(f"\nA soma vale {somar_1(5, 4, 1)}.")
r1 = somar_1(7, 14, 9)
r2 = somar_1(8, 10)
r3 = somar_1(9)
print(f"Meus cálculos deram {r1}, {r2} e {r3}.")


def fatorial(num=1):
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
    return fat


n = int(input("\nDigite um número: "))
print(f"O fatorial de {n} é {fatorial(n)}.")


def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input("\nDigite um número: "))
print(par(n))
if par(n):
    print("É par!")
else:
    print("Não é par!")
