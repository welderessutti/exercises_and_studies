produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30,
            'Livro', 34.90)

print('-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)

for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f"{produtos[p]:.<40}", end='')
    elif p % 2 == 1:
        print(f"R$ {produtos[p]:>7.2f}")

print('-' * 50)

# OUTRA FORMA QUE POSTARAM NOS COMENTÁRIOS:

produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,

            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print("=" * 50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("=" * 50)

for c in range(0, len(produtos), 2):
    print(f"{produtos[c]:.<40}", f" R$ {produtos[c+1]:>7.2f}")

print("="*50)
