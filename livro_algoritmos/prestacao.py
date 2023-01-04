valor = int(input('Digite o valor do bem: '))
taxa = int(input('Digite a taxa de juros: '))
tempo = int(input('Digite o tempo em atraso: '))

p = valor + (valor * (taxa / 100) * tempo)
print(p)
