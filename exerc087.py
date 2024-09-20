"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

import random
from time import sleep

def numeros_da_mega():
    numeros = list(range(1,60 +1))
    random.shuffle(numeros)
    return numeros[:6]

quant_de_jogos = int(input('Dig a quant de jogos que deseja gerar: '))
lista_composta = []
for jogo in range(quant_de_jogos):
    jogo = numeros_da_mega()
    lista_composta.append(jogo)
    
for jogo in lista_composta:
    jogo.sort()

print(lista_composta)

print('>>>GERADOR DE JOGOS DA MEGA<<')
for jogo in lista_composta:
    sleep(0.8)
    print(f'Jogo {lista_composta.index(jogo)+1}:')
    print(jogo)
    
