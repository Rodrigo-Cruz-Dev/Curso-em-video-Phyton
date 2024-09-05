"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
n = int(input(f'{'=' * 40}\nTente a adivinhar um numero de 1 a 10. \nDigite um numero de 1 a 10:'))
while n not in range(1,11):
    n = int(input('Digite apenas de 1 a 10: '))

m = randint(1,10)
contador = 1

while n != m:
    n = int(input('Você errou! Tente outra vez \nDigite um numero de 1 a 10: '))
    while n not in range(1,10):
        n = int(input('Digite apenas de 1 a 10: '))
    contador += 1

print(f'{'=' * 40} \nVocê escolheu o número {n}. \nO número sorteado foi {m}. \nParabens! Você acertou com {contador} tentativas! \n{'=' * 40}')
