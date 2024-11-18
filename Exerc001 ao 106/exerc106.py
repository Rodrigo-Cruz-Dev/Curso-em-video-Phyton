def func_de_help():
    
    print('MANUAL DE COMANDOS \n')
    while True:
        fun = input('Digite um comando ou função para acessar o manual: \n')
        print(f'\nAcessando o manual do comando {fun}: \n')
        print(help(fun))

    

func_de_help()