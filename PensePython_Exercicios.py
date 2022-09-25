import math
import turtle


# 1.3 Primeiro Programa:
def primeiro_programa():
    print('Hello World!')
    
# 1.4 Operadores Aritméticos:
def operadores():
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
def valores_tipos():
    print(type(2))
    print(type(42.0))
    print(type('Hello, World!'))
    pass

# 2.3 Expressões e instruções:
def expressoes():
    n = 17
    print(n + 25)    
    pass

# 4.1 Programa de Interface:
def programa_polygon(n=7, length=70):
    t = turtle.Turtle()
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

    turtle.mainloop()

def programa_circle(t=5, r=50):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    programa_polygon(n, length)
    
if __name__ == '__main__':
    programa_circle(7, 70)