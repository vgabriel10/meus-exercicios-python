"""
tabuada 3.0
faça a tabuada de um número ate o usuario digitar ele negativo
"""

while True:
    n = int(input('Quer ver a tabuada de que número ? '))
    if n < 0:
        break
    for c in range(1,11):
        print(n, ' x ', c, '= ', n * c)
print('Fim do programa')


# Minha Solução foi essa, porém a primeira é melhor
"""
n = 0
c = 1
n = int(input('Quer ver a tabuada de que número ? '))
while c < 12:
    if c == 11:
        n = int(input('Quer ver a tabuada de que número ? '))
        c = 1
    if n < 0:
        break
    print(n,' x ',c , '= ',n*c)
    c += 1

print('fim')
"""