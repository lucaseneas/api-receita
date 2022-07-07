class date:
    def __init__(self, mes, ano):
        self.month = mes
        self.year = ano

    def formated(self):
        month_name = {
            '2': 'Janeiro',
            '3': 'Fevereiro',
            '4': 'Março',
            '5': 'Abril',
            '6': 'Maio',
            '7': 'Junho',
            '8': 'Julho',
            '9': 'Agosto',
            '10': 'Setembro',
            '11': 'Outubro',
            '12': 'Novembro',
            '13': 'Dezembro'
        }
        year_convert = {
            '5': '2020',
            '6': '2021',
            '7': '2022'
        }

        written = f' Data: {month_name[str(self.month)]} de {year_convert[str(self.year)]}.'
        return written
