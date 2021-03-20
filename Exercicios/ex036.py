"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
 o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
  ou então o empréstimo será negado.
"""
casa = float(input('Qual o Valor da Casa ?'))
salario = float(input('Qual o seu Salário ?'))
anos = int(input('Em quantos Anos vai pagar a prestação'))
#calcular o valor das prestações lembrando que um ano tem 12 Meses
parcela = anos * 12
valor_parcela = casa / parcela
print(f'O valor da Prestação é de {valor_parcela:.2f} por mês')
#A prestação mensal não pode exceder 30% do salário
if valor_parcela <= salario * 30 / 100: #calculando 30% do salário
    print('Emprestimo Concedido')
else:
    print('Emprestimo Negado')
