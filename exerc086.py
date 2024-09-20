"""Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta."""
lista1 =[[],[],[]]
lista2 = [[],[],[]]
lista3 = [[],[],[]]

for item in range(3):
    n = int(input('Dig numero:'))
    lista1[item].append(n)

for item in range(3):
    n = int(input('Dig numero:'))
    lista2[item].append(n)

for item in range(3):
    n = int(input('Dig numero:'))
    lista3[item].append(n)

print(f'{lista1}\n{lista2}\n{lista3}')
