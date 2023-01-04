class Musica:
    def __init__(self, artista, album, musica, ano):
        self.artista = artista
        self.album = album
        self.musica = musica
        self.ano = ano


class Buscador:
    def posicao_musica(self, playlist, musica_buscada):
        for i in range(len(playlist)):
            if playlist[i].musica == musica_buscada:
                return i
        return -1

    def busca_musica(self, playlist, musica_buscada):
        posicao = self.posicao_musica(playlist, musica_buscada)
        if posicao != -1:
            achou_musica = playlist[posicao]
            print(f"A música buscada está na posição {posicao} da playlist.\n"
                  f"Artista: {achou_musica.artista}, Album: {achou_musica.album}, "
                  f"Musica: {achou_musica.musica}, Ano: {achou_musica.ano}.")
        else:
            print("A música buscada não está na playlist.")


artista_01 = Musica("Avenged Sevenfold", "Nightmare", "Nightmare", "2010")
artista_02 = Musica("Oasis", "(What's the Story) Morning Glory?", "Wonderwall", "1995")
artista_03 = Musica("The Beatles", "Rubber Soul", "In My Life", "1965")

playlist_artistas = [artista_01, artista_02, artista_03]

b = Buscador()

b.busca_musica(playlist_artistas, "Nightmare")
