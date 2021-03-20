"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

import time
import random
print('''
Suas Opções
[0] Pedra
[1] Papel
[2] Tesoura
''')
            # Minhas Opções
jogador = int(input('Qual a Sua Opção ?'))
time.sleep(2)
print('JO')
time.sleep(2)
print('KEN')
time.sleep(2)
print('PO!!!!')
if jogador == 0:
    print('Você Escolheu Pedra')
elif jogador == 1:
    print('Você Escolheu Papel')
elif jogador == 2:
    print('Você Escolheu Tesoura')
else:
    print('Opção invalida, Procure ler Atentamente!')
        # Opções do computador
computador = random.randint(0,2)
if computador == 0:
    print('O computador Escolheu Pedra!')
elif computador == 1:
    print('O computador Escolheu Papel')
elif computador == 2:
    print('O computador Escolheu Tesoura')
        # Ver Quem Ganhou
if jogador == computador:
    print('Empate')
elif jogador == 0 and computador == 1:          # 0 - pedra
    print('Computador Ganhou')                  # 1 - papel
elif jogador == 0 and computador == 2:          # 2 - tesoura
    print('Jogador Ganhou')
elif jogador == 1 and computador == 0:
    print('Jogador Ganhou')
elif jogador == 1 and computador == 2:
    print('Computador Ganhou')
elif jogador == 2 and computador == 0:
    print('Computador Ganhou')
elif jogador == 2 and computador == 1:
    print('Jogador Ganhou')

            #Terminei

        #Otimizações
"""
inves de criar estrutura de repetição para saber se é pedra, papel ou tesoura eu poderia ter feito uma lista
EX:
opção = int(input('''
Opções
[0] Pedra
[1] Papel
[2] Tesoura ''')
itens = ('pedra','papel','tesoura')
if opção == 0
    print('Você escolheu o item {}'.format(itens[opção])


"""