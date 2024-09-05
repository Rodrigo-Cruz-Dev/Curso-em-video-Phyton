""" Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""

def enfeit():
    print('==' * 40)
produtos = []
preços = []
contador = 0
while True:
    enfeit()
    produto = input('Nome do produto: ')
    preço = int(input('Preço: '))
    produtos.append(produto)
    preços.append(preço)
    if preço > 1000:
        contador +=1
    enfeit()
    continuar = input('Deseja continuar? [S / N]: ').strip().upper()[0]
    if continuar == 'N':
        break
enfeit()
print(f'A) Total gasto na compra: R${sum(preços)}.')
print(f'B) Quantidade de produtos que custam mais de R$1000: {contador}.')
print(f'C) Produto mais barato: {produtos[preços.index(min(preços))]}.' )
enfeit()
