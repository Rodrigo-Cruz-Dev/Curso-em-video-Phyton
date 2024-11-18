km = int(input('Digite quantos km: '))
d = float(input('Digite quantos dias: '))
preço = (60 * d) + (0.15 * km)
print('O valor a pagar é R${:.2f}'.format(preço))