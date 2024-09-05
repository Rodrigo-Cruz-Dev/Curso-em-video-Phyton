"""Crie um programa que leia uma frase qualquer 
e diga se ela é um palíndromo, 
desconsiderando os espaços. Exemplos de palíndromos:"""


texto = str(input('frase: '))
frase = texto.strip().upper().replace(' ','')
contrario = frase [:: -1]
contrario1 = texto [:: -1]
if frase == contrario:
    print(f'A frase: \n{texto} \né um palimdromo com \n{contrario1}')
else:
    print(f'A frase: {texto} \nnão é um palimdromo com \n{contrario1}')

