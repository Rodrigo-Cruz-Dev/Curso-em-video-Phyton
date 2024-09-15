# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

"""expr = (input('Dig uma expressão: '))
p1 =  expr.count('(')
p2 = expr.count(')')
n = expr.find(')')
n1 = expr.find('(')

if n<n1 or p1 != p2:
    print('Expressão incorreta')
else:
    print('Expressão correta')
"""

def verifica_parenteses(expressao):
  """Verifica se os parênteses em uma expressão estão balanceados.

  Args:
    expressao: A expressão a ser verificada.

  Returns:
    True se os parênteses estiverem balanceados, False caso contrário.
  """

  pilha_de_parenteses = []  # Pilha para armazenar parênteses abertos

  for caractere in expressao:
    # Se encontrar um parêntese aberto, adiciona à pilha
    if caractere == '(':
      pilha_de_parenteses.append(caractere)

    # Se encontrar um parêntese fechado:
    elif caractere == ')':
      # Se a pilha estiver vazia, há um parêntese fechado a mais
      if not pilha_de_parenteses:
        return False

      # Remove o último parêntese aberto da pilha
      pilha_de_parenteses.pop()

  # Se a pilha estiver vazia ao final, todos os parênteses foram fechados corretamente
  return not pilha_de_parenteses

# Solicita a expressão ao usuário
expressao = input("Digite uma expressão: ")

# Chama a função para verificar os parênteses
if verifica_parenteses(expressao):
  print("Expressão correta")
else:
  print("Expressão incorreta")