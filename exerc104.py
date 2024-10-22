"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')"""

def leiaint():
    n = input('Digite um n:')
    while not n.isnumeric():
        print('Dig apenas numeros')
        n = input('Digite um n:')
    print(f'Vc dig o num {n}')
       

leiaint()