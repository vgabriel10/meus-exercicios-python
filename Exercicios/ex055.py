"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""

lista = []
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}° Pessoa '))
    lista += [peso]
maior = max(lista)
menor = min(lista)
print(lista)
print(f'O maior peso foi {maior}')
print(f'O menor peso foi {menor}')





