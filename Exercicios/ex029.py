""" Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
 mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

vel = int(input('Qual a velocidade atual do carro ?'))
if vel <= 80:
    print('')
else:
    multa = (vel - 80)*7
    print('Você ultrapassou o limite permitido de 80 km/h e sera multado')
    print(f'A sua multa foi de R$ {multa}')
print('Dirija com segurança!')

#Esse codigo poderia ser feito utilizando apenas o (   IF   )

