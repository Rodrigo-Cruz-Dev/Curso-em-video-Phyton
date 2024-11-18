"""Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""
print('Programa para leitura da idade e o sexo.')
contador_maior_18 = 0
contador_homens = 0
contador_mulheres_menos_20 = 0
while True:
    idade = int(input('Idade: '))
    while idade not in range (0,150):
        idade = int(input('Idade: '))
    sexo = input('Sexo [M / F]').strip().upper()[0]
    while sexo not in ('M','F'):
        sexo = input('Sexo [M / F]').strip().upper()[0]

    if idade <= 18:
        contador_maior_18 +=1
    if sexo == 'M':
        contador_homens +=1
    if idade > 20 and sexo == 'F':
        contador_mulheres_menos_20 += 1

    continuar = input('Deseja continuar? [S / N ]: ').strip().upper()[0]
    while continuar not in ('S', 'N'):
        continuar = input('Deseja continuar? [S / N ]: ').strip().upper()[0]

    if continuar == 'N':
        break
    
print(f'Pessoas com mais de 18 anos: {contador_maior_18}')  
print(f'Quantidade de homens: {contador_homens}')  
print(f'Quantidade de mulheres com menos de 20 anos: {contador_mulheres_menos_20}')
print('Programa encerrado')