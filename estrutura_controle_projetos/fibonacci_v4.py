#!/usr/bin/python3
def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(10000):
        print(fib)
