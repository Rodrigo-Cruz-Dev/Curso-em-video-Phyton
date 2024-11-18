"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import datetime

dados = {}
ano = (datetime.today()).year

dados['Nome'] = str(input('Nome:'))
dados['Ano de nascimento'] = int(input('Ano de nascimento: '))

dados['Nº da carteira de trabalho'] = int(input('Nº da carteira de trabalho (0 não possui:): '))
if dados['Nº da carteira de trabalho'] > 0:
    dados['Ano da primeira contratação'] = int(input('Ano do contratação:'))
    dados['Salario'] = int(input('Salario: '))
    dados['Idade atual'] = ano - dados['Ano de nascimento']
    dados['Ano da aposentadoria'] = dados['Ano da primeira contratação'] + 30
    dados['Idade para a aposentadoria'] = (dados['Ano da aposentadoria'] - ano) + dados['Idade atual']
    print()
    for k, v in dados.items():
        print(f'{k}: {v}')
    print()
else:
    print('Usuario sem carteira')
