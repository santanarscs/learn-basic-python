import csv

with open('pessoa.csv') as entrada:
    for pessoa in csv.reader(entrada)
    print('Nome: {} Idade: {}'.format(*pessoa))
