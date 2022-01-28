"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
maior_de_idade = 0
menor_de_idade = 0
ano_atual = date.today().year
print(ano_atual)
for c in range(1,8):
    nascimento = int(input(f'Em que ano a {c}º nasceu ? '))
    idade = ano_atual - nascimento
    if idade >= 18:
        maior_de_idade += 1
    else:
        menor_de_idade += 1
print(f'Temos {maior_de_idade} pessoas maior de idade')
print(f'Temos {menor_de_idade} pessoas menor de idade')

