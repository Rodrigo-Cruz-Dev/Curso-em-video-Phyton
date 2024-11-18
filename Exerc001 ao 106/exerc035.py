a = float(input('Digite a medida 1:'))
b = float(input('Digite a medida 2: '))
c = float(input('Digite a medida 3: '))

if a + b > c and a + c > b and b + c > a:
    print('As medidas informadas podem formar um triangulo')

else:
    print('As medidas informadas não podem formar um triangulo')