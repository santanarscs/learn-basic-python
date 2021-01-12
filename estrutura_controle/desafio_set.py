PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    'Jõao gosta de futebol e política',
    'A praia foi divertida'
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidoas: ', intersecao)
    else:
        print('Texto autorizado', texto)
