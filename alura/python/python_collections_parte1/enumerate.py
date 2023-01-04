usuarios = [
    ("Welder", 34, 1988),
    ("Carmen", 63, 1959),
    ("Wilnir", 66, 1956)
]

for indice, usuario in enumerate(usuarios):
    print(indice, usuario)

print()

for nome, idade, ano in usuarios:
    print(nome, idade, ano)

print()

for nome, _, _, in usuarios:
    print(nome)
