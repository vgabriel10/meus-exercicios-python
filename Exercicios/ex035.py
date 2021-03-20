"""Desenvolva um programa que leia o comprimento de três retas
 e diga ao usuário se elas podem ou não formar um triângulo. """

""" formula
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
"""
# Jeito que o guanabara fez
print('=-'*30)
print('Analisando triangulos')
print('=-'*30)
a = float(input('Digite o primeiro segmento'))
b = float(input('Digite o segundo segmento'))
c = float(input('Digite o terceiro segmento'))
if a < b + c and b < b + 3 and c < a + b:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo!')


""" eu fiz dessa maneira, porém podemos deixar o codigo mais enxuto

print('=-'*30)
print('Analisando triangulos')
print('=-'*30)
a = float(input('Digite o primeiro segmento'))
b = float(input('Digite o segundo segmento'))
c = float(input('Digite o terceiro segmento'))
result = 0
if (b - c) < a < b + c:
    result += 1
if (a - c) < a < b + c:
    result += 1
if (a - b) < c < a + b:
    result += 1
if result == 3:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo!')
"""

