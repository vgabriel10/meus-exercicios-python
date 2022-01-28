from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'pessoas.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado com Sucesso')
else:
    criarArquivo(arq)

menu()
while True:
    try:
        opçao = int(input('Sua Opção: '))
    except(TypeError, ValueError):
        print('\033[31m ERRO: por favor, Digite um número inteiro valido!\033[m')
    except KeyboardInterrupt:
        print('\033[31m Erro, Nenhum Valor foi Informado! \033[m')
    else:
        if opçao == 1:
            lerArquivo(arq)
            menu()
        elif opçao == 2:
            cadastrarPessoas(arq)
            menu()
        elif opçao == 3:
            sair()
        else:
            print('\033[31m ERRO,Digite uma opção de 1 até 3 \033[m')