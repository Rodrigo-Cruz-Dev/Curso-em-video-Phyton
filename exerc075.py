"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
cont = 0
n1 = int(input(('dig um n: ')))
n2 = int(input(('dig um n: ')))
n3 = int(input(('dig um n: ')))
n4 = int(input(('dig um n: ')))
tupla = (n1, n2, n3, n4)
print(tupla)

if 9 in tupla:
    print(f'O num 9 aparece {tupla.count(9)} vez(es)')

if 3 in tupla:
    print(f'O num 3 aparece na posição {tupla.index(3) +1}')

for numero in tupla:
    if numero % 2 == 0:
        cont += 1
print(f'{cont} num par(es)  digitado(s)')



