from random import shuffle
a1 = str(input('Digite o nome do aluno'))
a2 = str(input('Digite o nome do aluno'))
a3 = str(input('Digite o nome do aluno'))
a4 = str(input('Digite o nome do aluno'))
lista = [a1,a2,a3,a4]
shuffle(lista)
print(lista)
#ou

#import random
print('x'*20)
print('')
print('Sorteio de ordens')
print('')
print('x'*20)
a1 = str(input('Digite o nome do aluno'))
a2 = str(input('Digite o nome do aluno'))
a3 = str(input('Digite o nome do aluno'))
a4 = str(input('Digite o nome do aluno'))
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print(lista)
