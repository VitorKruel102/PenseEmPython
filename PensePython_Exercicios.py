
# 1.3 Primeiro Programa: 
def PrimeiroPrograma():
    print('Hello World!')


# 1.4 Operadores Aritméticos:
def Operadores():
    soma = 40 + 2
    subtracao = 43 - 1
    multiplicacao = 6 * 7
    divisao = 84 / 2
    exponenciacao = 6 ** 2

    print(f'Soma: {soma}')
    print(f'Subtração: {subtracao}')
    print(f'Multiplicacao: {multiplicacao}')
    print(f'Divisão: {divisao}')
    print(f'Exponenciação: {exponenciacao}')
    

# 1.5 Valores e Tipos:
def ValorTipos():
    print(type(2))
    print(type(42.0))
    print(type('Hello, World!'))
    pass


if __name__ == '__main__':
    ValorTipos()