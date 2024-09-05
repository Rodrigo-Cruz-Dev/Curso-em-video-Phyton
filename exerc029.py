velocidade = float(input('Informe a velocidade:'))
if velocidade >= 80:
    print(f'Você ultrapassou a velocidade permitida de 80km estando a {velocidade}km e recebeu um multa de R${(velocidade - 80 ) * 7.00 + 200}')
else:
    print('Boa viagem')