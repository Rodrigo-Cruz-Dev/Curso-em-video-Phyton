import random
numero_computador = [0, 1, 2 , 3 , 4 , 5]
numero_computador_escolhido = random.choice(numero_computador)
print(numero_computador_escolhido)
numero_usuario = int(input('Digite um numero de 1 a 5:'))
if numero_usuario == numero_computador_escolhido:
    print('Parabens, você acertou! Você escolheu o número {} e o número que o computador escolheu tambem foi {}.'.format(numero_usuario, numero_computador_escolhido))
else:   
    print(f'Você não acertou! Você escolheu o número {numero_usuario} e o número que o computador escolheu foi {numero_computador_escolhido}.')