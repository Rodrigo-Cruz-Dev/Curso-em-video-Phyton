"""Desenvolva um programa que leia seis números inteiros e 
mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o."""

cont = 0
soma = 0
for c in range(6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você digitou {cont} número pares e a soma deles é {soma}')