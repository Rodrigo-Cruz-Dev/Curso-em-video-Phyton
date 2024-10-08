from time import sleep
def contador_personal():
    print('Imprimindo de 0 a 10')
    numero1 = 11
    for i in range(1, numero1):
        sleep(0.3)
        print(i, end=' ', flush=True) 

    print('\nImprimindo de 10 a 0 pulando de 2 em 2')
    numero2= range(0,11,2)
    numero_invert = reversed(numero2)
    for i in numero_invert: 
        sleep(0.3)
        print(i, end=' ', flush=True)

    print('\nAgora é sua vez: ')
    num1 = int(input('Dig o num inicial: '))
    num2 = int(input('Dig o num final: ')) + 1
    interv= int(input('Dig o intervalo: '))

    if num1 > num2:
        contagem = range(num2-1, num1+1, interv)
        contagem = reversed(contagem)
    else:
        contagem = range(num1, num2, interv)

    for i in contagem: 
            sleep(0.3)
            print(i, end=' ', flush=True)


contador_personal()
