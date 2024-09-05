"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

valor_casa = float(input('Informe o valor do ímovel:'))
renda = float(input('Informe o valor da renda:'))
anos = int(input('Informe quantos anos a pagar:'))

quant_parcelas = anos * 12
valor_parcela = valor_casa / quant_parcelas
salario_30 = renda * 0.30

if salario_30 >= valor_parcela :
    print('O emprestimo foi aprovado e o valor das parcelas é igual {:.2f} de {:.2f}'.format(quant_parcelas, valor_parcela))

elif salario_30 < valor_parcela:
    print('O emprestimo foi reprovado pois o valor das {} parcelas é de {} e excede 30% do seu salario que é {}'.format(quant_parcelas, valor_parcela , salario_30))
