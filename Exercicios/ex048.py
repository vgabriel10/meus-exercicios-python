"""
Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
print('=-'* 20)
print('Multiplos de 3 que são impares de 1 à 500')
print('=-'* 20)
soma = 0
quant_valores = 0
for c in range(3,501,3):
    if c % 2 == 1:
        quant_valores += 1
        soma += c
print(f'A quantidade de valores solicitados foi de {quant_valores}')
print(f'A soma dos multiplos de três que são impares no intervalo de 1 até 500 é {soma}')