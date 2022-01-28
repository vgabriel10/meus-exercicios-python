"""
 Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ('aprender','bola','maria','playstation','xbox')

for p in palavras:
    print(f'\n Na palavra {p} Temos ',end=' ')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras,end=' ')