"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
 e fechados na ordem correta.
"""
expr = str(input('Digite a sua Expressão: '))
pilha = []
for simbolo in expr:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0: # Esse parenteses fechado ---- ) ---- não pode ser o primeiro
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é valida')
else:
    print('Sua expressão é invalida')


""" Minha solução, tá errada pois ela não percebe a ordem, exemplo: a expressão pode começar com ) ao inves de (
parenteses_Aberto = 0
parenteses_Fechado = 0
expressao = str(input('Digite uma Expressão: '))
for parenteses in expressao:
    if parenteses == '(':
        parenteses_Aberto += 1
    elif parenteses == ')':
        parenteses_Fechado += 1
if parenteses_Aberto == parenteses_Fechado:
    print('A expressão é Valida!')
else:
    print('A expressão é invalida')
"""