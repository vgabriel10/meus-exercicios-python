""" Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez."""

f = str(input('Digite uma frase')).lower().strip()
print('A letra A apareceu {} vezes na frase'.format(f.count('a'))) #count => quantas vezes a letra aparece
print('Ela aparece pela primeira vez na posição {}'.format(f.find('a')+1)) #find => A posição em que a letra aparece pela primeira vez.
                                                                           #OBS: começa contando do 0 por isso o + 1

print('A letra A apareceu na ultima vez na posição {}'.format(f.rfind('a')+1)) #rfind => R de right => direita, ele procura a ultima posição do A
                                                                               #contando da direita para a esquerda

