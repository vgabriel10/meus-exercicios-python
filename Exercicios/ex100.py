"""
 Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
 A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
 mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""

import random
números = []
def sorteia():
    print('5 Valores Sorteados da Lista: ',end=' ')
    for c in range(0,5):
        números.append(random.randint(0,9))
        print(números[c],end=' ')
    print('FIM!')
    somaPar(números)


def somaPar(lista_Numeros):
    pares = []
    for c in range(0,len(lista_Numeros)):
        if lista_Numeros[c] % 2 == 0:
            pares.append(lista_Numeros[c])
    soma_Numeros = sum(pares)
    print(f'Somando os Valores pares de {lista_Numeros}, Temos {soma_Numeros}')


sorteia()
