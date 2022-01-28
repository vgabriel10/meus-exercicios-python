"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
 OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print('=-'*20)
print('Banco do Brasil')
print('=-'*20)
sacar = int(input('Digite quanto você quer Sacar em R$ ?'))
ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0
while sacar <= 0:
    print(f'Impossivel Sacar {sacar} R$, Digite Novamente!')
    sacar = int(input('Digite quanto você quer Sacar em R$ ?'))
while True:
    if sacar >= 50:
        sacar -=50
        ced50 += 1
    elif sacar >= 20:
        sacar -= 20
        ced20 += 1
    elif sacar >= 10:
        sacar -= 10
        ced10 += 1
    else:
        sacar -= 1
        ced1 += 1
    if sacar == 0:
        break
print(f'Total de {ced50} cedulas de 50 R$')
print(f'Total de {ced20} de cedulas de 20 R$ ')
print(f'Total de {ced10} cedula de 10 R$ ')
print(f'Total de {ced1} cedula de 1 R$')
print('=-'*20)
print('Volte Sempre para o Banco do Brasil!')
print('=-'*20)