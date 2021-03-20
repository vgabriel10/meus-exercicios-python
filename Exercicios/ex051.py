"""
 Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
 No final, mostre os 10 primeiros termos dessa progressão.
"""


p_termo = int(input('Digite o primeiro Termo'))
razao = int(input('Digite a Razão'))
decimo_termo = p_termo + (10 - 1) * razao     # Formula para saber qual vai ser o décimo termo
for p_termo in range(p_termo, decimo_termo + razao, razao):    #Colocando o inicio e o Fim para não ficar em loop infinito
    print(p_termo,'!',end=' ')
print('Acabou')


