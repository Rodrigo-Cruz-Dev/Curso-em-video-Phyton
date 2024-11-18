"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão."""

pri_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão: '))

for c in range (10):
    termos = pri_termo + c * razao
    print(termos, end=' ')

