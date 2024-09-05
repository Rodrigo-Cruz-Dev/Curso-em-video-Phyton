"""Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, mostre quantos números foram digitados 
e qual foi a soma entre elas (desconsiderando o flag)."""

contador = soma =  0
while True:
    numero = int(input('Digite um numero: (999 para parar)'))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'{contador} números foram digitados e a soma entre eles foi {soma}.')