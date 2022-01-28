def metade(valor=0,formatação=False):
    """
    -> Metade do valor
    :param valor: número que vai ser recebido
    :param formatação: se for True vai trazer o valor formatado
    :return: Retorna a metade do valor
    """
    result = valor / 2
    if formatação == True:
        result = moeda(valor=result)
    return result


def dobro(valor=0,formatação=False):
    """
    -> Dobro do valor
    :param valor: número que vai ser recebido
    :param formatação: se for True vai trazer o valor formatado
    :return: Retorna o dobro do valor
    """
    result = valor * 2
    if formatação == True:
        result = moeda(valor=result)
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
        result = moeda(valor=result)
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
        result = moeda(valor=result)
    return result


def moeda(valor=0.0,moeda='R$'):
    """
    -> Formata o valor da moeda
    :param valor: número recebido
    :param moeda: moeda a ser formatada
    :return: Retorna o número formatado

    """
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor,taxa_Aumento=5,taxa_Redução=5):
    valor_Format = moeda(valor)
    valor_Dobro = dobro(valor,True)
    valor_Metade = metade(valor,True)
    valor_Aumento = aumentar(valor,taxa_Aumento,True)
    valor_Redução = diminuir(valor,taxa_Redução,True)
    tamanho = 50
    print('-'*tamanho)
    print('Resumo do Valor'.center(50))
    print('-'*tamanho)
    print(f'Preço Analizado: \t\t{valor_Format}')
    print(f'Dobro do Preço: \t\t{valor_Dobro}')
    print(f'Metade do Preço: \t\t{valor_Metade}')
    print(f'{taxa_Aumento}% de Aumento: \t\t{valor_Aumento}')
    print(f'{taxa_Redução}% de Redução: \t\t{valor_Redução}')


