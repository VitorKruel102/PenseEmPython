# 1.3 Primeiro Programa: 
from audioop import mul
from pickletools import read_uint1
from re import sub


def PrimeiroPrograma():
    print('Hello World!')


# 1.4 Operadores Aritméticos:
def Operadores():
    soma = 40 + 2
    subtracao = 43 - 1
    multiplicacao = 6 * 7
    divisao = 84 / 2

    print(f'Soma: {soma}')
    print(f'Subtração: {subtracao}')
    print(f'Multiplicacao: {multiplicacao}')
    print(f'Divisão: {divisao}')
    

if __name__ == '__main__':
    Operadores()