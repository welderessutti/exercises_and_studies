class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano
        self._likes = 0

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self._ano} - Likes: {self._likes}"

    def dar_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._duracao = duracao
        super().__init__(nome, ano)

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self._ano} - Duração: {self._duracao} - Likes: {self._likes}"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._temporadas = temporadas
        super().__init__(nome, ano)

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self._ano} - Temporadas: {self._temporadas} - Likes: {self._likes}"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def __getitem__(self, item):
        return self.programas[item]

    def __len__(self):
        return len(self.programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

listinha = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', listinha)

for programa in minha_playlist:
    print(programa)

print(f'Tamanho: {len(minha_playlist)}')
