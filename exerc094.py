"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""

dados = []

while True:
    dic = {}

    dic['nome'] = input('Nome: ')

    dic['sexo'] = input('Sexo [M / F]:').upper()[0]

    while dic['sexo'] not in 'MmFf':
        dic['sexo'] = input('Digite apenas M ou F \nSexo:').upper()
    
    while True:
        try:
            dic['idade'] = int(input('Idade: '))
            break
        except ValueError:
            print('Digite a idade apenas em números!')

    dados.append(dic)

    continuar = input('Deseja continuar [S / N]')
    if continuar in 'Nn':
        break

quant_pess = len(dados)
soma_das_idades = 0
mulheres = []
pessoas_aci_med = []


for usuario in dados:
    soma_das_idades += usuario['idade']

media_idade = soma_das_idades / quant_pess

for usuario in dados:
    if usuario['sexo'] == 'F':    
        mulheres.append(usuario['nome'])

    if usuario['idade'] > (media_idade):
        pessoas_aci_med.append(usuario['nome'])


print(f'Foram cadastradas {quant_pess} pessoas')
print(f'A média de idade é {media_idade}')
print('Mulheres cadastradas:')
for mulher in mulheres:
    print(f'>{mulher}')
print(f'Pessoas com idade acima da média: ')
for pessoa in pessoas_aci_med:
    print(f'>{pessoa}')


    

