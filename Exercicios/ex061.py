"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
termo1 = int(input('Digite o primeiro Termo: '))
razão = int(input('Digite a razão: '))
c = 10
while c > 0:
    c -= 1
    print(termo1, '!', end=' ')
    termo1 += razão
print('Fim do Programa')


