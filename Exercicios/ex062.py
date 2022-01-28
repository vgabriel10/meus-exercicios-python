"""
 Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
  O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
termo = int(input('Digite o primeiro Termo: '))
razão = int(input('Digite a razão: '))
c = 0
quant_termos = 10
while not c == quant_termos:
    print(termo, '!', end=' ')
    c += 1
    if c == quant_termos:
        quant_termos += int(input('\n Quantos termos você quer mostrar a mais ?, Digite [0] para terminar'))
    termo += razão
print(f'Foram Solicitados {quant_termos} Termos!!!')
print('Fim do Programa')

#Programa não finalizado, a parte de perguntar se quer continuar não tá em loop