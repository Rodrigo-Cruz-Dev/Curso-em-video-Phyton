from random import randint
jog = int(input('Escolha: \n[0] pedra \n[1] papel \n[2] tesoura \n'))
comp = randint(0,2)
opcoes = ['Pedra', 'Papel', 'Tesoura']
vitorias = { 0 : 2, 1 : 0, 2 : 1}

if jog not in [0, 1, 2]:
    print('Digite apenas 0, 1 ou 2!')
else:
    print(f'Jogador escolheu {opcoes[jog]} e o computador escolheu {opcoes[comp]}.')
    
    if jog == comp:
        print('Empate')
    elif comp == vitorias.get(jog):
        print('Parabens você ganhou!')
    else:
        print('Você perdeu')
