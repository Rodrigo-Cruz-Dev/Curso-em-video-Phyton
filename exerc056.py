""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

from statistics import mean

nomes=[]
idades=[]
sexos=[]
nome_home_mais_velho = ''
maior_idade_homem = 0
mulheres_menos_de_20 = 0

for i in range(4):
    nome = str(input('Nome: '))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo M/F:')).strip().upper()

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

    if sexo == 'M' and idade> maior_idade_homem:
        maior_idade_homem = idade
        nome_home_mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_menos_de_20 +=1


print(nomes, idades, sexos)
print(f'Média das idades: {mean(idades)}')
print(f'Nome do homem mais velho é: {nome_home_mais_velho}.')
print(f'Quantidade de mulheres com menos de 20 anos é {mulheres_menos_de_20}')

