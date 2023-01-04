usuarios_cadastrados = []

while True:
    novo_usuario = [(input('Digite seu nome de usuário: ').lower())]

    for novo in novo_usuario:
        if novo in usuarios_cadastrados:
            print(f'O usuário {novo} já existe. Tente outro.')
        else:
            usuarios_cadastrados.append(novo)
            print(f'O usuário {novo} foi cadastrado com sucesso!')

    continuar = input('\nDeseja continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Opção inválida. Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

print(len(usuarios_cadastrados), end=' ')
print(usuarios_cadastrados)
