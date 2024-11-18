#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: Quantos números foram digitados. A lista de valores, ordenada de forma decrescente. Se o valor 5 foi digitado e está ou não na lista.

lista_de_numeros = []
while True:
    n = input('Dig um num: ')
        
    lista_de_numeros.append(n)
    continuar = input('Deseja continuar? S \ N: ').upper().strip()[0]
    if continuar == 'N':
        break

print(lista_de_numeros)

print(f'{len(lista_de_numeros)} num digitados')

lista_de_numeros.sort(reverse=True)
print(f'Lista em ordem decrescente {lista_de_numeros}')

if 5 in lista_de_numeros:
    print('5 esta na lista')
else:
    print('5 não esta na lista')
