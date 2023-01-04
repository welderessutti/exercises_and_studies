primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))

lista = [primeiro, segundo, terceiro]
ordem = sorted(lista)

print(f'\nO número maior é {ordem[-1]}.')
print(f'O número menor é {ordem[0]}.')

# OU

print(f'\nO número maior é {max(lista)}.')
print(f'O número menor é {min(lista)}.')

# PROOFESSOR FEZ ASSIM:

menor = primeiro

if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro


maior = primeiro

if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

print(f'\nO número maior é {maior}.')
print(f'O número menor é {menor}.')
