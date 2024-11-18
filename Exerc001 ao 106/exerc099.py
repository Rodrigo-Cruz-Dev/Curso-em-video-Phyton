"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

def maior_valor():
    maior = []
    while True:
        valor = input('Dig valor:')
        maior.append(valor)
        continuar = input('Deseja cont? S/N')
        if continuar in 'Nn':
            break
    print(f'Foram digitados {len(maior)} valores: {maior}')
    print(f'O maior valor é {max(maior)}')

