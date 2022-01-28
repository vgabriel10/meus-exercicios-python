"""
 Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota
 – A média da turma
– A situação (opcional)
"""
def notas(*n,sit=False):
    """
    -> Armazena as notas dos alunos em um dicionario

    :param n: são as notas que serão recebidas
    :param sit: É a situação do aluno, ele vem por padrão com False
    :return: Retorna um Dicionario com os dados do aluno
    """
    media = (sum(n))/len(n)
    notas_Alunos = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': media}
    if sit == True:
        if media >= 9:
            situação = ('Ótimo')
            notas_Alunos["situação"] = situação
        elif media >= 7:
            situação = ('Boa')
            notas_Alunos["situação"] = situação
        elif media >= 6:
            situação = ('Razoavel')
            notas_Alunos["situação"] = situação
        elif media < 6:
            situação = ('Ruim')
            notas_Alunos["situação"] = situação
    return notas_Alunos


resp = notas(10,5,2,3,2,sit=True)
print(resp)
help(notas)
