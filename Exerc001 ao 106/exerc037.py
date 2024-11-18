"""Escreva um programa em Python que leia um número inteiro qualquer 
e peça para o usuário escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal."""

numero_inteiro = int(input('Digite um número inteiro:'))
escolha = int(input('Escolha: \n1 para binário \n2 para octal  \n3 para hexadecimal: '))

if escolha == 1:
    print(f' O número {numero_inteiro} convertido para binario é {bin(numero_inteiro)[2:]}')
elif escolha == 2:
    print(f'O numero {numero_inteiro} convertido em octal é {oct(numero_inteiro)[2:]}')
elif escolha == 3:
    print(f'O numero {numero_inteiro} convertido em hexadecimal é {hex(numero_inteiro)[2:]}')
else:
    print('Opção invalidade, digite apenas 1,2 ou 3')

