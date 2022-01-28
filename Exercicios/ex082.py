"""
 Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras
 que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o
 conteúdo das três listas geradas.
"""

lista_Numeros = []
numeros_Par = []
numeros_Impar = []
while True:
    numero = int(input('Digite um Numero: '))
    lista_Numeros.append(numero)
    if numero % 2 == 0:
        numeros_Par.append(numero)
    else:
        numeros_Impar.append(numero)
    continuar = str(input('Quer Continuar ? [S/N] '))
    while not continuar in 'nNsS':
        print('Valor Invalido, Digite Novamente!')
        continuar = str(input('Quer Continuar ? [S/N] '))
    if continuar in 'nN':
        break
print(f'A lista de completa é {lista_Numeros}')
print(f'A lista de pares é {numeros_Par}')
print(f'A lista de Impares é {numeros_Impar}')