largura= float(input('Informe a largura:'))
altura = float(input('Informa a altura:'))
area = largura * altura
resposta = area / 2
print('A parede tem uma area de {}m² e você vai gastar {:.2f}litros de tinta.'.format(area, resposta))
