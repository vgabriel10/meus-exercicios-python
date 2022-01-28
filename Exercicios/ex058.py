"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
  palpites foram necessários para vencer.
"""
from random import randint
n = randint(0,10)
print('Eai meu freguês, tá pronto pra levar uma pisa ?')
print('Tenta acertar o número que eu pensei entre 0 e 10 ')
palpite = -1000
tentativas = 0
while not n == palpite:
    palpite = int(input('Manda teu palpite ?'))
    tentativas += 1
    if palpite > n:
        print('Menos que isso...')
    elif palpite < n:
        print('Mais que isso...')
print('Aeee Parabéns você acertou')
if tentativas > 3:
    print(f'Mas também né meu fiii')
    print(f'se depois de {tentativas} Tentativas Não acertasse')
elif tentativas <= 3 and tentativas > 1:
    print('HEHEHE até que tu não é tão ruim nisso')
    print(f'Precisou apenas de {tentativas} tentativas para acertar ')
elif tentativas == 1:
    print('Tá lendo a minha mente é ?')



