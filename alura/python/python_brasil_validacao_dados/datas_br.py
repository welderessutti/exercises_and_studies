from datetime import datetime


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_lista = [
            "Janeiro", "Fevereiro", "Março",
            "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro",
            "Outubro", "Novembro", "Dezembro"
        ]

        mes_numero = self.momento_cadastro.month - 1
        return meses_lista[mes_numero]

    def dia_semana(self):
        dias_lista = [
            "Segunda", "Terça", "Quarta"
            "Quinta", "Sexta", "Sábado",
            "Domingo"
        ]

        dia_numero = self.momento_cadastro.weekday()
        return dias_lista[dia_numero]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        diferenca = datetime.today() - self.momento_cadastro
        return diferenca
