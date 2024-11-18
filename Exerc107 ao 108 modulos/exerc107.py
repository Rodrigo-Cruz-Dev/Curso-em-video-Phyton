
import moeda

v = float(input('Digite o valor do produto:'))
p = float(input('Digite a porcentagem de alteração:'))

print(f'Produto com aumento  de {p}% = {moeda.moeda(moeda.aumentar(v,p))}')
print(f'Produto com desconto de {p}% = {moeda.moeda(moeda.diminuir(v,p))}')
print(f'Produto com aumento de  100% = {moeda.moeda(moeda.dobro(v))}')
print(f'Produto com desconto de  50% = {moeda.moeda(moeda.metade(v))}')

