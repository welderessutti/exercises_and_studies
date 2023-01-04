from lib import interface
from lib import arquivo
from time import sleep

arq = "cursoemvideo.txt"

if not arquivo.arquivo_existe(arq):
    arquivo.criar_arquivo(arq)

while True:
    resposta = interface.menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoaa", "Sair do sistema"])
    if resposta == 1:
        arquivo.ler_arquivo(arq)
    elif resposta == 2:
        arquivo.cabecalho("NOVO CADASTRO")
        nome = input("Nome: ")
        idade = interface.leia_int("Idade: ")
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        interface.cabecalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(1)
