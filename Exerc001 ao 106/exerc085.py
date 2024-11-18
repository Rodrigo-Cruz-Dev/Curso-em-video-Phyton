"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""

lista = [[],[]]

while True:
    n = int(input('Dig um numero: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
    parar = input('Continuar? [S/N]: ')[0]
    if parar in 'Nn':
        break

print(f'Lista de pares> {sorted(lista[0])}')
print(f'Lista de impares> {sorted(lista[1])}')