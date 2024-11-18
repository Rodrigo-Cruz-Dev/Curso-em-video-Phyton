"""Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores M ou F. 
Caso esteja errado, peça a digitação 
novamente até ter um valor correto.
"""

sexo = input('Sexo: M / F: ').strip().upper()[0]
while sexo not in ('M', 'F'):
    print('Digite apenas M ou F')
    sexo = input('Sexo: M / F: ').strip().upper()
print(sexo)