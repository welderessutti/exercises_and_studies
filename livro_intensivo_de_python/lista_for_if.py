# LISTA COM "FOR" E "IF":

users = ['gabriel', 'julio', 'mateus', 'admin']

for user in users:
    if user == 'admin':
        print(f'Olá {user}, gostaria de ver um relatóirio de status?')
    else:
        print(f'Olá {user}, obrigado por fazer login novamante.')

# VERIFICANDO SE UMA LISTA ESTÁ VAZIA COM "IF" E "FOR", PYTHON DEVOLVE "FALSE" PARA LISTA VAZIA:

ingredientes = []

if ingredientes:
    for ingrediente in ingredientes:
        print(f'\nAdicionar o ingrediente {ingrediente}.')
else:
    print('\nSua lista de ingredientes está vazia.')
