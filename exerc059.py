"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.

r=("="*50)
print(f'{r}')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print(f'{r}')
menu = 0

while menu != 5:
    menu = int(input(f'{r}\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n{r}\n'))

    if  menu == 1:
        resultado = num1 + num2
        print(f'A soma entre o número {num1} e o número {num2} é {resultado}')
    elif menu == 2:
        resultado = num1 * num2
        print(f'A multiplicação entre o numero {num1} e o numero {num2} é {resultado}')
    elif menu == 3:     
        resultado = max(num1, num2)
        print(f'O maior número entre o numero {num1} e o numero {num2} é {resultado}')
    elif menu == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        menu = 0
    elif menu == 5:
        print('Encerrando....')
    else:
        print('Opção invalida! tente novamente')

print(f'Programa finalizado.\n{r}')"""

num1 = int(input('dig num1:'))
num2 = int(input('dig num2:'))

menu = 0
while menu != 5:
    menu = int(input('DIGITE OPC DESEJADA 1 SOMA,2 MULT, 3 MAIOR, 4 DIGITAR NVS NUM, 5 ENCERRAR'))
    
    if menu ==1:
        print(f'total soma {num1} + {num1}: {num1 + num2}')
    elif menu ==2:
        print(f'total mulp {num1} * {num2}: {num1 * num2}')
    elif menu == 3:
        print(f'maior numero entre {num1}, {num2}: {max(num1, num2)}')
    elif menu == 4:
        num1 = int(input('dig num1:'))
        num2 = int(input('dig n2:'))
        menu = 0
    elif menu == 5:
         print('encerrando programa.....')
    else:
        print('opçao invalida')

print('programa finalizado')