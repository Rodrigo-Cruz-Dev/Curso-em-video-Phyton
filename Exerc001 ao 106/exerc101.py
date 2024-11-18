""" Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""
def vota(nasc):
    from datetime import datetime
    ano = (datetime.today()).year
    idade = ano - nasc
    if idade <=16 or idade >65:
        return f'Idade: {idade}, Voto opcional.'
    elif idade in range(0,16):
        return f'Idade: {idade}, Não vota.'    
    else:   
        return f'Idade: {idade}, Voto obrigatório.'
    

nasc = int(input('Dig ano: '))
print(vota(nasc))