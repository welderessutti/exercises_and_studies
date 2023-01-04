print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

termo = int(input('Quantos termos você quer mostrar?: '))

cont = 1

primeiro = 0
segundo = 1

while cont <= termo:
    print(f'{primeiro} -> ', end='')
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro
    cont += 1

print('FIM')
