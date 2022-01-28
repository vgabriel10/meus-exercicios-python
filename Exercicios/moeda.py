def metade(n=0):
    result = n / 2
    return result

def dobro(n=0):
    result = n * 2
    return result


def aumentar(valor=0,porcen=0):
    result = valor + (valor * porcen) / 100
    return result


def diminuir(valor=0,porcen=0):
    result = valor - (valor * porcen) / 100
    return result


def moeda(preço=0,moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')
