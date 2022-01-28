"""
 Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
 separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
lista_Numeros = [[],[]]

cont = 0
for c in range(0,7):
    cont += 1
    numero = int(input(f'Digite o {cont}º Valor: '))
    if numero % 2 == 0:
        lista_Numeros[0].append(numero)
    else:
        lista_Numeros[1].append(numero)
lista_Numeros[0].sort()
lista_Numeros[1].sort()
print(f'Os valores pares foram {lista_Numeros[0]}')
print(f'Os valores impares foram {lista_Numeros[1]}')