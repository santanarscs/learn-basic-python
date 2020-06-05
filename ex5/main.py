from person import Person

def main():
  person = Person()
  person.setName(input('Entre com seu nome: '))
  person.setAge(int(input('Entre com sua idade: ')))
  person.setHeight(float(input('Entre com sua alutra: '))) 
  person.setWeight(float(input('Entre com seu peso: ')))
  print('Oi {} você tem {}, sua altura é de {}, e peso {}, logo seu IMC é de {:.2f}'
    .format(person.getName(), person.getAge(), person.getHeight(), person.getWeight(), person.getImc()))

main()