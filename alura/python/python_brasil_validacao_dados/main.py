from cpf_cnpj import Documento

aaa = 54127188000162
bbb = 38826187878

cnpj_teste = Documento.cria_documento(aaa)
cpf_teste = Documento.cria_documento(bbb)

print(cnpj_teste)
print(cpf_teste)
