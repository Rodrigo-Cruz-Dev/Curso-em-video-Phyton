frase = str(input('Digite uma frase:')).upper().strip()
print('A frase possui {} letras A' .format(frase.count('A')))
print('A primeira letra A aparede na posição {} '. format(frase.find('A') + 1))
print('A ultima letra A aparece na posição {}' .format(frase.rfind('A') + 1 ))
