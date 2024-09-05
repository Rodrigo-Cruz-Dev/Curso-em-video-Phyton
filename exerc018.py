import math
ang1 = float(input('Digite o angulo que você deseja:'))
ang2 = math.radians(ang1)
print('O angulo de {} tem o SENO de {}'.format(ang1, math.sin(ang2)))
print('O angulo de {} tem o COSSENO de {}'.format(ang1, math.cos(ang2)))
print('O angulo de {} tem a TANGENTE de {}'.format(ang1, math.tan(ang2)))