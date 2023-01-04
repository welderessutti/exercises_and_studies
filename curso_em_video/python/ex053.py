frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(f'O inverso da frase {junto} é {inverso}.')
if inverso == junto:
    print(f'A frase {frase} é um palíndromo.')
else:
    print(f'A frase {frase} não é um palíndromo.')

# SEM USAR O "FOR"

frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(f'O inverso da frase {junto} é {inverso}.')
if inverso == junto:
    print(f'A frase {frase} é um palíndromo.')
else:
    print(f'A frase {frase} não é um palíndromo.')

print(f'\n{palavras}')
print(junto)
print(inverso)
print(len(junto))






















