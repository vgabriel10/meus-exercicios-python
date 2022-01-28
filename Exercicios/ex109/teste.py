"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
from ex109 import moeda


preço = float(input('Digite o preço: '))
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço,True)}')
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço,True)}')
print(f'Aumentamos 10%, temos {moeda.aumentar(preço,10,True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preço,13,True)}')