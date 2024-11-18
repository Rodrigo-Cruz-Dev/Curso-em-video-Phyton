
import moeda

v = float(input('Digite o valor do produto:'))
p = float(input('Digite a porcentagem de alteração:'))

print(f'Produto com aumento  de {p}% = {moeda.aumentar(v,p, True)}')
print(f'Produto com desconto de {p}% = {moeda.diminuir(v,p, True)}')
print(f'Produto com aumento de  100% = {moeda.dobro(v, True)}')
print(f'Produto com desconto de  50% = {moeda.metade(v, True)}')

