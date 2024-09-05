"""Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

print('O programa lê o número informado e realiza a soma entres todos os números informados, O programa só vai parar quando o usuário digitar o valor 999 ' )
n = 0
contador = 0
soma = 0

while True:
    n = int(input('Digite um número:'))

    if n == 999:
        break

    contador +=1
    soma += n

print(f'Você digitou {contador} números e a soma deles é: {soma}')
