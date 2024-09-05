import math
catop = float(input('Comprimento do cateto oposto:'))
catad = float(input('Comprimento do cateto adjacente:'))
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(catop, catad)))