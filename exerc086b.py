"""Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta."""

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz [linha][coluna] = int(input(f'Dig um valor para {linha},{coluna} '))
print(matriz)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

"""Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

soma_total_par = 0
for linha in matriz:
    for elemento in linha:
        if elemento %2 ==0:
            soma_total_par+=elemento
print(soma_total_par)

soma_terc = 0
for linha in matriz:
    soma_terc+=linha[2]
print(soma_terc)

maior_valor_seg_linha = max(matriz[1])
print(maior_valor_seg_linha)
