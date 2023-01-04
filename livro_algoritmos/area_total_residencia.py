confirmacao = 'sim'.lower()
area_total = 0

while confirmacao == 'sim':
    comodo = input('Qual o cômodo?: ').upper()
    largura = float(input('Qual a largura?: '))
    comprimento = float(input('Qual o comprimento?: '))

    area = largura * comprimento
    area_total += area

    print(f'O cômodo {comodo} possui área de {area} m².')

    confirmacao = input('\nDeseja acrescentar mais cômodos? Sim ou Não?: ').lower()

'''    if confirmacao == 'sim' or 'não' or 'nao':
        confirmacao = confirmacao
    else:
        print('Resposta inválida. Digite Sim ou Não!')
        confirmacao = input('Deseja acrescentar mais cômodos? Sim ou Não?: ').lower()
'''

print(f'A área total da residência é: {area_total} m².')
