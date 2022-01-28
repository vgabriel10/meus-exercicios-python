"""
: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
 valor digitado e as suas respectivas posições na lista.
"""
numero = []
maior = 0
menor = 0
for c in range(0,5):
    numero.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        maior = menor = numero[c]
    else:
        if numero[c] > maior:
            maior = numero[c]
        if numero[c] < menor:
            menor = numero[c]

print(f'O maior valor digitado foi {maior} nas posições ',end='')
for pos, valores in enumerate(numero):
    if numero[pos] == maior:
        print(f'{pos}...',end='')
print(f'\n O menor valor digitado foi {menor} nas posições ',end='')
for pos, valores in enumerate(numero):
    if numero[pos] == menor:
        print(f'{pos}...',end='')
