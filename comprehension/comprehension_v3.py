generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))  # Saida 0
print(next(generator))  # Saida 4
print(next(generator))  # Saida 16
print(next(generator))  # Saida 36
print(next(generator))  # Saida 64
# print(next(generator)) # Error
