"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

lista = []
boletim = []
notas_Individuais = []
while True:
    lista.append(str(input('Digite o Nome do Alunoª: ')))
    lista.append(float(input('Digite a primeira Nota: ')))
    lista.append(float(input('Digite a segunda Nota: ')))
    media = (lista[1] + lista[2]) / 2
    lista.append(media)
    boletim.append(lista[:])
    lista.clear()
    continuar = str(input('Quer Continuar [S/N] ? '))
    while continuar not in 'SsNn':
        print('Valor Invalido, Digite Novamente! ')
        continuar = str(input('Quer Continuar [S/N] ? '))
    if continuar in 'nN':
        break
print('='*60)
print('N     Nome          Media')
for i,aluno in enumerate(boletim):
    print(i,f'   {aluno[0]:^10}     {aluno[3]:^5}')
escolher_Aluno = int(input('Escolher a Nota de que Aluno ? (Digite o número do Aluno ou 999 para interromper): '))
while True:
    for i,aluno in enumerate(boletim):
        if escolher_Aluno != i:
            print('Valor invalido,Digite Novamente!')
            print('=-' * 40)
            escolher_Aluno = int(input('Escolher a Nota de que Aluno ? (Digite o número do Aluno ou 999 para interromper): '))
        if escolher_Aluno == i:
            print(f'A nota do Aluno {aluno[0]} é {aluno[1]} e {aluno[2]}')
            print('=-'*40)
            escolher_Aluno = int(input('Escolher a Nota de que Aluno ? (Digite o número do Aluno ou 999 para interromper): '))
        elif escolher_Aluno == 999:
            break

