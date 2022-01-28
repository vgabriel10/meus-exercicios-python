"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
"""

n = (int(input('Digite um Número ')),
int(input('Digite Outro Número ')),
int(input('Digite mais um Número ')))
print(f'Você Digitou {n}')
vezes9 = n.count(9)
print(f'O valor 9 apareceu {vezes9} vezes')
if 3 in n:
    print(f'O número 3 apareceu pela primeira vez na posição {n.index(3)+1}')
else:
    print('O valor 3 não foi digitado!')
for valor in n:
    if valor % 2 == 0:
        print('Os valores pares digitados foram', end=' ')
        print(valor,end= ' ')
    else:
        print('Não foram inseridos Valores Pares!')
        break

"""
Podemos Também usar a tupla dessa maneira
n = tuple(int(input('Digite um número')) for c in range(1,5))
"""
