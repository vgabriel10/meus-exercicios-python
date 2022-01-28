"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""
print('=-'*25)
print('Mercadinho')
print('=-'*25)
valor_tot = 0
MaisDeMil = 0
MaisBarato = 0
nome_Barato = ' '
c = 0
while True:
    produto = str(input('Digite o Nome do Produto ? '))
    preço = float(input('Digite o Preço do Produto ? '))
    while preço < 0:
        print('Valor invalido, Por Favor Digite Novamente')
        preço = float(input('Digite o Preço do Produto ? '))
    # PREÇO TOTAL
    valor_tot += preço
    # MAIS DE 1000 R$
    if preço > 1000:
        MaisDeMil += 1
    # MAIS BARATO
    c += 1
    if c == 1:
        MaisBarato = preço
    else:
        MaisBarato = preço
        nome_Barato = produto
    continuar = str(input('Quer Continuar [S/N] ?')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção invalida, Digite Novamente ')
        continuar = str(input('Quer Continuar [S/N] ?')).strip().upper()[0]
    # SAINDO DO LOOP
    if continuar == 'N':
        break
print(f'O total gasto nas compras foi de {valor_tot} Reais')
print(f'Temos {MaisDeMil} produto com preço superior a 1000 R$')
print(f'O produto mais barato foi a {nome_Barato} com o preço de {preço}')






