a = []
b = []
c = []

for x in range(0, 10):
    a.append(int(input(f'Digite o {x + 1}º número "A": ')))
    b.append((int(input(f'Digite o {x + 1}º número "B": '))))
    c.append(a[x] - b[x])

resposta = input('Deseja procurar um elemento na lista "C"? [S/N]: ').strip().upper()

while resposta == 'S':
    pesquisa = int(input('Qual elemento deseja pesquisa?: ').strip())
    i = 0
    acha = False

    while i <= 9 and acha is False:
        if pesquisa == c[i]:
            acha = True
        else:
            i += 1

    if acha is True:
        print(f'O elemento {pesquisa} foi encontrado na posição {i + 1} da lista "C".')
    else:
        print(f'O elemento {pesquisa} não foi encontrado na lista "C".')

    resposta = input('Deseja continuar pesquisando? [S/N]: ').strip().upper()
