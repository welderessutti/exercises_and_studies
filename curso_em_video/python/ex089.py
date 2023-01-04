lista = []
nome = []
nota = []

while True:
    nome.append(input('Nome: ').strip().title())
    nota.append(float(input('Nota 1: ').strip()))
    nota.append(float(input('Nota 2: ').strip()))
    nome.append(nota[:])
    lista.append(nome[:])
    nome.clear()
    nota.clear()

    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Opção inválida. Quer continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

print('-=' * 13)
print(f'{"Nº":<4}', end='')
print(f'{"NOME":<14}', end='')
print(f'{"MÉDIA":<4}')
print('-' * 26)

for a, b in enumerate(lista):
    print(f'{a:<4}', end='')
    print(f'{lista[a][0]:<14}', end='')
    print(f'{(lista[a][1][0] + lista[a][1][1]) / 2:>4}')

print('-' * 26)

while True:
    mostrar_nota = int(input('Mostrar notas de qual aluno? (999 interrompe): ').strip())
    while mostrar_nota < 0 or mostrar_nota > (len(lista) - 1) and mostrar_nota != 999:
        mostrar_nota = int(input('Opção inválida. Mostrar notas de qual aluno? (999 interrompe): ').strip())
    if mostrar_nota == 999:
        break

    print(f'Notas de {lista[mostrar_nota][0]} são: {lista[mostrar_nota][1]}')
    print('-' * 26)

# PROFESSOR FEZ ASSIM:

ficha = list()

while True:
    nome_1 = input('Nome: ').strip().title()
    nota1 = float(input('Nota 1: ').strip())
    nota2 = float(input('Nota 2: ').strip())
    media = (nota1 + nota2) / 2
    ficha.append([nome_1, [nota1, nota2], media])

    continuar_1 = input('Quer continuar? [S/N]: ').strip().upper()
    while continuar_1 not in 'SN':
        continuar_1 = input('Opção inválida. Quer continuar? [S/N]: ').strip().upper()
    if continuar_1 == 'N':
        break

print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)

for x, z in enumerate(ficha):
    print(f'{x:<4}{z[0]:<10}{z[2]:>8.1f}')

while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): ').strip())
    while opc < 0 or opc > (len(ficha) - 1) and opc != 999:
        opc = int(input('Opção inválida. Mostrar notas de qual aluno? (999 interrompe): ').strip())
    if opc == 999:
        print('FINALIZANDO...')
        break

    print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

print('VOLTE SEMPRE!')
