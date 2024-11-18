""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""

notas = []
nota_aluno = []
while True:
    nome = nota_aluno.append(str(input('Nome: ')))
    nota1 = nota_aluno.append(int(input('Nota 1:')))
    nota2 = nota_aluno.append(int(input('Nota 2: ')))
    notas.append(nota_aluno[:])
    nota_aluno.clear()

    continuar = str(input('Deseja continuar [S/N]'))[0]
    if continuar in 'Nn':
        break

for aluno in notas:
        matricula = notas.index(aluno)
        nome = aluno[0]
        nota1 = aluno[1]
        nota2 = aluno[2]
        media = (nota1+nota2)/2
        print('*'*30)
        print(f'Aluno {nome} | Matricula numero: {matricula}')
        print(f'Nota 1: {nota1}')
        print(f'Nota 2: {nota2}')
        print(f'Média: {media}')
        print('*'*30)
boletim_individual = input('Deseja mostrar o boletim individual? [S / N]')[0]
if boletim_individual in 'Ss':
    escolha_matricu = int(input('Digite Matricula: '))
    print(f'Aluno: {nome}\nNota 1: {nota1}\nNota 2: {nota2}\nMédia:{media}')
else:
     print('Encerrado')
    