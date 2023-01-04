print('Gerador de PA')
print('-=' * 10)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

vezes = 10
cont_geral = 0
fim = False

while vezes != 0:
    cont = 1
    while cont <= vezes:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
        cont_geral += 1
    print('PAUSA')

    vezes = int(input('Quantos termos você quer mostrar a mais?: '))

print(f'Progressão finalizada com {cont_geral} termos mostrados.')
