# Desafio de Programação com a Linguagem Python

[x]	Faça um programa em Python utilizando os conceitos de listas e dicionário para armazenar o **código, o nome e o preço de um grupo de produtos**. Ao final o programa deve exibir o valor médio dos produtos e os nomes dos produtos com preço superior a média da grupo.

## Resolução

Neste desafio foi utilizado um 2 metodos funcionais *map* , *reduce* e *filter* para tratar a lista de pessoas que são informadas via input.

O map é repsonsavel por varrer a lista informada e retornar **uma nova lista** com o mesmo tamanho, porém que sofreu alguma alteração;

O reduce é responsavel por retornar **uma nova lista** com o valor total dos itens enviados;

O filter é responsavel por retornar **uma nova lista** do mesmo tamanho ou menor dos itens enviados;

Após obter o valor total de preços, foi utilizado o metodo *len()* para retornar o tamanho da lista e assim poder gerar a média do atributo;

Após definir a média dos valores foi gerado uma nova lista com os produtos que estavam acima da média de valor que posteriormente foram listados no retorno da execução do programa;

*Obs*: Tambem foi utilizado um conceito de **single responsibility principle** que tem como objetivo a responsabilidade única de cada método, por isso foi implementado os métodos

- mappingList()
- reduceList()
- calculateFinal()

*Existe a conciência que o codigo elaborado pode ser melhor desenvolvido*