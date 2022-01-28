"""
 Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
"""
termo = int(input('Quantos Termos Você quer mostrar ?'))
# O contador ira começar com 3 porque eu já imprimir o [0] e o [1] antes de começar a estrutura
cont = 3
t1 = 0
t2 = 1
print(t1,' - ',t2,end=' - ')
while cont <= termo:
    t3 = t1 + t2
    print(t3,end=' - ')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim do Programa')
