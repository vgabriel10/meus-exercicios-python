"""
 Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
 Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

"""     SE NÃO PASSAR NENHUM VALOR COMO PARÂMETRO ELE DA ERRO, PARA USAR ELE É BOM FAZER TRATAMENTO DE ERROS
def maior(*n):
    print('=='*30)
    print('Analisando Valores Recebidos...')
    print(f'{n} Ao todo foram informados {len(n)} Valores.')
    print(f'O maior Valor é o {max(n)}')
    print('==' * 40)


maior(5,4,7,10,6,4,1,2,3,73)
maior(10,100,3)
maior(7,7,5,2,3,4,1,4,10,100,200,500)
maior()
"""

def maior(*n):
    cont = maior = 0
    print('==' * 50)
    print('Analisando Valores Recebidos...')
    for valores in n:
        print(valores,end=' ')
        if cont == 0:
            maior = valores
        elif valores > maior:
            maior = valores
        cont += 1
    print()
    print(f'Ao todo foram informados {cont} valores')
    print(f'O maior Valor foi {maior}')
    print('==' * 50)


maior(5, 4, 7, 10, 6, 4, 1, 2, 3, 73)
maior(10, 100, 3)
maior(7, 7, 5, 2, 3, 4, 1, 4, 10, 100, 200, 500)
maior()