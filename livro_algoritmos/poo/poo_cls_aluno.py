class ClsSala:

    def __init__(self):
        self.__sala = ""


class ClsTurma(ClsSala):

    def __init__(self):
        self.__turma = ""
        super().__init__()


class ClsAluno(ClsTurma):

    def __init__(self):
        self.__nome = ""
        self.__notas = []
        self.__media = 0
        super().__init__()

    def __cmedia(self):
        media = sum(self.__notas) / len(self.__notas)
        self.__media = media
        return self.__media

    @property
    def nome(self):
        return self.__nome

    @property
    def notas(self):
        return self.__notas

    @property
    def pega_media(self):
        return self.__cmedia()

    @property
    def sala(self):
        return self.__sala

    @property
    def turma(self):
        return self.__turma

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @notas.setter
    def notas(self, nota):
        self.__notas.append(nota)

    @sala.setter
    def sala(self, sala):
        self.__sala = sala

    @turma.setter
    def turma(self, turma):
        self.__turma = turma


aluno = ClsAluno()

aluno.nome = input("Informe o nome: ")
aluno.turma = input("Informe a turma: ")
aluno.sala = input("Informe a sala: ")


for i in range(4):
    aluno.notas = float(input(f"Nota {i + 1}: "))

print(f"Nome: {aluno.nome}")
print(f"Turma: {aluno.turma}")
print(f"Sala: {aluno.sala}")


for x in aluno.notas:
    print(x)

print(f"Média: {aluno.pega_media}")
