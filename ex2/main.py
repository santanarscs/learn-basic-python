import math
from functools import reduce
# lista de produtos fixas para teste
# products = [
#   {'codigo': '001', 'name': 'Produto 001', 'price': 16.85},
#   {'codigo': '002', 'name': 'Produto 002', 'price': 28.30},
#   {'codigo': '003', 'name': 'Produto 003', 'price': 45.60},
#   {'codigo': '004', 'name': 'Produto 004', 'price': 89.90},
#   {'codigo': '005', 'name': 'Produto 005', 'price': 120.30},
#   {'codigo': '006', 'name': 'Produto 006', 'price': 30.00},
# ]

def mappingList(key, listItems):
  return list(map(lambda person: person[key], listItems))

def reduceList(listItems):
  return reduce((lambda x, y: x + y), listItems)

def calculateFinal(products):
  listPrices = mappingList('price', products)
  averagePrices = reduceList(listPrices) / len(products)
  expresiveProducts = list(filter(lambda product: product['price'] >= averagePrices, products))
  print("Oi, a média de valor dos protudos é de {:.2f}".format(averagePrices))
  print('Os produtos acima dessa média são esses:')
  for product in expresiveProducts:
    print(product['name'])

def main():
  escape = 's'
  persons = list()
  person = dict()
  while escape == 's':
    person['cod'] = int(input('Digite um código: '))
    person['name'] = input('Digite um nome para seu produto: ')
    person['price'] = float(input('Digite o preço do produto: '))
    persons.append(person.copy())
    escape = input('Deseja adicionar outro produto? [s/n]')
  else:
    calculateFinal(persons)


main()




