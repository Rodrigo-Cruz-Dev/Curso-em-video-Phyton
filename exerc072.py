# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ("zero","um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")


while True:
    opcao = int(input('Digite um numero de zero a vinte: '))
    if 0<= opcao <=20:
        print(f'Você digitou o número {numeros[opcao]}.')
        continuar = input('Continuar? S/N: ').strip().upper()
        if continuar == "N":
            break
    else:
        print('Numero invalido')
print('Programa encerrado')

    

    


    




