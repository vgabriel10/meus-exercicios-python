"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
def fatorial(f,show=False):
    """
    Uma função que calcula o fatorial de um Número
    
    :param f: É o número fatorial que foi passado
    :param show: Se for True ele mostra o calculo com o resultado, se for False ele só mostra apenas o resultado
    :return: Não Tem retorno
    """
    fatorial = 1
    for c in range(f,0,-1):
        fatorial *= c
        if show == True:
            for c in range(f,1,-1):
                print(f'{c} x ',end='')
                show = False
            print('1 = ',end='')
    print(f'{fatorial}')


fatorial(5,True)
print(help(fatorial))



