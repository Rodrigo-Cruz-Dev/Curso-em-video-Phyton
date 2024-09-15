#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

lista = []
for itens in range(5):
    lista.append(int(input('Dig um numero: ')))

print(f'O maior valor digitado foi {max(lista)} na posição: ',end=' ')
for indice, itens in enumerate(lista):
    if itens == (max(lista)):
        print(f'{indice}',end='...')

print(f'\nO menor número digitado foi {min(lista)} na posição:', end=' ')
for indice, itens in enumerate(lista):
    if itens == (min(lista)):
        print(f'{indice}', end='...')