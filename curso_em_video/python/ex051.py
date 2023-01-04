print('=' * 30)
print(f'{" TERMOS DE UMA PA ": ^30}')
print('=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(termo, 10 * razao + termo, razao):
    print(f'{c} -> ', end='')
print('ACABOU')

# UMA MANEIRA DIFERENTE QUE POSTARAM NOS COMENTÁRIOS:

primeiro = float (input('Primeiro Termo: '))
razao = float (input('Razão: '))

t = primeiro

for c in range (1, 11):
    print ('{:.2f}'.format(t))
    t = t + razao
