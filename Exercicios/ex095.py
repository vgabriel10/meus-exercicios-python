dados_Jogador = {}
lista_Jogadores = []
cod = 0
while True:
    dados_Jogador['cod'] = cod
    cod += 1
    dados_Jogador['nome'] = str(input('Nome do Jogador: '))
    partida = int(input(f'Quantas partidas {dados_Jogador["nome"]} jogou ? '))
    gols_Partida = []
    total_Gols = 0
    for c in range(0,partida):
        gols_Partida.append(int(input(f'Quantos gol o {dados_Jogador["nome"]} fez na partida {c + 1}: ')))
        total_Gols += gols_Partida[c]
    dados_Jogador['gols'] = gols_Partida[:]
    dados_Jogador['total'] = total_Gols
    lista_Jogadores.append(dados_Jogador.copy())
    continuar = str(input('Quer Continuar [S/N] ? '))
    while continuar not in 'NnSs':
        print('Valor Invalido, Digite Novamente')
        continuar = str(input('Quer Continuar [S/N] ? '))[0]
    if continuar in 'nN':
        break
    print('=-' * 30)
print()
print('--'*30)
for k in dados_Jogador.keys():
    print(f'{k:5^}',end='           ')
print('')
print('--'*30)
for cont in range(0,len(lista_Jogadores)):
    print(f'{lista_Jogadores[cont]["cod"]:<4}{lista_Jogadores[cont]["nome"]:^20}    {lista_Jogadores[cont]["gols"]}{lista_Jogadores[cont]["total"]:^6}')
while True:
    print('__'*30)
    escolher_Jogador = int(input('Digite o codigo do jogador para ver os seus dados (999 para parar): '))
    if escolher_Jogador == 999:
        break
    while escolher_Jogador > len(lista_Jogadores) - 1 and escolher_Jogador != 999:
        print('__' * 30)
        print(f'ERRO, Não existe jogador com o codigo {escolher_Jogador}')
        escolher_Jogador = int(input('Digite o codigo do jogador para ver os seus dados (999 para parar): '))
    if escolher_Jogador == 999:
        break
    print(f'Levantamento do jogador {lista_Jogadores[escolher_Jogador]["nome"]}:')
    quant_Gols = 0
    for jogo in range(0,len(lista_Jogadores[escolher_Jogador]["gols"])):
        print(f'No jogo {jogo + 1} fez {lista_Jogadores[escolher_Jogador]["gols"][quant_Gols]} gols')
        quant_Gols += 1
print('=-'*30)
print('Programa Encerrado')
print('=-'*30)
