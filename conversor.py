class data:
    def __init__(self, mes, ano):
        self.mes = mes
        self.ano = ano

    def dataFormatada(self):
        nomeMes = {
            '1': 'Janeiro',
            '2': 'Fevereiro',
            '3': 'Março',
            '4': 'Abril',
            '5': 'Maio',
            '6': 'Junho',
            '7': 'Julho',
            '8': 'Agosto',
            '9': 'Setembro',
            '10': 'Outubro',
            '11': 'Novembro',
            '12': 'Dezembro'
        }
        textoFormatado = f'{nomeMes[str(self.mes)]} de {self.ano}'
        return textoFormatado

    def converterMes(self):
        mesC = {
            '1': '2',
            '2': '3',
            '3': '4',
            '4': '5',
            '5': '6',
            '6': '7',
            '7': '8',
            '8': '9',
            '9': '10',
            '10': '11',
            '11': '12',
            '12': '13',
        }
        return f'{mesC[str(self.mes)]}'

    def converterAno(self):
        anoC = {
            '2020': '5',
            '2021': '6',
            '2022': '7',
            '2023': '8'
        }
        return f'{anoC[str(self.ano)]}'