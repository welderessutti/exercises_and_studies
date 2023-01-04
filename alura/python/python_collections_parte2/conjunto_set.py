usuarios_data_science = [1, 2, 3, 4, 5, 6, 10]
usuarios_machine_learning = [6, 7, 8, 9, 10, 1, 5]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)

print(set(assistiram))

for usuario in set(assistiram):
    print(usuario)

usuarios_data_science = {1, 2, 3, 4, 5, 6, 10}
usuarios_machine_learning = {6, 7, 8, 9, 10, 1, 5}

print(usuarios_machine_learning | usuarios_data_science)  # "|" = ou, traz todos os valores dos conjuntos sem repetí-los.
print(usuarios_machine_learning & usuarios_data_science)  # "&" = e, traz somente os valores dos conjuntos que se repetem.
print(usuarios_machine_learning - usuarios_data_science)  # "-" = menos, traz os valores de um conjunto que não se repetem.
print(usuarios_machine_learning ^ usuarios_data_science)  # "^" = ou exclusivo, traz os valores dos conjuntos que não se repetem.
# Utilizar o | para juntar conjuntos;
# Utilizar o & para juntar apenas números que estão no mesmo conjunto;
# Utilizar o - para remover números repetidos que estão em dois conjuntos;
# O que é ou (^) exclusivo.
print()

usuarios = {1, 2, 3, 4, 5, 6, 7}
print(len(usuarios))

usuarios.add(1)
print(len(usuarios))

usuarios.add(555)
print(len(usuarios))

usuarios = frozenset(usuarios)  # Congela o conjunto tornando-o imutável.
print(usuarios)

print()

meu_texto = "Bem vindo meu nome é Welder eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.split()
print(meu_texto)

meu_texto = set(meu_texto)
print(meu_texto)
