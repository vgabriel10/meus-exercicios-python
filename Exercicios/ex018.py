import math
angulo = int(input('Digite um número de um angúlo'))
cos = math.cos(math.radians(angulo)) #para calcular o cosseno o seno e a tangente tem que
seno = math.sin(math.radians(angulo)) #converter de graus para radianos
tang = math.tan(math.radians(angulo))
print('O valor do seno é {:.2f}, o do cosseno é {:.2f} e o da tangente é de {:.2f}'.format(seno,cos,tang))

#eu poderia importar apenas os modulos que eu iria utilizar dessa maneira

#from math import radians,sin,cos,tan

#dessa maneira eu iria economizar espaço pois não iria utilizar toda a biblioteca math

#e fazendo isso eu não precisaria mais refereciar a biblioteca utilizando o math.alguma coisa
#basta usar o modulo, ex: sin(seno), tan(tang)
