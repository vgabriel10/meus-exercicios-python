"""
 Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
  desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""

"""
frase = str(input('Digite uma frase: ')).strip()
# Tirar os espaços
frase_sem_espaco = frase.split()
# Juntar a frase
frase_junta = ''.join(frase_sem_espaco)
# Inverter ao contrario
quant_letras = len(frase_junta)
for c in range(quant_letras,0, -1): # O (C) vai começar no final até chegar no 0
    print(frase_junta[c-1],end='')      # e vai printar cada letra da ultima até a primeira, assim ele inverte a frase
# Descobrir se é palidromo ou não
if frase.split() == frase_junta[::-1]:
    print('\n''É palidrometro')
else:
    print('\n''Não é palidrometro')
"""
frase = str(input('Digite uma frase')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1,-1):
    inverso += junto[letra]
print(junto,inverso)
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palidromo')


