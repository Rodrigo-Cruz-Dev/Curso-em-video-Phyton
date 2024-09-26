"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""

from random import randint
print('==Jogo de dados==')
dados = {}
for jog in range(4):
    dados[jog] = randint(1,6)

for k , v in dados.items():
    print(f'Jogador {k+1} tirou {v} no dado.')

tupla = sorted(dados.items(), key=lambda item: item[1], reverse=True)
dados_ordenados = dict(tupla)

print('==RANKING DOS JOGADORES==')
for k, v in dados_ordenados.items():
    print(f'{k+1}º Lugar: Jogador {k+1} com {v}. ')


