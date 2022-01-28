def metade(n):
    calculo = n / 2
    result = moeda(calculo)
    return result

def dobro(n):
    calculo = n * 2
    result = moeda(calculo)
    return result


def aumentar(valor,porcen):
    calculo = valor + (valor * porcen) / 100
    result = moeda(calculo)
    return result


def diminuir(valor,porcen):
    calculo = valor - (valor * porcen) / 100
    result = moeda(calculo)
    return result


def moeda(n):
    convertendo_Str = str(f'R${n:.2f}')
    result = convertendo_Str.replace('.',',')
    return result


