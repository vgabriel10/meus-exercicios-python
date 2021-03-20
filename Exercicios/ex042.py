"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""
# Se essa formula tiver correta eles formam um Triângulo
# a < b + c and b < b + 3 and c < a + b:

a = float(input('Digite o primeiro segmento'))
b = float(input('Digite o segundo segmento'))
c = float(input('Digite o terceiro segmento'))
if a < b + c and b < b +3 and c < a + b:
    print('Os segmentos acima formam um  triângulo')
    if a == b and b == c:
        print('O Triângulo é EQUILÁTERO')
    elif a != b and a != c and b != c:
        print('O Triângulo é ESCALENO')
    #else:
        #print('O Triângulo é ISÓSCELES')
    elif a == b != c or a == c != b or c == b != a:
        print('O Triângulo é ISÓSCELES')
else:
    print('Os segmentos acima Não formam um triângulo')
