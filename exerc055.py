"""Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos."""

pesos=[]
for c in range (1,8):
    peso = float(input(f'informe o peso do dia {c}:'))
    pesos.append(peso)
    
menor = min(pesos)
maior = max(pesos)
print(f'O maior peso foi de {maior}Kg. \nO menor peso foi de {menor}Kg' )