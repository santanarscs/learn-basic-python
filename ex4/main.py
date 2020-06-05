
import os
dirname = os.path.dirname(__file__)
def readFileContent():
  fileRead = open(os.path.join(dirname, 'lista.txt'), 'r')
  text = fileRead.read()
  print(text)
  fileRead.close()

def writeFile():
  escape = 's'
  file = open(os.path.join(dirname, 'lista.txt'), 'w')
  while escape == 's':
    name = input('Digite um nome: ')
    phone = input('Digite um telefone: ')
    file.write('nome: {} telefone: {}\n'.format(name, phone))
    escape = input('Deseja adicionar outra pessoa? [s/n]')
  else:
    file.close()

def main():
  action = input('Deseja ler ou escrever novos dados no arquivo? [ler | escrever] ')
  if action == 'ler':
    readFileContent()
  elif action == 'escrever':
    writeFile()
  else:
    print('Opção inválida')

main()