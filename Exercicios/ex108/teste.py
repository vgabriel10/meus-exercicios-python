import moeda

preço = float(input('Digite o preço: '))
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'Aumentamos 10%, temos {moeda.moeda(moeda.aumentar(preço,10))}')
