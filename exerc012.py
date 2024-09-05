preço = float(input('Digite o preço do produto: R$'))
desconto = preço / 100 * 5
valor = preço - desconto 
print('O preço com o desconto de 5% é R${}.'.format(valor))