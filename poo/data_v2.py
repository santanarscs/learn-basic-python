class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


if __name__ == '__main__':
    d1 = Data(5, 12, 2021)
    print(d1)

    d2 = Data(7, 11, 2021)
    print(d2)
