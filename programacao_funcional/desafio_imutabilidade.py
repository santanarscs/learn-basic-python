from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Português do Brasil
setlocale(LC_ALL, 'pt_BR')

# meses_31 = filter(lambda mes: mdays[mes] == 31, range((1, 13)))
# print(meses_31)
# meses_nomes = map(lambda mes: month_name[mes], meses_31)
# juntar_meses = reduce(
#     lambda todos, nome_mes: f'{todos}\n- {nome_mes}', meses_nomes, 'Meses com 31 dias:')
# print(juntar_meses)
