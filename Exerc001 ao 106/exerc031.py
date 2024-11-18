km = float(input('Qual a distancia de sua viagem?'))
print(f'{km}km')
if km <= 200:
    print('O valor da viagem sera de R${}'.format(km * 0.50))
else:
    print('O valor da viagem será de R${}'.format(km * 0.45))