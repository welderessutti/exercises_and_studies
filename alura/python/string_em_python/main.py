url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

# Sanatização do URL.
url = url.strip()

# Validação do URL.
if url == "":
    raise ValueError("A URL está vazia.")

# Aqui eu fiz usando o método .split(), mais prático.
'''url_split = url.split("?")

url_base = url_split[0]
url_parametros = url_split[1]'''

# Separa as bases e os parâmetros.
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)

# Busca o valor de um parâmetro.
parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&", indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
