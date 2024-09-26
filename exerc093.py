"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

dados = {}

dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))
lista = []

for i in range(partidas):
    gol= int(input(f'Quantos gols na partida {i+1} ?'))
    lista.append(gol)

dados['gols'] = lista
dados['total'] = sum(lista)
print('-=' *30)
print(dados)
print('-=' *30)
for k , v in dados.items():
    print(f' O campo {k} tem o valor {v}.')
print('-=' *30)

print(f'O jogador {dados["nome"]} jogou {partidas} partidas')
for i, item in enumerate(lista):
    print(f'Na partida {i+1}, fez {item} gols.')
print(f'Foi um total de {dados['total']} gols')