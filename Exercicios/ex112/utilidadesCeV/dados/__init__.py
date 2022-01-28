def leiaDinheiro(texto):
    while True:
        valor = input(texto).strip()
        if valor.isascii() or valor.isnumeric() == True:
            if ',' in valor:
                valor = valor.replace(',','.')
                valor = float(valor)
                return valor
            elif '.' in valor:
                valor = float(valor)
                return valor
            elif valor.isnumeric():
                valor = float(valor)
                return valor
            else:
                print(f'\033[0:31m ERRO: "{valor}" é um preço inválido \033[m')
        else:
            print(f'\033[0:31m ERRO: "{valor}" é um preço inválido \033[m')

