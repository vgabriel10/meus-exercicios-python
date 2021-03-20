"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
 do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
ano_atual = date.today().year
nasc = int(input('Em que Ano você nasceu ?'))
idade = ano_atual - nasc
print(f'Quem Nasceu em {nasc} tem {idade} Anos em {ano_atual}')
if idade < 18:
    print(f'Ainda falta {18 - idade} Anos para se alistar')
    print(f'Você vai se alistar em {nasc + 18}')
elif idade > 18:
    print(f'Seu Alistamento foi em {nasc + 18}')
    print(f'Você Já deveria ter se alistado à {idade - 18} Anos atrás')
elif idade == 18:
    print('Você tem que se Alistar IMEDIATAMENTE!')
