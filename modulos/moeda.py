import locale

def aumentar(v,p):
    valor = v + ( p/100) * v
    return valor

def diminuir(v,p):
    valor = v - ( p/100 * v)
    return valor

def dobro(v):
    valor = v * 2
    return valor

def metade(v):
    valor = v /2
    return valor

def moeda(v=0):
    return f'R${v:.2f}'.replace('.', ',')
