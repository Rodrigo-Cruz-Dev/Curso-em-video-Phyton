"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação (opcional)"""


def notas():
    turma = []
    while True:
        
        aluno = input('Nome:')
        nota = []
        while True:
            n = int(input('Nota:'))
            nota.append(n)  
            continuar = input('Deseja lançar mais NOTAS? S/N: ').upper()[0]
            if continuar == 'N':    
                break
        média = sum(nota) / len(nota)
        maior = max(nota)
        menor = min(nota)
        if média >= 7:
            situação = 'Aprovado'
        else:
            situação = 'Reprovado'
            
        dicionario = {'aluno': aluno, 'notas':nota,'maior': maior,'menor': menor, 'média': média, 'situação': situação }
        
        turma.append(dicionario)

        continuar2 = input('Deseja lançar outro ALUNO? S/N: ').upper()[0]
        if continuar2 == 'N':
            break
    maiores_notas = []
    menores_notas = []
    media_da_turma = []
    
    print(' \nNOTAS E MÉDIA DOS ALUNOS \n')
    
    for aluno in turma: 
         
        print(f'Aluno: {aluno['aluno']}, Notas: {aluno['notas']} Maior nota: {aluno['maior']}, Menor nota: {aluno['menor']}, Situação: {aluno['situação']}')
        maiores_notas.append(aluno['maior'])
        menores_notas.append(aluno['menor'])
        media_da_turma.append(aluno['média'])

    
    print(f' \nA maior nota: {max(maiores_notas)}')
    print(f'A menor nota: {min(menores_notas)}')    
    print(f'A média da turma: {sum(media_da_turma)  / len(media_da_turma)} \n ')

notas()
