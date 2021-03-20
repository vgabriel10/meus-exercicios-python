"""
 Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
  que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
print('=-'*20)
print('SOMA DOS PARES')
print('=-'*20)
soma = 0
for c in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares foi de {soma}')