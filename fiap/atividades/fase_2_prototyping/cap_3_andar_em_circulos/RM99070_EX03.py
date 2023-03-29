soma_notas_alunos_impares = soma_notas_alunos_pares = 0

for numero_aluno_impar in range(1, 50, 2):
    print("\nVOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
    nota_aluno_impar = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {numero_aluno_impar}: "))
    soma_notas_alunos_impares += nota_aluno_impar

for numero_aluno_par in range(2, 51, 2):
    print("\nVOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
    nota_aluno_par = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {numero_aluno_par}: "))
    soma_notas_alunos_pares += nota_aluno_par

media_notas_alunos_impares = soma_notas_alunos_impares / 25
media_notas_alunos_pares = soma_notas_alunos_pares / 25

print(f"\nA média das notas da metade ímpar foi: {media_notas_alunos_impares:.2f}.")
print(f"A média das notas da metade par foi: {media_notas_alunos_pares:.2f}.\n")

if media_notas_alunos_impares > media_notas_alunos_pares:
    print("A metade ímpar teve a maior média.")
elif media_notas_alunos_pares > media_notas_alunos_impares:
    print("A metade par teve a maior média.")
else:
    print("As duas metades obtiveram a mesma média.")
