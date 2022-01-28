"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
 mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
n = int(input('Digite um número '))
resp = ' '
lista = [n]
while not resp == 'n':
    resp = str(input('Quer Continuar [S/N] ?')).strip().lower()[0]
    if resp != 's' and resp != 'n':
        print('Opção invalida, Digite Novamente ')
    elif resp == 'n':
        pass
    elif resp == 's':
        n = int(input('Digite um número '))
        lista += [n]
        soma_valores = sum(lista)
        quant_valores = len(lista)
        media = soma_valores / quant_valores
        maior = max(lista)
        menor = min(lista)
print(lista)
print(f'A media de Todos os valores foi de {media:.2f}')
print(f'O maior Valor foi {maior}')
print(f'O menor Valor foi {menor}')
print('Fim do Programa')

