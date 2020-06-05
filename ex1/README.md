# Desafio de Programação com a Linguagem Python

[x]	Faça um programa em Python utilizando os conceitos de listas e dicionário para armazenar o **código, o nome, a altura e a idade de um grupo de pessoas**. Ao final o programa deve exibir a quantidade de pessoas, a média das idades e a média das alturas das pessoas.

## Resolução

Neste desafio foi utilizado um 2 metodos funcionais *map* e *reduce* para tratar a lista de pessoas que são informadas via input.

O map é repsonsavel por varrer a lista informada e retornar **uma nova lista** com o mesmo tamanho, porém que sofreu alguma alteração;

O reduce é responsavel por retornar **uma nova lista** com o valor total dos itens enviados;

Após obter o valor total das idades e tamanho das pessoas, foi utilizado o metodo *len()* para retornar o tamanho da lista e assim poder gerar a média de cada atributo;

*Obs*: Tambem foi utilizado um conceito de **single responsibility principle** que tem como objetivo a responsabilidade única de cada método, por isso foi implementado os métodos

- mappingList()
- reduceList()
- calculateFinal()

*Existe a conciência que o codigo elaborado pode ser melhor desenvolvido*