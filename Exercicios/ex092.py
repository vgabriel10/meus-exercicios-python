"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = int(input('Digite o ano de nascimento: '))
idade = date.today().year - pessoa['idade']
pessoa['idade'] = idade
pessoa['CTPS'] = int(input('Numero da carteira de trabalho (0 Não tem): '))
if pessoa['CTPS'] > 0:
    pessoa['ano de contratação'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = idade + pessoa['ano de contratação'] + 35 - date.today().year
print('='*50)
print('-'*50)
for k,v in pessoa.items():
    print(f'{k}: {v}')
