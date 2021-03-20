"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
 escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""


n = int(input('Digite um número inteiro'))
print('[1] Binario')
print('[2] Octal')
print('[3] Hexadecimal')
opção = int(input('Digite a sua jogador'))
if opção == 1:
    conversão = bin(n)     #Não precisa transforamr em STR para fazer o fatiamento, eu que me confundir.
    valor = str(conversão)
    print(valor[2:]) #O primeiro parametro é onde começa depois onde termina e depois os Passos.
elif opção == 2:
    conversão = oct(n)
    valor = str(conversão)
    print(valor[2:])
elif opção == 3:
    conversão = hex(n)
    valor = str(conversão)
    print(valor[2:])
else:
    print('Você Digitou um Valor invalido')

"""
Eu também podia ter feito dessa maneira que é muito mais facil

n = int(input('Digite um número inteiro'))
print('O número {} em binario é {}'.format(n,bin(n)[2:]))

"""



