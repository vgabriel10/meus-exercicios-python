"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""
from datetime import date
ano = int(input('Digite um ano ? ou coloque 0 para analisar o Ano Atual'))
if ano == 0:
    ano = date.today().year #esse comando é para pegar o ano atual do computador
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print(f'O ano {ano} é Bissexto')
else:
    print(f'O Ano {ano} Não é bissexto')

"""Esse Sinal != Significa diferente"""


