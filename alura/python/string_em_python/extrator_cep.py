import re

endereco = "Rua Nove de Julho, 2013, Vila Georgina, Indaiatuba, Sp, 13333-070"

padrao = re.compile("[0-9]{5}-?[0-9]{3}")
busca = padrao.search(endereco)  # Match

print(busca)

if busca:
    cep = busca.group()
    print(cep)
