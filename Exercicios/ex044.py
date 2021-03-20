"""
Elabore um programa que calcule o valor a ser pago por um produto,
 considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
"""

#vp = valor a pagar
valor_compras = float(input('Preços das Compras'))
print('Formas de Pagamento')
formas = int(input('''
[1] à vista dinheiro/cheque: 10% de desconto

[2] à vista no cartão: 5% de desconto

[3] em até 2x no cartão: preço formal

[4] 3x ou mais no cartão: 20% de juros'''))
if formas == 1:
    valor_final = valor_compras - ((valor_compras * 10)/100)
    print(f'O Valor total ficou R${valor_final:.2f}')
elif formas == 2:
    valor_final = valor_compras - ((valor_compras * 5)/100)
    print(f'O Valor total ficou R${valor_final:.2f}')
elif formas == 3:
    parcela = int(input('Digite a quantidade de parcelas'))
    valor_parcelado = valor_compras / parcela
    print(f'O valor Parcelado foi de R${valor_parcelado} Sem Juros')
    print(f'O Valor total ficou R${valor_compras:.2f}')
elif formas == 4:
    parcelas = int(input('Em quantas Parcelas ?'))
    valor_final = valor_compras + ((valor_compras*20)/100)
    valor_parcelado = valor_final / parcelas
    print(f'Vai ficar R${valor_parcelado} em {parcelas} Parcelas com Juros de 20% ')
    print(f'O valor Total com vai ficar R${valor_final:.2f}')
else:
    print('Opção invalida, digite uma jogador de 1 à 4')