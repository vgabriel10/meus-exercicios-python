"""
 Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
 se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""
homens = 0
maior_18 = 0
mulh_men20 = 0
while True:
    print('-'*40)
    print('Cadastro de Pessoas')
    print('-'*40)
    idade = int(input('Digite a sua idade: '))
    # TRATAMENTO DE ERROS PARA VARIEAVEL SEXO
    sexo = str(input('Digite o seu Sexo: [M/F] ')).strip().lower()[0]
    while sexo not in 'mf':
        print('Opção invalida, Digite Novamente!')
        sexo = str(input('Digite o seu Sexo: [M/F] ')).strip().lower()[0]
    # CONTINUAR O LOOP OU NÃO
    continuar = str(input('Quer Continuar [S/N] ? ')).strip().lower()[0]
    while continuar not in 'sn':
        print('Opção Invalida, Digite Novamente!')
        continuar = str(input('Quer Continuar [S/N] ? ')).strip().lower()[0]
    if sexo == 'm':
        homens +=1
    if idade > 18:
        maior_18 += 1
    if sexo == 'f' and idade < 20:
        mulh_men20 += 1
    # CONDIÇÃO PARA ENCERRAR O LOOP
    if continuar == 'n':
        break
print('='*30)
print(f'Total de Pessoas com mais de 18 Anos é de {maior_18}')
print(f'Foram Cadastrados {homens} Homens')
print(f'Foram Cadastradas {mulh_men20} Mulheres com menos de 20 Anos')
print('='*50)






