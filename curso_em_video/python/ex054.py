from datetime import date
cont_menor = 0
cont_maior = 0

for ano in range(1, 8):
    ano_pessoa = int(input(f'Em que ano a {ano}ª pessoa nasceu?: '))
    if date.today().year - ano_pessoa < 21:
        cont_menor += 1
    else:
        cont_maior += 1

print(f'Ao todo tivemos {cont_maior} pessoas maiores de idade.')
print(f'E também tivemos {cont_menor} pessoas menores de idade.')
