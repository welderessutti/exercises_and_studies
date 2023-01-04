nome = str(input('Digite seu nome completo: ')).strip()

separa = nome.split()

print(f'O seu primeiro nome é {separa[0]} e o seu último nome é {separa[-1]}.')  # PROFESSOR FEZ A FORMULA UM POUCO DIFERENTE, FICARIA {separa[len(nome) -1]}.
