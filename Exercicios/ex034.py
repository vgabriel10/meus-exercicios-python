"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

s = float(input('Digite o seu salário'))
if s > 1250:
    nsal = s+(s * 10/100)
else:
    nsal = s+(s * 15/100)
print(f'Seu novo salario é de R${nsal:.2f}')
