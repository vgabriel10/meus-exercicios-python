a = float(input('Qual é a altura da parede em metros ?'))
l = float(input('Qual é a largura da parede em metros ?'))
tinta = a*l
print(f'A dimensão da area da sua parede é de {tinta} m')
t= tinta/2
print('Para pintar essa parede será necessario {} litros de tinta'.format(t))
