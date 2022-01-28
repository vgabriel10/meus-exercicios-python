"""
Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
"""
print('X-'*20)
print('Calculo de Fatorial')
print('X-'*20)
n = int(input('Digite um número '))
c = n
fatorial = 1    # Na multiplicação 1 é um número nulo pois o resultado é ele mesmo
while c > 0:
    print(c,end=' ')
    if c > 1:
        print('x',end=' ')
    else:
        print('=',end=' ')
    fatorial *= c
    c -= 1
print(fatorial)

