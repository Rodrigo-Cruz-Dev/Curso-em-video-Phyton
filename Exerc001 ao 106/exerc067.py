""" Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo."""

while True:
    numero = int(input('Este programa mostra a tabuada para o valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo \nDigite o número:'))
    if numero <= (-1):
        break
    for i in range(1,11):
        print(f'{numero} X {i} = {numero * i}')
    
print('Tabuada encerrada')