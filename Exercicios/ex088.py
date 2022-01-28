"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep
print('='*40)
print('Sorteio Mega Sena')
print('='*40)
lista_Sorteio = []
quant = int(input('Quantos Jogos quer que eu sorteie ? '))
for cont in range(0,quant):
    for c in range(0,6):
        numero = randint(1,60)
        while not numero in lista_Sorteio:
            if len(lista_Sorteio) < 6:
                lista_Sorteio.append(numero)
            else:
                break
    lista_Sorteio.sort()
    print(lista_Sorteio)
    sleep(1)
    lista_Sorteio.clear()
print('Boa Sorte!')