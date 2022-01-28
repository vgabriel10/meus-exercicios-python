"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPares = 0
soma_Terceira_Coluna = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite o Valor em [{linha},{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
        soma_Terceira_Coluna += matriz[linha][2]
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end=' ')
    print()
print(f'A soma de todos os valores pares foi de {somaPares}')
print(f'A soma de todos os valores da terceira coluna é de {soma_Terceira_Coluna}')
print(f'O maior valor da Segunda linha é {max(matriz[1])}')