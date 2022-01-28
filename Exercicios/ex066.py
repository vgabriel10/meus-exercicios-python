"""
Crie um programa que leia vários números inteiros digitados pelo usuario e pare quando o usuario digitar
o flag [999] no final faça a soma entre eles desconsiderando o flag e mostre quantos números o usuario
digitou
"""

n = s = c = 0   # Outra forma de declarar varias variaveis com valor 0
while True:
    n = int(input('Digite um número [999] para parar '))
    if n == 999:
        break
    c += 1
    s +=n
print(f'Você digitou {c} números, a soma de todos eles é de {s}')
