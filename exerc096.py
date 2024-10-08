"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""

def area(base,altura):
    area = base * altura
    print(f'A area de {base} e {altura} é {area}m²')
    return area 


base = float(input('Dig a altura: '))
altura = float(input('Dig o comprimento : '))

resultado = area(base,altura)