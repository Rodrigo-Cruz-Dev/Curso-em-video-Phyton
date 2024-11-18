from utilidades import linha, cabeçalho,menu, lerArquivo,criarArquivo,arqexiste, leiaint, cadastrar

arq = 'dados.txt' 

if not arqexiste(arq):
    criarArquivo(arq)

cabeçalho('SISTEMA DE CADASTRO')
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resposta == 0:
        #opção de listar o conteudo de um arquivo
        lerArquivo(arq)
        
    elif resposta == 1:
        cabeçalho('NOVO CADATRO')
        nome = str(input('Nome:'))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        print('Saindo do sistema')
        break
    else: 
        print('ERRO: Digite uma opção valida')