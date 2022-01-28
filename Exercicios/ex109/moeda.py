def metade(n=0,formatação=False):
    """
    -> Metade do valor
    :param n: número que vai ser recebido
    :param formatação: se for True vai trazer o valor formatado
    :return: Retorna a metade do valor
    """
    result = n / 2
    if formatação == True:
        result = moeda(preço=result)
    return result


def dobro(n=0,formatação=False):
    """
    -> Dobro do valor
    :param n: número que vai ser recebido
    :param formatação: se for True vai trazer o valor formatado
    :return: Retorna o dobro do valor
    """
    result = n * 2
    if formatação == True:
        result = moeda(preço=result)
    return result


def aumentar(valor=0,porcen=0,formatação=False):
    """
    -> Aumenta o valor
    :param valor: número recebido
    :param porcen: porcentagem recebiada
    :param formatação: se for True vai trazer o valor formatado
    :return: Retorna a porcentagem do valor a mais
    """
    result = valor + (valor * porcen) / 100
    if formatação == True:
        result = moeda(preço=result)
    return result


def diminuir(valor=0,porcen=0,formatação=False):
    """

    :param valor: número recebido
    :param porcen: porcentagem recebiada
    :param formatação: se for True vai trazer o valor formatado
    :return: Retorna a porcentagem do valor a menos
    """
    result = valor - (valor * porcen) / 100
    if formatação == True:
        result = moeda(preço=result)
    return result


def moeda(preço=0.0,moeda='R$'):
    """
    -> Formata o valor da moeda
    :param preço: número recebido
    :param moeda: moeda a ser formatada
    :return: Retorna o número formatado

    """
    return f'{moeda}{preço:.2f}'.replace('.',',')


