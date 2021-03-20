"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

""" Pode ser feito dessa maneira

n1 = int(input('Digite um Valor'))
n2 = int(input('Digite Outro Valor'))
n3 = int(input('Digite Outro Valor'))
maior = max(n1,n2,n3)
menor = min(n1,n2,n3)
print(f'O maior numero é {maior}')
print(f'O menor Número é {menor}')
"""

#forma usando a estrutura de repetição
n1 = int(input('Digite um Valor'))
n2 = int(input('Digite Outro Valor'))
n3 = int(input('Digite Outro Valor'))
#verificando o menor valor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor valor foi {menor}')
#verificando o maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor foi {maior}')




