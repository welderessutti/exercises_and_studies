media = 0
idade_homem_velho = 0
nome_homem_velho = ''
mulheres_20 = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = input('Nome: ').strip().title()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    media += idade

    if sexo == 'M' and idade > idade_homem_velho:
        idade_homem_velho = idade
        nome_homem_velho = nome
    elif sexo == 'F' and idade < 20:
        mulheres_20 += 1

print(f'A média de idade do grupo é de {media / 4} anos.')
print(f'O homem mais velho tem {idade_homem_velho} anos e se chama {nome_homem_velho}.')
print(f'Ao todo são {mulheres_20} mulheres com menos de 20 anos.')
