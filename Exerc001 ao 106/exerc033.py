num1 = int(input('digite um numero:'))
num2 = int(input('digite outro numero:'))
num3 = int(input('digite outro numero:'))
if num1 > num2 and num1 > num3:
    print(f'O maior número é:{num1}')

if num2 > num1 and num2 > num3:
    print(f'O maior número é:{num2}') 

if num3 > num1 and num3 > num2:
    print(f'O maior número é:{num3}')
    
if num1 < num2 and num1 < num3:
    print(f'O menor número é:{num1}')

if num2 < num1 and num2 < num3:
    print(f'O menor número é:{num2}')

if num3 < num1 and num3 < num2:
    print(f'O menor número é:{num3}')
                