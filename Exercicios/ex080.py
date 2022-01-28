"""
 Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
 já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

lista_Valores = list()
for c in range(0,5):
    valor = int(input('Digite um Valor ! '))
    if c == 0 or valor > lista_Valores[-1]:
        lista_Valores.append(valor)
        print('Valor Adicionado na ultima posição!')
    else:
        posicao = 0
        while posicao < len(lista_Valores):         #Vai sempre Ler o ultimo valor da lista para saber se ele é menor ou igual ao valor atual
            if valor <= lista_Valores[posicao]:     # Posição começa no 0 e ao final recebe + 1
                lista_Valores.insert(posicao,valor)
                print(f'Valor Adicionado na posição {posicao}')
                break
            posicao += 1
print(lista_Valores)

