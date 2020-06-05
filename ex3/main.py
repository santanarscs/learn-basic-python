from currency_converter import CurrencyConverter
c = CurrencyConverter()

def main():
  value = input('Digite o valor em real: ')
  currencyConvert = input('Em qual moeda quer converter? [dolar | euro | libra]: ')
  if currencyConvert == 'dolar':
    convertValue = c.convert(value, 'BRL', 'USD')
    print('R$ {} convertido em {} é igual a: US$ {:.2f}'.format(value, currencyConvert, convertValue))
  elif currencyConvert == 'euro':
    convertValue = c.convert(value, 'BRL', 'EUR')
    print('R$ {} convertido em {} é igual a: € {:.2f}'.format(value, currencyConvert, convertValue))
  elif currencyConvert == 'libra':
    convertValue = c.convert(value, 'BRL', 'GBP')
    print('R$ {} convertido em {} é igual a: £ {:.2f}'.format(value, currencyConvert, convertValue))
  else:
    print('{} não é uma moeda válida no sistema'.format(value))

main()