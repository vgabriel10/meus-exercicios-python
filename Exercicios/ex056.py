"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

idade_todos = 0
h_velho = 0
menos_de_20 = 0
nome_h_velho = ''
for p in range(1,5):
    print('='*20)
    print(f'{p}º Pessoa')
    print('=' * 20)
    nome = str(input('Digite o seu Nome '))
    idade = int(input('Digite a sua Idade '))
    sexo = str(input('Digite seu Sexo [M/F] ')).lower()
    idade_todos += idade
    if p == 1 and sexo == 'm':
        h_velho = idade
    if idade > h_velho:
        h_velho = idade
        nome_h_velho = nome
    elif sexo == 'f' and idade < 20:
        menos_de_20 += 1
print(f'A media de idade de todos é de {idade_todos/4}')
print(f'O homem mais velho é {nome_h_velho} com {h_velho} anos')
print('Ao todo', menos_de_20, ' mulher tem menos de 20 Anos')

# Falta só ajeitar o Homem mais velho pra terminar o programa