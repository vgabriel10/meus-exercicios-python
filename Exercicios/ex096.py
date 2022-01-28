def calcular_Área(a,b):
    área = a * b
    print(f'A área do terreno é de {área:.1f}m²')


print('Controle de Terrenos')
print('--'*20)
largura = float(input('Qual a largura do Terreno (m): '))
comprimento = float(input('Qual o comprimento do terreno (m): '))
calcular_Área(largura,comprimento)
