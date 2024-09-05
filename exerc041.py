""" Confederação Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta 
e mostre sua categoria, de acordo com a idade: 
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER"""

from datetime import date
ano = int(input('Informe o ano do nascimento: '))
idade = date.today().year - ano

if idade    <= 9:
    print(f'Sua idade é {idade}, sua é categoria é a: \nMIRIM')
elif idade <= 14:
    print(f'Sua idade é {idade} e sua categoria é a: \nINFANTIL')
elif idade <= 19:
    print(f'Sua idade é {idade} e sua categoria é a: \nJÚNIOR')
elif idade  <=25:
    print(f'Sua idade é {idade} e sua categoria é a:\nSENIOR')
else:
    print(f'Sua idade é {idade} e sua categoria é a: \nMASTER') 