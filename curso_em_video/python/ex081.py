lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar? [S/N]: ').strip().upper()

    while continuar not in 'SN':
        continuar = input('Opção inválida. Quer continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

lista.sort(reverse=True)  # OU lista.reverse()

print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista e está na posição {lista.index(5)}.')
else:
    print('O valor 5 não foi encontrado na lista!')
