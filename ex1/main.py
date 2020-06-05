import math
from functools import reduce

def mappingList(key, listItems):
  return list(map(lambda person: person[key], listItems))

def reduceList(listItems):
  return reduce((lambda x, y: x + y), listItems)

def calculateFinal(persons):
  listAges = mappingList('age', persons)
  listHeight = mappingList('height', persons)
  
  avergaAges = math.ceil(reduceList(listAges) / len(persons))
  averageHeight = reduceList(listHeight) / len(persons)
  sumPersons = len(persons)
  print(f"O valor total de pessoas é {sumPersons}")
  print("A média de altura de todas as pessoas é: {:.2f}".format(averageHeight))
  print(f"A média de idade de todas as pessoas é {avergaAges}")

def main():
  escape = 's'
  persons = list()
  person = dict()
  while escape == 's':
    person['cod'] = int(input('Digite um código: '))
    person['name'] = input('Digite um nome: ')
    person['height'] = float(input('Digite uma altura: '))
    person['age'] = int(input('Digite uma idade: '))
    persons.append(person.copy())
    escape = input('Deseja adicionar outra pessoa? [s/n]')
  else:
    calculateFinal(persons)


main()
