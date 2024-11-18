""" Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""
vogais = 'aeiou'
tupla = ('crie', 'um', 'programa', 'que', 'tenha', 'uma', 'tupla', 'com', 'varias', 'palavras')
for palavra in tupla:
    print(f'\nNa palavra {palavra}, temos a letras:', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
