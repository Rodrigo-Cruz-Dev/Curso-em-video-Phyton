""" Crie um programa que leia duas notas de um aluno e calcule sua média,
 mostrando uma mensagem no final, de acordo com a média atingida:"""

nota1 = float(input('Digita a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Sua média foi de {media:.1f} \nParabens você foi aprovado')

elif media <= 6.9 and media > 5:
    print(f'Sua média foi de {media:.1f} \nReprovado \nVocê pode fazer a recuperação.')

else:
    print(f'Média {media} \nVocê foi reprovado')

