from random import shuffle
n1 = input('Primeiro aluno:')
n2 = input('Segundo aluno:')
n3 = input('Terceiro aluno:')
n4 = input('Quarto aluno:')
lista = [n1, n2, n3 ,n4]
print(' O ordem de apresentão será')
shuffle(lista)
print(lista)