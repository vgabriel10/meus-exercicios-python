"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

lista_valores = []
while True:
    valor_digitado = int(input('Digite um Valor ! '))
    while valor_digitado in lista_valores:
        print('Valor Duplicado, Digite Novamente !')
        valor_digitado = int(input('Digite um Valor ! '))
    if valor_digitado not in lista_valores:
        lista_valores.append(valor_digitado)
        print('O valor foi Adicionado Com Sucesso!')
    continuar = str(input('Quer Continuar [S]/[N] ?')).lower()
    if continuar == 'n':
        break
print(sorted(lista_valores))



