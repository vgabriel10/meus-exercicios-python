#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
# o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Quantos dias o carro foi alugado ?'))
km = float(input('Quantos KM o veiculo percorreu ?'))
d = 60
kmrodados = 0.15
valor = (d * dias) + (km * kmrodados)
print(f'O valor que você tera que pagar é de: {valor:.2f}')
