"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
# BIBLIOTECA PARA ORDENAR OS DICIONÁRIOS
from operator import itemgetter
#######################################
jogadores = {'Jogador1':randint(1,6),'Jogador2':randint(1,6),'Jogador3':randint(1,6),'Jogador4':randint(1,6)}
print('Valores Sorteados: ')
for play,dado in jogadores.items():
    print(f'{play} jogou {dado} no dado')
    sleep(1)
print('=-'*30)
print('RANKING DOS JOGADORES')
ranking = []
ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True) # Ordena os valores de uma tupla
for i,v in enumerate (ranking):
    print(f'{i+1}º Lugar foi o {v[0]} com {v[1]} ')
    sleep(1)
