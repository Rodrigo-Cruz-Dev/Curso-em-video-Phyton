"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular."""
tupla = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 10.00)
for item in tupla:
    if type(item) is str:
        print(f'{item:.<30}', end='')
    else:
        print(f'R${item:>5.2f}')

for i in range(0,len(tupla),2):
    print(f'{tupla[i]:.<25}R${tupla[i+1]:>5.2f}')