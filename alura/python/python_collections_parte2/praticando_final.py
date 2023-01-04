from collections import Counter

texto1 = """
O programa Alura Stars é composto por várias pessoas que fortalecem a comunidade da Alura, compartilhando conhecimento, apoiando e incentivando mais gente a transformar suas vidas por meio da tecnologia.
Na última publicação do ano da série Mulheres em Tech, você vai conhecer algumas das mulheres que se destacam como embaixadoras desse time de estrelas.
Um problema comum quando estamos desenvolvendo uma aplicação é ficar empolgado(a) quando ela está funcionando bem no nosso ambiente. Mas, quando a utilizamos em outro computador ou subimos para produção, a aplicação não executa da forma como queríamos. Se estava funcionando perfeitamente, não deveria acontecer o mesmo em outros ambientes?
Para que os processos presentes nos fluxos de trabalho, como um ETL ou ELT, sejam gerenciados pelo Airflow, como podemos garantir que as tarefas serão executadas da melhor forma possível?
Antes de respondermos essa questão, vamos voltar um pouco no tempo. O Airflow surgiu em 2014, na Airbnb, com Maxime Beauchemin e a ideia de suprir a necessidade de gerenciar fluxos de trabalho (workflows) cada vez mais complexos. Você pode imaginar essa ferramenta como um maestro responsável por orquestrar vários músicos e suas execuções.
Para que seja possível lidar com todas as tarefas envolvidas em um fluxo de trabalho complexo, o Airflow utiliza de um mecanismo chamado Executor. Mas o que esse mecanismo faz exatamente? É isso que vamos descobrir agora!
"""

texto2 = """
Para entendermos a função do Executor dentro do Airflow, temos que conhecer dois conceitos essenciais antes: as tasks e os DAGs.
As tasks - em português, tarefas - constituem o elemento básico de execução do Airflow, pois é por meio delas que todo o processo de dados ocorre. Elas são organizadas de forma que cada tarefa tenha duas dependências. Uma tarefa possui outras tarefas que precisam ser executadas antes, ou seja, as upstream dela. Essa mesma tarefa também possui outras tarefas que só serão executadas depois dela, as que são downstream dela.
Quem gerencia as dependências, as ordens e as relações que dizem como as tarefas serão executadas é o DAG - Directed Acyclic Graph, em tradução livre, Grafo Acíclico Direcionado. Abaixo, podemos ver um exemplo básico de um DAG:
Para entendermos por que seu time precisa conhecer o Trello, vamos conhecer a Maria, que já realizou alguns trabalhos de maneira individual, mas foi contratada para trabalhar em equipe na empresa Bytestore. Ela e seu time têm algumas dúvidas sobre como dividir as tarefas de um projeto, definir prazos, responsáveis e priorizar o que é mais importante a ser executado.
Ao pesquisarem sobre ferramentas para aumentar a produtividade, as pessoas da equipe de Maria encontraram o Trello. Descobriram que ele pode ser usado para facilitar o gerenciamento de projetos, e melhorar a forma de lidar com o fluxo de informações e a gestão dos negócios. Assim, para ajudarmos a Maria, vamos aprender mais sobre essa ferramenta e entender as vantagens de usá-la na sua equipe.
"""


def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print(f"{caractere} -> {proporcao * 100:.2f} %")


analisa_frequencia_de_letras(texto1)
print()
analisa_frequencia_de_letras(texto2)
