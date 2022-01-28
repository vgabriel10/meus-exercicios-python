"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep
def contador(i,f,p):
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        f += 1
    elif i > f:
        f -= 1
    for c in range(i,f,p):
        print(c, end=' ')
        sleep(1)
    print(end='FIM!')
    print()
    print('-='*20)


contador(1,10,1)
contador(10,0,-2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Digite o Inicio: '))
fim = int(input('Digite o Fim: '))
passo = int(input('Digite o Passo: '))
while passo == 0:
    print('O passo não pode ser 0, Digite outro valor')
    passo = int(input('Digite o Passo: '))
contador(inicio,fim,passo)
