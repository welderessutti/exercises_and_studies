import json
import requests

r = requests.get("https://viacep.com.br/ws/13333070/json/")
r_json = r.json()
r_json_string = json.dumps(r_json)

with open("meu_arquivo.json", "w") as cep:
    cep.write(r_json_string)
cep.close()

with open("meu_arquivo.json", "r") as cep_json:
    leitura = json.load(cep_json)
    for x, z in leitura.items():
        print(x, z)
cep_json.close()
