"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

dados_Pessoas = {}
lista_Geral = []
while True:
    dados_Pessoas['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo [M/F]: '))
    while sexo not in 'MmFf':
        print('Valor Invalido, Digite Novamente!')
        sexo = str(input('Sexo [M/F]: '))
    dados_Pessoas['sexo'] = sexo
    dados_Pessoas['idade'] = int(input('Idade: '))
    lista_Geral.append(dados_Pessoas.copy())
    continuar = str(input('Quer Continuar [S/N] ? '))
    while continuar not in 'sSnN':
        print('dados invalidos,Digite Novamente')
        continuar = str(input('Quer Continuar [S/N] ? '))
    if continuar in 'Nn':
        break
    print('=-'*30)
print('=-'*30)
print(f'Foram Cadastradas {len(lista_Geral)} Pessoas')
idade = 0
lista_Mulheres = []
for c in range(0,len(lista_Geral)):
    idade += lista_Geral[c]['idade']
    if lista_Geral[c]['sexo'] in 'Ff':
        lista_Mulheres.append(lista_Geral[c]['nome'])
media_Idade = idade / len(lista_Geral)
print('=-'*30)
print(f'A media de idade é de {media_Idade:.2f}')
print('=-'*30)
print(f'As mulheres cadastradas foram {lista_Mulheres}')
print('=-'*30)
print('Lista de pessoas que estão com a idade acima da media')
print('__'*30)
for c in range(0,len(lista_Geral)):
    if lista_Geral[c]['idade'] > media_Idade:
        print(f'Nome: {lista_Geral[c]["nome"]} ,sexo = {lista_Geral[c]["sexo"]}, idade = {lista_Geral[c]["idade"]}')
        print('**'*30)
