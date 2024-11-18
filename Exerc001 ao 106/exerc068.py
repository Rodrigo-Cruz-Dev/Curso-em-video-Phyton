"""Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint,choice

print('Jogue par ou ímpar com o computador, o jogo só será interrompido quando o você perder')
cont = 0
while True:
    numero_do_computador = randint(1,11) 
    numero_do_usuario = int(input('Dig um num: ')) 
    escolha_da_maquina = choice(('Par', 'Impar'))
    escolha_do_usuario = str(input('Escolha Par/Impar: ')) 
    soma_dos_numeros = numero_do_computador + numero_do_usuario 
    

    resultado = 'Par' if soma_dos_numeros % 2 == 0 else 'Impar'
    vitória_do_usuario = True if escolha_do_usuario == resultado else False
    vitoria_da_maquina = True if escolha_da_maquina == resultado else False
    
    def texto1():
        print(f'Vc escolheu {numero_do_usuario} e {escolha_do_usuario}, o computador {numero_do_computador} e {escolha_da_maquina}, a soma total é {soma_dos_numeros}, que é {resultado}.')

    if vitória_do_usuario == True and vitoria_da_maquina == False:
        continuar_jogo = True
        cont +=1
        print(f'VITORIA!') 
        texto1()
              
    elif vitória_do_usuario == True and vitoria_da_maquina == True:
        continuar_jogo = True
        print(f'EMPATE!') 
        texto1()

    else:
        continuar_jogo = False
        
    if continuar_jogo != True:
        break

print('DERROTA!')
texto1()
print(f'{cont} vitorias consecutivas.')

