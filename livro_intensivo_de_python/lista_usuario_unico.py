current_users = ['welder', 'welderessutti', 'welderressutti', 'dedi']

new_users = ['phoebe', 'welder', 'carmen', 'dedi']

for new_user in new_users:
    if new_user in current_users:
        print(f'O usuário {new_user} está disponível.')
    else:
        print(f'O usuário {new_user} já está sendo utilizado. Tente outro.')
