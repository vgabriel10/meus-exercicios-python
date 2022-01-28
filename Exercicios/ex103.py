"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha
do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""
def ficha(n='',g=''):
    if n == '':
        n = ('< Desconhecido >')
    if g not in '1234567890':
        g = 0
    elif g == '':
        g = 0
    print(f'O jogador {n} fez {g} gols')


nome = str(input('Nome do Jogador: '))
gols = str(input('Gols: '))
ficha(nome,gols)
