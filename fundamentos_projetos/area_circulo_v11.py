#!/usr/bin/python3
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("É necessário informar o raio do circulo")
        print(f"Sintaxe: {sys.argv[0][2:]} <raio>")
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do curculo é: ', area)
