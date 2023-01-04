n1 = int(input('Digite um número: '))

x1 = bool(n1 - 2 * (n1 // 2))  # PODE UTILIZAR O OPERADOR "N1 % 2" PARA OBTER O RESTO DA DIVISÃO AO INVÉS DE FAZER A EQUAÇÃO.
x2 = bool(n1 - 3 * (n1 // 3))  # PODE UTILIZAR O OPERADOR "N1 % 3" PARA OBTER O RESTO DA DIVISÃO AO INVÉS DE FAZER A EQUAÇÃO.

if (x1 and not x2) or (not x1 and x2):
    print(f'O número {n1} é divisível somente por 2 ou somente por 3.\n')
else:
    print(f'O número {n1} não é divisível por 2 ou 3, ou é divisível por 2 e 3.\n')

print(type(x1))
print(type(x2))
print(x1)
print(x2)

# OU PODE FAZER DESTE JEITO SEM O TIPO PRIMITIVO "BOOL (LÓGICO)"

x3 = n1 - 2 * (n1 // 2)
x4 = n1 - 3 * (n1 // 3)

if (x3 and not x4) or (not x3 and x4):
    print(f'\nO número {n1} é divisível somente por 2 ou somente por 3.\n')
else:
    print(f'\nO número {n1} não é divisível por 2 ou 3, ou é divisível por 2 e 3.\n')

print(type(x3))
print(type(x4))
print(x3)
print(x4)
