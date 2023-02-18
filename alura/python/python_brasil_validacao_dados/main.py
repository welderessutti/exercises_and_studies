import requests
from acesso_cep import BuscaEndereco

meu_cep = "13333070"
cep_obj = BuscaEndereco(meu_cep)

cep_arq = cep_obj.acessa_via_cep()
print(cep_arq)
