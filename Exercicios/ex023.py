n = int(input('Digite um número de 0 á 9999'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
#Eu divido a parte inteira e tiro o modúlo para aparecer apenas um número
#Exemplo 1000 // 1 = 1000
print('Analisando o número')
print('A únidade é ',(u))
print('A dezena é', (d))
print('A centena é', (c))
print('A milhar é',(m))










