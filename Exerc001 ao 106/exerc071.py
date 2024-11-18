
valor = int(input('Informe o valor que sera sacado: R$'))

print(f'Valor solicitado R${valor}.')

notas_de_50 = (valor // 50)
print(notas_de_50, 'Notas de 50')

notas_de_20 = (valor - notas_de_50 * 50)  // 20
print(notas_de_20, 'Notas de 20')

notas_de_10 = (valor - notas_de_20 * 20 - notas_de_50 *50) // 10
print(notas_de_10, 'Notas de 10')

notas_de_1 = (valor - notas_de_20 * 20 - notas_de_50 *50 - notas_de_10 * 10) // 1
print(notas_de_1, 'Notas de 1')
