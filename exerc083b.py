# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = str(input('Digite uma expressão: '))

pilha = []

for caracter in expressao:
    if caracter == '(':
        pilha.append('(')

    elif caracter == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão correta')
else:
    print('Expressão incorreta')
