from random import shuffle

n1 = str(input('Primeiro aulno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

ordem = [n1, n2, n3, n4]
shuffle(ordem)  # APENAS EMBARALHA A LISTA, NÃO RECEBE (=) VARIÁVEL.

print(f'A ordem de apresentação vai ser: {ordem}')
