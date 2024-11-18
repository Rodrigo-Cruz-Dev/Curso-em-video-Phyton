"""Refaça o DESAFIO 35 dos triângulos,
acrescentando o recurso de mostrar 
que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes"""

a = float(input('Digite a medida 1:'))
b = float(input('Digite a medida 2: '))
c = float(input('Digite a medida 3: '))

if a + b > c and a + c > b and b + c > a:
    print('As medidas informadas podem formar um triangulo')

    if a == b and a == c and b == c:
        print('equilatero')

    elif a != b and a !=c and b!=c:
        print('escaleno')

    else:
        print('isosceles')

else:
    print('As medidas informadas não podem formar um triangulo')


