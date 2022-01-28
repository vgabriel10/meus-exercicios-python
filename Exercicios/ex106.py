"""
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""
from time import sleep
def ajuda(r):
    print(f'\033[0:30:44m Acessando Manual do comando {r}\033[m')
    print('\033[7:40m')
    sleep(0.5)
    help(r)
    print('\033[m')


while True:
    print('\033[0:30:42m=='*20)
    print('Sistema de Ajuda PyHELP')
    print('=='*20)
    print('\033[m')
    resp = str(input('Função ou Biblioteca: ')).lower()
    if resp == 'fim':
        print('\033[1:41m*_* '*20)
        print('Ate Logo'.center(60))
        print('*_* ' * 20)
        print('\033[m')
        break
    ajuda(resp)
