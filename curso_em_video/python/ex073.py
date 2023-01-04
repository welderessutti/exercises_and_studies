times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Corinthians', 'Internacional', 'Athletico-PR',
         'Atlético-MG', 'Santos', 'América-MG', 'Goiás', 'Bragantino', 'Fortaleza', 'São Paulo',
         'Botafogo', 'Ceará SC', 'Coritiba', 'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude')

print(f'Os 5 primeiros são {times[0:5]}.')
print(f'Os 4 últimos {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Corinthians está na {times.index("Corinthians") + 1}ª posição.')
