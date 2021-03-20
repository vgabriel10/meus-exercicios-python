"""Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
  O programa deverá escrever na tela se o usuário venceu ou perdeu."""

import random
n = random.randint(0,5)
print('Tente acertar o número que eu estou pensando ')
print('')
resp = int(input('Digite um Número de 1 à 5'))
print('O número em que eu estava pensando era {}'.format(n))
if resp == n:
    print('Parabéns Você acertou')
else:
    print('Ops... Você acabou errando e eu Venci HAHAHA')


