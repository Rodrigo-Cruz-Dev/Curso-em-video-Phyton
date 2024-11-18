#Aula 17

num = [2,5,9,1,]
print(num)
num[2] = 3 
num.append(7)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2,2)
print(num)
#num.pop(2)
print(num)
num.remove(2)
print(num)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for chave, itens in enumerate(valores):
    print(f'Na posicao {chave} encontro o valor {itens}')
