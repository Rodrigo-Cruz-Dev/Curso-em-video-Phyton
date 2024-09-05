""" Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade 
e quantas já são maiores."""

maior = 0
menor = 0

for c in range(7):
    idade = int(input('Digite a idade:'))
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f'{maior} pessoa{'s' if maior > 1 else ''} {'são' if maior > 1 else 'é'} maior{'es' if maior> 1 else ''} de idade.')
print(f'{menor} pessoa{'s' if menor > 1 else ''} {'são' if menor > 1 else 'é'} menor{'es' if menor> 1 else ''} de idade.')
