def leiaint():
    while True:
        try:
            n= int(input('Digite um numero inteiro: '))
            return n
            
        except ValueError :
            print('Digite um número válido')
def leiafloat():
    
    while True:
        try: 
            n = float(input('Digite um número flutuante(decimal, ex: 7.4):'))
            return n
            
        except ValueError:  
            print('Digite um número válido')


n = leiaint()
print(f'Voce digitou o número {n}.')