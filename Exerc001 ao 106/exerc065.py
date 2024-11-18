"""Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

parar = 0
lista_dos_numeros = []

while parar != 'N':
    numero_do_usuario = int(input('Informe um número: '))
    parar = input('Deseja inserir mais números? S/N: ').upper().strip()[0]

    lista_dos_numeros.append(numero_do_usuario)

print(f'O maior número foi: {max(lista_dos_numeros)} ')
print(f'O menor número foi: {min(lista_dos_numeros)}')
print(f'A média dos números foi: {sum(lista_dos_numeros) / len(lista_dos_numeros):.2f}')

