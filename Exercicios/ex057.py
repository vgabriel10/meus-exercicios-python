"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
 Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input('Digite o seu Sexo [M/F] ')).strip().lower()[0]
while sexo != 'm' and sexo != 'f':
    sexo = str(input('Dados inválidos, por favor insira seu Sexo Novamente ')).strip().lower()[0]
print(f'Sexo {sexo} registrado com sucesso')

