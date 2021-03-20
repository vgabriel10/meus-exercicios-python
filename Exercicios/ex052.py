"""
 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
n = int(input('Digite um número'))
divisiveis = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[0:31m',end='')  # Todos os números divisiveis são vermelho
        divisiveis += 1
    else:                           # Todos os números que não são divisiveis são Ciano
        print('\033[0:36m',end='')
    print(c, end=' ')
if divisiveis == 2:
    print('\n\033[m O número é primo')
else:
    print('\n\033[m O número NÃO é primo')


