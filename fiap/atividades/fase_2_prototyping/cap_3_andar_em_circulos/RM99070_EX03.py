# Inicia as variáveis soma_notas_alunos_impares e soma_notas_alunos_pares com o valor zero:
soma_notas_alunos_impares = soma_notas_alunos_pares = 0

# Executa um laço do tipo for de 1 à 49 pulando de 2 em 2, recebe como input as notas ímpares do usuário e
# faz a soma total das notas na variável soma_notas_alunos_impares:
for numero_aluno_impar in range(1, 50, 2):
    print("\nVOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
    nota_aluno_impar = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {numero_aluno_impar}: "))
    soma_notas_alunos_impares += nota_aluno_impar

# Executa um laço do tipo for de 2 à 50 pulando de 2 em 2, recebe como input as notas pares do usuário e
# faz a soma total das notas na variável soma_notas_alunos_pares:
for numero_aluno_par in range(2, 51, 2):
    print("\nVOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
    nota_aluno_par = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {numero_aluno_par}: "))
    soma_notas_alunos_pares += nota_aluno_par

# Calcula a média das notas dividindo a soma total das notas pela quantidade de alunos:
media_notas_alunos_impares = soma_notas_alunos_impares / 25
media_notas_alunos_pares = soma_notas_alunos_pares / 25

# Lança os outputs informando a média da metade ímpar e par:
print(f"\nA média das notas da metade ímpar foi: {media_notas_alunos_impares:.2f}.")
print(f"A média das notas da metade par foi: {media_notas_alunos_pares:.2f}.\n")

# Verifica qual metade obteve a maior média, e lança o output informando qual delas foi maior ou se houve empate:
if media_notas_alunos_impares > media_notas_alunos_pares:
    print("A metade ímpar teve a maior média.")
elif media_notas_alunos_pares > media_notas_alunos_impares:
    print("A metade par teve a maior média.")
else:
    print("As duas metades obtiveram a mesma média.")
