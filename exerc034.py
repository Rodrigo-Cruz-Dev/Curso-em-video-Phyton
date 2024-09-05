salario = float(input('Informe o valor de salario: '))
if salario > 1250:
    aumento = salario / 100 * 10
else:
    aumento = salario / 100 * 15

print('O valor do aumento é de {:.2f},seu salario novo é {:.2f}'.format(aumento, (salario+aumento)))
    