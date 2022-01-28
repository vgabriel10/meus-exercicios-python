"""
 Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
 retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""
def voto(nascimento):
    import datetime
    ano_Atual = datetime.date.today().year
    idade = ano_Atual - nascimento
    if idade > 65 or idade < 18 and idade >= 16:
        opção_Voto = ('Voto Opcional')
    elif idade >= 18:
        opção_Voto = ('Voto Obrigatorio')
    else:
        opção_Voto = ('Voto Negado')
    return opção_Voto,idade


print('+-'*20)
ano_Nasc = int(input('Digite seu Ano de Nascimento: '))
result = voto(ano_Nasc)
print(f'Com {result[1]} Anos: {result[0]}')


