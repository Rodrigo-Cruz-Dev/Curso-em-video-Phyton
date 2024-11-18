import os
def arqexiste(nome):
    import os
    try:
        os.chdir(r"C:\Users\rococ\Desktop\Curso Data Science\Cursoemvideo\Curso-em-video-Phyton")
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com succeso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
            
def leiaint(msg):
    while True:
        try: 
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: Digite um numero valido')
        except(KeyboardInterrupt):
            print('Usuario interronpeu a digitação')
            return 0
        else:
            return n

def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):

    cabeçalho('MENU PRINCIPAL')
    for i, item in enumerate(lista):
        print(f'{i} - {item}')
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc

def cadastrar( arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados')
        else:
            print(f'Nova registro de {nome} adicionado')
            a.close()