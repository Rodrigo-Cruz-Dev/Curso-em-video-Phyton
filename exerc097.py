"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável."""
def imprimir(texto):
    print( f'{'~' * (len(texto) + 2)} \n {texto}\n{'~' * (len(texto) + 2)}')


A = str(input('Dig texto: '))
imprimir(A)