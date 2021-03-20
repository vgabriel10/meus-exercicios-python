"""
 Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
 – O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
"""

n1 = float(input('Digite o Primeiro Valor'))
n2 = float(input('Digite o Segundo Valor'))
if n1 > n2:
    print('O Primeiro Valor é o Maior')
elif n2 > n1:
    print('O Segundo Valor é o Maior')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')
