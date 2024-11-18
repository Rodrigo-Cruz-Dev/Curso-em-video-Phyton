"""Crie um programa que faça 
o computador jogar Jokenpô com você."""

from random import choice

#Enfeite com vinte e cinco vezes o caracternome (ru) para facilitar o uso #
ru = (25 * '=')

#Escolha do jogador (esc_jog) , string com formatação ao final para input toda em maiuscula e sem espaços.#
esc_jog = str(input(f'{ru}\nEscolha! \nPedra \nPapel \nTesoura \n{ru} \nDigite: ')).upper().strip()

#Opções, lista para que possamos definir a opção random para a maquina escolher#
opcoes = ['PEDRA', 'PAPEL' ,'TESOURA'] 

#Escolha da maquina(esc_maq), com a função random que escolhera uma palavra da lista de forma aleatória#
esc_maq = choice(opcoes)

#Definindo novas variaveis com a escolha mas desta vez com a função upper e lower para o print não sair todo em maiusculo#
esc_jog_n = esc_jog.capitalize()
esc_maq_n = esc_maq.capitalize()

print(f'{ru} \nVocê escolheu: {esc_jog_n}. \nA maquina escolheu: {esc_maq_n}.\n{ru}')

if esc_jog == 'PEDRA' and esc_maq == 'TESOURA': 
    print('Pedra ganha de tesoura! \nParabéns você ganhou!')
elif esc_jog == 'PEDRA' and esc_maq == 'PAPEL':
    print('Pedra perde para papel! \nVocê perdeu!')
elif esc_jog == 'PEDRA' and esc_maq == 'PEDRA':
    print('Empatou!')
    
elif esc_jog == 'PAPEL' and esc_maq == 'PEDRA': 
    print('Papel ganha de pedra! \nParabéns você ganhou!')
elif esc_jog == 'PAPEL' and esc_maq == 'TESOURA':
    print('Papel perde para tesoura! \nVocê perdeu!')
elif esc_jog == 'PAPEL' and esc_maq == 'PAPEL':
    print('Empatou!')

elif esc_jog == 'TESOURA' and esc_maq == 'PAPEL': 
    print('Tesoura ganha de papel! \nParabéns você ganhou!')
elif esc_jog == 'TESOURA' and esc_maq == 'PEDRA':
    print('Tesoura perde para pedra! \nVocê perdeu!')
elif esc_jog == 'TESOURA' and esc_maq == 'TESOURA':
    print(f'Empatou!')
else:
    print('OPÇÃO INVALIDA!!!! \nDIGITE APENAS: PEDRA, PAPEL ou TESOURA!!!!!!')
print(f'{25 * '*'} \n{ru}')
