"""
 Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

valor1 = float(input('Digite o primeiro Valor '))
valor2 = float(input('Digite o segundo Valor '))
opção = 0
soma = 0
maior = 0
multiplicar = 0
while not opção == 5:
    opção = int(input('''
    Digite a sua Opção
    [ 1 ] somar

    [ 2 ] multiplicar

    [ 3 ] maior

    [ 4 ] novos números

    [ 5 ] sair do programa
    '''))
    if opção == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} é igual a {soma}')
        print('='*30)
    elif opção == 2:
        multiplicar = valor1 * valor2
        print(f'A multiplicação entre {valor1} e {valor2} é igual a {multiplicar}')
        print('=' * 30)
    elif opção == 3:
        maior = max(valor1,valor2)
        print(f'O maior valor entre {valor1} e {valor2} é {maior}')
        print('=' * 30)
    elif opção == 4:
        valor1 = float(input('Digite um novo valor '))
        valor2 = float(input('Digite outro novo valor'))
        print('=' * 30)
    elif opção > 5:
        print('Opção invalida, por favor digite novamente')
        print('=' * 30)
print('*'*20)
print('Programa Finalizado')
print('*'*20)


