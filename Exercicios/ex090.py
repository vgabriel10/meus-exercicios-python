"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

boletim = {}
boletim['nome'] = str(input('Digite o nome do Aluno: '))
boletim['media'] = float(input('Digite a media do Aluno: '))
if boletim['media'] >= 7:
    boletim['situacao'] = 'Aprovado'
elif boletim['media'] < 7 and boletim['media'] >= 4:
    boletim['situacao'] = 'Recuperação'
else:
    boletim['situacao'] = 'Reprovado'
for k, v in boletim.items():
    print(f'- {k} é {v}')

