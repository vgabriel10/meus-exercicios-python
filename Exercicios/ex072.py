"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
numero = int(input('Digite um número entre 0 e 20 '))
while numero > 20 or numero < 0:
    print('Opção invalida!, Digite Novamente')
    numero = int(input('Digite um número entre 0 e 20 '))
nome = ('zero','um', 'dois','Três','Quatro','Cinco',
        'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
        'Doze', 'Treze','Quatorze','Quinze','Dezesseis',
        'Dezessete','Dezoito','Dezenove','Vinte')

print(f'Você digitou o número {nome[numero]}')