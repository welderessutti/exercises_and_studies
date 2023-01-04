frase = str(input('Digite uma frase: ')).strip()

print(f'A letra "A" aparece na frase {frase.replace("á", "a").upper().count("A")} vezes.')
print(f'A letra "A" aparece primeiro na posição {frase.replace("á", "a").upper().find("A") + 1}.')
print(f'A letra "A" aparece por último na posição {frase.replace("á", "a").upper().rfind("A") + 1}.')
print(f'A frase contém o total de {len(frase)} caracteres.')
