"""Faça um programa que leia um número inteiro 
e diga se ele é ou não um número primo."""

n = int(input('numero: '))
cont = 0

for c in range (1 , n +1):
    if n % c == 0:
        cont += 1

if cont == 2:
    print(f'{n} é primo')
else:
    print(f' {n} não é primo')


    