agenda = []  # Criando uma lista vazia.

# DEFINIÇÃO DAS FUNÇÕES

# Descrição: Este procedimento cria um novo contato na agenda.
# Nome: novo()
# Tipo: procedimento
def novo():
    global agenda  # Definindo variável como Global.
    nome = p_nome()
    celular = input("Celular....: ")
    email   = input("E-mail.....: ")
    agenda.append([nome, celular, email])  # Adicionando os dados na agenda
    print("-----------------------------"
          "Registro gravado com Sucesso!!!"
          "-------------------------------")

# Descrição: Este procedimento lê um nome.
# Nome: p_nome()
# Tipo: procedimento
def p_nome():
    return(input("Nome.......: "))

# Descrição: Este procedimento lista um registro
# Nome: listar_dados(nome, celular, email)
# Tipo: procedimento
def listar_dados(nome, celular, email):
    print("Nome: %sCelular: %sEmail: %s" % (nome, celular, email))
    print("----------------------------------")

# Descrição: Este procedimento lista todos os registros da matriz.
# Nome: listar()
# Tipo: procedimento
def listar():  # Função para mostrar lista de contatos.
    print("CONTATOS DA AGENDA ###############")
    for e in agenda:
        listar_dados(e[0], e[1], e[2])
    print("FIM DA AGENDA ####################")

# Descrição: Esta função pesquisa um contato pelo nome.
# Nome: pesquisa(nome): int
# Tipo: função
def pesquisa(nome):  # Função para pesquisar contatos.
    name = nome.lower()
    for d, e in enumerate(agenda):  # percorre toda a matriz.
        if e[0].lower() == name:  # procura o nome desejado
            return d  # retorna o índice do nome encontrado
    return None  # retorna vazio se não encontrar

# Descrição: Este procedimento exibe o registro ou mensagem de insucesso
# Nome: pesquisar():
# Tipo: procedimento
def pesquisar():
    # pesquisa o nome
    p = pesquisa(p_nome())  # Entrada de dados.
    if p != None:
        print("Registro encontrado!")
        # atualiza as variáveis se encontrou
        nome = agenda[p][0]
        celular = agenda[p][1]
        email = agenda[p][2]
        # mostra o registro
        listar_dados(nome, celular, email)
    else:
        # exibe a mensagem de insucesso na procura do registro
        print("Nome não encontrado!!!")

# Descrição: Este procedimento apaga um contato
# Nome: apagar():
# Tipo: procedimento
def apagar():
    global agenda
    nome = p_nome()
    # retorna o índice do nome ou vazio
    p = pesquisa(nome)
    if p != None:  # Se encontrou o contato
        del agenda[p]  # exclui o contato
        print("-----------------------------"
              "Registro APAGADO com Sucesso!!!"
              "-------------------------------")
    else:
        # não encontrou o registro para excluir
        print("Nome não encontrado.")

# Descrição: Este procedimento edita um contato
# Nome: editar():
# Tipo: procedimento
def editar():
    p = pesquisa(p_nome())  # Entrada de dados.
    # Se encontrou o registro
    if p != None:
        # mostra o nome e pede a edição dos demais
        nome = agenda[p][0]
        print("Nome........: ", nome)
        celular = input("Celular....:")
        email = input("E-mail.....:")
        agenda[p] = [nome, celular, email]  # Armazenando os novos dados.
        print("-----------------------------"
              "Registro EDITADO com Sucesso!!!"
              "-------------------------------")
    else:
        print("Nome não encontrado.")  # Executa caso a condição seja falsa.

# Descrição: Esta função valida SE O ITEM DIGITADO FOI VALIDO
# Nome: validar(pergunta, inicia, fim): int
# Tipo: função
def validar(pergunta, inicio, fim):  # Função para validar números inteiros.
    while True:  # Criando um loop infinito.
        try:  # Criando um acordo/condição.
            valor = int(input(pergunta))  # Entrada de dados.
            if inicio <= valor <= fim:  # Determinando uma condição.
                return (valor)  # Executa caso for verdadeira.
            else:
                return (0)
        except ValueError:  # Executa caso for falsa.
            print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

# Descrição: Esta função retorna o item do menu ou 0 para invalido
# Nome: menu(pergunta, inicia, fim): int
# Tipo: função
def menu():  # Função que exibe o menu de opções.
    print("""
   1 - Adicionar novo contato
   2 - Editar um contato
   3 - Pesquisar contato
   4 - Lista de contatos
   5 - Apagar um contato
   6 - Sair
""")
    return validar("Escolha uma opção: ", 1, 6)

while True:  # Criando um loop infinito.
    opcao = menu()
    if opcao == 0:
        print("Opcao Inválida!")
    elif opcao == 6:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        pesquisar()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        apagar()
