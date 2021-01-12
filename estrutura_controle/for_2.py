palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end=",")
print('FIM')

aprovados = ['Raphael', 'Barbara', 'Fernando', 'Aramis']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')

for dia in dias_semana:
    print(f'Hoje é {dia}')

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
