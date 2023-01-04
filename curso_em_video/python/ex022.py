nome = str(input('Digite seu nome completo: ')).strip()

separa = nome.split()  # GERA EM LISTA

print(f'Seu nome em letra maiúscula é: {nome.upper()}')
print(f'Seu nome em letra minúscula é: {nome.lower()}')
print(f'Seu nome em letra título é: {nome.title()}')
print(f'Seu nome em letra capitalizada é: {nome.capitalize()}\n')

print(f'O seu nome tem ao todo {len(nome) - nome.count(" ")} letras.')  # REPARA QUE EU TIVE QUE USA "" ASPAS DUPLA OU print('O seu nome tem ao todo {} letras.' .format(len(nome) - nome.count(' ')).
print(f'O seu nome tem ao todo {len("".join(separa))} letras.\n')

print(f'O seu primeiro nome tem {nome.find(" ")} letras.')
print(f'O seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras.')
print(f'O seu último nome é {separa[-1]} e tem {len(separa[-1])}')
