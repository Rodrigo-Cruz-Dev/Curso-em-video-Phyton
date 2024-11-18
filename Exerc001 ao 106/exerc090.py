"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""

dicionario = {'nome': 'aaa' , 'media': 0}
dicionario['nome']= input('Nome do aluno: ')
dicionario['media']= float(input('Media do aluno: '))
if dicionario['media'] >= 7:
    dicionario['situacao'] = 'Aprovado'
else:
    dicionario['situacao'] = 'Reprovado'

for key, value in dicionario.items():
    print(f'{key} é igual a {value}')