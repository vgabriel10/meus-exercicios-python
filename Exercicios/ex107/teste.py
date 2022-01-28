import moeda

preço = float(input('Digite o preço: '))
print(f'O dobro de {preço} é {moeda.dobro(preço)}')
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'Aumentamos 10%, temos {moeda.aumentar(preço,10)}')