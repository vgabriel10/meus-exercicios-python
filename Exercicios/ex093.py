"""
 Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
 e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
 será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

dados_Jogador = {}
dados_Jogador['nome'] = str(input('Nome do Jogador: '))
partida = int(input(f'Quantas partidas {dados_Jogador["nome"]} jogou ? '))
gols_Partida = []
total_Gols = 0
for c in range(0,partida):
    gols_Partida.append(int(input(f'Quantos gol o {dados_Jogador["nome"]} fez na partida {c + 1}: ')))
    total_Gols += gols_Partida[c]
dados_Jogador['gols'] = gols_Partida[:]
dados_Jogador['total'] = total_Gols
print('=-'*30)
print(dados_Jogador)
print('=-'*30)
for k,v in dados_Jogador.items():
    print(f'{k}: {v}')
print('=-'*30)
print(f'O jogador {dados_Jogador["nome"]} jogou {partida} partidas.')
for p,v in enumerate(gols_Partida):
    print(f'Na partida {p + 1} fez {v} Gols')
print(f'Foi um total de {dados_Jogador["total"]} gols ')