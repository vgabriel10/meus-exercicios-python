"""
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um Valor para [{linha},{coluna}]: '))
print('=-'*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
    print()



""" Minha Solução
x = 0
matiz = [[],[],[]]
for y in range(0,3):
    matiz[0].append(int(input(f'Digite um Valor para {x,y}: ')))
    if y == 2:
        for y in range(0,3):
            x = 1
            matiz[1].append(int(input(f'Digite um Valor para {x,y}: ')))
            if y == 2:
                for y in range(0,3):
                    x = 2
                    matiz[2].append(int(input(f'Digite um Valor para {x,y}')))
print('=-'*40)
for valor in matiz[0]:
    print(f'[{valor}]',end=' ')
print()
for valor in matiz[1]:
    print(f'[{valor}]',end=' ')
print()
for valor in matiz[2]:
    print(f'[{valor}]',end=' ')
print()
print('=-'*40)
"""