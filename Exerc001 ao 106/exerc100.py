"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""

def sorteia_e_soma_par():
    from random import shuffle
    num = list(range(1,101))
    shuffle(num)
    numeros = num[:5]
    soma = []
    for item in numeros:
        if item % 2 == 0:
            soma.append(item)
    print(f'Os numeros sorteados foram {numeros}.')
    print(f'O soma dos pares é {sum(soma)}')

sorteia_e_soma_par()

