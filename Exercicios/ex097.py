"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva(‘Olá, Mundo!’) Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~
"""
def escreva(texto):
    quant_Caracter = len(texto) + 4
    print('~'*quant_Caracter)
    print(f'{texto.center(quant_Caracter)}')
    print('~'*quant_Caracter)


escreva('Gabriel')
escreva('Ceará')
escreva('Vitor Gabriel')
escreva('Vitor Gabriel Garcia Ribeiro Lindo')