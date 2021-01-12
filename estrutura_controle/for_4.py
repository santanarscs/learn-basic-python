from random import randint
for i in range(1, 11):
    if i == 6:
        break
    print(i)
else:
    print('FIM!!')


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue
    if sortear_dado() == i:
        print('ACERTOU', i)
        break
else:
    print('NÃO ACERTOU O NUMERO')
