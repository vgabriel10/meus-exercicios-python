"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dados


preço = dados.leiaDinheiro('Digite o Preço: R$')
moeda.resumo(preço)
