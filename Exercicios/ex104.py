"""
 Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
 só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""


def leiaInt(texto):
    numero = input(texto)
    while True:
        if numero.isnumeric() == True:
            global n
            n = int(numero)
            return n
        else:
            print('\033[31m ERRO, DIGITE UM NÚMERO INTEIRO VALIDO \033[m')
            numero = input(texto)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

