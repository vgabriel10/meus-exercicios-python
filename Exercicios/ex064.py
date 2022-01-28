"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

n = int(input('Digite um número [999 Para Parar]'))
soma = 0
quant_n = 0
while not n == 999:
    if n != 999:
        soma += n
        quant_n += 1
        n = int(input('Digite um número [999 Para Parar]'))
    elif n == 999:
        print('Fim do Programa')
print(f'Você Digitou {quant_n} Números ,a soma de todos os números foi de {soma}')
