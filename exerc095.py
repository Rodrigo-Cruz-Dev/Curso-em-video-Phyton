jogadores = []
while True:

    dados = {}

    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))

    lista = []

    for i in range(partidas):
        gol= int(input(f'Quantos gols na partida {i+1} ?'))
        lista.append(gol)

    dados['gols'] = lista
    dados['total'] = sum(lista)

    jogadores.append(dados)

    continuar = input('Deseja continuar? [s/n]').upper()[0]
    if continuar in 'N':    
        break

print(f'{'=-'*30} \n{'COD':<3} {'NOME':<20} {'GOLS':<20} {'TOTAL':>} \n{'=-'*30}')
for i, item in enumerate(jogadores):
    print(f'{i:<3} {item['nome']:<20} {str(item['gols']):<20} {item['total']:>} \n{'--' *30}')
print(f'{'=-'*30}')

print(jogadores)

while True:
    codigo = int(input(f'Informe o código do jogador que desejar ver separadamente: '))
    
    gol_do_jog =  jogadores[codigo]
    print(f'{'=-'*30} \nDados do jogador {(gol_do_jog['nome']).upper()}:')
    for i, item in enumerate(gol_do_jog['gols']):
        print(f'Na partida {i+1} o {gol_do_jog['nome']} fez {item} gol(s).')

    print(f'{'=-'*30}')
    continuarr = input('continuar? [S/N]: ' ).upper()[0]
    if continuarr == 'N':
        break 
print('Encerrando programa')

    
    