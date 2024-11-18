"""Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

ano_atual = date.today().year
ano = int(input('informe o ano de nascimento: '))
idade = ano_atual - ano
if idade > 19:
    print(f'Idade de {idade} anos. Já deve ter se alistado em {ano_atual - (idade - 18)}.')
elif idade < 18:
    print(f'ainda faltam {18 - idade} ano(s) para voce se alistar. Você deve se apresentar em {ano_atual + (18 - idade)}.')
else:
    print('Voce tem 18 anos e deve se alistar neste ano.')


