"""Elabore um programa que calcule 
o valor a ser pago por um produto, 
considerando o seu preço normal 
e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal 
3x ou mais no cartão: 20% de juros"""

valor_prod = float(input('Informe o valor de produto: '))
forma_de_pagamento = int(input('Escolha uma forma de pagamento: \nPara dinheiro digite 0 \nCartão a vista digite 1 \nParcelado até 2x digite 2 \nParcelado em 3x ou mais digite 3 \nOpção escolhida: ' ))
dinheiro = valor_prod - (valor_prod * 0.10)
vista_cart = valor_prod - (valor_prod * 0.05)
cart_2x = valor_prod 
cart_3x = valor_prod + (valor_prod * 0.20)

if forma_de_pagamento == 0:
    print(f'O valor do produto é {valor_prod} e com desconto fica por {dinheiro}')
elif forma_de_pagamento == 1:
    print(f'O valor do produto é {valor_prod} e com desconto fica por {vista_cart}.')
elif forma_de_pagamento == 2:
    print(f'O valor do produto é {valor_prod}')
else:
    print(f'O valor do produto é {cart_3x}')
