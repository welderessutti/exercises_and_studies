import requests

decada = 2010
url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?decada={decada}"

request = requests.get(url)

json = request.json()

nomes = json[0]["res"]

for i in nomes:
    print(i["ranking"], i["nome"], i["frequencia"])
