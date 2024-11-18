"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

lista = []
lista_individual = []
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    lista_individual.append(nome)
    lista_individual.append(peso)
    lista.append(lista_individual[:])
    lista_individual.clear()

    continuar = str(input('Deseja continuar [S/N]: ')).upper()[0]
    if continuar == 'N':
        break

print(lista)

print(f'Foram cadastradas {len(lista)} pessoas')


lista_de_pesos = [iten[1] for iten in lista]
pesos_ordenados = sorted(lista_de_pesos)
print(pesos_ordenados)

print(f'2 maiores pesos: {pesos_ordenados[-3:]}')

print(f'2 menores pesos: {pesos_ordenados[0:3]}')
