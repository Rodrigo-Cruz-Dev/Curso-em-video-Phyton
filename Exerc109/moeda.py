
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
