"""
 Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
  desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""

frase = str(input('Digite uma frase: ')).strip()
# Tirar os espaços
frase_sem_espaco = frase.split()
# Juntar a frase
frase_junta = ''.join(frase_sem_espaco)
# Inverter ao contrario
frase_invertida = ''
quant_letras = len(frase_junta)
for c in range(quant_letras,0, -1): # O (C) vai começar no final até chegar no 0
    print(frase_junta[c-1],end='')      # e vai printar cada letra da ultima até a primeira, assim ele inverte a frase
    ''' A ser Finalizado, 
    
    '''
    frase_invertida += c
print(frase_invertida)
# Descobrir se é palidromo ou não
