"""
 Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
  mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
print('-='*20)
print('Par ou Impar')
print('-='*20)
venceu = 0
while True:
    # Escolha do Usuario
    valor_usu = int(input('Digite um valor de 0 até 10 '))
    opção_usu = str(input('Par ou Impar [P/I] ')).strip().upper()[0]
    while opção_usu not in 'PpIi':
        print('Opção Invalida, digite novamente')
        opção_usu = str(input('Par ou Impar [P/I] ')).strip().upper()[0]
    print('-=' * 20)
    # Escolha do PC
    valor_pc = randint(0,10)
    opção_PC = ''
    if opção_usu == 'P':
        opção_PC = 'I'
        nome_opc = 'Impar'
    elif opção_usu == 'I':
        opção_PC = 'P'
        nome_opc = 'Par'
    print(f'O computador escolheu {valor_pc} e ficou com a opção {nome_opc}')
    # Fazendo o calculo para saber quem ganhou
    valor_tot = valor_usu + valor_pc
    result = ''
    if valor_tot % 2 == 0:
        result = 'P'
    else:
        result = 'I'
    # Vendo quem escolheu a opção certa
    if result == opção_usu:
        print('Parabéns, Você Venceu')
        print('¨'*50)
        venceu += 1
    elif result == opção_PC:
        print('Você Perdeu, mais sorte na próxima !!!')
        print('¨' * 50)
        break
print(f'Game Over, você venceu {venceu} vezes')




