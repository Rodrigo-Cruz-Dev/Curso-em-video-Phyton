#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    numero = int(input('Dig um número:'))
    if numero not in lista:
        lista.append(numero)
    else:
        print('numero já registrado, escolha outro')

    continuar = input('Deseja continuar? S / N ').upper().strip()[0]
    if continuar == 'N':
        break
lista.sort()
print(f'Sua lista:')
for itens in lista:
    print(f'{itens}', end='> ')