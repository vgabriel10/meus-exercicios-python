"""
Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
pessoas = []
lista_Pessoas = []
medir_Peso = []
maior = 0
menor = 0
while True:
    pessoas.append(str(input('Digite o Nome da Pessoa: ')))
    pessoas.append(float(input('Digite o Peso da Pessoa: ')))   # PESSOAS[1] É O PESO
    if len(lista_Pessoas) == 0:
        maior = pessoas[1]
        menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        elif pessoas[1] < menor:
            menor = pessoas[1]
    lista_Pessoas.append(pessoas[:])
    pessoas.clear()
    print('Pessoa Cadastrada com Sucesso!')
    continuar = str(input('Quer Continuar ? [S/N] '))
    while not continuar in 'SsNn':
        print('Dado Invalido, Digite Novamente!')
        continuar = str(input('Quer Continuar ? [S/N] '))
    if continuar in 'nN':
        break
print(f'Foram cadastradas {len(lista_Pessoas)} Pessoas !')
print(f'O maior peso foi de {maior} Kg',end=' ')
for nome0_Peso1 in lista_Pessoas:
    if nome0_Peso1[1] == maior:
        print(nome0_Peso1[0],',')
print(f'O menor peso foi de {menor} Kg',end=' ')
for nome0_Peso1 in lista_Pessoas:
    if nome0_Peso1[1] == menor:
        print(nome0_Peso1[0],',')
