n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n = (n1 + n2) / 2
print('Sua média é {:.1f}'.format(n))
if n >= 6:
    print('Parabens!')
else:
    print( 'Estude mais!')

print( 'Parabens!!' if n>=6 else 'Estude mais!!')