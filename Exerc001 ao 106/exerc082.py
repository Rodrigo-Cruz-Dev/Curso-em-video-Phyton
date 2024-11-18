#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Dig um num:')))
    continuar = str(input('Deseja continuar: [S/N]?: '))
    if continuar in 'Nn':
        break
for item in valores: 
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)

for item in valores:
    print(f'> {item}', end="")
print(f'\nPares: {pares}')
print(f'Impares:{impares}')

