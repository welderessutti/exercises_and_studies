lista = ['John', 'Paul', 'Ringo', 'George']

for c in lista:
    print(f'Dear {c}, I am pleased to invite you to my dinner.')

print('\nUnfortunately, Sir. John won´t be attending dinner.\n')

lista[0] = 'Welder'

for c in lista:
    print(f'Dear {c}, I am pleased to invite you to my dinner.')

print('\nI found a bigger table, there are more than three.\n')

lista.insert(0, 'Carmen')
lista.insert(3, 'Phoebe')
lista.append('Bob')

for c in lista:
    print(f'Dear {c}, I am pleased to invite you to my dinner.')

print('\nI will only be able to invite two people!\n')

while len(lista) > 2:
    print(f"I'm so sorry Dear {lista.pop()}, I won´t be able to invite you to dinner.")

print('\n')

for c in lista:
    print(f'Dear {c}, you are still invited to dinner.')

del lista[0]
del lista[0]

print(f'\n{lista}')
