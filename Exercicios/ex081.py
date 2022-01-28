"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista_Numero = []
while True:
    numero = int(input('Digite um Número: '))
    lista_Numero.append(numero)
    continuar = str(input('Quer Continuar [S/N] ? '))
    while not continuar in 'sSnN':
        print('Valor invalido, Digite Novamente')
        continuar = str(input('Quer Continuar [S/N] ? '))
    if continuar in 'nN':
        break
print(f'Foram digitados {len(lista_Numero)} Valores!')
lista_Numero.sort(reverse=True)
print(f'Valores na ordem Decrescente {lista_Numero}')
if 5 in lista_Numero:
    print('O valor 5 está na lista')
else:
    print('O valor 5 Não está na lista')
