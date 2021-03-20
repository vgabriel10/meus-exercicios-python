"""
: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""
from datetime import date
ano_atual = date.today().year   #today = Hoje, Year = Ano
ano_nasc = int(input('Digite o seu ano de nascimento'))
idade = ano_atual - ano_nasc
print(f'Você vai ter {idade} em {ano_atual}')
if idade <= 9:
    print('Sua Categoria é Mirim')
elif idade <= 14:
    print('Sua Categoria é Infantil')
elif idade <= 19:
    print('Sua Categoria é Júnior')
elif idade <= 25:
    print('Sua Categoria é Sênior ')
elif idade > 25:
    print('Sua Categoria é Master')

