
def aumentar(v=0, p=0, formato=False):
    valor = v + ( p/100) * v
    return valor if formato is False else moeda(valor)

def diminuir(v=0, p=0, formato=False):
    valor = v - ( p/100 * v)
    return valor if formato is False else moeda(valor)


def dobro(v=0, formato=False):
    valor = v * 2
    return valor if formato is False else moeda(valor)


def metade(v=0,formato=False):
    valor = v /2
    return valor if formato is False else moeda(valor)


def moeda(v=0):
    return f'R${v:.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxad=5):
    print('*' * 30)
    print('Resumo do valor'.center(30))
    print('*' * 30)
    print(f'Preço analisado:             \t{moeda(preço)}')
    print(f'Valor com aumento de  {taxaa}%: \t{aumentar(preço, taxaa, formato=True)}')
    print(f'Valor com desconto de {taxad}%: \t{diminuir(preço,taxad,formato=True)}')
    print('*' * 30)