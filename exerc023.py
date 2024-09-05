numero = input('Digite um número:')
numero = numero.zfill(4)
Unidade = numero[3]
Dezena = numero[2]
Centena = numero[1]
Milhar = numero[0]
print(f'Unidade:{Unidade} \nDezena:{Dezena} \nCentena:{Centena} \nMilhar:{Milhar}')