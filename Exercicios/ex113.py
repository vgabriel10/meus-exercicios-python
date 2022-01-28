"""
 Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
 de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""

def leiaInt(texto):
    while True:
        numero = input(texto)
        try:
            numero = int(numero)
        except:
            print('\033[31m ERRO, DIGITE UM NÚMERO INTEIRO VALIDO \033[m')
        else:
            return numero


def leiaFloat(texto):
   while True:
       numero = input(texto)
       try:
           numero = float(numero)
       except(TypeError,ValueError):
           print('\033[31m ERRO, DIGITE UM NÚMERO REAL VALIDO \033[m')
       except KeyboardInterrupt:
           print('\033[31m O USUARIO PREFIRIU NÃO DIGITAR ESSE NÚMERO \033[m')
           return 0
       else:
           return numero


numeroInt = leiaInt('Digite um Número Inteiro: ')
numeroReal = leiaFloat('Digite um Número Real: ')
print(f'O valor Inteiro digitado foi {numeroInt} e o valor Real foi {numeroReal}')

