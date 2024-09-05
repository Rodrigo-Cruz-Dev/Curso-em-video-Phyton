nome = str(input('Digite o seu nome completo:')).strip()
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
primeiro_nome = nome.split()[0]
print('Seu primeiro nome tem {} letras'.format(len(primeiro_nome)))
