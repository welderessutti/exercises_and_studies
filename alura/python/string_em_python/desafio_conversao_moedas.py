import re

'''Exemplos de URLs válidas:
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio

Exemplos de URL inválidas:
    https://bytebank/cambio
    http://bytebank.naoexiste/cambio
    ht:bytebank.naoexiste/cambio'''


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    @staticmethod
    def sanitiza_url(url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia.")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f"{self.url}\nParâmetros: {self.get_url_parametros()}\nURL base: {self.get_url_base()}"

    def __eq__(self, other):
        return self.url == other.url


url_01 = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url_01)

valor_dolar = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "real" and moeda_destino == "dolar":
    valor_conversao = int(quantidade) / valor_dolar
    print("O valor de R$ " + quantidade + " reais é igual a $ " + str(valor_conversao) + " dólares.")
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_conversao = int(quantidade) * valor_dolar
    print("O valor de $ " + quantidade + " dólares é igual a R$ " + str(valor_conversao) + " reais.")
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")
